#!/usr/bin/env python3
"""Exactly the six literals and 105 boxes frozen in INTAKE.md.

Self-contained standard-library author pilot. No files are written.
"""
from collections import Counter
from functools import lru_cache
from itertools import permutations, product
import hashlib
import json


def partitions(total, cap=None):
    if total == 0:
        yield ()
        return
    if cap is None:
        cap = total
    for first in range(min(total, cap), 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def wgp(partition):
    padded = partition + (0,)
    return tuple(sorted((i * (padded[i - 1] - padded[i])
                         for i in range(1, len(padded))
                         if padded[i - 1] > padded[i]), reverse=True))


def dsr(partition):
    durfee = sum(value >= i for i, value in enumerate(partition, 1))
    residual = [value - durfee if i < durfee else value
                for i, value in enumerate(partition)]
    if durfee:
        residual.append(durfee * durfee)
    return tuple(sorted((value for value in residual if value), reverse=True))


@lru_cache(None)
def cofactor_monomials(n):
    result = []
    for i in range(n):
        for j in range(n):
            rows = [row for row in range(n) if row != j]
            columns = [column for column in range(n) if column != i]
            result.append(tuple(sum(1 << (row * n + column)
                                    for row, column in zip(rows, perm))
                                for perm in permutations(columns)))
    return tuple(result)


def upa(matrix, n):
    result = 0
    for index, monomials in enumerate(cofactor_monomials(n)):
        count = sum(matrix & monomial == monomial for monomial in monomials)
        if count == 1:
            result |= 1 << index
    return result


@lru_cache(None)
def dag_pairs(n):
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


def dp3(relation, n):
    adjacency = [[0] * n for _ in range(n)]
    for index, (i, j) in enumerate(dag_pairs(n)):
        adjacency[i][j] = (relation >> index) & 1
    paths = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            paths[i][j] = (adjacency[i][j]
                           + sum(adjacency[i][k] * paths[k][j]
                                 for k in range(i + 1, j))) % 3
    return sum(1 << index for index, (i, j) in enumerate(dag_pairs(n))
               if paths[i][j] == 1)


def brf(function):
    counts = [0] * len(function)
    for start in range(1, len(function) + 1):
        seen = set()
        vertex = start
        while vertex not in seen:
            seen.add(vertex)
            counts[vertex - 1] += 1
            vertex = function[vertex - 1]
    return tuple(counts)


def ffr(items, capacity):
    remaining = []
    assigned = []
    for item in items:
        index = next((i for i, space in enumerate(remaining) if space >= item),
                     len(remaining))
        if index == len(remaining):
            remaining.append(capacity)
        remaining[index] -= item
        assigned.append(index)
    return tuple(remaining[i] for i in assigned)


def profile(states, step):
    states = list(states)
    assert len(states) == len(set(states)), "duplicate carrier state"
    arrows = {state: step(state) for state in states}
    assert set(arrows.values()) <= set(states), "carrier closure failure"
    indegrees = Counter(arrows.values())
    position_data = {}
    cycle_counts = Counter()
    longest_cycle = ()
    for start in states:
        if start in position_data:
            continue
        walk, seen = [], {}
        vertex = start
        while vertex not in seen and vertex not in position_data:
            seen[vertex] = len(walk)
            walk.append(vertex)
            vertex = arrows[vertex]
        if vertex in seen:
            cut = seen[vertex]
            cycle = walk[cut:]
            length = len(cycle)
            cycle_counts[length] += 1
            least_index = cycle.index(min(cycle))
            normalized = tuple(cycle[least_index:] + cycle[:least_index])
            if (len(normalized), normalized) > (len(longest_cycle), longest_cycle):
                longest_cycle = normalized
            for member in cycle:
                position_data[member] = (0, length)
            transient = walk[:cut]
        else:
            transient = walk
        for member in reversed(transient):
            child_height, child_period = position_data[arrows[member]]
            position_data[member] = (child_height + 1, child_period)
    assert len(position_data) == len(states)
    recurrent = sum(height == 0 for height, _ in position_data.values())
    assert recurrent == sum(length * count for length, count in cycle_counts.items())
    assert sum(indegrees.values()) == len(states)
    maximum_height = max(height for height, _ in position_data.values())
    height_witness = min(state for state in states
                         if position_data[state][0] == maximum_height)
    height_orbit = [height_witness]
    for _ in range(maximum_height + position_data[height_witness][1]):
        height_orbit.append(arrows[height_orbit[-1]])
    maximum_fibre = max(indegrees.values())
    maximum_targets = sorted(target for target, count in indegrees.items()
                             if count == maximum_fibre)
    encoded_arrows = json.dumps(sorted(arrows.items()), separators=(",", ":")).encode()
    return {"states": len(states), "image": len(indegrees),
            "recurrent": recurrent, "fixed": cycle_counts.get(1, 0),
            "cycles": dict(sorted(cycle_counts.items())), "height": maximum_height,
            "height_witness_orbit": height_orbit,
            "max_fibre": maximum_fibre,
            "max_fibre_targets": maximum_targets,
            "longest_cycle": longest_cycle,
            "transition_sha256": hashlib.sha256(encoded_arrows).hexdigest()}


def boxes():
    for name, step in (("WGP", wgp), ("DSR", dsr)):
        for total in range(25):
            yield name, {"N": total}, partitions(total), step
    for n in range(5):
        yield "UPA", {"n": n}, range(1 << (n * n)), lambda a, n=n: upa(a, n)
    for n in range(7):
        yield "DP3", {"n": n}, range(1 << (n * (n - 1) // 2)), lambda a, n=n: dp3(a, n)
    for n in range(7):
        yield "BRF", {"n": n}, product(range(1, n + 1), repeat=n), brf
    for capacity in range(6):
        for count in range(6):
            yield "FFR", {"M": capacity, "k": count}, product(range(capacity + 1), repeat=count), lambda a, capacity=capacity: ffr(a, capacity)


def main():
    count = 0
    for name, parameters, states, step in boxes():
        result = {"literal": name, "parameters": parameters,
                  "status": "PASS_FINITE_PILOT_ONLY", **profile(states, step)}
        print(json.dumps(result, sort_keys=True, separators=(",", ":")), flush=True)
        count += 1
    assert count == 105


if __name__ == "__main__":
    main()
