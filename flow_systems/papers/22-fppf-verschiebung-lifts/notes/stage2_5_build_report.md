# P22 Stage-2.5 corrected build report

Date: **2026-08-24**

## Result

**PASS.**  After the two citation-context corrections, the manuscript was
rebuilt with LuaLaTeX/BibTeX and two final LuaLaTeX passes.

| Metric | Result |
|---|---|
| pages | 12 |
| page size | A4 |
| PDF version | 1.5 |
| PDF size | 143,712 bytes |
| citation commands / bibliography entries | 18 / 3 |
| unresolved citations or references | 0 |
| overfull boxes | 0 |
| missing glyphs | 0 |
| fatal errors | 0 |
| embedded/subset fonts | yes |

Two pre-existing underfull-box notices remain in the manually line-broken
Chinese abstract.  They are nonblocking.  Visual inspection of final PDF
pages 1, 3, and 12 confirmed that the corrected source attribution, equation
(20) wording, abstracts, mathematics, and bibliography are legible and free
of clipping or overflow.

## Final artifact hashes

| Artifact | SHA-256 |
|---|---|
| `manuscript.tex` | `5976642a43907a3e01abdb586e9188c697d4a07e7137330a8f285538caaa02fc` |
| `references.bib` | `bd03813691db911316b18620ee4a1d212ac284fce7fb79af9f1b1cbc7ea71093` |
| `paper.bbl` | `4244c70dea32b053dc2df1c1435ebfeccc1e26f93dbe80179a523950ed091156` |
| `paper.log` | `f582825f7eb280b573dac5ff18c9c5dbb6638aea8c9c18189c9c537082f92113` |
| `paper.pdf` | `b106aa48ca5b3906a47691d035c29ed640aca378ed24adb51f29f83264daec3d` |

The PDF and log are newer than both source inputs.  No submission, release,
author contact, or Git action was performed.
