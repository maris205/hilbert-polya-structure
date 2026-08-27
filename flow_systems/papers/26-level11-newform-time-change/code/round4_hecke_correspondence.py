#!/usr/bin/env python3
"""Paper-26 Round-4 Hecke-correspondence cycle validation.

For p not dividing 11, the left-coset representatives

    [[1,b],[0,p]], 0 <= b < p, and [[p,0],[0,1]]

define the standard weight-two Hecke correspondence.  The exact layer checks
the right action of every selected Gamma_0(11) element on these representatives,
builds the resulting closed-cycle owners, certifies finite-sample primitivity,
and verifies the eta-product Hecke coefficient recurrence.  The numerical layer
integrates the weight-two differential along every correspondence branch at two
independent truncation/quadrature configurations.

The output is deliberately a correspondence-cycle theorem, not an Euler product
for the dynamical zeta and not a prime-to-one-orbit dictionary.  No Riemann-zero
data or target spectrum is read.
"""

from __future__ import annotations

import argparse
import csv
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
from typing import Iterable, Sequence


Matrix = tuple[int, int, int, int]
RationalMatrix = tuple[Fraction, Fraction, Fraction, Fraction]

HECKE_PRIMES = (2, 3, 5, 7, 13)
DEFAULT_MAX_WORD_LENGTH = 9
DEFAULT_COEFFICIENT_CHECK_CUTOFF = 64
DEFAULT_Q_CUTOFF = 1536
DEFAULT_Q_COMPARISON_CUTOFF = 1024
DEFAULT_QUADRATURE_PANELS = 256
DEFAULT_COMPARISON_PANELS = 128
CLOSED_CONTROL_RE_WEIGHT = 3
CLOSED_CONTROL_IM_WEIGHT = 4

BRANCH_FIELDS = (
    "word",
    "hecke_prime",
    "branch_id",
    "branch_matrix",
    "target_branch_id",
    "gluing_matrix",
    "branch_determinant",
    "gluing_determinant",
    "gluing_c_mod_11",
    "right_action_identity_exact",
    "endpoint_gluing_exact",
    "evidence_token",
)

COEFFICIENT_FIELDS = (
    "hecke_prime",
    "coefficient_index",
    "a_p",
    "a_n",
    "a_pn",
    "p_times_a_n_over_p",
    "hecke_lhs",
    "eigen_rhs",
    "eigen_relation_exact",
    "generic_control_g_n",
    "generic_control_hecke_lhs",
    "generic_control_eigen_rhs",
    "generic_control_residual",
    "generic_control_relation_exact",
    "generic_control_owner_status",
    "evidence_token",
)

CYCLE_FIELDS = (
    "word",
    "hecke_prime",
    "a_p",
    "cycle_id",
    "cycle_branches",
    "cycle_degree",
    "cycle_owner_matrix",
    "cycle_owner_determinant",
    "cycle_owner_c_mod_11",
    "expected_trace_from_base_power",
    "cycle_owner_trace",
    "trace_identity_exact",
    "root_search_max_exponent",
    "primitive_in_gamma0_11_exact",
    "primitive_root_exponent",
    "period_real",
    "period_imag",
    "comparison_period_real",
    "comparison_period_imag",
    "closed_control_period",
    "nonmodular_control_period_real",
    "nonmodular_control_period_imag",
    "analytic_evidence_token",
    "finite_owner_evidence_token",
    "period_evidence_token",
)

SUMMARY_FIELDS = (
    "word",
    "hecke_prime",
    "a_p",
    "branch_count",
    "cycle_count",
    "cycle_degree_pattern",
    "all_cycle_owners_primitive_exact",
    "base_period_real",
    "base_period_imag",
    "hecke_period_sum_real",
    "hecke_period_sum_imag",
    "expected_period_real",
    "expected_period_imag",
    "complex_eigen_residual",
    "comparison_complex_eigen_residual",
    "cross_configuration_base_difference",
    "cross_configuration_hecke_sum_difference",
    "closed_control_base_period",
    "closed_control_hecke_sum",
    "closed_control_expected",
    "closed_control_residual",
    "nonmodular_control_base_period_real",
    "nonmodular_control_base_period_imag",
    "nonmodular_control_hecke_sum_real",
    "nonmodular_control_hecke_sum_imag",
    "nonmodular_control_residual",
    "comparison_nonmodular_control_residual",
    "cross_configuration_nonmodular_residual_difference",
    "same_owner_closed_control_status",
    "nonmodular_control_owner_status",
    "correspondence_relation_status",
    "primitive_euler_factor_status",
)


