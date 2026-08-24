#!/usr/bin/env python3
"""Independent standard-library checker for the C124 evidence receipt."""
from __future__ import annotations

from fractions import Fraction
import itertools
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c124_hardy_evidence.json"


def F(value: str | int | Fraction, denominator: int | None = None) -> Fraction:
    return Fraction(value) if denominator is None else Fraction(value, denominator)


def fstr(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def mmul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))] for i in range(len(left))]


def eye(n: int) -> list[list[Fraction]]:
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def mpow(matrix: list[list[Fraction]], n: int) -> list[list[Fraction]]:
    result = eye(len(matrix))
    base = matrix
    while n:
        if n & 1:
            result = mmul(result, base)
        base = mmul(base, base)
        n //= 2
    return result


def trace(matrix: list[list[Fraction]]) -> Fraction:
    return sum(matrix[i][i] for i in range(len(matrix)))


def det2(matrix: list[list[Fraction]]) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def matvec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]


def vadd(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return [a + b for a, b in zip(left, right)]


def solve2(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    determinant = det2(matrix)
    assert determinant
    return [
        (rhs[0] * matrix[1][1] - matrix[0][1] * rhs[1]) / determinant,
        (matrix[0][0] * rhs[1] - rhs[0] * matrix[1][0]) / determinant,
    ]


def mstrings(matrix: list[list[Fraction]]) -> list[list[str]]:
    return [[fstr(value) for value in row] for row in matrix]


def vstrings(vector: list[Fraction]) -> list[str]:
    return [fstr(value) for value in vector]


def admissible(word: tuple[int, ...], B: list[list[int]]) -> bool:
    return all(B[word[k]][word[(k + 1) % len(word)]] for k in range(len(word)))


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def least_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[k:] + word[:k] for k in range(len(word)))


def compose(A: list[list[Fraction]], translations: list[Fraction], word: tuple[int, ...]) -> tuple[list[list[Fraction]], list[Fraction], list[Fraction], list[list[Fraction]]]:
    linear = eye(2)
    shift = [Fraction(0), Fraction(0)]
    for symbol in word:
        shift = vadd(matvec(A, shift), [translations[symbol], Fraction(0)])
        linear = mmul(A, linear)
    fixed = solve2(
        [[Fraction(i == j) - linear[i][j] for j in range(2)] for i in range(2)],
        shift,
    )
    phases: list[list[Fraction]] = []
    point = fixed
    for symbol in word:
        phases.append(point)
        point = vadd(matvec(A, point), [translations[symbol], Fraction(0)])
    assert point == fixed
    return linear, shift, fixed, phases


def main() -> None:
    evidence_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVIDENCE
    data = json.loads(evidence_path.read_text())
    checks = 0

    def ck(condition: bool, label: str) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    A = [[F(3) / 16, -F(1) / 32], [F(1) / 4, F(0)]]
    translations = [F(-2), F(0), F(2)]
    control = [F(-3) / 2, F(0), F(3) / 2]
    B = [[1, 1, 0], [1, 0, 1], [1, 0, 0]]
    weights = [F(1) / 2, F(1) / 3, F(1) / 5]
    W = [[F(B[i][j]) * weights[j] for j in range(3)] for i in range(3)]

    ck(data["schema"] == "hcs-c124-graph-directed-hardy-trace-v1", "schema")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    lock = data["source_lock"]
    ck(lock["candidate_id"] == "HCS-C124" and lock["clock"] == "one admissible graph edge per iterate", "source lock")
    ck(lock["determinant_convention"] == "D_H(z)=det(I-z*L)", "determinant convention")
    ck(lock["orbit_cutoff"].startswith("none in the theorem"), "cutoff")
    ck("external zero tables" in lock["forbidden_data"], "forbidden data")

    model = data["frozen_model"]
    ck(model["A"] == mstrings(A), "A")
    ck(model["translations"] == [fstr(v) for v in translations], "translations")
    ck(model["adjacency_B"] == [[str(v) for v in row] for row in B], "B")
    ck(model["edge_weights_c"] == [fstr(v) for v in weights], "weights")
    ck(model["weighted_adjacency_W_equals_B_diag_c"] == mstrings(W), "W")
    ck(trace(A) == F(3) / 16 and det2(A) == F(1) / 128, "A spectrum invariants")
    ck(model["symbolic_determinant"] == "Delta(z)=det(I-zW)=1-z/2-z^2/6-z^3/30", "Delta")

    row_norms = [sum(abs(value) for value in row) for row in A]
    first_radius = 3 * row_norms[0]
    second_radius = 3 * row_norms[1]
    original_gap = 2 - 2 * first_radius
    control_gap = F(3) / 2 - 2 * first_radius
    sep = data["strong_separation"]
    ck(sep["A_infinity_row_norms"] == [fstr(v) for v in row_norms], "row norms")
    ck(sep["A_infinity_norm"] == "1/4", "operator norm")
    ck(sep["first_coordinate_image_radius"] == fstr(first_radius), "first radius")
    ck(sep["second_coordinate_image_radius"] == fstr(second_radius), "second radius")
    ck(sep["original_pairwise_first_coordinate_gap"] == fstr(original_gap) and original_gap > 0, "separation gap")
    ck(sep["largest_first_coordinate_extent"] == "85/32" and F(85) / 32 < 3, "interior")
    ck(sep["strong_separation_proved"] is True, "separation flag")

    rooted_counts: dict[int, int] = {}
    primitive_reps: dict[int, list[str]] = {}
    for n in range(1, 9):
        rooted = [word for word in itertools.product(range(3), repeat=n) if admissible(word, B)]
        reps = sorted({least_rotation(word) for word in rooted if primitive(word)})
        rooted_counts[n] = len(rooted)
        primitive_reps[n] = ["".join(str(symbol) for symbol in word) for word in reps]
    periodic = data["periodic_orbits"]
    ck(periodic["rooted_closed_word_counts_n1_to_8"] == {str(n): rooted_counts[n] for n in range(1, 9)}, "rooted counts")
    ck(periodic["primitive_cycle_counts_n1_to_8"] == {str(n): len(primitive_reps[n]) for n in range(1, 9)}, "primitive counts")
    ck(periodic["primitive_representatives_n1_to_8"] == {str(n): primitive_reps[n] for n in range(1, 9)}, "primitive reps")
    ck(sum(rooted_counts.values()) == 284 and sum(len(v) for v in primitive_reps.values()) == 40, "prefix totals")

    monodromy, shift, fixed, phases = compose(A, translations, (0, 1, 2))
    ck(periodic["example_word"] == "012" and periodic["example_weight"] == "1/30", "example identity")
    ck(periodic["example_monodromy_A_cubed"] == mstrings(monodromy), "example monodromy")
    ck(periodic["example_composition_shift"] == [[fstr(v)] for v in shift], "example shift")
    det_i_m = det2([[F(i == j) - monodromy[i][j] for j in range(2)] for i in range(2)])
    ck(periodic["example_det_I_minus_monodromy"] == fstr(det_i_m), "example fixed determinant")
    ck(periodic["example_fixed_phase_points"] == [vstrings(point) for point in phases], "example points")
    ck(fixed == [F(38912) / 19929, -F(1600) / 19929], "example anchor")

    symbolic: dict[int, Fraction] = {}
    hardy: dict[int, Fraction] = {}
    for n in range(1, 9):
        symbolic[n] = trace(mpow(W, n))
        hardy[n] = symbolic[n] / ((1 - F(1, 8) ** n) * (1 - F(1, 16) ** n))
    hop = data["hardy_operator"]
    ck(hop["trace_class"] is True and hop["space"] == "H=direct_sum_{i=0}^2 H^2(D_3^2)", "Hardy owner")
    ck(hop["symbolic_trace_powers_n1_to_8"] == {str(n): fstr(symbolic[n]) for n in range(1, 9)}, "symbolic traces")
    ck(hop["hardy_trace_powers_n1_to_8"] == {str(n): fstr(hardy[n]) for n in range(1, 9)}, "Hardy traces")
    cutoff = {}
    for degree in range(6):
        cutoff[str(degree)] = {}
        for n in range(1, 4):
            partial = sum(F(1, 8) ** (r * n) * F(1, 16) ** (s * n) for r in range(degree + 1) for s in range(degree + 1 - r))
            cutoff[str(degree)][str(n)] = fstr(symbolic[n] * partial)
    ck(hop["polynomial_cutoff_trace_M0_to_M5_n1_to_n3"] == cutoff, "polynomial cutoff traces")

    coefficients = [F(1)]
    for n in range(1, 9):
        coefficients.append(-sum(hardy[k] * coefficients[n - k] for k in range(1, n + 1)) / n)
    fred = data["fredholm_and_primitive_identity"]
    ck(fred["taylor_coefficients_ascending_z0_to_z8"] == [fstr(v) for v in coefficients], "Fredholm coefficients")
    ck(fred["lattice_product"].startswith("product_{r,s>=0}"), "lattice product")
    ck("sum_[gamma]" in fred["primitive_log_expansion"], "primitive formula")
    ck(fred["owner_statement"].startswith("the same graph-directed source owns"), "joint owner")

    cmon, cshift, cfixed, cphases = compose(A, control, (0, 1, 2))
    blindness = data["translation_blindness_control"]
    ck(blindness["control_translations"] == [fstr(v) for v in control], "control translations")
    ck(blindness["control_pairwise_first_coordinate_gap"] == fstr(control_gap) and control_gap > 0, "control separation")
    ck(blindness["same_A_B_c_W"] is True and blindness["same_all_power_traces_and_fredholm_determinant"] is True, "blind invariants")
    ck(cmon == monodromy and cfixed != fixed, "blindness math")
    ck(blindness["control_example_composition_shift"] == [[fstr(v)] for v in cshift], "control shift")
    ck(blindness["control_example_fixed_phase_points"] == [vstrings(point) for point in cphases], "control points")
    ck(blindness["geometry_changed"] is True and "blind to branch translations" in blindness["negative_conclusion"], "negative control conclusion")

    progress = data["progress_over_prior_gate"]
    ck("nontrivial primitive" in progress["over_C119"] and "all-period" in progress["over_C123"], "progress")
    verdict = data["verdict"]
    ck(verdict["A1"] == "A1_WEAK", "A1")
    ck(verdict["A2"] == "A2_FAIL", "A2")
    ck(verdict["A3"] == "A3_FAIL", "A3")
    ck(verdict["A4"] == "A4_FAIL", "A4")
    ck(verdict["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    ck(verdict["route_b_invocation_allowed"] is False, "route B")
    ck(len(data["nonclaims"]) == 6 and "determinant sensitivity" in data["nonclaims"][-1], "nonclaims")

    print(json.dumps({"status": "C124_INDEPENDENT_CHECK_PASS", "checks": checks, "evidence": str(evidence_path)}, sort_keys=True))


if __name__ == "__main__":
    main()
