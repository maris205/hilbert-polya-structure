# P203 A original and repaired source-only builds

Root performed two genuinely new review cold builds with the exact pinned
review_cold_build.sh: one from frozen_round0 into qa_original, and another
from revision_a into qa_repair. Each empty temporary directory received only
main.tex and references.bib, then ran pdfLaTeX-recorder/BibTeX/pdfLaTeX/
pdfLaTeX with SOURCE_DATE_EPOCH1704067200,FORCE_SOURCE_DATE1,LC_ALL=C,TZ=UTC.
No author auxiliary, bibliography output or PDF was a build input.

Both command chains and comparisons exited0 (sessions58759 and51376).
The original4page PDF is617cea5d4f8b50a9946d05bafc2cfbf6fb01bbe45dab754813b07f4f12cc1167;
the repaired4page PDF is0738965406c046662618ec999474738c064c363fa66ba587e7b33a377f89b47d.
Original size286868bytes/21fonts; repaired309156bytes/22fonts. The only
added font is the monospaced face rendering the hold marker. All fonts are
embedded/subsetted/Unicode-mapped. Both PDFs have blank identity metadata,
unrotatedA4 pages, no encryption/forms/JavaScript/metadata streams. Final
logs have no Warning,Undefined,Overfull,Underfull orError matches; source
diff is exactly one new scope paragraph and unchanged code/bib/canonical.

Root actually opened every120dpi original page, and then every120dpi
repaired page; these are8 actual page views, not one set counted twice.

| Page | Original and repaired observations |
|---|---|
| 1 | Anonymous title, literal on all labelled graphs, two credited sources, entrance notation, generic descent and obstruction proof opening; legible and unclipped. |
| 2 | Full no-return proof including initial retired vertex, complete all-size witness and D/C definitions; no dropped signs or split-off assumptions. |
| 3 | Full inverse proof, classical cap and both literal realizations, S/K conditions and equality theorem; dense but legible with no overlapping list labels. |
| 4 | Equality proof, finite table, scope and both references. Original lacks visible HOLD, the actual A-M1 finding. Repair adds a visible HOLD_EXTERNAL paragraph above references without overflow or a fifth page. |

PDF extraction independently confirms the entire repaired release paragraph
including literal HOLD_EXTERNAL. Root read the actual one-insertion diff
and author A_RESPONSE.md, and byte-compared unchanged bibliography/code/
canonical against Round0. These builds are not the future two terminal
builds; their immutable original and repair directories remain separate.
The repaired PDF closes the delivery-scope issue without a mathematical
or provenance reconstruction. This is project QA, not PDF/A or external
submission approval. Any optional unavailable check is separately labelled.

Root actually invoked the ARS pdf_read_preflight.py on the repaired review
PDF. Its raw JSON is qa_repair/pdf_read_preflight.json; the result is
UNAVAILABLE because pypdf is not installed. That check is not labelled PASS.
The independent Poppler metadata/font/extraction and all-page visual evidence
above remains the completed project QA; no package installation was inferred.
