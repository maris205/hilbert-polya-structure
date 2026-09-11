# P202 build and author verification

Run from this paper directory. Python uses only the standard library.

```sh
python3 -B code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The recorded author stdout is code/CANONICAL.txt. It has 3,962,690
assertions and status PASS_AUTHOR_CONTROL. Two fresh processes produced
code/RUN1.txt and code/RUN2.txt, both byte-identical to CANONICAL.
The verifier originated in this writer's OR Stage1 audit; reuse is author
control, not another independent paper review.

The main development build used three pdfLaTeX passes and one BibTeX pass.
Two source-only builds were physically executed separately under
qa_round0/cold_build_1/ and cold_build_2/, each starting with only main.tex
and references.bib. Every command exited zero. Their final PDFs and the
main PDF share SHA-256
e1ca5021ff1ac74cff118d0d571fa0f3f74db32cc8b6ba5e7cd557fb69d88f8a.
No prior .aux or .bbl was supplied to a cold build. Logs are retained.

Final logs and BibTeX logs contain no Warning, Overfull, Underfull,
undefined, Error or Citation matches. Four A4 pages, 312,997 bytes,
25 embedded/subset/Unicode font entries; no Type3 fonts. Metadata fields
are empty, with no custom metadata or metadata stream. PDF text and
font/page metadata are retained in qa_round0/.

Every rendered page in qa_round0/visual/ was actually inspected. Page1
contains the complete inverse statement; page2 its proof and both run/
parking lemmas; page3 the core/time theorem and census statement; page4
finishes the count proof and contains exact-control limits and references.
No formula clipping or layout repair remains.

ARS pdf_read_preflight returned UNAVAILABLE (pypdf missing), with the
correct final PDF hash recorded. This advisory is not a structural PASS;
the successful Poppler and actual visual checks are separate evidence.
There is no venue-specific submission compliance claim.
