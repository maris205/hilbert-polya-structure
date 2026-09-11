#!/usr/bin/env python3
"""P199 author verifier: ordered child arrays and complete functional graphs.

Adapted byte-for-byte in mathematics from this author's earlier Stage-1
control. This reuse is NOT an independent paper-review implementation.

No author modules are imported.  Trees, surgery, reverse cuts, and the graph
are constructed here.  The graph's tails/cycles are found without the claimed
clock.  The word literal is used only as a cross-representation check.
"""

from collections import Counter, deque
from math import factorial, prod
import argparse

CHECKS = 0


def require(test, label):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(label)


def trees(n):
    if n == 0:
        yield ((),)
    else:
        for smaller in trees(n - 1):
            for parent in range(n):
                for slot in range(len(smaller[parent]) + 1):
                    rows = list(smaller) + [()]
                    rows[parent] = rows[parent][:slot] + (n,) + rows[parent][slot:]
                    yield tuple(rows)


def contour(tree):
    word = []

    def visit(vertex):
        for child in tree[vertex]:
            word.append(child)
            visit(child)
            word.append(child)

    visit(0)
    return tuple(word)


def surgery(tree):
    n = len(tree) - 1
    if n < 2:
        return tree
    root = list(tree[0])
    slot = root.index(1)
    root[slot:slot + 1] = [n + 1] + list(tree[1])
    return (tuple(v - 1 for v in root),) + tuple(
        tuple(v - 1 for v in tree[j]) for j in range(2, n + 1)
    ) + ((),)


def literal(word):
    n = len(word) // 2
    output = []
    for value in word:
        if value == 1:
            if n not in output:
                output.extend((n, n))
        else:
            output.append(value - 1)
    return tuple(output)


def left_join(word, label):
    first = word.index(label)
    second = word.index(label, first + 1)
    return word[:first + 1] + (label,) + word[first + 1:second] + word[second + 1:]


def inverse_cuts(target):
    n = len(target) - 1
    if n == 0:
        return {target}
    if n not in target[0]:
        return set()
    slot = target[0].index(n)
    out = set()
    for cut in range(len(target[0]) - slot):
        adopted = target[0][slot + 1:slot + 1 + cut]
        roots = target[0][:slot] + (0,) + target[0][slot + 1 + cut:]
        rows = [tuple(v + 1 for v in roots), tuple(v + 1 for v in adopted)]
        rows.extend(tuple(v + 1 for v in target[j]) for j in range(1, n))
        out.add(tuple(rows))
    return out


def functional_graph(successor):
    incoming = [[] for _ in successor]
    for i, j in enumerate(successor):
        incoming[j].append(i)
    degree = [len(row) for row in incoming]
    queue = deque(i for i, d in enumerate(degree) if d == 0)
    peeled = []
    while queue:
        i = queue.popleft()
        peeled.append(i)
        j = successor[i]
        degree[j] -= 1
        if degree[j] == 0:
            queue.append(j)
    tails = [0] * len(successor)
    periods = [0] * len(successor)
    cycle_lengths = []
    for i, d in enumerate(degree):
        if d and not periods[i]:
            cycle = [i]
            j = successor[i]
            while j != i:
                cycle.append(j)
                j = successor[j]
            cycle_lengths.append(len(cycle))
            for j in cycle:
                periods[j] = len(cycle)
    for i in reversed(peeled):
        tails[i] = tails[successor[i]] + 1
        periods[i] = periods[successor[i]]
    return incoming, tails, periods, cycle_lengths


def run_rank(n):
    states = list(trees(n))
    index = {tree: i for i, tree in enumerate(states)}
    size = prod(range(1, 2 * n, 2))
    require(len(states) == len(index) == size, "unique complete tree carrier")
    successors = []
    for tree in states:
        target = surgery(tree)
        require(target in index, "tree-map closure")
        successors.append(index[target])
        word = contour(tree)
        require(contour(target) == literal(word), "word/tree dictionary")
        old_internal = {j for j in range(1, n + 1) if tree[j]}
        new_internal = {j for j in range(1, n + 1) if target[j]}
        require(new_internal == {j - 1 for j in old_internal if j > 1}, "set transport")
        if n:
            joined = left_join(word, 1)
            cycled = tuple(n if j == 1 else j - 1 for j in joined)
            require(cycled == contour(target), "Brualdi-Dahl local factor T=cJ1")
        if 0 < n <= 5:
            for a in range(1, n + 1):
                require(left_join(left_join(word, a), a) == left_join(word, a), "join idempotence")
                for b in range(1, n + 1):
                    require(left_join(left_join(word, a), b) == left_join(left_join(word, b), a), "join commutation")

    incoming, tails, periods, cycles = functional_graph(successors)
    depths = Counter(tails)
    observed_max = max(map(len, incoming))
    max_targets = 0
    root_degree = Counter(len(tree[0]) for tree in states)
    for i, tree in enumerate(states):
        clock = max((j for j in range(1, n + 1) if tree[j]), default=0)
        require(tails[i] == clock, "graph-derived exact point tail")
        require(periods[i] == max(1, n), "graph-derived eventual exact period")
        require((tails[i] == 0) == (len(tree[0]) == n), "graph-derived recurrent iff star")
        reverse = inverse_cuts(tree)
        require(reverse == {states[j] for j in incoming[i]}, "entire target inverse set")
        fibre = 1 if n == 0 else (len(tree[0]) - tree[0].index(n) if n in tree[0] else 0)
        require(len(incoming[i]) == fibre, "target fibre formula including zero")
        maximum_characterization = n == 0 or (len(tree[0]) == n and tree[0][0] == n)
        require((len(incoming[i]) == max(1, n)) == maximum_characterization, "all maximum targets")
        max_targets += len(incoming[i]) == observed_max
    image = sum(bool(row) for row in incoming)
    require(image == (1 if n == 0 else 2 ** (n - 1) * factorial(n - 1)), "image count")
    require(observed_max == max(1, n), "maximum fibre")
    require(max_targets == factorial(max(0, n - 1)), "maximum target census")
    require(depths[0] == factorial(n), "recurrent census")
    require(Counter(cycles) == {max(1, n): factorial(n) // max(1, n)}, "exact cycle census")
    require(max(tails) == max(0, n - 1), "sharp tail")
    require(sum(len(row) for row in incoming) == size, "fibre mass")
    previous = 0
    for t in range(max(1, n)):
        cumulative = 1 if n == 0 else factorial(n + t) // (2 ** t * factorial(t))
        require(sum(depths[s] for s in range(t + 1)) == cumulative, "depth CDF")
        require(depths[t] == cumulative - previous, "exact layer difference")
        previous = cumulative
    require(sum((d + 1) * count for d, count in root_degree.items()) == 2 ** n * factorial(n), "root-gap image precursor")
    print(f"n={n} states={size} image={image} recurrent={depths[0]} tail={max(tails)} cycles={dict(sorted(Counter(cycles).items()))} max_fibre={observed_max} max_targets={max_targets} depths={tuple(depths[t] for t in range(max(tails)+1))}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=7)
    maximum = parser.parse_args().max_n
    if not 0 <= maximum <= 7:
        parser.error("complete functional-graph control supports 0 <= n <= 7")
    print("P199_AUTHOR_TREE_GRAPH_CONTROL")
    print("author_imports=none;tails=Kahn_peeling;inverse=full_set_comparison")
    for n in range(maximum + 1):
        run_rank(n)
    print(f"assertions={CHECKS}")
    print("PASS_BOUNDED_CONTROL_NOT_NOVELTY_OR_PAPER_REVIEW")


if __name__ == "__main__":
    main()
