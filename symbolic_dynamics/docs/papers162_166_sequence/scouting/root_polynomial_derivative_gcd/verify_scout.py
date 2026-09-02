#!/usr/bin/env python3
"""Literal finite-field checks for derivative-GCD dynamics."""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def degree(poly):
    poly = trim(poly)
    return -1 if poly == (0,) else len(poly) - 1


def monic_polynomials(p, maximum_degree):
    out = [(1,)]
    for d in range(1, maximum_degree + 1):
        out.extend(tuple(coefficients) + (1,) for coefficients in product(range(p), repeat=d))
    return tuple(out)


def poly_divmod(left, right, p):
    left = list(trim(left))
    right = trim(right)
    if right == (0,):
        raise ZeroDivisionError
    dr = degree(right)
    inverse = pow(right[-1], -1, p)
    quotient = [0] * max(1, len(left) - len(right) + 1)
    while not (len(left) == 1 and left[0] == 0) and len(left) - 1 >= dr:
        shift = len(left) - 1 - dr
        coefficient = left[-1] * inverse % p
        quotient[shift] = coefficient
        for i, value in enumerate(right):
            left[i + shift] = (left[i + shift] - coefficient * value) % p
        left = list(trim(left))
    return trim(quotient), trim(left)


def poly_multiply(left, right, p):
    if left == (0,) or right == (0,):
        return (0,)
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % p
    return trim(answer)


def monic(poly, p):
    poly = trim(poly)
    if poly == (0,):
        return poly
    inverse = pow(poly[-1], -1, p)
    return tuple(coefficient * inverse % p for coefficient in poly)


def poly_gcd(left, right, p):
    left, right = trim(left), trim(right)
    while right != (0,):
        _, remainder = poly_divmod(left, right, p)
        left, right = right, remainder
    return monic(left, p)


def derivative(poly, p):
    if len(poly) <= 1:
        return (0,)
    return trim([(i * poly[i]) % p for i in range(1, len(poly))])


def update(poly, p):
    return poly_gcd(poly, derivative(poly, p), p)


