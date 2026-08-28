# P24 Stage-1 research spine through Round 7

Manuscript status: **NOT STARTED**.  This document freezes the paper-facing
argument created by the research rounds; it is not an ARS Stage-2 draft.

## Working contribution

The paper studies whether complex holonomy in a torsion-free level-`(3)`
Gaussian Bianchi geodesic flow supplies arithmetic information beyond generic
three-dimensional hyperbolic dynamics.  The contribution is currently a
control architecture rather than an arithmetic correspondence:

1. an exact level-`(3)` torsion-freeness lemma and a finite exact Bianchi
   generator-word ledger (Round 2);
2. an exact rank-4 Schottky control exposing the danger of a
   geometry-mismatched infinite-volume comparison (Round 3);
3. a source-proved finite-volume, one-cusped, non-arithmetic `5_2=m015`
   control with a replayable complex-length prefix (Round 4);
4. an exact common marked-word census and a pre-frozen phase-sensitive
   comparison that closes the enumeration-type mismatch while identifying
   marked-generator-count/presentation as the remaining confound (Round 5);
5. a 25-marking-per-system elementary-Nielsen audit that stops the current
   phase statistic as marking-sensitive (Round 6).

The Round-4 advance is the first control in this project that simultaneously
matches hyperbolic dimension, finite volume, cusp presence, manifold status,
geodesic-flow clock, and complex-length orbit type while removing arithmeticity.

## Source-bound control proposition

**Proposition (established background, not a novelty claim).**  The complement
`Y=S^3\5_2` is an orientable torsion-free finite-volume hyperbolic 3-manifold
with one complete torus cusp, and its holonomy lattice is non-arithmetic.

**Proof ownership.**  HIKMOT Theorem 5.1 proves finite-volume hyperbolicity for
`m015`; the pinned SnapPy `True` isometry result rigorously binds `5_2` to
`m015`; the one-component complement supplies one cusp; and Reid's arithmetic
knot-complement classification makes every knot complement other than the
figure-eight non-arithmetic.  Exact links and limitations are recorded in
[`../notes/round4_source_audit.md`](../notes/round4_source_audit.md).

## Computational result available for a Results section

At real-length cutoff `3.05`, pinned SnapPy 3.3.2 returns 18 complex-length
groups representing 31 primitive geodesic classes by group multiplicity.  A
second implementation independently reproduces the first 9 classes across 6
groups, with identical multiplicities and maximum complex-length discrepancy
`2.2944137070481165e-31`.  The reported fields include complex length,
holonomy angle, orientation/parity, representative word and PSL trace square.

Epistemic status: **high-precision numerical observation**.  It is not a
Sage-interval certificate, and it does not establish full length-spectrum
completeness beyond the frozen software/cutoff contract.

## Round-5 methods result available for Methods and Results

The same executable rule now enumerates freely and cyclically reduced marked
words through length 5 on both systems, takes the canonical representative
under rotation and inversion, proves symbolic primitivity by the shortest word
root, and records the exact marked-orbit multiplicity.  This produces 2,074
candidate owners and 51 control owners.  Exact candidate evaluation gives
1,940 loxodromic, 132 parabolic, and two identity rows; the 212-bit control
evaluation gives 48 loxodromic and three parabolic rows.

The complex phase/length moment and its 64 target-free permutations were
frozen before execution.  On the 1,932 and 39 primitive loxodromic rows, the
standardized values are `-1.74684253916` and `-0.811352306226`; the absolute
contrast is `0.935490232934`.  Both observed magnitudes fall below their own
permutation means.  No inferential threshold was frozen.

Epistemic status: symbolic canonicalization, roots, multiplicities, and
candidate matrix checks are exact; control holonomies and phase statistics are
non-interval numerical observations.  The common **algorithm** does not remove
the marked-count-4/alphabet-8 versus marked-count-2/alphabet-4 presentation confound and does
not produce a complete metric spectrum.

## Round-6 decision result

Both systems now use four marked generators under identity plus all 24
elementary right Nielsen moves.  Candidate standardized phase width is
`0.916300044002`; the explicitly redundant stabilized control width is
`16.9152926064`.  The latter violates the frozen exploratory condition, so the
present statistic cannot justify a metric Bianchi prefix.

## Round-7 theorem result available for Theory and Results

For every level-`(3)` matrix `gamma=I+3A` in `SL_2(Z[i])`, exact determinant
expansion proves

```text
tr(gamma)-2=-9 det(A),
D9(gamma)=(tr(gamma)^2-4)/9 in Z[i].
```

This normalized trace discriminant is invariant under conjugacy and inversion.
If `S_0=1`, `S_1=t`, and `S_n=tS_(n-1)-S_(n-2)`, Cayley--Hamilton further gives

```text
D9(gamma^r)=D9(gamma) S_(r-1)(tr(gamma))^2.
```

The deterministic finite audit checks these identities on all 11,481 frozen
exact matrices and repetitions `r=1,...,5`.  It finds 145 distinct `D9` values,
leaving 11,336 rows beyond first occurrences.  An exact same-`D9` pair is
separated even after the unoriented owner quotient by the invariant
`((gamma-I)/3) mod 3` up to sign: this residue is fixed by `Gamma((3))`
conjugacy and negated by inversion.  Thus Round 7 supplies a genuine
source-derived arithmetic invariant and, simultaneously, a proof that `D9`
is not an injective orbit owner.  It does not resurrect the Round-6 phase
statistic or create a determinant/zero experiment.

## Central falsification logic

The decisive comparison is not “Bianchi versus any chaotic flow.”  Its first
marked-word implementation is now executed as:

```text
arithmetic finite-volume cusped H^3 flow
versus
non-arithmetic finite-volume cusped H^3 flow,
under one enumeration rule and one predeclared statistic,
followed by an explicit marking/presentation sensitivity gate.
```

If a marking-stable Bianchi holonomy signal persists with comparable strength
on `5_2`, the
current holonomy mechanism is generic to cusped hyperbolic 3-geometry and must
stop as an arithmetic explanation.  If a stable separation survives, it only
licenses a sharper arithmetic-structure question; it does not create an
orbit-to-prime-ideal map.  Round 5 cannot choose either branch because the
Round 6 resolves this branch negatively for the current statistic.  A new
positive branch needs a different source-derived invariant under a new freeze
or an intrinsic orbit-to-prime-ideal owner theorem.

## Claim firewall

- **Allowed:** the existence and non-arithmeticity of the `5_2` control by the
  cited theorem chain; exact executable topology fields; the bounded numerical
  length ledger; the improvement from an infinite-volume to a finite-volume
  cusp control; the exact marked-word theorem and descriptive pre-frozen phase
  comparison with its rank/presentation limitation.
- **Allowed:** the exact `D9` integrality, conjugacy/inversion invariance,
  repetition identity, and the frozen finite collision census.
- **Not allowed:** a full Bianchi primitive ledger, a presentation-invariant or
  metric-length comparison,
  an arithmetic-hypothesis verdict, an orbit-to-Gaussian-prime map, a full-flow
  Route-A tuple, full-flow A2--A4, Route B, or any determinant/operator claim.

The proxy-only tuple is
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_EXPLORATORY`; it cannot be transferred to the complete flow.

The paper remains in ARS Stage 1 / Proposal Stage 1 / Route A A0--A1.
