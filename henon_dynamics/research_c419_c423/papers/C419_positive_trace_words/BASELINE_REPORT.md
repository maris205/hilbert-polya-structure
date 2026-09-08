# C419 actual manuscript baseline

2026-09-08 UTC. This is an author preparation/build receipt, not either
independent manuscript review or the final deterministic release pair.

## Actual inputs and outputs

The article has fourteen production TeX/Bib inputs: main file, macros,
bibliography, nine section files and two separately input tables. Two
additional tables are inline in Section 5. Every central proof is typeset.
The line families are displayed equations, not a fifth table.

First successful PDF: [builds/baseline/main.pdf](builds/baseline/main.pdf),
11 pages, 346190 bytes, SHA256
9e163b6d99912a3f604ac1322e489943689c4b075dede46c56957b2e97d8c9a8.
Its fourteen sources were preserved under snapshots/baseline before polish.
The actual first build exited 0 but reported two underfull table paragraphs
and one 7.6 pt overfull paragraph. No failed build is hidden.

The author then changed the source-comparison table columns to ragged-right
and replaced the unbreakable phrase “proof/source” with “proof and source”.
Neither change modifies mathematics. A new directory was used for the build.
Current review baseline: [builds/author_polished/main.pdf](builds/author_polished/main.pdf),
11 pages, 345991 bytes, SHA256
ed7db89ae850acb7530c11c703359faaee15f8dd3d4fe7e4a4ae2c59cb3146a0.

Each actual invocation used latexmk -pdf -interaction=nonstopmode
-halt-on-error -file-line-error with its own output directory. Each exited
0 after three pdflatex and two BibTeX runs. The polished build additionally
set SOURCE_DATE_EPOCH=1788825600, FORCE_SOURCE_DATE=1, TZ=UTC, LC_ALL=C.
The two differently sourced builds are not claimed as a reproducibility pair.

## Actual author inspection

The complete extracted text of all eleven polished pages was read. All
eleven 90 dpi page PNGs were then visually inspected, including the wide
low-level table on page 8 and the bibliography on page 11: no visible
overlap, clipping or unreadable mathematics was found. The final log has
zero warning, undefined citation/reference, overfull or underfull matches.
All nineteen pdffonts rows are Type 1 and embedded, subset and Unicode-mapped.
These are baseline inspections, not a claim to have checked future final pages.

The historical classifier and helper were copied byte-for-byte to
[supplement/](supplement/README.md). Their original finite check receipt is
retained with two relative links adjusted for relocation and explicitly
historical status. No mathematical program was rerun during manuscript
preparation. The helper's later 45-line diagnostic is not the exact
39-line classifier used in the theorem.

## Remaining gates

Two genuine nonauthor full-manuscript passes and coordinator adjudication;
actual responses/revisions if requested; formal evaluation; two fresh final
build directories on identical approved inputs; every final page inspection;
and exact payload release. None is replaced by this baseline receipt.
