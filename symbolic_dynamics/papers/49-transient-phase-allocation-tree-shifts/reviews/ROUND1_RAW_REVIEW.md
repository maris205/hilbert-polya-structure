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