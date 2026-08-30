#!/usr/bin/env python3
"""Exact pilots for a module clock and three representation-data maps."""

from collections import Counter
from itertools import product


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


def rank_mod(matrix, p):
    work = [[entry % p for entry in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][col]), None
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][col], -1, p)
        work[pivot_row] = [(inverse * x) % p for x in work[pivot_row]]
        for row in range(rows):
            if row != pivot_row and work[row][col]:
                factor = work[row][col]
                work[row] = [
                    (x - factor * y) % p
                    for x, y in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def matmul(a, b, p):
    bt = list(zip(*b))
    return [
        [sum(x * y for x, y in zip(row, col)) % p for col in bt]
        for row in a
    ]


def valuation_delay_update(vector, p, modulus):
    return tuple(vector[1:]) + ((p * vector[0]) % modulus,)


def module_kernel_size(t, p, exponent, width):
    quotient, remainder = divmod(t, width)
    kernel_exponent = (
        (width - remainder) * min(exponent, quotient)
        + remainder * min(exponent, quotient + 1)
    )
    return p**kernel_exponent


def run_module_shift():
    for p, exponent, width in (
        (2, 2, 2),
        (2, 3, 2),
        (2, 2, 3),
        (3, 2, 2),
        (3, 2, 3),
        (5, 1, 3),
    ):
        modulus = p**exponent
        zero = (0,) * width
        depths = Counter()
        for vector in product(range(modulus), repeat=width):
            state = tuple(vector)
            depth = 0
            while state != zero:
                state = valuation_delay_update(state, p, modulus)
                depth += 1
                AUDIT.check(
                    depth <= exponent * width,
                    f"module orbit exceeded bound at {(p, exponent, width)}",
                )
            depths[depth] += 1

        for t in range(exponent * width + 1):
            cumulative = sum(count for depth, count in depths.items() if depth <= t)
            AUDIT.check(
                cumulative == module_kernel_size(t, p, exponent, width),
                f"module kernel CDF mismatch at {(p, exponent, width, t)}",
            )
        AUDIT.check(
            max(depths) == exponent * width,
            f"module depth is not sharp at {(p, exponent, width)}",
        )
        print(
            f"module p={p}, a={exponent}, r={width}: states={modulus ** width:>4}, "
            f"sharp depth={max(depths)}"
        )


def partitions(n, maximum=None):
    if n == 0:
        return ((),)
    if maximum is None:
        maximum = n
    out = []
    for first in range(min(maximum, n), 0, -1):
        for tail in partitions(n - first, first):
            out.append((first,) + tail)
    return tuple(out)


def remove_corners(partition):
    out = []
    for i, part in enumerate(partition):
        following = partition[i + 1] if i + 1 < len(partition) else 0
        if part > following:
            reduced = list(partition)
            reduced[i] -= 1
            if reduced[i] == 0:
                reduced.pop(i)
            out.append(tuple(reduced))
    return tuple(out)


def up_down_matrix(n):
    states = partitions(n)
    removals = {state: remove_corners(state) for state in states}
    out = [[0] * len(states) for _ in states]
    for source_index, source in enumerate(states):
        for lower in removals[source]:
            for target_index, target in enumerate(states):
                if lower in removals[target]:
                    out[target_index][source_index] += 1
    return states, out


def shifted_matrix(matrix, eigenvalue, p):
    out = [[entry % p for entry in row] for row in matrix]
    for i in range(len(out)):
        out[i][i] = (out[i][i] - eigenvalue) % p
    return out


def partition_number(n):
    return len(partitions(n)) if n >= 0 else 0


def up_down_eigen_multiplicity(n, eigenvalue):
    return partition_number(n - eigenvalue) - partition_number(n - eigenvalue - 1)


def run_up_down():
    large_prime = 101
    for n in range(1, 10):
        states, matrix = up_down_matrix(n)
        for eigenvalue in range(n + 1):
            nullity = len(states) - rank_mod(
                shifted_matrix(matrix, eigenvalue, large_prime), large_prime
            )
            AUDIT.check(
                nullity == up_down_eigen_multiplicity(n, eigenvalue),
                f"characteristic-zero eigenspace mismatch at {(n, eigenvalue)}",
            )

    for p in (2, 3, 5, 7):
        states, matrix = up_down_matrix(p)
        first_nullity = len(states) - rank_mod(matrix, p)
        square = matmul(matrix, matrix, p)
        second_nullity = len(states) - rank_mod(square, p)
        expected_kernel = partition_number(p) - partition_number(p - 1)
        AUDIT.check(
            first_nullity == expected_kernel,
            f"up-down first kernel mismatch at p={p}",
        )
        AUDIT.check(
            second_nullity == first_nullity + 1,
            f"missing first length-two modular Jordan chain at p={p}",
        )
        print(
            f"Young up-down n=p={p}: dimension={len(states):>2}, "
            f"nullities T,T^2=({first_nullity},{second_nullity})"
        )


def shift_mask(mask, m, amount):
    out = 0
    for i in range(m):
        if mask >> i & 1:
            out |= 1 << ((i + amount) % m)
    return out


def mckay_neighbor(mask, m):
    return shift_mask(mask, m, 1) | shift_mask(mask, m, -1)


def run_cyclic_mckay():
    for m in range(3, 15):
        singleton = 1
        state = singleton
        if m % 2:
            for _ in range(m - 1):
                state = mckay_neighbor(state, m)
            AUDIT.check(
                state == (1 << m) - 1,
                f"odd cyclic McKay support did not fill at m={m}",
            )
            before = singleton
            for _ in range(m - 2):
                before = mckay_neighbor(before, m)
            AUDIT.check(
                before != (1 << m) - 1,
                f"odd cyclic McKay depth was not sharp at m={m}",
            )
        else:
            for _ in range(m // 2 - 1):
                state = mckay_neighbor(state, m)
            even_class = sum(1 << i for i in range(0, m, 2))
            odd_class = sum(1 << i for i in range(1, m, 2))
            expected_class = (
                even_class if (m // 2 - 1) % 2 == 0 else odd_class
            )
            AUDIT.check(
                state == expected_class,
                f"even cyclic McKay parity core mismatch at m={m}",
            )
            AUDIT.check(
                mckay_neighbor(even_class, m) == odd_class
                and mckay_neighbor(odd_class, m) == even_class,
                f"even cyclic McKay 2-cycle failed at m={m}",
            )


def sumset_square(mask, m):
    support = [i for i in range(m) if mask >> i & 1]
    out = 0
    for i in support:
        for j in support:
            out |= 1 << ((i + j) % m)
    return out


def multiplicative_order_two(prime):
    value = 1
    for order in range(1, prime):
        value = 2 * value % prime
        if value == 1:
            return order
    raise AssertionError("2 has no multiplicative order")


def run_tensor_square_support():
    for prime in (3, 5, 7, 11, 13):
        singleton = 1 << 1
        state = singleton
        order = multiplicative_order_two(prime)
        for _ in range(order):
            state = sumset_square(state, prime)
        AUDIT.check(state == singleton, f"singleton doubling period failed at p={prime}")
        for mask in range(1, 1 << prime):
            if mask.bit_count() < 2:
                continue
            state = mask
            for _ in range(prime):
                state = sumset_square(state, prime)
                if state == (1 << prime) - 1:
                    break
            AUDIT.check(
                state == (1 << prime) - 1,
                f"non-singleton tensor support did not absorb at {(prime, mask)}",
            )


def main():
    run_module_shift()
    run_up_down()
    run_cyclic_mckay()
    run_tensor_square_support()
    print(
        "FALSE CONJECTURE A: all module deaths occur at multiples of r; the "
        "coordinate phase creates every residue class in the depth profile."
    )
    print(
        "FALSE CONJECTURE B: reducing the Young up-down spectrum modulo p is "
        "semisimple; at n=p a length-two zero Jordan chain appears."
    )
    print(
        "COLLISION CERTIFICATE: cyclic tensor-square support is literally "
        "sumset squaring, despite its representation-theoretic notation."
    )
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
