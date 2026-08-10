# HCS-C25 test report

**Date:** 2026-08-10
**Command:** `./code/run_c25.sh`
**Outcome:** `PASS`

The release command regenerates the producer certificate, executes the
independent checker, runs the mutation suite, and writes the artifact hash
manifest.

Producer summary:

```json
{"states":7,"state_frames":7,"fixed_fiber_edges":14,"identity_fixed_fiber_edges":6,"gamma_length":128,"gamma_positive":true,"stress_first_returns":35420,"stress_collisions":0}
```

Independent checker: eleven of eleven registered checks passed, with material
passport status `VERIFIED`.

Regression/mutation suite:

```text
Ran 14 tests
OK
```

The tests reject:

- reading the initial run as the compressed exponent 64 instead of scanning
  the actual 65-letter maximal `t` prefix;
- right-multiplied chronology;
- a transposed elementary edge and confusion of `B` with `B^T`;
- discarding the labeled state and retaining only the move word;
- a bordered section-word mutation;
- treating seven complete blocks as if they met the `3d-4=8` criterion;
- replacing the four-dimensional projective Jacobian exponent by three;
- projecting the decoder conclusion without the full-rank `H(2)`
  qualification;
- reversing the spanning-tree frame direction (`B^T S_src` in place of
  `B S_src`);
- swapping the state frames in the fixed-edge expression instead of using
  `S_dst^(-1) B_e S_src`;
- promoting the toy `ttt` central return to the AGY section branch;
- treating the finite length-22 replay as the injectivity proof or as an
  `n=13` orbit ledger.
