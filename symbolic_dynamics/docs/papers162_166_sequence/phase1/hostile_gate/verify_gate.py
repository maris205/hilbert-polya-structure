#!/usr/bin/env python3
"""Independent exact checks for the P162--P166 candidate hostile gate.

This file intentionally imports no scout implementation.  It tests a small,
adversarial parameter grid for RFW, CNG, AA01/USP, and BQC, including the
boundary cases used in the gate report.  Exhaustion is counterexample pressure,
not a proof or an ownership certificate.
"""

from collections import Counter
from itertools import combinations, product
from math import comb, gcd


ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(f"{label} [assertion {ASSERTIONS}]")


def iterate(function, state, steps):
    for _ in range(steps):
        state = function(state)
    return state


# ---------------------------------------------------------------------------
# RFW: reciprocal Fibonacci window


def inv0(value, prime):
    return 0 if value % prime == 0 else pow(value, prime - 2, prime)


def rfw_step(state, prime):
    x, y = state
    return y, x * y * inv0(x + y, prime) % prime


def fib_rank(prime):
    older, newer = 0, 1
    for index in range(1, 2 * prime + 4):
        older, newer = newer, (older + newer) % prime
        if older == 0:
            return index
    raise AssertionError("rank search failed")


def projective(vector, prime):
    x, y = vector
    return (1, y * inv0(x, prime) % prime) if x else (0, 1)


def mat_vec(vector, prime):
    x, y = vector
    return y, (x + y) % prime


def rfw_bad_lines(prime):
    rank = fib_rank(prime)
    vector = (1, 0)
    lines = []
    for _ in range(rank):
        lines.append(projective(vector, prime))
        vector = mat_vec(vector, prime)
    return tuple(lines)


def rfw_predicted_depth(state, prime, lines):
    x, y = state
    if state == (0, 0):
        return 0
    if y == 0:
        return 1
    if x == 0:
        return 2
    line = projective((inv0(x, prime), inv0(y, prime)), prime)
    if line not in lines:
        return 0
    index = lines.index(line)
    check(index >= 2, "RFW torus line cannot be a coordinate line")
    return len(lines) + 1 - index


def functional_depths(states, successor):
    depths = {}
    for start in states:
        if start in depths:
            continue
        path = []
        location = {}
        cursor = start
        while cursor not in depths and cursor not in location:
            location[cursor] = len(path)
            path.append(cursor)
            cursor = successor[cursor]
        if cursor in location:
            cut = location[cursor]
            for state in path[cut:]:
                depths[state] = 0
            path = path[:cut]
        for state in reversed(path):
            depths[state] = depths[successor[state]] + 1
    return depths


def rfw_one_fibre(target, prime):
    a, b = target
    if a == 0:
        return prime if b == 0 else 0
    if b == 0:
        return 2
    return int(a != b)


def rfw_all_fibre(target, time, prime, rank, lines):
    if time == 0:
        return 1
    if target == (0, 0):
        if time == 1:
            return prime
        return 1 + min(time + 1, rank) * (prime - 1)
    depth = rfw_predicted_depth(target, prime, lines)
    if depth == 0:
        return 1
    x, y = target
    if x == 0:
        return 0
    if y == 0:
        return 2 if time == 1 else int(2 <= time <= rank - 2)
    return int(time <= rank - 1 - depth)


