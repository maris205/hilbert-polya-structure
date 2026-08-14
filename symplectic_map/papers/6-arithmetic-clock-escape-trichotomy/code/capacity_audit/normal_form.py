"""Exact formal objects for canonical-readout closure and set semantics.

No function in this module evaluates a logarithm, constructs a prime, or
claims to prove a transcendence theorem.  The records instantiate only the
algebraic bookkeeping already proved in the proof package.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Iterable, Sequence


def _gcd(left: int, right: int) -> int:
    left = abs(left)
    right = abs(right)
    while right:
        left, right = right, left % right
    return left


def _lcm(left: int, right: int) -> int:
    if left <= 0 or right <= 0:
        raise ValueError("denominators must be positive")
    return left // _gcd(left, right) * right


def _formal_label(label: str) -> bool:
    """Require nonnumeric formal labels rather than embedded target values."""

    return bool(label) and not label.isdecimal()


@dataclass(frozen=True)
class MultiplierLogTerm:
    """One source-locked rational multiple of a formal positive modulus log."""

    modulus_label: str
    coefficient: Fraction
    positive_real_algebraic: bool
    square_is_s_unit: bool
    square_support: frozenset[str]


@dataclass(frozen=True)
class CanonicalReadout:
    """Formal certificate for one readout of the shape v + log(q) + alpha."""

    certificate_id: str
    v_coordinates: tuple[Fraction, ...]
    multiplier_terms: tuple[MultiplierLogTerm, ...]
    alpha_real_algebraic: bool
    target_independent: bool
    real_log_branch: bool


def audit_multiplier_closure(
    terms: Sequence[MultiplierLogTerm],
    *,
    declared_support: frozenset[str],
) -> dict[str, Any]:
    """Clear rational exponents and audit the squared-unit closure schema."""

    denominator = 1
    label_errors: list[str] = []
    support_errors: list[str] = []
    algebraic_errors: list[str] = []
    coefficient_errors: list[str] = []

    for term in terms:
        if not _formal_label(term.modulus_label):
            label_errors.append(term.modulus_label)
        if not isinstance(term.coefficient, Fraction):
            coefficient_errors.append(term.modulus_label)
            continue
        denominator = _lcm(denominator, term.coefficient.denominator)
        if not term.positive_real_algebraic or not term.square_is_s_unit:
            algebraic_errors.append(term.modulus_label)
        if not term.square_support.issubset(declared_support):
            support_errors.append(term.modulus_label)

    integer_exponents = [
        term.coefficient.numerator * (denominator // term.coefficient.denominator)
        for term in terms
        if isinstance(term.coefficient, Fraction)
    ]
    negative_powers_present = any(exponent < 0 for exponent in integer_exponents)
    rational_roots_required = denominator > 1
    passed = not label_errors and not support_errors and not algebraic_errors and not coefficient_errors
    return {
        "common_denominator": denominator,
        "integer_exponents_after_clearing": integer_exponents,
        "negative_powers_present": negative_powers_present,
        "negative_powers_use_unit_inversion": negative_powers_present,
        "rational_roots_required": rational_roots_required,
        "positive_root_finite_extension_required": rational_roots_required,
        "certified_object": "q_squared",
        "real_log_evaluated": False,
        "numeric_modulus_evaluated": False,
        "label_errors": label_errors,
        "coefficient_errors": coefficient_errors,
        "algebraic_or_unit_errors": algebraic_errors,
        "support_errors": support_errors,
        "pass": passed,
    }


def audit_canonical_readout(
    readout: CanonicalReadout,
    *,
    dimension: int,
    declared_support: frozenset[str],
) -> dict[str, Any]:
    """Audit one formal normal-form certificate without inspecting a target."""

    if dimension < 0:
        raise ValueError("dimension cannot be negative")
    coordinates_exact = (
        len(readout.v_coordinates) == dimension
        and all(isinstance(coordinate, Fraction) for coordinate in readout.v_coordinates)
    )
    multiplier = audit_multiplier_closure(
        readout.multiplier_terms,
        declared_support=declared_support,
    )
    passed = (
        _formal_label(readout.certificate_id)
        and coordinates_exact
        and readout.alpha_real_algebraic
        and readout.target_independent
        and readout.real_log_branch
        and multiplier["pass"]
    )
    return {
        "certificate_id": readout.certificate_id,
        "dimension": dimension,
        "coordinate_count": len(readout.v_coordinates),
        "coordinates_exact_rational": coordinates_exact,
        "alpha_real_algebraic": readout.alpha_real_algebraic,
        "target_independent": readout.target_independent,
        "real_log_branch": readout.real_log_branch,
        "multiplier_closure": multiplier,
        "target_value_inspected": False,
        "pass": passed,
    }


def select_one_certificate_per_distinct_hit(
    records: Iterable[tuple[str, str, bool]],
) -> dict[str, Any]:
    """Choose the first valid certificate per formal hit label.

    The theorem permits any choice.  First-valid selection is deterministic
    for auditing and never reads a numeric target value.
    """

    selected: dict[str, str] = {}
    total_records = 0
    invalid_labels: list[str] = []
    for hit_label, certificate_id, valid in records:
        total_records += 1
        if not _formal_label(hit_label) or not _formal_label(certificate_id):
            invalid_labels.append(hit_label)
            continue
        if valid and hit_label not in selected:
            selected[hit_label] = certificate_id
    repeated_records = total_records - len(selected)
    return {
        "selected": selected,
        "distinct_hit_count": len(selected),
        "input_record_count": total_records,
        "repeated_or_invalid_records_not_counted": repeated_records,
        "selection_rule": "first_valid_per_formal_label",
        "numeric_target_values_inspected": False,
        "invalid_labels": invalid_labels,
        "pass": not invalid_labels,
    }


def instantiate_outside_valuation_schema(
    relation: Sequence[tuple[str, int]],
) -> dict[str, Any]:
    """Instantiate the final exact valuation equation for formal labels.

    At a place over an outside prime label, the proof supplies the equation
    ``2*m*e=0`` with positive ramification index ``e``.  Setting ``e=1`` is a
    harmless exact representative for checking the coefficient implication;
    this function is a proof-schema control, not a prime computation.
    """

    labels = [label for label, _ in relation]
    unique_formal_labels = len(set(labels)) == len(labels) and all(_formal_label(label) for label in labels)
    coefficients_exact = all(isinstance(coefficient, int) for _, coefficient in relation)
    equations = [
        {
            "outside_label": label,
            "coefficient": coefficient,
            "twice_coefficient": 2 * coefficient,
            "valuation_equation_zero_holds": 2 * coefficient == 0,
            "coefficient_forced_zero": coefficient == 0,
        }
        for label, coefficient in relation
        if isinstance(coefficient, int)
    ]
    all_coefficients_zero = coefficients_exact and all(item["coefficient_forced_zero"] for item in equations)
    return {
        "labels": labels,
        "unique_formal_labels": unique_formal_labels,
        "coefficients_exact_integers": coefficients_exact,
        "equations": equations,
        "nonzero_relation_survives": unique_formal_labels and coefficients_exact and not all_coefficients_zero,
        "all_coefficients_zero": all_coefficients_zero,
        "prime_values_generated_or_tested": False,
        "pass": unique_formal_labels and coefficients_exact,
    }
