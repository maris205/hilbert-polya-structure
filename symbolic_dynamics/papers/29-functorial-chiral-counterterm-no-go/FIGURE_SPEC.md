# Figure specification — Paper 29 / SD-C31

All figures are vector TikZ.  They encode theorem structure and categorical dependence, not estimated effect sizes.

## Figure 1 — critical quadratic decomposition

**File:** `figures/quadratic_decomposition.tex`

Display the finite quadratic ledger as three additive boxes:

1. the divergent diagonal germ
   \(2C_\eta\sum p^{-1}\);
2. the absolutely summable diagonal tail
   \(2C_\eta\sum p^{-1-2\eta}\);
3. the absolutely summable mixed phase
   \(M_\eta(t)\).

Arrows show that leading-only subtraction removes box 1, whereas full-diagonal subtraction removes boxes 1 and 2.  A brace identifies their finite scheme shift.  Color is redundant with text labels.

**Claim:** natural divergence cancellation does not select between two explicit finite parts.

## Figure 2 — naturality boundary

**File:** `figures/naturality_boundary.tex`

The upper pipeline runs from pointed isomorphism and order-ideal active-cutoff compatibility to an equivariant compatible Hermitian pair kernel, and then to the weighted-
\(\ell^1\) convergence conditions.  A dashed boundary follows: a normalization axiom is still missing, and nonlocal filtered-tower invariants remain open.

**Claim:** the theorem classifies a scoped quadratic category; it is not a universal naturality theorem.

## Figure 3 — exact control matrix

**File:** `figures/control_matrix.tex`

Rows are standard divisibility, mutated cover, composite-only, generic DAG, and random inventory.  Columns record nonzero mixed Gram pairs, positive/nonzero fourth-order ledger, relabel/cutoff gates where applicable, and the absence of a selective preregistered pair coefficient.  Use check marks plus words rather than color alone.

**Claim:** the local mixed mechanism survives controls and no tested local multiplier separates the arithmetic row.

## Accessibility and integrity

- Every color distinction is paired with a label, symbol, or border style.
- Captions state the inference boundary.
- No numeric prime label is used as a classifier.
- The control figure reports exact counts, not magnitudes or fitted statistics.
- Route rejection is stated in text and not encoded only by red color.
