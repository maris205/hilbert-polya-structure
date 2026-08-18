# Paper improvement log

## Outcome

Two GPT-5.4 xhigh review-and-repair rounds were completed.  The first review
scored the manuscript 7/10 (`Almost`) with no critical issue, three major
presentation/provenance issues, and four minor proof/prose issues.  The second
review scored the revised manuscript 9/10 (`Almost ready`) with no critical or
major issue and three minor source-locator/wording issues.  Every listed issue
was repaired before the final deterministic build.

The preserved stage PDFs are:

- `main_round0_original.pdf`: draft before the two review rounds;
- `main_round1.pdf`: result after the first repair round;
- `main_round2.pdf`: final result after the second repair round and final QA;
- `main.pdf`: byte-identical release-candidate copy of `main_round2.pdf`.

No Feishu configuration was present, so no notification was sent.  Round 2 used
a fresh ephemeral reviewer session supplied with the full revised source because
no persistent reply channel was available.

## Score Progression

| Round | Paper snapshot | Review score | Findings entering repair | Disposition |
|---|---|---:|---|---|
| Round 0 | Original writer draft | not scored | Baseline before paper-review rounds | Preserved as `main_round0_original.pdf` |
| Round 1 | First reviewed draft | 7/10 (`Almost`) | 0 critical, 3 major, 4 minor | All listed findings repaired; preserved as `main_round1.pdf` |
| Round 2 | Revised source review | 9/10 (`Almost ready`) | 0 critical, 0 major, 3 minor | All listed findings repaired; final candidate preserved as `main_round2.pdf` |

### Remaining issues summary

The final compiled manuscript has 16 A4 pages.  No reviewer-listed critical,
major, or minor item remains open after the recorded repairs.  Independent
writer audit is still required, so this log does not assert a clean release
verdict.

## Round 1 fixes

1. Removed internal audit/process language from the theorem-first main body and
   moved the exact replay, Route, hashes, chronology, and provenance material to
   detachable non-anonymous appendices.
2. Deleted bounded-search/no-collision language as claim support and based all
   priority boundaries only on direct mathematical and source comparison.
3. Removed identifying authority-package paths and commit vocabulary from the
   anonymous main narrative.
4. Expanded the Ban--Hu--Lai hypothesis and locator audit and explained why the
   primitive full shift lies under the author-manuscript quantifiers.
5. Added explicit discrete covering estimates for Hausdorff and box dimension.
6. Added the bounded-holomorphic-neighborhood sentence to the natural-boundary
   contradiction.
7. Rewrote front-end ownership/Route terminology into conventional theorem-first
   prose.

## Round 1 raw review (verbatim)

**Score**

7/10

**Summary**

The core mathematics looks solid and interesting. I do not see a fatal break in the exact finite-\(N\) chain calculus in §3 (\eqref{eq:chain-product}, \eqref{eq:valuation-census}, \eqref{eq:exact-remainder}), the composite-\(q\) inverse-limit extension, either accumulation inclusion in \eqref{eq:acc-log}, the golden coefficient algebra in §4 (\eqref{eq:gamma-residue}, \eqref{eq:gamma-modes}, \eqref{eq:separation-certificate}), the dyadic radial coefficient and sign in §5 (\eqref{eq:radial-coefficient}), or the continuation contradiction for the natural boundary. The Ban--Hu--Lai author-manuscript correction is mostly careful and, importantly, insulated from the unverified version of record.

The main problem is not proof integrity but paper shape: too much of the manuscript is devoted to ownership/provenance/Route/audit language that is not standard mathematical exposition and significantly hurts readability, anonymity posture, and submission readiness.

**Ranked Strengths**

1. The exact remainder formula in §3 is clean, sharp, and genuinely useful: the increment identity, valuation census, and summation-by-parts mechanism fit together very well.
2. The golden specialization in §4 is the strongest part of the paper: \(\gamma_k\) is derived exactly, the algebraic tail certificate is explicit, and the all-level separation argument is convincing.
3. The natural-boundary proof in §5 is efficient and correctly normalized; the \(Q=4,\xi=i\) check is a good safeguard against the common phase/sign mistake.
4. The manuscript is unusually disciplined about separating finite replay from proof; §6 does not try to sell computation as evidence for the infinite theorems.
5. The author-manuscript correction in §2.2 is substantially fairer than most such discussions because it states the checked artifact and refuses to project the claim onto the version of record.

