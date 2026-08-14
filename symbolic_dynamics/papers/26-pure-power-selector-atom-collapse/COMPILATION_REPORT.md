# Compilation Report — Paper26 / SD-C28

**Artifact:** `main.pdf`  
**Final build date:** 2026-08-14  
**Engine:** pdfTeX 1.40.22 / LaTeX2e (TeX Live 2022)  
**Bibliography:** BibTeX 0.99d with `plainnat`  
**Paper size:** A4, \(595.276\times841.89\) pt  
**Page count:** 19  
**File size:** 512,551 bytes  
**SHA-256:** `13007f2e50dda9e77996f6877ee45adf0ff60a81ebb577ad00a2adb4d0e12941`

## Clean build sequence

`latexmk` is unavailable in the environment, so the final bibliography-aware
build used the explicit sequence

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The last pass stabilized at 19 pages and 512,551 bytes with no changed-label,
citation, reference, or rerun warning.

## Automated audit

- Final `main.log`: zero LaTeX/package warnings, zero overfull or underfull
  boxes, zero undefined references or citations, and zero changed-label
  warnings.
- Final `main.blg`: zero BibTeX warnings.
- Source scan over `main.tex`, `math_commands.tex`, every section, and every
  TikZ source: no ASCII control bytes or carriage returns and no unescaped
  command-like `mathbb`, `operatorname`, `ell`, `chi`, `Re`, `prod`, or `sum`
  token in a mathematical context.
- Text extraction: no unresolved-reference marker, drafting placeholder,
  `TODO`, `TBD`, `FIXME`, or raw LaTeX-command residue.
- Citation parity: 16 distinct cited keys and 16 bibliography entries, with
  neither a missing entry nor an orphan entry.
- Abstract length: 209 source words after simple LaTeX stripping, within the
  frozen 150–250-word target.
- Fonts: every font reported by `pdffonts` is Type 1, embedded, and subsetted;
  no Type 3 font occurs.
- Graphics: `pdfimages -list` reports no raster images; all three manuscript
  figures remain vector TikZ.
- Metadata and security: title, subject, keywords, and anonymous author are
  present; the PDF is unencrypted and contains no JavaScript or forms.
- Links: internal `hyperref` navigation is active; the one external annotation
  resolves to the cited Numdam primary record for Béal's 1995 article.

## Visual audit

Raster inspections at 140–150 dpi covered the title/abstract, the three
figures, the character and determinant theorems, the evidence and route
tables, and the final declaration page.  The first render exposed connector
arrowheads entering text in the selector-collapse diagram, a clipped radical
annotation in the character diagram, and a nearly empty final page.  The
TikZ routes and labels were revised and the declarations were reflowed.  In
the final 19-page render, node text, arrows, equations, captions, table rules,
margins, the route tuple, and the last-page declarations are legible without
clipping or overlap.

## Scientific consistency audit

The compiled manuscript keeps the following firewalls explicit:

1. the positive-word selector theorem versus the separate empty-word
   conventions \(\chi_m(\varepsilon)=m\) and \(\chi_m(\varepsilon)=0\);
2. wordwise cyclic traces versus aggregate traces after commuting the color
   variables;
3. ordinary traces and determinants versus the honest even/odd graded ratio;
4. semisimplified virtual-character rigidity versus literal simultaneous
   diagonalization of the representing matrices;
5. the orbitwise reduced-support exterior fiber versus a fixed stationary
   transfer fiber;
6. shared analytic renewal versus the disjoint coordinate-projector atom
   blocks that survive the selector;
7. the original digit marker \(u^{\ell(n)}\) versus the induced completed-return
   marker \(z\);
8. the finite-dimensional character theorem versus the explicit countable
   projector construction on its absolute trace-class domain.

The frozen strict route record is identical in the source lock, manuscript,
proof package, narrative, and exact route evaluation:

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

The central result is correspondingly scoped: a finite stationary even
graded realization with the required trace on every positive word has, in
the semisimple Grothendieck group, one net color character per supplied
color, plus only canceling/dormant sectors; radical extensions are
trace-invisible.  This controls the graded determinant but does not assert
matrix conjugacy or a universal infinite-dimensional theorem.

## Integrated exact evidence

The manuscript reports the independently finalized 58/58 exact-test result
over 51,734 scientific rows: 34,636 projector rows, 15,029 radical-extension
rows, 1,274 graded word checks, 8 Hankel/syntactic checks, 34 aggregate
firewall rows, 12 support-exterior checks, 12 bar/Hochschild checks, 72 local
de Rham checks, 120 tensor-word checks, 21 arbitrary-inventory controls, 511
marker rows, and 5 strict-route gates.  The aggregate block includes 32
commuted-pencil passes and the two noncommutative witnesses
\(\operatorname{Str}(012)=1\) and \(\operatorname{Str}(210)=-1\).

Two fresh runs produced byte-identical code/generated-result snapshots across
27 artifacts, with combined SHA-256
`8dba8bd574f02fd364e5e8ea987f19ba200a003e68edb1c02ee2f65ac77375e4`;
the 29-entry SHA ledger passed.  This certificate covers code and generated
results, not manuscript or documentation files.  The computation checks the
finite formulas and firewalls; it does not replace the theorem proofs or
license analytic continuation.

## Review policy and cleanup

The standing instruction explicitly skipped the manuscript-review loop.
Primary-source, proof, formula, reverse-outline, exact-evidence, build, font,
link, control-byte, and visual audits were retained.  After this report, the
LaTeX auxiliary products are moved to a recoverable temporary directory; the
authority directory retains the modular sources, bibliography, TikZ figures,
`main.tex`, and the final `main.pdf`.
