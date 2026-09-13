# Paper20 independent deterministic-build R2 audit (page-fixed retry)

Date: 2026-08-22 UTC  
Review ID: BUILD_R2_PAGEFIX_RETRY_2026_08_22

This is an independent, read-only audit of the two fresh page-fixed build
roots. I did not run LaTeX, BibTeX, Ghostscript, or any rebuild; the PDF
readback tools used below do not modify the manuscript or its build outputs.
I did not edit the source, metadata, source-revision receipt, build receipt,
or any author-controlled file. No CAS, experiment, data, network, transport,
publication, or upload action was performed.

## Build authority and frozen inputs

The retry is the one authorized by
notes/BUILD_AUTHORIZATION_R1_PAGEFIX_RETRY.md
(SHA-256 6994e72d95239c5110abd5f032712e0ef2f5bfcb5e651ca6267d286e5272fd87)
after the page-fixed source authorization and two fresh source passes. The
retry note requires a working-directory change for every child invocation and
forbids reuse of the consumed CWD-failure roots. The exact sequence is

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

in each of

    /tmp/p20-paper20-r1-pagefix-retry-A-ev483m
    /tmp/p20-paper20-r1-pagefix-retry-B-s4iTTx

with the locked environment HOME=/root, PATH=/usr/bin:/bin,
FORCE_SOURCE_DATE=1, LANG=C, LC_ALL=C,
SOURCE_DATE_EPOCH=1787356800, and TZ=UTC; the authorization declares
network access disabled. The harness reports exit status zero for all eight
children. Independently, every command log has the expected tool transcript,
the expected terminal output, and no fatal TeX/BibTeX diagnostic.

The source identities copied into both roots and read back from the live
project are:

| input | bytes / LF | SHA-256 |
|---|---:|---|
| paper/main.tex | 61,835 / 1,619 | b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90 |
| paper/math_commands.tex | 702 / 20 | 37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582 |
| paper/references.bib | 2,335 / 73 | 529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf |
| paper/PAPER_PLAN.md | 22,064 / 397 | 4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3 |
| experiments/source_lock.json | 11,847 / 1 | 57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581 |

The two roots have byte-identical copies of all three inputs. Their input
hashes also match the page-fixed source reviews
notes/INDEPENDENT_PAPER_SOURCE_R1_PAGEFIX_REVIEW.md
(e83053d521542773696a59478944d8974b46b97b5b854cb7c775cc257cb2ee30) and
notes/INDEPENDENT_PAPER_SOURCE_R2_PAGEFIX_REVIEW.md
(e81e148cc8e9d4b220a62146a6bebb906df0cdb4fb5e555eca423e8ef2a8eaa5).
At this pre-receipt audit point the R1 metadata and source-revision receipt
still intentionally carry null build-artifact fields; this review does not
silently infer a metadata transition. A subsequent receipt must bind the
fresh identities below and record the explicit build-permission transition.

## Two-root artifact identity

The final output of the four-pass sequence is byte-identical between roots.
The following values were independently rehashed (all files are regular
0644 files):

| output | bytes / LF | SHA-256 (A = B) |
|---|---:|---|
| main.pdf | 429,723 / 2,338 | 07426e1892fbbb85876a6f79401318c16f9d3aee96ae7d6ae2b087a25ca98e40 |
| main.aux | 11,920 / 139 | a96b8a6d534c04f897581590f431164f75f600ee0c85ce062cdc33ad617a8d16 |
| main.bbl | 2,282 / 56 | 15c4662bc3e3c6b65eef8a8b80d7f8210da9b8b3011a9ba5c5896504adff81f6 |
| main.blg | 900 / 46 | 3292543c220a005dc56db3fdaf1287cd9f142cc52b2d0db012f4da156ae66e15 |
| main.log | 28,899 / 734 | 34bf450186dfc29b4355ade433de214f48daf09efb724e0941a32456a6b5771f |
| main.out | 5,653 / 25 | 9cfe3093cc76d9ea5da78ad4dc35e3701dcbd91e14031ba6052e937212f12fa2 |

cmp reports equality for each of these six outputs and for all four command
logs. The generated roots contain no source divergence. The PDF hash above
is the receipt-ready replacement identity; the existing
paper/main_round1.pdf in the project is a historical pre-page-fix artifact
with a different hash and is not substituted for this identity by inference.

