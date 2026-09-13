# Round 2 Proposal-Refinement Review

**Review scope:** proposal fidelity, method focus, feasibility, and
claim-driven validation only. This is not the later source-lock correctness,
citation, or proof-completeness review.

**Verdict:** **READY**

**Overall score:** **9.3/10**

The package clears the refinement gate: the weighted score is at least 9,
the Problem Anchor is preserved, the paper has one dominant contribution,
and no proposal-level blocker remains. The independent novelty estimate of
**6.1--6.5/10** is not overridden by this verdict. That estimate measures
external originality and standalone paper mass; the 9.3 score measures how
well the chosen, deliberately scoped proposal has been anchored, specified,
simplified, and made executable.

## Scorecard

| Dimension | Score | Assessment |
|---|---:|---|
| Problem Fidelity | 9.7 | The complete normalized quartic fixed-trace-zero fiber remains the immutable target throughout the batch report, research question, claim matrix, plan, and tracker. The all-\(m\) result explains the quartic recovery mechanism without replacing the anchored problem with a global cutoff claim. |
| Method Specificity | 9.4 | The category, quotient coordinate, cyclic equations, Jacobian trace, trace--residue exponent, weights, two eliminated monomials, coefficient formula, fixed-cycle subtraction, and pointwise/cyclewise conventions are concrete enough to guide proof and implementation. P1--P10 isolate the exact proof obligations. |
| Contribution Quality | 9.2 | The sharp quartic full-fiber/minimal-separator theorem is unmistakably dominant. The uniform two-term law and finite slope certificate are a single supporting mechanism rather than a parallel paper. Mature residue and normal-form tools are correctly treated as prior machinery. |
| Frontier Leverage | 9.5 | This exact algebraic-dynamics problem has no natural LLM/VLM/diffusion/RL role. The explicit decision not to bolt on a frontier component is appropriate; current leverage here means exact quotient, residue, degeneration, and coefficient-extraction methods used at the right interfaces. |
| Feasibility | 8.9 | The quartic target and finite certificate evaluators are bounded exact tasks with no data or accelerator dependence. The main residual mathematical risk is the complete all-\(m\) Puiseux/trace-order lemma in P5, but it is isolated, has a precise failure boundary, and is not concealed by finite checks. |
| Validation Focus | 9.0 | The scientific core is three blocks: quartic fiber/low-period blindness (B2), quartic period-three separation (B3), and the symbolic uniform law/certificate (B4). B1 and B5 are definition and integrity controls, not extra scientific claims. The plan refuses interpolation, scans, and a tie-breaking third engine. |
| Venue Readiness | 8.7 | If the proof closes and the exact audit passes, this is a sharply positioned specialist exact-dynamics note. Venue ambition must remain calibrated to the independent novelty and standalone-size assessments; the package should not be marketed as a global multiplier-rigidity or all-quartic theorem. |

Weighted score using the research-refine weights:

\[
0.15(9.7)+0.25(9.4)+0.25(9.2)+0.15(9.5)
+0.10(8.9)+0.05(9.0)+0.05(8.7)=9.305.
\]

## Required Checks

### Problem Anchor

**Preserved.** The package consistently asks for the first separating formal
period on the complete normalized quartic fixed-trace-zero fiber and for a
degree-uniform algebraic mechanism explaining that recovery. It does not
drift to all quartic Hénon maps, a global value of \(P(4)\), or universal
all-degree separation.

### Contribution focus

**Focused.** The dominant contribution is the quartic full-fiber theorem:
classification of the fiber, exact period-three affine coordinate, and
minimality because periods one and two are blind. The all-\(m\) residue law
and nested-binomial coefficient are properly subordinate: they explain why
the quartic calculation is structural and end at the explicit open
nonvanishing problem. No third contribution should be added.

### Simplicity

