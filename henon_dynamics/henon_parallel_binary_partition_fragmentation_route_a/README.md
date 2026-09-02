# C301 — parallel binary partition fragmentation

This package closes one complete paper-sized result for candidate `HCS-C301`
and obstruction `HEN-O285`.  It studies a synchronous Markov chain on
**labelled** set partitions: at every integer time, each label receives a fresh
fair bit and every existing block is refined by its two nonempty bit fibres.

The main advance is an all-parameter theorem, not a slice of a larger paper:

- the exact kernel from every starting partition at every time;
- the complete partition and block-count distributions;
- the exact absorption-time CDF, mass, and mean;
- the characteristic polynomial, source spectral determinant, traces, and a
  proved squarefree annihilator;
- the birthday critical limit with the dyadic lattice qualification.

The final manuscript is `paper/main.pdf`.  Three materially different review
states are archived as `main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf`; the final PDF is byte-identical to round 2.

## Reproduce

Run from this directory:

```bash
python3 code/c301_fragmentation_producer.py
python3 code/c301_fragmentation_checker.py
python3 code/c301_fragmentation_sympy_crosscheck.py
python3 code/c301_fragmentation_replay.py
python3 code/c301_fragmentation_mutation.py
python3 code/c301_release_manifest.py
```

The release command regenerates evidence, rebuilds every PDF twice under the
fixed epoch, checks fonts and warnings, validates the strict Route-A YAML, and
enforces the exact 27-payload/28-physical-file closure.

## Scope

The frozen literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.  The honest Route-A tuple
is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` and the verdict is
`ROUTE_A_REJECTED`.  The finite Markov determinant is never identified with an
arithmetic zeta or L-function, and Route B is not invoked.
