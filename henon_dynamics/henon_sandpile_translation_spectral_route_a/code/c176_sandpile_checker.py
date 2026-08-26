#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C176."""
from __future__ import annotations

from hashlib import sha256
from itertools import permutations, product
import json
from math import gcd
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c176_sandpile_evidence.json"
checks = 0


def require(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def edge_pairs(n: int) -> list[tuple[int, int]]:
    return [(u, v) for u in range(n) for v in range(u + 1, n)]


def code_for(n: int, edges: set[tuple[int, int]]) -> str:
    return "".join("1" if edge in edges else "0" for edge in edge_pairs(n))


def canonical(n: int, edges: tuple[tuple[int, int], ...]) -> str:
    codes = []
    for permutation in permutations(range(n)):
        relabelled = {
            tuple(sorted((permutation[u], permutation[v])))
            for u, v in edges
        }
        codes.append(code_for(n, relabelled))
    return min(codes)


def is_connected(n: int, edges: tuple[tuple[int, int], ...]) -> bool:
    adjacency = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    reached = {0}
    frontier = {0}
    while frontier:
        frontier = set().union(*(adjacency[v] for v in frontier)) - reached
        reached |= frontier
    return len(reached) == n


def degree_list(n: int, edges: tuple[tuple[int, int], ...]) -> list[int]:
    return [sum(v in edge for edge in edges) for v in range(n)]


def laplacian(n: int, edges: tuple[tuple[int, int], ...], sink: int) -> tuple[list[int], list[list[int]]]:
    vertices = [v for v in range(n) if v != sink]
    index = {v: i for i, v in enumerate(vertices)}
    degrees = degree_list(n, edges)
    matrix = [[degrees[v] if v == w else 0 for w in vertices] for v in vertices]
    for u, v in edges:
        if u != sink and v != sink:
            matrix[index[u]][index[v]] -= 1
            matrix[index[v]][index[u]] -= 1
    return vertices, matrix


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def det_leibniz(matrix: list[list[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    return sum(
        permutation_sign(permutation)
        * product_value([matrix[i][permutation[i]] for i in range(n)])
        for permutation in permutations(range(n))
    )


def product_value(values: list[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def matrix_minor(matrix: list[list[int]], removed_row: int, removed_column: int) -> list[list[int]]:
    return [
        [entry for column, entry in enumerate(row) if column != removed_column]
        for row_index, row in enumerate(matrix) if row_index != removed_row
    ]


def adj(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    return [
        [((-1) ** (i + j)) * det_leibniz(matrix_minor(matrix, j, i)) for j in range(n)]
        for i in range(n)
    ]


def multiply(matrix: list[list[int]], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(row[i] * vector[i] for i in range(len(vector))) for row in matrix)


def stable_configurations(degrees: list[int], vertices: list[int]) -> list[tuple[int, ...]]:
    return list(product(*(range(degrees[v]) for v in vertices)))


def burning_test(
    state: tuple[int, ...],
    edges: tuple[tuple[int, int], ...],
    vertices: list[int],
) -> bool:
    """Independent Dhar implementation: burn every currently eligible vertex."""
    index = {v: i for i, v in enumerate(vertices)}
    unburned = set(vertices)
    while unburned:
        eligible = {
            v for v in unburned
            if state[index[v]] >= sum(
                v in edge and (edge[1] if edge[0] == v else edge[0]) in unburned
                for edge in edges
            )
        }
        if not eligible:
            return False
        unburned -= eligible
    return True


def stabilize(
    state: tuple[int, ...],
    addition: tuple[int, ...],
    n: int,
    edges: tuple[tuple[int, int], ...],
    sink: int,
    vertices: list[int],
    reverse_choice: bool,
) -> tuple[int, ...]:
    index = {v: i for i, v in enumerate(vertices)}
    degrees = degree_list(n, edges)
    heights = [state[i] + addition[i] for i in range(len(vertices))]
    ordered = list(reversed(vertices)) if reverse_choice else vertices
    topplings = 0
    while True:
        unstable = next((v for v in ordered if heights[index[v]] >= degrees[v]), None)
        if unstable is None:
            return tuple(heights)
        heights[index[unstable]] -= degrees[unstable]
        for u, v in edges:
            if u == unstable and v != sink:
                heights[index[v]] += 1
            elif v == unstable and u != sink:
                heights[index[u]] += 1
        topplings += 1
        if topplings > 100000:
            raise AssertionError("stabilization did not terminate")


def signature(state: tuple[int, ...], adjugate: list[list[int]], D: int) -> tuple[int, ...]:
    return tuple(value % D for value in multiply(adjugate, state))


def cycles(mapping: dict[tuple[int, ...], tuple[int, ...]]) -> list[int]:
    remaining = set(mapping)
    lengths = []
    while remaining:
        start = min(remaining)
        current = start
        length = 0
        while current in remaining:
            remaining.remove(current)
            current = mapping[current]
            length += 1
        require(current == start, "mapping cycle closure")
        lengths.append(length)
    return sorted(lengths)


def expected_sources(vertices: list[int]) -> list[tuple[str, tuple[int, ...]]]:
    r = len(vertices)
    sources = [("zero", (0,) * r)]
    for i, vertex in enumerate(vertices):
        sources.append((f"unit_at_vertex_{vertex}", tuple(int(j == i) for j in range(r))))
    sources.append(("all_ones", (1,) * r))
    return sources


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    body = dict(data)
    claimed_hash = body.pop("payload_sha256")
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    require(sha256(encoded).hexdigest() == claimed_hash, "payload hash")
    require(set(data) == {
        "schema", "candidate_id", "date_utc", "source_commit", "scope_literal",
        "source_lock", "recurrent_bridge_theorem", "order_theorem",
        "orbit_spectral_theorem", "stable_state_boundary", "finite_replay",
        "progress_and_boundary", "route_a", "scope_flags", "nonclaims",
        "payload_sha256",
    }, "top-level closure")
    require(data["schema"] == "HCS-C176-v1", "schema")
    require(data["candidate_id"] == "HCS-C176", "candidate")
    require(data["date_utc"] == "2026-08-26", "date")
    require(data["source_commit"] == "100e5f601a0196710d53784bdeef40d2bff89fa8", "source commit")
    require(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    lock = data["source_lock"]
    require(set(lock) == {
        "object", "family", "arithmetic_origin", "clock", "normalization",
        "determinant_convention", "cutoff", "precision", "allowed_data", "forbidden_data",
    }, "lock closure")
    require("connected undirected loopless multigraph" in lock["object"] and "designated sink" in lock["object"], "object")
    require("every such graph" in lock["family"] and "nonnegative chip vector" in lock["family"], "family")
    require(lock["clock"] == "one application T_b(eta)=stabilize(eta+b)", "clock")
    require("reduced Laplacian" in lock["normalization"] and "recurrent" in lock["normalization"], "normalization")
    require("Artin--Mazur" in lock["determinant_convention"] and "restricted to the recurrent set" in lock["determinant_convention"], "determinant convention")
    require("all 30 connected isomorphism types" in lock["cutoff"] and "2<=|V|<=5" in lock["cutoff"], "cutoff")
    require("no intrinsic rational-prime" in lock["arithmetic_origin"], "arithmetic origin")
    require("target zero or prime tables" in lock["forbidden_data"] and "Route-B" in lock["forbidden_data"], "forbidden data")

    bridge = data["recurrent_bridge_theorem"]
    require(set(bridge) == {"critical_group", "representatives", "translation", "scope"}, "bridge closure")
    require("K(G,s)=Z^" in bridge["critical_group"] and "D=det(Delta)" in bridge["critical_group"], "critical group")
    require("unique recurrent stable representative" in bridge["representatives"] and "torsor" in bridge["representatives"], "representatives")
    require("translation by [b]" in bridge["translation"], "translation")
    require("does not identify all stable configurations" in bridge["scope"], "bridge scope")

    order_theorem = data["order_theorem"]
    require(set(order_theorem) == {"definition", "smith", "adjugate", "zero_source", "sink_only"}, "order closure")
    require("min{ell>=1" in order_theorem["definition"] and "Delta Z^" in order_theorem["definition"], "order definition")
    require("U*Delta*V=diag(d_i)" in order_theorem["smith"] and "lcm_i" in order_theorem["smith"], "Smith formula")
    require("adj(Delta)*b" in order_theorem["adjugate"] and "D/gcd" in order_theorem["adjugate"], "adjugate formula")
    require(order_theorem["zero_source"] == "b=0 has L=1", "zero source")
    require("r=0" in order_theorem["sink_only"] and "D=L=1" in order_theorem["sink_only"], "sink-only edge")

    orbit_theorem = data["orbit_spectral_theorem"]
    require(set(orbit_theorem) == {"cycles", "fixed_counts", "zeta", "determinant", "spectrum", "reversal", "self_adjoint"}, "orbit theorem closure")
    require("exact length L" in orbit_theorem["cycles"] and "D/L" in orbit_theorem["cycles"], "cycles theorem")
    require("D if L divides n" in orbit_theorem["fixed_counts"], "fixed theorem")
    require("(1-z^L)^(-D/L)" in orbit_theorem["zeta"], "zeta theorem")
    require("(1-z^L)^(D/L)" in orbit_theorem["determinant"], "determinant theorem")
    require("L-th root" in orbit_theorem["spectrum"] and "multiplicity D/L" in orbit_theorem["spectrum"], "spectrum theorem")
    require("R*T_b*R=T_b^(-1)" in orbit_theorem["reversal"] and "antiunitary" in orbit_theorem["reversal"], "reversal theorem")
    require("if and only if L<=2" in orbit_theorem["self_adjoint"], "self-adjoint theorem")

    replay = data["finite_replay"]
    require(set(replay) == {
        "vertex_max", "graph_rows", "sink_rows", "translation_rows",
        "graph_count_by_vertex_order", "graph_row_count", "sink_row_count",
        "translation_case_count", "fixed_count_row_count",
        "full_stable_noninjective_case_count", "stable_transition_checks",
        "recurrent_transition_checks", "fixed_count_state_checks",
    }, "replay closure")
    require(replay["vertex_max"] == 5, "vertex max")
    require(replay["graph_count_by_vertex_order"] == {"2": 1, "3": 2, "4": 6, "5": 21}, "graph spectrum")
    require(replay["graph_row_count"] == len(replay["graph_rows"]) == 30, "graph count")
    require(replay["sink_row_count"] == len(replay["sink_rows"]) == 137, "sink count")
    require(replay["translation_case_count"] == len(replay["translation_rows"]) == 780, "translation count")
    require(replay["fixed_count_row_count"] == sum(len(row["fixed_counts"]) for row in replay["translation_rows"]) == 8704, "fixed row count")
    require(replay["full_stable_noninjective_case_count"] == sum(not row["full_stable_injective"] for row in replay["translation_rows"]) == 610, "noninjective case count")
    require(replay["stable_transition_checks"] == 32938, "stable transition metric")
    require(replay["recurrent_transition_checks"] == 13764, "recurrent transition metric")
    require(replay["fixed_count_state_checks"] == 212504, "fixed count metric")

    graph_rows = {row["graph_id"]: row for row in replay["graph_rows"]}
    sink_rows = {(row["graph_id"], row["sink"]): row for row in replay["sink_rows"]}
    translation_rows = {
        (row["graph_id"], row["sink"], row["source_label"]): row
        for row in replay["translation_rows"]
    }
    require(len(graph_rows) == 30 and len(sink_rows) == 137 and len(translation_rows) == 780, "unique keys")

    stable_checks = 0
    recurrent_checks = 0
    fixed_state_checks = 0
    observed_codes = set()
    order_counts = {2: 0, 3: 0, 4: 0, 5: 0}
    for graph_id, graph_row in graph_rows.items():
        require(set(graph_row) == {"graph_id", "vertex_count", "canonical_upper_triangle_code", "edges"}, f"graph closure {graph_id}")
        n = graph_row["vertex_count"]
        edges = tuple(tuple(edge) for edge in graph_row["edges"])
        code = graph_row["canonical_upper_triangle_code"]
        require(graph_id == f"n{n}-{code}", f"graph id {graph_id}")
        require(all(0 <= u < v < n for u, v in edges), f"edge normalization {graph_id}")
        require(len(set(edges)) == len(edges), f"simple edge uniqueness {graph_id}")
        require(is_connected(n, edges), f"connected {graph_id}")
        require(code == code_for(n, set(edges)) == canonical(n, edges), f"canonical code {graph_id}")
        require((n, code) not in observed_codes, f"duplicate graph {graph_id}")
        observed_codes.add((n, code))
        order_counts[n] += 1
        degrees = degree_list(n, edges)

        for sink in range(n):
            vertices, delta = laplacian(n, edges, sink)
            D = det_leibniz(delta)
            adjugate = adj(delta)
            require(D > 0, f"positive determinant {graph_id} sink={sink}")
            # Verify Delta*adj(Delta)=D*I directly.
            for i in range(len(vertices)):
                for j in range(len(vertices)):
                    value = sum(delta[i][q] * adjugate[q][j] for q in range(len(vertices)))
                    require(value == (D if i == j else 0), f"adjugate identity {graph_id} sink={sink} {i},{j}")

            stable = stable_configurations(degrees, vertices)
            recurrent = [state for state in stable if burning_test(state, edges, vertices)]
            require(len(recurrent) == D, f"recurrent determinant {graph_id} sink={sink}")
            signatures = {signature(state, adjugate, D): state for state in recurrent}
            require(len(signatures) == D, f"unique recurrent class representatives {graph_id} sink={sink}")
            sink_row = sink_rows[(graph_id, sink)]
            require(set(sink_row) == {
                "graph_id", "sink", "non_sink_vertices", "vertex_degrees",
                "reduced_laplacian", "determinant_D", "stable_state_count",
                "recurrent_state_count",
            }, f"sink closure {graph_id} sink={sink}")
            require(sink_row["non_sink_vertices"] == vertices, f"vertices {graph_id} sink={sink}")
            require(sink_row["vertex_degrees"] == degrees, f"degrees {graph_id} sink={sink}")
            require(sink_row["reduced_laplacian"] == delta, f"Laplacian {graph_id} sink={sink}")
            require(sink_row["determinant_D"] == D, f"D {graph_id} sink={sink}")
            require(sink_row["stable_state_count"] == len(stable), f"stable count {graph_id} sink={sink}")
            require(sink_row["recurrent_state_count"] == D, f"recurrent count {graph_id} sink={sink}")

            for label, b in expected_sources(vertices):
                row = translation_rows[(graph_id, sink, label)]
                require(set(row) == {
                    "graph_id", "sink", "source_label", "b", "adjugate_times_b",
                    "order_L", "recurrent_state_count_D", "recurrent_cycle_count",
                    "observed_cycle_lengths", "full_stable_state_count",
                    "full_stable_image_size", "full_stable_injective", "fixed_counts",
                }, f"translation closure {graph_id} sink={sink} source={label}")
                require(tuple(row["b"]) == b, f"source vector {graph_id} sink={sink} source={label}")
                w = multiply(adjugate, b)
                require(tuple(row["adjugate_times_b"]) == w, f"adj*b {graph_id} sink={sink} source={label}")
                common = D
                for value in w:
                    common = gcd(common, abs(value))
                L = D // common
                require(row["order_L"] == L, f"adj order {graph_id} sink={sink} source={label}")
                direct_order = next(
                    ell for ell in range(1, D + 1)
                    if all((ell * value) % D == 0 for value in w)
                )
                require(direct_order == L, f"minimal order {graph_id} sink={sink} source={label}")

                recurrent_map = {}
                for state in recurrent:
                    low = stabilize(state, b, n, edges, sink, vertices, False)
                    high = stabilize(state, b, n, edges, sink, vertices, True)
                    require(low == high, f"toppling-order independence recurrent {graph_id} sink={sink} source={label} state={state}")
                    require(high in signatures.values(), f"recurrent invariance {graph_id} sink={sink} source={label} state={state}")
                    source_signature = tuple(value % D for value in w)
                    expected_signature = tuple(
                        (a + c) % D
                        for a, c in zip(signature(state, adjugate, D), source_signature)
                    )
                    require(signature(high, adjugate, D) == expected_signature, f"torsor translation {graph_id} sink={sink} source={label} state={state}")
                    recurrent_map[state] = high
                    recurrent_checks += 1
                require(set(recurrent_map.values()) == set(recurrent), f"recurrent permutation {graph_id} sink={sink} source={label}")
                lengths = cycles(recurrent_map)
                require(lengths == row["observed_cycle_lengths"], f"cycle ledger {graph_id} sink={sink} source={label}")
                require(set(lengths) == {L}, f"uniform cycles {graph_id} sink={sink} source={label}")
                require(row["recurrent_state_count_D"] == D, f"row D {graph_id} sink={sink} source={label}")
                require(row["recurrent_cycle_count"] == len(lengths) == D // L, f"cycle count {graph_id} sink={sink} source={label}")

                inverse_map = {value: key for key, value in recurrent_map.items()}
                inverse_state = {
                    state: signatures[tuple((-value) % D for value in signature(state, adjugate, D))]
                    for state in recurrent
                }
                for state in recurrent:
                    reversed_step = inverse_state[recurrent_map[inverse_state[state]]]
                    require(reversed_step == inverse_map[state], f"group inversion reversor {graph_id} sink={sink} source={label} state={state}")
                square_identity = all(recurrent_map[recurrent_map[state]] == state for state in recurrent)
                require(square_identity == (L <= 2), f"self-adjoint boundary {graph_id} sink={sink} source={label}")

                full_map = {}
                for state in stable:
                    low = stabilize(state, b, n, edges, sink, vertices, False)
                    high = stabilize(state, b, n, edges, sink, vertices, True)
                    require(low == high, f"toppling-order independence stable {graph_id} sink={sink} source={label} state={state}")
                    full_map[state] = high
                    stable_checks += 1
                image_size = len(set(full_map.values()))
                require(row["full_stable_state_count"] == len(stable), f"full state count {graph_id} sink={sink} source={label}")
                require(row["full_stable_image_size"] == image_size, f"full image size {graph_id} sink={sink} source={label}")
                require(row["full_stable_injective"] == (image_size == len(stable)), f"full injectivity {graph_id} sink={sink} source={label}")

                current = {state: state for state in recurrent}
                require(len(row["fixed_counts"]) == 2 * L + 2, f"fixed row length {graph_id} sink={sink} source={label}")
                for n_iterate, fixed_row in enumerate(row["fixed_counts"], 1):
                    current = {state: recurrent_map[image] for state, image in current.items()}
                    observed = sum(state == image for state, image in current.items())
                    formula = D if n_iterate % L == 0 else 0
                    require(set(fixed_row) == {"n", "fixed_count_formula", "fixed_count_enumerated"}, f"fixed closure {graph_id} sink={sink} source={label} n={n_iterate}")
                    require(fixed_row["n"] == n_iterate, f"fixed n {graph_id} sink={sink} source={label}")
                    require(fixed_row["fixed_count_formula"] == fixed_row["fixed_count_enumerated"] == observed == formula, f"fixed count {graph_id} sink={sink} source={label} n={n_iterate}")
                    fixed_state_checks += len(recurrent)

    require(order_counts == {2: 1, 3: 2, 4: 6, 5: 21}, "independent graph counts")
    require(stable_checks == replay["stable_transition_checks"], "stable metric replay")
    require(recurrent_checks == replay["recurrent_transition_checks"], "recurrent metric replay")
    require(fixed_state_checks == replay["fixed_count_state_checks"], "fixed metric replay")

    # Explicit full-stable-state counterexample.
    path_edges = ((0, 1), (1, 2))
    vertices, _ = laplacian(3, path_edges, 2)
    path_stable = stable_configurations(degree_list(3, path_edges), vertices)
    path_map = {state: stabilize(state, (1, 0), 3, path_edges, 2, vertices, True) for state in path_stable}
    require(path_stable == [(0, 0), (0, 1)], "path stable states")
    require(path_map == {(0, 0): (0, 1), (0, 1): (0, 1)}, "path collapse")
    require([state for state in path_stable if burning_test(state, path_edges, vertices)] == [(0, 1)], "path recurrent singleton")

    boundary = data["stable_state_boundary"]
    require(set(boundary) == {"warning", "counterexample", "nonclaim"}, "boundary closure")
    require("need not be injective or unitary" in boundary["warning"], "stable warning")
    require("path 0-1-2" in boundary["counterexample"] and "both stable states" in boundary["counterexample"], "counterexample text")
    require("no all-stable-state cycle classification" in boundary["nonclaim"], "boundary nonclaim")

    # Empty non-sink set convention is algebraically closed.
    require(det_leibniz([]) == 1 and adj([]) == [], "empty matrix convention")
    require(data["order_theorem"]["sink_only"].startswith("if r=0"), "r=0 declaration")

    route = data["route_a"]
    require(set(route) == {"tuple", "overall", "A0_qualification", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route closure")
    require(route["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "route tuple")
    require(route["overall"] == "ROUTE_A_REJECTED", "overall")
    require(route["A1_qualification"] == "COMPLETE_INTRINSIC_RECURRENT_PRIMITIVE_CYCLES_WITHOUT_ARITHMETIC_INFORMATION", "A1 qualification")
    require("RECURRENT_TRANSLATION_PERMUTATION" in route["A4_qualification"] and "INVERSION_REVERSAL" in route["A4_qualification"], "A4 qualification")
    require(route["route_b_invocation_allowed"] is False, "Route B")
    require(not any(data["scope_flags"].values()), "scope flags")
    require(len(data["nonclaims"]) == 5, "nonclaims")
    joined = " ".join(data["nonclaims"])
    require("novelty" in joined and "root numbers" in joined and "external peer review" in joined, "nonclaim boundary")
    print(json.dumps({"status": "C176_INDEPENDENT_CHECK_PASS", "assertions": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