## PDF integrity and locked page contract

Independent readback of both PDFs gives the same result:

* pdfinfo: 23 pages, Letter size, PDF 1.5, unencrypted, no JavaScript;
  CreationDate and ModDate are the deterministic 2026-08-22 08:00 CST value
  implied by SOURCE_DATE_EPOCH=1787356800.
* Ghostscript null-page parsing exits zero.
* pdftotext -layout places section 12 Conclusion on page 22 and places
  References later on that same page; page 23 continues the references.
  The auxiliary file independently records sec:conclusion at page 22.
  Therefore the body-through-conclusion count is 22 pages, not 23, and the
  references are excluded after the split.
* The locked substantive-page contract is minimum 22, maximum 26, planned
  24. The measured 22-page body is inside the contract and meets its hard
  minimum.

The first pdflatex pass transiently reports the expected missing-auxiliary
and pre-BibTeX undefined items; those are not final-artifact diagnostics.
The final fourth pass and the final main.log have the following counts:

| check | count / result |
|---|---:|
| fatal TeX errors (!, emergency stop) | 0 |
| undefined references | 0 |
| undefined citations | 0 |
| overfull hboxes | 0 |
| underfull hboxes | 3 (advisory, in the bounded related-work table) |
| hyperref PDF-string warnings | 4 (math tokens in bookmarks) |
| final label-changed warning | 1 (advisory) |
| BibTeX warnings (warning$) | 0 |

The residual underfull, hyperref, and label warnings are recorded rather than
hidden; none is a page-contract or PDF-integrity blocker. Marker scans of
the final PDF text and the three manuscript input files find zero occurrences
of ??, [?], TODO, TBD, VERIFY, FIXME, or Missing $.

## Fonts, labels, and citations

pdffonts reports 25 font rows in each final PDF (the page-fixed source uses
one additional LM Mono face); every row has emb=yes, sub=yes, and uni=yes.
The two main.bbl files are identical and contain seven unique BibTeX keys.
Those seven keys agree with the seven entries in references.bib and the
\bibcite/citation records in main.aux; no undefined-citation diagnostic
remains. The final auxiliary records resolve the manuscript's labels,
including the conclusion page and the page-fixed leading-form labels. No
duplicate or missing reference target was observed in the readback.

## Old and non-authoritative artifacts

The consumed CWD-failure roots

    /tmp/p20-paper20-r1-pagefix-A-JBuZF3
    /tmp/p20-paper20-r1-pagefix-B-w344h4

contain only the three copied inputs and four short failure logs each; they
contain no PDF, auxiliary, bibliography, or log output from a successful
build, and were not reused. The earlier non-page-fixed roots
/tmp/p20-paper20-r1-A-7GEBaI and
/tmp/p20-paper20-r1-B-rx5cFc, together with the project
paper/main_round1.pdf (424,691 bytes,
e40b4b44a3a8fa7e1102efdbc615476a9fa038cf146777838de6b9e0b5cb24f9, 22
pages), are historical pre-page-fix outputs. paper/main_round0.pdf and the
unversioned paper/main.pdf are the immutable 14-page R0 artifact (380,574
bytes, ed58824860f77186210fee298b1631e7877868dc828b4b3a9cd048fcaa1545e9).
None of these older files is used as evidence for the replacement build.

During this read-only audit a text extraction probe left
/tmp/p20-paper20-r1-pagefix-retry-B-s4iTTx/main.txt (75,075 bytes, 1,208
LF); it is reviewer-created residue, not a compiler output, is excluded from
the artifact table and any future receipt, and must not be persisted into the
project. It does not alter any source, PDF, auxiliary, or hash comparison.

## R2 verdict and permission boundary

Both fresh roots produce the same valid page-fixed PDF, satisfy the locked
22--26 substantive-page gate, and pass the independent diagnostics,
font-embedding, citation, and source-identity checks. No build-integrity
blocker was found. This note is an audit verdict only: it does not authorize
source edits, another build, CAS, experiments, publication, transport,
upload, or replacement persistence. The author-side build receipt must bind
the exact replacement PDF/output hashes above, both root identities, the page
split, diagnostic counts, fresh source-review hashes, and the no-source-edit
boundary before downstream publication-stage work.

BUILD_R2_PAGEFIX_PASS
