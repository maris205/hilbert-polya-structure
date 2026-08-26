#!/usr/bin/env python3
"""Independent C188 checker: Karp, closure-critical graph, SCC gcd, and binary powers."""
from __future__ import annotations

from fractions import Fraction
from functools import reduce
from hashlib import sha256
from itertools import permutations, product
import json
import math
from pathlib import Path
from typing import Optional


Q = Fraction
Entry = Optional[Fraction]
Matrix = tuple[tuple[Entry, ...], ...]
Vector = tuple[Entry, ...]
NEG: Entry = None
ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c188_max_plus_evidence.json"
SOURCE_COMMIT = "908a6818caedb0c46195a591873a2ac9c685b55e"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def dec(text: str) -> Entry:
    return NEG if text == "-inf" else Q(text)


def enc(x: Entry) -> str:
    if x is NEG:
        return "-inf"
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def matrix(raw: list[list[str]]) -> Matrix:
    return tuple(tuple(dec(x) for x in row) for row in raw)


def encoded(a: Matrix) -> list[list[str]]:
    return [[enc(x) for x in row] for row in a]


def identity(n: int) -> Matrix:
    return tuple(tuple(Q(0) if i == j else NEG for j in range(n)) for i in range(n))


def multiply(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return tuple(
        tuple(
            max((a[i][k] + b[k][j] for k in range(n) if a[i][k] is not NEG and b[k][j] is not NEG), default=NEG)
            for j in range(n)
        )
        for i in range(n)
    )


def matrix_max(a: Matrix, b: Matrix) -> Matrix:
    def join(x: Entry, y: Entry) -> Entry:
        if x is NEG:
            return y
        if y is NEG:
            return x
        return max(x, y)
    return tuple(tuple(join(x, y) for x, y in zip(rx, ry)) for rx, ry in zip(a, b))


def power(a: Matrix, exponent: int) -> Matrix:
    result = identity(len(a))
    base = a
    k = exponent
    while k:
        if k & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        k >>= 1
    return result


def apply(a: Matrix, x: Vector) -> Vector:
    return tuple(
        max((aij + xj for aij, xj in zip(row, x) if aij is not NEG and xj is not NEG), default=NEG)
        for row in a
    )


def projective(x: Vector) -> Vector:
    finite = [v for v in x if v is not NEG]
    if not finite:
        return x
    m = max(finite)
    return tuple(NEG if v is NEG else v - m for v in x)


def divs(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def strongly_connected(a: Matrix) -> bool:
    n = len(a)
    for transpose in (False, True):
        reached = {0}
        frontier = [0]
        while frontier:
            u = frontier.pop(0)
            neighbors = [v for v in range(n) if (a[v][u] if transpose else a[u][v]) is not NEG]
            for v in neighbors:
                if v not in reached:
                    reached.add(v)
                    frontier.append(v)
        if len(reached) != n:
            return False
    return True


def karp_lambda(a: Matrix) -> Fraction:
    n = len(a)
    dp: list[list[Entry]] = [[Q(0)] * n]
    for _ in range(n):
        next_row = []
        for v in range(n):
            vals = [dp[-1][u] + a[u][v] for u in range(n) if dp[-1][u] is not NEG and a[u][v] is not NEG]
            next_row.append(max(vals) if vals else NEG)
        dp.append(next_row)
    candidates = []
    for v in range(n):
        if dp[n][v] is NEG:
            continue
        ratios = [
            (dp[n][v] - dp[k][v]) / (n - k)
            for k in range(n)
            if dp[k][v] is not NEG
        ]
        candidates.append(min(ratios))
    return max(candidates)


def shifted(a: Matrix, lam: Fraction) -> Matrix:
    return tuple(tuple(NEG if x is NEG else x - lam for x in row) for row in a)


def kleene_truncated(b: Matrix, stride: int = 1) -> Matrix:
    n = len(b)
    q = power(b, stride)
    star = identity(n)
    term = identity(n)
    for _ in range(1, n):
        term = multiply(term, q)
        star = matrix_max(star, term)
    return star


def critical_edges_by_closure(b: Matrix) -> set[tuple[int, int]]:
    star = kleene_truncated(b)
    edges = set()
    for i, row in enumerate(b):
        for j, weight in enumerate(row):
            if weight is not NEG and star[j][i] is not NEG and weight + star[j][i] == 0:
                edges.add((i, j))
    return edges


def tarjan(nodes: set[int], edges: set[tuple[int, int]]) -> list[list[int]]:
    adjacency = {u: [] for u in nodes}
    for u, v in edges:
        adjacency[u].append(v)
    index = 0
    indices: dict[int, int] = {}
    low: dict[int, int] = {}
    stack: list[int] = []
    on_stack: set[int] = set()
    result: list[list[int]] = []

    def visit(v: int) -> None:
        nonlocal index
        indices[v] = low[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)
        for w in adjacency[v]:
            if w not in indices:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                comp.append(w)
                if w == v:
                    break
            result.append(sorted(comp))

    for node in sorted(nodes):
        if node not in indices:
            visit(node)
    return sorted(result)


def graph_cyclicity(comp: list[int], edges: set[tuple[int, int]]) -> int:
    comp_set = set(comp)
    adjacency = {u: [] for u in comp}
    for u, v in edges:
        if u in comp_set and v in comp_set:
            adjacency[u].append(v)
    root = comp[0]
    distance = {root: 0}
    queue = [root]
    while queue:
        u = queue.pop(0)
        for v in adjacency[u]:
            if v not in distance:
                distance[v] = distance[u] + 1
                queue.append(v)
    check(len(distance) == len(comp), "critical SCC reachability")
    g = 0
    for u in comp:
        for v in adjacency[u]:
            g = math.gcd(g, abs(distance[u] + 1 - distance[v]))
    return g


def cycles_by_permutations(a: Matrix) -> list[tuple[int, ...]]:
    n = len(a)
    found = []
    for length in range(1, n + 1):
        for cyc in permutations(range(n), length):
            if cyc[0] != min(cyc):
                continue
            if all(a[cyc[i]][cyc[(i + 1) % length]] is not NEG for i in range(length)):
                found.append(cyc)
    return sorted(found)


def cycle_rows(a: Matrix, lam: Fraction) -> list[dict]:
    result = []
    for cyc in cycles_by_permutations(a):
        weight = sum((a[cyc[i]][cyc[(i + 1) % len(cyc)]] for i in range(len(cyc))), Q(0))
        mean = weight / len(cyc)
        result.append({
            "nodes": list(cyc),
            "length": len(cyc),
            "weight": enc(weight),
            "mean": enc(mean),
            "critical": mean == lam,
        })
    return result


def csr(b: Matrix, edges: set[tuple[int, int]], gamma: int) -> tuple[Matrix, Matrix, Matrix]:
    n = len(b)
    star = kleene_truncated(b, gamma)
    nodes = {v for e in edges for v in e}
    c = tuple(tuple(star[i][j] if j in nodes else NEG for j in range(n)) for i in range(n))
    r = tuple(tuple(star[i][j] if i in nodes else NEG for j in range(n)) for i in range(n))
    s = tuple(tuple(b[i][j] if (i, j) in edges else NEG for j in range(n)) for i in range(n))
    return c, s, r


def catalog() -> list[tuple[str, Matrix]]:
    rows: list[tuple[str, Matrix]] = []
    seen = set()

    def register(name: str, a: Matrix) -> None:
        key = tuple(tuple(enc(x) for x in row) for row in a)
        if key not in seen:
            seen.add(key)
            rows.append((name, a))

    values = [NEG, Q(-1), Q(0), Q(1)]
    number = 0
    for flat in product(values, repeat=4):
        a = (tuple(flat[0:2]), tuple(flat[2:4]))
        if strongly_connected(a):
            register(f"grid2_{number:03d}", a)
            number += 1
    register("singleton_shift", ((Q(7, 3),),))
    for n in range(3, 7):
        register(f"pure_cycle_{n}", tuple(tuple(Q(0) if j == (i + 1) % n else NEG for j in range(n)) for i in range(n)))
    raw = [[NEG] * 5 for _ in range(5)]
    raw[0][1] = raw[1][0] = Q(0)
    raw[2][3] = raw[3][4] = raw[4][2] = Q(0)
    raw[1][2] = raw[4][0] = Q(-7)
    register("critical_scc_2_plus_3", tuple(tuple(row) for row in raw))
    for m in range(2, 25):
        register(f"unbounded_transient_m{m:02d}", ((Q(0), Q(-m)), (Q(0), Q(-1))))
    for denominator in range(2, 6):
        weights = [Q(1, denominator), Q(-1, denominator), Q(2, denominator)]
        n = 3
        register(
            f"rational_cycle_q{denominator}",
            tuple(tuple(weights[i] if j == (i + 1) % n else NEG for j in range(n)) for i in range(n)),
        )
    return rows


def expected_tags(matrix_id: str) -> list[str]:
    if matrix_id.startswith("grid2_"):
        return ["complete_two_by_two_grid"]
    if matrix_id == "singleton_shift":
        return ["dimension_one", "primitive"]
    if matrix_id.startswith("pure_cycle_"):
        return ["pure_cycle", "transient_zero"]
    if matrix_id == "critical_scc_2_plus_3":
        return ["multiple_critical_scc", "gamma_lcm_six"]
    if matrix_id.startswith("unbounded_transient_m"):
        m = int(matrix_id.rsplit("m", 1)[1])
        return ["fixed_support_transient_family", f"expected_transient_{m}"]
    if matrix_id.startswith("rational_cycle_q"):
        return ["rational_weights", "nonintegral_lambda"]
    raise AssertionError(f"unknown matrix id {matrix_id}")


def vector_expectations(b: Matrix, gamma: int, transient: int) -> list[dict]:
    n = len(b)
    vectors: list[tuple[str, Vector]] = [("zero", tuple(Q(0) for _ in range(n)))]
    vectors += [(f"basis_{j}", tuple(Q(0) if i == j else NEG for i in range(n))) for j in range(n)]
    vectors += [
        ("descending", tuple(Q(-i) for i in range(n))),
        ("fractional", tuple(Q(i, n + 1) for i in range(n))),
    ]
    result = []
    maximum = transient + gamma
    pows = [power(b, t) for t in range(maximum + 1)]
    for vector_id, x in vectors:
        states = [apply(p, x) for p in pows]
        projects = [projective(y) for y in states]
        raw_period = next(p for p in divs(gamma) if states[transient + p] == states[transient])
        proj_period = next(p for p in divs(gamma) if projects[transient + p] == projects[transient])
        raw_t = next(t for t in range(transient + 1) if states[t + raw_period] == states[t])
        proj_t = next(t for t in range(transient + 1) if projects[t + proj_period] == projects[t])
        result.append({
            "vector_id": vector_id,
            "x": [enc(v) for v in x],
            "eventual_period": raw_period,
            "eventual_transient": raw_t,
            "projective_period": proj_period,
            "projective_transient": proj_t,
            "attraction_divisors": [p for p in divs(gamma) if states[transient + p] == states[transient]],
            "projective_attraction_divisors": [p for p in divs(gamma) if projects[transient + p] == projects[transient]],
        })
    return result


def expected_theorem() -> dict:
    return {
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


def verify(data: dict) -> int:
    payload_hash = data.pop("payload_sha256", None)
    raw = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    check(payload_hash == sha256(raw).hexdigest(), "payload hash")
    data["payload_sha256"] = payload_hash
    check(data["schema"] == "hcs-c188-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C188", "candidate")
    check(data["date_utc"] == "2026-08-26", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["evaluator"] == {"version": "0.2.0", "path": "flow_systems/skills/route-a-evaluator.md", "sha256": EVALUATOR_SHA256}, "evaluator")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["source_lock"] == {
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
    }, "source lock exact map")
    check(data["attribution"] == {
        "status": "CLASSICAL_THEOREMS_SOURCE_LOCKED_PACKAGE_DERIVATIONS_ONLY",
        "cyclicity_owner": "SERGEEV_2009_AND_CLASSICAL_PREDECESSORS_AS_CITED_THERE",
        "csr_owner": "SERGEEV_AND_SCHNEIDER_2012",
        "package_increment": "ONE_SOURCE_LOCKED_ALL_PARAMETER_DYNAMICAL_CLASSIFICATION_WITH_EXECUTABLE_BOUNDARIES",
        "finite_evidence_role": "REGRESSION_ONLY_NOT_PROOF_OF_THE_ALL_MATRIX_THEOREMS",
    }, "attribution exact map")
    check(data["theorem"] == expected_theorem(), "theorem exact map")
    check(data["route_a"] == {
        "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        "A0_qualification": "WEIGHTS_SUPPORT_AND_CYCLE_MEANS_HAVE_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
        "A1_qualification": "ULTIMATE_MAX_PLUS_PERIODS_ARE_EXACT_BUT_HAVE_NO_A0_ARITHMETIC_PAYLOAD",
        "A2_qualification": "CSR_AND_PERIODIC_POWERS_DO_NOT_IDENTIFY_A_TARGET_DIVISOR",
        "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_CONTINUATION_OR_WEIL_COMPRESSION",
        "A4_qualification": "MAX_PLUS_SEMIMODULE_DYNAMICS_SUPPLIES_NO_SOURCE_NATIVE_HILBERT_SPACE_QUANTIZATION",
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }, "route exact map")
    check(data["scope_flags"] == {
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
    }, "scope flags exact map")
    check(data["nonclaims"] == [
        "PRIORITY_FOR_THE_CLASSICAL_CYCLICITY_THEOREM_OR_CSR_EXPANSION",
        "A_UNIFORM_DIMENSION_ONLY_WEIGHT_INDEPENDENT_TRANSIENT",
        "EVERY_VECTOR_OR_PROJECTIVE_ORBIT_HAS_EXACT_PERIOD_GAMMA",
        "ONE_GLOBAL_LINEAR_PERIOD_FOR_GENERAL_REDUCIBLE_MATRICES",
        "RATIONAL_PRIME_SEMANTICS_TARGET_DIVISOR_OR_FUNCTIONAL_EQUATION",
        "HILBERT_POLYA_OPERATOR_ROUTE_B_AUTHORIZATION_EXTERNAL_REVIEW_OR_ACCEPTANCE_SCORE",
    ], "nonclaims")
    sources = data["source_registry"]
    check(len(sources) == 2, "two sources")
    check(sources[0] == {
        "authors": ["Sergei Sergeev"],
        "title": "Max algebraic powers of irreducible matrices in the periodic regime: An application of cyclic classes",
        "journal": "Linear Algebra and its Applications",
        "volume": "431", "issue": "8", "year": 2009, "pages": "1325-1339",
        "doi": "10.1016/j.laa.2009.04.027", "arxiv": "0903.3960",
        "role": "CYCLICITY_ULTIMATE_PERIOD_ATTRACTION_CONES_AND_ULTIMATE_SPANS",
    }, "source one")
    check(sources[1] == {
        "authors": ["Sergei Sergeev", "Hans Schneider"],
        "title": "CSR expansions of matrix powers in max algebra",
        "journal": "Transactions of the American Mathematical Society",
        "volume": "364", "issue": "11", "year": 2012, "pages": "5969-5994",
        "doi": "10.1090/S0002-9947-2012-05605-4", "arxiv": "0912.2534",
        "role": "CSR_EXPANSION_AND_REDUCIBLE_MULTIRATE_BOUNDARY",
    }, "source two")

    finite = data["finite_regression"]
    expected_catalog = catalog()
    check(finite["matrix_count"] == len(expected_catalog) == 177, "matrix count")
    check(len(finite["matrix_rows"]) == len(expected_catalog), "matrix rows")
    vector_cursor = 0
    cycle_total = 0
    component_total = 0
    csr_cells = 0
    propagation_cells = 0
    for (matrix_id, expected_a), row in zip(expected_catalog, finite["matrix_rows"]):
        check(row["matrix_id"] == matrix_id, f"id {matrix_id}")
        a = matrix(row["A"])
        check(a == expected_a, f"catalog matrix {matrix_id}")
        check(row["tags"] == expected_tags(matrix_id), f"tags {matrix_id}")
        check(row["dimension"] == len(a), f"dimension {matrix_id}")
        check(row["support_edge_count"] == sum(x is not NEG for rr in a for x in rr), f"support count {matrix_id}")
        check(strongly_connected(a), f"irreducible {matrix_id}")
        lam = karp_lambda(a)
        check(row["lambda"] == enc(lam), f"Karp lambda {matrix_id}")
        b = shifted(a, lam)
        check(row["B"] == encoded(b), f"normalization {matrix_id}")
        expected_cycles = cycle_rows(a, lam)
        check(row["simple_cycles"] == expected_cycles, f"cycle ledger {matrix_id}")
        cycle_total += len(expected_cycles)
        edges = critical_edges_by_closure(b)
        check(row["critical_edges"] == [list(e) for e in sorted(edges)], f"critical edges {matrix_id}")
        nodes = {v for e in edges for v in e}
        comps = tarjan(nodes, edges)
        comp_rows = [{"nodes": comp, "cyclicity": graph_cyclicity(comp, edges)} for comp in comps]
        check(row["critical_components"] == comp_rows, f"critical components {matrix_id}")
        component_total += len(comp_rows)
        gamma = reduce(math.lcm, (item["cyclicity"] for item in comp_rows), 1)
        check(row["gamma"] == gamma, f"gamma {matrix_id}")
        check(row["minimal_matrix_power_period"] == gamma, f"minimal period field {matrix_id}")
        transient = row["minimal_transient"]
        check(power(b, transient + gamma) == power(b, transient), f"transient equality {matrix_id}")
        for t in range(transient):
            check(power(b, t + gamma) != power(b, t), f"minimal transient {matrix_id}:{t}")
        for p in range(1, gamma):
            check(power(b, transient + p) != power(b, transient), f"minimal ultimate period {matrix_id}:{p}")
        for t in range(transient, transient + 3 * gamma + len(a) + 1):
            check(power(b, t + gamma) == power(b, t), f"propagation {matrix_id}:{t}")
            propagation_cells += len(a) * len(a)
        check(row["power_at_transient"] == encoded(power(b, transient)), f"power T {matrix_id}")
        check(row["power_one_period_later"] == encoded(power(b, transient + gamma)), f"power T+g {matrix_id}")
        c, s, r = csr(b, edges, gamma)
        check(row["C"] == encoded(c) and row["S"] == encoded(s) and row["R"] == encoded(r), f"CSR matrices {matrix_id}")
        csr_t = row["csr_transient"]
        for t in range(csr_t, csr_t + 3 * gamma + 1):
            check(multiply(multiply(c, power(s, t)), r) == power(b, t), f"CSR equality {matrix_id}:{t}")
            csr_cells += len(a) * len(a)
        for t in range(csr_t):
            matches = all(multiply(multiply(c, power(s, u)), r) == power(b, u) for u in range(t, t + 2 * gamma))
            check(not matches, f"minimal CSR transient {matrix_id}:{t}")
        check(row["primitive"] is (gamma == 1), f"primitive {matrix_id}")
        expectations = vector_expectations(b, gamma, transient)
        selected = finite["vector_rows"][vector_cursor:vector_cursor + len(expectations)]
        check(len(selected) == len(expectations), f"vector slice {matrix_id}")
        for got, expected in zip(selected, expectations):
            expected["matrix_id"] = matrix_id
            check(got == expected, f"vector classification {matrix_id}:{expected['vector_id']}")
        vector_cursor += len(expectations)

    check(vector_cursor == finite["vector_row_count"] == len(finite["vector_rows"]) == 901, "vector total")
    check(finite["simple_cycle_count"] == cycle_total == 441, "cycle total")
    check(finite["critical_component_count"] == component_total == 189, "component total")
    check(finite["csr_cells_checked"] == csr_cells == 5469, "CSR cells")
    check(finite["propagation_cells_checked"] == propagation_cells == 7471, "propagation cells")
    family = finite["unbounded_transient_family"]
    check(len(family) == 24, "transient family length")
    for m, item in enumerate(family, 1):
        b = ((Q(0), Q(-m)), (Q(0), Q(-1)))
        least = next(t for t in range(m + 1) if power(b, t + 1) == power(b, t))
        check(item == {"m": m, "minimal_transient": least, "bottom_right_formula_at_t": "max(-t,-m)"}, f"unbounded family {m}")
        check(least == m, f"unbounded exact {m}")
    reducible = finite["reducible_boundary"]
    red = ((Q(0), NEG), (NEG, Q(1)))
    check(reducible == {
        "A": encoded(red),
        "component_growth_rates": ["0", "1"],
        "powers_t_1_to_5": [encoded(power(red, t)) for t in range(1, 6)],
        "conclusion": "NO_SINGLE_NORMALIZATION_MAKES_BOTH_DIAGONAL_COMPONENTS_PERIODIC",
    }, "reducible boundary")
    check(data["progress_and_boundary"] == {
        "progress": "A_SINGLE_ALL_IRREDUCIBLE_CLASSIFICATION_CONNECTS_CRITICAL_CYCLES_MATRIX_POWERS_CSR_VECTOR_PERIODS_ATTRACTION_CONES_AND_ULTIMATE_SPANS",
        "period_boundary": "MATRIX_PERIOD_IS_EXACTLY_GAMMA_BUT_INDIVIDUAL_VECTOR_AND_PROJECTIVE_PERIODS_CAN_BE_SMALLER",
        "transient_boundary": "TRANSIENT_IS_MATRIX_DEPENDENT_AND_UNBOUNDED_AT_FIXED_DIMENSION_AND_SUPPORT",
        "reducible_boundary": "REDUCIBILITY_INTRODUCES_MULTIPLE_GROWTH_RATES_AND_CSR_TERMS",
        "proof_boundary": "CLASSICAL_ALL_MATRIX_THEOREMS_ARE_CITED_FINITE_CENSUS_IS_REGRESSION_ONLY",
        "arithmetic_boundary": "NO_INTRINSIC_RATIONAL_PRIME_OR_TARGET_DIVISOR_SEMANTICS",
    }, "progress boundary exact map")
    return ASSERTIONS


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assertions = verify(data)
    print(json.dumps({
        "status": "C188_CHECKER_PASS",
        "assertions": assertions,
        "matrices": data["finite_regression"]["matrix_count"],
        "vectors": data["finite_regression"]["vector_row_count"],
        "method": "KARP_CLOSURE_TARJAN_GCD_BINARY_POWERS",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