**Weaknesses**

- `MAJOR` — §1 “Verification audit” and “Ownership boundary”; §2 Table \cref{tab:ownership}; §6 entire; §7 “Route outcome” and “Retrospective chronology”; Appendix B.2–B.5.  
  The paper is overloaded with internal audit/provenance/process language (`Route`, `State A`, hashes, authority package, duplicate stops, retrospective candidate selection). This is not standard mathematical exposition and it materially obscures the theorem package.  
  Minimum fix: cut almost all of this from the paper itself. Keep at most one short prior-work paragraph, one short reproducibility paragraph, and move the rest to a non-anonymous supplement or repository note.

- `MAJOR` — §2 Table \cref{tab:ownership}, row “proved here; no exact collision found in a bounded search”; Appendix B.2 “bounded search”.  
  The manuscript still lets negative search evidence leak into claim framing. That is bad mathematical hygiene even though you explicitly downgrade it.  
  Minimum fix: delete all “bounded search/no exact collision found” language from the main paper and from any place that sounds like claim support; restrict priority language to direct mathematical/source comparison only.

- `MAJOR` — Appendix B.3–B.4, especially “Paper-44 authority package”, protected paths, commits, hashes, `State-A` workflow.  
  For an anonymous math submission, this is inappropriate and may compromise blind-review posture while adding no mathematical value.  
  Minimum fix: remove identifying workflow/package nomenclature entirely from the submission version.

- `MINOR` — §2.2, \eqref{eq:bhl-displayed}.  
  The Ban--Hu--Lai correction is mostly careful, but for maximum fairness it should quote the exact hypotheses of the arXiv v1 statement, not only the displayed asymptotic and dictionary. As written, the reader has to trust that the full-shift counterexample lies inside the original quantifiers.  
  Minimum fix: add the precise theorem/remark locator and hypothesis subset from arXiv:2210.09115v1, then explicitly say why \(A=J_d\) satisfies those hypotheses.

- `MINOR` — §4, proof of \cref{thm:golden}; Appendix A “All-level separation and dimension”.  
  The Hausdorff/box dimension proof is basically correct, but the lower-bound step is still a bit terse for publication standard: “an interval of radius comparable to \(t^n\) meets only a bounded number of them” should be converted into an explicit covering/packing estimate.  
  Minimum fix: add one displayed statement such as \(N(K,\delta)\asymp 2^n\) for \(\delta\asymp t^n\), or spell out the bounded-overlap implication for both Hausdorff and box dimensions.

- `MINOR` — §5, proof of \cref{thm:natural}.  
  The continuation contradiction is correct, but one more explicit sentence would make it airtight for skimmers: namely, if \(H\) is holomorphic on a neighborhood \(U\ni \xi\) and equals \(G\) on \(U\cap\mathbb D\), then \(H\) is bounded near \(\xi\), contradicting \eqref{eq:radial-coefficient}.  
  Minimum fix: add that sentence directly in the proof.

- `MINOR` — Abstract final sentence; §1 and §7 throughout.  
  “prior-owned”, “eligible”, “nonclaims”, “Route”, and “retrospective” are not good front-end prose for a math paper. They slow the skim and make the manuscript sound defensive.  
  Minimum fix: rewrite the abstract/introduction/conclusion in standard theorem-first prose and compress the ownership discussion to conventional prior-work language.

**Missing References If Any**

No missing citation is fatal to the proofs, but the context is thin.

Recommended additions:
- Delange on classical digital-sum/summatory fluctuations.
- Flajolet–Gourdon–Dumas on Mellin/digital fluctuation asymptotics.
- Optionally Moran or Hutchinson for a standard dimension reference under strong separation, even if you keep the proof self-contained.

**Verdict**

Almost.

The theorem core looks publishable to me: exact finite-\(N\) identity, full accumulation-set characterization, golden separation, dimension, and dyadic natural boundary all survive audit. What stops “Ready” is the presentation architecture, not the mathematics. A submission version should be cut back hard to theorems, proofs, and a conventional prior-work discussion.

ROUND1_REVIEW_COMPLETE

## Round 2 fixes

