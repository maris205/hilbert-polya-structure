#!/usr/bin/env python3
"""Independent hostile Review-B verifier for P174.

The implementation starts from the literal minimum-pivot rule.  Points and
states are represented by permutation tables and frozensets.  Reverse fibres
are reconstructed from the full edge relation, functional-graph data are
obtained by generic orbit tracing and union--find, and boundary identities are
also checked symbolically over a larger prime range.  No author, scout, or
Review-A module is imported.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations
from math import comb


FULL_GRAPH_PRIMES = (2, 3, 5, 7, 11, 13, 17)
SYMBOLIC_LIMIT = 101
CHECKS = 0


def require(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


@lru_cache(maxsize=None)
def inverse_residue(value: int, prime: int) -> int:
    """Find the inverse by finite search, independently of Fermat powering."""
    if not 0 < value < prime:
        raise ValueError("inverse requested outside the nonzero field elements")
    for candidate in range(1, prime):
        if (value * candidate) % prime == 1:
            return candidate
    raise AssertionError(f"no inverse for value={value}, modulus={prime}")


def projective_tables(prime: int):
    """Build every gamma_a and its inverse as explicit point permutations."""
    infinity = prime
    forward = {}
    reverse = {}
    points = tuple(range(prime + 1))
    for pivot in range(prime):
        row = {}
        for point in points:
            if point == pivot:
                image = infinity
            elif point == infinity:
                image = 0
            else:
                image = inverse_residue((point - pivot) % prime, prime)
            row[point] = image
        require(set(row) == set(points), f"projectivity domain p={prime} a={pivot}")
        require(set(row.values()) == set(points), f"projectivity range p={prime} a={pivot}")
        inverse_row = {image: point for point, image in row.items()}
        for point in points:
            require(
                inverse_row[row[point]] == point,
                f"table inverse p={prime} a={pivot} x={point}",
            )
        forward[pivot] = row
        reverse[pivot] = inverse_row
    return forward, reverse


def state_space(prime: int, size: int):
    return tuple(
        frozenset(chosen) for chosen in combinations(range(prime + 1), size)
    )


def least_finite(state: frozenset[int], prime: int):
    candidates = [point for point in state if point < prime]
    return min(candidates) if candidates else None


def apply_literal(state: frozenset[int], prime: int, forward):
    pivot = least_finite(state, prime)
    if pivot is None:
        raise ValueError("state has no finite pivot")
    return frozenset(forward[pivot][point] for point in state)


def orbit_profile(start, successor):
    """Return tail, least period, and the recurrent cycle by generic tracing."""
    first_seen = {}
    current = start
    while current not in first_seen:
        first_seen[current] = len(first_seen)
        current = successor[current]
    tail = first_seen[current]
    period = len(first_seen) - tail
    cycle = set()
    point = current
    for _ in range(period):
        cycle.add(point)
        point = successor[point]
    require(point == current, "cycle traversal closes")
    return tail, period, frozenset(cycle)


def iterate(state, successor, exponent: int):
    current = state
    for _ in range(exponent):
        current = successor[current]
    return current


class DisjointSet:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, item: int) -> int:
        root = item
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[item] != item:
            following = self.parent[item]
            self.parent[item] = root
            item = following
        return root

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return
        if self.rank[left_root] < self.rank[right_root]:
            left_root, right_root = right_root, left_root
        self.parent[right_root] = left_root
        if self.rank[left_root] == self.rank[right_root]:
            self.rank[left_root] += 1


def fixed_coefficient(prime: int, chosen_nonzero: int) -> int:
    """Coefficient of (1+v)^2(1+v^2)^((p-3)/2), expanded directly."""
    if prime == 2:
        return int(chosen_nonzero == 0)
    answer = 0
    paired_orbits = (prime - 3) // 2
    for chosen_singletons in (0, 1, 2):
        leftover = chosen_nonzero - chosen_singletons
        if leftover >= 0 and leftover % 2 == 0:
            answer += choose(2, chosen_singletons) * choose(
                paired_orbits, leftover // 2
            )
    return answer


def expected_height(target: frozenset[int], prime: int) -> int:
    if prime not in target:
        return 0
    inverse_labels = [
        inverse_residue(point, prime) for point in target if 0 < point < prime
    ]
    return prime - max(inverse_labels, default=0)


def audit_box(prime: int, size: int, forward, reverse):
    infinity = prime
    states = state_space(prime, size)
    state_set = set(states)
    successor = {}
    parents = defaultdict(list)

    for source in states:
        pivot = least_finite(source, prime)
        require(pivot is not None, f"finite pivot p={prime} k={size}")
        target = apply_literal(source, prime, forward)
        require(len(target) == size, f"cardinality p={prime} k={size}")
        require(target in state_set, f"carrier closure p={prime} k={size}")
        require(infinity in target, f"forced infinity p={prime} k={size}")
        require(
            (0 in target) == (infinity in source),
            f"unique preimage of zero p={prime} k={size}",
        )
        reconstructed = frozenset(reverse[pivot][point] for point in target)
        require(reconstructed == source, f"table reconstruction p={prime} k={size}")
        successor[source] = target
        parents[target].append(source)

    expected_first = {state for state in states if infinity in state}
    expected_core = {
        state for state in states if infinity in state and 0 in state
    }
    actual_first = set(successor.values())
    actual_second = {successor[successor[state]] for state in states}
    require(actual_first == expected_first, f"first image p={prime} k={size}")
    require(actual_second == expected_core, f"second image p={prime} k={size}")

    profiles = {}
    depth_histogram = Counter()
    recurrent_cycles = set()
    fixed_states = 0
    for state in states:
        tail, period, cycle = orbit_profile(state, successor)
        profiles[state] = (tail, period, cycle)
        expected_tail = (
            0
            if 0 in state and infinity in state
            else 1
            if infinity in state
            else 2
        )
        require(tail == expected_tail, f"tail p={prime} k={size} state={sorted(state)}")
        require(period in (1, 2), f"period p={prime} k={size}")
        require(
            iterate(state, successor, 4) == iterate(state, successor, 2),
            f"M4=M2 p={prime} k={size}",
        )
        depth_histogram[tail] += 1
        if tail == 0:
            recurrent_cycles.add(cycle)
            expected_inversion = frozenset(forward[0][point] for point in state)
            require(
                successor[state] == expected_inversion,
                f"core inversion p={prime} k={size}",
            )
            require(
                iterate(state, successor, 2) == state,
                f"core involution p={prime} k={size}",
            )
        if successor[state] == state:
            fixed_states += 1

    recurrent_count = choose(prime - 1, size - 2)
    expected_fixed = fixed_coefficient(prime, size - 2)
    require(
        depth_histogram
        == Counter(
            {
                0: recurrent_count,
                1: choose(prime - 1, size - 1),
                2: choose(prime, size),
            }
        ),
        f"depth census p={prime} k={size}",
    )
    require(fixed_states == expected_fixed, f"fixed census p={prime} k={size}")
    expected_cycles = (recurrent_count + expected_fixed) // 2
    require(len(recurrent_cycles) == expected_cycles, f"cycle census p={prime} k={size}")
    require(
        sum(len(cycle) == 2 for cycle in recurrent_cycles)
        == (recurrent_count - expected_fixed) // 2,
        f"two-cycle census p={prime} k={size}",
    )

    index = {state: position for position, state in enumerate(states)}
    components = DisjointSet(len(states))
    for state in states:
        components.union(index[state], index[successor[state]])
    weak_component_count = len({components.find(i) for i in range(len(states))})
    require(
        weak_component_count == expected_cycles,
        f"weak components p={prime} k={size}",
    )

    for exponent in range(1, 7):
        actual_fixed_iterate = sum(
            iterate(state, successor, exponent) == state for state in states
        )
        predicted = expected_fixed if exponent % 2 else recurrent_count
        require(
            actual_fixed_iterate == predicted,
            f"fixed iterate p={prime} k={size} m={exponent}",
        )

    fibre_histogram = Counter()
    maximum_targets = []
    for target in states:
        sources = parents.get(target, [])
        actual_pivots = sorted(least_finite(source, prime) for source in sources)
        require(
            len(actual_pivots) == len(set(actual_pivots)),
            f"one parent per pivot p={prime} k={size}",
        )
        height = expected_height(target, prime)
        expected_pivots = list(range(height))
        require(
            actual_pivots == expected_pivots,
            f"pivot interval p={prime} k={size} T={sorted(target)}",
        )
        by_pivot = {least_finite(source, prime): source for source in sources}
        for pivot in actual_pivots:
            forced = frozenset(reverse[pivot][point] for point in target)
            require(
                forced == by_pivot[pivot],
                f"forced inverse p={prime} k={size} a={pivot}",
            )
            require(
                apply_literal(forced, prime, forward) == target,
                f"forced inverse edge p={prime} k={size} a={pivot}",
            )

        mark_coefficients = Counter(actual_pivots)
        require(
            all(mark_coefficients[power] == int(power < height) for power in range(prime)),
            f"pivot polynomial p={prime} k={size}",
        )

        if target in expected_core:
            parent_depths = Counter(profiles[source][0] for source in sources)
            require(
                parent_depths == Counter({0: 1, 1: max(0, height - 1)}),
                f"core incoming depths p={prime} k={size}",
            )
        elif target in expected_first:
            require(
                all(profiles[source][0] == 2 for source in sources),
                f"first-layer incoming depths p={prime} k={size}",
            )
        else:
            require(not sources, f"zero-fibre stratum p={prime} k={size}")

        fibre_histogram[len(sources)] += 1
        if len(sources) == prime - size + 2:
            maximum_targets.append(target)

    require(
        fibre_histogram[0] == choose(prime, size),
        f"zero-fibre census p={prime} k={size}",
    )
    for fibre_size in range(1, prime + 1):
        require(
            fibre_histogram[fibre_size]
            == choose(prime - fibre_size, size - 2),
            f"positive fibre census p={prime} k={size} q={fibre_size}",
        )
    require(len(maximum_targets) == 1, f"unique maximum p={prime} k={size}")
    explicit_maximum = frozenset(
        {0, infinity}
        | {
            inverse_residue(label, prime)
            for label in range(1, size - 1)
        }
    )
    require(
        maximum_targets[0] == explicit_maximum,
        f"maximum target identity p={prime} k={size}",
    )
    require(
        sum(fibre_size * multiplicity for fibre_size, multiplicity in fibre_histogram.items())
        == len(states),
        f"fibre mass p={prime} k={size}",
    )

    return {
        "states": len(states),
        "core": recurrent_count,
        "fixed": expected_fixed,
        "max_fibre": prime - size + 2,
    }


def audit_excluded_boundaries(prime: int, forward) -> None:
    infinity = prime
    full_line = frozenset(range(prime + 1))
    require(
        apply_literal(full_line, prime, forward) == full_line,
        f"excluded full-line fixed state p={prime}",
    )
    require(
        least_finite(frozenset({infinity}), prime) is None,
        f"singleton infinity lacks pivot p={prime}",
    )
    for finite in range(prime):
        singleton = frozenset({finite})
        require(
            apply_literal(singleton, prime, forward) == frozenset({infinity}),
            f"finite singleton hits undefined singleton p={prime} x={finite}",
        )


def symbolic_parameter_audit(limit: int):
    primes = tuple(number for number in range(2, limit + 1) if is_prime(number))
    boxes = 0
    for prime in primes:
        for value in range(1, prime):
            inverse = inverse_residue(value, prime)
            require((value * inverse) % prime == 1, f"symbolic inverse p={prime}")
            require(
                inverse_residue(inverse, prime) == value,
                f"inversion involution p={prime}",
            )
        for pivot in range(prime):
            for increment in range(1, prime):
                require(
                    ((pivot + increment) % prime >= pivot)
                    == (pivot < prime - increment),
                    f"no-wrap equivalence p={prime} a={pivot} b={increment}",
                )
        for size in range(2, prime + 1):
            boxes += 1
            carrier = choose(prime + 1, size)
            recurrent = choose(prime - 1, size - 2)
            fixed = fixed_coefficient(prime, size - 2)
            require(
                recurrent
                + choose(prime - 1, size - 1)
                + choose(prime, size)
                == carrier,
                f"symbolic depth partition p={prime} k={size}",
            )
            require(0 <= fixed <= recurrent, f"symbolic fixed bound p={prime} k={size}")
            require(
                (recurrent - fixed) % 2 == 0,
                f"symbolic two-cycle integrality p={prime} k={size}",
            )
            positive_targets = sum(
                choose(prime - fibre_size, size - 2)
                for fibre_size in range(1, prime + 1)
            )
            require(
                positive_targets == choose(prime, size - 1),
                f"symbolic positive target mass p={prime} k={size}",
            )
            require(
                positive_targets + choose(prime, size) == carrier,
                f"symbolic target partition p={prime} k={size}",
            )
            source_mass = sum(
                fibre_size * choose(prime - fibre_size, size - 2)
                for fibre_size in range(1, prime + 1)
            )
            require(source_mass == carrier, f"symbolic fibre mass p={prime} k={size}")
            require(
                choose(size - 2, size - 2) == 1,
                f"symbolic unique maximum p={prime} k={size}",
            )
    return len(primes), boxes


def audit_smallest_graph() -> None:
    prime = 2
    forward, _reverse = projective_tables(prime)
    depth_two = frozenset({0, 1})
    depth_one = frozenset({1, 2})
    core = frozenset({0, 2})
    require(apply_literal(depth_two, prime, forward) == depth_one, "p=2 edge depth 2")
    require(apply_literal(depth_one, prime, forward) == core, "p=2 edge depth 1")
    require(apply_literal(core, prime, forward) == core, "p=2 core fixed")


def main() -> None:
    print("P174 HOSTILE REVIEW B — INDEPENDENT EXACT CONTROL")
    print("PROVENANCE frozenset/permutation-table/union-find; no project imports")
    print("STATUS PROVISIONAL_AMBER / HOLD_EXTERNAL")

    total_boxes = 0
    total_states = 0
    for prime in FULL_GRAPH_PRIMES:
        require(is_prime(prime), f"full-graph prime p={prime}")
        forward, reverse = projective_tables(prime)
        prime_states = 0
        for size in range(2, prime + 1):
            result = audit_box(prime, size, forward, reverse)
            total_boxes += 1
            total_states += result["states"]
            prime_states += result["states"]
        audit_excluded_boundaries(prime, forward)
        print(
            f"FULL_GRAPH p={prime} boxes={prime-1} states={prime_states} "
            "all-theorem axes PASS"
        )

    audit_smallest_graph()
    prime_count, symbolic_boxes = symbolic_parameter_audit(SYMBOLIC_LIMIT)
    print(
        f"SYMBOLIC primes<=101 count={prime_count} boxes={symbolic_boxes} "
        "no-wrap/count/boundary identities PASS"
    )
    print(f"FULL_GRAPH_BOXES {total_boxes}")
    print(f"FULL_GRAPH_STATES {total_states}")
    print("BOUNDARIES p=2,k=2; k=1 obstruction; k=p+1 fixed PASS")
    print("THEOREM image tower and exact depths PASS")
    print("THEOREM inversion core, cycles, fixed iterates, components PASS")
    print("THEOREM every-target pivot interval and marked fibre PASS")
    print("THEOREM positive fibre distribution and unique maximum PASS")
    print(f"ASSERTIONS {CHECKS}")
    print("VERDICT EXECUTABLE_CLAIMS_PASS")


if __name__ == "__main__":
    main()
