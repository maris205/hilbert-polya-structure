# Paper Improvement Log

The fixed workflow used one persistent GPT-5.4/xhigh session, `01a0224e-9bcd-78d1-9618-add703ac249a`,
for exactly two manuscript-review turns.  The raw outputs below are reproduced
verbatim and also preserved as standalone review artifacts.

## Score progression

| Round | Score | Verdict | Key changes |
|---|---:|---|---|
| Round 0 (original) | 8/10 | Almost | Baseline manuscript; proofs passed, four production-level MINOR issues remained. |
| Round 1 | 9/10 | Yes | Figure numbering synchronized, counterexample typo fixed, warnings removed, and SCC terminology standardized. |
| Round 2 (review-final) | 9/10 | Yes | No reviewer-requested manuscript change; deterministic trailer-ID closure and A/B QA. |
| Post-audit production repair | -- | re-audit hold | ToUnicode delimiter mappings and fail-closed raw-extraction QA; theorem text unchanged. |

## Round 1 review and fixes

<details>
<summary>GPT-5.4 xhigh review (Round 1), verbatim</summary>

1. **Overall Score and Verdict**

**8/10**: mathematically strong and scope-disciplined, with publishable core results, but round 0 still needs a small amount of production/provenance cleanup before I would move to an unqualified accept-level recommendation.  
**Verdict:** **Almost**

2. **Summary**

The paper gives an exact Hausdorff-dimension formula for a complete cyclic core with an unrestricted one-level feeder, then extends the mechanism to the canonical unrestricted \(L\)-level forced chain with exact denominator \(d^L\), monotonicity, and an explicit \(O(d^{-L})\) approach to the spectral mean. The proofs are self-contained, respect the BLW firewall, and the four-state example does exactly the intended job of falsifying a naive SCC-max rule. The remaining issues are mostly production, cross-document consistency, and polishing rather than theorem-level defects.

3. **Strengths, ranked**

1. The scope control is excellent. The manuscript repeatedly states the exact family proved, the excluded classes, and the nonclaims, and it does not smuggle in a broader reducible theorem.
2. The main arguments are genuinely self-contained. The cylinder-count/Frostman route, finite-union reduction, and elementary spectral-mean calculation avoid reliance on version-sensitive BLW equality clauses.
3. The saturation section is sharp and correctly qualified: universal sufficiency, Fourier-qualified necessity, and an explicit nondivisible witness are all present and cleanly separated.
4. The canonical deeper-chain result is stronger than a heuristic limit statement: it keeps the exact \(d^L\) denominator, proves monotonicity by the embedding \(m\mapsto dm\), and gives a concrete balanced-composition error bound.
5. The four-state corollary is minimal, transparent, and carefully delimited: it refutes one tempting general formula without pretending to solve arbitrary reducible cases.
6. The figures and captions are mostly honest and useful. In particular, the captions explicitly distinguish analytic formulas, exact optimizer data, and balanced-certificates from experiments.

4. **Weaknesses, ranked and tagged**

1. **MINOR**: The manuscript’s figure numbering is internally consistent, but the frozen support documents are not. `PAPER_PLAN.md`, `CLAIMS_EVIDENCE.md`, and `figures/data/figure_provenance.json` treat the optimizer/certificate plot as Figure 2 and the two-phase parity plot as Figure 3, while the manuscript presents them as Figures 3 and 2 respectively. This weakens the reproducibility narrative even though the mathematics is unaffected.
2. **MINOR**: The mandatory witness in Section 5 has a visible TeX typo: in [Example 5, `ex:nondivisible`] the display reads `p=4,qquad d=N=2,qquad ...` instead of using `\qquad`. A headline counterexample should not carry a display-level error.
3. **MINOR**: The build layer is not yet clean. `BUILD_RECEIPT.txt` reports 33 warnings, including an `enumitem` negative labelwidth warning; the PDF remains readable, but a paper that emphasizes exact verification should also present a tidier typesetting audit.
4. **MINOR**: The four-state discussion shifts between “cyclic essential strongly connected component” and “cyclic strongly connected components” in Section 8 and the conclusion. The logical point survives, but the terminology should be made uniform.

