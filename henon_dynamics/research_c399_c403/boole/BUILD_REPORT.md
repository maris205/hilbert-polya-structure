# Reviewed research-draft build receipt

Date: 2026-09-05. Output: [paper/main.pdf](paper/main.pdf), **9 pages**, 348,715
bytes. Status: complete unnumbered research manuscript with full proofs;
**not** a C-numbered release, formal Route-A evaluation, five-paper completion,
journal submission, human review or publication-novelty certificate.

## Review and actual revisions

The complete author proof received an independent current-team mathematical
review in [BOOLE_INDEPENDENT_REVIEW.md](../reviews/BOOLE_INDEPENDENT_REVIEW.md).
The manuscript then received the separate full-text/claim/citation comparison
in [BOOLE_MANUSCRIPT_REVIEW.md](../reviews/BOOLE_MANUSCRIPT_REVIEW.md).

The manuscript credits Mendoza–Ruiz's prepole domain and the covered unweighted
census consequences. A minor abstract correction replaced the ambiguous
“only after” with the exact statement that the specified compensation works
and the unreduced family does not. The dilogarithm is now named in the abstract
and the Mendoza theorem locators are explicit. The reviewer rechecked those
affected passages and hashes; no mathematical formula changed. The original
proof and numerical checker were not rewritten or rerun for these prose edits.

## Two clean deterministic builds

Working directory for each command:
`henon_dynamics/research_c399_c403/boole/paper/` under the repository root.
The two output directories were created separately by `mktemp -d` and were
empty before the builds.

```sh
env SOURCE_DATE_EPOCH=1788566400 FORCE_SOURCE_DATE=1 TZ=UTC \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/tmp/boole-final-a.k1Kqyg main.tex
env SOURCE_DATE_EPOCH=1788566400 FORCE_SOURCE_DATE=1 TZ=UTC \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/tmp/boole-final-b.6bePHF main.tex
cmp /tmp/boole-final-a.k1Kqyg/main.pdf /tmp/boole-final-b.6bePHF/main.pdf
```

Both `latexmk` processes exited **0**; `cmp` exited **0**. Each normal fresh
build used bibliography/cross-reference passes until resolved. The source
suppresses PDF date and trailer-ID fields; the document itself has a fixed
explicit date. This is byte reproducibility for these inputs and environment,
not a claim that every TeX distribution produces identical bytes.

Environment observed: Latexmk 4.76; pdfTeX 3.141592653-2.6-1.40.22,
TeX Live 2022/dev/Debian; LaTeX2e 2021-11-15 patch level 1; BibTeX 0.99d.
No package installation or system-setting change was performed.

| Generated artifact | SHA256 |
|---|---|
| Both fresh PDFs and saved `paper/main.pdf` | `5b4a42a5b16a06c496f5326a6cdd16abe550357a36f0b5b059c637f62e105f0a` |
| [build/compile-a.log](build/compile-a.log), final engine pass | `59102ae09ea765042626ce50b32ef50ecef926e1af22380b77b79ec4e8ace803` |
| [build/compile-b.log](build/compile-b.log), final engine pass | `3ed39c6ae3e50dbd072dd7b51bf06601d06fd39a52f4b263edcad18498c165e7` |

The log hashes differ because they record the different temporary paths.
Only the PDF bytes are asserted identical. These logs are actual final engine
logs, not fabricated or a claim to archive every earlier stdout line.

## Output checks actually performed

- `pdfinfo`: 9 pages, 348,715 bytes, unencrypted PDF 1.5, US letter pages.
  The main text ends on page 8; references occupy page 9. No venue page limit
  was imposed or represented as checked.
- A search of **both final engine logs** for `Warning`, `Overfull`, `Underfull`,
  `undefined`, and `multiply defined` returned no matches (the expected `rg`
  exit code is 1). Early fresh-build unresolved references were resolved by
  the normal later passes; they were not hidden or counted as final warnings.
- `pdffonts` on the final PDF: all 21 font rows embedded, subsetted, and with
  Unicode maps. No missing-font claim is inferred merely from successful TeX.
- `pdftotext` succeeded; a full extracted-text search found no `??`, `[?]`,
  `TODO`, `FIXME`, or `[VERIFY]` markers. This search is not a mathematical proof.
- `pdftoppm -r 105 -png` rendered every page. The coordinator visually inspected
  pages **1–9 individually**, including all displayed formulas, theorem/case
  layout, references, and page transitions. No text/number overlap, missing
  glyph, clipping, or blank-content page was observed. The reference-only
  final page is intentional, not padding to satisfy a quota.
- All seven section files are included by `main.tex`. Three bibliography
  entries support all four actual citation contexts, as checked in the
  independent manuscript review; no orphan bibliography entry was found.

## Exact final manuscript inputs

Paths below are relative to `paper/`. These ten files are the complete authored
TeX/BibTeX input set; class/package/font files come from the environment above.

| Input | SHA256 |
|---|---|
| `main.tex` | `3c0ac8773f090e4128cf72ae472c641ae38e506eaaa8ad23bc33cf0e63e90d10` |
| `math_commands.tex` | `146265b3722a829eb228c421706e8132f6a5b00e8e30fb0dbbab064d812e6ea2` |
| `references.bib` | `5e151da1071901897c890144bca159ab50247e502abc583f5548f78fb18763d1` |
| `sections/0_abstract.tex` | `b84e3afb9584f29828acf478bb0a40d89ffb6e168bce83496c8d6668c43c5fd0` |
| `sections/1_introduction.tex` | `d8d34e93f82e3679a934ec4aa99f62c4a2885757e381d58f587275d2edc77d8c` |
| `sections/2_dynamics.tex` | `f3ea7b594e34bb57ac75906d724cd5364aadd96b00495db50993f82172b82255` |
| `sections/3_indices.tex` | `6e3c79d7874a9358cddb3c478ee760e193924a5b2b88c06e20726eef2a1b206e` |
| `sections/4_products.tex` | `148fd977b2b55a46d7b341d972d11ad7c755d631b4470f4223bbc72807861e57` |
| `sections/5_critical.tex` | `e4bfceaaf89ddc36bec47d6ed8b7703406dc15b9e6bb424c85caf207fa33dcb5` |
| `sections/6_scope.tex` | `ea86b39414523dc3d00a514b82dfd9801cf651581cd9d308fc2b469bf8913dec` |

The proof snapshot remains
`9ef4c0d8e3beab75e95be19d5a835e4b491392ce1565589997fa213f0296f725`.
The final amended manuscript review is
`347a5768c1b64a92068ce6f18535095176093c3a8b1d119e84890b12ffb703bb`.
Build success and input identity do not establish global novelty or a natural
finite-real transfer operator. Remaining batch admission/evaluation/release
gates are not relabelled as passed by this research-draft receipt.
