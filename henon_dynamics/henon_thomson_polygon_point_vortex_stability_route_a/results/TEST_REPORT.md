# Test report

All commands were run with `PYTHONDONTWRITEBYTECODE=1` from the package root.

```text
C284_PRODUCER_PASS
C284 independent raw-Hessian checker: PASS (65655 assertions; producer-independent 2N x 2N reconstruction for N=3..64)
C284_SYMPY_PASS (4585 exact identities; raw Cartesian Hessians and symmetry slices for N=3,4,6 plus coefficient-counted N=3..64 root sums)
C284 double fresh-path byte replay: PASS (885870 bytes on both independent paths)
C284 hostile mutation audit: PASS 76/76 (repaired-hash schema/semantic attacks plus stale-hash, raw duplicate-key, and nonstandard-constant controls)
```

The checker imports no producer module.  For every `N=3..64` it constructs the
raw `2N x 2N` Cartesian augmented Hessian, checks the rotating equilibrium and
matrix symmetry, derives local radial--tangential blocks, verifies full cyclic
block structure, performs the complex DFT, applies the Hessian and Hamiltonian
linearization to explicit rotation/scale/translation/centered-complement
vectors, and compares every exact row contract with the evidence ledger.

The SymPy program separately differentiates exact Cartesian pair potentials
for `N=3,4,6`, reconstructs their DFT blocks and slice actions, and checks the
complete root-of-unity identity for all evidence sizes by coefficient counting.
Replay writes to two unrelated nested temporary paths.  Seventy-three
schema/semantic/order/duplicate-drop attacks receive repaired payload hashes;
stale-hash, raw duplicate-key, and raw nonstandard-constant controls complete
the 76 specimens.  Rejection therefore cannot be attributed merely to
integrity metadata.

Coverage includes exact top/nested/row schemas and types, the full headline,
all `reduced_role` values, exact `N=7` singular cells, first `N=8` hyperbolic
cells, symmetry directions, circulation/radius scaling, collision and
zero-circulation faces, scope flags, Route-A tuple, source-owner fields,
same-size duplicate/drop-replace attacks, and hash integrity.
