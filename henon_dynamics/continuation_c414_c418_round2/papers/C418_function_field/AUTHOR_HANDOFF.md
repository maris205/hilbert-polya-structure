# C418 author manuscript handoff

Status: **COMPLETE_AUTHOR_DRAFT; NONAUTHOR_MANUSCRIPT_REVIEW_PENDING**.
This is not a final release, deterministic double-build certificate,
Route A evaluation or independent review of an authored manuscript.

## Payload and exact argument

`main.tex`, seven included section files, `references.bib`,
`CITATION_AUDIT.md` and the actual nine-page `main.pdf` form the draft.
The section plan is the frozen C418 plan in `../../BATCH_PLAN.md`.
All proof steps are typeset in the article itself, including finite
pole integrality, across-cycle common degree, unique C / P up to sign,
the exact injective signed graph, seven least-state cases, ordinary
period lift, every row collision and sharp 14/8/6 counts. Table 3 gives
explicit common-P coordinate words for all fourteen equality points;
it is a direct expansion of the already proved reconstruction rule.

The full 489-line proof and complete nonauthor review/source audit
were read before writing. No old proof or diagnostic was modified or
rerun. Author clarity checks included reading the complete extracted
PDF text, comparing every claim in the frozen matrix with its proof
section, and reading section/paragraph topic sentences in sequence.
The abstract was tightened to say P or -P plus a constant rather than
ambiguously implying only two fixed translates. This does not change
the family or theorem. No unfinished sections or bibliography markers
remain, and every section file is included by main.tex.

## Actual author build and checks

Working directory: this manuscript directory. Command, each call exit 0:

```sh
env SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build_author main.tex
```

There were three successful author invocations: initial compilation
(with ordinary first-pass unresolved references resolved by latexmk),
one shorter paragraph heading to remove a 14.81087pt overfull box,
and the abstract wording correction above. The last TeX log is retained
at `build_author/main.log`, with BibTeX evidence in `main.blg`/`main.bbl`.
The author output was copied without replacing any existing file to
`main.pdf`. Its current size is 341957 bytes, nine pages.

Observed tools: latexmk 4.76 (20 November 2021); pdfTeX
3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian); BibTeX 0.99d.
The final `rg` scan of TeX/BibTeX logs reports no Warning, undefined,
Overfull or Underfull matches; its only selected line is the PDF output.
`pdffonts main.pdf` lists twenty fonts, all embedded/subset with Unicode
maps, no Type 3 fonts. `pdftotext -layout` successfully extracted and
the author read the full nine pages before the local abstract precision
edit. Final visual inspection remains a release gate, not a claim here.

| Artifact at handoff | SHA256 |
|---|---|
| main.tex | `dade97cf4fbf9ddb22cd35d3766242d100b666eb1cbc81937c0d8ce7d8de7084` |
| references.bib | `21284d37d84251e0530839c58c4194d2e4cac12cdd8ddf871b37da450ec6284b` |
| main.pdf | `0c9d6c53a422b8a8733cfaab68afdc0b60daedec57c46468973e63e1d844ac6e` |
| build_author/main.log | `9b806d48c3a513abe6635e237888ee74235dfc9f2ae47a0b3b0e993cab933422` |
| build_author/main.bbl | `4cac74846f5ca57bb5c756f7b46114c5cc52b7b5eebd24f9ea88df5cb84b296b` |
| build_author/main.blg | `a4630bbf295d7118387f0e49a72545c3b604ee72956279749f7a6799494fd3da` |

## Remaining gates

An independent current-team reader must check the actual complete
TeX/Bib/PDF against the proof and accessed-source limits, including
the explicit equality-coordinate table. Root owns adjudication,
the pinned evaluation, final two fresh deterministic builds,
all-page visual review and release sealing/Git. No target Euler,
root-number, automorphy or divisor correspondence is inferred.
