# Independent Stage-2 audit: affine divisibility Toeplitz factors

## Verdict

`STAGE2_CLEAN`

This is a theorem/proof/validation verdict for the frozen package
`/tmp/p50_toeplitz_stage2`.  It does not authorize a manuscript, numbering,
installation, priority claim, or publication action.

## Frozen-byte closure

- Raw `SHA256SUMS.txt` SHA-256:
  `c070bd76d8a28e1b918fa040d9346db32776f238e7081d8c3504648b137a583e`.
- All 13 self-excluding rows passed `sha256sum -c` and the package verifier.
- An auditor-owned output directory reproduced all three evidence files
  byte-for-byte; their SHA-256 values are `620c53d7...`, `b6e7f69c...`, and
  `99ee0fb2...`.
- The frozen package retained zero cache, bytecode, symlink, or nonregular
  entries before and after the replay.

## Independent finite/exact checks

Two root-side checkers import no candidate module.

The skeleton/high-center/partition checker (script SHA
`7b7e207d4b90ce0e7f1adb9dd9a9ba2320272cf8292c17abdb619bf74a1bc5f1`;
result SHA
`7eec5a0e4eee1a35e79645713c79ca3c88cb86dd39d5ca8c18996453e3dfdcc0`)
passed 984,576 skeleton-position checks, 3,744 high-center checks, and 9,874
partition checks across 728 directives, including 2,216 admissible partitions.

The prime/composite constructive checker (script SHA
`31d8858be6b2ea36f52cb1cf65046c82b8371527be9e66f935f251dfab307c2b`;
result SHA
`bb956913938c7653dec8c5d68077176b2bfcd6d83788b63993767c1d5e9284bd`)
rejected 200,988 smaller prime-base candidate periods and checked 426,088
composite-base position shifts.  These bounded checks are controls only; the
written proof carries the infinite quantifiers.

## Proof audit

The proof closes the following without importing the finite census:

1. `Per_{p^N}` is exactly the complement of the one residue
   `r_N+p^N Z`; both `r_N` and `r_{N+1}` occur in every alleged hole
   progression, so no hole point is accidentally periodic.
2. The one-hole skeleton gives essential `p^N` periods, normal
   simple-Toeplitz recursion, and aperiodicity for every integer `p>=3`.
3. For prime `p`, every smaller common period is killed at the high center
   indexed by its exact `p`-exponent.  For composite `p`,
   `ell*p^N` preserves every position of `B_N` for every integer translate,
   including its exponent-`N` position.  Hence constructiveness is iff prime.
4. The high-center identity never treats a composite-base quotient as a
   unit.  CHL supplies an arbitrary radius, the off-center window freezes,
   periodic directive indices extend the relation to every letter, and orbit
   density extends equality to the full subshift.
5. Exact target support makes the induced letter map both surjective and
   unique.  Admissible kernels are exactly independent-set partitions of the
   cyclic adjacency graph; refinement has the stated arrow direction, and
   the graphical-Stirling/chromatic formulas count target classes rather
   than labeled maps.

Cross-base and nonpointed maps remain nonclaims, as required.

## Source boundary

The bounded source verdict is supported but deliberately not absolute.
Downarowicz--Kwiatkowski--Lacroix (1995), Theorem 1 already owns the general
same-period, over-zero aligned-symbol criterion.  The residual here is the
high-center collapse of every such map in this explicit affine family to a
unique letter quotient and its concrete partition poset.  Hosseini--Yassawi
owns the constructive terminology and the pure-power cross-base obstruction;
the package contributes the exact prime/composite status of this family.
No priority wording is licensed.

No authority, Git, README, mirror, manuscript, figure, seal, or installation
path was written during this audit.
