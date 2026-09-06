"""Exact bounded certificate; no global f^12 expansion and no file writes."""
import json
from flint import fmpz_mod_poly_ctx

R = fmpz_mod_poly_ctx(3)
x = R([0, 1])
h = x**4 + 2*x**3 + 2
Q = x**3 + 2*x**2 + x + 1
cycle = [x]
v = x
for j in range(1, 13):
    v = (v + v**4) % h
    if j < 12:
        assert v != x
        cycle.append(v)
assert v == x
assert len({str(v) for v in cycle}) == 12

# Elementary irreducibility certificate: neither a linear factor nor any of
# the three monic irreducible quadratics over F_3 divides h.
linear_values = [int(h(a)) for a in range(3)]
quadratics = [x*x+1, x*x+x+2, x*x+2*x+2]
remainders = [h % g for g in quadratics]
assert all(value != 0 for value in linear_values)
assert all(value != 0 for value in remainders)
assert h.is_irreducible()

modulus = h**13
v = x
for _ in range(12):
    v = (v + v.pow_mod(4, modulus)) % modulus
assert (v - x) == h**12 * Q
assert Q % h != 0
assert ((x**36)*Q) % h == x*x+x
assert (x*x+x).gcd(h) == 1

orbit_polynomial = R([1,1,2,2,1,0,2,0,0,1,0,2,1])
h1 = x**4+2*x*x+2
h2 = x**4+x*x+x+1
assert orbit_polynomial == h*h1*h2
assert orbit_polynomial.gcd(orbit_polynomial.derivative()) == 1
assert orbit_polynomial(0) == 1
# All three quartics belong to the displayed cycle, not just to a union of
# unrelated Frobenius orbits.
assert h1.compose(cycle[1]) % h == 0
assert h2.compose(cycle[2]) % h == 0
assert (x.pow_mod(81,h)-x)%h == 0
assert all((u+u**4)%h == cycle[(j+1)%12] for j,u in enumerate(cycle))

# B(T) = product (1 + a_j/(1+a_j) T), since product(1+a_j)=1.
# This formula computes it directly from the ordinary cycle polynomial.
B = R(0)
for i, coefficient in enumerate(orbit_polynomial.coeffs()):
    B += coefficient * ((-1)**i) * (1+x)**(12-i)
expected_B = R([1,0,0,0,1,2,0,2,1,0,0,2,1])
assert B == expected_B
assert B[4] == 1 and all(B[j] == 0 for j in range(1,4))

print(json.dumps({
    "status": "PASS",
    "characteristic": 3,
    "h_coefficients_ascending": [2,0,0,2,1],
    "linear_values": linear_values,
    "quadratic_remainders": [str(r) for r in remainders],
    "minimal_period": 12,
    "orbit_representatives": [str(r) for r in cycle],
    "modulus_degree": modulus.degree(),
    "h_adic_valuation": 12,
    "h_adic_leading_quotient_coefficients_ascending": [1,1,2,1],
    "translated_leading_coefficient": "a^2 + a",
    "cycle_polynomial_coefficients_ascending": [int(c) for c in orbit_polynomial.coeffs()],
    "orbit_polynomial_B_coefficients_ascending": [int(c) for c in B.coeffs()],
    "B_minus_one_order": 4,
}, indent=2))
