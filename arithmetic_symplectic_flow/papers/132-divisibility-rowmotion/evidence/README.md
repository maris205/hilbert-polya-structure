# Evidence — ASFS-SCOUT-20260914-96

**Date:** 2026-09-14  
**Status:** `PRE-P0 STOP — INFINITE DIVISIBILITY ROWMOTION IS NOT SURJECTIVE; PRIME-RANK SOURCE ORBIT DOES NOT RETURN`

## Primary literature and exact use

1. Michael Joseph, *Antichain toggling and rowmotion*, Electronic Journal of
   Combinatorics 26(1) (2019), Paper 1.29. The publisher-hosted full text was
   read at Section 2.1 and Definition 2.4 on 2026-09-14. Section 2.1 states the
   finite-poset convention; Definition 2.4 gives the frozen rowmotion formula.
   The source establishes the finite comparison only.
   [Publisher full text](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i1p29/pdf/)
2. Jessica Striker and Nathan Williams, *Promotion and Rowmotion*, European
   Journal of Combinatorics 33 (2012), 1919--1942. The arXiv metadata and abstract
   were inspected to verify source identity and the promotion/rowmotion
   context. No infinite-divisibility theorem is attributed to this source.
   [Version 3 metadata](https://arxiv.org/abs/1108.1172v3)

Search queries were `rowmotion infinite posets order ideals minimal elements
complement bijection finite poset` and `rowmotion divisibility poset integers
infinite periodic orbits`. Retrieval informed the finite/infinite source
boundary; it is not a nonexistence search certificate.

## Exact inputs, method, and limits

The input is the [version-1 card](../candidate-card.md): P=N_{>=2} with
divisibility, every downset included, R(I)=downarrow(min(P\\I)). Proofs in the
[paper](../paper.md) derive the image, explicit source orbit, and prime-power
height law. The arguments use no approximation, finite cutoff, floating-point
precision, or externally supplied prime list. No orbit computation was run.

The two comparator chain calculations are elementary exact checks on separate
objects; their returns or escape are not credited to P. A full classification
of arbitrary periodic infinite downsets remains OPEN after the decisive
non-surjectivity stop. No analytic object or geometric realization is supplied.

## Verification

A second [independent review](review.md) also checked the image characterization,
rank orbit, and finite-height necessary condition, with no required correction.

An independent delegated model check of the three elementary propositions
confirmed the image/inverse argument, the rank-orbit formula, and the finite
prime-power-height law, including the empty and full downset edge cases. The
review agreed that periods at least 2 remain OPEN and that the finite-height
identity must not be extrapolated to infinite height. This is model-assisted
proof checking, not external peer review or a novelty assessment.

Package-local Markdown targets and the prior-work link are checked for
existence. The same candidate ID and stop status appear in the paper, card,
claim ledger, and README. These documentary checks do not prove the theorem;
the explicit proofs are the mathematical evidence.

**Decision:** `stop`; portfolio `fork`. Classical A0/A1/A2 `UNASSIGNED`;
formal Route coordinates `NOT EVALUATED`; Route B `NOT INVOKED`.
