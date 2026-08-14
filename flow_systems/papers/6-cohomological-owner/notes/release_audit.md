# Paper 6 post-build integrity audit

Audit date: **2026-08-13**  
Scope: build, deterministic reproduction, package completeness, and visual
rendering; the independent citation/source audit is recorded separately.

## Verdict

**PASS.**  The paper builds, reproduces,
and satisfies the project contents required by Proposal §12.2.  No manuscript
claim was altered during this post-build audit.

Independent closure is also complete:

- citation/source audit: **ACCEPT**, `notes/citation_audit.md`, SHA-256
  `e6eb0438d15f359dc9f19a05697051eb8acd2dd440437a6931d2f12f6181de22`;
- mathematical/Route/release peer review: **ACCEPT** with no residual required
  minor issue, `notes/peer_review_round1.md`, SHA-256
  `910318c90e1407ceb5350d9fe362bfe1f46912829d275dc03b7f4b7fe1838346`.

## Build record

Command:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

Results:

- XeLaTeX + BibTeX completed successfully.
- PDF: 9 pages, US Letter.
- `paper/paper.pdf` SHA-256:
  `f8eccdd7d486a10885d6f5502ad929f08d5ce27b14cb2457f1de8999b9f14573`.
- `paper/manuscript.tex` SHA-256:
  `d36783ebbfabd67fdda7f04d1aae3556e72b137e51985b7cd6448a35f0cb8219`.
- `paper/references.bib` SHA-256:
  `9cae6271cefad92c78de9a4cb9533fb12503760e11f05b3f06d240cef1c67e05`.
- no undefined citation or reference;
- no overfull box;
- no missing glyph;
- no BibTeX warning or compilation error;
- one nonfatal underfull hbox (`badness 2698`) in the deterministic-controls
  paragraph.

## Reproduction record

`bash experiments/reproduce.sh` completed with 10/10 tests passing and five
of five generated artifacts hash-locked.  The manifest file SHA-256 is
`4a78e430d08134bca09b88b4e5f3adf25b68692212893f6abeaad407d1711c16`.
The run uses exact integer/rational arithmetic and no target-zero data,
fitting, randomness, network data, or floating-point root finder.

## Visual inspection

All nine PDF pages were rendered and inspected at 130 dpi.  Explicit checks
covered:

- page 1: title, author block, English and simplified-Chinese abstracts;
- page 2: native TikZ ownership diagram and opening text;
- pages 3--6: owner table, theorem statements, domains, displayed formulas,
  proof endings, and line wrapping;
- page 7: Route-A/Route-B table and limitations;
- page 8: declarations, artifact map, and bibliography start;
- page 9: remaining bibliography and URL wrapping.

Text, equations, tables, CJK glyphs, URLs, and page numbers are legible, with
no clipping or overlap.  Figure 1 uses a clearly labeled dashed
`no operator bridge` connection; its caption now describes exactly that
visible convention.

## Proposal §12.2 package check

- `README.md`: present;
- `paper/manuscript.tex`: present;
- `paper/references.bib`: present;
- `paper/figures/`: present with native TikZ;
- `paper/paper.pdf`: present;
- `code/`: implementation, tests, and README present;
- `experiments/`: reproduction script and README present;
- `results/`: generated artifacts and README present;
- `notes/`: protocol, source, proof, composition, and release audits present.

## Source metadata correction

The local Teschl PDF hash resolves to the 2009 first edition, GSM 99, not the
2014 second edition.  `notes/source_audit.md` and `paper/references.bib` use
the title-page-confirmed 2009 metadata.  The theorem numbers used in the proof
remain valid, so this integrity correction changes no mathematical result.