5. **For every CRITICAL or MAJOR weakness, a minimal, concrete, globally consistent fix tied to exact section/equation/theorem locations**

No **CRITICAL** or **MAJOR** weaknesses identified. The needed changes are local cleanup, not theorem surgery.

6. **Missing or incorrect references, if any**

**Required:** None identified within the frozen scope. The present citations are sufficient for the claims actually made, and the owner-subtraction firewall is handled correctly.

**Optional:** If the target journal expects a conventional citation for the mass-distribution/Frostman principle used in [Section 3, Lemma `lem:cylinder-dimension`], one may add a standard reference, but it is not logically necessary because the proof is written out. No additional citation should be used to import BLW primitive/equality or spectral-radius claims; the current self-contained approach is the right one.

7. **Exact claims-versus-proof audit**

Under the stated frozen assumptions — \(d\ge 2\), \(p\ge 1\), positive phase sizes, complete cyclic blocks, ordered \(d\)-ary tree, no feeder return edge, and natural logarithms — the claims line up with the proofs.

- **Q0:** Supported. [Section 3, Lemma `lem:cylinder-dimension`] correctly handles the metric endpoint window \([e^{-|\Delta_n|},e^{-|\Delta_{n-1}|})\), the lower-bound Frostman direction, and the liminf normalization. This is the right foundation for every equiprobable stratum later used.
- **Q1:** Supported. [Section 4, Theorem `thm:core`] derives the core formula from the exact prefix count \((\ref{eq:core-prefix-count})\) plus the weighted-limit lemma, with the backward index \(j-t\) kept consistent. The elementary computation of \(\rho(C(a))\) is clean and does not violate the BLW firewall.
- **Q2:** Supported. [Section 4, Proposition `prop:fixed-one-level` and Theorem `thm:one-level`] correctly separate ordered child assignments from compositions, use finite unions only after that separation, and make core dominance explicit through concentrated compositions in \((\ref{eq:concentrated-dominance})\). The finite-composition variant is properly restricted to separately declared one-level families in [Remark `rem:finite-composition`].
- **Q3:** Supported. [Section 5, Theorem `thm:saturation`] proves the universal upper bound by mean preservation and the exact equivalence between saturation, constant circular convolution, and equality of shifted integer products.
- **Q4:** Supported with the stated extra hypothesis. [Section 5, Theorem `thm:fourier-divisibility`] gets the quantifiers right: \(p\mid N\) is universally sufficient, while necessity is asserted only under full nonzero Fourier support of \(c\). The mandatory nondivisible witness is present in [Example `ex:nondivisible`]; only the display typo should be fixed.
- **Q5:** Supported. [Section 6, Theorem `thm:two-phase`] gives the exact two-phase formulas, treats the \(\delta=0\) boundary separately, and proves strict gain for nonconstant profiles without overclaiming an empirical phenomenon.
- **Q6:** Supported. [Section 7, Theorems `thm:deep-exact` and `thm:deep-convergence`] correctly derive the exact denominator \(d^L\) from \((\ref{eq:deep-scale-ratio})\), prove monotonicity via \((\ref{eq:grid-embedding})\), and establish the balanced error bound \((\ref{eq:DL-rate})\). The restricted-family scope is also handled correctly: [Proposition `prop:balanced-access`] gives only the bounded-access conclusion and explicitly refuses to infer monotonicity without an added nesting condition.
- **Q7:** Supported. [Section 8, Corollary `cor:four-state`] computes \(\log 2/3\) for the cyclic core and \(\log 2/2\) for the full shift directly from earlier theorems, and the concluding sentence is properly limited to refuting an SCC-max Hausdorff formula rather than claiming a general reducible theory.

