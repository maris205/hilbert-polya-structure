#!/usr/bin/env python3
"""Exact prototype for the full-shift-semiring trial-division shift."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


def write_csv(path: Path, fieldnames: Sequence[str], rows: Sequence[Dict[str, object]]) -> None:
    """Write deterministic UTF-8/LF CSV with an explicit column order."""
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fieldnames), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def sieve_primes(limit: int) -> List[int]:
    flag = [True] * (limit + 1)
    if limit >= 0:
        flag[0] = False
    if limit >= 1:
        flag[1] = False
    for p in range(2, math.isqrt(limit) + 1):
        if flag[p]:
            for k in range(p * p, limit + 1, p):
                flag[k] = False
    return [n for n in range(2, limit + 1) if flag[n]]


def trial_accepts(n: int, max_divisor: int | None = None, shift: int = 0) -> bool:
    """Fully unrolled trial division using successor, tensor, and order.

    The inner ``q`` loop is intentional: the candidate never receives an
    existential factor oracle. It constructs successive full-shift objects
    F_q and compares F_d tensor F_q with the target F_n.
    """
    target = n + shift
    d = 2
    while d * d <= target:
        if max_divisor is not None and d > max_divisor:
            return True
        q = 2
        while d * q < target:
            q += 1
        if d * q == target:
            return False
        d += 1
    return target >= 2


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    numerator: int
    denominator: int

    @property
    def weight(self) -> Fraction:
        return Fraction(self.numerator, self.denominator)


def graph_edges(limit: int, cemetery_depth: int = 3, s_integer: int = 2) -> Tuple[List[str], List[Edge], List[int]]:
    """Finite audit of the explicit quotient-search graph.

    ``Q:n:d:q`` exposes the search for a tensor cofactor instead of hiding it
    behind the one-step predicate ``exists q: d*q=n``. The missing cemetery
    tail creates no cycle and therefore cannot change any audited trace.
    """
    nodes: List[str] = []
    node_set: set[str] = set()
    edges: List[Edge] = []
    accepted: List[int] = []

    def add_node(v: str) -> None:
        if v not in node_set:
            node_set.add(v)
            nodes.append(v)

    def add_edge(u: str, v: str, denom: int) -> None:
        add_node(u)
        add_node(v)
        edges.append(Edge(u, v, 1, denom**s_integer))

    for n in range(2, limit + 1):
        start = f"I:{n}"
        test = f"T:{n}:2"
        add_edge(start, test, 2 * n)
        d = 2
        while True:
            here = f"T:{n}:{d}"
            add_node(here)
            if d * d > n:
                accept = f"A:{n}"
                add_edge(here, accept, n * d)
                add_edge(accept, accept, n)
                accepted.append(n)
                break
            q = 2
            q_here = f"Q:{n}:{d}:{q}"
            add_edge(here, q_here, n * d * q)
            while True:
                q_here = f"Q:{n}:{d}:{q}"
                add_node(q_here)
                product = d * q
                if product == n:
                    first = f"R:{n}:1"
                    add_edge(q_here, first, n * d * q)
                    for k in range(1, cemetery_depth):
                        add_edge(f"R:{n}:{k}", f"R:{n}:{k+1}", n * (k + 1))
                    break
                if product > n:
                    nxt = f"T:{n}:{d+1}"
                    add_edge(q_here, nxt, n * d * q)
                    d += 1
                    break
                q_next = f"Q:{n}:{d}:{q+1}"
                add_edge(q_here, q_next, n * d * q)
                q += 1
            if product == n:
                break
    return nodes, edges, accepted


def decider_graph_edges(
    limit: int,
    name: str,
    predicate,
    runtime,
    cemetery_depth: int = 3,
    s_integer: int = 2,
) -> Tuple[List[str], List[Edge], List[int]]:
    """Universal total-decider wrapper used as the strongest control.

    ``runtime(n)`` is a positive finite integer standing for the number of
    deterministic configurations exposed before the terminal decision.
    The time-index factor makes the entrywise nuclear bound independent of
    how quickly this runtime grows.
    """
    nodes: List[str] = []
    node_set: set[str] = set()
    edges: List[Edge] = []
    accepted: List[int] = []

    def add_node(v: str) -> None:
        if v not in node_set:
            node_set.add(v)
            nodes.append(v)

    def add_edge(u: str, v: str, denom: int) -> None:
        add_node(u)
        add_node(v)
        edges.append(Edge(u, v, 1, denom**s_integer))

    for n in range(2, limit + 1):
        steps = int(runtime(n))
        assert steps >= 1
        for t in range(steps):
            add_edge(f"C:{name}:{n}:{t}", f"C:{name}:{n}:{t+1}", n * (t + 2))
        terminal = f"C:{name}:{n}:{steps}"
        if predicate(n):
            accept = f"A:{name}:{n}"
            add_edge(terminal, accept, n * (steps + 2))
            add_edge(accept, accept, n)
            accepted.append(n)
        else:
            add_edge(terminal, f"R:{name}:{n}:1", n * (steps + 2))
            for k in range(1, cemetery_depth):
                add_edge(f"R:{name}:{n}:{k}", f"R:{name}:{n}:{k+1}", n * (k + 1))
    return nodes, edges, accepted


def tarjan_scc(nodes: Sequence[str], edges: Sequence[Edge]) -> List[List[str]]:
    adj: Dict[str, List[str]] = {v: [] for v in nodes}
    for edge in edges:
        adj[edge.source].append(edge.target)
    index = 0
    stack: List[str] = []
    on_stack: set[str] = set()
    indices: Dict[str, int] = {}
    low: Dict[str, int] = {}
    result: List[List[str]] = []

    def visit(v: str) -> None:
        nonlocal index
        indices[v] = low[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)
        for w in adj[v]:
            if w not in indices:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp: List[str] = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                comp.append(w)
                if w == v:
                    break
            result.append(comp)

    for node in nodes:
        if node not in indices:
            visit(node)
    return result


def recurrent_nodes(nodes: Sequence[str], edges: Sequence[Edge]) -> List[str]:
    loops = {edge.source for edge in edges if edge.source == edge.target}
    recurrent: List[str] = []
    for comp in tarjan_scc(nodes, edges):
        if len(comp) > 1 or any(v in loops for v in comp):
            recurrent.extend(comp)
    return sorted(recurrent)


def trace_power(edges: Sequence[Edge], r: int) -> Fraction:
    """Exact matrix trace by sparse dynamic multiplication."""
    nodes = sorted({e.source for e in edges} | {e.target for e in edges})
    idx = {v: i for i, v in enumerate(nodes)}
    matrix: Dict[Tuple[int, int], Fraction] = {
        (idx[e.target], idx[e.source]): e.weight for e in edges
    }
    power = dict(matrix)
    for _ in range(1, r):
        nxt: Dict[Tuple[int, int], Fraction] = {}
        by_left: Dict[int, List[Tuple[int, Fraction]]] = {}
        by_right: Dict[int, List[Tuple[int, Fraction]]] = {}
        for (i, k), value in power.items():
            by_left.setdefault(k, []).append((i, value))
        for (k, j), value in matrix.items():
            by_right.setdefault(k, []).append((j, value))
        for k in set(by_left) & set(by_right):
            for i, a in by_left[k]:
                for j, b in by_right[k]:
                    nxt[(i, j)] = nxt.get((i, j), Fraction(0)) + a * b
        power = nxt
    return sum((value for (i, j), value in power.items() if i == j), Fraction(0))


def determinant_fraction(nodes: Sequence[str], edges: Sequence[Edge], z: Fraction) -> Fraction:
    """Bareiss determinant of I-zT over Q."""
    idx = {v: i for i, v in enumerate(nodes)}
    n = len(nodes)
    a = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for edge in edges:
        a[idx[edge.target]][idx[edge.source]] -= z * edge.weight
    sign = 1
    prev = Fraction(1)
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * p - a[i][k] * a[k][j]) / prev
        prev = p
    return sign * a[-1][-1]


def shuffled_presentation(limit: int, seed: int) -> Dict[str, object]:
    rng = random.Random(seed)
    values = list(range(1, limit + 1))
    labels = [f"v{i:04d}" for i in range(1, limit + 1)]
    rng.shuffle(labels)
    label_of = dict(zip(values, labels))
    value_of = {label: value for value, label in label_of.items()}

    def successor(label: str) -> str | None:
        value = value_of[label]
        return label_of.get(value + 1)

    def multiply(left: str, right: str) -> str | None:
        return label_of.get(value_of[left] * value_of[right])

    accepted: List[str] = []
    two = label_of[2]
    for n in range(2, limit + 1):
        n_label = label_of[n]
        d_label = two
        while True:
            d = value_of[d_label]
            square = multiply(d_label, d_label)
            if square is None or value_of[square] > n:
                accepted.append(n_label)
                break
            q_label = two
            while True:
                product = multiply(d_label, q_label)
                if product == n_label:
                    break
                q = value_of[q_label]
                if product is None or d * q > n:
                    product = None
                    break
                next_q = successor(q_label)
                assert next_q is not None
                q_label = next_q
            if product == n_label:
                break
            next_label = successor(d_label)
            assert next_label is not None
            d_label = next_label
    decoded = sorted(value_of[label] for label in accepted)
    return {"seed": seed, "accepted_decoded": decoded, "label_digest": hashlib.sha256("|".join(accepted).encode()).hexdigest()}


def gf2_degree(poly: int) -> int:
    return poly.bit_length() - 1


def gf2_mod(dividend: int, divisor: int) -> int:
    rem = dividend
    degree = gf2_degree(divisor)
    while rem and gf2_degree(rem) >= degree:
        rem ^= divisor << (gf2_degree(rem) - degree)
    return rem


def gf2_monic(degree: int) -> Iterable[int]:
    return range(1 << degree, 1 << (degree + 1))


def gf2_irreducible(poly: int) -> bool:
    degree = gf2_degree(poly)
    if degree <= 0:
        return False
    for d in range(1, degree // 2 + 1):
        for divisor in gf2_monic(d):
            if gf2_mod(poly, divisor) == 0:
                return False
    return True


def polynomial_control(max_degree: int = 8) -> Dict[str, object]:
    counts: Dict[str, int] = {}
    polys: List[int] = []
    for degree in range(1, max_degree + 1):
        selected = [p for p in gf2_monic(degree) if gf2_irreducible(p)]
        counts[str(degree)] = len(selected)
        polys.extend(selected)
    # Euler product coefficient audit in u through max_degree.
    coeff = [1] + [0] * max_degree
    for degree_str, multiplicity in counts.items():
        degree = int(degree_str)
        for _ in range(multiplicity):
            new = coeff[:]
            for base in range(max_degree + 1):
                if coeff[base] == 0:
                    continue
                power = 1
                while base + power * degree <= max_degree:
                    new[base + power * degree] += coeff[base]
                    power += 1
            coeff = new
    target = [2**n for n in range(max_degree + 1)]
    return {
        "max_degree": max_degree,
        "irreducible_counts": counts,
        "selected_total": len(polys),
        "euler_coefficients": coeff,
        "target_coefficients": target,
        "exact": coeff == target,
    }


def entropy_shuffle_control(limit: int, seed: int) -> Dict[str, object]:
    """Keep the semiring selector but break entropy/object compatibility."""
    primes = sieve_primes(limit)
    masses = list(range(2, limit + 1))
    rng = random.Random(seed)
    rng.shuffle(masses)
    mass_of = dict(zip(range(2, limit + 1), masses))
    target = sum((Fraction(1, p * p) for p in primes), Fraction(0))
    shuffled = sum((Fraction(1, mass_of[p] ** 2) for p in primes), Fraction(0))
    return {
        "seed": seed,
        "selected_count": len(primes),
        "target_trace_s2": str(target),
        "shuffled_trace_s2": str(shuffled),
        "exact_target": target == shuffled,
        "absolute_difference": str(abs(target - shuffled)),
    }


def fibonacci_set(limit: int) -> set[int]:
    values = {2}
    a, b = 1, 2
    while b <= limit:
        values.add(b)
        a, b = b, a + b
    return values


def universal_decider_controls(limit: int = 24) -> List[Dict[str, object]]:
    fib = fibonacci_set(limit)
    predicates = {
        "squares": (lambda n: math.isqrt(n) ** 2 == n, lambda n: math.isqrt(n)),
        "powers_two": (lambda n: n & (n - 1) == 0, lambda n: n.bit_length()),
        "fibonacci": (lambda n: n in fib, lambda n: len(fibonacci_set(n))),
        "hash_mod_five": (
            lambda n: ((1103515245 * n + 19023) & 0x7FFFFFFF) % 5 == 0,
            lambda n: n.bit_length() + 3,
        ),
    }
    rows: List[Dict[str, object]] = []
    for name, (predicate, runtime) in predicates.items():
        nodes, edges, accepted = decider_graph_edges(limit, name, predicate, runtime)
        recurrent = recurrent_nodes(nodes, edges)
        expected_recurrent = sorted(f"A:{name}:{n}" for n in accepted)
        # An independent dense rational determinant is deliberately kept at
        # a tiny fixed prefix; the large-prefix theorem audit uses the exact
        # SCC/closed-walk census and avoids cubic symbolic elimination.
        matrix_limit = min(limit, 8)
        matrix_nodes, matrix_edges, matrix_accepted = decider_graph_edges(
            matrix_limit, name, predicate, runtime
        )
        z = Fraction(1, 5)
        actual_det = determinant_fraction(matrix_nodes, matrix_edges, z)
        expected_det = math.prod(
            (Fraction(1) - z * Fraction(1, n * n) for n in matrix_accepted),
            start=Fraction(1),
        )
        rows.append({
            "name": name,
            "limit": limit,
            "accepted": accepted,
            "nodes": len(nodes),
            "edges": len(edges),
            "recurrent_exact": recurrent == expected_recurrent,
            "matrix_audit_limit": matrix_limit,
            "determinant_exact": actual_det == expected_det,
            "determinant": str(actual_det),
        })
    return rows


def run(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    cutoffs = [32, 64, 128, 256, 512]
    support_rows = []
    for limit in cutoffs:
        accepted = [n for n in range(2, limit + 1) if trial_accepts(n)]
        primes = sieve_primes(limit)
        support_rows.append({
            "limit": limit,
            "accepted": len(accepted),
            "expected": len(primes),
            "false_positive": sorted(set(accepted) - set(primes)),
            "false_negative": sorted(set(primes) - set(accepted)),
            "exact": accepted == primes,
        })

    nodes, edges, accepted = graph_edges(24, cemetery_depth=3, s_integer=2)
    trace_rows = []
    for r in range(1, 13):
        actual = trace_power(edges, r)
        expected = sum((Fraction(1, p ** (2 * r)) for p in accepted), Fraction(0))
        trace_rows.append({"r": r, "actual": str(actual), "expected": str(expected), "exact": actual == expected})
    # The explicit quotient-search graph is deliberately large. Keep the
    # independent dense Bareiss check on a fixed small prefix while the
    # larger prefix is audited through SCCs and all power traces.
    matrix_limit = 8
    matrix_nodes, matrix_edges, matrix_accepted = graph_edges(
        matrix_limit, cemetery_depth=2, s_integer=2
    )
    z = Fraction(1, 3)
    actual_det = determinant_fraction(matrix_nodes, matrix_edges, z)
    expected_det = math.prod(
        (Fraction(1) - z * Fraction(1, p**2) for p in matrix_accepted),
        start=Fraction(1),
    )
    recurrent = recurrent_nodes(nodes, edges)

    bounded_rows = []
    for depth in [2, 3, 5, 7, 11]:
        selected = [n for n in range(2, 513) if trial_accepts(n, max_divisor=depth)]
        false_positive = sorted(set(selected) - set(sieve_primes(512)))
        bounded_rows.append({"depth": depth, "selected": len(selected), "false_positive_count": len(false_positive), "first_false_positive": false_positive[:10]})

    shifted = [n for n in range(2, 513) if trial_accepts(n, shift=1)]
    primes_512 = sieve_primes(512)
    shifted_overlap = len(set(shifted) & set(primes_512))

    rng = random.Random(19100)
    population = list(range(2, 513))
    random_controls = []
    for seed in range(19100, 19132):
        rng.seed(seed)
        selected = sorted(rng.sample(population, len(primes_512)))
        overlap = len(set(selected) & set(primes_512))
        random_controls.append({"seed": seed, "overlap": overlap, "selected": len(selected), "support_accuracy": overlap / len(primes_512)})

    # Absolute entry sum for increasing graph cutoffs: finite evidence for the S1 theorem.
    norm_rows = []
    for limit in cutoffs:
        _, finite_edges, _ = graph_edges(limit, cemetery_depth=32, s_integer=2)
        for sigma in [1.1, 1.25, 1.5, 2.0]:
            # Re-evaluate the frozen roof exponent at noninteger sigma from denominators.
            # ``edge.weight`` was instantiated at s_integer=2.  Recover the
            # same roof at the requested real exponent without changing the
            # graph or its support.
            entry_sum = sum(float(edge.weight) ** (sigma / 2.0) for edge in finite_edges)
            norm_rows.append({"limit": limit, "sigma": sigma, "entry_l1_sum": entry_sum})

    decider_rows = universal_decider_controls(24)
    summary = {
        "candidate": "SD-C21",
        "support_rows": support_rows,
        "finite_graph": {
            "limit": 24,
            "nodes": len(nodes),
            "edges": len(edges),
            "accepted": accepted,
            "recurrent_nodes": recurrent,
            "recurrent_exact_accept_loops": set(recurrent) == {f"A:{p}" for p in accepted},
            "transient_nodes": len(nodes) - len(recurrent),
            "trace_rows": trace_rows,
            "matrix_audit_limit": matrix_limit,
            "matrix_nodes": len(matrix_nodes),
            "matrix_edges": len(matrix_edges),
            "determinant_actual": str(actual_det),
            "determinant_expected": str(expected_det),
            "determinant_exact": actual_det == expected_det,
        },
        "transported_shuffle": shuffled_presentation(512, 19021),
        "entropy_shuffle_control": entropy_shuffle_control(512, 19022),
        "additive_only_control": {
            "selected": 511,
            "false_positive_count": 511 - len(primes_512),
            "exact_target": False,
        },
        "bounded_depth_controls": bounded_rows,
        "shifted_factor_control": {
            "selected": len(shifted),
            "prime_overlap": shifted_overlap,
            "prime_count": len(primes_512),
            "symmetric_difference": len(set(shifted) ^ set(primes_512)),
        },
        "random_accept_controls": random_controls,
        "polynomial_ufd_control": polynomial_control(8),
        "universal_decider_controls": decider_rows,
        "trace_norm_rows": norm_rows,
        "verdict": {
            "go_semiring_sieve_parent": all(row["exact"] for row in support_rows) and actual_det == expected_det,
            "stop_recurrent_advance": set(recurrent) == {f"A:{p}" for p in accepted},
            "proves_too_much_risk": polynomial_control(8)["exact"] and all(
                row["recurrent_exact"] and row["determinant_exact"]
                for row in decider_rows
            ),
            "route_b_locked": True,
        },
    }
    (output / "run_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    support_csv = [
        {
            "limit": row["limit"],
            "accepted": row["accepted"],
            "expected": row["expected"],
            "false_positive_count": len(row["false_positive"]),
            "false_negative_count": len(row["false_negative"]),
            "exact": row["exact"],
        }
        for row in support_rows
    ]
    write_csv(
        output / "support_certificates.csv",
        ("limit", "accepted", "expected", "false_positive_count", "false_negative_count", "exact"),
        support_csv,
    )
    write_csv(
        output / "power_trace_ledger.csv",
        ("r", "actual", "expected", "exact"),
        trace_rows,
    )
    write_csv(
        output / "bounded_depth_controls.csv",
        ("depth", "selected", "false_positive_count", "first_false_positive"),
        [
            {
                **row,
                "first_false_positive": ";".join(str(value) for value in row["first_false_positive"]),
            }
            for row in bounded_rows
        ],
    )
    write_csv(
        output / "random_accept_controls.csv",
        ("seed", "overlap", "selected", "support_accuracy"),
        random_controls,
    )
    write_csv(
        output / "universal_decider_controls.csv",
        ("name", "limit", "accepted", "nodes", "edges", "recurrent_exact", "matrix_audit_limit", "determinant_exact", "determinant"),
        [
            {
                **row,
                "accepted": ";".join(str(value) for value in row["accepted"]),
            }
            for row in decider_rows
        ],
    )
    write_csv(
        output / "trace_class_entry_sums.csv",
        ("limit", "sigma", "entry_l1_sum"),
        norm_rows,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    run(args.output)


if __name__ == "__main__":
    main()
