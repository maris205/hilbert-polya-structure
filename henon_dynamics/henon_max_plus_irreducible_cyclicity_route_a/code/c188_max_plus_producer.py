#!/usr/bin/env python3
"""Produce the exact C188 max-plus cyclicity and orbit ledger."""
from __future__ import annotations

from fractions import Fraction
from functools import reduce
from hashlib import sha256
from itertools import product
import json
import math
import os
from pathlib import Path
from typing import Optional


Q = Fraction
Entry = Optional[Fraction]
Matrix = tuple[tuple[Entry, ...], ...]
Vector = tuple[Entry, ...]
NEG: Entry = None
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(os.environ.get("C188_OUTPUT", ROOT / "results/c188_max_plus_evidence.json"))
SOURCE_COMMIT = "908a6818caedb0c46195a591873a2ac9c685b55e"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"


def add(x: Entry, y: Entry) -> Entry:
    return NEG if x is NEG or y is NEG else x + y


def enc(x: Entry) -> str:
    if x is NEG:
        return "-inf"
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def enc_matrix(a: Matrix) -> list[list[str]]:
    return [[enc(x) for x in row] for row in a]


def enc_vector(x: Vector) -> list[str]:
    return [enc(v) for v in x]


def identity(n: int) -> Matrix:
    return tuple(tuple(Q(0) if i == j else NEG for j in range(n)) for i in range(n))


def mp_mul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    out = []
    for i in range(n):
        row = []
        for j in range(n):
            terms = [a[i][k] + b[k][j] for k in range(n) if a[i][k] is not NEG and b[k][j] is not NEG]
            row.append(max(terms) if terms else NEG)
        out.append(tuple(row))
    return tuple(out)


def mp_vec(a: Matrix, x: Vector) -> Vector:
    out = []
    for row in a:
        terms = [v + xj for v, xj in zip(row, x) if v is not NEG and xj is not NEG]
        out.append(max(terms) if terms else NEG)
    return tuple(out)


def mp_max(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(
            y if x is NEG else x if y is NEG else max(x, y)
            for x, y in zip(row_a, row_b)
        )
        for row_a, row_b in zip(a, b)
    )


def normalize_projective(x: Vector) -> Vector:
    finite = [v for v in x if v is not NEG]
    if not finite:
        return x
    top = max(finite)
    return tuple(NEG if v is NEG else v - top for v in x)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def lcm(values: list[int]) -> int:
    return reduce(math.lcm, values, 1)


def support_strong(a: Matrix) -> bool:
    n = len(a)
    for reverse in (False, True):
        seen = {0}
        stack = [0]
        while stack:
            u = stack.pop()
            for v in range(n):
                edge = a[v][u] if reverse else a[u][v]
                if edge is not NEG and v not in seen:
                    seen.add(v)
                    stack.append(v)
        if len(seen) != n:
            return False
    return True


def simple_cycles(a: Matrix, allowed_edges: set[tuple[int, int]] | None = None) -> list[tuple[int, ...]]:
    n = len(a)
    cycles: list[tuple[int, ...]] = []
    for start in range(n):
        def dfs(path: list[int], used: set[int]) -> None:
            u = path[-1]
            for v in range(start, n):
                if a[u][v] is NEG or (allowed_edges is not None and (u, v) not in allowed_edges):
                    continue
                if v == start:
                    cycles.append(tuple(path))
                elif v not in used:
                    dfs(path + [v], used | {v})
        dfs([start], {start})
    return sorted(set(cycles))


def cycle_weight(a: Matrix, cyc: tuple[int, ...]) -> Fraction:
    return sum((a[cyc[i]][cyc[(i + 1) % len(cyc)]] for i in range(len(cyc))), Q(0))


def components(nodes: set[int], edges: set[tuple[int, int]]) -> list[list[int]]:
    left = set(nodes)
    result = []
    while left:
        seed = min(left)
        forward = {seed}
        stack = [seed]
        while stack:
            u = stack.pop()
            for x, v in edges:
                if x == u and v not in forward:
                    forward.add(v)
                    stack.append(v)
        backward = {seed}
        stack = [seed]
        while stack:
            u = stack.pop()
            for v, x in edges:
                if x == u and v not in backward:
                    backward.add(v)
                    stack.append(v)
        comp = sorted(forward & backward)
        result.append(comp)
        left -= set(comp)
    return sorted(result)


