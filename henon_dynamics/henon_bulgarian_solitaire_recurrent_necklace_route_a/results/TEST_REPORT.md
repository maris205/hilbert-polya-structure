# C190 test report

## Exact executable checks

- Producer: PASS — 40 systems, 757 recurrent words, 114 cycles, 248 fixed
  rows, 117 period rows, and 248 spectral rows.
- Independent checker: PASS — 658,664 assertions; no producer import.
- Direct full-partition oracle: PASS — all 215,307 partitions for
  `1<=N<=40`; 757 direct recurrent states and 114 direct cycles.
- SymPy reconstruction: PASS — 2,210 checks.
- Canonical replay: PASS — 772,424 bytes and exact SHA-256 match.
- Mutation suite: PASS — 118 repaired-hash plus one stale-hash rejection.

## Independence and coverage

The producer generates fixed-weight words using combinations.  The checker
instead generates all Boolean words by Cartesian product and all integer
partitions by a descending recursive generator.  It constructs the actual
Bulgarian successor of every partition and discovers recurrent nodes from the
full functional graph.  It verifies every word/partition mapping, rotation,
phase reflection, fixed iterate, direct cycle, Möbius period, zeta factor,
determinant factor, root multiplicity, source field, Route-A qualification,
scope flag, and nonclaim.

The SymPy path independently checks partition numbers, binomials, Möbius
inversion, determinant degree, characteristic degree, trace identities,
Burnside cycle totals, triangular specializations, and explicit N=8 Koopman
and reflection matrices.

The finite oracle does not prove Brandt's all-`N` theorem.  Aggregate
transient counts certify the algebraic zero multiplicity; complete transient
trees, hitting times, and nilpotent Jordan sizes remain outside scope.