1. Made the Ban--Hu--Lai locator exact by spelling out the Theorem 3.3(2) to
   Theorem 3.1 to Theorem 3.1(2)-proof to Remark 3.4 chain.
2. Replaced the remaining internal adjective `frozen` with `present` in the
   mathematical narrative.
3. Replaced `Primary-owned/elementary` with the neutral
   `standard/elementary` in the ownership table.

## Round 2 raw review (verbatim)

Score: 9/10

Verdict: Almost ready

No CRITICAL or MAJOR mathematical issues remain.

Concise summary: the revised source is mathematically coherent and materially stronger than round 1. The exact remainder formula, both accumulation inclusions, the golden-mode algebra and tail certificate, the Hausdorff/box-dimension argument, and the corrected radial coefficient with explicit natural-boundary contradiction all check out. The Ban–Hu–Lai reconciliation is now substantively fair, zero-credit is consistently maintained, and the replay/Route/chronology material is quarantined clearly enough for a release copy.

Ranked strengths:
1. `sections/3_exact_boundary.tex` now gives a clean exact finite-\(N\) law and both accumulation inclusions without smuggling in finite replay.
2. `sections/4_golden_geometry.tex` is much tighter: the Binet reduction, mode decomposition, \(99044\) certificate, strong separation, and discrete covering estimates fit together correctly.
3. `sections/5_natural_boundary.tex` fixes the normalization/sign issue and closes the analytic step with the needed bounded-holomorphic contradiction.
4. The author-manuscript correction in `sections/2_prior_correction.tex` is now same-object, quantified, and properly caveated to `arXiv:2210.09115v1` rather than over-claiming against the journal version.

Remaining issues:

MINOR: `sections/2_prior_correction.tex`, subsection `The author-manuscript specialization`, opening paragraph beginning “The checked artifact is the author manuscript…”. The locator is slightly too compressed. In `arXiv:2210.09115v1`, the explicit “1-d mixing SFT with transition matrix \(A\)” hypothesis is spelled out in the proof of Theorem 3.1(2), while Theorem 3.3(2) reduces to that proof and Remark 3.4 supplies the `d=1`, `N=p^{kn}` specialization. Minimum fix: name that reduction chain explicitly so the source audit is exact rather than inferred.

MINOR: `sections/2_prior_correction.tex`, final sentence of the full-shift counterexample paragraph: “under our frozen primitive one-dimensional definition.” `frozen` is still internal audit/process vocabulary in the main theorem narrative. Minimum fix: replace `frozen` with `present` or delete the adjective.

MINOR: `sections/2_prior_correction.tex`, Table `tab:ownership`, row “Multiplicative SFT, \(q\)-adic chain partition, chain product — Primary-owned/elementary”. `Primary-owned` reads like provenance bookkeeping rather than standard scholarly attribution. Minimum fix: change to `standard/elementary` or equivalent neutral wording.

Missing references: none genuinely required. The present citations are adequate for the mathematical claims made here. I specifically checked the Ban–Hu–Lai locator/quantifier chain against [arXiv:2210.09115v1](https://arxiv.org/abs/2210.09115v1) and its [PDF](https://arxiv.org/pdf/2210.09115v1).

Residual risk: I did not run a TeX compile from the prompt alone, so this is a source-level mathematical/presentation review rather than a build audit.

ROUND2_REVIEW_COMPLETE

## Final verification after round 2

The three remaining minor findings were repaired, followed by two independent
clean builds and the full compile/font/citation/text/bounding-box/control-character/
visual QA reported in `COMPILATION_REPORT.md`.  `main.pdf` and
`main_round2.pdf` are byte-identical with SHA-256
`3ee4b7662f9d5f8fdd6a410461c7c8094cb5c2782fbbb486603f56b9841cb66d`.

A later seal audit found that `plainnat` lowercased the blackboard-bold (N) in
one bibliography title.  Double grouping now protects `\(\mathbb{N}^d\)` in
`references.bib`; the generated BBL preserves the uppercase token and page 16
renders it legibly.  The synchronized plan now records the actual six main
sections and Appendices A--C.  These were post-review editorial/provenance
repairs, not a third scoring round.  The fixed-epoch double build and complete
PDF QA were rerun afterward; independent release audit remains outstanding.