def critical_data(a: Matrix) -> tuple[Fraction, list[dict], set[tuple[int, int]], list[dict], int]:
    cycles = simple_cycles(a)
    assert cycles
    means = [(cyc, cycle_weight(a, cyc), cycle_weight(a, cyc) / len(cyc)) for cyc in cycles]
    lam = max(mean for _, _, mean in means)
    critical_cycles = [cyc for cyc, _, mean in means if mean == lam]
    critical_edges = {
        (cyc[i], cyc[(i + 1) % len(cyc)])
        for cyc in critical_cycles
        for i in range(len(cyc))
    }
    critical_nodes = {v for edge in critical_edges for v in edge}
    comp_rows = []
    for comp in components(critical_nodes, critical_edges):
        comp_set = set(comp)
        sub_cycles = [
            cyc for cyc in simple_cycles(a, critical_edges)
            if set(cyc).issubset(comp_set)
        ]
        cyc = reduce(math.gcd, (len(c) for c in sub_cycles))
        comp_rows.append({"nodes": comp, "cyclicity": cyc})
    gamma = lcm([row["cyclicity"] for row in comp_rows])
    cycle_rows = [
        {
            "nodes": list(cyc),
            "length": len(cyc),
            "weight": enc(weight),
            "mean": enc(mean),
            "critical": mean == lam,
        }
        for cyc, weight, mean in means
    ]
    return lam, cycle_rows, critical_edges, comp_rows, gamma


def shift(a: Matrix, lam: Fraction) -> Matrix:
    return tuple(tuple(NEG if x is NEG else x - lam for x in row) for row in a)


def powers_until(a: Matrix, limit: int) -> list[Matrix]:
    out = [identity(len(a))]
    for _ in range(limit):
        out.append(mp_mul(out[-1], a))
    return out


def least_transient(powers: list[Matrix], gamma: int) -> int:
    for t in range(len(powers) - gamma):
        if powers[t + gamma] == powers[t]:
            return t
    raise AssertionError("transient search limit exhausted")


def csr_matrices(b: Matrix, critical_edges: set[tuple[int, int]], gamma: int) -> tuple[Matrix, Matrix, Matrix]:
    n = len(b)
    q = identity(n)
    for _ in range(gamma):
        q = mp_mul(q, b)
    star = identity(n)
    term = identity(n)
    for _ in range(1, n):
        term = mp_mul(term, q)
        star = mp_max(star, term)
    critical_nodes = {v for edge in critical_edges for v in edge}
    c = tuple(tuple(star[i][j] if j in critical_nodes else NEG for j in range(n)) for i in range(n))
    r = tuple(tuple(star[i][j] if i in critical_nodes else NEG for j in range(n)) for i in range(n))
    s = tuple(tuple(b[i][j] if (i, j) in critical_edges else NEG for j in range(n)) for i in range(n))
    return c, s, r


def csr_power(c: Matrix, s_powers: list[Matrix], r: Matrix, t: int) -> Matrix:
    return mp_mul(mp_mul(c, s_powers[t]), r)


def least_csr_transient(powers: list[Matrix], c: Matrix, s: Matrix, r: Matrix, gamma: int) -> int:
    s_powers = powers_until(s, len(powers) - 1)
    for t in range(len(powers) - 2 * gamma):
        if all(csr_power(c, s_powers, r, u) == powers[u] for u in range(t, t + 2 * gamma)):
            return t
    raise AssertionError("CSR transient search limit exhausted")


def matrix_key(a: Matrix) -> tuple[tuple[str, ...], ...]:
    return tuple(tuple(enc(x) for x in row) for row in a)


def cycle_matrix(n: int, weights: list[Fraction]) -> Matrix:
    return tuple(
        tuple(weights[i] if j == (i + 1) % n else NEG for j in range(n))
        for i in range(n)
    )