def audit_rfw():
    signatures = []
    # Include p=2 as a scope-pressure control even though the proposed lane is odd.
    for prime in (2, 3, 5, 7, 11, 13):
        states = tuple(product(range(prime), repeat=2))
        successor = {state: rfw_step(state, prime) for state in states}
        rank = fib_rank(prime)
        lines = rfw_bad_lines(prime)
        check(len(lines) == len(set(lines)) == rank, f"RFW line orbit p={prime}")
        depths = functional_depths(states, successor)
        for state in states:
            check(depths[state] == rfw_predicted_depth(state, prime, lines),
                  f"RFW depth p={prime} state={state}")
        expected = Counter({0: prime * prime - rank * (prime - 1),
                            1: prime - 1})
        expected[2] += 2 * (prime - 1)
        for depth in range(3, rank):
            expected[depth] += prime - 1
        check(Counter(depths.values()) == expected, f"RFW histogram p={prime}")
        check(max(depths.values()) == rank - 1, f"RFW height p={prime}")

        one = Counter(successor.values())
        for target in states:
            check(one[target] == rfw_one_fibre(target, prime),
                  f"RFW one-fibre p={prime} target={target}")
        current = {state: state for state in states}
        for time in range(rank + 2):
            fibres = Counter(current.values())
            for target in states:
                check(fibres[target] == rfw_all_fibre(
                    target, time, prime, rank, lines),
                    f"RFW all-fibre p={prime} t={time} target={target}")
            current = {state: successor[value] for state, value in current.items()}

        # On the nonsingular torus the reciprocal coordinates advance linearly.
        conjugacy_checks = 0
        for x, y in states:
            if x and y and (x + y) % prime:
                left = rfw_step((x, y), prime)
                reciprocals = (inv0(x, prime), inv0(y, prime))
                advanced = mat_vec(reciprocals, prime)
                check((inv0(left[0], prime), inv0(left[1], prime)) == advanced,
                      f"RFW reciprocal conjugacy p={prime} state={(x, y)}")
                conjugacy_checks += 1
        signatures.append((prime, rank, max(depths.values()), len(one),
                           conjugacy_checks))
    return signatures


# ---------------------------------------------------------------------------
# CNG: cyclic neighbour gcd / sliding meet


def meet_step(word):
    size = len(word)
    if size == 0:
        return word
    return tuple(min(word[index], word[(index + 1) % size])
                 for index in range(size))


def window_meet(word, time):
    size = len(word)
    if size == 0:
        return word
    return tuple(min(word[(index + offset) % size]
                     for offset in range(time + 1))
                 for index in range(size))


def meet_depth(word):
    if len(word) <= 1:
        return 0
    floor = min(word)
    flags = tuple(value > floor for value in word)
    if not any(flags):
        return 0
    longest = run = 0
    for flag in flags + flags:
        run = run + 1 if flag else 0
        longest = max(longest, run)
    return min(longest, len(word) - 1)


def prime_power_value(exponents, prime):
    return tuple(prime ** exponent for exponent in exponents)


def gcd_step(values):
    size = len(values)
    return tuple(gcd(values[index], values[(index + 1) % size])
                 for index in range(size))


def audit_cng():
    signatures = []
    for cap, size in ((0, 1), (1, 1), (1, 2), (1, 5), (2, 3), (2, 5), (3, 4)):
        carrier = tuple(product(range(cap + 1), repeat=size))
        depths = Counter()
        for word in carrier:
            for time in range(size + 2):
                check(iterate(meet_step, word, time) == window_meet(word, time),
                      f"CNG window cap={cap} size={size} word={word} t={time}")
            depth = meet_depth(word)
            terminal = (min(word),) * size
            check(iterate(meet_step, word, depth) == terminal,
                  f"CNG depth upper cap={cap} size={size} word={word}")
            if depth:
                check(iterate(meet_step, word, depth - 1) != terminal,
                      f"CNG depth sharp cap={cap} size={size} word={word}")
            values = prime_power_value(word, 2)
            check(gcd_step(values) == prime_power_value(meet_step(word), 2),
                  f"CNG literal gcd shadow cap={cap} size={size} word={word}")
            depths[depth] += 1
        check(max(depths) == max(0, size - 1),
              f"CNG global height cap={cap} size={size}")
        # The binary case is literally word AND its cyclic right shift.
        if cap == 1:
            for word in carrier:
                bits = sum(value << index for index, value in enumerate(word))
                out = sum(value << index for index, value in enumerate(meet_step(word)))
                mask = (1 << size) - 1
                shifted = ((bits >> 1) | ((bits & 1) << (size - 1))) if size else 0
                check(out == (bits & shifted & mask),
                      f"CNG binary AND conjugacy size={size} word={word}")
        signatures.append((cap, size, len(carrier), dict(sorted(depths.items()))))
    return signatures