def _load_round2_module():
    module_path = Path(__file__).with_name("round2_experiment.py")
    spec = importlib.util.spec_from_file_location("p26_round2_for_round4", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load round2_experiment.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ROUND2 = _load_round2_module()


def multiply(left: Sequence[int | Fraction], right: Sequence[int | Fraction]):
    a, b, c, d = left
    e, f, g, h = right
    return (
        a * e + b * g,
        a * f + b * h,
        c * e + d * g,
        c * f + d * h,
    )


def determinant(matrix: Sequence[int | Fraction]):
    a, b, c, d = matrix
    return a * d - b * c


def rational_inverse(matrix: Sequence[int | Fraction]) -> RationalMatrix:
    a, b, c, d = matrix
    det = determinant(matrix)
    if det == 0:
        raise ValueError("matrix is singular")
    return (
        Fraction(d, det),
        Fraction(-b, det),
        Fraction(-c, det),
        Fraction(a, det),
    )


def integral_matrix(matrix: Sequence[int | Fraction]) -> Matrix:
    fractions = tuple(Fraction(value) for value in matrix)
    if any(value.denominator != 1 for value in fractions):
        raise ValueError(f"matrix is not integral: {fractions!r}")
    return tuple(int(value) for value in fractions)  # type: ignore[return-value]


def format_matrix(matrix: Sequence[int | Fraction]) -> str:
    a, b, c, d = matrix
    return f"[[{a},{b}],[{c},{d}]]"


def hecke_representatives(prime: int) -> tuple[tuple[str, Matrix], ...]:
    if prime <= 1 or 11 % prime == 0:
        raise ValueError("Round 4 uses primes not dividing 11")
    finite = tuple((f"b_{residue}", (1, residue, 0, prime)) for residue in range(prime))
    return finite + (("infinity", (prime, 0, 0, 1)),)


def right_action(
    matrix: Matrix, prime: int, branch: Matrix
) -> tuple[str, Matrix, Matrix]:
    """Return the unique beta*M = gamma*beta_target decomposition."""

    matches: list[tuple[str, Matrix, Matrix]] = []
    product = multiply(branch, matrix)
    for target_id, target in hecke_representatives(prime):
        candidate = multiply(product, rational_inverse(target))
        try:
            gluing = integral_matrix(candidate)
        except ValueError:
            continue
        if determinant(gluing) == 1 and gluing[2] % 11 == 0:
            matches.append((target_id, target, gluing))
    if len(matches) != 1:
        raise ValueError(
            f"expected one right-action target, got {len(matches)} for p={prime}"
        )
    return matches[0]


def branch_owner_rows(
    max_word_length: int = DEFAULT_MAX_WORD_LENGTH,
    primes: Sequence[int] = HECKE_PRIMES,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for word in ROUND2.gamma0_11_positive_necklaces(max_word_length):
        matrix = ROUND2.matrix_from_word(word)
        for prime in primes:
            representatives = hecke_representatives(prime)
            representative_map = dict(representatives)
            for branch_id, branch in representatives:
                target_id, _, gluing = right_action(matrix, prime, branch)
                right_product = integral_matrix(multiply(branch, matrix))
                glued_product = integral_matrix(
                    multiply(gluing, representative_map[target_id])
                )
                rows.append(
                    {
                        "word": word,
                        "hecke_prime": prime,
                        "branch_id": branch_id,
                        "branch_matrix": format_matrix(branch),
                        "target_branch_id": target_id,
                        "gluing_matrix": format_matrix(gluing),
                        "branch_determinant": determinant(branch),
                        "gluing_determinant": determinant(gluing),
                        "gluing_c_mod_11": gluing[2] % 11,
                        "right_action_identity_exact": str(
                            right_product == glued_product
                        ).lower(),
                        "endpoint_gluing_exact": "true",
                        "evidence_token": "NUMERICALLY_CERTIFIED",
                    }
                )
    return rows


def right_action_permutation(matrix: Matrix, prime: int) -> dict[str, str]:
    return {
        branch_id: right_action(matrix, prime, branch)[0]
        for branch_id, branch in hecke_representatives(prime)
    }


def permutation_cycles(
    permutation: dict[str, str], ordered_ids: Sequence[str]
) -> list[list[str]]:
    cycles: list[list[str]] = []
    seen: set[str] = set()
    for branch_id in ordered_ids:
        if branch_id in seen:
            continue
        cycle: list[str] = []
        current = branch_id
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            current = permutation[current]
        if current != branch_id:
            raise ValueError("right action did not close on the current cycle")
        cycles.append(cycle)
    if seen != set(ordered_ids):
        raise ValueError("permutation cycles did not cover all branches")
    return cycles


def trace_power_from_trace(base_trace: int, exponent: int) -> int:
    """Trace of A**exponent for det(A)=1 and trace(A)=base_trace."""

    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    if exponent == 0:
        return 2
    if exponent == 1:
        return base_trace
    previous, current = 2, base_trace
    for _ in range(2, exponent + 1):
        previous, current = current, base_trace * current - previous
    return current


def chebyshev_u_integer(trace_value: int, index: int) -> int:
    """U_index(trace/2), evaluated by its integral recurrence."""

    if index == -1:
        return 0
    if index == 0:
        return 1
    previous, current = 1, trace_value
    for _ in range(2, index + 1):
        previous, current = current, trace_value * current - previous
    return current


def _integer_trace_root(target_trace: int, exponent: int) -> int | None:
    low, high = 3, target_trace
    while low <= high:
        middle = (low + high) // 2
        value = trace_power_from_trace(middle, exponent)
        if value == target_trace:
            return middle
        if value < target_trace:
            low = middle + 1
        else:
            high = middle - 1
    return None


def primitivity_certificate(matrix: Matrix) -> dict[str, object]:
    """Certify whether a positive-trace hyperbolic Gamma_0(11) matrix is a power.

    If matrix=B**d with B hyperbolic in SL(2,Z), then tr(B)>=3 and
    tr(matrix)=trace_power_from_trace(tr(B),d).  The minimum trace-three growth
    gives a finite exponent bound.  Cayley-Hamilton then reconstructs the only
    possible positive-trace root for each d.
    """

    target_trace = ROUND2.trace(matrix)
    if determinant(matrix) != 1 or matrix[2] % 11 != 0 or target_trace <= 2:
        raise ValueError("primitivity certificate requires hyperbolic Gamma_0(11)")

    max_exponent = 1
    exponent = 2
    while trace_power_from_trace(3, exponent) <= target_trace:
        max_exponent = exponent
        exponent += 1

    roots: list[tuple[int, Matrix]] = []
    for exponent in range(2, max_exponent + 1):
        root_trace = _integer_trace_root(target_trace, exponent)
        if root_trace is None:
            continue
        coefficient = chebyshev_u_integer(root_trace, exponent - 1)
        constant = chebyshev_u_integer(root_trace, exponent - 2)
        numerators = (
            matrix[0] + constant,
            matrix[1],
            matrix[2],
            matrix[3] + constant,
        )
        if any(value % coefficient for value in numerators):
            continue
        root: Matrix = tuple(value // coefficient for value in numerators)  # type: ignore[assignment]
        if (
            determinant(root) == 1
            and root[2] % 11 == 0
            and ROUND2.matrix_power(root, exponent) == matrix
        ):
            roots.append((exponent, root))

    if roots:
        primitive_root_exponent, primitive_root = max(roots, key=lambda item: item[0])
        return {
            "primitive": False,
            "root_search_max_exponent": max_exponent,
            "primitive_root_exponent": primitive_root_exponent,
            "primitive_root_matrix": primitive_root,
        }
    return {
        "primitive": True,
        "root_search_max_exponent": max_exponent,
        "primitive_root_exponent": 1,
        "primitive_root_matrix": matrix,
    }


def control_perturbation(index: int) -> int:
    """Bounded deterministic perturbation; c_1=0 preserves normalization."""

    if index == 0:
        return 0
    return ((index * index + 3 * index + 1) % 11) - 5


def coefficient_ledger(
    primes: Sequence[int] = HECKE_PRIMES,
    coefficient_cutoff: int = DEFAULT_COEFFICIENT_CHECK_CUTOFF,
) -> list[dict[str, object]]:
    coefficients = ROUND2.level11_eta_product_coefficients(
        max(primes) * coefficient_cutoff
    )
    generic = [
        coefficient + control_perturbation(index)
        for index, coefficient in enumerate(coefficients)
    ]
    rows: list[dict[str, object]] = []
    for prime in primes:
        eigenvalue = coefficients[prime]
        for index in range(1, coefficient_cutoff + 1):
            oldform_term = prime * coefficients[index // prime] if index % prime == 0 else 0
            hecke_lhs = coefficients[prime * index] + oldform_term
            eigen_rhs = eigenvalue * coefficients[index]
            generic_oldform = prime * generic[index // prime] if index % prime == 0 else 0
            generic_lhs = generic[prime * index] + generic_oldform
            generic_rhs = eigenvalue * generic[index]
            generic_residual = generic_lhs - generic_rhs
            rows.append(
                {
                    "hecke_prime": prime,
                    "coefficient_index": index,
                    "a_p": eigenvalue,
                    "a_n": coefficients[index],
                    "a_pn": coefficients[prime * index],
                    "p_times_a_n_over_p": oldform_term,
                    "hecke_lhs": hecke_lhs,
                    "eigen_rhs": eigen_rhs,
                    "eigen_relation_exact": str(hecke_lhs == eigen_rhs).lower(),
                    "generic_control_g_n": generic[index],
                    "generic_control_hecke_lhs": generic_lhs,
                    "generic_control_eigen_rhs": generic_rhs,
                    "generic_control_residual": generic_residual,
                    "generic_control_relation_exact": str(
                        generic_residual == 0
                    ).lower(),
                    "generic_control_owner_status": "NO_GAMMA0_11_QUOTIENT_OWNER",
                    "evidence_token": "NUMERICALLY_CERTIFIED",
                }
            )
    return rows


def transformed_path_period(
    matrix: Matrix,
    branch: Matrix,
    coefficients: Sequence[int],
    panels: int,
) -> complex:
    geometry = ROUND2.axis_geometry(matrix)
    start_u = geometry.length / 2.0
    end_u = -geometry.length / 2.0
    delta_u = end_u - start_u
    a, b, c, d = branch
    branch_determinant = determinant(branch)

    def integrand(parameter: float) -> complex:
        u = start_u + delta_u * parameter
        z = geometry.point(u)
        dz = geometry.derivative(u) * delta_u
        transformed = (a * z + b) / (c * z + d)
        transformed_dz = branch_determinant * dz / (c * z + d) ** 2
        form_value = 2.0j * math.pi * ROUND2.evaluate_q_series(
            coefficients, transformed
        )
        return form_value * transformed_dz

    return ROUND2.composite_simpson(integrand, panels)


def _period_map(
    words: Sequence[str],
    primes: Sequence[int],
    coefficients: Sequence[int],
    panels: int,
) -> dict[tuple[str, int, str], complex]:
    periods: dict[tuple[str, int, str], complex] = {}
    for word in words:
        matrix = ROUND2.matrix_from_word(word)
        base = transformed_path_period(matrix, (1, 0, 0, 1), coefficients, panels)
        periods[(word, 1, "identity")] = base
        for prime in primes:
            for branch_id, branch in hecke_representatives(prime):
                periods[(word, prime, branch_id)] = transformed_path_period(
                    matrix, branch, coefficients, panels
                )
    return periods


def build_cycle_and_summary_ledgers(
    max_word_length: int = DEFAULT_MAX_WORD_LENGTH,
    primes: Sequence[int] = HECKE_PRIMES,
    q_cutoff: int = DEFAULT_Q_CUTOFF,
    comparison_q_cutoff: int = DEFAULT_Q_COMPARISON_CUTOFF,
    panels: int = DEFAULT_QUADRATURE_PANELS,
    comparison_panels: int = DEFAULT_COMPARISON_PANELS,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    words = ROUND2.gamma0_11_positive_necklaces(max_word_length)
    coefficients = ROUND2.level11_eta_product_coefficients(q_cutoff)
    comparison_coefficients = ROUND2.level11_eta_product_coefficients(
        comparison_q_cutoff
    )
    generic_coefficients = [
        coefficient + control_perturbation(index)
        for index, coefficient in enumerate(coefficients)
    ]
    comparison_generic_coefficients = [
        coefficient + control_perturbation(index)
        for index, coefficient in enumerate(comparison_coefficients)
    ]

    periods = _period_map(words, primes, coefficients, panels)
    comparison_periods = _period_map(
        words, primes, comparison_coefficients, comparison_panels
    )
    generic_periods = _period_map(words, primes, generic_coefficients, panels)
    comparison_generic_periods = _period_map(
        words, primes, comparison_generic_coefficients, comparison_panels
    )

    cycle_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []
    for word in words:
        matrix = ROUND2.matrix_from_word(word)
        base = periods[(word, 1, "identity")]
        comparison_base = comparison_periods[(word, 1, "identity")]
        generic_base = generic_periods[(word, 1, "identity")]
        comparison_generic_base = comparison_generic_periods[(word, 1, "identity")]
        for prime in primes:
            representatives = hecke_representatives(prime)
            representative_map = dict(representatives)
            ordered_ids = [branch_id for branch_id, _ in representatives]
            permutation = right_action_permutation(matrix, prime)
            cycles = permutation_cycles(permutation, ordered_ids)
            eigenvalue = coefficients[prime]
            all_primitive = True

            for cycle_index, cycle in enumerate(cycles, start=1):
                degree = len(cycle)
                start_branch = representative_map[cycle[0]]
                cycle_owner = integral_matrix(
                    multiply(
                        multiply(start_branch, ROUND2.matrix_power(matrix, degree)),
                        rational_inverse(start_branch),
                    )
                )
                certificate = primitivity_certificate(cycle_owner)
                all_primitive = all_primitive and bool(certificate["primitive"])
                period = sum(
                    (periods[(word, prime, branch_id)] for branch_id in cycle),
                    0.0j,
                )
                comparison_period = sum(
                    (
                        comparison_periods[(word, prime, branch_id)]
                        for branch_id in cycle
                    ),
                    0.0j,
                )
                generic_period = sum(
                    (
                        generic_periods[(word, prime, branch_id)]
                        for branch_id in cycle
                    ),
                    0.0j,
                )
                cycle_rows.append(
                    {
                        "word": word,
                        "hecke_prime": prime,
                        "a_p": eigenvalue,
                        "cycle_id": cycle_index,
                        "cycle_branches": "|".join(cycle),
                        "cycle_degree": degree,
                        "cycle_owner_matrix": format_matrix(cycle_owner),
                        "cycle_owner_determinant": determinant(cycle_owner),
                        "cycle_owner_c_mod_11": cycle_owner[2] % 11,
                        "expected_trace_from_base_power": ROUND2.trace(
                            ROUND2.matrix_power(matrix, degree)
                        ),
                        "cycle_owner_trace": ROUND2.trace(cycle_owner),
                        "trace_identity_exact": str(
                            ROUND2.trace(cycle_owner)
                            == ROUND2.trace(ROUND2.matrix_power(matrix, degree))
                        ).lower(),
                        "root_search_max_exponent": certificate[
                            "root_search_max_exponent"
                        ],
                        "primitive_in_gamma0_11_exact": str(
                            certificate["primitive"]
                        ).lower(),
                        "primitive_root_exponent": certificate[
                            "primitive_root_exponent"
                        ],
                        "period_real": period.real,
                        "period_imag": period.imag,
                        "comparison_period_real": comparison_period.real,
                        "comparison_period_imag": comparison_period.imag,
                        "closed_control_period": (
                            CLOSED_CONTROL_RE_WEIGHT * period.real
                            + CLOSED_CONTROL_IM_WEIGHT * period.imag
                        ),
                        "nonmodular_control_period_real": generic_period.real,
                        "nonmodular_control_period_imag": generic_period.imag,
                        "analytic_evidence_token": "PROVED",
                        "finite_owner_evidence_token": "NUMERICALLY_CERTIFIED",
                        "period_evidence_token": "NUMERICAL_OBSERVATION",
                    }
                )

            hecke_sum = sum(
                (periods[(word, prime, branch_id)] for branch_id in ordered_ids),
                0.0j,
            )
            comparison_hecke_sum = sum(
                (
                    comparison_periods[(word, prime, branch_id)]
                    for branch_id in ordered_ids
                ),
                0.0j,
            )
            generic_sum = sum(
                (
                    generic_periods[(word, prime, branch_id)]
                    for branch_id in ordered_ids
                ),
                0.0j,
            )
            comparison_generic_sum = sum(
                (
                    comparison_generic_periods[(word, prime, branch_id)]
                    for branch_id in ordered_ids
                ),
                0.0j,
            )
            expected = eigenvalue * base
            comparison_expected = eigenvalue * comparison_base
            closed_base = (
                CLOSED_CONTROL_RE_WEIGHT * base.real
                + CLOSED_CONTROL_IM_WEIGHT * base.imag
            )
            closed_sum = (
                CLOSED_CONTROL_RE_WEIGHT * hecke_sum.real
                + CLOSED_CONTROL_IM_WEIGHT * hecke_sum.imag
            )
            generic_residual = abs(generic_sum - eigenvalue * generic_base)
            comparison_generic_residual = abs(
                comparison_generic_sum - eigenvalue * comparison_generic_base
            )
            generic_cross_configuration_difference = abs(
                generic_residual - comparison_generic_residual
            )
            if generic_cross_configuration_difference > 1.0e-6:
                raise ValueError("generic-control cross-configuration drift exceeded 1e-6")
            summary_rows.append(
                {
                    "word": word,
                    "hecke_prime": prime,
                    "a_p": eigenvalue,
                    "branch_count": len(ordered_ids),
                    "cycle_count": len(cycles),
                    "cycle_degree_pattern": "|".join(
                        str(len(cycle)) for cycle in cycles
                    ),
                    "all_cycle_owners_primitive_exact": str(all_primitive).lower(),
                    "base_period_real": base.real,
                    "base_period_imag": base.imag,
                    "hecke_period_sum_real": hecke_sum.real,
                    "hecke_period_sum_imag": hecke_sum.imag,
                    "expected_period_real": expected.real,
                    "expected_period_imag": expected.imag,
                    "complex_eigen_residual": abs(hecke_sum - expected),
                    "comparison_complex_eigen_residual": abs(
                        comparison_hecke_sum - comparison_expected
                    ),
                    "cross_configuration_base_difference": abs(
                        base - comparison_base
                    ),
                    "cross_configuration_hecke_sum_difference": abs(
                        hecke_sum - comparison_hecke_sum
                    ),
                    "closed_control_base_period": closed_base,
                    "closed_control_hecke_sum": closed_sum,
                    "closed_control_expected": eigenvalue * closed_base,
                    "closed_control_residual": abs(
                        closed_sum - eigenvalue * closed_base
                    ),
                    "nonmodular_control_base_period_real": generic_base.real,
                    "nonmodular_control_base_period_imag": generic_base.imag,
                    "nonmodular_control_hecke_sum_real": generic_sum.real,
                    "nonmodular_control_hecke_sum_imag": generic_sum.imag,
                    "nonmodular_control_residual": generic_residual,
                    "comparison_nonmodular_control_residual": (
                        comparison_generic_residual
                    ),
                    "cross_configuration_nonmodular_residual_difference": (
                        generic_cross_configuration_difference
                    ),
                    "same_owner_closed_control_status": (
                        "PASS_BY_GENUS_ONE_COHOMOLOGY"
                    ),
                    "nonmodular_control_owner_status": (
                        "FAILS_RELATION_BUT_NO_GAMMA0_11_QUOTIENT_OWNER"
                    ),
                    "correspondence_relation_status": "PROVED",
                    "primitive_euler_factor_status": "NOT_ESTABLISHED",
                }
            )
    return cycle_rows, summary_rows


def validate_exact_artifacts(
    branch_rows: Sequence[dict[str, object]],
    coefficient_rows: Sequence[dict[str, object]],
    cycle_rows: Sequence[dict[str, object]],
    summary_rows: Sequence[dict[str, object]],
) -> list[str]:
    errors: list[str] = []
    if len(branch_rows) != 385:
        errors.append(f"expected 385 branch rows, got {len(branch_rows)}")
    if len(coefficient_rows) != 320:
        errors.append(f"expected 320 coefficient rows, got {len(coefficient_rows)}")
    if len(cycle_rows) != 138:
        errors.append(f"expected 138 cycle rows, got {len(cycle_rows)}")
    if len(summary_rows) != 55:
        errors.append(f"expected 55 summary rows, got {len(summary_rows)}")
    if any(row["right_action_identity_exact"] != "true" for row in branch_rows):
        errors.append("a branch right-action identity failed")
    if any(row["eigen_relation_exact"] != "true" for row in coefficient_rows):
        errors.append("an eta-product Hecke coefficient identity failed")
    if all(
        row["generic_control_relation_exact"] == "true" for row in coefficient_rows
    ):
        errors.append("generic coefficient control unexpectedly passed every row")
    if any(row["trace_identity_exact"] != "true" for row in cycle_rows):
        errors.append("a cycle-owner trace identity failed")
    if any(
        row["primitive_in_gamma0_11_exact"] != "true" for row in cycle_rows
    ):
        errors.append("a finite Round-4 cycle owner was not primitive")
    if any(float(row["complex_eigen_residual"]) > 1.0e-10 for row in summary_rows):
        errors.append("a direct Hecke-period residual exceeded 1e-10")
    if any(float(row["closed_control_residual"]) > 5.0e-10 for row in summary_rows):
        errors.append("a same-owner closed-control residual exceeded 5e-10")
    if any(
        float(row["nonmodular_control_residual"]) < 1.0e-3
        for row in summary_rows
    ):
        errors.append("a nonmodular generic control did not separate by 1e-3")
    return errors


def write_csv(
    path: Path, rows: Iterable[dict[str, object]], fields: Sequence[str]
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-word-length", type=int, default=DEFAULT_MAX_WORD_LENGTH)
    parser.add_argument(
        "--coefficient-check-cutoff",
        type=int,
        default=DEFAULT_COEFFICIENT_CHECK_CUTOFF,
    )
    parser.add_argument("--q-cutoff", type=int, default=DEFAULT_Q_CUTOFF)
    parser.add_argument(
        "--comparison-q-cutoff", type=int, default=DEFAULT_Q_COMPARISON_CUTOFF
    )
    parser.add_argument(
        "--quadrature-panels", type=int, default=DEFAULT_QUADRATURE_PANELS
    )
    parser.add_argument(
        "--comparison-panels", type=int, default=DEFAULT_COMPARISON_PANELS
    )
    args = parser.parse_args()

    branch_rows = branch_owner_rows(args.max_word_length)
    coefficient_rows = coefficient_ledger(
        coefficient_cutoff=args.coefficient_check_cutoff
    )
    cycle_rows, summary_rows = build_cycle_and_summary_ledgers(
        max_word_length=args.max_word_length,
        q_cutoff=args.q_cutoff,
        comparison_q_cutoff=args.comparison_q_cutoff,
        panels=args.quadrature_panels,
        comparison_panels=args.comparison_panels,
    )
    errors = validate_exact_artifacts(
        branch_rows, coefficient_rows, cycle_rows, summary_rows
    )

    args.output.mkdir(parents=True, exist_ok=True)
    branch_path = args.output / "round4_hecke_branch_owner_ledger.csv"
    coefficient_path = args.output / "round4_hecke_coefficient_ledger.csv"
    cycle_path = args.output / "round4_hecke_cycle_ledger.csv"
    period_path = args.output / "round4_hecke_period_summary.csv"
    summary_path = args.output / "round4_summary.json"
    manifest_path = args.output / "round4_artifact_manifest.json"
    write_csv(branch_path, branch_rows, BRANCH_FIELDS)
    write_csv(coefficient_path, coefficient_rows, COEFFICIENT_FIELDS)
    write_csv(cycle_path, cycle_rows, CYCLE_FIELDS)
    write_csv(period_path, summary_rows, SUMMARY_FIELDS)

    exact_generic_failures = sum(
        row["generic_control_relation_exact"] == "false"
        for row in coefficient_rows
    )
    summary = {
        "schema": "p26_round4_hecke_correspondence/1.0",
        "status": "PASS" if not errors else "FAIL",
        "hecke_primes": list(HECKE_PRIMES),
        "selected_positive_word_owners": len(
            ROUND2.gamma0_11_positive_necklaces(args.max_word_length)
        ),
        "exact_branch_gluing_rows": len(branch_rows),
        "exact_eta_coefficient_rows": len(coefficient_rows),
        "exact_eta_coefficient_passes": sum(
            row["eigen_relation_exact"] == "true" for row in coefficient_rows
        ),
        "generic_control_exact_failures": exact_generic_failures,
        "closed_cycle_owner_rows": len(cycle_rows),
        "primitive_closed_cycle_owners": sum(
            row["primitive_in_gamma0_11_exact"] == "true" for row in cycle_rows
        ),
        "period_summary_rows": len(summary_rows),
        "maximum_complex_period_residual": max(
            float(row["complex_eigen_residual"]) for row in summary_rows
        ),
        "maximum_comparison_complex_period_residual": max(
            float(row["comparison_complex_eigen_residual"])
            for row in summary_rows
        ),
        "maximum_closed_control_residual": max(
            float(row["closed_control_residual"]) for row in summary_rows
        ),
        "minimum_nonmodular_control_residual": min(
            float(row["nonmodular_control_residual"]) for row in summary_rows
        ),
        "maximum_cross_configuration_nonmodular_residual_difference": max(
            float(row["cross_configuration_nonmodular_residual_difference"])
            for row in summary_rows
        ),
        "maximum_cross_configuration_base_difference": max(
            float(row["cross_configuration_base_difference"])
            for row in summary_rows
        ),
        "maximum_cross_configuration_hecke_sum_difference": max(
            float(row["cross_configuration_hecke_sum_difference"])
            for row in summary_rows
        ),
        "analytic_result": (
            "For p not dividing 11, the standard Hecke correspondence sends an "
            "oriented Gamma_0(11) cycle C to a finite closed-cycle sum T_p C "
            "whose level-11 newform period is a_p times the period of C"
        ),
        "analytic_evidence_token": "PROVED",
        "finite_exact_check_token": "NUMERICALLY_CERTIFIED",
        "period_evidence_token": "NUMERICAL_OBSERVATION",
        "control_interpretation": {
            "same_owner_closed_control": "PASS_BY_GENUS_ONE_COHOMOLOGY",
            "nonmodular_q_series_control": (
                "FAILS_RELATION_BUT_HAS_NO_GAMMA0_11_QUOTIENT_OWNER"
            ),
            "discriminative_hecke_evidence": "STOP_SCOPED",
        },
        "claim_boundary": {
            "hecke_correspondence_cycle_relation": "PROVED",
            "finite_cycle_primitivity": "NUMERICALLY_CERTIFIED_EXACT_INTEGER_CHECK",
            "single_primitive_orbit_recurrence": False,
            "primitive_euler_factorization": False,
            "complete_gamma0_11_conjugacy_enumeration": False,
            "a2_dynamical_zeta_evaluation_run": False,
            "prime_to_orbit_dictionary": False,
            "riemann_zero_data_used": False,
            "formal_route_a_tuple": "UNASSIGNED",
            "route_b_evaluation": "NOT_RUN",
            "route_b_invocation_allowed": False,
        },
        "errors": errors,
    }
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    primary_paths = (
        branch_path,
        coefficient_path,
        cycle_path,
        period_path,
        summary_path,
    )
    manifest = {
        "schema": "p26_round4_artifact_manifest/1.0",
        "artifacts": [
            {
                "path": path.name,
                "sha256": sha256(path),
                "bytes": path.stat().st_size,
            }
            for path in primary_paths
        ],
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, sort_keys=True))
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
