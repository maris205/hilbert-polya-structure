#!/usr/bin/env python3
"""Independent AM1 original-square functional-graph check, no pruning."""

import argparse
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import sys


BOUND = 19
PARAMETERS = tuple(range(-145, 2))


def original_step(point, a):
    x, y = point
    return (y, y * (y + 1) // 2 + a - x)


def rotation_minimum(word):
    return min(tuple(word[j:] + word[:j]) for j in range(len(word)))


def states_of(word):
    return {(word[j], word[(j + 1) % len(word)]) for j in range(len(word))}


def verify_cycle(word, a):
    states = states_of(word)
    if not word or len(states) != len(word):
        raise AssertionError((a, "nonprimitive cycle", word))
    for j in range(len(word)):
        expected = (word[(j + 1) % len(word)], word[(j + 2) % len(word)])
        if original_step((word[j], word[(j + 1) % len(word)]), a) != expected:
            raise AssertionError((a, "wrong recurrence", word, j))
    return states


def independent_graph(a):
    vertices = tuple((x, y) for x in range(-BOUND, BOUND + 1)
                     for y in range(-BOUND, BOUND + 1))
    vertex_set = set(vertices)
    successor = {v: original_step(v, a) for v in vertices}
    completed = set()
    cycles = []
    cycle_states = set()
    traversed = 0
    for start in vertices:
        if start in completed:
            continue
        path = []
        position = {}
        point = start
        while point in vertex_set and point not in completed and point not in position:
            position[point] = len(path)
            path.append(point)
            traversed += 1
            point = successor[point]
        if point in position:
            cycle = path[position[point]:]
            word = rotation_minimum([v[0] for v in cycle])
            expanded = verify_cycle(word, a)
            if expanded != set(cycle) or expanded.intersection(cycle_states):
                raise AssertionError((a, "cycle extraction mismatch"))
            cycle_states.update(expanded)
            cycles.append(word)
        completed.update(path)
    if completed != vertex_set or traversed != len(vertices):
        raise AssertionError((a, "functional graph not completely processed"))
    if len(cycles) != len(set(cycles)):
        raise AssertionError((a, "duplicate oriented cycle"))
    if {successor[v] for v in cycle_states} != cycle_states:
        raise AssertionError((a, "periodic set is not invariant"))
    return {
        "a": a,
        "original_coordinate_bound": BOUND,
        "graph_vertex_count": len(vertices),
        "vertices_processed_once": traversed,
        "out_of_box_edges": sum(v not in vertex_set for v in successor.values()),
        "oriented_cycle_words": sorted(cycles),
        "least_period_histogram": dict(sorted(Counter(map(len, cycles)).items())),
        "periodic_points": len(cycle_states),
        "periodic_states": sorted(cycle_states),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--author-result", required=True, type=Path)
    parser.add_argument("--author-producer", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists() or args.output.is_symlink():
        raise FileExistsError(args.output)

    # Author output is deliberately not loaded until our whole computation ends.
    independent = [independent_graph(a) for a in PARAMETERS]
    author_bytes = args.author_result.read_bytes()
    author = json.loads(author_bytes)
    author_rows = author["parameters"]
    if [row["a"] for row in author_rows] != list(PARAMETERS):
        raise AssertionError("author parameter range/order mismatch")
    if ((author["parameter_min"], author["parameter_max"], author["parameter_count"])
            != (-145, 1, 147)):
        raise AssertionError("author parameter metadata mismatch")
    if author["period_cutoff"] is not None:
        raise AssertionError("unexpected author period cutoff")
    producer_hash = sha256(args.author_producer.read_bytes()).hexdigest()
    if author["script_sha256"] != producer_hash:
        raise AssertionError("author producer has changed since its certificate")

    for computed, claimed in zip(independent, author_rows):
        a = computed["a"]
        words = [tuple(c["word"]) for c in claimed["cycles"]]
        claimed_states = set()
        for c, word in zip(claimed["cycles"], words):
            if c["least_period"] != len(word) or rotation_minimum(list(word)) != word:
                raise AssertionError((a, "author word labeling mismatch"))
            expanded = verify_cycle(word, a)
            if claimed_states.intersection(expanded):
                raise AssertionError((a, "author cycles overlap"))
            claimed_states.update(expanded)
        if sorted(words) != computed["oriented_cycle_words"]:
            raise AssertionError((a, "full oriented cycle mismatch", words, computed))
        if claimed_states != set(computed["periodic_states"]):
            raise AssertionError((a, "periodic state mismatch"))
        if claimed["periodic_points"] != computed["periodic_points"]:
            raise AssertionError((a, "periodic cardinality mismatch"))
        if claimed["oriented_cycles"] != len(words):
            raise AssertionError((a, "cycle cardinality mismatch"))
        if {int(k): v for k, v in claimed["least_period_cycle_counts"].items()} != computed["least_period_histogram"]:
            raise AssertionError((a, "period histogram mismatch"))
        computed["author_cycle_and_state_match"] = True

    all_periods = sorted({len(w) for row in independent for w in row["oriented_cycle_words"]})
    max_points = max(row["periodic_points"] for row in independent)
    summary = {
        "all_147_full_cycle_and_state_sets_match": True,
        "all_graph_vertices_processed_once": sum(r["vertices_processed_once"] for r in independent),
        "total_periodic_points_across_parameters": sum(r["periodic_points"] for r in independent),
        "total_oriented_cycles_across_parameters": sum(len(r["oriented_cycle_words"]) for r in independent),
        "least_periods": all_periods,
        "maximum_points_at_one_parameter": max_points,
        "parameters_at_maximum": [r["a"] for r in independent if r["periodic_points"] == max_points],
    }
    for key in ("total_periodic_points_across_parameters", "total_oriented_cycles_across_parameters",
                "least_periods", "maximum_points_at_one_parameter", "parameters_at_maximum"):
        if summary[key] != author["summary"][key]:
            raise AssertionError(("author summary mismatch", key))
    document = {
        "schema": "am1_independent_original_square/1",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": sys.version,
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "author_result_sha256": sha256(author_bytes).hexdigest(),
        "author_producer_sha256_read_not_run": producer_hash,
        "algorithm": "path-index functional graph cycle extraction on the full original square",
        "no_filtered_alphabet": True,
        "no_iterative_pruning": True,
        "period_cutoff": None,
        "summary": summary,
        "parameters": independent,
    }
    with args.output.open("x", encoding="utf-8") as output:
        json.dump(document, output, indent=2, sort_keys=True)
        output.write("\n")
    print(json.dumps(summary, sort_keys=True, indent=2))
    print("output_sha256=" + sha256(args.output.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
