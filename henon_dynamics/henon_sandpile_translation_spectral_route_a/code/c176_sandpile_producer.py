#!/usr/bin/env python3
"""Produce the exact HCS-C176 recurrent sandpile translation certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import permutations, product
import json
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c176_sandpile_evidence.json"
SOURCE_COMMIT = "100e5f601a0196710d53784bdeef40d2bff89fa8"
VERTEX_MAX = 5


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def pairs(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def connected(n: int, edges: tuple[tuple[int, int], ...]) -> bool:
    adjacency = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adjacency[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n


def edge_bits(n: int, edges: set[tuple[int, int]]) -> str:
    return "".join("1" if edge in edges else "0" for edge in pairs(n))


def canonical_code(n: int, edges: tuple[tuple[int, int], ...]) -> str:
    best: str | None = None
    for perm in permutations(range(n)):
        mapped = {
            tuple(sorted((perm[u], perm[v])))
            for u, v in edges
        }
        code = edge_bits(n, mapped)
        if best is None or code < best:
            best = code
    assert best is not None
    return best


def decode_edges(n: int, code: str) -> tuple[tuple[int, int], ...]:
    return tuple(edge for edge, bit in zip(pairs(n), code) if bit == "1")


def graph_representatives() -> list[tuple[int, str, tuple[tuple[int, int], ...]]]:
    reps = {}
    for n in range(2, VERTEX_MAX + 1):
        edge_list = pairs(n)
        for mask in range(1 << len(edge_list)):
            edges = tuple(edge_list[i] for i in range(len(edge_list)) if mask & (1 << i))
            if not connected(n, edges):
                continue
            code = canonical_code(n, edges)
            reps[(n, code)] = decode_edges(n, code)
    return [(n, code, reps[(n, code)]) for n, code in sorted(reps)]


def degrees(n: int, edges: tuple[tuple[int, int], ...]) -> list[int]:
    out = [0] * n
    for u, v in edges:
        out[u] += 1
        out[v] += 1
    return out


def reduced_laplacian(n: int, edges: tuple[tuple[int, int], ...], sink: int) -> tuple[list[int], list[list[int]]]:
    vertices = [v for v in range(n) if v != sink]
    index = {v: i for i, v in enumerate(vertices)}
    deg = degrees(n, edges)
    matrix = [[0] * len(vertices) for _ in vertices]
    for v in vertices:
        matrix[index[v]][index[v]] = deg[v]
    for u, v in edges:
        if u != sink and v != sink:
            matrix[index[u]][index[v]] -= 1
            matrix[index[v]][index[u]] -= 1
    return vertices, matrix


def determinant(matrix: list[list[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    work = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for k in range(n - 1):
        if work[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if work[i][k] != 0), None)
            if swap is None:
                return 0
            work[k], work[swap] = work[swap], work[k]
            sign *= -1
        pivot = work[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                work[i][j] = (work[i][j] * pivot - work[i][k] * work[k][j]) // previous
        previous = pivot
    return sign * work[n - 1][n - 1]


def minor(matrix: list[list[int]], row: int, column: int) -> list[list[int]]:
    return [
        [value for j, value in enumerate(source_row) if j != column]
        for i, source_row in enumerate(matrix) if i != row
    ]


def adjugate(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    return [
        [((-1) ** (i + j)) * determinant(minor(matrix, j, i)) for j in range(n)]
        for i in range(n)
    ]


def matvec(matrix: list[list[int]], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def stable_states(n: int, edges: tuple[tuple[int, int], ...], sink: int, vertices: list[int]) -> list[tuple[int, ...]]:
    deg = degrees(n, edges)
    return list(product(*(range(deg[v]) for v in vertices)))


def recurrent_burning(
    state: tuple[int, ...],
    n: int,
    edges: tuple[tuple[int, int], ...],
    sink: int,
    vertices: list[int],
) -> bool:
    index = {v: i for i, v in enumerate(vertices)}
    unburned = set(vertices)
    while unburned:
        burnable = []
        for v in sorted(unburned):
            unburned_neighbors = sum(
                1 for edge in edges if v in edge and (edge[1] if edge[0] == v else edge[0]) in unburned
            )
            if state[index[v]] >= unburned_neighbors:
                burnable.append(v)
        if not burnable:
            return False
        unburned.remove(burnable[0])
    return True


def stabilize(
    state: tuple[int, ...],
    addition: tuple[int, ...],
    n: int,
    edges: tuple[tuple[int, int], ...],
    sink: int,
    vertices: list[int],
) -> tuple[int, ...]:
    index = {v: i for i, v in enumerate(vertices)}
    deg = degrees(n, edges)
    heights = [state[i] + addition[i] for i in range(len(vertices))]
    while True:
        unstable = next((v for v in vertices if heights[index[v]] >= deg[v]), None)
        if unstable is None:
            return tuple(heights)
        heights[index[unstable]] -= deg[unstable]
        for u, v in edges:
            if u == unstable and v != sink:
                heights[index[v]] += 1
            elif v == unstable and u != sink:
                heights[index[u]] += 1


def cycle_lengths(mapping: dict[tuple[int, ...], tuple[int, ...]]) -> list[int]:
    unseen = set(mapping)
    lengths = []
    while unseen:
        start = min(unseen)
        current = start
        length = 0
        while current in unseen:
            unseen.remove(current)
            current = mapping[current]
            length += 1
        assert current == start
        lengths.append(length)
    return sorted(lengths)


def source_vectors(vertices: list[int]) -> list[tuple[str, tuple[int, ...]]]:
    r = len(vertices)
    out = [("zero", (0,) * r)]
    for i, vertex in enumerate(vertices):
        vector = tuple(1 if j == i else 0 for j in range(r))
        out.append((f"unit_at_vertex_{vertex}", vector))
    out.append(("all_ones", (1,) * r))
    return out


def build() -> dict:
    representatives = graph_representatives()
    graph_rows = []
    sink_rows = []
    translation_rows = []
    stable_transition_checks = 0
    recurrent_transition_checks = 0
    fixed_count_checks = 0

    for n, code, edges in representatives:
        graph_id = f"n{n}-{code}"
        graph_rows.append({
            "graph_id": graph_id,
            "vertex_count": n,
            "canonical_upper_triangle_code": code,
            "edges": [list(edge) for edge in edges],
        })
        deg = degrees(n, edges)
        for sink in range(n):
            vertices, laplacian = reduced_laplacian(n, edges, sink)
            D = determinant(laplacian)
            adj = adjugate(laplacian)
            stable = stable_states(n, edges, sink, vertices)
            recurrent = [state for state in stable if recurrent_burning(state, n, edges, sink, vertices)]
            assert len(recurrent) == D
            sink_rows.append({
                "graph_id": graph_id,
                "sink": sink,
                "non_sink_vertices": vertices,
                "vertex_degrees": deg,
                "reduced_laplacian": laplacian,
                "determinant_D": D,
                "stable_state_count": len(stable),
                "recurrent_state_count": len(recurrent),
            })

            for label, b in source_vectors(vertices):
                w = matvec(adj, b)
                common = D
                for value in w:
                    common = gcd(common, abs(value))
                L = D // common
                recurrent_map = {
                    state: stabilize(state, b, n, edges, sink, vertices)
                    for state in recurrent
                }
                assert set(recurrent_map.values()) == set(recurrent)
                lengths = cycle_lengths(recurrent_map)
                assert lengths and set(lengths) == {L}
                full_map = {
                    state: stabilize(state, b, n, edges, sink, vertices)
                    for state in stable
                }
                stable_transition_checks += len(stable)
                recurrent_transition_checks += len(recurrent)
                fixed_counts = []
                current = {state: state for state in recurrent}
                for iterate_n in range(1, 2 * L + 3):
                    current = {state: recurrent_map[image] for state, image in current.items()}
                    observed = sum(image == state for state, image in current.items())
                    formula = D if iterate_n % L == 0 else 0
                    assert observed == formula
                    fixed_count_checks += len(recurrent)
                    fixed_counts.append({
                        "n": iterate_n,
                        "fixed_count_formula": formula,
                        "fixed_count_enumerated": observed,
                    })
                translation_rows.append({
                    "graph_id": graph_id,
                    "sink": sink,
                    "source_label": label,
                    "b": list(b),
                    "adjugate_times_b": list(w),
                    "order_L": L,
                    "recurrent_state_count_D": D,
                    "recurrent_cycle_count": D // L,
                    "observed_cycle_lengths": lengths,
                    "full_stable_state_count": len(stable),
                    "full_stable_image_size": len(set(full_map.values())),
                    "full_stable_injective": len(set(full_map.values())) == len(stable),
                    "fixed_counts": fixed_counts,
                })

    by_order = {}
    for row in graph_rows:
        by_order[str(row["vertex_count"])] = by_order.get(str(row["vertex_count"]), 0) + 1

    data = {
        "schema": "HCS-C176-v1",
        "candidate_id": "HCS-C176",
        "date_utc": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "addition and stabilization on recurrent stable configurations of a finite connected undirected loopless multigraph with a designated sink",
            "family": "every such graph, every sink, and every nonnegative chip vector b on the non-sink vertices",
            "arithmetic_origin": "none; the graph critical group and chip addition have no intrinsic rational-prime or prime-power semantics",
            "clock": "one application T_b(eta)=stabilize(eta+b)",
            "normalization": "stable heights 0<=eta_v<deg(v), reduced Laplacian Delta, uniform counting measure on recurrent configurations",
            "determinant_convention": "Artin--Mazur zeta and finite Koopman determinant of T_b restricted to the recurrent set",
            "cutoff": "all-graph proof; exhaustive simple-graph regression on all 30 connected isomorphism types with 2<=|V|<=5, every sink, and zero/unit/all-ones additions",
            "precision": "exact integer topplings, determinants, adjugates, quotient orders and finite permutations",
            "allowed_data": "the frozen graph, sink, chip vector, reduced Laplacian, recurrent configurations and derived exact group data",
            "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
        },
        "recurrent_bridge_theorem": {
            "critical_group": "K(G,s)=Z^(V_non_sink)/Delta Z^(V_non_sink), with D=det(Delta)",
            "representatives": "every class in K(G,s) has a unique recurrent stable representative, so the recurrent set is a canonical K(G,s)-torsor and has D elements",
            "translation": "T_b(eta)=stabilize(eta+b) preserves the recurrent set and is translation by [b]",
            "scope": "the theorem is on recurrent stable configurations; it does not identify all stable configurations with the critical group",
        },
        "order_theorem": {
            "definition": "L=ord_K([b])=min{ell>=1: ell*b lies in Delta Z^(V_non_sink)}",
            "smith": "if U*Delta*V=diag(d_i), then L=lcm_i d_i/gcd(d_i,(U*b)_i)",
            "adjugate": "with w=adj(Delta)*b and D=det(Delta), L=D/gcd(D,w_1,...,w_r)",
            "zero_source": "b=0 has L=1",
            "sink_only": "if r=0, use D=L=1 and the singleton empty recurrent configuration",
        },
        "orbit_spectral_theorem": {
            "cycles": "every recurrent orbit has exact length L and there are D/L primitive cycles",
            "fixed_counts": "#Fix(T_b^n on recurrent configurations)=D if L divides n and zero otherwise",
            "zeta": "zeta_T_b(z)=(1-z^L)^(-D/L)",
            "determinant": "det(I-z*U_b)=(1-z^L)^(D/L)",
            "spectrum": "every L-th root of unity occurs with multiplicity D/L",
            "reversal": "group inversion R is involutive and R*T_b*R=T_b^(-1); conjugation after R is antiunitary",
            "self_adjoint": "the finite Koopman unitary U_b is self-adjoint if and only if L<=2",
        },
        "stable_state_boundary": {
            "warning": "addition-stabilization on all stable configurations need not be injective or unitary and is not the phase space of the translation theorem",
            "counterexample": "on the path 0-1-2 with sink 2 and b=(1,0), both stable states (0,0) and (0,1) map to (0,1), while the recurrent set is the singleton {(0,1)}",
            "nonclaim": "no all-stable-state cycle classification or eventual-recurrence theorem is asserted for arbitrary b",
        },
        "finite_replay": {
            "vertex_max": VERTEX_MAX,
            "graph_rows": graph_rows,
            "sink_rows": sink_rows,
            "translation_rows": translation_rows,
            "graph_count_by_vertex_order": by_order,
            "graph_row_count": len(graph_rows),
            "sink_row_count": len(sink_rows),
            "translation_case_count": len(translation_rows),
            "fixed_count_row_count": sum(len(row["fixed_counts"]) for row in translation_rows),
            "full_stable_noninjective_case_count": sum(not row["full_stable_injective"] for row in translation_rows),
            "stable_transition_checks": stable_transition_checks,
            "recurrent_transition_checks": recurrent_transition_checks,
            "fixed_count_state_checks": fixed_count_checks,
        },
        "progress_and_boundary": {
            "progress": "proves the all-graph recurrent-torsor bridge, two exact translation-order formulas, uniform orbit law, zeta, determinant, spectrum, reversal and self-adjoint boundary",
            "route_a_obstruction": "the exact critical-group dynamics has no intrinsic prime semantics, target divisor comparison, or target global analytic structure",
            "sentinel_boundary": "finite simple-graph enumeration regression-tests the proof and does not extrapolate the multigraph theorem",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "A0_qualification": "NO_INTRINSIC_ARITHMETIC_ORIGIN_OR_PRIME_CORRESPONDENCE",
            "A1_qualification": "COMPLETE_INTRINSIC_RECURRENT_PRIMITIVE_CYCLES_WITHOUT_ARITHMETIC_INFORMATION",
            "A2_qualification": "EXACT_SOURCE_ZETA_AND_FINITE_DETERMINANT_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3_qualification": "FINITE_RATIONAL_SOURCE_STRUCTURE_WITH_NO_TARGET_GLOBAL_ANALYTIC_COMPARISON",
            "A4_qualification": "SAME_CLOCK_RECURRENT_TRANSLATION_PERMUTATION_WITH_UNIFORM_KOOPMAN_UNITARY_AND_GROUP_INVERSION_REVERSAL",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "used_target_zero_table": False,
            "used_target_prime_table": False,
            "used_arithmetic_local_data": False,
            "claimed_target_divisor_match": False,
            "claimed_target_functional_equation": False,
            "claimed_hilbert_polya": False,
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "external novelty or priority for the classical recurrent sandpile and critical-group facts",
            "prime semantics for critical-group translations or their repetitions",
            "permutation or unitarity of addition-stabilization on all stable configurations",
            "a target divisor, functional equation, counting law, continuation, or Weil compression",
            "arithmetic local factors, Euler factors, root numbers, automorphy, a Hilbert--Polya operator, Route-B authorization, or external peer review",
        ],
    }
    data["payload_sha256"] = sha256(canonical_bytes(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    replay = data["finite_replay"]
    print(json.dumps({
        "status": "C176_PRODUCER_PASS",
        "graphs": replay["graph_row_count"],
        "sinks": replay["sink_row_count"],
        "translation_cases": replay["translation_case_count"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
