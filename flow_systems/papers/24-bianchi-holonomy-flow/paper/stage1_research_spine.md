# P24 Stage-1 research spine after Round 4

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
   control with a replayable complex-length prefix (Round 4).

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

## Central falsification logic

The decisive future comparison is not “Bianchi versus any chaotic flow.”  It
is:

```text
arithmetic finite-volume cusped H^3 flow
versus
non-arithmetic finite-volume cusped H^3 flow,
under one enumeration rule and one predeclared statistic.
```

If the Bianchi holonomy signal persists with comparable strength on `5_2`, the
current holonomy mechanism is generic to cusped hyperbolic 3-geometry and must
stop as an arithmetic explanation.  If a stable separation survives, it only
licenses a sharper arithmetic-structure question; it does not create an
orbit-to-prime-ideal map.

## Claim firewall

- **Allowed:** the existence and non-arithmeticity of the `5_2` control by the
  cited theorem chain; exact executable topology fields; the bounded numerical
  length ledger; the improvement from an infinite-volume to a finite-volume
  cusp control.
- **Not allowed:** a full Bianchi primitive ledger, matched length statistics,
  an arithmetic-hypothesis verdict, an orbit-to-Gaussian-prime map, a formal
  Route-A tuple, A2--A4, Route B, or any determinant/operator claim.

The paper remains in ARS Stage 1 / Proposal Stage 1 / Route A A0--A1.
