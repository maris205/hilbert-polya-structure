# HCS-C146: clean fixed circles on a Heisenberg nilmanifold

C146 freezes the standard upper-triangular Heisenberg group, its integer
lattice, and the hyperbolic horizontal matrix `A=[[2,1],[1,1]]`.  The required
integer-valued central correction is included explicitly, so the map is a
genuine lattice automorphism rather than a toral formula pasted onto a
nontrivial circle bundle.

Every iterate fixes the embedded central circle pointwise.  Consequently the
fixed set is never discrete, the ordinary isolated-orbit stability factor is
zero at every iterate, and the Lefschetz number is zero.  The transverse toral
control has exactly `|det(A^n-I)|=L_(2n)-2` isolated points.  A period-two
cocycle witness refutes the tempting but false claim that every horizontal
fixed class lifts to a fixed circle; no full nilmanifold component count is
asserted.

The release contains exact evidence through iterate 20, an independent
checker, an independent SymPy reconstruction, byte replay, hostile mutations,
a complete theorem package, two genuine internal review/fix rounds, four
retained PDFs, and a self-excluded content-addressed manifest.

The Haar-preserving map also gives a natural Koopman unitary on `L^2(N)`, but
no bridge from that operator to the singular orbit-family weights; it is only
a formal lift hint.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  Verdict:
`(A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall
`ROUTE_A_EXPLORATORY`; Route B is not authorized.
