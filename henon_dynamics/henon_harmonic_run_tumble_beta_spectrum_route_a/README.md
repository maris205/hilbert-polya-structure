# HCS-C328: harmonic run-and-tumble beta law

This package closes the source-local stationary law, all polynomial moments, the full stationary two-by-two correlation matrix, and every finite polynomial filter of the one-dimensional harmonic run-and-tumble process
`dx=(v sigma-mu x)dt`, with symmetric flips at rate `lambda` and `mu,v,lambda>0`.

The filtered resonance theorem distinguishes the cases missed by a diagonal-only calculation: when `2lambda/mu=k` is a positive integer and `v>0`, odd `k` gives size-two Jordan blocks, while even `k` is semisimple because the repeated diagonal entries lie in different parity chains.  The claim is not a full `L2` spectral classification.

The finite receipt has 12 parameter rows, 108 moment rows, 60 correlation rows, 216 spectral cells, and 33 resonances.  The independent checker performs 2,226 checks, SymPy closes 61 identities, replay is byte exact, and 66 hostile mutations are rejected.

The strict Route-A tuple is all FAIL, the overall verdict is `ROUTE_A_REJECTED`, and Route B remains locked under `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python -B code/c328_run_tumble_producer.py
python -B code/c328_run_tumble_checker.py
python -B code/c328_run_tumble_sympy_crosscheck.py
python -B code/c328_run_tumble_replay.py
python -B code/c328_run_tumble_mutation.py
python -B code/c328_release_manifest.py
```

The readable artifact is `paper/main.pdf`; `C328_RELEASE_MANIFEST.json` is the release ledger.
