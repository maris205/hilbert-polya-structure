# P203 B: new source-only cold build and all-page inspection

Result: PASS for the actual repaired Round1 source/PDF. No author build
directory or earlier review build was reused.

## Actual cold build

The stable script was read and executed as follows, from repository root:

~~~
bash docs/papers197_201_sequence/qa/review_cold_build.sh \
  /root/autodl-tmp/symbolic_dynamics/papers/203-monochromatic-triangle-complementation/frozen_round1 \
  /root/autodl-tmp/symbolic_dynamics/papers/203-monochromatic-triangle-complementation/frozen_round1/main.pdf \
  /root/autodl-tmp/symbolic_dynamics/docs/papers197_201_sequence/reviews/p203_b/qa
~~~

The script created a new temporary directory beneath this review's QA
directory, copied only main.tex and references.bib, ran pdflatex with
recorder, BibTeX, and two further pdflatex passes, compared the output
against the frozen PDF, and preserved the cold directory. It exported
SOURCE_DATE_EPOCH=1704067200, FORCE_SOURCE_DATE=1, TZ=UTC and LC_ALL=C.
The actual execution completed with exit 0 (session 10016).

Both the cold and frozen PDF have SHA-256:
0738965406c046662618ec999474738c064c363fa66ba587e7b33a377f89b47d.
A subsequent actual hash check reconfirmed equality. Cold main.tex and
references.bib are the source inputs; generated aux/bbl/out files and
system TeX packages/fonts account for the other recorder inputs.
The preserved main.fls and all three compiler stdout files are available
under qa/cold_build/. There was no preexisting bbl/aux/PDF copied in.

The final main.log scan for Overfull, Underfull, undefined, multiply
defined, Warning, Error and Emergency returned no matches (rg exit 1).
First-pass expected unresolved cross-references are not confused with
the final-pass result. BibTeX and all compiler commands completed.

## Metadata and structural fallback

Actual pdfinfo reports four A4 pages, 309,156 bytes, rotation zero,
PDF 1.5, no encryption, JavaScript, metadata stream or custom metadata.
Title, subject, keywords, author, creator and producer fields are empty.
The printed author is Anonymous. Actual pdffonts contains 22 font records,
all Type 1 with embedding, subsetting and Unicode mapping marked yes.
The literal tool outputs are stored as qa/PDFINFO.txt and qa/PDFFONTS.txt.

The ARS pdf_read_preflight tool was actually attempted first and returned
UNAVAILABLE because pypdf is not installed. Its unchanged JSON is retained.
This is not represented as a successful structural parse. The independent
pdfinfo, successful PDF rendering, extracted text and four actual page
views provide the executed fallback checks; no external service or
package installation was required.

## Actual visual inspection of every page

The new script rendered the frozen PDF to 120 dpi images in qa/visual/.
All four images were actually opened with the image-viewing tool, not
inferred from text extraction or a prior review.

| Page | Actual visual finding |
|---|---|
| 1 | Anonymous title/abstract and literal piecewise update are readable. The operation/static-owner subtraction appears in the introduction. Lemma 2.1 begins cleanly; its continuation across the page break is intelligible. No clipped equation, citation or running material. |
| 2 | Lemma 2.1 concludes; the fixed-anchor and initial-retired-vertex arguments are visible. The sharp witness's three-case equation and induction fit without collision. The inverse D/C definitions at the bottom are complete and legible. |
| 3 | The full inverse statement and both-direction proof are readable. The maximum-fibre display and its star/top realizations fit. All S1--S3 and K1--K3 clauses, including K3's flipped/unflipped distinction, are present without clipping. |
| 4 | The equality proof concludes correctly. The finite table has aligned values for n=3..6. The added scope/release paragraph visibly states HOLD_EXTERNAL, bounded ownership, no global novelty/priority and no authorized release. Both references are complete and unclipped. |

The four inspected page images and extracted layout text are retained.
The paper is compact but readable in the project short anonymous amsart
format. No build, anonymity, bibliography-layout or visual repair is
required. This finding is not an external-release authorization.
