# HCS-C147: primitive orbit families in the square billiard

C147 freezes the unit square billiard and unfolds it to the doubled square
torus.  Each ordered positive coprime pair `(m,n)` is an absolute-direction
representative with four signed unfolded sectors, or two after time reversal;
coordinate swap remains distinct.  It gives representative displacement
`(2m,2n)`, length
`2 sqrt(m^2+n^2)`, and a clean one-parameter family.  After removing the
finitely many vertex-hitting offsets, the transverse circle decomposes into
open cylinders.  These cylinders have positive transverse length but zero
measure in the full energy shell because the direction itself is fixed.

The exact `m,n<=40` ledger has 979 positive primitive directions and agrees
with the Möbius count.  The first length collision not explained by coordinate
swap is `(1,8)` versus `(4,7)`, both with square 65.  Replacing the square by a
rectangle of height `2^(1/4)` removes every distinct positive-direction length
collision by independence of `1` and `sqrt(2)`.

The full reduced Poincare linearization has eigenvalue one tangent to every
fixed-family curve, so the ordinary isolated-orbit denominator is singular.
The intrinsic positive Dirichlet half-wave supplies a unitary, clock-matched,
time-reversal-symmetric quantization but no clean-family trace or target match.
The release contains
proofs, exact evidence, independent checker and SymPy paths, byte replay,
hostile mutations, two internal review/fix rounds, four retained PDFs, and a
self-excluded manifest.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  Verdict:
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, overall
`ROUTE_A_EXPLORATORY`; Route B is not authorized.
