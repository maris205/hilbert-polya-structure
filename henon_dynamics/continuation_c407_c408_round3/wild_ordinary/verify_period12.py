"""Exact local certificate for a proposed first-return counterexample."""
import json
from flint import fmpz_mod_poly_ctx, fq_default_ctx

p = 3
base = fmpz_mod_poly_ctx(p)
modulus = base([2, 0, 0, 2, 1])
ctx = fq_default_ctx(modulus=modulus, var="a")
a = ctx([0, 1])
zero, one = ctx(0), ctx(1)
cutoff = 19


def multiply(left, right):
    output = [ctx(0) for _ in range(cutoff)]
    for i, x in enumerate(left):
        for j, y in enumerate(right[:cutoff-i]):
            output[i+j] += x*y
    return output


def pth(poly):
    out = [ctx(0) for _ in range(cutoff)]
    for i in range((cutoff-1)//p + 1):
        out[p*i] = poly[i]**p
    return out


orbit = []
current = a
while current not in orbit:
    orbit.append(current)
    current += current**4
assert current == a and len(orbit) == 12
assert all(x != zero and x != -one for x in orbit)
qcycle = [one]
for x in orbit:
    qcycle = [zero]+qcycle
    for i in range(len(qcycle)-1):
        qcycle[i] -= x*qcycle[i+1]
assert all(x**3 == x for x in qcycle)
assert all(x != a for x in orbit[1:])

# Direct translated coordinate, without using the orbit-sum criterion.
jet = [zero, one] + [zero for _ in range(cutoff-2)]
for point in orbit:
    jp = pth(jet)
    jpp1 = multiply(jp, jet)
    jet = [(one+point**p)*jet[i]+point*jp[i]+jpp1[i] for i in range(cutoff)]
jet[1] -= one
first = next(i for i,x in enumerate(jet) if x != zero)
assert first > 3

output = {"p":p, "modulus_coefficients_ascending":[2,0,0,2,1],
          "period":len(orbit), "orbit":[str(x) for x in orbit],
          "cycle_polynomial_coefficients_ascending":[str(x) for x in qcycle],
          "sum":[str(sum((x/(one+x) for x in orbit),zero))],
          "jet_cutoff":cutoff, "first_return_multiplicity":first,
          "jet_nonzero_coefficients":{i:str(x) for i,x in enumerate(jet) if x != zero}}
print(json.dumps(output, ensure_ascii=False, indent=2))
