# C168 exact-validation plan

## Claim-bearing gates

1. Reconstruct the one-site DFT gate, characteristic polynomial, four
   distinct roots, rank, moduli, normalized phases, and non-torsion ratio.
2. Prove the tensor secular product, degree `3^k`, and generalized-zero
   dimension `4^k-3^k` for every `k`.
3. Derive the three-step Fourier law and prove strict contraction for each
   fixed nonzero mode by exact algebra.
4. Derive the centered log-modulus mean/variance and exact mixed transform.
5. Reconstruct the hole-zero finite-group control and its TV bound.
6. Verify the hole-reflection and antiunitary/projector-order matrix
   identities without converting them into a self-adjoint claim.

## Deterministic sentinels

- Spectral ledgers: `1<=k<=24`.
- Exact `Q(i/sqrt(2))` Fourier recurrence: `1<=m<=24`.
- Hole-zero residue ledgers: `1<=k<=24`.
- Decimal columns: display-only checks derived from exact rationals.

## Validation separation

- Producer serializes evidence.
- Checker independently recreates exact arithmetic and enforces complete
  nested-key closure.
- SymPy independently reconstructs the matrices, tensor rank, recurrences,
  moments, finite-group control, and antiunitary identities.
- Replay compares bytes.
- Semantic mutations repair the content hash before invoking the checker;
  a separate stale-hash attack tests content addressing.

## Release gates

Compile the bilingual manuscript twice in fresh fixed-epoch directories,
require byte identity, two A4 pages, embedded fonts, clean warnings/boxes,
and visual inspection.  Close exactly 27 payload hashes in the self-excluded
manifest.  Finite tests never substitute for the written all-parameter
proofs.