Global audit points:

- **Assumptions:** Explicit and stable throughout. I did not find silent use of incomplete blocks, return edges, zero phase sizes, or arbitrary feeder shapes.
- **Metric endpoints:** Correctly handled in [Section 3, `\eqref{eq:ball-window}`] and in Appendix A.
- **Finite unions:** Used in the right places and with the right role: first on finitely many root-phase or ordered-assignment strata, then on the full shift.
- **Core dominance:** Explicitly proved for one level in \((\ref{eq:concentrated-dominance})\) and for deeper chains via concentrated compositions plus monotonicity.
- **Fourier quantifiers:** Correctly one-way unless full nonzero Fourier support is assumed.
- **Nondivisible witness:** Mathematically correct and properly positioned as a mandatory counterexample to an unconditional converse.
- **Exact \(d^L\) denominator:** Proved, not guessed.
- **Monotonicity:** Properly derived from the integer embedding, not from a continuous relaxation.
- **Balanced error bound:** Correct within the stated hypotheses, and one-sidedness is appropriate because \(a_j\ge 1\) implies \(H_j(c)\ge 0\).
- **Restricted-family scope:** Appropriately limited; no silent upgrade to arbitrary multilevel restricted feeders.
- **Four-state conclusion:** Correctly scoped and not overstated.

8. **Figure/table, anonymous A4, and build/QA audit**

- **Figure 1:** Strong schematic. It conveys the mechanism well, the caption is honest, and the “ordered children, grouped only for counting” disclaimer is important and well placed.
- **Figure 2:** Readable and mathematically appropriate. The caption correctly says this is an analytic plot for discrete \(d\), not an experiment or a continuous-\(d\) claim.
- **Figure 3:** Substantively good. The left exact-optimizer panel and right certificate panel are clearly distinguished in the caption, which matters. The right-panel legend is a bit dense but still usable.
- **Tables 1 and 2:** Conceptually well chosen. Table 1 does the source-boundary work without promotional language; Table 2 gives deterministic counts and frozen anchors rather than pseudo-performance metrics.
- **Anonymous A4 audit:** Passed. The manuscript uses `article` with A4/11pt, has `Anonymous Authors`, no affiliations, acknowledgements, grants, repository link, or self-identifying prose. The PDF metadata also shows `Author: Anonymous Authors`.
- **Build/QA audit:** Broadly passed, but not clean. The deterministic build story, fixed `SOURCE_DATE_EPOCH`, page size, and embedded fonts are all good. The remaining problems are the 33 warnings, the `enumitem` warning, the visible `qquad` typo in Section 5, and the auxiliary-document figure-number mismatch. The PDF is untagged, which is not usually fatal for this genre but is worth knowing.

ROUND1_REVIEW_COMPLETE

</details>

Raw-review SHA-256: `ea44bac099131348e1044d4a6869e169e0ccfd8e26c91d86ee0747d2a81d1928`.
Raw-event SHA-256: `772fa3ba26d715a1bfe02efae6c8f6584c26a8f738dec0475da99abe0b5bc48d`.

### Fixes implemented

1. Synchronized Figure 2 (two-phase analytic plot) and Figure 3
   (optimizer/convergence plot) across the manuscript, plan,
   claims--evidence matrix, deterministic generators, verifier, and provenance.
2. Repaired the visible `qquad` typo in the mandatory nondivisible witness.
3. Reworked table and appendix layout at source level and extended the clean
   build pass, reducing the warning count from 33 to zero without suppressing
   diagnostics.
4. Defined and standardized `cyclic essential SCC` across Section 8, the
   claims matrix, and the conclusion.

## Round 2 review and fixes

<details>
<summary>GPT-5.4 xhigh review (Round 2), verbatim</summary>

1. **Overall Score and Verdict**

**9/10**: a strong, narrowly scoped mathematical paper with self-contained proofs, correct claim discipline, and now clean production/reproducibility presentation.  
**Verdict:** **Yes**

