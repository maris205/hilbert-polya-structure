# P22 Stage 4 revised-paper build report

Date: **2026-08-25**

## Result

**PASS.**  After the authorized 13-operation revision passed manual semantic-
drift review, the anchored working draft was materialized by removing only
whole-line ARS block markers.  The resulting public source was built in an
isolated staging directory with LuaLaTeX, BibTeX, and two final LuaLaTeX
passes; the validated outputs were then promoted to `paper/`.

| Metric | Result |
|---|---|
| pages | 13 |
| page size | A4 |
| PDF version | 1.5 |
| PDF size | 152,437 bytes |
| citation commands / bibliography entries | 21 / 3 |
| new bibliography entries | 0 |
| unresolved citations or references | 0 |
| overfull boxes | 0 |
| missing glyphs | 0 |
| fatal errors | 0 |
| embedded/subset font rows | 9 / 9 |
| `AUTHOR TO CONFIRM` placeholders | 0 |
| public Route/Gate prose | 0 |
| ARS block markers in public source | 0 |

Two pre-existing underfull-box notices remain in the manually line-broken
Chinese abstract.  They are nonblocking.  Visual inspection of the staged PDF
pages 1, 12, and 13 confirmed that the author/affiliation/contact block, both
abstracts, revised conclusion, contribution/funding/interest declarations,
limitations, and bibliography are legible and show no clipping or overflow.
The promoted PDF is byte-identical to that validated staged PDF.

## Artifact hashes

| Artifact | SHA-256 |
|---|---|
| anchored Stage-4 draft | `663ade71e41de81afd376db516ed8f548af3090cf342dd4db052eb212ce3c2d2` |
| public `manuscript.tex` | `2e8a6872eabb512dbd7ef04f5be933717a472c931199b9be509cb654599d4da2` |
| `references.bib` | `bd03813691db911316b18620ee4a1d212ac284fce7fb79af9f1b1cbc7ea71093` |
| `paper.aux` | `8dccd2e46ccec96962f7ce05a06f9219afbaa523a346487eb356389542da9afb` |
| `paper.bbl` | `4244c70dea32b053dc2df1c1435ebfeccc1e26f93dbe80179a523950ed091156` |
| `paper.blg` | `d12f01b6d33b0765ba9204428f685094d04af823b58ae07c21a7f1d272a08c11` |
| `paper.out` | `b8d6985e21e604681981c7d3ed6f3418021ece61e82e7b5484a2c869f5dfa6dd` |
| `paper.log` | `2a34713f5aa255c006efb9110300502d132edcc1118b787727352c0c62584153` |
| `paper.pdf` | `0ed4af9ef021876efafedf7b2457e3f371cfeb953b82c1773bcea20d8490cb8b` |

The PDF and log are newer than both source inputs.  No submission, release,
external contact, Git action, Stage 3-prime re-review, or Route advancement
was performed by this build.
