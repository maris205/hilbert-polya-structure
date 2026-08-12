# Paper Improvement Log

## Score progression

| Version | Score | Verdict | Status |
|---|---:|---|---|
| Round 0 baseline | — | Internal complete draft | Preserved |
| Round 1 review | 6/10 | Revise | Implemented |
| Round 2 review | 8/10 | Weak accept | Complete |

## Round 1

The complete independent review is preserved at
[`reviews/round1_review.md`](reviews/round1_review.md).  It found no
conclusion-changing mathematical error in the direct-image or closure
theorems, but required tighter positioning and hierarchy.

### Actions implemented

1. Replaced “minimal,” “sharp topological extension,” and
   “assumption-complete” language by an explicit sufficient-condition and
   assumption-explicit formulation.
2. Separated the compact-target proposition from the periodic-point
   obstruction and stated that it uses only compactness and continuity.
3. Narrowed the contribution to a wheel-source-specific obstruction package;
   the periodic coboundary mechanism remains explicitly classical.
4. Added an early direction statement: Paper 03 studies source-to-target
   images and closures, unlike the target-to-source strict extensions screened
   previously.
5. Made the decoder--fiber equivalence an explicit lemma.
6. Reproduced the wheel residue-graph source definition, not just its
   recurrence and grading.
7. Added the final real-topology step that locally finite lag-pair sets are
   closed and miss the diagonal.
8. Protected ordinary positive suspension roofs explicitly: the obstruction
   concerns inherited pointwise absolute labels on revisited states.
9. Replaced the figure's ambiguous “finite-valued” phrase by
   “ordinary, uncompactified clock space.”
10. Recompiled with bibliography and preserved `main_round1.pdf`.

### Round 1 artifacts

- `main_round0_original.pdf`: untouched baseline.
- `main_round1.pdf`: revision after the actions above.
- `main.pdf`: current working copy, byte-identical to Round 1 at this
  checkpoint.

## Round 2

The complete independent verification is preserved at
[`reviews/round2_review.md`](reviews/round2_review.md).  It rechecked the
direct-image theorem, closure topology, compact-target proposition, controls,
prior-art language, and route discipline.  It found no remaining Critical or
Major issue and assigned **8/10, Weak Accept**.

### Round 2 actions

1. Generalized the direct-image clause in `SOURCE_LOCK.md` from the integer
   clock alone to a frozen clock $a_k\in C$, explicitly covering both $q$ and
   $\log q$.
2. Rechecked the mutable Heeren working-paper metadata against the SSRN
   landing page and exposed both SSRN 6015434 and DOI
   `10.2139/ssrn.6015434` in the rendered bibliography.
3. Synchronized README, source-lock, control, figure-spec, and paper-plan
   status with the final theorem boundary.
4. Recompiled from source and repeated citation, reference, box, font,
   metadata, control-byte, and visual checks.

### Final Round 2 artifact

`main_round2.pdf` is byte-identical to the final `main.pdf`; hashes and build
details are recorded in `COMPILATION_REPORT.md`.
