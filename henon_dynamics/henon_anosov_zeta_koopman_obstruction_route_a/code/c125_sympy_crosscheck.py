#!/usr/bin/env python3
"""Fresh SymPy reconstruction of the C125 exact claims."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "results/c125_anosov_evidence.json").read_text())
A = sp.Matrix([[2, 1], [1, 1]])
I = sp.eye(2)
z = sp.symbols("z")
checks = 0

assert A.det() == 1 and sp.trace(A) == 3
checks += 2
characteristic = sp.factor(A.charpoly().as_expr())
assert characteristic == sp.Symbol("lambda") ** 2 - 3 * sp.Symbol("lambda") + 1
checks += 1
assert A.eigenvals() == {(sp.Integer(3) - sp.sqrt(5)) / 2: 1, (sp.Integer(3) + sp.sqrt(5)) / 2: 1}
checks += 2

rows = DATA["all_order_fixed_point_theorem"]["rows"]
for n, row in enumerate(rows, start=1):
    power = A**n
    signed = int((power - I).det())
    fixed = abs(signed)
    assert row["A_power"] == [list(map(int, power.row(index))) for index in range(2)]
    assert row["trace_A_power"] == int(sp.trace(power))
    assert row["signed_det_A_power_minus_I"] == signed
    assert row["fixed_point_count"] == fixed
    assert fixed == row["trace_A_power"] - 2
    assert signed == -fixed
    primitive = sum(
        int(sp.mobius(n // divisor)) * DATA["all_order_fixed_point_theorem"]["fixed_point_counts_n_1_to_12"][divisor - 1]
        for divisor in sp.divisors(n)
    )
    assert primitive == row["primitive_point_count"]
    assert primitive // n == row["primitive_orbit_count"]
    checks += 8

zeta = (1 - z) ** 2 / (1 - 3 * z + z**2)
series = sp.series(zeta, z, 0, 13).removeO().expand()
coefficients = [int(series.coeff(z, degree)) for degree in range(13)]
assert coefficients == DATA["artin_mazur_zeta"]["series_coefficients_z_0_to_12"]
checks += 13
log_series = sp.series(sp.log(zeta), z, 0, 13).removeO().expand()
for n, fixed in enumerate(DATA["all_order_fixed_point_theorem"]["fixed_point_counts_n_1_to_12"], start=1):
    assert sp.simplify(log_series.coeff(z, n) - sp.Rational(fixed, n)) == 0
    checks += 1

# Fourier action and the explicit noncompactness witness.
seen_sources: set[tuple[int, int]] = set()
seen_images: set[tuple[int, int]] = set()
for row in DATA["koopman_obstruction"]["orthonormal_test_sources_and_images"]:
    source = sp.Matrix(row["source_k"])
    image = A.T * source
    assert list(map(int, image)) == row["image_A_transpose_k"]
    seen_sources.add(tuple(row["source_k"]))
    seen_images.add(tuple(row["image_A_transpose_k"]))
    checks += 2
assert len(seen_sources) == 12 and len(seen_images) == 12
checks += 2
assert DATA["koopman_obstruction"]["unitary"] is True
assert DATA["koopman_obstruction"]["noncompact"] is True
assert DATA["koopman_obstruction"]["trace_class"] is False
assert DATA["koopman_obstruction"]["ordinary_trace_class_fredholm_determinant_defined"] is False
checks += 4

# Parabolic control: B^n-I is singular for every positive n.
B = sp.Matrix([[1, 1], [0, 1]])
for n in range(1, 13):
    assert B**n == sp.Matrix([[1, n], [0, 1]])
    assert (B**n - I).det() == 0
    checks += 2

# Independently enumerate the cyclic Fourier-aliasing controls.
for control in DATA["negative_controls"]["wraparound_fourier_aliasing"]["rows"]:
    n = control["iterate_n"]
    power = A**n
    recovered = []
    for modulus in control["moduli_2_to_12"]:
        count = 0
        for first in range(modulus):
            for second in range(modulus):
                vector = (power - I) * sp.Matrix([first, second])
                count += int(all(int(entry) % modulus == 0 for entry in vector))
        recovered.append(count)
    assert recovered == control["wraparound_traces"]
    assert len(set(recovered)) > 1
    checks += len(recovered) + 1

route = DATA["route_a_verdict"]
assert route["canonical_tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
assert route["overall"] == "ROUTE_A_EXPLORATORY"
assert route["route_b_invocation_allowed"] is False
checks += 6
nonclaims = " | ".join(DATA["nonclaims"])
assert "target divisor match" in nonclaims
assert "ordinary operator trace" in nonclaims
assert "Euler factors" in nonclaims
assert "Route-B authorization" in nonclaims
checks += 4

print("C125_SYMPY_PASS", checks, "exact symbolic checks")
