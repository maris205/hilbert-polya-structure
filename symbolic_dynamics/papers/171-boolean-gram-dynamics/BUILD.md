# P171 build and verification ledger

**Artifact:** `papers/171-boolean-gram-dynamics`  
**Status:** `ROUND2 DUAL-REVIEW FREEZE / HOLD_EXTERNAL`  
**Build date:** 2026-09-03 UTC

## Author verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 verify_p171.py
decision: AUTHOR_ROUND0_PASS
external status: HOLD_EXTERNAL_OWNER_THIN
assertions: 594,955
verifier SHA-256: eef567a25b0a6daefdbe926218b4c526392230abaec1033aa7b749e385600abc
stdout SHA-256: bc3ba0e2b647ff5c888ad7534ef0088398cc7f58b2b71bde9688e3bc9e11e617
fresh process replays: 2/2
byte-identical replay/output match: yes
```

The standard-library verifier imports no scouting, historical verifier, or
paper module.  It exhausts every source and every codomain target through
`n=4`; compares the literal and formula fibres; independently checks cover
feasibility, all-time powers, clocks, endpoints, and fixed counts; and
replays the sharp path witness through `n=64`.

## Canonical build

Toolchain:

```text
pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
BibTeX 0.99d (TeX Live 2022/dev/Debian)
```

The explicit settling sequence was:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The retained command logs are `build_pdflatex_1.log`, `build_bibtex.log`,
`build_pdflatex_2.log`, and `build_pdflatex_3.log`.  The settled LaTeX and
BibTeX logs contain no warning, bad box, unresolved citation/reference,
rerun request, duplicate destination, or fatal/error diagnostic.

Two additional builds ran in separate fresh temporary directories initially
containing only `main.tex` and `references.bib`.  Their settled logs are
`build_cold1_settled.log`, `build_cold1_bibtex.log`,
`build_cold2_settled.log`, and `build_cold2_bibtex.log`.  Both produced
SHA-256

```text
1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1
```

and each PDF matched the canonical PDF byte for byte.

## Round-0 PDF freeze

```text
canonical PDF: main.pdf
frozen copy: main_round0_original.pdf
round-copy byte match: yes
cold-build byte matches: 2/2
pages: 3
bytes: 329,559
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: 1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1
font rows: 25
unembedded/unsubsetted/non-Unicode font rows: 0
encrypted: no
forms: none
JavaScript: no
embedded files: none
raster images: none
```

All three pages were rendered at 144 dpi and inspected at original image
detail.  The abstract, theorem continuation, boxed fibre sum, set equations,
small-fibre table, exact census, references, running heads, and page numbers
are legible and inside the A4 page box.  Title, author, subject, keywords,
creator, and producer metadata fields are blank; the visible byline and
running heads are anonymous.

## Frozen core hashes

```text
1a1ca296a922d02a12fe8d01ae3c4122eee892ef5f6a5c83e801c218247cc197  main.tex
806c750e41c8226b62fad89a9273859257bf9a882e0a5a1e8b43bf4714d0c7e3  references.bib
eef567a25b0a6daefdbe926218b4c526392230abaec1033aa7b749e385600abc  verify_p171.py
bc3ba0e2b647ff5c888ad7534ef0088398cc7f58b2b71bde9688e3bc9e11e617  verification_output.txt
1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1  main.pdf
1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1  main_round0_original.pdf
```

## Historical Round-0 boundary

At author freeze this was an author-side Round-0 artifact, not a review.  The
hostile re-entry gate was `GREEN_OWNER_THIN`, external circulation remained
`HOLD_EXTERNAL`, and no release or submission action was authorized.

## Round-1 and Round-2 no-change closeout

Hostile Review A and independent nonauthor Hostile Review B each returned
`ACCEPT_INTERNAL / PROVABLE AS STATED` with
`0 Critical / 0 Major / 0 Minor`.  Neither requested a source or artifact
repair.  The round distinction is provenance-only:

```text
author Round 0: main_round0_original.pdf
post-Review-A:  main_round1.pdf
post-Review-B:  main_round2.pdf
live canonical: main.pdf
```

All four paths are byte-identical, three-page PDFs of 329,559 bytes with
SHA-256
`1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1`.
Review B replayed the 594,955-assertion author verifier twice and ran an
independent 729,535-assertion column-support/coverage implementation.  Its
two additional source-only builds, all-page visual check, and
font/metadata/anonymity/lifecycle checks all passed.

The Round-0 sections above remain historical evidence.  The final
paper-local `SHA256SUMS` is regenerated after both review reports and all
round artifacts are present.  Final status is
`ROUND2 DUAL-REVIEW FREEZE / GREEN_OWNER_THIN / HOLD_EXTERNAL`.
