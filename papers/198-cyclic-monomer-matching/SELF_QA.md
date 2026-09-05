# P198 Round0 author self-QA

Date: 2026-09-05 UTC. Scope: author checks only. Review A and B: NOT_RUN. External status: HOLD_EXTERNAL.

| Check | Executed result |
|---|---|
| Full proof audit | All five sections contain proofs; interval necessity and sufficiency, odd-prefix wrap exclusion, rank separation of rotor predecessor and n=3 image boundary are explicit |
| Paper-local exact test | 237,845 assertions; every matching at every odd n=3,...,21 |
| Fresh process determinism | Two recorded runs match code/CANONICAL.txt exactly, both stderr files empty |
| Cold build determinism | Two separate source-only directories; pdfLaTeX/BibTeX/pdfLaTeX/pdfLaTeX; identical PDF bytes |
| Final log check | No Warning, Overfull, Underfull, undefined, or Error match in either final main.log |
| Bibliography check | Both in-text keys resolved; verified journal metadata; full-text gaps disclosed in SOURCE_AUDIT.md |
| PDF inspection | Four pages rendered at 85 dpi and all visually inspected; readable equations/table, no clipping or overlap; references occupy page four |
| Text extraction | Full pdftotext output read; no unresolved citation or reference marker |
| Font and metadata audit | pdffonts lists all fonts embedded; A4 pages, anonymous visible author placeholder, blank identifying PDF metadata |
| Frozen integrity | round0_frozen/SHA256SUMS independently checked: all six files OK; original and current PDF hashes identical |

The PDF source is a compact amsart note, not a venue-specific submission template. A short references-only final page is a layout choice, not omitted content. No author identity, funding or conflict declaration has been invented.

Residual risks are scientific ownership and historical completeness, not an unreported passing review: source coverage is bounded, P51–P56 manuscripts are missing, and standard matching facts have been explicitly deducted. Author checks cannot substitute for independent manuscript reviews.

