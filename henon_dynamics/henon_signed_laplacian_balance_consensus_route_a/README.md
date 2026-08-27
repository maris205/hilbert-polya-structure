# HCS-C203 — signed-Laplacian consensus and full pseudoforest expansion

C203 treats every finite disconnected static undirected simple signed graph
with positive weights.  It gives the exact kernel, projector, semigroup limit,
spectral rate, every principal minor and the full characteristic polynomial.

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
ROUTE_A_REJECTED
```

Route B is false under `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python code/c203_signed_laplacian_producer.py
python code/c203_signed_laplacian_checker.py
python code/c203_signed_laplacian_sympy_crosscheck.py
python code/c203_signed_laplacian_replay.py
python code/c203_signed_laplacian_mutation.py
python code/c203_release_manifest.py
```

The evidence contains all 760 graphs and 11,894 root sets for `n<=4`; the
final paper is `paper/main.pdf`.
