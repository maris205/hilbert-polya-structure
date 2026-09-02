# HCS-C308: finite Hatano--Nelson boundary/skin atlas

This package proves an all-parameter finite-chain theorem for asymmetric nearest-neighbor hopping: exact positive-OBC similarity and Chebyshev spectrum, canonical left/right modes, amplitude skin envelope versus biorthogonal density, conditioning, propagator, resolvent, PBC Fourier ellipse, and every zero-hopping face.

Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  Route A is rejected with tuple `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and Route B remains locked.  No topology, disorder, interaction, arithmetic, or Hilbert--Polya claim is made.

## Reproduce

From this directory run:

```text
python code/c308_hatano_nelson_producer.py
python code/c308_hatano_nelson_checker.py
python code/c308_hatano_nelson_sympy_crosscheck.py
python code/c308_hatano_nelson_replay.py
python code/c308_hatano_nelson_mutation.py
python code/c308_release_manifest.py
```

The final command rechecks the exact 28-file/27-payload ledger and fresh-build PDF determinism.  `python -O code/c308_hatano_nelson_checker.py` must fail explicitly.