2. **Resolution audit of all four first-round MINOR issues**

- **Figure numbering consistency:** Resolved. The manuscript, `PAPER_PLAN.md`, `CLAIMS_EVIDENCE.md`, the provenance JSON, and the rendered PDF now agree that Figure 2 is the two-phase analytic plot and Figure 3 is the optimizer/convergence plot.
- **Nondivisible-witness typo:** Resolved. In Section 5, Example 5.4 now correctly displays `p=4,\qquad d=N=2,\qquad a=(2,3,2,3),\qquad m=(1,1,0,0)`.
- **Build/layout cleanup:** Resolved. `build/round1/BUILD_RECEIPT.txt` reports `warning_lines=0`, and the provided QA states zero undefined references/citations, A4, 19 pages, and embedded fonts; the appendix/table layout is visibly repaired in the rendered pages.
- **Terminology for cyclic essential SCC:** Resolved. Section 8 now defines “cyclic essential” once and uses the terminology consistently in the corollary, surrounding prose, claims matrix, and conclusion.

3. **Summary**

The revised manuscript now reads as a clean, internally consistent theory paper: the one-level transient optimizer, the saturation arithmetic, the canonical \(L\)-level chain, and the four-state obstruction are all proved within the declared frozen scope. The proofs remain self-contained and properly fenced from BLW’s version-sensitive equalities, while the production layer now matches the rigor of the mathematics.

4. **Strengths, ranked**

1. The theorem scope is exceptionally well controlled: the paper proves exactly the frozen complete-cyclic families and explicitly refuses broader reducible, return-edge, incomplete-block, or arbitrary transient-feeder claims.
2. The main arguments are genuinely self-contained: exact cylinder counts, finite unions, and a compatible uniform measure carry the dimension results without importing external equality clauses.
3. The saturation section is precise and correctly quantified: universal sufficiency, Fourier-qualified necessity, and the mandatory nondivisible witness are separated exactly as they should be.
4. The deeper-chain result is mathematically substantive: it keeps the exact \(d^L\) denominator, proves monotonicity by the integer embedding \(m\mapsto dm\), and gives an explicit balanced \(O(d^{-L})\) rate.
5. The four-state example is minimal and well used: it refutes the intended cyclic-essential-SCC maximum formula without pretending to settle arbitrary reducible Hausdorff dimension.
6. The reproducibility layer is strong and appropriately subordinate: exact verification supports bookkeeping, falsification controls, and independent audits without being used as proof.

5. **Remaining weaknesses, ranked and tagged CRITICAL, MAJOR, or MINOR**

No remaining weaknesses identified at the CRITICAL, MAJOR, or MINOR level in the revised round-1 manuscript.

6. **For every CRITICAL or MAJOR weakness, a minimal, concrete, globally consistent fix tied to exact section/equation/theorem locations**

No CRITICAL or MAJOR weaknesses remain, so no mandatory fix is requested.

7. **Missing or incorrect references, if any**

- **Required:** None identified.
- **Optional:** A standard Frostman/mass-distribution citation could be added only if a target journal prefers one for Section 3, Lemma `lem:cylinder-dimension`, but it is not logically necessary because the argument is written out in full.
- The owner-subtraction firewall remains correct: no BLW primitive/equality or external spectral-radius equality needs to be imported.

8. **Exact claims-versus-proof audit covering Q0--Q7, assumptions, metric endpoints, finite unions, core dominance, Fourier quantifiers, the nondivisible witness, the exact d^L denominator, monotonicity, the balanced error bound, restricted-family scope, and the four-state conclusion**

