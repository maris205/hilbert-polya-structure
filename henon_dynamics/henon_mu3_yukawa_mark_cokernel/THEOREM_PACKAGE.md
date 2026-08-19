# HCS-C66 theorem package

Status: **PREFREEZE_COMPLETE_NOT_RELEASED**.

Let `S1,...,S16` be the exact C64 subgroup representatives and let
`M_ij = |(G/S_j)^(S_i)|` be the 16-by-16 restricted self-mark matrix.  The
central theorem is

```text
SNF(M) = [1, 2,2,2,2,2,2,2,2,2,2, 4,4,4, 24,144].
```

Thus the restricted mark-map cokernel is

```text
coker(M) ~= (Z/2)^10 + (Z/4)^3 + Z/24 + Z/144.
```

Its primary factors are `(Z/2)^10 + (Z/4)^3 + Z/8 + Z/16` at 2 and
`Z/3 + Z/9` at 3.  The product of the factors is
`226492416 = 2^23 * 3^3`, the C64 determinant.

The theorem concerns only the explicitly frozen 16-type submodule.  It does
not assert the Smith form of a full table of marks, a full Burnside-ring
classification, or any arithmetic/local conclusion.  The mandatory scope
literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Gates

* G0: exact C64 evidence/manifest and C65 evidence hash rebind;
* G1: 16-by-16 shape, rank, determinant, and scope checks;
* G2: independent exact Smith algorithm and complete divisibility chain;
* G3: independent library Smith cross-check and C65 compatibility;
* G4: clean replay, hostile mutations, and manuscript audit;
* G5: PDF compilation and self-excluding manifest.

The arithmetic/local gate remains outside scope.
