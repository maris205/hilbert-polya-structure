"""Independent exact evaluator for the Paper 37 source fixtures.

This module deliberately does not import ``source_core``.  It reimplements
word reduction, affine-group evaluation, and exact 2x2 matrix arithmetic.
All arithmetic is over integers or ``fractions.Fraction``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any


Matrix = tuple[int, int, int, int]
IDENTITY: Matrix = (1, 0, 0, 1)
ZERO: Matrix = (0, 0, 0, 0)
INVERSE = {"u": "U", "U": "u", "v": "V", "V": "v"}


@dataclass
class CheckBook:
    rows: list[dict[str, Any]] = field(default_factory=list)

    def check(self, name: str, condition: bool, detail: Any = None) -> None:
        row = {"name": name, "passed": bool(condition)}
        if detail is not None:
            row["detail"] = detail
        self.rows.append(row)
        if not condition:
            raise AssertionError(f"exact check failed: {name}: {detail!r}")

    def summary(self) -> dict[str, int]:
        passed = sum(1 for row in self.rows if row["passed"])
        return {"passed": passed, "total": len(self.rows)}


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    a, b, c, d = left
    e, f, g, h = right
    return (
        a * e + b * g,
        a * f + b * h,
        c * e + d * g,
        c * f + d * h,
    )


def matrix_trace(matrix: Matrix) -> int:
    return matrix[0] + matrix[3]


def matrix_determinant(matrix: Matrix) -> int:
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def matrix_inverse_sl2(matrix: Matrix) -> Matrix:
    if matrix_determinant(matrix) != 1:
        raise ValueError("the frozen connection expects SL(2,Z) matrices")
    a, b, c, d = matrix
    return (d, -b, -c, a)


def matrix_power(matrix: Matrix, exponent: int) -> Matrix:
    if exponent < 0:
        return matrix_power(matrix_inverse_sl2(matrix), -exponent)
    result = IDENTITY
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        power //= 2
    return result


def word_holonomy(word: str, connection: dict[str, list[int] | tuple[int, ...]]) -> Matrix:
    result = IDENTITY
    for letter in word:
        raw = connection[letter]
        matrix: Matrix = (int(raw[0]), int(raw[1]), int(raw[2]), int(raw[3]))
        result = matrix_multiply(result, matrix)
    return result


def factor_polynomial(matrix: Matrix) -> tuple[int, int, int]:
    """Coefficients of det(I-tM)=1-tr(M)t+det(M)t^2."""
    return (1, -matrix_trace(matrix), matrix_determinant(matrix))


def inverse_word(word: str) -> str:
    return "".join(INVERSE[letter] for letter in reversed(word))


def freely_reduce(word: str) -> str:
    stack: list[str] = []
    for letter in word:
        if stack and stack[-1] == INVERSE[letter]:
            stack.pop()
        else:
            stack.append(letter)
    return "".join(stack)


def cyclically_reduce(word: str) -> str:
    reduced = freely_reduce(word)
    while len(reduced) > 1 and reduced[0] == INVERSE[reduced[-1]]:
        reduced = freely_reduce(reduced[1:-1])
    return reduced


def is_cyclically_nonbacktracking(word: str) -> bool:
    if not word:
        return False
    for index, letter in enumerate(word):
        if word[(index + 1) % len(word)] == INVERSE[letter]:
            return False
    return True


def is_literal_primitive(word: str) -> bool:
    if not word:
        return False
    for period in range(1, len(word)):
        if len(word) % period == 0 and word == word[:period] * (len(word) // period):
            return False
    return True


def canonical_rotation(word: str) -> str:
    return min(word[index:] + word[:index] for index in range(len(word)))


def affine_multiply(left: tuple[Fraction, int], right: tuple[Fraction, int],
                    exponent: int) -> tuple[Fraction, int]:
    b, k = left
    d, ell = right
    return (b + Fraction(exponent) ** k * d, k + ell)


def affine_evaluate(word: str, exponent: int) -> tuple[Fraction, int]:
    generators = {
        "u": (Fraction(1), 0),
        "U": (Fraction(-1), 0),
        "v": (Fraction(0), 1),
        "V": (Fraction(0), -1),
    }
    value = (Fraction(0), 0)
    for letter in word:
        value = affine_multiply(value, generators[letter], exponent)
    return value


def supertrace(word: str, connection: dict[str, Any], power: int = 1) -> int:
    even = matrix_power(word_holonomy(word, connection["even"]), power)
    odd = matrix_power(word_holonomy(word, connection["odd"]), power)
    return matrix_trace(even) - matrix_trace(odd)


def direct_factor_row(relator: str, connection: dict[str, Any]) -> dict[str, Any]:
    even = word_holonomy(relator, connection["even"])
    odd = word_holonomy(relator, connection["odd"])
    even_factor = factor_polynomial(even)
    odd_factor = factor_polynomial(odd)
    return {
        "relator": relator,
        "length": len(relator),
        "even_holonomy": list(even),
        "odd_holonomy": list(odd),
        "even_factor": list(even_factor),
        "odd_factor": list(odd_factor),
        "direct_factor_cancels": even_factor == odd_factor,
        "even_invertible": matrix_determinant(even) != 0,
        "odd_invertible": matrix_determinant(odd) != 0,
        "even_is_identity": even == IDENTITY,
        "odd_is_identity": odd == IDENTITY,
        "power_supertraces_1_to_12": [
            supertrace(relator, connection, power) for power in range(1, 13)
        ],
    }


def reconstruct_raw(relator: str, candidate: dict[str, Any]) -> str:
    relator_left = relator if int(candidate["left_sign"]) == 1 else inverse_word(relator)
    relator_right = relator if int(candidate["right_sign"]) == 1 else inverse_word(relator)
    left = str(candidate["left_conjugator"])
    right = str(candidate["right_conjugator"])
    return (left + relator_left + inverse_word(left)
            + right + relator_right + inverse_word(right))


def mixed_ledger(relator: str, connection: dict[str, Any],
                 candidates: list[dict[str, Any]], affine_exponent: int | None,
                 checks: CheckBook, namespace: str) -> dict[str, Any]:
    unique: dict[str, dict[str, Any]] = {}
    reconstruction_failures = 0
    for candidate in candidates:
        raw = reconstruct_raw(relator, candidate)
        if raw != candidate["raw_word"]:
            reconstruction_failures += 1
            continue
        reduced = cyclically_reduce(raw)
        if not reduced or not is_cyclically_nonbacktracking(reduced):
            continue
        canonical = canonical_rotation(reduced)
        if not is_literal_primitive(canonical):
            continue
        if affine_exponent is not None:
            if affine_evaluate(canonical, affine_exponent) != (Fraction(0), 0):
                continue
        if canonical not in unique:
            trace_gap = supertrace(canonical, connection, 1)
            unique[canonical] = {
                "word": canonical,
                "length": len(canonical),
                "first_supertrace": trace_gap,
                "power_supertraces_1_to_4": [
                    supertrace(canonical, connection, power)
                    for power in range(1, 5)
                ],
                "raw_word": raw,
                "left_conjugator": candidate["left_conjugator"],
                "right_conjugator": candidate["right_conjugator"],
                "left_sign": candidate["left_sign"],
                "right_sign": candidate["right_sign"],
            }

    leaking = [row for row in unique.values() if row["first_supertrace"] != 0]
    leaking.sort(key=lambda row: (row["length"], row["word"], row["first_supertrace"]))
    checks.check(f"{namespace}:raw_reconstruction", reconstruction_failures == 0,
                 reconstruction_failures)
    checks.check(f"{namespace}:nonempty_normal_closure_sample", bool(unique), len(unique))
    witness = leaking[0] if leaking else None
    return {
        "raw_candidate_count": len(candidates),
        "unique_primitive_cyclic_words": len(unique),
        "mixed_first_trace_leaks": len(leaking),
        "shortest_mixed_leak": witness,
    }


def evaluate_source_fixtures(fixtures: dict[str, Any]) -> dict[str, Any]:
    checks = CheckBook()
    checks.check("schema", fixtures["schema"] == "paper37-source-fixtures-v1")
    checks.check("baseline_exponent", fixtures["baseline_exponent"] == 4)
    checks.check("no_source_oracle", not any(fixtures["source_prohibitions"].values()),
                 fixtures["source_prohibitions"])

    affine_results = []
    for row in fixtures["affine_rows"]:
        exponent = int(row["exponent"])
        relator = str(row["relator"])
        connection = row["connection"]
        direct = direct_factor_row(relator, connection)
        namespace = f"affine_r{exponent}"
        checks.check(f"{namespace}:relator_length", len(relator) == exponent + 3)
        checks.check(f"{namespace}:relator_is_closed",
                     affine_evaluate(relator, exponent) == (Fraction(0), 0))
        checks.check(f"{namespace}:relator_nonbacktracking",
                     is_cyclically_nonbacktracking(relator))
        checks.check(f"{namespace}:direct_all_orders",
                     direct["direct_factor_cancels"]
                     and all(value == 0 for value in direct["power_supertraces_1_to_12"]))
        checks.check(f"{namespace}:nonflat",
                     not direct["even_is_identity"] or not direct["odd_is_identity"])
        checks.check(f"{namespace}:ordinary_invertible",
                     direct["even_invertible"] and direct["odd_invertible"])
        mixed = mixed_ledger(
            relator,
            connection,
            row["mixed_candidates"],
            exponent,
            checks,
            namespace,
        )
        checks.check(f"{namespace}:mixed_leak_exists",
                     mixed["shortest_mixed_leak"] is not None)
        affine_results.append({
            "exponent": exponent,
            "parameter_class": (
                "balanced_control" if exponent == 1 else
                "composite_baseline" if exponent == 4 else
                "exponent_mutation"
            ),
            "direct": direct,
            "mixed": mixed,
        })

    checks.check("affine_family:direct_cancellation_is_generic",
                 all(row["direct"]["direct_factor_cancels"] for row in affine_results))
    checks.check("affine_family:mixed_leak_is_universal_in_sweep",
                 all(row["mixed"]["shortest_mixed_leak"] is not None
                     for row in affine_results))

    fixed_results = []
    for row in fixtures["fixed_one_relator_rows"]:
        control_id = str(row["control_id"])
        direct = direct_factor_row(str(row["relator"]), row["connection"])
        mixed = mixed_ledger(
            str(row["relator"]), row["connection"], row["mixed_candidates"],
            None, checks, f"fixed_{control_id}"
        )
        fixed_results.append({
            "control_id": control_id,
            "direct": direct,
            "mixed": mixed,
        })

    random_results = []
    for row in fixtures["random_one_relator_rows"]:
        control_id = str(row["control_id"])
        direct = direct_factor_row(str(row["relator"]), row["connection"])
        mixed = None
        if direct["direct_factor_cancels"]:
            mixed = mixed_ledger(
                str(row["relator"]), row["connection"], row["mixed_candidates"],
                None, checks, f"random_{control_id}"
            )
            checks.check(f"random_{control_id}:direct_pass_mixed_fail",
                         mixed["shortest_mixed_leak"] is not None)
        random_results.append({
            "control_id": control_id,
            "direct": direct,
            "mixed": mixed,
        })

    random_direct_cancellations = sum(
        1 for row in random_results if row["direct"]["direct_factor_cancels"]
    )
    random_mixed_failures_after_direct = sum(
        1 for row in random_results
        if row["direct"]["direct_factor_cancels"]
        and row["mixed"] is not None
        and row["mixed"]["shortest_mixed_leak"] is not None
    )
    checks.check("random_controls:not_universally_direct",
                 0 < random_direct_cancellations < len(random_results),
                 random_direct_cancellations)
    checks.check("random_controls:every_direct_hit_leaks_mixed",
                 random_direct_cancellations == random_mixed_failures_after_direct,
                 [random_direct_cancellations, random_mixed_failures_after_direct])

    random_presentation_results = []
    random_by_id = {row["control_id"]: row for row in random_results}
    for presentation in fixtures["random_presentations"]:
        index = int(str(presentation["control_id"])[1:])
        pair = [random_by_id[f"R{2 * index:02d}"], random_by_id[f"R{2 * index + 1:02d}"]]
        all_direct = all(row["direct"]["direct_factor_cancels"] for row in pair)
        any_mixed_leak = any(
            row["mixed"] is not None
            and row["mixed"]["shortest_mixed_leak"] is not None
            for row in pair
        )
        random_presentation_results.append({
            "control_id": presentation["control_id"],
            "relators": list(presentation["relators"]),
            "all_direct_factors_cancel": all_direct,
            "mixed_leak_after_direct_hit": any_mixed_leak,
        })
    all_direct_presentations = [
        row for row in random_presentation_results if row["all_direct_factors_cancel"]
    ]
    checks.check("random_presentations:some_all_direct_hits", bool(all_direct_presentations),
                 len(all_direct_presentations))
    checks.check("random_presentations:all_direct_hits_still_leak",
                 all(row["mixed_leak_after_direct_hit"] for row in all_direct_presentations))

    # Exact boundary fixtures: first-trace cancellation is weaker than a full
    # factor; nilpotent cancellation is incompatible with invertible transport.
    traceless_invertible: Matrix = (0, -1, 1, 0)
    nilpotent: Matrix = (0, 1, 0, 0)
    checks.check("boundary:traceless_first_power", matrix_trace(traceless_invertible) == 0)
    checks.check("boundary:traceless_second_power_visible",
                 matrix_trace(matrix_power(traceless_invertible, 2)) == -2)
    checks.check("boundary:traceless_factor_nontrivial",
                 factor_polynomial(traceless_invertible) == (1, 0, 1))
    checks.check("boundary:nilpotent_all_powers",
                 all(matrix_trace(matrix_power(nilpotent, power)) == 0
                     for power in range(1, 9)))
    checks.check("boundary:nilpotent_factor_trivial",
                 factor_polynomial(nilpotent) == (1, 0, 0))
    checks.check("boundary:nilpotent_not_invertible", matrix_determinant(nilpotent) == 0)

    baseline_connection = fixtures["affine_rows"][3]["connection"]
    for letter in ("u", "v"):
        reverse = INVERSE[letter]
        for parity in ("even", "odd"):
            product_matrix = matrix_multiply(
                tuple(baseline_connection[parity][letter]),
                tuple(baseline_connection[parity][reverse]),
            )
            checks.check(f"backtrack:{parity}:{letter}", product_matrix == IDENTITY)

    # A flat balanced pair is an exact all-ledger cancellation control.  It is
    # deliberately presentation independent and therefore proves too much.
    flat_connection = {
        "even": baseline_connection["even"],
        "odd": baseline_connection["even"],
    }
    flat_words = [row["relator"] for row in fixtures["affine_rows"]]
    flat_words.extend(row["relator"] for row in fixtures["random_one_relator_rows"])
    checks.check("flat_control:all_sampled_words_cancel",
                 all(supertrace(str(word), flat_connection, power) == 0
                     for word in flat_words for power in range(1, 5)))

    result = {
        "schema": "paper37-scientific-results-v1",
        "arithmetic_mode": "exact_integer_and_fraction",
        "source_evaluator_separated": True,
        "unit_graph_step_marker_preserved": True,
        "hashimoto_backtracks_excluded_before_coefficients": True,
        "affine_results": affine_results,
        "fixed_one_relator_results": fixed_results,
        "random_one_relator_results": random_results,
        "random_presentations": random_presentation_results,
        "control_summary": {
            "affine_parameter_rows": len(affine_results),
            "random_one_relator_rows": len(random_results),
            "random_direct_cancellations": random_direct_cancellations,
            "random_mixed_failures_after_direct_cancellation": random_mixed_failures_after_direct,
            "random_two_relator_presentations": len(random_presentation_results),
            "random_presentations_all_direct": len(all_direct_presentations),
            "flat_balanced_cancels_every_sampled_word": True,
            "traceless_first_trace_trap": {
                "matrix": list(traceless_invertible),
                "factor": list(factor_polynomial(traceless_invertible)),
            },
            "nilpotent_nonlocal_system_control": {
                "matrix": list(nilpotent),
                "factor": list(factor_polynomial(nilpotent)),
            },
        },
        "theorem_boundary": {
            "ordinary_factor_cancellation_requires_nilpotent_holonomy": True,
            "invertible_local_transport_forbids_nilpotent_holonomy": True,
            "graded_factor_cancellation_equals_nonzero_spectral_matching": True,
            "direct_cell_cancellation_does_not_imply_mixed_cancellation": True,
            "normal_closure_saturation_cancels_every_closed_cayley_word": True,
            "saturated_ledger_has_nonzero_arithmetic_sector": False,
            "finite_enumeration_used_as_infinite_proof": False,
        },
        "decision": {
            "hard_status": "STOP_LOCAL_COEFFICIENT_SATURATION",
            "route_tuple": [
                "A0_STRUCTURAL_ARITHMETIC_RELATION",
                "A1_FAIL",
                "A2_ANALYTIC_DETERMINANT",
                "A3_FAIL",
                "A4_FAIL",
            ],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "proves_too_much": True,
        },
        "checks": checks.rows,
        "check_summary": checks.summary(),
    }
    return result