# ---------------------------------------------------------------------------
# AA01/USP: unit-pivot Schur stripping over two nonisomorphic order-four rings


class Ring:
    def __init__(self, name, elements, add, multiply, units, inverse):
        self.name = name
        self.elements = tuple(elements)
        self.add = add
        self.multiply = multiply
        self.units = frozenset(units)
        self.inverse = inverse
        self.zero = 0

    def neg(self, value):
        return next(candidate for candidate in self.elements
                    if self.add(value, candidate) == self.zero)

    def sub(self, left, right):
        return self.add(left, self.neg(right))


def ring_z4():
    return Ring("Z4", range(4), lambda a, b: (a + b) % 4,
                lambda a, b: a * b % 4, (1, 3),
                lambda a: pow(a, -1, 4))


def dual_mul(left, right):
    a, b = left & 1, (left >> 1) & 1
    c, d = right & 1, (right >> 1) & 1
    return (a * c) | (((a * d + b * c) % 2) << 1)


def ring_dual_f2():
    return Ring("F2eps", range(4), lambda a, b: a ^ b,
                dual_mul, (1, 3), lambda a: a)


FAIL = None


def matrices(ring, size):
    if size == 0:
        yield ()
        return
    for entries in product(ring.elements, repeat=size * size):
        yield tuple(tuple(entries[size * row:size * (row + 1)])
                    for row in range(size))


def schur_step(matrix, ring):
    if matrix is FAIL or matrix == ():
        return matrix
    size = len(matrix)
    pivot = matrix[0][0]
    if pivot not in ring.units:
        return FAIL
    if size == 1:
        return ()
    pivot_inverse = ring.inverse(pivot)
    answer = []
    for row in range(1, size):
        output_row = []
        for column in range(1, size):
            correction = ring.multiply(
                ring.multiply(matrix[row][0], pivot_inverse), matrix[0][column])
            output_row.append(ring.sub(matrix[row][column], correction))
        answer.append(tuple(output_row))
    return tuple(answer)


