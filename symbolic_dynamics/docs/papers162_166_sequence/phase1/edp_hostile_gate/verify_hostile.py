#!/usr/bin/env python3
"""Fresh exact hostile verifier for endpoint-duplicating partition pullback.

This program does not import the scout or use restricted-growth words.  A
partition is a tuple of literal blocks.  Besides checking the EDP claims, it
exhausts every endofunction through four labels to expose the generic
inverse-image-on-equivalences engine behind the candidate.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from math import comb


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, witness: object) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(witness)


A = Audit()
Partition = tuple[tuple[int, ...], ...]


def normalize(blocks: object) -> Partition:
    cleaned = [tuple(sorted(block)) for block in blocks if block]
    return tuple(sorted(cleaned, key=lambda block: block[0]))


@lru_cache(maxsize=None)
def partitions(n: int) -> tuple[Partition, ...]:
    """Generate Pi_n by literal insertion into blocks, not by RGS words."""
    if n == 0:
        return ((),)
    out: set[Partition] = set()
    for old in partitions(n - 1):
        out.add(normalize(old + ((n,),)))
        for position in range(len(old)):
            blocks = list(old)
            blocks[position] = blocks[position] + (n,)
            out.add(normalize(blocks))
    return tuple(sorted(out))


@lru_cache(maxsize=None)
def stirling2(n: int, k: int) -> int:
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    return stirling2(n - 1, k - 1) + k * stirling2(n - 1, k)


@lru_cache(maxsize=None)
def bell(n: int) -> int:
    return sum(stirling2(n, k) for k in range(n + 1))


def labels(pi: Partition) -> dict[int, int]:
    return {value: block_id for block_id, block in enumerate(pi) for value in block}


def block_count(pi: Partition) -> int:
    return len(pi)


def root_size(pi: Partition) -> int:
    if not pi:
        return 0
    return len(next(block for block in pi if 1 in block))


def indiscrete(n: int) -> Partition:
    return () if n == 0 else (tuple(range(1, n + 1)),)


def pullback(pi: Partition, mapping: tuple[int, ...]) -> Partition:
    """Pull an equivalence relation back along a literal 1-based map."""
    source_class = labels(pi)
    buckets: dict[int, list[int]] = defaultdict(list)
    for x, image in enumerate(mapping, start=1):
        buckets[source_class[image]].append(x)
    return normalize(buckets.values())


def predecessor_power(n: int, t: int) -> tuple[int, ...]:
    h = min(t, max(0, n - 1))
    return tuple(max(1, x - h) for x in range(1, n + 1))


def edp_step(pi: Partition) -> Partition:
    return pullback(pi, predecessor_power(sum(map(len, pi)), 1))


def edp_closed(pi: Partition, t: int) -> Partition:
    return pullback(pi, predecessor_power(sum(map(len, pi)), t))


def edp_iterate(pi: Partition, t: int) -> Partition:
    current = pi
    for _ in range(t):
        current = edp_step(current)
    return current


def supported(eta: Partition, h: int) -> bool:
    block_of = labels(eta)
    return all(block_of[x] == block_of[1] for x in range(1, h + 2))


def restriction(pi: Partition, retained: set[int]) -> Partition:
    return normalize(tuple(value for value in block if value in retained) for block in pi)


def deflate(eta: Partition, h: int) -> Partition:
    n = sum(map(len, eta))
    return normalize(tuple(value - h for value in block if value > h) for block in eta)


def root_prefix(pi: Partition) -> int:
    if not pi:
        return 0
    root = next(set(block) for block in pi if 1 in block)
    answer = 0
    while answer + 1 in root:
        answer += 1
    return answer


def predicted_depth(pi: Partition) -> int:
    n = sum(map(len, pi))
    if n <= 1 or pi == indiscrete(n):
        return 0
    return n - root_prefix(pi)


def literal_depth(pi: Partition) -> int:
    n = sum(map(len, pi))
    current = pi
    for depth in range(n + 1):
        if current == indiscrete(n):
            return depth
        current = edp_step(current)
    raise AssertionError(("depth did not terminate", pi))


def closed_increment_polynomial(h: int, b: int) -> Counter[tuple[int, int]]:
    """Distribution by (total blocks, extra root elements)."""
    out: Counter[tuple[int, int]] = Counter()
    for new_only in range(h + 1):
        choose = comb(h, new_only)
        attached_old = h - new_only
        for new_blocks in range(new_only + 1):
            partition_ways = stirling2(new_only, new_blocks)
            for root_attached in range(attached_old + 1):
                ways = (
                    choose
                    * partition_ways
                    * comb(attached_old, root_attached)
                    * (b - 1) ** (attached_old - root_attached)
                )
                if ways:
                    out[(b + new_blocks, root_attached)] += ways
    return out


def recurrence_increment_polynomial(h: int, b: int) -> Counter[tuple[int, int]]:
    """Independent sequential extension recurrence."""
    current: Counter[tuple[int, int]] = Counter({(0, 0): 1})
    for _ in range(h):
        following: Counter[tuple[int, int]] = Counter()
        for (new_blocks, root_attached), multiplicity in current.items():
            following[(new_blocks, root_attached + 1)] += multiplicity
            following[(new_blocks, root_attached)] += multiplicity * (b - 1 + new_blocks)
            following[(new_blocks + 1, root_attached)] += multiplicity
        current = following
    return Counter({(b + k, r): value for (k, r), value in current.items()})


def predicted_fibre(eta: Partition, t: int) -> Counter[tuple[int, int]]:
    n = sum(map(len, eta))
    h = min(t, max(0, n - 1))
    if not supported(eta, h):
        return Counter()
    b = block_count(eta)
    a = root_size(eta) - h
    A.check(a >= 1, ("nonpositive deflated root", n, t, eta, a))
    return Counter(
        {(blocks, a + extra): value for (blocks, extra), value in closed_increment_polynomial(h, b).items()}
    )


def refines(finer: Partition, coarser: Partition) -> bool:
    coarse_class = labels(coarser)
    return all(
        coarse_class[left] == coarse_class[right]
        for block in finer
        for left in block
        for right in block
    )


def mapping_power(mapping: tuple[int, ...], t: int) -> tuple[int, ...]:
    current = tuple(range(1, len(mapping) + 1))
    for _ in range(t):
        current = tuple(mapping[value - 1] for value in current)
    return current


def mapping_kernel(mapping: tuple[int, ...]) -> Partition:
    buckets: dict[int, list[int]] = defaultdict(list)
    for x, value in enumerate(mapping, start=1):
        buckets[value].append(x)
    return normalize(buckets.values())


def induced_image_partition(eta: Partition, mapping: tuple[int, ...]) -> Partition:
    """Descend eta >= ker(mapping) to the labelled image of mapping."""
    representatives: dict[int, int] = {}
    for x, value in enumerate(mapping, start=1):
        representatives.setdefault(value, x)
    eta_class = labels(eta)
    buckets: dict[int, list[int]] = defaultdict(list)
    for value in sorted(representatives):
        buckets[eta_class[representatives[value]]].append(value)
    return normalize(buckets.values())


def generic_pullback_audit() -> int:
    """Exhaust the generic engine for all endofunctions through n=4."""
    function_count = 0
    for n in range(1, 5):
        carrier = partitions(n)
        for mapping in product(range(1, n + 1), repeat=n):
            function_count += 1
            for t in range(n + 2):
                power = mapping_power(mapping, t)
                kernel = mapping_kernel(power)
                rank = len(set(power))
                actual: dict[Partition, int] = Counter(pullback(pi, power) for pi in carrier)
                expected_image = {eta for eta in carrier if refines(kernel, eta)}
                A.check(set(actual) == expected_image, ("generic principal filter", n, mapping, t))
                A.check(len(actual) == bell(rank), ("generic Bell image", n, mapping, t, rank))
                invisible = n - rank
                for eta, fibre in actual.items():
                    descended = induced_image_partition(eta, power)
                    b = block_count(descended)
                    expected = sum(recurrence_increment_polynomial(invisible, b).values())
                    A.check(fibre == expected, ("generic extension fibre", n, mapping, t, eta))
            for pi in carrier:
                current = pi
                for t in range(n + 2):
                    A.check(current == pullback(pi, mapping_power(mapping, t)),
                            ("generic iterate", n, mapping, pi, t))
                    current = pullback(current, mapping)
    return function_count


def edp_audit() -> tuple[list[str], int]:
    rows: list[str] = []
    grand_states = 0

    for h in range(15):
        for b in range(1, 9):
            A.check(
                closed_increment_polynomial(h, b) == recurrence_increment_polynomial(h, b),
                ("closed polynomial versus extension DP", h, b),
            )

    for n in range(1, 9):
        carrier = partitions(n)
        grand_states += len(carrier)
        A.check(len(carrier) == bell(n), ("independent Bell census", n))
        A.check(len(set(carrier)) == len(carrier), ("duplicate partitions", n))

        depths = Counter()
        inventory = Counter((block_count(pi), root_size(pi)) for pi in carrier)
        for pi in carrier:
            actual_depth = literal_depth(pi)
            expected_depth = predicted_depth(pi)
            A.check(actual_depth == expected_depth, ("point depth", n, pi))
            depths[actual_depth] += 1
            A.check((edp_step(pi) == pi) == (pi == indiscrete(n)), ("fixed locus", n, pi))

        expected_depths = Counter({0: 1})
        for depth in range(1, n):
            expected_depths[depth] = bell(depth + 1) - bell(depth)
        A.check(depths == expected_depths, ("depth histogram", n, depths, expected_depths))
        A.check(max(depths) == max(0, n - 1), ("sharp height", n))

        image_sizes: list[int] = []
        unsupported_total = 0
        previous_image: set[Partition] | None = None
        for t in range(n + 3):
            h = min(t, n - 1)
            fibres: dict[Partition, Counter[tuple[int, int]]] = defaultdict(Counter)
            for pi in carrier:
                iterated = edp_iterate(pi, t)
                closed = edp_closed(pi, t)
                A.check(iterated == closed, ("EDP iterate", n, t, pi))
                rho = restriction(pi, set(range(1, n - h + 1)))
                A.check(deflate(closed, h) == rho, ("restriction/deflation", n, t, pi))
                fibres[closed][(block_count(pi), root_size(pi))] += 1

            image = set(fibres)
            expected_image = {eta for eta in carrier if supported(eta, h)}
            A.check(image == expected_image, ("EDP image support", n, t))
            A.check(len(image) == bell(n - h), ("Bell staircase", n, t))
            if previous_image is not None:
                A.check(image <= previous_image, ("nested image staircase", n, t))
            previous_image = image
            image_sizes.append(len(image))

            total_mass = 0
            aggregate = Counter()
            for eta in carrier:
                observed = fibres.get(eta, Counter())
                predicted = predicted_fibre(eta, t)
                A.check(observed == predicted, ("every-target z/u fibre", n, t, eta))
                A.check(bool(observed) == supported(eta, h), ("unsupported target", n, t, eta))
                total_mass += sum(observed.values())
                aggregate.update(observed)
                if not observed:
                    unsupported_total += 1
                else:
                    b = block_count(eta)
                    expected_unweighted = sum(recurrence_increment_polynomial(h, b).values())
                    A.check(sum(observed.values()) == expected_unweighted,
                            ("r-Bell specialization", n, t, eta))
                    if t == 0:
                        A.check(observed == Counter({(b, root_size(eta)): 1}),
                                ("identity-time singleton", n, eta))
                    if t == 1:
                        # The advertised b+1 corollary needs n>=2: at n=1,
                        # h=min(1,n-1)=0 and the identity fibre is a singleton.
                        expected_one_step = 1 if n == 1 else b + 1
                        A.check(sum(observed.values()) == expected_one_step,
                                ("one-step boundary", n, eta))

            A.check(total_mass == bell(n), ("fibre mass", n, t, total_mass))
            A.check(aggregate == inventory, ("weighted fibre mass", n, t))
            if t >= n - 1:
                A.check(image == {indiscrete(n)}, ("saturated image", n, t))
                A.check(fibres[indiscrete(n)] == inventory, ("saturated z/u inventory", n, t))

        rows.append(
            f"n={n}|states={len(carrier)}|height={max(depths)}|"
            f"depths={','.join(f'{d}:{depths[d]}' for d in sorted(depths))}|"
            f"images={','.join(map(str, image_sizes))}|unsupported_checks={unsupported_total}"
        )
    return rows, grand_states


def main() -> None:
    generic_functions = generic_pullback_audit()
    rows, grand_states = edp_audit()
    print("EDP_FRESH_HOSTILE_GATE_V1")
    print(f"generic_endofunctions={generic_functions}|generic_boxes=1..4")
    print(f"edp_boxes=8|edp_states={grand_states}")
    for row in rows:
        print(row)
    print(f"assertions={A.assertions}")
    print("MATHEMATICS PASS")
    print("DECISION KILL_GENERIC_PULLBACK_RBELL_AND_P110_COLLISION")
    print("EXTERNAL HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
