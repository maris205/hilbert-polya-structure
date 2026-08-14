# Compilation Report — Paper27 / SD-C29

**Artifact:** main.pdf
**Final build date:** 2026-08-14
**Engine:** pdfTeX 1.40.22 / LaTeX2e (TeX Live 2022)
**Bibliography:** BibTeX 0.99d with plainnat
**Paper size:** A4, \(595.276\times841.89\) pt
**Page count:** 20
**File size:** 542,303 bytes
**SHA-256:** b2237df1d7cbaadaeefb0bafb0f54997528251838d5a98a8ea7807fb10522557

## Source lock

The sole mathematical and literature source was
/tmp/paper27_research_package.md, SHA-256
216415568c467d5640b2cbb7e9d1114a625d2854188845296b250338f754b083.
No theorem class, source family, repair, or route claim was added during
manuscript production.

## Clean build sequence

The environment does not provide latexmk, so the bibliography-aware build
used:

~~~text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

Two final stability passes followed the route-table reflow. The last build
stabilized at 20 pages and 542,303 bytes.

## Automated audit

- Final main.log: zero LaTeX/package warnings, zero overfull or underfull
  boxes, zero undefined references or citations, and zero changed-label
  warnings.
- Final main.blg: zero BibTeX warnings.
- Source scan over main.tex, math_commands.tex, every section, every TikZ
  source, and every writer-owned Markdown package: no ASCII control byte or
  carriage return.
- Mathematical-token scan: no unescaped command-like mathbb, operatorname,
  ell, zeta, mu, varepsilon, Re, prod, or sum token in a mathematical
  context. Tight sum/product spellings were normalized before the final build.
- Text extraction: no unresolved-reference marker, drafting placeholder,
  TODO, TBD, FIXME, VERIFY, or raw LaTeX command residue.
- Citation parity: 15 distinct cited keys and 15 bibliography entries, with
  neither a missing entry nor an orphan entry.
- Abstract length: 218 source words after simple LaTeX stripping, within the
  frozen 150–250-word target.
- Fonts: every font reported by pdffonts is embedded and subsetted Type 1;
  no Type 3 font occurs.
- Graphics: pdfimages reports no raster image. All three manuscript figures
  remain vector TikZ.
- Metadata and security: title, subject, keywords, and anonymous author are
  present; the PDF is A4, unencrypted, and contains no JavaScript or forms.
- Hyperref internal navigation is active. The final PDF has no external URL
  annotation.

## Visual audit

Raster inspection at 140–150 dpi covered:

- page 1, title, abstract, research-status box, and opening equation;
- page 3, the source/compiler/collapse hero diagram and route tuple;
- page 7, the oblique/coordinate similarity firewall;
- page 12, the analytic-domain diagram and exact-evidence opening;
- pages 13–14, the exact tables and five-gate route table;
- pages 19–20, the ownership ledger and declarations.

The initial render exposed an overlong monospaced A0 gate label. It was given
a semantic two-line break and re-rendered. Figure connectors, node text,
equations, captions, table rules, route labels, margins, and final
declarations are legible without clipping or overlap. Color status labels
remain paired with textual labels.

## Scientific consistency audit

The compiled paper keeps these boundaries explicit:

1. source-derived covers versus a supplied prime/color projector inventory;
2. incidence compilation of all coordinates versus atom selection by the
   cover predicate;
3. the composite source letter \(p^r\) versus the temporal repetition
   \(p,p,\ldots,p\);
4. wordwise annihilation before trace versus scalar aggregation after
   commuting variables;
5. ordinary Fredholm determinants versus their honest even/odd graded ratio;
6. individual trace-class projectors for \(\eta>1/2\) versus bounded global
   similarity only for \(\eta>1\);
7. the completed-return marker \(z^r\) versus the original digit marker
   \(u^{r\ell(p)}\);
8. scalar continuation of the product versus same-object operator
   continuation;
9. ordinary cyclic similarity invariants versus untested adjoint mixed-Gram
   geometry.

The strict route record is identical in the source lock, preregistration,
paper plan, narrative, manuscript, and integrated result summary:

~~~text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
~~~

## Integrated exact evidence

The finalized integration passes 61/61 deterministic regression tests and
records 2,384 exact ledger rows: 2,379 scientific, control, and comparison
rows plus five route gates.

The ledger contains 4 incidence-inverse rows, 30 primitive rows, 900 pair
relations, 256 cover classifications, 1,016 necklace classes, 80 marker
checks, 8 power traces, 4 Fredholm/de Rham rows, 24 weighted-Hilbert rows,
3 bounded-similarity certificates, 2 source-mutation rows, 30
stability/equivariance rows, 13 ablations, 9 comparison rows, and 5 route
gates.

The canonical runner starts from a fresh result directory, fixes
PYTHONHASHSEED=0, and runs generator, tests, and analyzer twice. All 30
compared code/generated-result artifacts are byte identical. The
double-run-certificate SHA-256 is
7050130e3c3f98f1ebc6531aad27094498fe0bceb63ae823249e6e8572a5b386;
the 32-entry ledger passes and has SHA-256
21765990e8cdd418baac8d340ca119aa50c3306fb6a4c7f6cd48c04ef5016b0d.
That certificate covers code and generated results, not manuscript or
documentation. No target-zero data were used.

## Review policy and cleanup

The standing instruction explicitly skipped every manuscript-review loop.
Source, derivation, proof, citation, exact-evidence, compilation, font, link,
control-byte, reverse-outline, and visual audits were retained.

After this report, LaTeX auxiliary products are moved to a recoverable
temporary directory. The authority directory retains the modular sources,
bibliography, vector TikZ figures, main.tex, and final main.pdf.
