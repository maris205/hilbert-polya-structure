# HCS-C269 — finite-field Chebyshev functional graphs

This package proves a parameter-uniform functional-graph theorem for the non-normalized Chebyshev/Dickson first-kind map

\[
T_d(z+z^{-1})=z^d+z^{-d}
\]

on every finite field `F_q`, for every prime power `q` and every integer `d>=1`.  It is not another abstract power-map census.  The new owner is the ramified inversion quotient of the two cyclic covers of orders `q-1` and `q+1`, including their one- or two-point branch gluing.  That labeled quotient determines every regular tree and every exceptional folded branch tree.  Closed formulas then give all fixed and primitive counts, finite source zeta, global tail layers, image ranks, every zero Jordan-block size, and the full-function Koopman characteristic polynomial.  `d=0` is retained as a separate constant-map boundary.

The theorem remains valid in characteristic two.  Exact evidence crosses 11 field models and degrees `0,...,10`: 121 maps, 1,914 directly followed vertices, 77 nonprime-field cases, and 33 characteristic-two cases.  The independent checker imports no producer; it also proves every stored modulus monic and irreducible over `GF(p)` and requires one common model for all degrees at fixed `q`.

Frozen provenance:

- source commit: `9cb7483e97ef82fdc06d45ecb3043f183ce22391`
- fixed epoch: `1788134400`
- evaluator: Route-A v0.2.0, SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- verdict: `ROUTE_A_EXPLORATORY`, with `A4_FORMAL_HINT`; Route B disabled

The finite-field parameters give a weak intrinsic arithmetic relation, but no rational-prime orbit dictionary or logarithmic prime clock.  The finite composition matrix is only a formal operator hint: it is generally nonnormal and no self-adjoint realization is constructed.  No arithmetic local datum, bad Euler factor, root number, automorphy statement, target divisor, functional equation, or Hilbert–Pólya operator is claimed.  Workspace ownership is not a literature-priority claim.

## Reproduce

```bash
python3 -B code/c269_chebyshev_producer.py
python3 -B code/c269_chebyshev_checker.py
python3 -B code/c269_chebyshev_sympy_crosscheck.py
python3 -B code/c269_chebyshev_replay.py
python3 -B code/c269_chebyshev_mutation.py
python3 -B code/c269_release_manifest.py
```
