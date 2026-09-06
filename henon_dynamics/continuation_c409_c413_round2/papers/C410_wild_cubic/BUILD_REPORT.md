# C410 author build report

Date: 2026-09-06. Status: **AUTHOR BUILD PASS**.

This is the initial author build, not the final independent manuscript review
or the batch owner's two-clean-directory reproducibility certificate.

## Deliverables

- `main.tex`, `math_commands.tex`, `references.bib`.
- Nine inputs in `sections/`, including the abstract and eight numbered
  sections; all are referenced by `main.tex`.
- `main.pdf`: 13 pages, 407,977 bytes.
- `PAPER_PLAN.md`, `CITATION_AUDIT.md`, `AUTHOR_REVERSE_OUTLINE.md`.
- Native build artifacts in `build_author/`, including the final log,
  BibTeX log, text extraction and page renders.

The title is *Wild cubic inverse-image towers in characteristic three*.
`Anonymous Authors` is a deliberate neutral byline: no author identities,
affiliations, acknowledgments, or funding were invented.

## Build environment and command

Tools found: `pdflatex`, `latexmk`, `bibtex`, `pdfinfo`, `pdffonts`,
`pdftotext` and `pdftoppm`.

- pdfTeX: `3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)`.
- latexmk: `4.76`.
- Document: 11-point `article`, one-inch margins, Latin Modern Type 1 fonts,
  numeric `natbib`, `plainnat` bibliography.
- No journal/conference template or page cap was supplied. The ML-specific
  example page limits in the compilation skill were not imposed on this
  mathematical article.

```bash
env SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -file-line-error -outdir=build_author main.tex
```

PDF creation/modification dates and trailer identifiers are suppressed in the
source to support the batch owner's subsequent clean-build comparison.

## Build history

1. Initial compilation stopped at `sections/7_ramification.tex`, at the end
   of the Riemann--Hurwitz `align*`. The underlying error was a missing
   backslash before `left`. `build_author/attempt1_failed.log` preserves
   the initial failure evidence.
2. After that one-character source correction, latexmk completed its normal
   LaTeX/BibTeX passes successfully and produced a 13-page PDF.
3. Author source inspection then corrected a stray comma in the exponent
   for the threefold product defining `E_n`. The final verification build
   succeeded. No further compile-fix attempts were needed.

Initial-pass undefined-citation and undefined-label messages are not final
errors: they disappeared after BibTeX and the normal reference-resolution
passes. The retained first failure log is intentionally not represented as
the final clean log.

## Final checks actually performed

| Check | Result |
|---|---|
| `latexmk` exit status | 0; all targets up to date |
| `pdfinfo` | Valid unencrypted PDF 1.5, 13 letter-size pages |
| Main body versus references | Conclusion ends on page 12; references occupy page 13 |
| Final `.log` and `.blg` scan | No Warning, Error, undefined, multiply-defined, Overfull or Underfull matches |
| Font inspection | All 26 font-object rows are embedded/subset Type 1; no Type 3 fonts |
| Text extraction | Successful with `pdftotext -layout`; no unresolved reference/citation placeholders seen |
| Visual inspection | All pages 1--13 rendered at 85 dpi with `pdftoppm` and individually viewed |
| Page layout | No clipped formulas, overlaps, blank pages, missing glyphs or table overflow observed |
| Citation coverage | Six cited entries, checked in the separate citation ledger |
| Source wiring | All nine section files included, none orphaned |
| Root PDF | Copied from the final generated `build_author/main.pdf` |

The visual inspection covered the title/abstract, all three theorem statements,
the complete proofs, the derived table, the scope conclusion and all references.
Some lemma statements/proofs continue naturally across pages; no mathematical
content was removed to avoid those ordinary page breaks.

## Final artifact hashes

```text
9d16aa8a475bf2eca95ca95f768d62a8525b2f352afb868deea88c48114c745a  main.pdf
5928dfba0c047a381bba7f0b087d47dfa4fa34033351414a14f693bd31d40b23  main.tex
79a4656e2a9eca557a042b2183721317576841a8437fcd07bced38e70adf6c92  references.bib
```

## Handoff boundary

Author-side assembly, citation checking, reverse-outline checking and initial
compilation are complete. A non-author must now review the actual complete
manuscript. The batch owner retains responsibility for the final clean builds,
reproducibility comparison, shared evaluation files and Git operations.

## Post-review source precision revision

The coordinator-selected optional root-distinctness clarification from the
non-author full-manuscript review was implemented in
`sections/3_normal_form.tex`; `REVISION_NOTES.md` records the exact change.
The theorem and all computed invariants are unchanged. The original reviewer
will check the affected paragraph. This is a source-only revision: the
13-page author PDF and its hash above describe the earlier reviewed build,
not a rebuild of this final paragraph. The coordinator's pending fresh
builds must compile the revised source before final PDF delivery.
