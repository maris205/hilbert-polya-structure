# P197 Review B cold build and page QA

The actual cold build used the new directory `qa/cold_build/`, initially
containing only copies of frozen Round-1 `main.tex` and `references.bib`.
No aux, bbl, log, PDF or author output was supplied as build input.

Commands from that directory were pdflatex, bibtex, pdflatex, pdflatex.
Their stdout files and all generated artifacts are retained. The result
equals `papers/197-ternary-cyclic-sign-difference/main_round1.pdf` byte for
byte, with SHA-256
`42cb9e1e7cd10858a7ecf98faf2d8ced79faeb31211f608fd20f4b75a01b792a`.
It contains four A4 pages, 371,181 bytes, PDF 1.5, and is unencrypted.
Title, author, subject, keywords, creator and producer metadata are blank.
Every font entry is embedded and subsetted. The final log has no Warning,
Overfull, Underfull, undefined or Error matches. The rg zero-match status
is not a build failure.

An initial compiler command was mistakenly launched from repository root
after the copying step, where no main.tex exists. It exited without a PDF.
Its generated `texput.log` was moved into this review's QA as
`MISLAUNCHED_ROOT_TEXPUT.log`. No manuscript file was modified by that
failed invocation. The successful source-only build was then run from the
correct new directory. This correction is a reviewer execution matter,
not an author repair or a second successful cold build.

The ARS structural preflight was run once. Its sidecar
`qa/PDF_PREFLIGHT.json` reports **UNAVAILABLE** because pypdf is not
installed. It is not promoted to structural PASS. Independent Poppler
metadata parsing, font inspection, four-page rendering and byte identity
succeeded. Page references below denote the actual rendered output order,
not a fabricated pypdf page-anchor certificate.

Every raster page was opened with the image viewer:

| Page | Actual visual result |
|---|---|
| 1 | Anonymous title and abstract legible; exact local rule and attribution boundaries fit; the local-certificate table continues normally on page 2 |
| 2 | Complete eight-row table visible; the recurrent theorem, parity cases and junction phases fit with no clipped equations or missing signs |
| 3 | Depth/fixed trace statements and characteristic factorization readable; all seven initial counts present; inverse theorem continues normally onto page 4 |
| 4 | Gap product proof, all extremal cases, numerical table, limitations and all three references fit; no collisions, cutoff text or unresolved references |

Files `qa/visual/page-1.png` through `page-4.png` preserve the views.
No author source, bibliography, code, canonical, original PDF or frozen
snapshot was edited. This is one successful source-only review build, not
the batch's later two-build terminal experiment. The scientific source
boundary remains `OWNER_AMBER / HOLD_EXTERNAL`.
