# C404 paper plan

Title: All-period resonant counts for nonlinear Hénon–Frobenius maps.

One sentence: for a coefficient-uniform family of nonlinear resonant maps of
the affine plane, a pullback leading-term recurrence gives every fixed-point
count and hence a zeta function whose every positive power has a natural
boundary.

Type: complete mathematics article, not a venue submission. Plain article,
anonymous author block, no invented affiliation. No artificial page minimum
or ML conference limit. All quantified proofs must be in the PDF. Use modular
section files and only actually cited bibliography entries.

## Claim–evidence map

| Claim | Primary evidence | Role in paper |
|---|---|---|
| All-period formula under F_q, a!=0, 2<=m<q, p∤m | PROOF_PACKAGE §§3–6; independent review | Main theorem |
| Counts are ordinary geometric points | coprime initial forms plus Jacobian a^n | Essential convention, not optional footnote |
| Every positive zeta power has meromorphic natural boundary | PROOF_PACKAGE §7; independent radial-order check | Corollary of the same count |
| Cannot be directly vector-group-endomorphism conjugate | N1=qm non-p-power; SOURCE_AUDIT §3 | Narrow collision exclusion |
| Removing p∤m is false | q8 nonlinear exact example gives 2816, not 2944 | Hypothesis control, not general classification |

## Proposed sections

0. Abstract: lead with the explicit count, define q=p^e and r=p^v_p(n),
   state the nonlinear/coefficient hypotheses and natural boundary. No
   priority or target-arithmetic claims. Around 150–230 words if natural.
1. Introduction and source positioning: distinguish one-variable Bridy,
   direct algebraic-group BCH, and the actual affine-plane obligation.
   State the main theorem early. No historical source-source reconstruction
   presented as novelty; bounded literature confidence is not firstness.
2. System, clocks and equalizers: define H, Phi, S and prove the coincidence
   identity scheme-theoretically. Explain that delta is a linear operator
   on a ring, not a nonlinear-map binomial or a derivation.
3. Leading-term recurrence: include the complete polynomial lemma, coefficient
   survival, every delta iterate, and the p-primary time factorization.
4. Exact count: identify both actual leading forms, the standard-monomial
   rectangle and reducedness. Do not replace this with numerical evidence.
5. Analytic corollary: full zeta product derivation, normal convergence,
   radial orders and density for every positive integer power.
6. Boundaries and exact checks: direct-vector-group obstruction, genuine F4
   convention, the p|m failure, limitations of the five bounded checks and
   ordinary-period/Hasse–Weil/target distinctions.
7. Conclusion and reproducibility: summarize the one closed question; state
   missing full hidden-quotient classification and no target RH bridge.
   Disclose AI-assisted research/internal review, no human-peer-review claim.

No illustrative raster figure is needed. A compact mathematical comparison
of source families or a short exact-check table may be included only if it
improves clarity; do not generate decorative figures or add a test quota.

## Citations and reviewed scope

Use SOURCE_AUDIT S1–S4 as the verified base. Cite the exact arXiv versions
for theorem numbering where the published numbering differs. Reuse trusted
project BibTeX if available and cross-check metadata; otherwise verified
publisher/author metadata suffice under the citation fallback, with no
unresolved fabricated fields. Keep the classical ideal criterion attributed.

The existing independent proof/source review is in
`../wild_dynamics/CROSS_REVIEW_HENON_RESONANCE.md`. It found zero mathematical
blockers and no required correction. Its source-boundary feedback governs
the outline: do not claim all dynamically affine presentations are excluded.
The full drafted text still requires a non-author claim/notation/citation
and reverse-outline pass before release. The reviewer must read the actual
draft rather than only this plan.

Next gate: draft LaTeX, compile an initial PDF and record actual warnings;
coordinate final manuscript review and deterministic two-fresh-build QA.
