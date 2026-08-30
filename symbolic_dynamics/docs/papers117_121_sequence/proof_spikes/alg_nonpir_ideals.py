#!/usr/bin/env python3
"""Bounded exact pilots on ideals of F_p[x,y]/(x,y)^(d+1).

The ring is non-principal as soon as d>=1.  The shear lane works with exact
row spaces and scales to moderate d.  The Frobenius-root lane deliberately
uses only tiny rings and literal enumeration of every ring element.
"""

from itertools import product
from math import comb


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


def rref_basis(vectors, p):
    work = [list(vector) for vector in vectors if any(x % p for x in vector)]
    if not work:
        return ()
    cols = len(work[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][col] % p),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][col] % p, -1, p)
        work[pivot_row] = [(inverse * x) % p for x in work[pivot_row]]
        for row in range(len(work)):
            if row != pivot_row and work[row][col] % p:
                factor = work[row][col] % p
                work[row] = [
                    (x - factor * y) % p
                    for x, y in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    rows = [tuple(row) for row in work[:pivot_row]]
    rows.sort(key=lambda row: next(i for i, x in enumerate(row) if x))
    return tuple(rows)


def in_span(vector, basis, p):
    return len(rref_basis((*basis, tuple(vector)), p)) == len(basis)


def span_sum(*bases, p):
    vectors = []
    for basis in bases:
        vectors.extend(basis)
    return rref_basis(vectors, p)


def monomials(d):
    return tuple((i, total - i) for total in range(d + 1) for i in range(total + 1))


def unit_vector(index, size):
    out = [0] * size
    out[index] = 1
    return tuple(out)


class TruncatedRing:
    def __init__(self, p, d):
        self.p = p
        self.d = d
        self.monomials = monomials(d)
        self.locate = {monomial: i for i, monomial in enumerate(self.monomials)}
        self.dimension = len(self.monomials)

    def multiply_variable(self, vector, variable):
        out = [0] * self.dimension
        di, dj = (1, 0) if variable == "x" else (0, 1)
        for coefficient, (i, j) in zip(vector, self.monomials):
            target = (i + di, j + dj)
            if coefficient and sum(target) <= self.d:
                out[self.locate[target]] = (
                    out[self.locate[target]] + coefficient
                ) % self.p
        return tuple(out)

    def ideal_closure(self, generators):
        basis = rref_basis(generators, self.p)
        while True:
            images = [
                self.multiply_variable(vector, variable)
                for vector in basis
                for variable in ("x", "y")
            ]
            enlarged = span_sum(basis, rref_basis(images, self.p), p=self.p)
            if enlarged == basis:
                return basis
            basis = enlarged

    def is_ideal(self, basis):
        return all(
            in_span(self.multiply_variable(vector, variable), basis, self.p)
            for vector in basis
            for variable in ("x", "y")
        )

    def principal_monomial_ideal(self, i, j):
        return self.ideal_closure(
            (unit_vector(self.locate[(i, j)], self.dimension),)
        )

    def alpha_vector(self, vector, scalar=1):
        """Substitute x -> x + scalar*y and y -> y."""
        out = [0] * self.dimension
        for coefficient, (i, j) in zip(vector, self.monomials):
            if not coefficient:
                continue
            for k in range(i + 1):
                target = (k, i - k + j)
                value = coefficient * comb(i, k) * pow(scalar, i - k, self.p)
                out[self.locate[target]] = (
                    out[self.locate[target]] + value
                ) % self.p
        return tuple(out)

    def alpha_ideal(self, basis, scalar=1):
        return rref_basis(
            (self.alpha_vector(vector, scalar) for vector in basis), self.p
        )

    def shear_join(self, basis):
        return span_sum(basis, self.alpha_ideal(basis), p=self.p)

    def frobenius_vector(self, vector):
        out = [0] * self.dimension
        for coefficient, (i, j) in zip(vector, self.monomials):
            target = (self.p * i, self.p * j)
            if coefficient and sum(target) <= self.d:
                out[self.locate[target]] = coefficient % self.p
        return tuple(out)

    def all_vectors(self):
        return product(range(self.p), repeat=self.dimension)

    def frobenius_root(self, basis):
        preimage = [
            tuple(vector)
            for vector in self.all_vectors()
            if in_span(self.frobenius_vector(vector), basis, self.p)
        ]
        return rref_basis(preimage, self.p)

    def maximal_ideal(self):
        return rref_basis(
            (
                unit_vector(index, self.dimension)
                for index, monomial in enumerate(self.monomials)
                if sum(monomial) > 0
            ),
            self.p,
        )


def shear_samples(ring):
    samples = [()]
    for i, j in ring.monomials[1:]:
        samples.append(ring.principal_monomial_ideal(i, j))
    top = [
        unit_vector(ring.locate[(i, ring.d - i)], ring.dimension)
        for i in range(ring.d + 1)
    ]
    if len(top) >= 2:
        samples.append(ring.ideal_closure((top[0], top[-1])))
    return tuple(dict.fromkeys(samples))


def run_shear_join():
    for p, max_d in ((2, 5), (3, 4), (5, 4), (7, 3)):
        for d in range(1, max_d + 1):
            ring = TruncatedRing(p, d)
            bound = min(d, p - 1)
            for ideal in shear_samples(ring):
                AUDIT.check(ring.is_ideal(ideal), f"sample is not an ideal at {(p, d)}")
                state = ideal
                orbit_span = ideal
                depth = 0
                while True:
                    updated = ring.shear_join(state)
                    orbit_span = span_sum(
                        orbit_span,
                        ring.alpha_ideal(ideal, depth + 1),
                        p=p,
                    )
                    AUDIT.check(
                        updated == orbit_span,
                        f"orbit-span iterate failed at {(p, d, depth)}",
                    )
                    AUDIT.check(
                        ring.is_ideal(updated),
                        f"shear join left the ideal lattice at {(p, d, depth)}",
                    )
                    if updated == state:
                        break
                    state = updated
                    depth += 1
                    AUDIT.check(depth <= bound, f"shear depth exceeded bound {(p, d)}")

            witness_x_degree = min(ring.d, p - 1)
            witness = ring.principal_monomial_ideal(
                witness_x_degree, ring.d - witness_x_degree
            )
            state = witness
            witness_depth = 0
            while ring.shear_join(state) != state:
                state = ring.shear_join(state)
                witness_depth += 1
            AUDIT.check(
                witness_depth == bound,
                f"top-degree shear witness is not sharp at {(p, d)}",
            )
            print(
                f"shear p={p}, d={d}, ring-dim={ring.dimension:>2}: "
                f"sharp depth={witness_depth}"
            )


def ceil_log_base(number, base):
    exponent = 0
    power = 1
    while power < number:
        power *= base
        exponent += 1
    return exponent


def run_frobenius_root():
    for p, d in ((2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (5, 1)):
        ring = TruncatedRing(p, d)
        maximal = ring.maximal_ideal()
        zero_ideal = ()
        expected_depth = ceil_log_base(d + 1, p)
        samples = [zero_ideal]
        samples.extend(
            ring.principal_monomial_ideal(i, j)
            for i, j in ring.monomials[1:]
        )
        for initial in tuple(dict.fromkeys(samples)):
            state = initial
            depth = 0
            while state != maximal:
                updated = ring.frobenius_root(state)
                AUDIT.check(
                    span_sum(state, updated, p=p) == updated,
                    f"Frobenius root is not expansive at {(p, d, depth)}",
                )
                AUDIT.check(
                    ring.is_ideal(updated),
                    f"Frobenius root left the ideal lattice at {(p, d, depth)}",
                )
                state = updated
                depth += 1
                AUDIT.check(
                    depth <= expected_depth,
                    f"Frobenius-root orbit exceeded bound at {(p, d)}",
                )
            if initial == zero_ideal:
                AUDIT.check(
                    depth == expected_depth,
                    f"zero-ideal Frobenius depth is not sharp at {(p, d)}",
                )
        AUDIT.check(
            ring.frobenius_root(maximal) == maximal,
            f"maximal ideal is not fixed at {(p, d)}",
        )
        print(
            f"Frobenius-root p={p}, d={d}, ring-dim={ring.dimension:>2}: "
            f"zero-to-maximal depth={expected_depth}"
        )


def main():
    run_shear_join()
    run_frobenius_root()
    print(
        "FALSE CONJECTURE A: the shear closure depth is d in every "
        "characteristic; it saturates at min(d,p-1)."
    )
    print(
        "FALSE CONJECTURE B: Frobenius-root depth follows the Loewy length d; "
        "the zero ideal reaches the maximal ideal in ceil(log_p(d+1)) steps."
    )
    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
