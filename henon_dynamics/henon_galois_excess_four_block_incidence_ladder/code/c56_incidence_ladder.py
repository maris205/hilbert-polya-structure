#!/usr/bin/env python3
"""Exact HCS-P56 certificate for the four-block incidence ladder."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c56_certificate.json"

X, T, Z = sp.symbols("X T Z")
E1, E3, E4A, E4B, E5A, E5B, E6 = sp.symbols(
    "E_1 E_3 E_4A E_4B E_5A E_5B E_6"
)
ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)

DEPENDENCIES = {
    "p55_readme": (
        TRACK / "henon_galois_excess_three_block_obstruction" / "README.md",
        "112c0c12444a8b14069e57046efd8e55de7c8ea23373d2f70987bd0ff8980967",
    ),
    "p55_proof": (
        TRACK / "henon_galois_excess_three_block_obstruction" / "PROOF_PACKAGE.md",
        "d341f8b2bdcc17afb94e8ed5ed36c0296c0df527d7d619f11077ae4a641a639d",
    ),
    "p55_certificate": (
        TRACK
        / "henon_galois_excess_three_block_obstruction"
        / "results"
        / "c55_certificate.json",
        "d21cdcdfcce7cb279fab02ee3222c5d5a10e4fc6efa63e2e611d135e2ff27f1c",
    ),
    "p55_code": (
        TRACK
        / "henon_galois_excess_three_block_obstruction"
        / "code"
        / "c55_galois_blocks.py",
        "b5227176497429051b834f12e90deadf3605016374ea39cdf4c86f53388411c3",
    ),
    "p54_certificate": (
        TRACK
        / "henon_mahler_pressure_pole_galois_excess_gate"
        / "results"
        / "c54_certificate.json",
        "d6932d0b24111866253508b5dd7c33972856cfdbddd5dfdd7db77a92a38f233c",
    ),
    "p31_certificate": (
        TRACK / "henon_bowen_pressure_gate" / "results" / "c31_certificate.json",
        "9f326c8442f5f1dfb8215527491a9ebbac2395fde7892c88bc78634df24c5cca",
    ),
    "orbit_catalog": (
        TRACK / "henon_instability_roof_zeta" / "results" / "catalog_validation.json",
        "0eab1930a17e4315e59eebc9dc7d3ef111b674d3625f09ca3396c1aa7c814fde",
    ),
}

TRACE5 = sp.Poly(
    T**6
    + 3300 * T**5
    - 34165368 * T**4
    - 7291075328 * T**3
    + 26529205510272 * T**2
    + 3609165326736384 * T
    - 4266315336505009664,
    T,
)
TRACE5_INTERVALS = (
    (-7607, -7606),
    (-711, -710),
    (-590, -589),
    (390, 391),
    (770, 771),
    (4445, 4446),
)


def canonical_sha(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def dependency_locks() -> dict[str, dict[str, str]]:
    locks: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency hash changed: {name}")
        locks[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return locks


def rotations(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(word[i:] + word[:i] for i in range(len(word)))


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def primitive_cycles(max_period: int = 6) -> dict[int, list[tuple[int, ...]]]:
    result: dict[int, list[tuple[int, ...]]] = {}
    for n in range(1, max_period + 1):
        cycles: set[tuple[int, ...]] = set()
        for word in itertools.product(range(4), repeat=n):
            if all(ADJACENCY[word[i]][word[(i + 1) % n]] for i in range(n)) and primitive(word):
                cycles.add(min(rotations(word)))
        result[n] = sorted(cycles)
    return result


def family_a(n: int) -> tuple[int, ...]:
    if n < 3:
        raise ValueError("A_n starts at n=3")
    return (0,) * (n - 2) + (2, 1)


def family_b(n: int) -> tuple[int, ...]:
    if n < 4:
        raise ValueError("B_n starts at n=4")
    return (0,) * (n - 3) + (2, 3, 1)


def block_counter(word: tuple[int, ...], width: int) -> dict[tuple[int, ...], int]:
    counter: dict[tuple[int, ...], int] = {}
    for i in range(len(word)):
        block = tuple(word[(i + j) % len(word)] for j in range(width))
        counter[block] = counter.get(block, 0) + 1
    return counter


def row_difference(
    positive: tuple[int, ...], negative: tuple[int, ...], width: int
) -> dict[tuple[int, ...], int]:
    result = block_counter(positive, width)
    for block, value in block_counter(negative, width).items():
        result[block] = result.get(block, 0) - value
    return {block: value for block, value in result.items() if value}


def signed_sum(rows: tuple[tuple[int, tuple[int, ...]], ...], width: int) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for sign, word in rows:
        for block, value in block_counter(word, width).items():
            result[block] = result.get(block, 0) + sign * value
    return {block: value for block, value in result.items() if value}


def incidence_matrix(words: list[tuple[int, ...]], width: int) -> tuple[list[tuple[int, ...]], sp.Matrix]:
    counters = [block_counter(word, width) for word in words]
    blocks = sorted({block for counter in counters for block in counter})
    matrix = sp.Matrix([[counter.get(block, 0) for block in blocks] for counter in counters])
    return blocks, matrix


def symbolic_ladder(max_width: int = 64) -> dict[str, object]:
    verified: list[int] = []
    insertion_rows: dict[str, dict[str, int]] = {}
    for m in range(3, max_width + 1):
        delta_a = row_difference(family_a(m + 1), family_a(m), m)
        delta_b = row_difference(family_b(m + 2), family_b(m + 1), m)
        expected = {
            (0,) * (m - 1) + (2,): 1,
            (1,) + (0,) * (m - 1): 1,
            (1,) + (0,) * (m - 2) + (2,): -1,
        }
        if delta_a != expected or delta_b != expected:
            raise ArithmeticError(f"insertion identity failed at m={m}")
        relation = signed_sum(
            (
                (1, family_a(m)),
                (1, family_b(m + 2)),
                (-1, family_a(m + 1)),
                (-1, family_b(m + 1)),
            ),
            m,
        )
        if relation:
            raise ArithmeticError(f"incidence ladder failed at m={m}")
        if m in (3, 4, 5, max_width):
            insertion_rows[str(m)] = {"".join(map(str, key)): value for key, value in expected.items()}
        verified.append(m)
    return {
        "theorem": "N_m(A_m)+N_m(B_{m+2})=N_m(A_{m+1})+N_m(B_{m+1}) for every m>=3",
        "proof_difference": "e_(0^(m-1)2)+e_(10^(m-1))-e_(10^(m-2)2)",
        "finite_verification_range": [verified[0], verified[-1]],
        "selected_insertion_rows": insertion_rows,
    }


def derivative(q: sp.Expr) -> sp.Matrix:
    return sp.Matrix([[-12 * q, -1], [1, 0]])


def monodromy(coordinates: tuple[sp.Expr, ...]) -> sp.Matrix:
    matrix = sp.eye(2)
    for coordinate in coordinates:
        matrix = derivative(coordinate) * matrix
    return matrix.applyfunc(sp.simplify)


def recurrence_residuals(coordinates: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    n = len(coordinates)
    return tuple(
        sp.simplify(
            1 - 6 * coordinates[i] ** 2 - coordinates[(i - 1) % n] - coordinates[(i + 1) % n]
        )
        for i in range(n)
    )


def period_six_algebra() -> dict[str, object]:
    sqrt7 = sp.sqrt(7)
    discriminant = sp.sqrt(25 + 4 * sqrt7)
    a = (-1 - discriminant) / 12
    c = -sqrt7 / 6
    d = (-1 + discriminant) / 12
    coordinates = (a, a, c, d, d, c)
    residuals = recurrence_residuals(coordinates)
    if any(residuals):
        raise ArithmeticError("period-six recurrence mismatch")
    matrix = monodromy(coordinates)
    trace = sp.simplify(sp.trace(matrix))
    expected_trace = 18062 + 5352 * sqrt7
    if trace != expected_trace or not sp.det(matrix).equals(1):
        raise ArithmeticError("period-six monodromy mismatch")
    trace_minpoly = sp.Poly(sp.minimal_polynomial(trace, T), T)
    if trace_minpoly != sp.Poly(T**2 - 36124 * T + 125728516, T):
        raise ArithmeticError("period-six trace field mismatch")
    multiplier_minpoly = sp.Poly(
        Z**4 - 36124 * Z**3 + 125728518 * Z**2 - 36124 * Z + 1, Z
    )
    if sp.factor_list(multiplier_minpoly.as_expr())[1] != [(multiplier_minpoly.as_expr(), 1)]:
        raise ArithmeticError("period-six multiplier polynomial reducible")
    reduction13 = sp.Poly(multiplier_minpoly.as_expr(), Z, modulus=13)
    gcd13 = sp.gcd(reduction13, sp.Poly(Z**13 - Z, Z, modulus=13))
    gcd169 = sp.gcd(reduction13, sp.Poly(Z**169 - Z, Z, modulus=13))
    if gcd13.degree() != 0 or gcd169.degree() != 0:
        raise ArithmeticError("period-six mod-13 irreducibility witness failed")
    half_conjugate = 9031 - 2676 * sqrt7
    lower_margin = 7081**2 - 2676**2 * 7
    upper_margin = 2676**2 * 7 - 7080**2
    if (lower_margin, upper_margin) != (13729, 432):
        raise ArithmeticError("period-six trace isolation margins changed")
    if not (1950 < half_conjugate < 1951):
        raise ArithmeticError("period-six conjugate trace was not isolated")
    excess = sp.acosh(half_conjugate)
    return {
        "word": "000231",
        "sign_word": "---++-",
        "coordinates_exact": [str(value) for value in coordinates],
        "coordinates_decimal_40": [str(sp.N(value, 40)) for value in coordinates],
        "recurrence_residuals": [str(value) for value in residuals],
        "trace": str(trace),
        "trace_conjugate": str(18062 - 5352 * sqrt7),
        "trace_minpoly_coefficients": [int(value) for value in trace_minpoly.all_coeffs()],
        "multiplier_minpoly_coefficients": [int(value) for value in multiplier_minpoly.all_coeffs()],
        "multiplier_degree": multiplier_minpoly.degree(),
        "multiplier_mod_13_coefficients": [1, 3, 6, 3, 1],
        "multiplier_mod_13_gcd_degrees": [gcd13.degree(), gcd169.degree()],
        "determinant": 1,
        "physical_length_decimal_50": str(sp.N(sp.acosh(trace / 2), 50)),
        "galois_excess": str(excess),
        "galois_excess_decimal_50": str(sp.N(excess, 50)),
        "conjugate_half_trace_interval": [1950, 1951],
        "square_margins": [lower_margin, upper_margin],
    }


def excess_obstruction() -> dict[str, object]:
    if [int(TRACE5.count_roots(left, right)) for left, right in TRACE5_INTERVALS] != [1] * 6:
        raise ArithmeticError("period-five trace intervals changed")
    roots = sorted((sp.re(root) for root in sp.nroots(TRACE5.as_expr(), n=80)), key=float)
    lengths = [sp.acosh(sp.Abs(root) / 2) for root in roots]
    total_height = sum(lengths, sp.Float(0, 80))
    excess_a5 = total_height - lengths[0]
    excess_b5 = total_height - lengths[-1]
    excess_a4 = sp.acosh(287 - 96 * sp.sqrt(6))
    excess_b6 = sp.acosh(9031 - 2676 * sp.sqrt(7))
    delta4 = excess_a4 + excess_b6 - excess_a5 - excess_b5

    integer_margin = 709**2 - 104 * 3902
    if integer_margin != 96873:
        raise ArithmeticError("logarithmic obstruction margin changed")
    if not (2 * sp.acosh(355) > sp.acosh(52) + sp.acosh(1951)):
        raise ArithmeticError("exact obstruction inequality failed")
    if not delta4 < 0:
        raise ArithmeticError("numeric obstruction sign changed")
    return {
        "period_5_trace_intervals": [list(interval) for interval in TRACE5_INTERVALS],
        "period_5_total_height_decimal_50": str(sp.N(total_height, 50)),
        "A5_excess_decimal_50": str(sp.N(excess_a5, 50)),
        "B5_excess_decimal_50": str(sp.N(excess_b5, 50)),
        "A4_excess_decimal_50": str(sp.N(excess_a4, 50)),
        "B6_excess_decimal_50": str(sp.N(excess_b6, 50)),
        "delta_4_decimal_50": str(sp.N(delta4, 50)),
        "strict_chain": "E(A5)+E(B5)>2 acosh(355)>acosh(52)+acosh(1951)>E(A4)+E(B6)",
        "integer_comparison": {"709_squared": 709**2, "104_times_3902": 104 * 3902, "margin": integer_margin},
        "width_at_most_4_obstruction": True,
    }


def finite_sharpness() -> dict[str, object]:
    words = [
        (0,),
        family_a(3),
        family_a(4),
        family_b(4),
        family_a(5),
        family_b(5),
        family_b(6),
    ]
    selected = [
        (0, 0, 0, 0, 0),
        (0, 0, 0, 2, 1),
        (0, 0, 0, 2, 3),
        (0, 0, 2, 1, 0),
        (0, 0, 2, 3, 1),
        (0, 2, 1, 0, 2),
        (0, 2, 3, 1, 0),
    ]
    matrix = sp.Matrix(
        [[block_counter(word, 5).get(block, 0) for block in selected] for word in words]
    )
    if matrix.det() != 1:
        raise ArithmeticError("width-five interpolation minor changed")
    solution = matrix.inv() * sp.Matrix([E1, E3, E4A, E4B, E5A, E5B, E6])
    four_words = [family_a(4), family_b(6), family_a(5), family_b(5)]
    _, width4 = incidence_matrix(four_words, 4)
    if width4.rank() != 3 or (sp.Matrix([[1, 1, -1, -1]]) * width4) != sp.zeros(1, width4.cols):
        raise ArithmeticError("width-four relation matrix changed")
    return {
        "width_4_four_row_rank": width4.rank(),
        "width_4_left_relation": [1, 1, -1, -1],
        "width_5_selected_blocks": ["".join(map(str, block)) for block in selected],
        "width_5_minor": [[int(value) for value in row] for row in matrix.tolist()],
        "width_5_determinant": int(matrix.det()),
        "width_5_interpolating_values": [str(value) for value in solution],
        "finite_witness_sharp_at_width_5": True,
    }


def holder_gate() -> dict[str, object]:
    return {
        "discrepancy": "Delta_m=E(A_m)+E(B_(m+2))-E(A_(m+1))-E(B_(m+1))",
        "one_sided_holder_necessary_bound": "|Delta_m| <= C(4m+4) theta^(alpha*m)",
        "quantifiers": "every integer m>=3 for one fixed C>0, 0<theta<1, alpha>0",
        "two_sided_caveat": "requires an explicit cohomological reduction to a future-dependent representative",
        "status": "OPEN_ASYMPTOTICS",
    }


def build_base_certificate() -> dict[str, object]:
    cycles = primitive_cycles(6)
    expected_counts = {1: 1, 2: 0, 3: 1, 4: 2, 5: 2, 6: 2}
    if {period: len(rows) for period, rows in cycles.items()} != expected_counts:
        raise ArithmeticError("primitive cycle census changed")
    expected_cycles = {
        3: [family_a(3)],
        4: [family_a(4), family_b(4)],
        5: [family_a(5), family_b(5)],
        6: [family_a(6), family_b(6)],
    }
    if any(cycles[period] != rows for period, rows in expected_cycles.items()):
        raise ArithmeticError("A/B family identification changed")
    return {
        "artifact": "HCS-P56",
        "claim_class": "PROVED_EXACT_FINITE_MEMORY_OBSTRUCTION_AND_INFINITE_NECESSARY_LADDER",
        "arithmetic_advance": False,
        "route_a": "ROUTE_A_EXPLORATORY",
        "route_b": "NOT_AUTHORIZED",
        "dependencies": dependency_locks(),
        "cycle_counts": {str(period): count for period, count in expected_counts.items()},
        "cycle_families": {
            "A_n": "0^(n-2)21, n>=3",
            "B_n": "0^(n-3)231, n>=4",
            "through_period_6": {
                str(period): ["".join(map(str, word)) for word in cycles[period]]
                for period in range(1, 7)
            },
        },
        "incidence_ladder": symbolic_ladder(),
        "period_6_B": period_six_algebra(),
        "four_block_obstruction": excess_obstruction(),
        "finite_sharpness": finite_sharpness(),
        "holder_gate": holder_gate(),
        "strongest_positive_result": "an exact all-m block-incidence ladder and an exact degree-four B6 multiplier field",
        "strongest_obstruction": "the m=4 forced excess identity fails by an explicit strict logarithmic inequality",
        "open_theorem": "determine the asymptotics of Delta_m and test exponential Holder decay",
        "reusable_structure": "the identical three-atom insertion difference for A and B block rows",
        "round2_clue": "derive a recurrence or renormalization law for Delta_m along the two homoclinic cycle families",
    }


def exact_schema(candidate: object, expected: object, path: str = "root") -> None:
    if type(candidate) is not type(expected):
        raise ValueError(f"type changed at {path}")
    if isinstance(expected, dict):
        if set(candidate) != set(expected) or any(type(key) is not str for key in candidate):
            raise ValueError(f"keys changed at {path}")
        for key in expected:
            exact_schema(candidate[key], expected[key], f"{path}.{key}")
    elif isinstance(expected, list):
        if len(candidate) != len(expected):
            raise ValueError(f"length changed at {path}")
        for index, value in enumerate(expected):
            exact_schema(candidate[index], value, f"{path}[{index}]")
    elif candidate != expected:
        raise ValueError(f"value changed at {path}")


def mutation_audit(base: dict[str, object]) -> dict[str, object]:
    mutations = (
        ("promote_arithmetic", lambda row: row.__setitem__("arithmetic_advance", True)),
        ("promote_route_a", lambda row: row.__setitem__("route_a", "ROUTE_A_PASS")),
        ("authorize_route_b", lambda row: row.__setitem__("route_b", "ROUTE_B_PASS")),
        ("drop_dependency", lambda row: row["dependencies"].pop("p55_proof")),
        ("forge_dependency", lambda row: row["dependencies"]["p55_proof"].__setitem__("sha256", "0" * 64)),
        ("change_cycle_count", lambda row: row["cycle_counts"].__setitem__("6", 3)),
        ("change_family", lambda row: row["cycle_families"].__setitem__("A_n", "0^(n-1)21")),
        ("shorten_ladder", lambda row: row["incidence_ladder"].__setitem__("finite_verification_range", [3, 8])),
        ("change_insertion", lambda row: row["incidence_ladder"].__setitem__("proof_difference", "two atoms")),
        ("change_trace", lambda row: row["period_6_B"].__setitem__("trace", "18062")),
        ("change_trace_minpoly", lambda row: row["period_6_B"]["trace_minpoly_coefficients"].__setitem__(2, 0)),
        ("change_multiplier_degree", lambda row: row["period_6_B"].__setitem__("multiplier_degree", 2)),
        ("change_interval", lambda row: row["period_6_B"].__setitem__("conjugate_half_trace_interval", [1949, 1951])),
        ("flip_obstruction", lambda row: row["four_block_obstruction"].__setitem__("width_at_most_4_obstruction", False)),
        ("change_integer_margin", lambda row: row["four_block_obstruction"]["integer_comparison"].__setitem__("margin", 0)),
        ("change_rank", lambda row: row["finite_sharpness"].__setitem__("width_4_four_row_rank", 4)),
        ("change_determinant", lambda row: row["finite_sharpness"].__setitem__("width_5_determinant", -1)),
        ("drop_selected_block", lambda row: row["finite_sharpness"]["width_5_selected_blocks"].pop()),
        ("promote_holder", lambda row: row["holder_gate"].__setitem__("status", "PROVED")),
        ("drop_two_sided_caveat", lambda row: row["holder_gate"].__setitem__("two_sided_caveat", "none")),
    )
    rejected: list[str] = []
    for label, mutate in mutations:
        candidate = copy.deepcopy(base)
        mutate(candidate)
        try:
            exact_schema(candidate, base)
        except ValueError:
            rejected.append(label)
        else:
            raise RuntimeError(f"mutation accepted: {label}")
    return {
        "count": len(rejected),
        "labels": rejected,
        "trace_sha256": canonical_sha(rejected),
    }


def run_check() -> dict[str, object]:
    base = build_base_certificate()
    audit = mutation_audit(base)
    result = dict(base)
    result["mutation_audit"] = audit
    result["base_payload_sha256"] = canonical_sha(base)
    result["check"] = True
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    if not args.check:
        raise SystemExit("explicit --check is required")
    result = run_check()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
