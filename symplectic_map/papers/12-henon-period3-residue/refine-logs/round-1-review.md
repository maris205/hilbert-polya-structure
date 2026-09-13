# Round 1 Review — Historical Quartic-Only Proposal

## Review Scope

This review scores only the historical proposal in `INITIAL_PROPOSAL.md`: the
quartic fixed-trace-zero fiber, the exact period-three moment, and recovery of
the normalized coordinate \(L^3\). It does not credit the later all-\(m\)
residue law or finite coefficient certificate.

## Scorecard

| Dimension | Score | Assessment |
|---|---:|---|
| Problem Fidelity | 10/10 | The proposal answers exactly the anchored question: it identifies the first separating trace period on the complete normalized quartic fixed-trace-zero fiber. It does not drift to all quartic Henon maps or to a global effective-cutoff theorem. |
| Method Specificity | 5/10 | The theorem targets and decisive identity are precise, but the four-step approach mostly says “prove” and “compute.” It does not expose the elimination/residue mechanism, the relevant quotient algebra, how fixed points are removed from the formal-period-three moment, or an independently checkable certificate for the coefficient. |
| Contribution Quality | 5/10 | Recovering \(L^3\) at the minimal period is sharp and intrinsic, but the family and period-one/two blindness are inherited from Cantat--Dujardin. In this form, the new content is concentrated in one quartic elimination identity, while the surrounding formal-period and residue tools are mature. That is too little mathematical mass and too little mechanism for a strong standalone paper. |
| Frontier Leverage | 9/10 | Foundation-model-era machinery is not a natural fit for this pure algebraic-dynamical theorem. The appropriately frontier-aware choice is to avoid artificial ML components and use exact symbolic algebra only as verification, not as the contribution. |
| Feasibility | 8/10 | The quartic fiber classification and exact symbolic calculation are bounded and plausible. Feasibility is reduced only because the proposal omits a proof contract and a second exact route that would distinguish a theorem from an unchecked computer-algebra output. |
| Validation Focus | 5/10 | The proposal names the final formula but gives no minimal validation block: no independent exact engine, fixed-point-subtraction check, pointwise/cyclewise count check, conjugacy-exponent check, or negative control against promoting a fiberwise result to a global one. |
| Venue Readiness | 5/10 | The effective period-three separator is worth recording, but the historical package reads as a compact exact calculation rather than a paper-level structural result. The closest-work distinction is real yet too narrow to carry a top-venue-style standalone paper without a mechanism explaining the quartic identity. |

**Weighted overall score: 6.7/10.**

Using the prescribed weights:


\[
0.15(10)+0.25(5)+0.25(5)+0.15(9)+0.10(8)+0.05(5)+0.05(5)
=6.65\approx6.7.
\]

**Verdict: REVISE.** The READY threshold is not met, and the lack of
standalone mathematical mass/mechanism is a blocking issue.

## Required Fixes for Dimensions Below 7

### Method Specificity — 5/10

- **Specific weakness:** The proposal provides conclusions but not the
  mechanism that produces them. In particular, it gives no cyclic
  complete-intersection model, trace/residue interface, grading or symmetry
  argument, formal-period subtraction step, or finite certificate for the
  coefficient of \(L^3\).
- **Concrete method-level fix:** Build the period-three computation in a
  cyclic quotient with an auxiliary coupling parameter; identify the
  Jacobian determinant representing the derivative trace; state the
  complete-intersection trace-residue identity used to extract the moment;
  use a weight/symmetry argument to restrict the allowed parameter monomials;
  and end with a finite combinatorial coefficient formula that can be checked
  independently. Spell out how the fixed-point component is subtracted and
  how the remaining formal length converts pointwise data to cyclewise data.
- **Priority:** CRITICAL.

### Contribution Quality — 5/10

- **Specific weakness:** The only visibly new object is the quartic identity
  \(S_2^{(3)}(L)=-1296000-1572864L^3\). Because the exceptional family and
  low-period blindness are prior art, this risks being perceived as one
  successful elimination rather than a new structural theorem.
- **Concrete method-level fix:** Keep the quartic separator as the dominant
  theorem, but add the smallest degree-uniform explanation: for
  \(f_{m,a}=(y+(x^m-a)^2,x)\), derive a formal period-three residue law whose
  parameter dependence factors through the normalized quotient coordinate
  \(a^{2m-1}\), together with an explicit finite certificate for its slope.
  Do not require universal nonvanishing of that slope; state it as open. This
  turns the quartic computation into the sharp complete-fiber case of one
  mechanism rather than one isolated identity.
- **Priority:** CRITICAL.

### Validation Focus — 5/10

- **Specific weakness:** There is no claim-driven exact audit separating the
  mathematical theorem from a single symbolic computation.
- **Concrete method-level fix:** Use two independent exact engines for the
  quartic moment and certificate cases, plus targeted negative controls for
  fixed-point subtraction, the exponent \(2m-1\) (hence \(L^3\) at \(m=2\)),
  cyclic signs, formal-period multiplicities, and the forbidden inference
  from finitely many \(m\)-checks to universal nonvanishing. These checks
  should verify the proof contract rather than expand into a benchmark suite.
- **Priority:** IMPORTANT.

### Venue Readiness — 5/10

- **Specific weakness:** The proposal does not yet explain why the period-three
  identity is structurally inevitable or reusable, so its novelty and paper
  size remain below a standalone threshold despite the sharp endpoint.
- **Concrete method-level fix:** Organize the paper around one thesis: a
  degree-uniform trace-residue mechanism explains why period three detects the
  normalized parameter, and the quartic fiber is the first complete case in
  which the coefficient is explicitly nonzero and period three is therefore
  minimal. Treat fiber classification, exact coefficient evaluation, and
  fixed-component subtraction as supporting lemmas, not parallel
  contributions.
- **Priority:** CRITICAL.

## Simplification Opportunities

1. Preserve the quartic minimal-separator theorem as the single headline; do
   not add height, unstable-spectrum, arithmetic-finiteness, prime/zero, or
   global-rigidity directions to manufacture paper size.
2. Reuse standard global-residue and formal-period machinery explicitly as
   tools. Claim novelty only for the specialized uniform law, quotient
   coordinate dependence, finite coefficient certificate, and sharp quartic
   consequence.
3. Make universal slope nonvanishing an explicit nonclaim. The paper needs a
   mechanism and a certified quartic instance, not an unsupported theorem for
   every degree.

## Modernization Opportunities

NONE. No LLM, learned component, or other foundation-model primitive naturally
improves the mathematical claim. Exact computer algebra may support
verification but must not substitute for the residue and symmetry proof.

## Drift Warning

NONE. The historical proposal remains faithful to the normalized quartic
fixed-trace-zero fiber. The required uniform mechanism should explain that
result without changing the headline into a universal separating theorem.

## Concrete Required Refinement

Retain the complete quartic theorem and its exact affine formula, but embed it
in one minimal structural mechanism: derive on
\(f_{m,a}=(y+(x^m-a)^2,x)\) an all-\(m\) formal period-three residue law affine
in the exact normalized coordinate \(a^{2m-1}\), and give a transparent finite
certificate for its slope. Specialize this mechanism at \(m=2\) to certify the
nonzero \(L^3\) coefficient and hence the minimal quartic separator. Explicitly
leave universal slope nonvanishing open and exclude unrelated paper-size
patches.
