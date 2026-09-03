#!/usr/bin/env python3
"""Independent hostile-review verifier for P176.

This program deliberately does not import the manuscript, scout, author, or
Review-A code.  States are immutable binary strings; literal coordinate
rotation uses string slicing; orbit clocks use Brent's algorithm; and phase
components are reconstructed as small functional digraphs before comparison
with the claimed run/boundary description.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from math import comb, gcd
import sys


ASSERTIONS = 0


def require(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def binary_strings(length: int):
    """Generate fixed-length binary strings in lexical order."""
    if length == 0:
        yield ""
        return
    width = f"0{length}b"
    for value in range(1 << length):
        yield format(value, width)


def spin(word: str, amount: int) -> str:
    """Left circular coordinate rotation."""
    n = len(word)
    require(n > 0, "rotation carrier must be nonempty")
    amount %= n
    return word[amount:] + word[:amount]


def update(word: str) -> str:
    """The literal P176 map: rotate by the frequency of the first symbol."""
    return spin(word, word.count(word[0]))


def complement(word: str) -> str:
    return word.translate(str.maketrans("01", "10"))


def positive_divisors(number: int):
    small = []
    large = []
    probe = 1
    while probe * probe <= number:
        if number % probe == 0:
            small.append(probe)
            if probe * probe != number:
                large.append(number // probe)
        probe += 1
    return small + large[::-1]


def least_block(word: str) -> int:
    """Least positive coordinate-rotation period of a word."""
    n = len(word)
    for block in positive_divisors(n):
        if word == word[:block] * (n // block):
            return block
    raise AssertionError("full length must be a period")


def brent_clock(start: str):
    """Return (preperiod, period) using constant-memory Brent detection."""
    power = 1
    period = 1
    tortoise = start
    hare = update(start)
    while tortoise != hare:
        if power == period:
            tortoise = hare
            power *= 2
            period = 0
        hare = update(hare)
        period += 1

    preperiod = 0
    tortoise = start
    hare = start
    for _ in range(period):
        hare = update(hare)
    while tortoise != hare:
        tortoise = update(tortoise)
        hare = update(hare)
        preperiod += 1
    return preperiod, period


def canonical_rotation(word: str) -> str:
    return min(spin(word, shift) for shift in range(len(word)))


def claimed_predecessors(target: str):
    """Closed-form inverse candidates, deduplicated as actual strings."""
    n = len(target)
    weight = target.count("1")
    if weight == 0 or weight == n:
        return {target}
    candidates = set()
    from_one = spin(target, -weight)
    if from_one[0] == "1":
        candidates.add(from_one)
    from_zero = spin(target, weight)
    if from_zero[0] == "0":
        candidates.add(from_zero)
    return candidates


def mobius(number: int) -> int:
    """Elementary square-free factorization definition of the Moebius value."""
    remaining = number
    prime_count = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            if remaining % divisor == 0:
                return 0
            prime_count += 1
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def primitive_count_formula(length: int, weight: int) -> int:
    total = 0
    for divisor in positive_divisors(gcd(length, weight)):
        total += mobius(divisor) * comb(length // divisor, weight // divisor)
    return total


def fixed_count_formula(n: int) -> int:
    answer = 0
    for block in positive_divisors(n):
        repeats = n // block
        for block_weight in range(block + 1):
            if (repeats * block_weight) % block == 0:
                answer += primitive_count_formula(block, block_weight)
    return answer


def predicted_histogram(n: int, weight: int):
    layer = comb(n, weight)
    if weight == 0 or weight == n or (2 * weight) % n == 0:
        return {0: 0, 1: layer, 2: 0}
    twins = comb(n - 2, weight - 1)
    return {0: twins, 1: layer - 2 * twins, 2: twins}


def periodic_vertices(successor):
    """Find all directed cycles of a finite outdegree-one graph directly."""
    cycles = set()
    for origin in range(len(successor)):
        order = []
        first_seen = {}
        cursor = origin
        while cursor not in first_seen:
            first_seen[cursor] = len(order)
            order.append(cursor)
            cursor = successor[cursor]
        cycle = frozenset(order[first_seen[cursor] :])
        cycles.add(cycle)
    # Remove cycles seen only as downstream suffixes of transient origins.
    return {cycle for cycle in cycles if all(successor[v] in cycle for v in cycle)}


def graph_distance_to_cycles(successor, cycles):
    recurrent = set().union(*cycles)
    depths = []
    for origin in range(len(successor)):
        cursor = origin
        depth = 0
        while cursor not in recurrent:
            cursor = successor[cursor]
            depth += 1
            require(depth <= len(successor), "component failed to reach recurrence")
        depths.append(depth)
    return depths


def direct_component_audit(representative: str) -> None:
    """Rebuild each +/- generator component and test the complete classification."""
    n = len(representative)
    block = least_block(representative)
    weight = representative.count("1")
    step_gcd = gcd(weight, block)
    expected_length = block // step_gcd

    unseen = set(range(block))
    components = []
    while unseen:
        start = min(unseen)
        positions = []
        cursor = start
        while cursor in unseen:
            positions.append(cursor)
            unseen.remove(cursor)
            cursor = (cursor + weight) % block
        require(cursor == start, "generator walk did not close at its start")
        components.append(positions)

    require(len(components) == step_gcd, "wrong number of generator components")
    require(all(len(c) == expected_length for c in components), "wrong component length")
    require(
        set().union(*(set(c) for c in components)) == set(range(block)),
        "generator components fail to partition phases",
    )

    for positions in components:
        letters = [representative[position] for position in positions]
        length = len(positions)
        local_successor = [
            (q + 1) % length if letters[q] == "1" else (q - 1) % length
            for q in range(length)
        ]
        cycles = periodic_vertices(local_successor)
        depths = graph_distance_to_cycles(local_successor, cycles)

        if length == 1:
            expected_cycles = {frozenset({0})}
        elif length == 2:
            expected_cycles = {frozenset({0, 1})}
        elif len(set(letters)) == 1:
            expected_cycles = {frozenset(range(length))}
        else:
            expected_cycles = {
                frozenset({q, (q + 1) % length})
                for q in range(length)
                if letters[q] == "1" and letters[(q + 1) % length] == "0"
            }
        require(cycles == expected_cycles, "10-boundary recurrent classification failed")

        predicted_depths = []
        for q, letter in enumerate(letters):
            distance = 0
            if letter == "1":
                while letters[(q + distance + 1) % length] == "1" and distance < length:
                    distance += 1
            else:
                while letters[(q - distance - 1) % length] == "0" and distance < length:
                    distance += 1
            predicted_depths.append(0 if distance == length else distance)
        require(depths == predicted_depths, "run-distance tail formula failed")

        longest_run = 1
        if len(set(letters)) == 1:
            longest_run = length
        else:
            for q in range(length):
                run = 1
                while run < length and letters[(q + run) % length] == letters[q]:
                    run += 1
                longest_run = max(longest_run, run)
        expected_maximum = 0 if len(set(letters)) == 1 else longest_run - 1
        require(max(depths) == expected_maximum, "longest-run component clock failed")


def period_witness(n: int, period: int) -> str:
    """Construct the sparse witness for every proper divisor period >=3."""
    spacing = n // period
    support = set(range(spacing - 1)) | {spacing}
    return "".join("1" if index in support else "0" for index in range(n))


def audit_size(n: int, digest) -> dict:
    states = list(binary_strings(n))
    incoming = defaultdict(set)
    records = {}
    layer_primitive = Counter()
    necklaces = {}

    for state in states:
        target = update(state)
        require(len(target) == n and set(target) <= {"0", "1"}, "carrier closure failed")
        require(target.count("1") == state.count("1"), "weight preservation failed")
        require(canonical_rotation(target) == canonical_rotation(state), "necklace preservation failed")
        require(update(complement(state)) == complement(target), "complement equivariance failed")
        incoming[target].add(state)

        clock = brent_clock(state)
        block = least_block(state)
        weight = state.count("1")
        records[state] = (clock, block, weight)
        fixed_condition = (weight % block == 0)
        require((target == state) == fixed_condition, "wordwise fixed criterion failed")
        if block == n:
            layer_primitive[weight] += 1
        necklaces.setdefault(canonical_rotation(state), state)
        digest.update(f"{n}:{state}>{target}:{clock}:{block};".encode())

    # Literal inverse fibres and the complete 0/1/2 histogram, layer by layer.
    observed_histograms = {}
    for target in states:
        predicted = claimed_predecessors(target)
        actual = incoming.get(target, set())
        require(predicted == actual, f"inverse candidates failed for n={n}, y={target}")
        require(len(actual) <= 2, "a fibre exceeded two points")
        for source in predicted:
            require(update(source) == target, "inverse candidate is spurious")

    for weight in range(n + 1):
        layer_targets = [word for word in states if word.count("1") == weight]
        histogram = Counter(len(incoming.get(word, set())) for word in layer_targets)
        observed = {degree: histogram.get(degree, 0) for degree in (0, 1, 2)}
        expected = predicted_histogram(n, weight)
        require(observed == expected, f"fibre histogram failed at n={n}, k={weight}")
        require(sum(observed.values()) == comb(n, weight), "target mass failed")
        require(sum(degree * observed[degree] for degree in (0, 1, 2)) == comb(n, weight), "source mass failed")
        if 0 < weight < n and 2 * weight == n:
            for word in layer_targets:
                require(update(update(word)) == word, "tie layer is not an involution")
        observed_histograms[weight] = observed

    image_observed = sum(bool(incoming.get(target)) for target in states)
    image_formula = 2 + sum(
        comb(n, weight)
        - (0 if (2 * weight) % n == 0 else comb(n - 2, weight - 1))
        for weight in range(1, n)
    )
    require(image_observed == image_formula, "whole-image formula failed")

    # Phase conjugacy and component classification, one representative per necklace.
    for representative in necklaces.values():
        block = least_block(representative)
        weight = representative.count("1")
        for phase in range(block):
            state = spin(representative, phase)
            signed_step = weight if state[0] == "1" else -weight
            require(
                update(state) == spin(representative, phase + signed_step),
                "signed phase reduction failed",
            )
        direct_component_audit(representative)

    # Exact clocks, period inventory, deepest states, and small-n sentinels.
    depths = {word: records[word][0][0] for word in states}
    periods = {records[word][0][1] for word in states}
    deepest = {word for word in states if depths[word] == max(depths.values())}
    if n == 1:
        expected_periods = {1}
        expected_depth = 0
        expected_deepest = {"0", "1"}
    else:
        expected_periods = {1, 2} | {d for d in positive_divisors(n) if 3 <= d < n}
        expected_depth = n - 2
        if n == 2:
            expected_deepest = set(states)
        else:
            first = "01" + "0" * (n - 2)
            expected_deepest = {first, complement(first)}
    require(periods == expected_periods, f"period inventory failed for n={n}")
    require(max(depths.values()) == expected_depth, f"sharp clock failed for n={n}")
    require(deepest == expected_deepest, f"deepest-state classification failed for n={n}")

    # Primitive-word Moebius formula and the aggregate fixed census.
    for weight in range(n + 1):
        require(
            layer_primitive[weight] == primitive_count_formula(n, weight),
            f"primitive weighted count failed at ({n},{weight})",
        )
    fixed_observed = sum(update(word) == word for word in states)
    fixed_formula = fixed_count_formula(n)
    require(fixed_observed == fixed_formula, f"fixed census failed at n={n}")

    total_histogram = Counter()
    for histogram in observed_histograms.values():
        total_histogram.update(histogram)
    return {
        "states": len(states),
        "necklaces": len(necklaces),
        "image": image_observed,
        "fixed": fixed_observed,
        "depth": expected_depth,
        "deepest": len(deepest),
        "periods": ",".join(map(str, sorted(periods))),
        "fibres": "/".join(str(total_histogram[d]) for d in (0, 1, 2)),
    }


def arithmetic_stress(limit: int) -> None:
    for n in range(2, limit + 1):
        # Construct every advertised long period without enumerating 2^n states.
        for period in positive_divisors(n):
            if not 3 <= period < n:
                continue
            base = period_witness(n, period)
            spacing = n // period
            require(base.count("1") == spacing, "sparse witness has wrong weight")
            require(least_block(base) == n, "sparse witness is not primitive")
            pointed = spin(base, spacing - 1)
            preperiod, observed_period = brent_clock(pointed)
            require((preperiod, observed_period) == (0, period), "long-period witness failed")

        # Histogram formulas are nonnegative and conserve both target and source mass.
        image = 2
        for weight in range(1, n):
            histogram = predicted_histogram(n, weight)
            require(all(value >= 0 for value in histogram.values()), "negative histogram coefficient")
            require(sum(histogram.values()) == comb(n, weight), "large-n target mass failed")
            require(
                histogram[1] + 2 * histogram[2] == comb(n, weight),
                "large-n source mass failed",
            )
            image += histogram[1] + histogram[2]
        require(2 <= image <= (1 << n), "large-n image bound failed")


def main() -> None:
    exhaustive_limit = 17
    stress_limit = 96
    digest = sha256()
    rows = []
    for n in range(1, exhaustive_limit + 1):
        rows.append((n, audit_size(n, digest)))
    arithmetic_stress(stress_limit)

    print("P176 independent hostile-review verifier B")
    print("method=string slicing + Brent clocks + direct component functional graphs")
    print(f"exhaustive_n=1..{exhaustive_limit}")
    print(f"constructive_and_arithmetic_stress_n=2..{stress_limit}")
    print("n states necklaces image fixed max_tail deepest periods fibres_0/1/2")
    for n, row in rows:
        print(
            n,
            row["states"],
            row["necklaces"],
            row["image"],
            row["fixed"],
            row["depth"],
            row["deepest"],
            row["periods"],
            row["fibres"],
        )
    print(f"transition_clock_digest={digest.hexdigest()}")
    print(f"assertions={ASSERTIONS}")
    print("RESULT: PASS")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"RESULT: FAIL: {error}", file=sys.stderr)
        raise