**The scientific method is the smallest adequate route.** It reuses
normalized Hénon theory and complete-intersection residue machinery, adds no
trainable or decorative component, and removes numerical root splitting,
interpolation, degree scans, extra families, extra periods, and a third
engine. The long lifecycle registry is governance density rather than method
sprawl. In eventual paper-facing prose, B1/B5 and the R000--R120 lifecycle
should remain appendix/provenance material so that the visible narrative is
the three-block B2--B4 scientific core.

### Nilpotent scheme wording

**Correct and sufficiently careful.** The design does not say that
\(q=p'\) vanishes as an element of the nonreduced fixed algebra. It says that
\(q\) is generally nonzero nilpotent with \(q^2=0\), and interprets
\(0^{\times 2m}\) and \(2^{\times((2m)^2-2m)}\) through multiplication
spectra/formal zero-cycles with scheme multiplicity. That distinction is
essential at \(a=0\) and should be retained verbatim in the manuscript.
Similarly, fixed-cycle subtraction must continue to be described as formal
cycle subtraction, not as discarding reduced fixed points.

### Nonclaims

**Preserved across all reviewed artifacts.** In particular:

- \(D_m\ne0\) for every \(m\ge2\) remains open;
- finite checks do not prove the uniform theorem or nonvanishing;
- period three is not claimed to separate every even-degree family;
- the quartic family and period-one/two blindness are not claimed as new;
- the theorem is not extended to all quartic Hénon maps or to a global
  equality \(P(4)=3\);
- global residues, dynatomic cycles, normal forms, and low-period Hénon
  algebra remain prior machinery;
- no arithmetic, height, saddle-spectrum, or global rigidity conclusion is
  imported.

### Proportionality of \(T_{\mathrm{reg}}=(8,9)\)

**Proportionate as frozen.** Two isolated indices are enough for the stated
implementation-falsification role: they cover even/odd parity and adjacent
\(\lfloor m/2\rfloor\) branches, while the actual all-\(m\) statement remains
proof-derived. The plan also keeps the check cheap by evaluating only the
finite \(H/A/D/E\) certificate, not the high-degree quotient/residue engine.
The tuple must not be enlarged, mined for a trend, or presented as validation
of universal nonvanishing. Conversely, reducing it to one index would lose
one of the two explicitly targeted branch/parity checks without materially
simplifying the audit.

## Remaining Risks and Actions

No item below is a proposal-refinement blocker.

1. **P5 is the decisive proof risk (IMPORTANT for source lock).** The later
   correctness review must verify the full diagonal/non-diagonal Puiseux
   branch partition, valuation bound strictly beyond \(m\), trace descent
   under ramified base change, and absence of contributions at infinity. No
   finite engine agreement can repair a gap there.
2. **Keep the proof/audit boundary visible (MINOR editorial action).** The
   opening method thesis can be read too quickly as though two implementations
   certify the symbolic all-\(m\) theorem. The later clean proposal or paper
   should continue to state in the same paragraph that the source proof proves
   C2 and the finite evaluators only falsify implementation disagreements.
3. **Keep protocol out of the headline story (MINOR simplification).** The
   tracker is appropriately strict, but the paper narrative should present
   B2--B4 first and relegate one-shot lifecycle counters, negative fixtures,
   and manifest machinery to reproducibility/provenance material.

## Simplification Opportunities

- Do not change the mathematical method or add a new mechanism.
- In paper-facing exposition, compress B1 and B5 into one proof-contract and
  scope-integrity paragraph or appendix table; retain the detailed tracker as
  an audit artifact.
- State the two primary claims once near the front, then organize all lemmas
  and checks under the dominant quartic theorem and its supporting uniform
  mechanism.

## Modernization Opportunities

**NONE.** No foundation-model-era primitive is a natural technical answer to
this bottleneck, and adding one would weaken the proposal.

## Drift Warning

**NONE.**

## Blocking Issues

**NONE at the proposal-refinement stage.** This READY verdict does not grant
`SOURCE_LOCK_PASS`, implementation authorization, registered execution, a
correctness certificate, or a stronger novelty claim.
