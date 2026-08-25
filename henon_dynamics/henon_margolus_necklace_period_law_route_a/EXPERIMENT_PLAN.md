# C165 exact validation plan

The computation is a theorem sentinel and artifact audit, not the authority
for the all-parameter statements.

## Producer

1. Construct `A` and `B` independently from their pair partitions.
2. Compose the full-tick site permutation for every `1<=m<=16`.
3. Record the reversed-odd pairing and verify its cyclic intertwining.
4. Reconstruct all fixed counts for `1<=n<=m`, exact periods for every
   `d|m`, zeta and Koopman factors, and the rational concentration bound.
5. Directly enumerate all `4^m` configurations for `m<=8`.
6. Serialize canonical JSON and a payload hash excluding only the hash field.

## Independent checks

- The checker imports no producer code and reconstructs the two layers,
  composition, inverse, reflection, site cycles, necklace inversion, state
  enumeration, source zeta, determinant factors, schema, tuple, and scope.
- SymPy independently verifies the site characteristic polynomial
  `(y^m-1)^2`, reflection matrix identities, Moebius sums, trace-log
  coefficients, small Koopman characteristic polynomials, and exact bounds.
- Replay regenerates the evidence in a temporary directory and demands byte
  equality.
- The hostile suite changes 57 claim-bearing values while repairing the
  payload hash, then separately tests one stale hash.

## Release gates

- all exact-code commands pass on the released bytes;
- all 27 manifested payload paths are present with exact hashes and no extra
  release file;
- three paper stages are content-distinct and final `main.pdf` equals round 2;
- two fresh LuaLaTeX builds at `SOURCE_DATE_EPOCH=1787616000` are
  byte-identical;
- all fonts are embedded; logs contain no warning, box, reference, citation,
  or missing-glyph issue; rendered pages are visually inspected;
- auxiliary and cache files are removed.

Failure of any gate blocks release rather than weakening the theorem into a
finite observation.