def catalog() -> list[tuple[str, Matrix, list[str]]]:
    rows: list[tuple[str, Matrix, list[str]]] = []
    seen: set[tuple[tuple[str, ...], ...]] = set()

    def add_row(name: str, a: Matrix, tags: list[str]) -> None:
        assert support_strong(a), name
        key = matrix_key(a)
        if key not in seen:
            seen.add(key)
            rows.append((name, a, tags))

    values = [NEG, Q(-1), Q(0), Q(1)]
    grid_index = 0
    for flat in product(values, repeat=4):
        a = (tuple(flat[:2]), tuple(flat[2:]))
        if support_strong(a):
            add_row(f"grid2_{grid_index:03d}", a, ["complete_two_by_two_grid"])
            grid_index += 1

    add_row("singleton_shift", ((Q(7, 3),),), ["dimension_one", "primitive"])
    for n in range(3, 7):
        add_row(f"pure_cycle_{n}", cycle_matrix(n, [Q(0)] * n), ["pure_cycle", "transient_zero"])

    multi = [[NEG for _ in range(5)] for _ in range(5)]
    multi[0][1] = multi[1][0] = Q(0)
    multi[2][3] = multi[3][4] = multi[4][2] = Q(0)
    multi[1][2] = multi[4][0] = Q(-7)
    add_row("critical_scc_2_plus_3", tuple(tuple(row) for row in multi), ["multiple_critical_scc", "gamma_lcm_six"])

    for m in range(2, 25):
        a = ((Q(0), Q(-m)), (Q(0), Q(-1)))
        add_row(f"unbounded_transient_m{m:02d}", a, ["fixed_support_transient_family", f"expected_transient_{m}"])

    for q in range(2, 6):
        weights = [Q(1, q), Q(-1, q), Q(2, q)]
        add_row(f"rational_cycle_q{q}", cycle_matrix(3, weights), ["rational_weights", "nonintegral_lambda"])
    return rows


def classify_vector(b: Matrix, powers: list[Matrix], gamma: int, matrix_transient: int, vector_id: str, x: Vector) -> dict:
    states = [mp_vec(p, x) for p in powers]
    projective = [normalize_projective(y) for y in states]
    raw_period = next(p for p in divisors(gamma) if states[matrix_transient + p] == states[matrix_transient])
    proj_period = next(p for p in divisors(gamma) if projective[matrix_transient + p] == projective[matrix_transient])
    raw_transient = next(t for t in range(matrix_transient + 1) if states[t + raw_period] == states[t])
    proj_transient = next(t for t in range(matrix_transient + 1) if projective[t + proj_period] == projective[t])
    attr = [p for p in divisors(gamma) if states[matrix_transient + p] == states[matrix_transient]]
    projective_attr = [p for p in divisors(gamma) if projective[matrix_transient + p] == projective[matrix_transient]]
    return {
        "vector_id": vector_id,
        "x": enc_vector(x),
        "eventual_period": raw_period,
        "eventual_transient": raw_transient,
        "projective_period": proj_period,
        "projective_transient": proj_transient,
        "attraction_divisors": attr,
        "projective_attraction_divisors": projective_attr,
    }