- **Assumptions:** Stable and explicit throughout: \(d\ge 2\), \(p\ge 1\), positive phase sizes, complete cyclic blocks, rooted ordered \(d\)-ary tree, and no return edge. No scope drift is visible.
- **Q0:** Supported. Section 3, Lemma `lem:cylinder-dimension` correctly proves the liminf cylinder formula for the equiprobable strata actually used in the paper.
- **Q1:** Supported. Section 4, Theorem `thm:core` derives \(\dim_H T_{C(a)}=\min_j H_j(c)\) from exact prefix counts and the backward-index weighted-limit lemma.
- **Q2:** Supported. Section 4, Proposition `prop:fixed-one-level` and Theorem `thm:one-level` correctly pass from ordered assignments to compositions via a finite union and prove feeder dominance over core-root strata by concentrated compositions.
- **Q3:** Supported. Section 5, Theorem `thm:saturation` proves the spectral-mean upper bound and the exact equivalence with constant circular convolution and shifted integer-product equality.
- **Q4:** Supported with the stated extra hypothesis. Section 5, Theorem `thm:fourier-divisibility` gets the quantifiers right: sufficiency is universal, necessity is only under full nonzero Fourier support, and Example `ex:nondivisible` correctly blocks any unconditional converse.
- **Q5:** Supported. Section 6, Theorem `thm:two-phase` gives the closed parity-sensitive formulas and treats the \(\delta=0\) boundary correctly.
- **Q6:** Supported. Section 7, Theorems `thm:deep-exact` and `thm:deep-convergence` prove the exact denominator \(d^L\), the monotone embedding, the upper bound by \(\bar c\), and the explicit balanced \(O(d^{-L})\) gap estimate.
- **Q7:** Supported. Section 8, Corollary `cor:four-state` correctly derives \(\log 2/3\) for the cyclic core and \(\log 2/2\) for the full shift, and the concluding claim is properly limited to falsifying the cyclic-essential-SCC maximum formula.
- **Metric endpoints:** Correct. The closed-ball interval \([e^{-|\Delta_n|},e^{-|\Delta_{n-1}|})\) is handled with the right inclusion/exclusion direction in Section 3 and Appendix A.
- **Finite unions:** Correctly used only over finitely many root-phase strata, ordered assignments, or fixed-depth compositions.
- **Core dominance:** Explicitly proved at one level by concentrated compositions and at depth \(L\) by concentrated controls plus monotonicity.
- **Fourier quantifiers:** Correctly stated and maintained; the manuscript never upgrades qualified necessity to an unconditional iff.
- **Nondivisible witness:** Correct mathematically and now typeset cleanly.
- **Exact \(d^L\) denominator:** Proved from the ratio \(|\Delta_{n-L}|/|\Delta_n|\to d^{-L}\), not inferred heuristically.
- **Monotonicity:** Correctly comes from \(D_{K+1}(dm;c)=D_K(m;c)\), not from a continuous relaxation.
- **Balanced error bound:** Correct within the frozen hypotheses and used only as a certificate, not as an optimizer claim.
- **Restricted-family scope:** Properly fenced in Proposition `prop:balanced-access`; monotonicity is not inferred without an added nesting condition.
- **Four-state conclusion:** Correctly scoped, with no false generalization to arbitrary reducible matrices.

9. **Figure/table, anonymous A4, and build/QA audit**

- **Figures and tables:** Figure 1 remains an effective mechanism schematic; Figure 2 and Figure 3 are now consistently numbered and honestly captioned; Table 1 and Table 2 are appropriate and non-promotional.
- **Anonymous A4 audit:** Passed. The manuscript remains A4/11pt/article, the author block is `Anonymous Authors`, and there is no identifying prose, acknowledgements, affiliations, grants, or repository link.
- **Build/QA audit:** Passed cleanly. The fixed-epoch round-1 build reports PDF SHA-256 `197a8ed9bd604da16ed7f844fac123bcc60b13e75e40c3b810583f62eacdd11b`, 19 pages, A4, `warning_lines=0`, zero undefined references/citations, and embedded fonts. The production layer is now consistent with the manuscript’s claimed reproducibility standard.

ROUND2_REVIEW_COMPLETE

</details>

