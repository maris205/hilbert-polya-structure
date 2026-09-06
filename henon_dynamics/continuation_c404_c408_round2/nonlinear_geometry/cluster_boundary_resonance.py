"""Exact local certificate, not a census or an all-period theorem.

For F_6(x,y)=(y,(1+y**6)/x), certify the five-step boundary
configuration (0,i,u,-u,-i), u**6+i*u+1=0, has local length two.
No floating-point roots are used.  Output is deterministic JSON.
"""

import json

import sympy as sp


u = sp.symbols("u")
x = sp.symbols("x0:5")
eqs = [x[j] ** 6 + 1 - x[(j - 1) % 5] * x[(j + 1) % 5] for j in range(5)]
point = dict(zip(x, [0, sp.I, u, -u, -sp.I]))
g = sp.Poly(u**6 + sp.I * u + 1, u, extension=sp.I)


def polynomial(value):
    return sp.Poly(sp.expand(value), u, extension=sp.I)


def residue(value):
    numerator, denominator = sp.fraction(sp.cancel(value))
    numerator = polynomial(numerator).rem(g)
    denominator = polynomial(denominator).rem(g)
    assert sp.gcd(denominator, g).degree() == 0
    return (numerator * sp.invert(denominator, g)).rem(g)


def nonzero_at_every_root(value):
    return sp.gcd(residue(value), g).degree() == 0


equation_residues = [str(residue(f.subs(point)).as_expr()) for f in eqs]
assert equation_residues == ["0"] * 5
assert sp.gcd(g, g.diff()).degree() == 0

jacobian = sp.Matrix(eqs).jacobian(x).subs(point)
assert residue(jacobian.det()).is_zero
implicit_jacobian = jacobian[1:5, 1:5]
minor = sp.factor(implicit_jacobian.det())
assert nonzero_at_every_root(minor)

# Solve f_1=...=f_4=0 for x_1,...,x_4 as functions of a=x_0.
# Formal implicit differentiation works over each simple root field of g.
velocity = -implicit_jacobian.inv() * jacobian[1:5, 0]
full_velocity = sp.Matrix([1, *velocity])
hessians = [sp.hessian(f, x).subs(point) for f in eqs]
forcing = sp.Matrix(
    [(full_velocity.T * hessians[j] * full_velocity)[0] for j in range(1, 5)]
)
acceleration = -implicit_jacobian.inv() * forcing
first_derivative = (jacobian[0:1, :] * full_velocity)[0]
second_derivative = (
    (full_velocity.T * hessians[0] * full_velocity)[0]
    + (jacobian[0:1, 1:5] * acceleration)[0]
)
claimed_second_derivative = 2 * u**2 * (9 * u**5 - sp.I) / (9 * (6 * u**5 - sp.I))
assert residue(first_derivative).is_zero
assert residue(second_derivative - claimed_second_derivative).is_zero
assert nonzero_at_every_root(second_derivative)

# At a configuration with two zeros (0,t,0,1/t,1/t), t^6=-1,
# use 6*t^5=-6/t and 6*(1/t)^5=-6*t to simplify its Jacobian.
t = sp.symbols("t", nonzero=True)
two_zero_point = [0, t, 0, 1 / t, 1 / t]
two_zero_jacobian = sp.zeros(5)
diagonal = [0, -6 / t, 0, -6 * t, -6 * t]
for j in range(5):
    two_zero_jacobian[j, j] = diagonal[j]
    two_zero_jacobian[j, (j - 1) % 5] -= two_zero_point[(j + 1) % 5]
    two_zero_jacobian[j, (j + 1) % 5] -= two_zero_point[(j - 1) % 5]
assert sp.factor(two_zero_jacobian.det()) == -6 / t

report = {
    "status": "PASS_EXACT_LOCAL_CERTIFICATE",
    "field": "QQ(i), then each root field of u^6+i*u+1",
    "map": "F_6(x,y)=(y,(1+y^6)/x)",
    "clock": 5,
    "point": ["0", "i", "u", "-u", "-i"],
    "minimal_polynomial_condition": str(g.as_expr()),
    "equation_residues": equation_residues,
    "root_polynomial_squarefree": True,
    "full_jacobian_determinant_zero": True,
    "implicit_4x4_minor": str(minor),
    "implicit_minor_invertible_at_every_root": True,
    "remaining_equation_first_derivative": "0",
    "remaining_equation_second_derivative": str(claimed_second_derivative),
    "second_derivative_nonzero_at_every_root": True,
    "local_length": 2,
    "two_zero_configuration_jacobian_determinant": "-6/t",
    "single_zero_quotient_length_per_coordinate": 6**3,
    "two_zero_configurations_total": 5 * 6,
    "double_points_total": 5 * 2 * 6,
    "boundary_length_from_proved_decomposition": 5 * 6**3 - 5 * 6 + 5 * 2 * 6,
    "torus_length_from_proved_decomposition": 6**5 - (5 * 6**3 - 5 * 6 + 5 * 2 * 6),
    "rejected_low_period_fit_value": 6**5 - 5 * 6**3 + 5 * 6,
    "scope": "Local algebra plus the written period-5 decomposition; not an independent exhaustive Groebner census.",
}
print(json.dumps(report, indent=2, sort_keys=True))
