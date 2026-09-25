# Separate mathematical review — AQC-20260916-IMS01

**Paper:** 205-invariant-measure-support  
**Reviewer invocation:** `/root/research_controller/invariant_measure_reviewer_round21`  
**Review / final-core binding:** 2026-09-16 09:40:02 UTC  
**Disposition:** NO UNRESOLVED MATHEMATICAL OR SCOPE FINDING within the frozen contract.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

## Actual review sequence and limits

I first read only the new [frozen card](../candidate-card.md), the entire
[194 dependency proof](../../194-rapid-decay-cone-completion/paper.md),
and the relevant stream guidance. Before reading the author proof, I
derived the logarithmic pair-coordinate strip argument, arbitrary
circle-mixture classification, and a locally finite deck-periodized
bounded-continuous witness. These derivations were sent to the controller.
The inherited conversation already exposed research context and possible
approaches: this was a separate actual model invocation, not a blind,
cross-model or human peer review.

I then read the complete final [paper](../paper.md),
[README](../README.md), [card](../candidate-card.md),
[claim ledger](../claim-ledger.md), and [evidence index](README.md).
ARS router, academic-paper workflow and argument-builder instructions
were personally read and used only for bounded claim/evidence/reasoning
and adverse-scope checks. No full publication pipeline, venue judgement,
numeric score, external model/API, or new research line was invoked.

## Mathematical checks

1. **Full-owner coordinate and measurability.** Each pair set U_ab is
   open, deck-saturated and flow invariant in the exact 194 quotient.
   Adding a deck power adds the same integer to both logarithmic terms,
   so h_ab descends continuously. Its physical-time increment is the
   nonzero constant c_ab times time. The half-open strips in Lemma 2
   are Borel, pairwise disjoint integer-time translates and cover U_ab.
   Finite mass forces each strip to be null; countable additivity
   gives null mass for the whole pair set. No recurrence or unproved
   countable-base hypothesis is needed.

2. **Infinite supports and complete classification.** The countable
   union over all distinct atom pairs is exactly the entire mixed
   locus, including every infinite support. Its complement Gamma is
   closed. Each individual singleton circle is homeomorphic to the
   compact time circle by 194's return equation and quotient
   Hausdorffness. Equal arc partitions and continuity of finite
   measures determine its invariant probability as normalized time
   measure. Thus Theorem 3 gives all, and only, arbitrary countable
   mixtures with unique weights; it does not force one common circle.

3. **A genuine lost continuous observable.** In Proposition 4 the
   mass-window ratio 5/3 is strictly less than the least nontrivial
   deck growth factor 2. At most one periodized summand is nonzero.
   Mass bounds on a neighborhood also bound all possible summand
   indices uniformly, proving local finiteness and continuity on the
   full cover. Reindexing proves deck invariance, and the quotient
   therefore owns the bounded scalar function. Its value is 1/4 at
   [(q_2+q_3)/2], whereas it vanishes on every singleton circle. It
   is the same nonzero C_b function lost in every classified L2 space.

4. **Adverse controls.** The mixed orbit map is globally injective by
   194's aperiodic return equation. Its Lebesgue pushforward is an
   infinite invariant Borel measure. Compact orbit segments are
   closed and have finite preimage length, and their union is the
   Borel orbit; adjoining its null complement proves sigma-finiteness.
   Thus the finite-mass restriction is substantive. The generic
   distinct-multiplier calculation and the equal-multiplier periodic
   counterexample correctly delimit arithmetic specificity.

5. **Representation and owner boundary.** Invariance and the inverse
   flow make ordinary L2 pullback unitary, but the scalar observation
   map is not faithful. No mixed state has been removed. This is not
   a no-go theorem for arbitrary Hilbert models or nonunitary orbit
   features. No determinant from 201, classical geometry, natural A0,
   quantum generator, target spectrum or formal Route conclusion is
   imported. Naturalness remains OPEN.

No author correction was required. The supported decision is ADVANCE
the classification and STOP finite-invariant-probability L2 as a
faithful representation of every continuous full-state observation.
This review is evidence of the checks above, not a correctness certificate.

## One final binding of the four mathematical cores

After the author confirmed these four files were final, their SHA-256
values were taken once with `sha256sum`:

| Core file | SHA-256 |
| --- | --- |
| README.md | `4ca87e402898c75a11552722b435bd688be836037c35ffd540cf9f8858ac4d13` |
| candidate-card.md | `e0126cac84591652f27ea9cd8e35ffe2a89364e295414aa50295b9a7db26f582` |
| paper.md | `c06cbbfe80c83a931dcfccf699aafa6e23fbe1c4166c2dcc066fc7537d10175b` |
| claim-ledger.md | `c3510a641a8e64c2e90a6b369cefe5e3a62a1419fdfca4f9126496911eb95d30` |

The evidence index is intentionally unbound so actual process receipts
can be appended without changing reviewed mathematical cores. Root
owns the single integrated Round21 link/identity/mechanical check;
this reviewer did not perform a duplicate whole-batch sweep or edit
author cores, old packages, navigation, Git, or configuration.