def audit_usp():
    signatures = []
    for ring in (ring_z4(), ring_dual_f2()):
        order, units = len(ring.elements), len(ring.units)
        for size in (0, 1, 2, 3):
            carrier = tuple(matrices(ring, size))
            for time in range(size + 1):
                survivors = sum(iterate(lambda matrix: schur_step(matrix, ring),
                                        matrix, time) is not FAIL
                                for matrix in carrier)
                check(survivors == units ** time * order ** (size * size - time),
                      f"USP survival ring={ring.name} n={size} t={time}")
            if size:
                failure_shells = []
                for time in range(size):
                    first_failure = sum(
                        iterate(lambda matrix: schur_step(matrix, ring), matrix, time)
                        is not FAIL
                        and iterate(lambda matrix: schur_step(matrix, ring), matrix,
                                    time + 1) is FAIL
                        for matrix in carrier)
                    predicted = (units ** time * order ** (size * size - time)
                                 * (order - units) // order)
                    check(first_failure == predicted,
                          f"USP failure shell ring={ring.name} n={size} t={time}")
                    failure_shells.append(first_failure)
                successful = units ** size * order ** (size * size - size)
                check(sum(failure_shells) + successful == len(carrier),
                      f"USP mass ring={ring.name} n={size}")

            # Every time-t target fibre from the matching source stratum.
            for time in range(0, min(2, 3 - size) + 1):
                source_size = size + time
                source = tuple(matrices(ring, source_size))
                fibres = Counter(iterate(lambda matrix: schur_step(matrix, ring),
                                         matrix, time) for matrix in source)
                predicted = units ** time * order ** (
                    2 * size * time + time * (time - 1))
                for target in carrier:
                    check(fibres[target] == predicted,
                          f"USP target ring={ring.name} k={size} t={time}")
        signatures.append((ring.name, order, units))
    return signatures


# ---------------------------------------------------------------------------
# BQC: consecutive-block loopless OR quotient of labelled simple graphs


def graph_edges(size):
    return tuple(combinations(range(size), 2))


def graph_step(code, size, divisor):
    edges = graph_edges(size)
    position = {edge: index for index, edge in enumerate(edges)}
    answer = 0
    for index, (left, right) in enumerate(edges):
        if not ((code >> index) & 1):
            continue
        image_left, image_right = left // divisor, right // divisor
        if image_left == image_right:
            continue
        edge = tuple(sorted((image_left, image_right)))
        answer |= 1 << position[edge]
    return answer


def ceil_log(base, value):
    if value <= 1:
        return 0
    height, power = 0, 1
    while power < value:
        power *= base
        height += 1
    return height


def block_sizes(size, divisor):
    count = (size + divisor - 1) // divisor
    return tuple(min(divisor, size - block * divisor) for block in range(count))


def supported_targets(size, active):
    edges = graph_edges(size)
    active_positions = [index for index, (left, right) in enumerate(edges)
                        if left < active and right < active]
    for compact in range(1 << len(active_positions)):
        code = 0
        for bit, position in enumerate(active_positions):
            if (compact >> bit) & 1:
                code |= 1 << position
        yield code


def bqc_fibre_polynomial(size, divisor, target):
    sizes = block_sizes(size, divisor)
    active = len(sizes)
    positions = {edge: index for index, edge in enumerate(graph_edges(size))}
    polynomial = Counter({0: 1})

    def multiply(left, right):
        answer = Counter()
        for degree_left, count_left in left.items():
            for degree_right, count_right in right.items():
                answer[degree_left + degree_right] += count_left * count_right
        return answer

    free = sum(comb(block, 2) for block in sizes)
    polynomial = multiply(polynomial, Counter({degree: comb(free, degree)
                                               for degree in range(free + 1)}))
    for left, right in combinations(range(active), 2):
        target_edge = (target >> positions[(left, right)]) & 1
        if target_edge:
            capacity = sizes[left] * sizes[right]
            factor = Counter({degree: comb(capacity, degree)
                              for degree in range(1, capacity + 1)})
            polynomial = multiply(polynomial, factor)
    return polynomial


def audit_bqc():
    signatures = []
    for size, divisor in ((1, 2), (2, 3), (3, 2), (5, 2), (5, 3), (6, 4)):
        total = 1 << comb(size, 2)
        height = ceil_log(divisor, size)
        for time in range(height + 2):
            direct_divisor = divisor ** time
            images = Counter()
            weighted = {}
            for code in range(total):
                iterated = iterate(lambda graph: graph_step(graph, size, divisor),
                                   code, time)
                direct = graph_step(code, size, direct_divisor)
                check(iterated == direct,
                      f"BQC semigroup n={size} c={divisor} t={time} code={code}")
                images[direct] += 1
                weighted.setdefault(direct, Counter())[code.bit_count()] += 1
            active = (size + direct_divisor - 1) // direct_divisor
            targets = tuple(supported_targets(size, active))
            check(set(images) == set(targets),
                  f"BQC image n={size} c={divisor} t={time}")
            for target in targets:
                predicted = bqc_fibre_polynomial(size, direct_divisor, target)
                check(weighted[target] == predicted,
                      f"BQC weighted fibre n={size} c={divisor} t={time} target={target}")
                check(sum(predicted.values()) == images[target],
                      f"BQC fibre mass n={size} c={divisor} t={time} target={target}")
            check(sum(images.values()) == total,
                  f"BQC global mass n={size} c={divisor} t={time}")
        if size > 1:
            extreme = 1 << (graph_edges(size).index((0, size - 1)))
            check(iterate(lambda graph: graph_step(graph, size, divisor),
                          extreme, height - 1) != 0,
                  f"BQC sharp lower n={size} c={divisor}")
            check(iterate(lambda graph: graph_step(graph, size, divisor),
                          extreme, height) == 0,
                  f"BQC sharp upper n={size} c={divisor}")
        signatures.append((size, divisor, height))
    return signatures


def main():
    print("P162_P166_CANDIDATE_HOSTILE_GATE")
    print(f"RFW {audit_rfw()}")
    print(f"CNG {audit_cng()}")
    print(f"USP {audit_usp()}")
    print(f"BQC {audit_bqc()}")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("STATUS PASS")
    print("EXTERNAL HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
