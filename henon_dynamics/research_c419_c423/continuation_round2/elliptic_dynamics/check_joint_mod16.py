"""Exact, bounded diagnostic for ED1; never an infinite-law proof.

Only standard library. Reconstruct the proposed mixture and enumerate each
matrix directly modulo 2**k for 1 <= k <= 4. Value k means censored >= k,
including determinant zero modulo 2**k. No files are written.
"""

from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
import sys


def caplaw(k, minimum, mass):
    law = {j: mass(j) for j in range(minimum, k)}
    law[k] = 1 - sum(law.values(), Q(0))
    return law


def proposed(k):
    out = defaultdict(Q)

    def put(a, b, weight):
        out[min(a, k), min(b, k)] += weight

    geom0 = caplaw(k, 0, lambda j: Q(1, 2 ** (j + 1)))
    geom1 = caplaw(k, 1, lambda j: Q(1, 2**j))
    detlaw = caplaw(
        k, 0, lambda j: Q(3, 4) * (Q(1, 2**j) - Q(1, 2 ** (2 * j + 1)))
    )
    # GL_2(F_2): order-three, nonidentity unipotent, identity.
    put(0, 0, Q(1, 3))
    put(1, 1, Q(1, 4))
    for a, b in product(geom0, repeat=2):
        put(2 + a, 2 + b, Q(1, 4) * geom0[a] * geom0[b])
    # The identity branch is I+2M; its two valuations shift by two.
    put(2, 2, Q(1, 6) * Q(1, 8))
    for a, weight in geom1.items():
        put(2 + a, 2, Q(1, 6) * Q(3, 16) * weight)
        put(2, 2 + a, Q(1, 6) * Q(3, 16) * weight)
    for a, weight in detlaw.items():
        put(4 + a, 2, Q(1, 6) * Q(1, 16) * weight)
        put(2, 4 + a, Q(1, 6) * Q(1, 16) * weight)
    for a, b in product(geom1, repeat=2):
        put(2 + a, 2 + b, Q(1, 6) * Q(3, 8) * geom1[a] * geom1[b])
    return dict(out)


def truncated_v2(number, k):
    for j in range(k):
        if number % (2 ** (j + 1)):
            return j
    return k


def direct(k):
    counts = defaultdict(int)
    modulus = 2**k
    total = 0
    for a, b, c, d in product(range(modulus), repeat=4):
        det = a * d - b * c
        if not det % 2:
            continue
        left = truncated_v2(1 - a - d + det, k)
        right = truncated_v2(1 + a + d + det, k)
        counts[left, right] += 1
        total += 1
    expected = 6 * 2 ** (4 * (k - 1))
    if total != expected:
        raise RuntimeError(("incorrect group order", k, total, expected))
    return total, {key: Q(value, total) for key, value in counts.items()}


def main():
    print("Python", sys.version.split()[0])
    for k in range(1, 5):
        total, observed = direct(k)
        expected = proposed(k)
        if sum(expected.values(), Q(0)) != 1:
            raise RuntimeError(("mixture not normalized", k))
        if observed != expected:
            differences = {
                str(key): (str(observed.get(key, 0)), str(expected.get(key, 0)))
                for key in set(observed) | set(expected)
                if observed.get(key, 0) != expected.get(key, 0)
            }
            raise RuntimeError(("distribution mismatch", k, differences))
        print(f"k={k}; modulus={2**k}; matrices={total}; bins={len(observed)}; PASS")
    print("Bounded censored distributions only; no prime limit or novelty certified.")


if __name__ == "__main__":
    main()
