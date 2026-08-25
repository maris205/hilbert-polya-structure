# C141 paper improvement log

This log records two real **internal** theorem/scope audits performed during package construction. They are not external peer review, and no numerical review score is asserted.

## Round 0 — baseline draft

Status: compiled and preserved as `paper/main_round0_original.pdf` (2 pages).

Frozen audit questions:

- Does the paper derive the branch signs and the \(m=2\) trace denominator correctly?
- Does it prove that inverse words exhaust all roots, rather than only construct some roots?
- Are \(m=0,1\) true operator controls rather than numerical coincidences?
- Does the primitive product begin at \(k=2\)?
- Is raw-product convergence kept inside \(|u|<4\)?

## Round 1 — internal theorem audit

Status: completed against the baseline PDF, `THEOREM_PACKAGE.md`, and the canonical evidence. This was an internal construction audit, not external review.

Findings and edits:

1. **Multiplier bridge needed to be explicit.** The proof used the inverse contraction to infer simple forward roots but did not print the identity. Added \(\psi_w'(p)=\Lambda_n(p)^{-1}\).
2. **Orbit regrouping multiplicity was implicit.** Added that a primitive orbit contributes at each of its \(\ell(p)\) rooted points when \(n=r\ell(p)\), cancelling the period factor in the trace logarithm.
3. **Absolute convergence object was underspecified.** Changed “absolute factor sum” to the sum of absolute values of the factor deviations, matching the majorant actually proved.
4. **Layout defect.** The exact receipt created a 38.8pt overfull box. Replaced slash fractions by compact stacked fractions and reduced the table type size without changing any value.

Mathematical outcome: theorem retained; no formula or scope claim was weakened or enlarged.

## Round 2 — internal scope/reproducibility audit

Status: completed after text extraction and visual inspection of both pages of round 1. This was an internal construction audit, not external review.

Findings and edits:

1. **Legibility rather than overflow.** Round 1 removed every overfull box, but the degree-five and degree-six fractions were too small in a three-column table. Kept rows 1–4 in a readable table and moved rows 5–6 to full-width display equations.
2. **Product convergence language.** Specified that the majorant controls
   factor deviations, gives compact-uniform convergence in `|u|<4`, and
   identifies the product with the Fredholm determinant there by the identity
   theorem.
3. **Product terminology.** Added an explicit statement that the primitive product is source dynamical and is not an arithmetic Euler product.
4. **Evidence anchoring.** Added the leading canonical evidence digest to the reproducibility paragraph, while retaining the full digest in `results/RESULTS.md` and the manifest.
5. **Claim boundary.** Rechecked that the entire Fredholm determinant is not used to globalize the raw product, the \(z^2-2\) negative control is limited to the same owner disk, and A4 remains failed.

Acceptance decision: retain the theorem and strict tuple; proceed to fixed-epoch double compilation, font/warning checks, and a fresh visual audit.