Raw-review SHA-256: `39c75656329d1ee7e5a246ec661041c2a8e562ee8c7fd955a9c282224326a9f7`.
Raw-event SHA-256: `1dfd21b3cb68af0a2ba99a94c0ceec8dfdd34e4dec9941e4ae15449506dc2944`.

### Fixes implemented

The reviewer identified no remaining CRITICAL, MAJOR, or MINOR weakness, so no
mathematical or expository source was changed after the review.  The closure
build did expose pdfTeX's run-dependent trailer identifier; the preamble now
suppresses that nonsemantic identifier so fixed-epoch clean builds are
byte-identical.  This production-only change does not alter rendered content.

## Post-independent-audit production repair

The pre-reaudit PDF anchor
`b7a7fab18f3d3bd9bd87eddf02ea2003fb91a96b6ec3731f6e1b32b448f89d5b`
and package-manifest anchor
`1febd58af420c8bdc7d8b7e44577590f461ad3022a6a745d8e2b5294fa761d83`
are withdrawn.  An independent audit found ten XML-illegal C0 characters in
raw Poppler bbox XHTML because eight used extensible-delimiter glyphs lacked
explicit ToUnicode mappings; the earlier verifier had incorrectly sanitized
those characters before parsing.

The preamble now maps the eight audited delimiter glyphs to real Unicode and
maps every additional Latin Modern delimiter piece exposed by the expanded
C0/DEL/C1/U+FFFD/PUA gate.  The verifier now scans default, layout, raw, bbox,
bbox-layout, and PyMuPDF extraction without sanitization and parses both raw
bbox XML streams fail-closed.  Fresh fixed-epoch A/B and official builds are
byte-identical at SHA-256
`aa2a5df28cd7139d9e19aea9bb035cd03f5d787e36260d8a52ed2d33ead930a4`.
All nineteen page rasters, including affected pages 4, 5, 6, and 9, are
pixel-identical to the reviewed rendering.  The theorem and exposition files,
figures, frozen inputs, and review artifacts are unchanged.

The repaired package is held at
`HOLD_FOR_FRESH_INDEPENDENT_WRITER_REAUDIT`; neither prior manuscript review is
reopened or represented as an audit of the production repair.

## PDF history and active repair

- `main_round0_original.pdf` --- original generated paper; SHA-256
  `c54005bd446d6d2ced854bcc519626131f7cb6374e04d119dfa046789bb0ccac`.
- `main_round1.pdf` --- after Round 1 fixes; SHA-256
  `197a8ed9bd604da16ed7f844fac123bcc60b13e75e40c3b810583f62eacdd11b`.
- withdrawn pre-reaudit Round 2 anchor --- SHA-256
  `b7a7fab18f3d3bd9bd87eddf02ea2003fb91a96b6ec3731f6e1b32b448f89d5b`;
  retained as history, not as an active manuscript.
- `main_round2.pdf` --- repaired active manuscript awaiting fresh independent
  re-audit; SHA-256
  `aa2a5df28cd7139d9e19aea9bb035cd03f5d787e36260d8a52ed2d33ead930a4`.

## Final writer closure

The fresh independent writer re-audit subsequently returned its exact
pre-install verdict `WRITER PRE-INSTALL CLEAN` with manifest SHA-256
`3c883d01ad29874b91c70393b43b60661ea5bbe2bbf0040187d1e7cc61aa9041`.
The independently owned authority post-output audit returned
`P49 INDEPENDENT POST-OUTPUT CLEAN` with result SHA-256
`9f4a9d308e71671be29240f1864fb640ceb6e67b8b72e6b185d72748b005b671`.
Those are quoted upstream audit outcomes, not a writer-side installation
claim.  The minimal `FINAL_WRITER_OVERLAY` binds both audit records, the
protected Stage-A capture, and two new fixed-epoch build lanes.  Its exact
writer status is `HOLD_FOR_INDEPENDENT_WRITER_AUDIT`.
