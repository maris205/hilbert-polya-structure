#!/usr/bin/env python3
"""Generate the prime-blind SD-C34 candidate census and source controls."""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
from pathlib import Path
import random
from typing import Dict, List, Sequence, Tuple

from residue_core import (
    ResidueGrammar,
    build_grammar,
    canonical_diamonds,
    canonical_point,
    census_row,
    compose,
    cross_edge_weight_bases,
    permutation_cycle_lengths,
    units_mod,
)


ROOT = Path(__file__).resolve().parents[1]
CORE = Path(__file__).with_name("residue_core.py")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def stable_json(data: object) -> bytes:
    return (json.dumps(data, sort_keys=True, indent=2) + "\n").encode("utf-8")


def write_json(path: Path, data: object) -> None:
    path.write_bytes(stable_json(data))


def write_csv(path: Path, rows: Sequence[Dict[str, object]], fields: Sequence[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def random_relation_action(size: int, seed: int) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    rng = random.Random(seed)
    order = list(range(size))
    rng.shuffle(order)
    s_map = list(range(size))
    for index in range(0, size - 1, 2):
        left, right = order[index], order[index + 1]
        s_map[left], s_map[right] = right, left

    order = list(range(size))
    rng.shuffle(order)
    r_map = list(range(size))
    triple_limit = size - size % 3
    for index in range(0, triple_limit, 3):
        first, second, third = order[index], order[index + 1], order[index + 2]
        r_map[first], r_map[second], r_map[third] = second, third, first
    return tuple(s_map), tuple(r_map)


def matched_semiring_clone_control(
    grammar: ResidueGrammar,
    source_row: Dict[str, int],
    trace_order: int,
    seed: int,
) -> Dict[str, object]:
    """Transport every operation-table entry and projective edge."""

    modulus = grammar.modulus
    rng = random.Random(seed)
    encode_list = list(range(modulus))
    rng.shuffle(encode_list)
    encode = tuple(encode_list)
    decode_list = [0] * modulus
    for old, new in enumerate(encode):
        decode_list[new] = old
    decode = tuple(decode_list)

    def clone_add(left: int, right: int) -> int:
        return encode[(decode[left] + decode[right]) % modulus]

    def clone_mul(left: int, right: int) -> int:
        return encode[(decode[left] * decode[right]) % modulus]

    def clone_neg(value: int) -> int:
        return encode[(-decode[value]) % modulus]

    source_units = units_mod(modulus)

    def canonical_clone_point(point: Tuple[int, int]) -> Tuple[int, int]:
        old_point = decode[point[0]], decode[point[1]]
        representative = canonical_point(modulus, old_point, source_units)
        return encode[representative[0]], encode[representative[1]]

    encoded_source_points = tuple((encode[a], encode[b]) for a, b in grammar.points)
    clone_points = tuple(sorted(encoded_source_points))
    clone_index = {point: index for index, point in enumerate(clone_points)}
    old_to_clone = tuple(clone_index[point] for point in encoded_source_points)

    clone_s: List[int] = []
    clone_r: List[int] = []
    for left, right in clone_points:
        s_point = canonical_clone_point((clone_neg(right), left))
        r_point = canonical_clone_point((clone_neg(right), clone_add(left, right)))
        clone_s.append(clone_index[s_point])
        clone_r.append(clone_index[r_point])

    clone_grammar = ResidueGrammar(modulus, clone_points, tuple(clone_s), tuple(clone_r))
    clone_row = census_row(clone_grammar, trace_order)
    graph_transport_exact = all(
        clone_grammar.s_image[old_to_clone[old]] == old_to_clone[grammar.s_image[old]]
        and clone_grammar.r_image[old_to_clone[old]] == old_to_clone[grammar.r_image[old]]
        for old in range(grammar.size)
    )
    semiring_transport_exact = all(
        clone_add(encode[left], encode[right]) == encode[(left + right) % modulus]
        and clone_mul(encode[left], encode[right]) == encode[(left * right) % modulus]
        for left in range(modulus)
        for right in range(modulus)
    )
    clone_add_table = [
        [clone_add(left, right) for right in range(modulus)]
        for left in range(modulus)
    ]
    clone_mul_table = [
        [clone_mul(left, right) for right in range(modulus)]
        for left in range(modulus)
    ]
    certificate = {
        "transport_seed": seed,
        "element_relabel": encode,
        "state_bijection": old_to_clone,
        "clone_zero": encode[0],
        "clone_one": encode[1],
        "clone_add_table_sha256": sha256_bytes(stable_json(clone_add_table)),
        "clone_mul_table_sha256": sha256_bytes(stable_json(clone_mul_table)),
        "semiring_transport_exact": semiring_transport_exact,
        "graph_transport_exact": graph_transport_exact,
        "source_row_sha256": sha256_bytes(stable_json(source_row)),
        "clone_row_sha256": sha256_bytes(stable_json(clone_row)),
    }
    exact_equal = semiring_transport_exact and graph_transport_exact and clone_row == source_row
    return {
        "modulus": modulus,
        "element_relabel_sha256": sha256_bytes(stable_json(encode)),
        "clone_add_table_sha256": certificate["clone_add_table_sha256"],
        "clone_mul_table_sha256": certificate["clone_mul_table_sha256"],
        "source_row_sha256": certificate["source_row_sha256"],
        "matched_clone_row_sha256": certificate["clone_row_sha256"],
        "transport_certificate_sha256": sha256_bytes(stable_json(certificate)),
        "semiring_transport_exact": int(semiring_transport_exact),
        "graph_transport_exact": int(graph_transport_exact),
        "exact_equal": int(exact_equal),
    }


def source_oracle_certificate() -> Dict[str, object]:
    payload = CORE.read_bytes()
    source = payload.decode("utf-8")
    forbidden_patterns = [
        "is_prime",
        "factor",
        "prime_table",
        "target_zero",
        "riemann",
        "zero_ordinate",
        "requests",
        "urllib",
        "socket",
        "subprocess",
    ]
    hits = [pattern for pattern in forbidden_patterns if pattern in source.lower()]
    tree = ast.parse(source)
    imports = sorted(
        node.names[0].name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import) and node.names
    )
    imports += sorted(
        node.module or ""
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
    )
    return {
        "candidate_core": "residue_core.py",
        "candidate_core_sha256": sha256_bytes(payload),
        "forbidden_patterns": forbidden_patterns,
        "forbidden_hits": hits,
        "imports": sorted(imports),
        "pass": not hits,
        "note": "classification is isolated in independent_evaluator.py after the source census",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--cutoff", type=int, default=192)
    parser.add_argument("--trace-order", type=int, default=8)
    parser.add_argument("--random-trials", type=int, default=48)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    rows: List[Dict[str, object]] = []
    clone_rows: List[Dict[str, object]] = []
    for modulus in range(2, args.cutoff + 1):
        grammar = build_grammar(modulus)
        raw = census_row(grammar, args.trace_order)
        rows.append(dict(raw))
        clone_rows.append(
            matched_semiring_clone_control(
                grammar,
                raw,
                args.trace_order,
                1000003 + modulus,
            )
        )

    raw_fields = [
        "modulus",
        "state_count",
        "projective_defect",
        "s_cycle_count",
        "s_fixed_count",
        "s_two_cycle_count",
        "r_cycle_count",
        "r_fixed_count",
        "r_three_cycle_count",
        "forward_component_size",
        "overlap_state_count",
    ] + [f"trace_{order}" for order in range(1, args.trace_order + 1)]
    write_csv(args.output / "candidate_census.csv", rows, raw_fields)

    clone_fields = [
        "modulus",
        "element_relabel_sha256",
        "clone_add_table_sha256",
        "clone_mul_table_sha256",
        "source_row_sha256",
        "matched_clone_row_sha256",
        "transport_certificate_sha256",
        "semiring_transport_exact",
        "graph_transport_exact",
        "exact_equal",
    ]
    write_csv(args.output / "matched_clone.csv", clone_rows, clone_fields)

    sampled_sizes = sorted({int(row["state_count"]) for row in rows})
    random_rows: List[Dict[str, object]] = []
    for trial in range(args.random_trials):
        size = sampled_sizes[trial % len(sampled_sizes)]
        s_map, r_map = random_relation_action(size, 320000 + trial)
        identity = tuple(range(size))
        s_lengths = permutation_cycle_lengths(s_map)
        r_lengths = permutation_cycle_lengths(r_map)
        random_rows.append(
            {
                "trial": trial,
                "state_count": size,
                "s2_identity": int(compose(s_map, 2) == identity),
                "r3_identity": int(compose(r_map, 3) == identity),
                "s_cycle_count": len(s_lengths),
                "r_cycle_count": len(r_lengths),
                "overlap_state_count": size,
                "universal_recurrence_nonzero": int(bool(s_lengths) and bool(r_lengths)),
            }
        )
    write_csv(
        args.output / "random_relation_controls.csv",
        random_rows,
        [
            "trial",
            "state_count",
            "s2_identity",
            "r3_identity",
            "s_cycle_count",
            "r_cycle_count",
            "overlap_state_count",
            "universal_recurrence_nonzero",
        ],
    )

    diamonds = []
    for modulus, doubled, sextupled, tripled in canonical_diamonds(args.cutoff):
        bases = cross_edge_weight_bases(modulus)
        diamonds.append(
            {
                "base_modulus": modulus,
                "cycle_vertices": [modulus, doubled, sextupled, tripled],
                "top_modulus": sextupled,
                "simple_length": 4,
                "nonbacktracking": 1,
                "weight_bases": list(bases),
                "weight_base_product": bases[0] * bases[1] * bases[2] * bases[3],
                "expected_product": 216 * modulus**4,
            }
        )
    write_json(args.output / "candidate_diamonds.json", diamonds)
    write_json(args.output / "source_oracle_certificate.json", source_oracle_certificate())
    write_json(
        args.output / "bare_ufd_control.json",
        {
            "candidate_id": "SD-C34",
            "control": "ordinary_polynomial_UFD_presentation",
            "source_relation": "2=1+1",
            "transported_required_value": "x_2",
            "ordinary_polynomial_sum": "(1)+(1)",
            "ordinary_addition_matches": False,
            "source_lock_passes": False,
            "interpretation": "inherited bare clone failure; not a universal clone separation",
            "target_zero_data_used": False,
            "route_b_invocation_allowed": False,
        },
    )
    print(
        json.dumps(
            {
                "candidate_rows": len(rows),
                "matched_rows": len(clone_rows),
                "random_rows": len(random_rows),
                "diamonds": len(diamonds),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
