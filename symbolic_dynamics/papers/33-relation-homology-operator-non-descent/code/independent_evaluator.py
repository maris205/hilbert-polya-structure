#!/usr/bin/env python3
"""Independent low-level evaluator for Paper 33 / SD-C35.

This file imports no candidate, generator, or classifier module.  It rebuilds
all finite projective actions, relation ranks, controls, arithmetic labels,
twist rows, and the cross boundary directly from the frozen result tables.
"""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
from collections import deque
from math import gcd
from pathlib import Path
from random import Random
from statistics import mean, pstdev
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple


Point = Tuple[int, int]
SparseVector = Dict[int, int]
RANK_MODULUS = 1_000_003
EXPECTED_CORE_SHA256 = (
    "3843f0871278c0c2544494be3fff1bca1def98bfb6b870141812fd90b8897168"
)
EXPECTED_RUNNER_SHA256 = (
    "03e840f8941e69220a467fa106a55939529bd1adbe1b2fe2d2e67d2fb1887335"
)
EXPECTED_PROTOTYPE_AGGREGATE = (
    "c5c5f34673590f98e89e6229354a8dc8fc851677c7af8702d4bf54a87e8037d4"
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: List[Mapping[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def units_mod(n: int) -> Tuple[int, ...]:
    return tuple(a for a in range(n) if gcd(a, n) == 1)


def canonical_point(
    n: int,
    point: Point,
    units: Sequence[int],
) -> Point:
    a, b = point
    return min((u * a % n, u * b % n) for u in units)


def projective_action(n: int) -> Tuple[Tuple[Point, ...], Tuple[int, ...], Tuple[int, ...]]:
    units = units_mod(n)
    seen: set[Point] = set()
    points: List[Point] = []
    for a in range(n):
        for b in range(n):
            if (a, b) in seen or gcd(gcd(a, b), n) != 1:
                continue
            orbit = {(u * a % n, u * b % n) for u in units}
            seen.update(orbit)
            points.append(min(orbit))
    frozen_points = tuple(sorted(points))
    index = {point: i for i, point in enumerate(frozen_points)}
    s_image = tuple(
        index[canonical_point(n, ((-b) % n, a), units)]
        for a, b in frozen_points
    )
    r_image = tuple(
        index[canonical_point(n, ((-b) % n, (a + b) % n), units)]
        for a, b in frozen_points
    )
    return frozen_points, s_image, r_image


def compose(mapping: Sequence[int], power: int) -> Tuple[int, ...]:
    out = tuple(range(len(mapping)))
    for _ in range(power):
        out = tuple(mapping[i] for i in out)
    return out


def orbits(mapping: Sequence[int]) -> Tuple[Tuple[int, ...], ...]:
    unseen = set(range(len(mapping)))
    answer: List[Tuple[int, ...]] = []
    while unseen:
        start = min(unseen)
        cycle = []
        current = start
        while current in unseen:
            unseen.remove(current)
            cycle.append(current)
            current = mapping[current]
        answer.append(tuple(cycle))
    return tuple(answer)


def component_count(
    s_image: Sequence[int],
    r_image: Sequence[int],
) -> int:
    unseen = set(range(len(s_image)))
    components = 0
    s_inverse = [0] * len(s_image)
    r_inverse = [0] * len(r_image)
    for i, j in enumerate(s_image):
        s_inverse[j] = i
    for i, j in enumerate(r_image):
        r_inverse[j] = i
    while unseen:
        components += 1
        start = min(unseen)
        unseen.remove(start)
        queue = deque([start])
        while queue:
            x = queue.popleft()
            for y in (
                s_image[x],
                r_image[x],
                s_inverse[x],
                r_inverse[x],
            ):
                if y in unseen:
                    unseen.remove(y)
                    queue.append(y)
    return components


def relation_dimension(
    s_image: Sequence[int],
    r_image: Sequence[int],
) -> int:
    return (
        len(s_image)
        + component_count(s_image, r_image)
        - len(orbits(s_image))
        - len(orbits(r_image))
    )


def relation_vectors(
    s_image: Sequence[int],
    r_image: Sequence[int],
) -> Tuple[SparseVector, ...]:
    vectors: List[SparseVector] = []
    for orbit in orbits(s_image):
        vectors.append({i: 1 for i in orbit})
    for orbit in orbits(r_image):
        vectors.append({i: 1 for i in orbit})
    return tuple(vectors)


def sparse_rank(
    vectors: Iterable[Mapping[int, int]],
    modulus: int = RANK_MODULUS,
) -> int:
    pivots: Dict[int, SparseVector] = {}
    for original in vectors:
        vector = {
            i: value % modulus
            for i, value in original.items()
            if value % modulus
        }
        while vector:
            pivot = min(vector)
            if pivot not in pivots:
                inverse = pow(vector[pivot], modulus - 2, modulus)
                vector = {
                    i: value * inverse % modulus
                    for i, value in vector.items()
                }
                pivots[pivot] = vector
                break
            factor = vector[pivot]
            basis = pivots[pivot]
            for i, value in basis.items():
                updated = (
                    vector.get(i, 0) - factor * value
                ) % modulus
                if updated:
                    vector[i] = updated
                elif i in vector:
                    del vector[i]
    return len(pivots)


def adjacency_ranks(
    s_image: Sequence[int],
    r_image: Sequence[int],
) -> Tuple[int, int]:
    relations = relation_vectors(s_image, r_image)
    images: List[SparseVector] = []
    for vector in relations:
        image: SparseVector = {}
        for i, coefficient in vector.items():
            for target in (s_image[i], r_image[i]):
                image[target] = (
                    image.get(target, 0) + coefficient
                ) % RANK_MODULUS
                if image[target] == 0:
                    del image[target]
        images.append(image)
    return sparse_rank(relations), sparse_rank(relations + tuple(images))


def divisors(n: int) -> Tuple[int, ...]:
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def phi(n: int) -> int:
    return sum(gcd(a, n) == 1 for a in range(1, n + 1))


def cusp_count(n: int) -> int:
    return sum(phi(gcd(d, n // d)) for d in divisors(n))


def arithmetic_class(n: int) -> str:
    divisor = next(
        (d for d in range(2, int(n ** 0.5) + 1) if n % d == 0),
        None,
    )
    if divisor is None:
        return "prime"
    remaining = n
    while remaining % divisor == 0:
        remaining //= divisor
    if remaining == 1:
        return "prime_power"
    return "mixed_composite"


def relabel(
    s_image: Sequence[int],
    r_image: Sequence[int],
    seed: int,
) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    rng = Random(seed)
    permutation = list(range(len(s_image)))
    rng.shuffle(permutation)
    inverse = [0] * len(s_image)
    for old, new in enumerate(permutation):
        inverse[new] = old
    s_new = tuple(
        permutation[s_image[inverse[new]]]
        for new in range(len(s_image))
    )
    r_new = tuple(
        permutation[r_image[inverse[new]]]
        for new in range(len(r_image))
    )
    return s_new, r_new


def random_involution(size: int, rng: Random) -> Tuple[int, ...]:
    items = list(range(size))
    rng.shuffle(items)
    mapping = list(range(size))
    while len(items) >= 2:
        if rng.randrange(5) == 0:
            items.pop()
            continue
        a = items.pop()
        b = items.pop()
        mapping[a] = b
        mapping[b] = a
    return tuple(mapping)


def random_order_three(size: int, rng: Random) -> Tuple[int, ...]:
    items = list(range(size))
    rng.shuffle(items)
    mapping = list(range(size))
    while len(items) >= 3:
        if rng.randrange(6) == 0:
            items.pop()
            continue
        a = items.pop()
        b = items.pop()
        c = items.pop()
        mapping[a] = b
        mapping[b] = c
        mapping[c] = a
    return tuple(mapping)


def random_transitive_action(
    size: int,
    seed: int,
) -> Tuple[Tuple[int, ...], Tuple[int, ...], int]:
    rng = Random(seed)
    for attempt in range(1, 20_001):
        s_image = random_involution(size, rng)
        r_image = random_order_three(size, rng)
        if component_count(s_image, r_image) == 1:
            return s_image, r_image, attempt
    raise RuntimeError("independent random action sampling failed")


def independent_cross(cutoff: int) -> Dict[str, object]:
    nodes = tuple(range(2, cutoff + 1))
    edges = tuple(sorted(
        (n, multiplier * n)
        for n in nodes
        for multiplier in (2, 3)
        if multiplier * n <= cutoff
    ))
    edge_index = {edge: i for i, edge in enumerate(edges)}
    adjacency = {n: set() for n in nodes}
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    unseen = set(nodes)
    components = 0
    while unseen:
        components += 1
        start = min(unseen)
        unseen.remove(start)
        queue = deque([start])
        while queue:
            x = queue.popleft()
            for y in adjacency[x]:
                if y in unseen:
                    unseen.remove(y)
                    queue.append(y)
    squares = tuple(
        (n, 2 * n, 6 * n, 3 * n)
        for n in nodes
        if 6 * n <= cutoff
    )
    boundaries: List[SparseVector] = []
    for n, n2, n6, n3 in squares:
        vector: SparseVector = {}
        for a, b, sign in (
            (n, n2, 1),
            (n2, n6, 1),
            (n3, n6, -1),
            (n, n3, -1),
        ):
            vector[edge_index[(a, b)]] = sign % RANK_MODULUS
        boundaries.append(vector)
    graph_betti = len(edges) - len(nodes) + components
    boundary_rank = sparse_rank(boundaries)
    return {
        "cutoff": cutoff,
        "nodes": len(nodes),
        "edges": len(edges),
        "components": components,
        "diamonds": len(squares),
        "graph_betti_before_filling": graph_betti,
        "diamond_boundary_rank": boundary_rank,
        "homology_after_filling": graph_betti - boundary_rank,
        "component_invariant": "remove_all_factors_2_and_3",
    }


def expected_twists() -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for k in range(6):
        s_zero = int(k % 2 == 1)
        r_zero = int(k % 3 != 0)
        rows.append({
            "kind": "honest_character",
            "even_character": str(k),
            "odd_character": "",
            "superdimension": "1",
            "s2_relator_word_trace": "1",
            "r3_relator_word_trace": "1",
            "diamond_word_trace": "1",
            "kills_identity_cycle_words": "0",
            "s_norm_polynomial_zero": str(s_zero),
            "r_norm_polynomial_zero": str(r_zero),
            "kills_both_chain_norms": str(s_zero * r_zero),
            "cusp_sr_value": f"t^{(5 * k) % 6}",
            "cusp_sr_nonzero": "1",
        })
    for even in range(6):
        for odd in range(even + 1, 6):
            a = 5 * even % 6
            b = 5 * odd % 6
            s_zero = int(even % 2 == odd % 2)
            r_zero = int(
                (even % 3 == 0) == (odd % 3 == 0)
            )
            rows.append({
                "kind": "zero_superdimension_difference",
                "even_character": str(even),
                "odd_character": str(odd),
                "superdimension": "0",
                "s2_relator_word_trace": "0",
                "r3_relator_word_trace": "0",
                "diamond_word_trace": "0",
                "kills_identity_cycle_words": "1",
                "s_norm_polynomial_zero": str(s_zero),
                "r_norm_polynomial_zero": str(r_zero),
                "kills_both_chain_norms": str(s_zero * r_zero),
                "cusp_sr_value": f"t^{a}-t^{b}",
                "cusp_sr_nonzero": "1",
            })
    return rows


class CheckLedger:
    def __init__(self) -> None:
        self.total = 0
        self.passed = 0
        self.failures: List[Dict[str, object]] = []

    def check(
        self,
        condition: bool,
        scope: str,
        name: str,
        observed: object,
        expected: object,
    ) -> None:
        self.total += 1
        if condition:
            self.passed += 1
        else:
            self.failures.append({
                "scope": scope,
                "check": name,
                "observed": observed,
                "expected": expected,
            })


def ast_imports_project_modules(path: Path) -> List[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    forbidden = {
        "cycle_quotient_core",
        "source_generator",
        "post_census_classifier",
        "generate_results",
    }
    hits: List[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] in forbidden:
                    hits.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] in forbidden:
                hits.append(node.module)
    return sorted(hits)


def rounded(value: float) -> float:
    return round(value, 12)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", default="results")
    args = parser.parse_args()

    result_dir = Path(args.result_dir)
    code_dir = Path(__file__).resolve().parent
    ledger = CheckLedger()

    raw_rows = read_csv(result_dir / "modulus_source_census.csv")
    census = read_csv(result_dir / "modulus_homology_census.csv")
    matched = read_csv(result_dir / "matched_clone.csv")
    random_rows = read_csv(result_dir / "random_action_controls.csv")
    twists = read_csv(result_dir / "twist_census.csv")
    cross_payload = json.loads(
        (result_dir / "cross_square_complex.json").read_text(
            encoding="utf-8"
        )
    )

    ledger.check(
        len(raw_rows) == len(census) == 191,
        "global",
        "modulus_row_counts",
        [len(raw_rows), len(census)],
        [191, 191],
    )
    ledger.check(
        [int(row["modulus"]) for row in census] == list(range(2, 193)),
        "global",
        "modulus_range",
        [row["modulus"] for row in census[:2] + census[-2:]],
        "2,...,192",
    )

    class_values: Dict[str, List[Tuple[int, int]]] = {
        "prime": [],
        "prime_power": [],
        "mixed_composite": [],
    }
    for raw, row in zip(raw_rows, census):
        n = int(row["modulus"])
        scope = f"modulus:{n}"
        for key, value in raw.items():
            ledger.check(
                row[key] == value,
                scope,
                f"raw_column_preserved:{key}",
                row[key],
                value,
            )

        points, s_image, r_image = projective_action(n)
        identity = tuple(range(len(points)))
        s_orbits = orbits(s_image)
        r_orbits = orbits(r_image)
        components = component_count(s_image, r_image)
        relative_betti = relation_dimension(s_image, r_image)
        relation_rank, augmented_rank = adjacency_ranks(s_image, r_image)
        cusps = cusp_count(n)
        cuspidal = relative_betti - (cusps - 1)
        units = units_mod(n)
        cusp = points.index(canonical_point(n, (1, 0), units))
        middle = r_image[cusp]
        end = s_image[middle]
        label = arithmetic_class(n)
        class_values[label].append((relative_betti, cuspidal))

        expected_values = {
            "state_count": len(points),
            "s_orbits": len(s_orbits),
            "r_orbits": len(r_orbits),
            "relation_rank": relation_rank,
            "relative_betti": relative_betti,
            "cusp_count": cusps,
            "cuspidal_betti": cuspidal,
            "cusp_rs_middle_distinct": int(cusp != middle),
            "cusp_rs_returns": int(cusp == end),
            "adjacency_augmented_rank": augmented_rank,
            "adjacency_descends": int(augmented_rank == relation_rank),
            "evaluator_class": label,
            "evaluator_prime": int(label == "prime"),
            "residual_relative_nonzero": int(relative_betti > 0),
            "residual_cuspidal_nonzero": int(cuspidal > 0),
        }
        for key, expected in expected_values.items():
            observed: object = row[key]
            if isinstance(expected, int):
                observed = int(observed)
            ledger.check(
                observed == expected,
                scope,
                key,
                observed,
                expected,
            )
        ledger.check(
            compose(s_image, 2) == identity,
            scope,
            "s_squared_identity",
            compose(s_image, 2) == identity,
            True,
        )
        ledger.check(
            compose(r_image, 3) == identity,
            scope,
            "r_cubed_identity",
            compose(r_image, 3) == identity,
            True,
        )
        ledger.check(
            components == 1,
            scope,
            "transitive_action",
            components,
            1,
        )
        same_s_orbit = any(cusp in orbit and middle in orbit for orbit in s_orbits)
        same_r_orbit = any(cusp in orbit and middle in orbit for orbit in r_orbits)
        ledger.check(
            same_s_orbit and same_r_orbit,
            scope,
            "cusp_difference_orthogonal_to_relation_orbits",
            [same_s_orbit, same_r_orbit],
            [True, True],
        )

    n2 = census[0]
    ledger.check(
        int(n2["relation_rank"]) == 2
        and int(n2["adjacency_augmented_rank"]) == 3,
        "modulus:2",
        "explicit_non_descent_rank_jump",
        [n2["relation_rank"], n2["adjacency_augmented_rank"]],
        [2, 3],
    )

    ledger.check(
        len(matched) == 191,
        "matched",
        "row_count",
        len(matched),
        191,
    )
    for row in matched:
        n = int(row["modulus"])
        scope = f"matched:{n}"
        points, s_image, r_image = projective_action(n)
        original_betti = relation_dimension(s_image, r_image)
        original_rank = len(points) - original_betti
        s_clone, r_clone = relabel(
            s_image,
            r_image,
            1_003_003 + n,
        )
        clone_betti = relation_dimension(s_clone, r_clone)
        clone_rank = len(points) - clone_betti
        expected = {
            "state_count_equal": 1,
            "component_count_equal": int(
                component_count(s_clone, r_clone) == 1
            ),
            "relative_betti_original": original_betti,
            "relative_betti_clone": clone_betti,
            "relation_rank_original": original_rank,
            "relation_rank_clone": clone_rank,
            "transport_exact": int(
                original_betti == clone_betti
                and original_rank == clone_rank
            ),
        }
        for key, value in expected.items():
            observed = int(row[key])
            ledger.check(
                observed == value,
                scope,
                key,
                observed,
                value,
            )

    ledger.check(
        len(random_rows) == 64,
        "random",
        "row_count",
        len(random_rows),
        64,
    )
    random_betti: List[int] = []
    for row in random_rows:
        trial = int(row["trial"])
        seed = int(row["seed"])
        size = int(row["states"])
        scope = f"random:{trial}"
        s_image, r_image, attempts = random_transitive_action(size, seed)
        components = component_count(s_image, r_image)
        residual = relation_dimension(s_image, r_image)
        random_betti.append(residual)
        expected = {
            "seed": 330000 + trial,
            "states": [12, 18, 24, 30, 36, 42, 48, 60, 72][
                trial % 9
            ],
            "sampling_attempts": attempts,
            "s_orbits": len(orbits(s_image)),
            "r_orbits": len(orbits(r_image)),
            "components": components,
            "s2_killed_by_relation_quotient": 1,
            "r3_killed_by_relation_quotient": 1,
            "residual_betti": residual,
            "residual_nonzero": int(residual > 0),
        }
        for key, value in expected.items():
            observed = int(row[key])
            ledger.check(
                observed == value,
                scope,
                key,
                observed,
                value,
            )
        identity = tuple(range(size))
        ledger.check(
            compose(s_image, 2) == identity,
            scope,
            "s_squared_identity",
            compose(s_image, 2) == identity,
            True,
        )
        ledger.check(
            compose(r_image, 3) == identity,
            scope,
            "r_cubed_identity",
            compose(r_image, 3) == identity,
            True,
        )

    expected_twist_rows = expected_twists()
    ledger.check(
        len(twists) == len(expected_twist_rows) == 21,
        "twists",
        "row_count",
        len(twists),
        21,
    )
    for index, (row, expected) in enumerate(
        zip(twists, expected_twist_rows)
    ):
        scope = f"twist:{index}"
        for key, value in expected.items():
            ledger.check(
                row[key] == value,
                scope,
                key,
                row[key],
                value,
            )

    honest = [
        row for row in twists if row["kind"] == "honest_character"
    ]
    virtual = [
        row
        for row in twists
        if row["kind"] == "zero_superdimension_difference"
    ]
    firewall = {
        "honest_identity_cycle_word_killers": sum(
            int(row["kills_identity_cycle_words"]) for row in honest
        ),
        "honest_both_chain_norm_killers": sum(
            int(row["kills_both_chain_norms"]) for row in honest
        ),
        "honest_cusp_nonzero": sum(
            int(row["cusp_sr_nonzero"]) for row in honest
        ),
        "virtual_identity_word_killers": sum(
            int(row["kills_identity_cycle_words"]) for row in virtual
        ),
        "virtual_both_chain_norm_killers": sum(
            int(row["kills_both_chain_norms"]) for row in virtual
        ),
        "virtual_cusp_nonzero": sum(
            int(row["cusp_sr_nonzero"]) for row in virtual
        ),
    }
    expected_firewall = {
        "honest_identity_cycle_word_killers": 0,
        "honest_both_chain_norm_killers": 2,
        "honest_cusp_nonzero": 6,
        "virtual_identity_word_killers": 15,
        "virtual_both_chain_norm_killers": 2,
        "virtual_cusp_nonzero": 15,
    }
    for key, expected in expected_firewall.items():
        ledger.check(
            firewall[key] == expected,
            "twists",
            key,
            firewall[key],
            expected,
        )

    cross_expected = independent_cross(192)
    for key, expected in cross_expected.items():
        ledger.check(
            cross_payload[key] == expected,
            "cross",
            key,
            cross_payload[key],
            expected,
        )

    source_scan = json.loads(
        (result_dir / "source_oracle_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    separation = json.loads(
        (result_dir / "source_separation_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    bridge = json.loads(
        (result_dir / "prototype_bridge_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    imports = ast_imports_project_modules(Path(__file__).resolve())
    ledger.check(
        not imports,
        "firewall",
        "independent_evaluator_imports_no_project_module",
        imports,
        [],
    )
    ledger.check(
        source_scan["pass"] is True and not source_scan["hits"],
        "firewall",
        "prototype_core_source_scan",
        source_scan,
        "pass with zero hits",
    )
    ledger.check(
        separation["pass"] is True
        and not separation["banned_identifier_hits"],
        "firewall",
        "candidate_classifier_physical_separation",
        separation,
        "pass with zero banned identifiers",
    )
    ledger.check(
        bridge["pass"] is True,
        "bridge",
        "prototype_bridge_certificate",
        bridge["pass"],
        True,
    )
    ledger.check(
        bridge["prototype_core_sha256_actual"] == EXPECTED_CORE_SHA256,
        "bridge",
        "core_sha256",
        bridge["prototype_core_sha256_actual"],
        EXPECTED_CORE_SHA256,
    )
    ledger.check(
        bridge["prototype_runner_sha256_actual"] == EXPECTED_RUNNER_SHA256,
        "bridge",
        "runner_sha256",
        bridge["prototype_runner_sha256_actual"],
        EXPECTED_RUNNER_SHA256,
    )
    ledger.check(
        bridge["prototype_payload_aggregate_actual"]
        == EXPECTED_PROTOTYPE_AGGREGATE,
        "bridge",
        "payload_aggregate",
        bridge["prototype_payload_aggregate_actual"],
        EXPECTED_PROTOTYPE_AGGREGATE,
    )

    class_counts = {
        label: {
            "blocks": len(values),
            "relative_nonzero": sum(relative > 0 for relative, _ in values),
            "cuspidal_nonzero": sum(cuspidal > 0 for _, cuspidal in values),
            "relative_betti_sum": sum(relative for relative, _ in values),
            "cuspidal_betti_sum": sum(cuspidal for _, cuspidal in values),
        }
        for label, values in class_values.items()
    }
    expected_class_counts = {
        "prime": {
            "blocks": 43,
            "relative_nonzero": 43,
            "cuspidal_nonzero": 38,
            "relative_betti_sum": 611,
            "cuspidal_betti_sum": 568,
        },
        "prime_power": {
            "blocks": 14,
            "relative_nonzero": 14,
            "cuspidal_nonzero": 9,
            "relative_betti_sum": 189,
            "cuspidal_betti_sum": 82,
        },
        "mixed_composite": {
            "blocks": 134,
            "relative_nonzero": 134,
            "cuspidal_nonzero": 130,
            "relative_betti_sum": 3994,
            "cuspidal_betti_sum": 3068,
        },
    }
    for label, expected_values in expected_class_counts.items():
        for key, expected in expected_values.items():
            ledger.check(
                class_counts[label][key] == expected,
                f"class:{label}",
                key,
                class_counts[label][key],
                expected,
            )

    summary = json.loads(
        (result_dir / "summary.json").read_text(encoding="utf-8")
    )
    ledger.check(
        summary["class_summary"] == class_counts,
        "summary",
        "independent_class_summary",
        summary["class_summary"],
        class_counts,
    )
    ledger.check(
        summary["moduli"] == 191,
        "summary",
        "moduli",
        summary["moduli"],
        191,
    )
    ledger.check(
        summary["matched_clone_exact_rows"] == 191,
        "summary",
        "matched_clone_exact_rows",
        summary["matched_clone_exact_rows"],
        191,
    )
    ledger.check(
        summary["random_controls_residual_nonzero"] == 64,
        "summary",
        "random_controls_residual_nonzero",
        summary["random_controls_residual_nonzero"],
        64,
    )
    ledger.check(
        summary["route_tuple"]
        == [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "summary",
        "route_tuple",
        summary["route_tuple"],
        "strict tuple",
    )
    ledger.check(
        summary["overall"] == "ROUTE_A_REJECTED"
        and summary["route_b"] == "LOCKED",
        "summary",
        "route_closure",
        [summary["overall"], summary["route_b"]],
        ["ROUTE_A_REJECTED", "LOCKED"],
    )

    run_parameters = json.loads(
        (result_dir / "run_parameters.json").read_text(encoding="utf-8")
    )
    ledger.check(
        run_parameters["target_zero_data"] == "none",
        "target_zero",
        "data_absent",
        run_parameters["target_zero_data"],
        "none",
    )

    comparison_rows: List[Dict[str, object]] = []
    for label in ("prime", "prime_power", "mixed_composite"):
        relative = [value[0] for value in class_values[label]]
        cuspidal = [value[1] for value in class_values[label]]
        comparison_rows.append({
            "stratum": label,
            "blocks": len(relative),
            "relative_nonzero": sum(value > 0 for value in relative),
            "cuspidal_nonzero": sum(value > 0 for value in cuspidal),
            "relative_betti_mean": rounded(mean(relative)),
            "relative_betti_population_std": rounded(pstdev(relative)),
            "relative_betti_min": min(relative),
            "relative_betti_max": max(relative),
            "cuspidal_betti_mean": rounded(mean(cuspidal)),
            "cuspidal_betti_population_std": rounded(pstdev(cuspidal)),
            "cuspidal_betti_min": min(cuspidal),
            "cuspidal_betti_max": max(cuspidal),
        })
    write_csv(result_dir / "evaluation_comparison.csv", comparison_rows)

    evaluation = {
        "candidate_id": "SD-C35",
        "evaluation_type": "independent_low_level_reconstruction",
        "imports_candidate_or_generator_modules": False,
        "arithmetic_ground_truth": (
            "independent deterministic division of each modulus"
        ),
        "generator_sequence": "R then S",
        "operator_word_right_to_left_convention": "SR",
        "low_level_checks_passed": ledger.passed,
        "low_level_checks_total": ledger.total,
        "failures": ledger.failures,
        "class_counts": class_counts,
        "character_firewall": firewall,
        "cross": cross_expected,
        "random_control_statistics": {
            "count": len(random_betti),
            "sum": sum(random_betti),
            "min": min(random_betti),
            "max": max(random_betti),
            "mean": rounded(mean(random_betti)),
            "population_std": rounded(pstdev(random_betti)),
        },
        "prototype_bridge": {
            "core_sha256": EXPECTED_CORE_SHA256,
            "runner_sha256": EXPECTED_RUNNER_SHA256,
            "payload_aggregate": EXPECTED_PROTOTYPE_AGGREGATE,
            "tests": "25/25",
        },
        "route_tuple": [
            "A0_STRUCTURAL_ARITHMETIC_RELATION",
            "A1_FAIL",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "target_zero_data_used": False,
        "target_zero_metrics": {
            "zero_error_train": "not_applicable",
            "zero_error_validation": "not_applicable",
            "zero_error_test": "not_applicable",
            "extra_zero_count": "not_applicable",
            "missing_zero_count": "not_applicable",
            "root_count_discrepancy": "not_applicable",
        },
        "branch_action": "CLOSE_SEMIRING_RESIDUE_FAMILY",
        "pass": not ledger.failures,
    }
    (result_dir / "evaluation.json").write_text(
        json.dumps(evaluation, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "candidate_id": "SD-C35",
        "checks": f"{ledger.passed}/{ledger.total}",
        "pass": evaluation["pass"],
    }, sort_keys=True))
    if ledger.failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
