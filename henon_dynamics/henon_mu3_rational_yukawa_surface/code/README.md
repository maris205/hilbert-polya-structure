# HCS-C55 exact replay

This directory contains the finite-algebra certificate lane for C55.  It does
not claim that a computer algebra replay proves Hilbert/Rim algebraization, a
relative VHS, an honest Calabi--Yau threefold, or a motivic realization.

`c55_producer.py` constructs the exact certificate over
`Q(rho)/(rho^2+rho+1)`.  Its main controls are the 83-dimensional
`R_(1,0)` tangent-operator quotient and multiplication-by-`y` isomorphism,
the four rational invariant directions, the corrected semilinear Cayley
descent `D(z)=rho*z`, 20 direct specialized cube reductions, the primitive
rational cubic, and the length-16 Jacobian quotient.

`c55_checker.py` independently rebuilds the finite group and quotient
arithmetic, uses Singular's distinct `Wp` order for the 20 raw traces, checks
all 13 named gates, and closes all 1,589 certificate scalar leaves into 292
central semantic, 1,296 derived, and one chronology-only leaf.

Run a read-only replay with:

```bash
code/run_c55.sh
```

Refreshing results is deliberately coupled to the persistent scoped
code/results manifest:

```bash
code/run_c55.sh --refresh-results --refresh-manifest
```

The grouped promotion of certificate, independent check, and scoped manifest
is rollback-safe.  `CODE_RESULTS_HASHES.sha256` is the persistent scoped
identity, and the default runner verifies that identity.  The already-current
`ARTIFACT_HASHES.sha256` full manifest is verified separately with
`c55_hash_manifest.py --full-only`; this does not overwrite the historical
scoped identity.
