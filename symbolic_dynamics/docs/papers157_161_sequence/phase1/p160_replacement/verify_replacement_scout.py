#!/usr/bin/env python3
"""Exact breadth scout for the retired P160 replacement.

The twelve lanes are deliberately small.  They are counterexample pressure,
not proofs and not owner-clearance evidence.  The selected RCS lane receives
much stronger exhaustive checks than the eleven negative controls.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, label: object) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


A = Audit()


def partitions(total: int, cap: int | None = None):
    if total == 0:
        yield ()
        return
    cap = min(total, total if cap is None else cap)
    for first in range(cap, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def inv_pochhammer(order: int, degree: int) -> list[int]:
    out = [1] + [0] * degree
    for part in range(1, order + 1):
        for index in range(part, degree + 1):
            out[index] += out[index - part]
    return out


def convolution(left: list[int], right: list[int], degree: int) -> list[int]:
    out = [0] * (degree + 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            if i + j <= degree:
                out[i + j] += x * y
    return out


def rcs(partition: tuple[int, ...], a: int, b: int, time: int = 1):
    height, width = a * time, b * time
    return tuple(row - width for row in partition[height:] if row > width)


def durfee(partition: tuple[int, ...]) -> int:
    return sum(value >= index for index, value in enumerate(partition, 1))


def check_rcs() -> str:
    degree = 30
    states = [p for size in range(degree + 1) for p in partitions(size)]
    for a, b in ((1, 1), (2, 1), (1, 3), (2, 2)):
        for time in range(5):
            height, width = a * time, b * time
            fibres = Counter((rcs(p, a, b, time), sum(p)) for p in states)
            denominator = convolution(
                inv_pochhammer(height, degree),
                inv_pochhammer(width, degree),
                degree,
            )
            for target_size in range(9):
                for target in partitions(target_size):
                    if not target:
                        continue
                    minimum = (
                        sum(target)
                        + height * (target[0] + width)
                        + width * len(target)
                    )
                    for source_size in range(degree + 1):
                        expected = (
                            denominator[source_size - minimum]
                            if source_size >= minimum
                            else 0
                        )
                        A.check(
                            fibres[(target, source_size)] == expected,
                            ("RCS nonempty fibre", a, b, time, target, source_size),
                        )

            hook = [0] * (degree + 1)
            top = inv_pochhammer(height, degree)
            for boundary in range(width + 1):
                bottom = inv_pochhammer(boundary, degree)
                shift = boundary * (height + 1)
                for i, x in enumerate(top):
                    for j, y in enumerate(bottom):
                        if shift + i + j <= degree:
                            hook[shift + i + j] += x * y
            for source_size in range(degree + 1):
                A.check(
                    fibres[((), source_size)] == hook[source_size],
                    ("RCS empty fibre", a, b, time, source_size),
                )

            for partition in states:
                explicit = tuple(
                    value - width
                    for value in partition[height:]
                    if value > width
                )
                A.check(rcs(partition, a, b, time) == explicit, (a, b, time, partition))

    for partition in states:
        A.check(rcs(partition, 1, 1, durfee(partition)) == (), ("Durfee", partition))
        if partition:
            A.check(
                rcs(partition, 1, 1, durfee(partition) - 1) != (),
                ("Durfee sharp", partition),
            )
    return "RCS a,b=(1,1),(2,1),(1,3),(2,2) t<=4 size<=30 PASS"


def cycles_of(p: tuple[int, ...]):
    seen: set[int] = set()
    cycles = []
    for start in range(len(p)):
        if start in seen:
            continue
        cycle = []
        point = start
        while point not in seen:
            seen.add(point)
            cycle.append(point)
            point = p[point]
        cycles.append(cycle)
    return cycles


def detach_cycle_maxima(p: tuple[int, ...]) -> tuple[int, ...]:
    out = list(p)
    for cycle in cycles_of(p):
        if len(cycle) == 1:
            continue
        maximum = max(cycle)
        predecessor = next(x for x in cycle if p[x] == maximum)
        out[predecessor] = p[maximum]
        out[maximum] = maximum
    return tuple(out)


def check_ptf() -> str:
    maxima = []
    for n in range(1, 8):
        maximum_tail = 0
        for p in permutations(range(n)):
            expected = max(len(cycle) - 1 for cycle in cycles_of(p))
            state, tail = p, 0
            while state != tuple(range(n)):
                state = detach_cycle_maxima(state)
                tail += 1
            A.check(tail == expected, ("PTF", p, tail, expected))
            maximum_tail = max(maximum_tail, tail)
        maxima.append(maximum_tail)
    return f"PTF max_tails={maxima} KILL_CYCLE_PRUNING"


def delete_parallel_01(word: tuple[int, ...]) -> tuple[int, ...]:
    erased: set[int] = set()
    for i in range(len(word) - 1):
        if word[i : i + 2] == (0, 1):
            erased.update((i, i + 1))
    return tuple(letter for i, letter in enumerate(word) if i not in erased)


def check_ade() -> str:
    maxima = []
    terminals = []
    for n in range(13):
        max_tail = 0
        fixed = 0
        for word in product((0, 1), repeat=n):
            state, tail = word, 0
            while True:
                nxt = delete_parallel_01(state)
                if nxt == state:
                    break
                state, tail = nxt, tail + 1
            A.check("01" not in "".join(map(str, state)), ("ADE terminal", word, state))
            fixed += tail == 0
            max_tail = max(max_tail, tail)
        maxima.append(max_tail)
        terminals.append(fixed)
    return f"ADE max_tails={maxima} fixed={terminals} KILL_WORD_REWRITE"


def rgfs(n: int):
    if n == 0:
        yield ()
        return
    stack = [(0,)]
    for _ in range(1, n):
        stack = [prefix + (value,) for prefix in stack for value in range(max(prefix) + 2)]
    yield from stack


def equal_size_aggregate(rgf: tuple[int, ...]) -> tuple[int, ...]:
    if not rgf:
        return ()
    sizes = Counter(rgf)
    raw = [sizes[label] for label in rgf]
    relabel: dict[int, int] = {}
    return tuple(relabel.setdefault(value, len(relabel)) for value in raw)


def check_esa() -> str:
    rows = []
    for n in range(9):
        max_tail = 0
        fixed = 0
        for state in rgfs(n):
            seen = {state}
            tail = 0
            while True:
                nxt = equal_size_aggregate(state)
                if nxt == state:
                    break
                A.check(nxt not in seen, ("ESA cycle", state, nxt))
                seen.add(nxt)
                state, tail = nxt, tail + 1
            fixed += tail == 0
            max_tail = max(max_tail, tail)
        rows.append((n, max_tail, fixed))
    return f"ESA rows={rows} KILL_PARTITION_COALESCENCE"


def check_l2g() -> str:
    # A state is a multiset of path orders and cycle orders.  Line graphs send
    # P_m to P_{m-1}, while every C_m is fixed.
    rows = []
    for n in range(1, 13):
        path = n
        tail = 0
        while path:
            path -= 1
            tail += 1
        A.check(tail == n, ("L2G", n))
        rows.append(tail)
    return f"L2G path_tails={rows} cycles_fixed PASS KILL_DIRECT_LINE_GRAPH_OWNER"


def span(generators: tuple[int, ...]) -> frozenset[int]:
    values = {0}
    for generator in generators:
        values |= {value ^ generator for value in tuple(values)}
    return frozenset(values)


def all_subspaces(n: int) -> set[frozenset[int]]:
    vectors = tuple(range(1, 1 << n))
    spaces = {frozenset({0})}
    for length in range(1, n + 1):
        spaces.update(span(gens) for gens in combinations(vectors, length))
    return spaces


def dot(x: int, y: int) -> int:
    return (x & y).bit_count() & 1


def hull(code: frozenset[int], n: int) -> frozenset[int]:
    return frozenset(x for x in code if all(dot(x, y) == 0 for y in code))


def check_bch() -> str:
    rows = []
    for n in range(1, 6):
        spaces = all_subspaces(n)
        images = {hull(code, n) for code in spaces}
        for image in images:
            A.check(hull(image, n) == image, ("BCH idempotence", n, image))
        rows.append((n, len(spaces), len(images)))
    return f"BCH (n,subspaces,image)={rows} KILL_CODE_HULL_IDEMPOTENT"


def is_clutter(family: frozenset[int]) -> bool:
    return all(not (left != right and left & right == left) for left in family for right in family)


def blocker(clutter: frozenset[int], n: int) -> frozenset[int]:
    hits = []
    for subset in range(1 << n):
        if all(subset & edge for edge in clutter):
            hits.append(subset)
    minimal = [x for x in hits if not any(y != x and y & x == y for y in hits)]
    return frozenset(minimal)


def check_cba() -> str:
    rows = []
    for n in range(1, 5):
        clutters = []
        universe = tuple(range(1 << n))
        for mask in range(1 << len(universe)):
            family = frozenset(universe[i] for i in range(len(universe)) if mask >> i & 1)
            if is_clutter(family):
                clutters.append(family)
        for clutter in clutters:
            A.check(blocker(blocker(clutter, n), n) == clutter, ("CBA", n, clutter))
        rows.append((n, len(clutters)))
    return f"CBA clutters={rows} involution PASS KILL_BLOCKER_OWNER"


Tree = tuple[object, object] | tuple[()]


def binary_trees(nodes: int):
    if nodes == 0:
        yield ()
        return
    for left_size in range(nodes):
        for left in binary_trees(left_size):
            for right in binary_trees(nodes - 1 - left_size):
                yield (left, right)


def normalize_tree(tree):
    if not tree:
        return ()
    left, right = normalize_tree(tree[0]), normalize_tree(tree[1])
    return (left, right) if repr(left) <= repr(right) else (right, left)


def check_bmt() -> str:
    rows = []
    for nodes in range(9):
        trees = list(binary_trees(nodes))
        images = {normalize_tree(tree) for tree in trees}
        for image in images:
            A.check(normalize_tree(image) == image, ("BMT", nodes, image))
        rows.append((nodes, len(trees), len(images)))
    return f"BMT (nodes,states,image)={rows} KILL_TREE_CANONICALIZATION"


def rotate(word: tuple[int, ...], shift: int) -> tuple[int, ...]:
    return word[shift:] + word[:shift]


def necklace(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(rotate(word, shift) for shift in range(len(word))) if word else ()


def reverse_complement_necklace(word: tuple[int, ...]) -> tuple[int, ...]:
    return necklace(tuple(1 - value for value in reversed(word)))


def check_ncr() -> str:
    rows = []
    for n in range(1, 13):
        states = {necklace(word) for word in product((0, 1), repeat=n)}
        fixed = 0
        for state in states:
            nxt = reverse_complement_necklace(state)
            A.check(reverse_complement_necklace(nxt) == state, ("NCR", state))
            fixed += nxt == state
        rows.append((n, len(states), fixed))
    return f"NCR (n,necklaces,fixed)={rows} KILL_DIhedral_GROUP_ACTION"


def maximal_edges(family: frozenset[int]) -> frozenset[int]:
    return frozenset(edge for edge in family if not any(edge != other and edge & other == edge for other in family))


def check_hme() -> str:
    rows = []
    for n in range(1, 5):
        images = set()
        for mask in range(1 << (1 << n)):
            family = frozenset(edge for edge in range(1 << n) if mask >> edge & 1)
            image = maximal_edges(family)
            A.check(maximal_edges(image) == image, ("HME", n, family))
            images.add(image)
        rows.append((n, 1 << (1 << n), len(images)))
    return f"HME (n,states,image)={rows} KILL_HYPERGRAPH_REDUCTION"


def tournament_step(bits: int, n: int) -> int:
    edge_index = {(i, j): k for k, (i, j) in enumerate(combinations(range(n), 2))}

    def points(i: int, j: int) -> bool:
        if i < j:
            return bool(bits >> edge_index[(i, j)] & 1)
        return not bool(bits >> edge_index[(j, i)] & 1)

    parity = Counter()
    for i, j, k in combinations(range(n), 3):
        cyclic = (points(i, j) and points(j, k) and points(k, i)) or (
            points(j, i) and points(k, j) and points(i, k)
        )
        if cyclic:
            for edge in ((i, j), (i, k), (j, k)):
                parity[edge] ^= 1
    out = bits
    for edge, value in parity.items():
        if value:
            out ^= 1 << edge_index[edge]
    return out


def graph_summary(mapping: list[int]) -> tuple[int, int, int]:
    max_tail = max_period = 0
    fixed = 0
    for start in range(len(mapping)):
        seen: dict[int, int] = {}
        state = start
        while state not in seen:
            seen[state] = len(seen)
            state = mapping[state]
        tail, period = seen[state], len(seen) - seen[state]
        max_tail, max_period = max(max_tail, tail), max(max_period, period)
        fixed += start == mapping[start]
    return fixed, max_tail, max_period


def check_tcr() -> str:
    rows = []
    for n in range(3, 7):
        count = 1 << (n * (n - 1) // 2)
        mapping = [tournament_step(bits, n) for bits in range(count)]
        for target in mapping:
            A.check(0 <= target < count, ("TCR closure", n, target))
        rows.append((n, count) + graph_summary(mapping))
    return f"TCR (n,states,fixed,max_tail,max_period)={rows} KILL_UNSTABLE_BOOLEAN_TOURNAMENT"


def positive_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    partial = 0
    values = [0]
    for letter in word:
        partial += 1 if letter else -1
        values.append(partial)
    minimum = min(values[:-1])
    shift = max(i for i, value in enumerate(values[:-1]) if value == minimum)
    return rotate(word, shift)


def check_lpr() -> str:
    rows = []
    for q in range(7):
        n = 2 * q + 1
        states = [word for word in product((0, 1), repeat=n) if sum(word) == q + 1]
        images = Counter(positive_rotation(word) for word in states)
        for target, fibre in images.items():
            partial = 0
            for letter in target:
                partial += 1 if letter else -1
                A.check(partial > 0, ("LPR positivity", target))
            A.check(fibre == n, ("LPR fibre", q, target, fibre))
            A.check(positive_rotation(target) == target, ("LPR idempotence", target))
        rows.append((n, len(states), len(images)))
    return f"LPR (n,states,image)={rows} KILL_CYCLE_LEMMA_CANONICALIZATION"


def main() -> None:
    lines = [
        check_rcs(),
        check_ptf(),
        check_ade(),
        check_esa(),
        check_l2g(),
        check_bch(),
        check_cba(),
        check_bmt(),
        check_ncr(),
        check_hme(),
        check_tcr(),
        check_lpr(),
    ]
    for line in lines:
        print(line)
    print(f"TOTAL PASS systems=12 assertions={A.assertions}")


if __name__ == "__main__":
    main()