def main() -> None:
    matrix_rows = []
    vector_rows = []
    total_cycles = 0
    critical_components_total = 0
    csr_cells_checked = 0
    propagation_cells_checked = 0
    for matrix_id, a, tags in catalog():
        lam, cycles, critical_edges, comp_rows, gamma = critical_data(a)
        b = shift(a, lam)
        powers = powers_until(b, 520)
        transient = least_transient(powers, gamma)
        for t in range(transient, transient + 3 * gamma + len(a) + 1):
            assert powers[t + gamma] == powers[t]
            propagation_cells_checked += len(a) * len(a)
        for p in divisors(gamma)[:-1]:
            assert powers[transient + p] != powers[transient]
        c, s, r = csr_matrices(b, critical_edges, gamma)
        csr_transient = least_csr_transient(powers, c, s, r, gamma)
        s_powers = powers_until(s, csr_transient + 3 * gamma + 2)
        for t in range(csr_transient, csr_transient + 3 * gamma + 1):
            assert csr_power(c, s_powers, r, t) == powers[t]
            csr_cells_checked += len(a) * len(a)
        row = {
            "matrix_id": matrix_id,
            "tags": tags,
            "dimension": len(a),
            "support_edge_count": sum(x is not NEG for rr in a for x in rr),
            "A": enc_matrix(a),
            "lambda": enc(lam),
            "B": enc_matrix(b),
            "simple_cycles": cycles,
            "critical_edges": [list(e) for e in sorted(critical_edges)],
            "critical_components": comp_rows,
            "gamma": gamma,
            "minimal_matrix_power_period": gamma,
            "minimal_transient": transient,
            "csr_transient": csr_transient,
            "C": enc_matrix(c),
            "S": enc_matrix(s),
            "R": enc_matrix(r),
            "power_at_transient": enc_matrix(powers[transient]),
            "power_one_period_later": enc_matrix(powers[transient + gamma]),
            "primitive": gamma == 1,
        }
        matrix_rows.append(row)
        total_cycles += len(cycles)
        critical_components_total += len(comp_rows)

        n = len(a)
        vectors: list[tuple[str, Vector]] = [("zero", tuple(Q(0) for _ in range(n)))]
        vectors += [
            (f"basis_{j}", tuple(Q(0) if i == j else NEG for i in range(n)))
            for j in range(n)
        ]
        vectors += [
            ("descending", tuple(Q(-i) for i in range(n))),
            ("fractional", tuple(Q(i, n + 1) for i in range(n))),
        ]
        for vector_id, x in vectors:
            vrow = classify_vector(b, powers, gamma, transient, vector_id, x)
            vrow["matrix_id"] = matrix_id
            vector_rows.append(vrow)

    transient_family = []
    for m in range(1, 25):
        b = ((Q(0), Q(-m)), (Q(0), Q(-1)))
        powers = powers_until(b, m + 2)
        t = least_transient(powers, 1)
        assert t == m
        assert powers[m - 1][1][1] == Q(-(m - 1))
        assert powers[m][1][1] == Q(-m)
        assert powers[m + 1][1][1] == Q(-m)
        transient_family.append({"m": m, "minimal_transient": t, "bottom_right_formula_at_t": "max(-t,-m)"})

    reducible = ((Q(0), NEG), (NEG, Q(1)))
    reducible_powers = powers_until(reducible, 5)
    reducible_boundary = {
        "A": enc_matrix(reducible),
        "component_growth_rates": ["0", "1"],
        "powers_t_1_to_5": [enc_matrix(reducible_powers[t]) for t in range(1, 6)],
        "conclusion": "NO_SINGLE_NORMALIZATION_MAKES_BOTH_DIAGONAL_COMPONENTS_PERIODIC",
    }

    theorem = {
        "cyclicity": "FOR_EVERY_IRREDUCIBLE_RATIONAL_MAX_PLUS_MATRIX_NORMALIZED_POWERS_HAVE_MINIMAL_ULTIMATE_PERIOD_GAMMA",
        "transient": "THE_MINIMAL_TRANSIENT_IS_THE_LEAST_T_WITH_B_POWER_T_PLUS_GAMMA_EQUAL_B_POWER_T",
        "propagation": "ONE_EQUALITY_PROPAGATES_TO_ALL_LATER_TIMES_BY_RIGHT_MAX_PLUS_MULTIPLICATION",
        "csr": "AFTER_A_MATRIX_DEPENDENT_TRANSIENT_B_POWER_T_EQUALS_C_TIMES_S_POWER_T_TIMES_R",
        "vectors": "EVERY_VECTOR_AND_PROJECTIVE_ORBIT_HAS_ULTIMATE_PERIOD_DIVIDING_GAMMA_AND_MAY_HAVE_A_STRICTLY_SMALLER_PERIOD",
        "attraction": "EXACT_PERIOD_P_IS_ATTR_P_MINUS_THE_UNION_OF_ATTR_Q_OVER_PROPER_DIVISORS_Q_OF_P",
        "ultimate_spans": "THE_COLUMN_CONES_OF_B_POWER_T_PLUS_R_REPEAT_WITH_R_MODULO_GAMMA_AND_CAPTURE_EVERY_EVENTUAL_ORBIT",
        "eigencone": "THE_NORMALIZED_EIGENCONE_BX_EQUALS_X_IS_CONTAINED_IN_THE_PERIOD_ONE_ATTRACTION_CONE",
        "primitive": "GAMMA_ONE_MEANS_EVENTUAL_CONSTANT_MATRIX_POWERS_NOT_TRANSIENT_ZERO",
        "unbounded_transient": "THE_FIXED_TWO_BY_TWO_SUPPORT_FAMILY_HAS_MINIMAL_TRANSIENT_M_SO_NO_DIMENSION_ONLY_WEIGHT_INDEPENDENT_BOUND_EXISTS",
        "reducible_boundary": "REDUCIBLE_MATRICES_CAN_HAVE_MULTIPLE_GROWTH_RATES_AND_MULTIPLE_CSR_TERMS",
    }
    route_a = {
        "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        "A0_qualification": "WEIGHTS_SUPPORT_AND_CYCLE_MEANS_HAVE_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
        "A1_qualification": "ULTIMATE_MAX_PLUS_PERIODS_ARE_EXACT_BUT_HAVE_NO_A0_ARITHMETIC_PAYLOAD",
        "A2_qualification": "CSR_AND_PERIODIC_POWERS_DO_NOT_IDENTIFY_A_TARGET_DIVISOR",
        "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_CONTINUATION_OR_WEIL_COMPRESSION",
        "A4_qualification": "MAX_PLUS_SEMIMODULE_DYNAMICS_SUPPLIES_NO_SOURCE_NATIVE_HILBERT_SPACE_QUANTIZATION",
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }
    payload = {
        "schema": "hcs-c188-evidence-v1",
        "candidate_id": "HCS-C188",
        "date_utc": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "evaluator": {
            "version": "0.2.0",
            "path": "flow_systems/skills/route-a-evaluator.md",
            "sha256": EVALUATOR_SHA256,
        },
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "semiring": "MAX_PLUS_RATIONAL_WITH_MINUS_INFINITY",
            "source_notation_translation": "LOG_ISOMORPHISM_FROM_MAX_TIMES_TO_MAX_PLUS_PRESERVES_SUPPORT_CRITICAL_CYCLES_AND_CYCLICITY",
            "family": "ALL_IRREDUCIBLE_SQUARE_MATRICES_WITH_STRONGLY_CONNECTED_FINITE_SUPPORT",
            "normalization": "B_EQUALS_A_MINUS_MAXIMUM_CYCLE_MEAN_LAMBDA",
            "critical_graph": "UNION_OF_ALL_CYCLES_ATTAINING_LAMBDA",
            "cyclicity": "LCM_OF_GCD_CYCLE_LENGTHS_OF_CRITICAL_STRONGLY_CONNECTED_COMPONENTS",
            "clock": "ONE_MAX_PLUS_MATRIX_MULTIPLICATION",
            "measure": "NONE_REQUIRED",
            "operator": "MAX_PLUS_LINEAR_SELF_MAP_ON_THE_TROPICAL_SEMIMODULE",
            "determinant_convention": "NONE",
            "cutoff": "ALL_PARAMETER_THEOREM_WITH_DECLARED_FINITE_CENSUS_REGRESSION",
            "allowed_data": "RATIONAL_WEIGHTS_SUPPORT_CYCLES_CRITICAL_GRAPH_POWERS_CSR_AND_TEST_VECTORS",
            "forbidden_data": "TARGET_ZERO_OR_PRIME_TABLES_ARITHMETIC_LOCAL_DATA_EULER_FACTORS_ROOT_NUMBERS_AUTOMORPHY_AND_ROUTE_B",
        },
        "attribution": {
            "status": "CLASSICAL_THEOREMS_SOURCE_LOCKED_PACKAGE_DERIVATIONS_ONLY",
            "cyclicity_owner": "SERGEEV_2009_AND_CLASSICAL_PREDECESSORS_AS_CITED_THERE",
            "csr_owner": "SERGEEV_AND_SCHNEIDER_2012",
            "package_increment": "ONE_SOURCE_LOCKED_ALL_PARAMETER_DYNAMICAL_CLASSIFICATION_WITH_EXECUTABLE_BOUNDARIES",
            "finite_evidence_role": "REGRESSION_ONLY_NOT_PROOF_OF_THE_ALL_MATRIX_THEOREMS",
        },
        "source_registry": [
            {
                "authors": ["Sergei Sergeev"],
                "title": "Max algebraic powers of irreducible matrices in the periodic regime: An application of cyclic classes",
                "journal": "Linear Algebra and its Applications",
                "volume": "431",
                "issue": "8",
                "year": 2009,
                "pages": "1325-1339",
                "doi": "10.1016/j.laa.2009.04.027",
                "arxiv": "0903.3960",
                "role": "CYCLICITY_ULTIMATE_PERIOD_ATTRACTION_CONES_AND_ULTIMATE_SPANS",
            },
            {
                "authors": ["Sergei Sergeev", "Hans Schneider"],
                "title": "CSR expansions of matrix powers in max algebra",
                "journal": "Transactions of the American Mathematical Society",
                "volume": "364",
                "issue": "11",
                "year": 2012,
                "pages": "5969-5994",
                "doi": "10.1090/S0002-9947-2012-05605-4",
                "arxiv": "0912.2534",
                "role": "CSR_EXPANSION_AND_REDUCIBLE_MULTIRATE_BOUNDARY",
            },
        ],
        "theorem": theorem,
        "finite_regression": {
            "matrix_count": len(matrix_rows),
            "matrix_rows": matrix_rows,
            "vector_row_count": len(vector_rows),
            "vector_rows": vector_rows,
            "simple_cycle_count": total_cycles,
            "critical_component_count": critical_components_total,
            "csr_cells_checked": csr_cells_checked,
            "propagation_cells_checked": propagation_cells_checked,
            "unbounded_transient_family": transient_family,
            "reducible_boundary": reducible_boundary,
        },
        "progress_and_boundary": {
            "progress": "A_SINGLE_ALL_IRREDUCIBLE_CLASSIFICATION_CONNECTS_CRITICAL_CYCLES_MATRIX_POWERS_CSR_VECTOR_PERIODS_ATTRACTION_CONES_AND_ULTIMATE_SPANS",
            "period_boundary": "MATRIX_PERIOD_IS_EXACTLY_GAMMA_BUT_INDIVIDUAL_VECTOR_AND_PROJECTIVE_PERIODS_CAN_BE_SMALLER",
            "transient_boundary": "TRANSIENT_IS_MATRIX_DEPENDENT_AND_UNBOUNDED_AT_FIXED_DIMENSION_AND_SUPPORT",
            "reducible_boundary": "REDUCIBILITY_INTRODUCES_MULTIPLE_GROWTH_RATES_AND_CSR_TERMS",
            "proof_boundary": "CLASSICAL_ALL_MATRIX_THEOREMS_ARE_CITED_FINITE_CENSUS_IS_REGRESSION_ONLY",
            "arithmetic_boundary": "NO_INTRINSIC_RATIONAL_PRIME_OR_TARGET_DIVISOR_SEMANTICS",
        },
        "route_a": route_a,
        "scope_flags": {
            "used_target_zero_table": False,
            "used_target_prime_table": False,
            "used_arithmetic_local_data": False,
            "claimed_target_divisor_match": False,
            "claimed_target_functional_equation": False,
            "claimed_global_novelty": False,
            "claimed_hilbert_polya": False,
            "claimed_uniform_transient": False,
            "claimed_all_vector_periods_equal_gamma": False,
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "PRIORITY_FOR_THE_CLASSICAL_CYCLICITY_THEOREM_OR_CSR_EXPANSION",
            "A_UNIFORM_DIMENSION_ONLY_WEIGHT_INDEPENDENT_TRANSIENT",
            "EVERY_VECTOR_OR_PROJECTIVE_ORBIT_HAS_EXACT_PERIOD_GAMMA",
            "ONE_GLOBAL_LINEAR_PERIOD_FOR_GENERAL_REDUCIBLE_MATRICES",
            "RATIONAL_PRIME_SEMANTICS_TARGET_DIVISOR_OR_FUNCTIONAL_EQUATION",
            "HILBERT_POLYA_OPERATOR_ROUTE_B_AUTHORIZATION_EXTERNAL_REVIEW_OR_ACCEPTANCE_SCORE",
        ],
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    payload["payload_sha256"] = sha256(raw).hexdigest()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C188_PRODUCER_PASS",
        "matrices": len(matrix_rows),
        "vectors": len(vector_rows),
        "cycles": total_cycles,
        "critical_components": critical_components_total,
        "csr_cells": csr_cells_checked,
        "propagation_cells": propagation_cells_checked,
        "payload_sha256": payload["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
