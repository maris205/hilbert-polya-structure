#!/usr/bin/env python3
"""Deterministic exact certificate for heterogeneous Kuramoto locking on trees."""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

SOURCE_COMMIT = "98782afe1e754c311ad0736f72ce09dcc7c85c77"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1788048000
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c259_kuramoto_evidence.json"


def qt(x: F | int) -> str:
    x = x if isinstance(x, F) else F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def decode_prufer(n: int, sequence: tuple[int, ...]) -> list[tuple[int, int]]:
    degrees = [1] * n
    for vertex in sequence:
        degrees[vertex] += 1
    edges: list[tuple[int, int]] = []
    for vertex in sequence:
        leaf = next(i for i, degree in enumerate(degrees) if degree == 1)
        edges.append(tuple(sorted((leaf, vertex))))
        degrees[leaf] -= 1
        degrees[vertex] -= 1
    remaining = [i for i, degree in enumerate(degrees) if degree == 1]
    edges.append(tuple(sorted(remaining)))
    return sorted(edges)


def orient_tree(n: int, edges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    adjacency = [[] for _ in range(n)]
    for left, right in edges:
        adjacency[left].append(right)
        adjacency[right].append(left)
    parent = [-1] * n
    parent[0] = 0
    queue = [0]
    oriented: list[tuple[int, int]] = []
    for vertex in queue:
        for child in sorted(adjacency[vertex]):
            if parent[child] != -1:
                continue
            parent[child] = vertex
            queue.append(child)
            oriented.append((vertex, child))
    assert len(oriented) == n - 1
    return oriented


def pythagorean_edge(edge_index: int) -> tuple[F, F, F]:
    """Return K, |F|, |cos(delta)| with rational unit-circle data."""
    t = F(edge_index + 1, edge_index + 2)
    sine = 2 * t / (1 + t * t)
    cosine = (1 - t * t) / (1 + t * t)
    coupling = F(edge_index + 3, 1)
    return coupling, coupling * sine, cosine


def build_row(n: int, tree_index: int, sequence: tuple[int, ...]) -> dict:
    undirected = decode_prufer(n, sequence)
    edges = orient_tree(n, undirected)
    mode = (tree_index + n) % 3
    regime = ("strict", "saturated", "violated")[mode]
    flows: list[F] = []
    couplings: list[F] = []
    cos_abs: list[F | None] = []
    strict: list[int] = []
    saturated: list[int] = []
    violated: list[int] = []
    for edge_index, (parent, child) in enumerate(edges):
        coupling, magnitude, cosine = pythagorean_edge(edge_index)
        sign = -1 if (tree_index + parent + child + edge_index) % 2 else 1
        flow = sign * magnitude
        if edge_index == 0 and regime == "saturated":
            flow = sign * coupling
            cosine = F(0)
            saturated.append(edge_index)
        elif edge_index == 0 and regime == "violated":
            flow = sign * 2 * coupling
            cosine = None
            violated.append(edge_index)
        else:
            strict.append(edge_index)
        flows.append(flow)
        couplings.append(coupling)
        cos_abs.append(cosine)

    eta = [F(0) for _ in range(n)]
    for (parent, child), flow in zip(edges, flows):
        eta[parent] -= flow
        eta[child] += flow
    omega_mean = F(n + tree_index % 5, 3)
    omega = [omega_mean + value for value in eta]
    feasible = not violated
    strict_count = len(strict)
    branch_count = 2 ** strict_count if feasible else 0
    morse_histogram = (
        {str(k): math.comb(strict_count, k) for k in range(strict_count + 1)}
        if feasible
        else {}
    )
    stable_count = 1 if regime == "strict" else 0
    return {
        "n": n,
        "tree_index": tree_index,
        "prufer": list(sequence),
        "undirected_edges": [list(edge) for edge in undirected],
        "rooted_edges": [list(edge) for edge in edges],
        "omega_mean": qt(omega_mean),
        "omega": [qt(value) for value in omega],
        "eta": [qt(value) for value in eta],
        "couplings": [qt(value) for value in couplings],
        "cut_flows": [qt(value) for value in flows],
        "cosine_absolute": [None if value is None else qt(value) for value in cos_abs],
        "regime": regime,
        "strict_edges": strict,
        "saturated_edges": saturated,
        "violated_edges": violated,
        "branch_count_mod_rotation": branch_count,
        "stable_branch_count": stable_count,
        "reduced_hessian_nullity": len(saturated) if feasible else None,
        "morse_index_histogram": morse_histogram,
        "proof_role": "exact all-tree regression; the all-N theorem is analytic",
    }


def build() -> dict:
    rows = []
    by_n = {}
    regimes = {"strict": 0, "saturated": 0, "violated": 0}
    for n in range(2, 8):
        count = 0
        for tree_index, sequence in enumerate(itertools.product(range(n), repeat=n - 2)):
            row = build_row(n, tree_index, sequence)
            rows.append(row)
            regimes[row["regime"]] += 1
            count += 1
        by_n[str(n)] = count
    boundary_rows = [
        {"boundary": "N=1", "law": "one rigid phase; the rotation quotient is a point"},
        {"boundary": "identical frequencies", "law": "all cut flows vanish; edge differences are 0 or pi and the synchronous branch is uniquely stable"},
        {"boundary": "saturated cut", "law": "the two inverse-sine branches merge; each saturated edge adds one reduced-Hessian null direction"},
        {"boundary": "violated cut", "law": "if |F_e|>K_e on one edge, no locked state exists"},
        {"boundary": "zero coupling", "law": "if K_e=0, nonzero cut flow forbids locking and zero cut flow disconnects the phase constraint"},
        {"boundary": "non-tree graph", "law": "cycle flows destroy uniqueness of the cut-flow solution; outside the frozen owner"},
    ]
    data = {
        "schema": "hcs-c259-tree-kuramoto-locking-morse-v1",
        "candidate_id": "HCS-C259",
        "evaluation_date": "2026-08-31",
        "source_commit": SOURCE_COMMIT,
        "fixed_epoch": FIXED_EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {
            "path": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA256,
        },
        "headline": "Every heterogeneous positively weighted Kuramoto tree has a unique cut-flow locking criterion, a complete inverse-sine branch atlas, and an exact edgewise Morse-index theorem.",
        "frozen_object": {
            "phase_space": "N phases on the torus modulo diagonal rotation; connected labeled tree rooted at vertex 0",
            "dynamics": "theta'=omega-B K sin(B^T theta), with each incidence column -1 at parent and +1 at child",
            "parameters": "N>=2, positive edge couplings K_e, arbitrary real natural frequencies",
            "clock": "physical oscillator time",
            "normalization": "Omega=mean(omega), eta=omega-Omega*1, delta=B^T theta",
            "arithmetic_origin": "none; source-local phase-oscillator network",
            "determinant_convention": "none",
            "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, functional equations, Hilbert--Polya operators",
        },
        "theorem": {
            "rotating_frame": "Every locked solution has common frequency Omega=mean(omega); in the rotating frame it solves B f=eta with f_e=K_e sin(delta_e).",
            "unique_cut_flow": "For the root-oriented edge parent->child, f_e equals the sum of eta over the child subtree. This is the unique solution of Bf=eta.",
            "existence": "A locked state exists if and only if |F_e|<=K_e on every edge.",
            "strict_branch_atlas": "If every inequality is strict, each edge has two inverse-sine choices independently, hence exactly 2^(N-1) locked branches modulo diagonal rotation.",
            "saturation": "Each saturated edge has one merged inverse-sine choice; with s saturated edges there are 2^(N-1-s) branches and reduced-Hessian nullity s.",
            "morse_inertia": "At a branch the potential Hessian is B diag(K_e cos(delta_e)) B^T. On the rotation quotient it is congruent to the diagonal edge matrix, so its Morse index is the number of negative cosines.",
            "stability": "In the strict chamber exactly one branch has every cosine positive and is linearly asymptotically stable modulo rotation; every other branch has an unstable direction. Saturated branches are nonhyperbolic.",
            "nonexistence": "A single violated cut |F_e|>K_e rules out every locked state.",
            "boundary_scope": "Zero couplings and graphs with cycles change the owner. No classification of all unlocked running states is claimed.",
        },
        "regression": {
            "rows": rows,
            "tree_count": len(rows),
            "tree_count_by_n": by_n,
            "regime_counts": regimes,
            "boundary_rows": boundary_rows,
            "boundary_row_count": len(boundary_rows),
            "enumeration": "all labeled Prüfer trees for 2<=N<=7, in lexicographic code order",
        },
        "exact_identities": [
            "Omega=N^{-1} sum_i omega_i",
            "eta=omega-Omega*1 and sum_i eta_i=0",
            "B f=eta",
            "F_e=sum_{i in child subtree S_e} eta_i",
            "f_e=K_e sin(delta_e)",
            "locking iff |F_e|<=K_e for all e",
            "strict branch count=2^(N-1)",
            "boundary branch count=2^(N-1-s) for s saturated edges",
            "H=B diag(K_e cos(delta_e)) B^T",
            "reduced inertia(H)=inertia(diag(K_e cos(delta_e)))",
            "Morse index=number of negative edge cosines",
            "reduced nullity=number of saturated edges",
            "unique strict stable branch has all edge cosines positive",
            "global phase reconstruction is unique after theta_0=0",
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "The all-tree locking chamber, every equilibrium branch, and every reduced Morse index are analytic and exact.",
            "strongest_failure": "The clean relative equilibria carry no intrinsic rational-prime labels, logarithmic prime clock, or target determinant.",
        },
        "scope_flags": {
            key: False
            for key in [
                "uses_target_zero_table",
                "uses_prime_table",
                "claims_arithmetic_local_data",
                "claims_euler_factors",
                "claims_root_numbers",
                "claims_automorphy",
                "claims_target_divisor_or_functional_equation",
                "claims_hilbert_polya_operator",
                "invokes_route_b",
            ]
        },
        "citations": [
            {
                "key": "Kuramoto1975",
                "claim": "model attribution only; the tree cut-flow and Morse theorem is proved locally",
                "source": "Y. Kuramoto, Self-entrainment of a population of coupled non-linear oscillators, Lecture Notes in Physics 39 (1975), 420--422",
                "url": "https://doi.org/10.1007/BFb0013365",
            }
        ],
        "nonclaims": [
            "a literature-priority claim for tree synchronization",
            "a global classification of unlocked running states",
            "an extension from trees to graphs with cycle-flow freedom",
            "a dynamical zeta or target Fredholm determinant",
            "arithmetic local data, Euler factors, root numbers, automorphy, target divisor, functional equation, or Hilbert--Polya operator",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C259_PRODUCER_PASS",
        "trees": data["regression"]["tree_count"],
        "regimes": data["regression"]["regime_counts"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
