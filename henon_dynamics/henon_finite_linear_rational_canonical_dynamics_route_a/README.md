# HCS-C204: finite linear dynamics in rational canonical form

This package gives an all-parameter theorem for the functional graph of every
linear endomorphism `A` of a finite-dimensional vector space over `F_q`.  From
the invariant factors it recovers every fixed-point count, the periodic
subspace, the maximal preperiod, exact-period points and cycles, the
Artin--Mazur zeta function, and the characteristic polynomial of composition
on the full function space.  Eight exhaustive finite controls include
nilpotent, inseparable, nonsemisimple, multiple-block, and genuine GF(4)
arithmetic.

Reproduce with:

```bash
python3 code/c204_finite_linear_producer.py
python3 code/c204_finite_linear_checker.py
python3 code/c204_finite_linear_sympy_crosscheck.py
python3 code/c204_finite_linear_replay.py
python3 code/c204_finite_linear_mutation.py
python3 code/c204_release_manifest.py
```

The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  Finite-field arithmetic is not
reported as target local arithmetic.  The exact route record is
`overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`.
