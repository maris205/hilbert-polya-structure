# Bounded exact computation receipts

2026-09-06. All calculations in this file were executed in the current
round2 lane. No old sealed census was rerun. Current scout calculations
were limited to the bounds below and do not prove universal statements.

## Retained proof-supporting probe

Command:

    python /root/autodl-tmp/hilbert-polya-structure/henon_dynamics/continuation_c404_c408_round2/wild_dynamics/exact_probe.py

Result: exit code 0, python-flint 0.9.0. Complete printed JSON was saved as
`EXACT_RESULTS.json` without altering numerical entries. Five H-cases,
nineteen periods. Largest fixed polynomial degree in this saved run: 4096.

The probe independently isolates exact-period squarefree factors by gcd
with earlier exact-period factors. It computes weights from their actual
first-return multiplicities, not from the asserted W_n formula. It also
reconstructs every fixed polynomial and checks all previous factors have
the predicted new multiplicity at return times. These are integer/prime-
field exact checks and not floating-point root approximations.

The p=3,H=1+x+x²,n=2 double-weight factor was separately extracted. Its
printed squarefree factorization was

    (1, [(x,4), (x²+2x+2,6),
         (x¹¹+2x⁹+x⁸+2x⁷+x⁵+x⁴+2x³+2x+2,3)])

and gcd(x²+2x+2,f−x)=1. This exact output supplies the counterexample in
the proof package, not a fitted or inferred cycle structure.

## Exploratory simple-H bound

Before writing the full-family theorem, direct squarefree computations for
f=x+x^{p+1} used p=3,n≤9; p=5,n≤6; p=7,n≤5; a p=2 boundary comparison
used n≤12. The largest polynomial degree among those bounds was 531441.
These transient outputs were not used to claim any all-period theorem.
The p=2 map is Chebyshev D3 and is outside the odd-characteristic theorem.
No further census expansion is planned.

## Separate dx-preserving candidate C

The following exact probe was executed (exit code 0). It is reproduced
here so the rejected extension has a bounded reproducible receipt without
adding more experiments to the retained weighted probe.

```python
from flint import nmod_poly
for p in [3, 5]:
    x = nmod_poly([0, 1], p)
    f = x + x**(2*p)
    g = x
    for n in range(1, p+1):
        g = f.compose(g)
        if n in [1, 2, p]:
            fixed = g-x
            sf = fixed.factor_squarefree()[1]
            ord0 = next(i for i in range(1, fixed.degree()+1) if fixed[i])
            print(p, n, ord0, [(h.degree(), int(e)) for h, e in sf])
```

Output:

    3 1 6 [(1,6)]
    3 2 6 [(1,6),(10,3)]
    3 3 36 [(1,36),(60,3)]
    5 1 10 [(1,10)]
    5 2 10 [(1,10),(18,5)]
    5 5 1000 [(1,1000),(19800,5)]

This rejects a direct transplant of the dx/x local-growth rule to
dx-preserving maps. No formula for subsequent p-powers is asserted.

## Operation scope

No GPU work, external model/API calls, third-party manuscript uploads,
PDF generation, old-directory writes, Git writes, or Route-A evaluator
invocations were performed by this lane. JSON syntax/hash checks are
non-mutating integrity checks, not additional mathematical experiments.
