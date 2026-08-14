# Compilation Report — Paper25 / SD-C27

**Artifact:** `main.pdf`  
**Final build date:** 2026-08-14  
**Engine:** pdfTeX 1.40.22 / LaTeX2e (TeX Live 2022)  
**Bibliography:** BibTeX 0.99d with `plainnat`  
**Paper size:** A4, \(595.276\times841.89\) pt  
**Page count:** 21  
**File size:** 511,033 bytes  
**SHA-256:** `e46c31da3517272080800a074a516dfc558c425fafb455618c25acf44928ac28`

## Clean build sequence

Pre-existing auxiliary products and the prior PDF were moved to a recoverable
temporary directory before the final source build.  `latexmk` is not
installed in the environment, so the explicit sequence was used:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

One final stability pass produced the same page count and file size with no
changed-label, citation, or reference warning.

## Automated audit

- Final `main.log`: zero LaTeX/package warnings, zero overfull or underfull
  boxes, zero undefined references, and zero multiply-defined labels.
- Final `main.blg`: zero BibTeX warnings.
- Text extraction: no unresolved-reference marker, drafting placeholder,
  `TODO`, or `TBD` string.
- Abstract length: 216 source words, inside the frozen 150–250-word target.
- Fonts: every font reported by `pdffonts` is embedded and subsetted.
- Metadata: title, subject, keywords, and anonymous author are present.
- PDF properties: unencrypted, no JavaScript, no form content, and A4 page
  geometry.

## Visual audit

Raster inspections were made at 130–140 dpi for:

- page 3, the local-escape/global-collapse hero diagram;
- page 13, the shared/disjoint and digit/return ownership diagram;
- page 15, the exact-evidence table and implementation integrity paragraph;
- page 16, the strict route table and Paper26 obligation.

The initial figure render exposed overlapping annotation labels.  The TikZ
layout was revised and rechecked.  In the final render, node text, arrows,
captions, equations, table rules, margins, and the route tuple are legible
with no clipping or overlap.  Both figures remain vector TikZ artifacts.

## Scientific consistency audit

The compiled manuscript and source packages consistently distinguish:

1. ordinary degree-zero and degree-one Fredholm determinants from their
   graded/relative quotient;
2. the ordinary ungraded block product from the graded ratio;
3. one shared recurrent disk from one recurrent disk per supplied label;
4. original binary digit marker \(u^{\ell(n)}\) from induced completed-return
   marker \(z\);
5. exact finite polynomial cohomology from the infinite Bergman fixed-word
   trace proof;
6. the ordinary tensor-fiber obstruction from any unsupported universal
   nontensor or anisotropic no-go.

The tuple is identical in the source lock, manuscript, result summary, and
narrative:

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

## Integrated exact evidence

The manuscript reports the independently finalized 53/53 exact test result,
4,095 code branches plus the 4,096-word prefix certificate, 3,066 scalar
rows, 40 chain/characteristic rows, 320 supertrace rows, 21 shared/disjoint
determinant rows and 168 shared/disjoint power rows on the first four labels
of each finite fixture, 1,183 primitive necklaces
with all 1,174 mixed rows surviving, 42 arbitrary-inventory controls, 4,095
marker rows, and 21 nuclearity rows.

The 42 controls use full-inventory sums and \(z=1\) products at their frozen
cutoffs.  The experiment runner produced two fresh byte-identical 30-artifact
code/results snapshots with SHA-256
`be46c96d2b9472b301e56c4b99c8f0654b00d13ed6ad9a826ef4d43297fbc36e`;
its 32-entry SHA ledger passed.  That certificate does not cover manuscript
or documentation files.  These computations corroborate exact formulas and
ownership firewalls; they do not replace the infinite proofs or expand the
theorem class.  No target-zero or target-root data were used.

## Cleanup

After this audit, auxiliary LaTeX products are moved out of the authority
directory.  The retained authority build artifacts are the modular sources,
bibliography, TikZ figures, `main.tex`, and `main.pdf`.
