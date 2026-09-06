#!/usr/bin/env python3
"""Bounded, self-contained LUB static-adapter checks, n=1,...,6 only.

Threshold-graph BFS supplies the forward map. Recursive strict heap
labellings independently supply every source set. No root pilot import.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from math import comb, prod

checks = 0
digest = sha256()


def require(statement):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(checks)


def components(word, upper=True):
    n = len(word)
    result = [0] * n
    for level in sorted(set(word)):
        allowed = {i for i, value in enumerate(word)
                   if (value >= level if upper else value <= level)}
        unseen = set(allowed)
        while unseen:
            start = min(unseen)
            queue, found = [start], {start}
            unseen.remove(start)
            for vertex in queue:
                for neighbour in ((vertex - 1) % n, (vertex + 1) % n):
                    if neighbour in unseen:
                        unseen.remove(neighbour)
                        found.add(neighbour)
                        queue.append(neighbour)
            mask = sum(1 << i for i in found)
            for i in found:
                if word[i] == level:
                    result[i] = mask
    return tuple(result)


def step(word, upper=True):
    return tuple(mask.bit_count() for mask in components(word, upper))


def scan_step(word):
    """Strict-smaller directional stopping, crosschecked against graph BFS."""
    n = len(word)
    answer = []
    for i, value in enumerate(word):
        if value == min(word):
            answer.append(n)
            continue
        left = next(d for d in range(1, n) if word[(i - d) % n] < value)
        right = next(d for d in range(1, n) if word[(i + d) % n] < value)
        answer.append(left + right - 1)
    return tuple(answer)


def target_tree(target):
    masks = sorted(set(components(target, False)), key=lambda a: (-a.bit_count(), a))
    n = len(target)
    require(masks[0] == (1 << n) - 1)
    parents = [-1]
    for node, mask in enumerate(masks[1:], 1):
        ancestors = [j for j in range(node) if mask & masks[j] == mask]
        require(bool(ancestors))
        parents.append(min(ancestors, key=lambda j: masks[j].bit_count()))
    children = [[] for _ in masks]
    for node in range(1, len(masks)):
        children[parents[node]].append(node)
    atoms = []
    for node, mask in enumerate(masks):
        union = 0
        for child in children[node]:
            require(not (union & masks[child]))
            union |= masks[child]
        atom = mask ^ union
        require(bool(atom))
        require(all(target[i] == mask.bit_count() for i in range(n) if atom >> i & 1))
        atoms.append(atom)
    require(sum(atom.bit_count() for atom in atoms) == n)
    return tuple(masks), tuple(parents), tuple(tuple(c) for c in children), tuple(atoms)


def order_count(children, alphabet):
    @lru_cache(None)
    def count(node, available):
        return sum(prod(count(child, available - label) for child in children[node])
                   for label in range(1, available + 1))
    return count(0, alphabet)


def reconstruct_sources(parents, atoms, n):
    heights = [0] * len(parents)
    result = set()

    def visit(node):
        if node == len(parents):
            word = [0] * n
            for label, atom in zip(heights, atoms):
                for i in range(n):
                    if atom >> i & 1:
                        word[i] = label
            result.add(tuple(word))
            return
        minimum = 1 if node == 0 else heights[parents[node]] + 1
        for value in range(minimum, n + 1):
            heights[node] = value
            visit(node + 1)

    visit(0)
    return result


def profile(forward):
    tail, periods, cycles = {}, {}, Counter()
    for start in forward:
        if start in tail:
            continue
        path, local = [], {}
        current = start
        while current not in tail and current not in local:
            local[current] = len(path)
            path.append(current)
            current = forward[current]
        if current not in tail:
            cut = local[current]
            cycle = path[cut:]
            cycles[len(cycle)] += 1
            for vertex in cycle:
                tail[vertex], periods[vertex] = 0, len(cycle)
            path = path[:cut]
        for vertex in reversed(path):
            tail[vertex], periods[vertex] = tail[forward[vertex]] + 1, periods[forward[vertex]]
    for word, target in forward.items():
        require(periods[word] == periods[target])
        require(tail[word] == 0 or tail[word] == tail[target] + 1)
    return tail, periods, cycles


def main():
    rows = []
    total_sources = total_images = 0
    for n in range(1, 7):
        words = list(product(range(1, n + 1), repeat=n))
        forward, fibres = {}, defaultdict(set)
        for word in words:
            upper = components(word)
            target = tuple(mask.bit_count() for mask in upper)
            require(target == scan_step(word))
            require(components(target, False) == upper)
            require(step(target, False) == target)
            lower = step(word, False)
            require(step(lower, False) == lower)
            for i in range(n):
                j = (i + 1) % n
                require((word[i] == word[j]) == (target[i] == target[j]))
                require(word[i] == word[j] or (word[i] - word[j]) * (target[i] - target[j]) < 0)
            forward[word] = target
            fibres[target].add(word)
            digest.update(json.dumps([n, word, target, upper], separators=(",", ":")).encode())
            digest.update(b"\n")
        for target in words:
            require((step(target, False) == target) == (target in fibres))
        for target, sources in sorted(fibres.items()):
            require(forward[tuple(n + 1 - value for value in target)] == target)
            masks, parents, children, atoms = target_tree(target)
            counted = order_count(children, n)
            rebuilt = reconstruct_sources(parents, atoms, n)
            require(counted == len(sources))
            require(rebuilt == sources)
            require(len(rebuilt) == counted)
            for source in sources:
                heights = []
                for atom in atoms:
                    labels = {source[i] for i in range(n) if atom >> i & 1}
                    require(len(labels) == 1)
                    heights.append(next(iter(labels)))
                require(all(heights[parents[i]] < heights[i] for i in range(1, len(parents))))
            digest.update(json.dumps([n, target, masks, parents, atoms, counted], separators=(",", ":")).encode())
            digest.update(b"\n")
        require(len(fibres) == sum(comb(n - 1, k) * comb(n - 1 + k, k) for k in range(n)))
        tail, periods, cycles = profile(forward)
        require({w for w, target in forward.items() if w == target} == {(n,) * n})
        rows.append({"n": n, "states": len(words), "image": len(fibres),
                     "recurrent": sum(value == 0 for value in tail.values()),
                     "cycles_by_length": dict(sorted(cycles.items())), "height": max(tail.values()),
                     "maximum_fibre": max(map(len, fibres.values())),
                     "inverse_source_sets_compared": len(fibres)})
        total_sources += len(words)
        total_images += len(fibres)
    witnesses = []
    for word in ((1, 3, 2, 3), (1, 1, 2, 1, 2)):
        orbit = [word]
        for _ in range(3):
            orbit.append(step(orbit[-1]))
        witnesses.append(orbit)
    require(any(a < b for a, b in zip(witnesses[0][1], witnesses[0][3])))
    require(any(a > b for a, b in zip(witnesses[1][1], witnesses[1][3])))
    print(json.dumps({"status": "STATIC_ADAPTER_VERIFIED_NO_PROMOTION", "assertions": checks,
                      "sources": total_sources, "image_targets": total_images,
                      "full_parameter_temporal_claim": "NOT_PROVED",
                      "enumeration_sha256": digest.hexdigest(),
                      "nonmonotonicity_witness_orbits": witnesses,
                      "profiles": rows}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
