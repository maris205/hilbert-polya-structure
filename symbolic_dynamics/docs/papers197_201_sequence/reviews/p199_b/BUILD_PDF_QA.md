# P199 B source-only build and actual page QA

The review helper `qa/review_cold_build.sh` was read and run with the
absolute frozen_round1 directory, main_round1.pdf and this review directory.
A newly created private build directory initially contained only main.tex
and references.bib. With SOURCE_DATE_EPOCH=1704067200, FORCE_SOURCE_DATE=1,
TZ=UTC and LC_ALL=C it ran pdflatex -recorder, bibtex, pdflatex, pdflatex.
All commands succeeded and the final PDF byte-compared equal to Round1.
The helper preserved that actual directory as cold_build/ and rendered all
four pages at 120 dpi into visual/. No earlier aux/bbl/PDF was input.

The output SHA256 is
b6ba18a10e83281c1dd491b47cf5d8513ab9914933c659411c8d5c24b72478a0,
320,789 bytes, four A4 pages, PDF 1.5, unencrypted. Title, Author, Subject,
Keywords, Creator and Producer are blank. Every one of 24 font rows is
embedded, subsetted and Unicode-mapped. Final main.log/main.blg have no
Warning, Overfull, Underfull, undefined or Error matches; rg's no-match
exit is not a compile failure. The recorders and actual compiler stdout
are retained. No optional pypdf check is claimed in this B review.

Root opened every rendered page:

| Page | Actual view |
|---|---|
| 1 | Anonymous title/abstract, definitions, contour and owned join explanation readable; no clipping or missing symbols. |
| 2 | Exact clock, small-order witness and depth CDF/proof readable; equations and section transitions fit. |
| 3 | Entire inverse/cut/image proofs, finite table and scope readable; no overlap, truncated table or unresolved reference marker. |
| 4 | All three references visible and resolved. This intentionally sparse references-only last page is not hidden as a three-page paper. |

No source or bibliography edit was needed. The reviewed unchanged PDF is
the target for a no-change Round2 freeze. This is one actual review cold
build, not either of the two later terminal builds; those are separate.
QA_SHA256SUMS pins every cold_build/ and visual/ artifact from this folder.
