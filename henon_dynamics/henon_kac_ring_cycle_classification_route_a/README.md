# HCS-C170: all-marker Kac-ring cycle classification

This package proves, for every \(N\ge1\) and every marker word, the exact cycle classification controlled by \(\eta=\prod_j\varepsilon_j\), all-time fixed counts, zeta, Koopman determinant and roots, gauge/unfolded reversor, antiunitary, and self-adjoint boundary.

The Route-A v0.2 verdict is `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`. The primitive cycles are exact but belong to a finite reducible kinetic toy model. Route B is false.

Run:

```bash
python code/c170_kac_ring_producer.py
python code/c170_kac_ring_checker.py
python code/c170_sympy_crosscheck.py
python code/c170_replay.py
python code/c170_mutation.py
python code/c170_release_manifest.py
```

The final manuscript is `paper/main.pdf`; finite rows are regression sentinels only.
