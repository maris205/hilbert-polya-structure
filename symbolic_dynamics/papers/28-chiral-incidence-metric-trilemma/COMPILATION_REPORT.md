# Compilation report — Paper 28 / SD-C30

**Artifact:** main.pdf
**Final build date:** 2026-08-14
**Engine:** pdfTeX 1.40.22 / LaTeX2e (TeX Live 2022)
**Bibliography:** BibTeX 0.99d with plainnat
**Paper size:** A4, 595.276 by 841.89 pt
**Page count:** 13
**File size:** 447,390 bytes
**SHA-256:** 51095edc8a3e955d01d7158a5efcd7b8f08fe3e46cb8a69d96ffe66d09e56743

## Stable build sequence

The bibliography-aware build used

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

The last pass stabilized at 13 pages and 447,390 bytes.

## Automated audit

- Final main.log and main.blg contain no LaTeX, package, BibTeX,
  overfull-box, underfull-box, undefined-reference, undefined-citation,
  changed-label, or rerun warning. The only matching log text is the
  installed package name rerunfilecheck.
- Text extraction contains no unresolved reference marker, TODO, TBD,
  FIXME, drafting placeholder, or raw citation marker.
- Citation parity is exact: eight distinct cited keys and eight
  bibliography entries, with no orphan entry.
- The abstract has 170 words after detex extraction.
- Every PDF font reported by pdffonts is Type 1, embedded, and subsetted;
  no Type 3 font occurs.
- pdfimages reports zero raster images; all three figures are vector TikZ.
- PDF metadata records the title, subject, keywords, and anonymous author.
  The file is A4, unencrypted, and contains no JavaScript or form.

## Visual audit

All 13 pages were rasterized at 110 dpi. Detailed inspections covered:

1. title, abstract, research-status box, and first equations;
2. the common Schatten-strip figure and its open endpoints;
3. the fourth-frequency proof and metric theorem;
4. the native-versus-metric trilemma diagram;
5. the adversarial table, control matrix, and decimal sample table;
6. the strict route table and boxed tuple;
7. the final proof and scope-declaration page.

The final pages have no clipped equations, overlapping arrows, cropped
captions, table spill, or illegible labels. The route tuple fits within
its box, and the final page is substantively filled.

## Scientific consistency audit

The compiled manuscript keeps the following ownership firewalls explicit:

1. the main critical theorem is the arithmetic specialization \(u=1\);
2. if \(T_s(u)\) is displayed, repetition carries
   \(u^{r\ell(p)}\), and the altered \(|u|<1\) threshold is not
   continuation of the \(u=1\) theorem;
3. the finite \(B^2\) formula is a cutoff diagnostic, while the
   countable critical operator is not Hilbert–Schmidt;
4. the original Euler determinant on \(\Re s>1\) is distinct from the
   chiral third-regularized determinant on \(1/3<\Re s<2/3\);
5. the regularization deletes powers one and two, odd block traces
   vanish, and power four is first visible;
6. native fourth-order motion is exact but survives non-arithmetic
   aggregate controls;
7. positive metric rigidity erases motion by forcing coordinate-atom
   blocks;
8. \(\mathcal B_{1/2+it}\) is a \(t\)-dependent self-adjoint family,
   not a fixed spectral operator;
9. no target-zero datum or Route-B construction is present.

The frozen route is consistent across the source lock, preregistration,
proof package, narrative, manuscript, and scope appendix:

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_FAIL,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

Decision: ROUTE_A_REJECTED. Route B is locked false.

## Frozen exact evidence

- Corrected research package SHA-256:
  68df371e9c8b9a76638b7fdde643d42ba31c84ce13c02ffdb95367986bdff924
- Prototype SHA-256:
  e29553c5a04cb31393b6ef8f93d2718285bac52d956cffc04d4c8d53fc6cc737
- Result JSON SHA-256:
  118ae2e85e4ce8d403673f1d00725520c7137a3a032bb9201cda186a61cb5cfb

Two fresh prototype runs were byte-identical and all exact controls
passed. This certificate covers the frozen prototype and result artifact,
not the theorem proofs.

## Review policy

The standing instruction explicitly skipped a manuscript-review loop.
Proof, formula, source, reverse-outline, literature, exact-evidence,
build, font, metadata, control, and visual audits were retained.
After this report, transient LaTeX auxiliaries are moved to a recoverable
temporary directory; the authority directory retains modular sources,
bibliography, vector figures, main.tex, and the final main.pdf.
