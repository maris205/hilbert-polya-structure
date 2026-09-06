#!/usr/bin/env python3
"""Four fixed, declared HVD proof/source sentinels; no full-box enumeration."""
import json


def edges(word):
    return {(i, j) for i in range(len(word)) for j in range(i + 1, len(word))
            if all(word[k] < min(word[i], word[j]) for k in range(i + 1, j))}


def step(word):
    graph = edges(word)
    return tuple(sum(i in edge for edge in graph) for i in range(len(word)))


def record(word):
    states = [tuple(word)]
    for _ in range(3):
        states.append(step(states[-1]))
    return {"states": states, "edge_sets": [sorted(edges(x)) for x in states],
            "edge_counts": [len(edges(x)) for x in states],
            "square_norms": [sum(a * a for a in x) for x in states]}


def main():
    parent = record((0, 2, 1, 1, 0, 2))
    first = record((3, 2, 2, 1, 2, 2, 3))
    second = record((2, 1, 2, 2, 2, 1, 2))
    edge_increase = record((0, 2, 1, 2, 2, 2, 1, 2, 0))
    assert parent["states"][1:3] == [(1, 3, 2, 3, 2, 3), (1, 3, 2, 4, 2, 2)]
    assert (1, 3) not in parent["edge_sets"][0] and (1, 3) in parent["edge_sets"][1]
    assert parent["square_norms"][1:3] == [36, 38]
    assert first["states"][1] == second["states"][1] == (2, 2, 3, 2, 3, 2, 2)
    assert first["edge_sets"][0] != second["edge_sets"][0]
    assert edge_increase["edge_counts"][:2] == [10, 11]
    assert edge_increase["states"][1] == (1, 3, 2, 3, 2, 3, 2, 3, 1)
    print(json.dumps({"status": "PASS_NAMED_SENTINELS_ONLY", "assertions": 7,
                      "new_full_boxes": 0, "parent_n6": parent,
                      "primary_2021_figure6_first": first, "primary_2021_figure6_second": second,
                      "derived_n9_edge_count_increase": edge_increase}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
