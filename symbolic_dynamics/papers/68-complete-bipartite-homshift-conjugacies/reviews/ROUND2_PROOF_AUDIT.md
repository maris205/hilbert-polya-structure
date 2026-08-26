# Round 2 proof audit

## Provenance and release posture

**Provenance:** same independent cross-agent reviewer as Round 1.  The
requested GPT-5.4 child remained unavailable because of the structural thread
cap; this report does not claim GPT-5.4 provenance.  External release remains
**HOLD**, and no priority conclusion is made.

## Verdict and score

**Verdict:** **INTERNAL THEOREM PASS; Round 1 critical defect is closed.**

**Score:** **9.1/10** after Round 1 revision.

The corrected all-shape theorem now counts restrictions of global points,
not merely colourings of the induced graph.  The entropy, dimer necessity,
finite-dependence, thermodynamic, and finite-quotient descendants were traced
from their actual hypotheses and remain valid.

## Round 1 closure audit

1. **C1 closed.** For nonempty `F`, Lemma `lem:phase` gives exactly two
   disjoint global-phase restriction classes, of sizes
   `m^|F cap E| n^|F cap O|` and its reversal.  Completeness of the target
   extends every such restriction.  `N(empty)=1` is separately stated.
2. **Control semantics closed.** The script now enforces one lattice-wide
   phase.  The remote-even and remote-opposite-parity tests explicitly
   distinguish extendibility from local edge admissibility.
3. **M1 closed.** Theorem `thm:classification` now states memory set
   `{-e_1,0,e_1}`.  Equations (3.1)--(3.2) select the correct neighbour from
   the visible part membership.
4. **Gibbs equality closed.** The pressure proof begins with a joint
   `A x B` marginal, separates within-dimer independence from the two marginal
   Gibbs equalities, and then separates across-dimer Bernoulli equality.

## Independent proof trace

### Product classification

- Lemma `lem:phase` is path-parity exact for every `d>=1`.
- Every `A`-site anchors `(v,v+e_1)`; every `B`-site belongs to the unique
  anchor at `v-e_1`.  These dimers are disjoint and cover the lattice.
- Applying `f` once per dimer preserves target-part membership.  The anchor
  is symbol-detected, so every translation carries anchors to anchors.
- The same construction with `f^{-1}` reverses each dimer exactly.
- Corrected connected-box counts still give entropy `(1/2)log(mn)`, so entropy
  invariance yields the necessary product equality.

### Finite dependence

- For any remote even displacement, the target-part indicators are equal
  pointwise by the phase lemma.
- Finite dependence makes them independent, so `p=p^2` and the phase is
  deterministic.
- Odd subgroup elements exchange the two clopen phases; even subgroup
  elements preserve the parity-wise iid construction.  Both directions of
  the subgroup theorem follow.

### Pressure and periodic data

- Weighted restrictions inherit the same single global phase; rectangular
  parity densities tend to one half.
- The index-two even-subgroup full-shift model has dimer potential
  `varphi(a)+varphi(b)`.  Entropy and potential scale by the same factor two,
  while the finite phase mixture has zero entropy density.
- An odd period is impossible.  If `L<=E`, the quotient has
  `[E:L]` cosets of each parity, giving exactly `2(mn)^[E:L]` points.

## CRITICAL issues

None.

## MAJOR issues

None.

## MINOR issues

None requiring a manuscript change.  The bounded source status, rather than
a proof defect, is the only reason the release posture remains HOLD.

## Source and ownership recheck

The direct-source assignments remain accurate: Chandgotia’s Lecture 4 owns
the public complete-bipartite phase/MME picture; Chandgotia--Thorat Corollary
8.4 owns the four-cycle-free invariant finite-dependence obstruction; and the
one-sided Hom-shift category is separately scoped.  The corrected global
restriction formula makes no new literature claim.  URLs remain recorded in
`CITATION_AUDIT.md` and Round 1 review.

## Control and build audit

- Revised deterministic control: PASS.
- Round-1 build: 7 A4 pages.
- Log warnings/undefined references/undefined citations/box warnings: zero.
- Round-0 and Round-1 PDFs have distinct preserved hashes, proving the
  baseline was not overwritten.

## Release recommendation

**INTERNAL GO / EXTERNAL HOLD.** No further mathematical edit is demanded by
this audit.  Re-run the unchanged controls and build for the Round-2 frozen
artifact, then update final QA and checksums.