def irreducibles(p, maximum_degree):
    irreducible = []
    by_degree = defaultdict(list)
    for poly in monic_polynomials(p, maximum_degree):
        d = degree(poly)
        if d <= 0:
            continue
        reducible = False
        for divisor_degree in range(1, d // 2 + 1):
            for divisor in by_degree[divisor_degree]:
                if poly_divmod(poly, divisor, p)[1] == (0,):
                    reducible = True
                    break
            if reducible:
                break
        if not reducible:
            irreducible.append(poly)
            by_degree[d].append(poly)
    return tuple(irreducible)


def factor(poly, irreducible, p):
    remainder = poly
    answer = {}
    for prime in irreducible:
        exponent = 0
        while degree(remainder) >= degree(prime):
            quotient, rem = poly_divmod(remainder, prime, p)
            if rem != (0,):
                break
            exponent += 1
            remainder = quotient
        if exponent:
            answer[prime] = exponent
        if remainder == (1,):
            break
    check(remainder == (1,), f"complete factorization {poly}, rem={remainder}")
    return answer


def reconstruct(exponents, p):
    answer = (1,)
    for prime, exponent in exponents.items():
        for _ in range(exponent):
            answer = poly_multiply(answer, prime, p)
    return answer


def predicted_iterate(exponents, time, p):
    return {
        prime: exponent - min(time, exponent % p)
        for prime, exponent in exponents.items()
        if exponent - min(time, exponent % p) > 0
    }


def actual_iterate(poly, time, p):
    value = poly
    for _ in range(time):
        value = update(value, p)
    return value


def poly_convolve(left, right, cap):
    answer = [0] * (min(cap, len(left) + len(right) - 2) + 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            if i + j > cap:
                break
            answer[i + j] += a * b
    return answer


def allowed_exponent_series(prime_degree, p, cap, max_residue):
    answer = [0] * (cap + 1)
    for exponent in range(cap // prime_degree + 1):
        if exponent % p <= max_residue:
            answer[exponent * prime_degree] = 1
    return answer


def global_residue_product(irreducible, p, cap, max_residue):
    answer = [1]
    for prime in irreducible:
        answer = poly_convolve(
            answer,
            allowed_exponent_series(degree(prime), p, cap, max_residue),
            cap,
        )
    answer.extend([0] * (cap + 1 - len(answer)))
    return answer


def fibre_polynomial(target_factors, irreducible, p, cap, time):
    s = min(time, p - 1)
    answer = [1]
    target_primes = set(target_factors)
    for prime in irreducible:
        d = degree(prime)
        local = [0] * (cap + 1)
        if prime not in target_primes:
            local[0] = 1
            for extra in range(1, s + 1):
                if extra * d <= cap:
                    local[extra * d] = 1
        else:
            exponent = target_factors[prime]
            residue = exponent % p
            if residue == 0:
                for extra in range(s + 1):
                    if extra * d <= cap:
                        local[extra * d] = 1
            elif time < p and residue <= p - time - 1:
                if time * d <= cap:
                    local[time * d] = 1
            # otherwise this target is outside the time image
        answer = poly_convolve(answer, local, cap)
    answer.extend([0] * (cap + 1 - len(answer)))
    return answer


def geometric_sum(q, top):
    return sum(q ** d for d in range(top + 1))


def image_criterion(target_factors, p, cap, time):
    if time >= p:
        time = p - 1
    minimum_source_degree = 0
    for prime, exponent in target_factors.items():
        d = degree(prime)
        residue = exponent % p
        if residue == 0:
            minimum_source_degree += exponent * d
        elif residue <= p - time - 1:
            minimum_source_degree += (exponent + time) * d
        else:
            return False
    return minimum_source_degree <= cap


def main():
    boxes = ((2, 7), (3, 6), (5, 5), (7, 4))
    rows = []
    for p, cap in boxes:
        phase = monic_polynomials(p, cap)
        irreducible = irreducibles(p, cap)
        factors = {poly: factor(poly, irreducible, p) for poly in phase}
        depth_histogram = Counter()

        # Literal factor exponent law, point clocks, and strict recurrence.
        for poly in phase:
            exponents = factors[poly]
            predicted_depth = max((exponent % p for exponent in exponents.values()), default=0)
            value = poly
            actual_depth = 0
            while update(value, p) != value:
                next_value = update(value, p)
                check(degree(next_value) < degree(value), "strict degree loss")
                value = next_value
                actual_depth += 1
            check(actual_depth == predicted_depth, f"depth p={p}, f={poly}")
            depth_histogram[actual_depth] += 1
            for time in range(p + 2):
                predicted = reconstruct(predicted_iterate(exponents, time, p), p)
                literal = actual_iterate(poly, time, p)
                check(literal == predicted, f"iterate p={p},t={time},f={poly}")

        check(max(depth_histogram) == min(p - 1, cap), "sharp height")
        fixed_count = sum(count for depth, count in depth_histogram.items() if depth == 0)
        check(fixed_count == geometric_sum(p, cap // p), "fixed count")

        # Degree-refined depth and time-image Euler products.
        for time in range(p + 1):
            depth_product = global_residue_product(irreducible, p, cap, min(time, p - 1))
            direct_depth = Counter(degree(poly) for poly in phase
                                   if max((e % p for e in factors[poly].values()), default=0) <= time)
            for d in range(cap + 1):
                check(depth_product[d] == direct_depth[d], "depth Euler product")

            images = {actual_iterate(poly, time, p) for poly in phase}
            predicted_images = {poly for poly in phase
                                if image_criterion(factors[poly], p, cap, time)}
            check(images == predicted_images, "capped time-image criterion")

        # Every-time, every-target degree-excess fibres.
        for time in range(p + 1):
            actual = defaultdict(Counter)
            for source in phase:
                target = actual_iterate(source, time, p)
                actual[target][degree(source) - degree(target)] += 1
            for target in phase:
                room = cap - degree(target)
                formula = fibre_polynomial(factors[target], irreducible, p, room, time)
                direct = actual.get(target, Counter())
                for excess in range(room + 1):
                    check(formula[excess] == direct[excess],
                          f"fibre p={p},N={cap},t={time},target={target},e={excess}")

        rows.append((p, cap, len(phase), len(irreducible),
                     tuple(sorted(depth_histogram.items())), fixed_count))

    payload = "\n".join(repr(row) for row in rows)
    print("POLYNOMIAL_DERIVATIVE_GCD_DYNAMICS_SCOUT_V1")
    print(f"boxes={len(boxes)}")
    print(f"row_sha256={sha256(payload.encode()).hexdigest()}")
    print(f"assertions={ASSERTIONS}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
