# HCS-C293 — magnetic Grushin cylinder

This package proves a complete spectral atlas for the Friedrichs-form
realization of

`G_alpha=-partial_x^2+x^2(-i partial_theta+alpha)^2`

on `L2(R x S1)`.  Noninteger flux has compact resolvent and exact
Fourier–Hermite levels.  Integer flux has exactly one resonant angular
channel, whose free-line absolutely continuous spectrum has a.e.
multiplicity two, coexisting with embedded positive-integer oscillator
eigenvalues; the singular-continuous part is empty.  The nonresonant sector
has exact heat, multiplicity, source-zeta, and logarithmic Weyl formulas.

Both the evidence JSON and Route-A evaluation YAML have duplicate-rejecting
exact nested schemas.  The parsed evaluation is also frozen by a canonical
semantic SHA-256.

The strict tuple is
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_NATURAL_QUANTIZATION)`,
but the overall verdict is `ROUTE_A_REJECTED`, Route B is disabled, and all
forbidden claim flags are false under `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python -B code/c293_grushin_producer.py
python -B code/c293_grushin_checker.py
python -B code/c293_grushin_sympy_crosscheck.py
python -B code/c293_grushin_replay.py
python -B code/c293_grushin_mutation.py
python -B code/c293_release_manifest.py
```
