# Formal LaTeX/PDF edition

This directory contains the generic, single-column theoretical-working-paper rendering of the Phase-I manuscript. It is intentionally not a journal submission template: the author, affiliation, funding, and competing-interest fields remain human-author placeholders, and the PDF prominently retains its internal-working-paper and nonclaim status.

The associated source-bound reading version is [../manuscript.md](../manuscript.md). The evidence corpus snapshot is `419ee36c1e310469209f7b83c096ec8aea448386` (2026-09-13 UTC); the prose manuscript was not part of that frozen historical corpus.

## Contents

| File | Purpose |
| --- | --- |
| [manuscript.tex](manuscript.tex) | Formal front matter, typography, declarations, and document structure. |
| [body.tex](body.tex) | Typeset body snapshot derived from the Markdown manuscript; it preserves the claims, tables, figure, and project-record keys. |
| [manuscript.pdf](manuscript.pdf) | Compiled formal working-paper PDF. |
| [build.sh](build.sh) | Reproducible two-pass LuaLaTeX build. |

`manuscript.tex` and `body.tex` are the typesetting source for this edition. The Markdown manuscript, evidence map, and citation audit remain the source-bound navigation and provenance record.

## Build

Run the following from this directory:

    ./build.sh

The build requires LuaLaTeX, TeX Gyre Termes/Termes Math, and the `AR PL SungtiL GB` CJK font used for the Chinese abstract. It writes transient artifacts into `build/` and updates the tracked `manuscript.pdf` only after both compilation passes succeed.

The PDF uses internal links from each project-record key (for example, `[P1-KB]`) to the appendix table. It deliberately does not rely on local-file PDF links, since readers often block those links. Exact repository-relative targets remain in the Markdown source and [citation audit](../citation-audit.md).

## Scope boundary

This edition is a presentation conversion, not an independent mathematical review or a new research result. It does not claim a proof of RH, a completed Hilbert--Pólya realization, a prime-power trace formula, a completed-\(\Xi\) determinant identity, or identification of the Riemann zeros. A successful compilation is evidence only of rendering integrity, not of mathematical validity or external peer review.
