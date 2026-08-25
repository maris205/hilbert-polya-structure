# C140 source audit

## Source class

C140 is a constructed exact symbolic-dynamical source, not a fit to external
data.  The alphabet is `{0,1}` and admissibility is the mod-three zero-gap
rule.  The all-zero point is explicitly included.  The label roof is frozen as
`tau(1)=1`, `tau(0)=sqrt(2)`.

## Frozen conventions

- Residue states are `0,1,2`, recording the zero count modulo three after the
  most recent `1`.
- Labeled edges are `0--1-->0`, `0--0-->1`, `1--0-->2`, `2--0-->0`.
- `u` marks label `1`; `v` marks label `0`.
- `D_cov=det(I-B)` belongs to the cover.  `D_140=Z_140^{-1}` belongs to
  intrinsic label periodic points after the exceptional-orbit correction.
- Every intrinsic label point is counted once; three cover lifts of the
  all-zero point are never called three label points.
- Periods 1–15 are replay sentinels only.

## Independence

The producer enumerates intrinsic label points and computes the cover trace.
The standard-library checker imports no producer code and reconstructs both
objects independently.  SymPy derives the determinant, rational correction,
and fifteen logarithmic coefficients.  Byte replay and hostile repaired-hash
tests provide separate integrity controls.

## Firewall

No prime or zero table, arithmetic/local factor, Euler factor, root number,
automorphy claim, target divisor, Hilbert--Polya operator, or Route-B input is
used.  Literal scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
