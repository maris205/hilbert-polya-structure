"""Independent, standard-library h-adic check of the period-12 obstruction.

This computes in F_3[x]/(h^13), not in F_81 or translated Taylor jets.
All polynomials use ascending coefficients; no full degree-4^12 iterate is built.
"""

import json

P = 3


def trim(a):
    a = [x % P for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b, sign=1):
    out = a + [0] * max(0, len(b) - len(a))
    for i, value in enumerate(b):
        out[i] = (out[i] + sign * value) % P
    return trim(out)


def mul(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def divmod_poly(a, b):
    a, b = trim(a), trim(b)
    if not b:
        raise ZeroDivisionError
    quotient = [0] * max(0, len(a) - len(b) + 1)
    inverse = pow(b[-1], -1, P)
    while a and len(a) >= len(b):
        degree = len(a) - len(b)
        coefficient = a[-1] * inverse % P
        quotient[degree] = coefficient
        a = add(a, [0] * degree + [coefficient * x for x in b], -1)
    return trim(quotient), a


def rem(a, modulus):
    return divmod_poly(a, modulus)[1]


def power(a, exponent, modulus=None):
    result = [1]
    while exponent:
        if exponent & 1:
            result = mul(result, a)
            if modulus:
                result = rem(result, modulus)
        exponent >>= 1
        if exponent:
            a = mul(a, a)
            if modulus:
                a = rem(a, modulus)
    return result


def gcd(a, b):
    while b:
        a, b = b, rem(a, b)
    inverse = pow(a[-1], -1, P)
    return trim([inverse * x for x in a])


def main():
    x = [0, 1]
    h = [2, 0, 0, 2, 1]
    derivative = trim([i * h[i] for i in range(1, len(h))])
    assert gcd(h, derivative) == [1]
    assert rem(add(power(x, 81, h), x, -1), h) == []
    assert gcd(h, add(power(x, 9, h), x, -1)) == [1]

    modulus = power(h, 13)
    current = x
    orbit = []
    proper_divisor_remainders = {}
    for period in range(1, 13):
        orbit.append(rem(current, h))
        current = rem(add(current, power(current, 4, modulus)), modulus)
        if period in [1, 2, 3, 4, 6]:
            difference = rem(add(current, x, -1), h)
            assert difference
            proper_divisor_remainders[period] = difference
    assert rem(add(current, x, -1), h) == []
    assert len({tuple(value) for value in orbit}) == 12

    residual = add(current, x, -1)
    valuation = 0
    quotient = residual
    while quotient:
        next_quotient, remainder = divmod_poly(quotient, h)
        if remainder:
            break
        valuation += 1
        quotient = next_quotient
    assert valuation == 12
    first_coefficient = rem(quotient, h)
    assert first_coefficient
    assert residual == mul(power(h, 12), first_coefficient)

    print(json.dumps({
        "method": "standard-library polynomial arithmetic modulo h^13",
        "prime": P,
        "h_ascending": h,
        "irreducible_degree": 4,
        "squarefree": True,
        "orbit_mod_h_ascending": orbit,
        "proper_divisor_nonzero_remainders": proper_divisor_remainders,
        "minimal_period": 12,
        "h_adic_valuation_f12_minus_x": valuation,
        "f12_minus_x_mod_h13": "h^12 times the following polynomial",
        "h_adic_first_coefficient_ascending": first_coefficient,
        "local_multiplicity_at_each_h_root": 12,
        "local_weight_divided_by_p": 4,
        "status": "EXACT_COUNTEREXAMPLE_VERIFIED",
    }, indent=2))


if __name__ == "__main__":
    main()
