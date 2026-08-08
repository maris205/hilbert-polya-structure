# HCS-C20 exact code

This directory contains a self-contained producer, a deliberately
non-importing independent checker, and a unittest suite for the candidate
HCS-C20 period-seven dihedral cover.

Run from this directory:

```bash
python c20_producer.py
python c20_independent_check.py
python -m unittest -v test_c20.py
```

`c20_producer.py` reconstructs the frozen septic and computes the generic
chronological-neighbor subresultants and norm exactly over `Q(sigma)`.  It
also counts the genus-two quotient over `F_p` and `F_{p^2}` without a finite
field package, counts the septic plane model over `F_{p^r}` for `r=1,2,3`,
and evaluates the cubic-field norms symbolically.  The plane counts use the
`galois` and `numpy` packages and are converted to normalization counts by
the recorded seven-infinity-branch and residual-node correction.

`c20_independent_check.py` does not import the producer, C19 code, or stored
C19 artifacts.  It also imports neither `galois` nor `numpy`: for every
`(p,r)` it constructs `F_p[t]/(m_r)` using its own base-`p` representation,
checks each degree-two or degree-three modulus irreducible by the no-root
criterion, builds exact field-operation tables, and independently enumerates
the plane points.  It repeats the remaining mathematics from locally stated
formulas and binds its report to the exact certificate bytes by SHA-256.

At exactly `p=5,11,13`, the producer and checker certify good reduction of
`B`, `C`, and `E`.  The certificate includes the irreducible septic-fiber
witness, residual-node gcd, seven separated infinity branches, exclusion of
full vertical `C7` inertia, purity, the tame reflection quotient, and the
plane-special-fiber birational comparison.  Consequently the displayed
`L_C` factors and `L_E=L_B L_C^2` are certified Hasse--Weil local factors at
those three primes.  No good-reduction assertion is made for other primes.

The group notation distinguishes edge reversal `R(x,y)=(y,x)` from the
scalar-fixing reflection `J=R*tau=(x,a-x^2-y)`; the scalar curve is
`C=E/<J>`.
