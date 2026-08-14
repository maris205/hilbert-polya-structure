# FIGURE SPECIFICATION — SD-C18

## Figure 1: formal lift and incompatibility triangle

**Purpose.** Give a skim reader the complete positive/negative result before
the technical sections.

**Artifact.** `figures/incompatibility_triangle.tex` (native vector TikZ).

## Content

The top node is the formal \(C_2\)-colored Burnside/species ledger.  It
contains the exact \(pqr\) residual

\[
 R_3=\mathbf1+\mathbf{sgn}-\mathbf{Std},
 \qquad \chi=(0,0,3).
\]

Three branches lead to canonical readouts:

1. **Augmentation/dimension:** returns the pure Euler scalar shadow but maps
   \(R_3\) to zero.
2. **Arithmetic specialization:** keeps distinct weights \(x_p=p^{-s}\) but
   turns atom relabeling into semilinear covariance; the fixed operator has
   trivial \(S_n\) stabilizer.
3. **Diagonal subset lift:** keeps representation lines and standard Adams
   powers, but changes \(b(x)^r\) into \(b(x^r)\) and introduces mixed
   superdeterminant factors.

The bottom bar states the model-specific conclusion:

```text
GO formal equivariant ledger
STOP arithmetic character-Fredholm fibers
```

## Visual design

- Width: full text width.
- Format: vector TikZ included directly in LaTeX.
- Palette: dark blue for the positive formal object, amber for the three
  warning branches, charcoal for equations and conclusions.
- Accessibility: every distinction is encoded by label and line style, not
  color alone; the figure remains legible in grayscale.
- No title inside the figure.
- Minimum text size: manuscript `\small`/`\footnotesize`, never below 8 pt.
- No decorative background or 3D effects.

## Caption

The formal \(C_2\)-colored Burnside ledger retains the \(pqr\) residual,
but each canonical analytic readout loses a required property.  Augmentation
kills the residual, distinct prime weights break fixed-fiber \(S_n\)
commutation, and the diagonal subset lift replaces \(b(x)^r\) by
\(b(x^r)\) and adds mixed determinant factors.  Thus formal equivariance is
retained while arithmetic character-Fredholm fibers stop.

## Traceability

```yaml
figure_table_trace:
  - artifact_id: fig-1
    source_data:
      dataset_id: exact-theorem-ledger
      file: PROOF_PACKAGE.md
    transformation:
      manual_derivation: "Theorems 3, 5–8 and 11; TikZ transcription in figures/incompatibility_triangle.tex"
    caption_claim: "The three canonical readouts cannot preserve Euler ledger, fixed arithmetic symmetry, and nontrivial resolved motion simultaneously."
    supported_manuscript_claims:
      - claim: "The formal Burnside ledger retains a nonzero pqr residual."
        locator: "Sections 4 and 6"
      - claim: "Canonical arithmetic character-Fredholm fibers fail for three distinct structural reasons."
        locator: "Sections 5–7"
    limitations:
      - "The diagram summarizes the canonical rank-one and diagonal lifts only."
      - "It does not assert a universal no-go for all equivariant symbolic extensions."
```

## Verification checklist

- [ ] all formulas match `PROOF_PACKAGE.md`;
- [ ] caption is self-contained;
- [ ] no unsupported analytic arrow is drawn;
- [ ] all text fits at A4 manuscript width;
- [ ] PDF fonts remain embedded because the figure is native TikZ;
- [ ] grayscale rendering preserves all branch distinctions.
