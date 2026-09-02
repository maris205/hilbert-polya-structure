# P166 build and verification ledger

**Artifact:** `papers/166-hamming-weight-translation-dynamics`  
**Status:** `ROUND-2 INTERNAL ACCEPT / REVIEWS A-B 0C-0M-0m / HOLD_EXTERNAL`.

## Author verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
assertions: 17,017,929
status: PASS
canonical SHA-256: 7ef213d9334acc39c835f9c9da4b52f4581b423e76de82406d65ece73c55cc06
verifier SHA-256: bf3d58ffddc3ff41381e08b8eaeaca7bde865733b431c2f35d2e63765ab30038
fresh byte-identical replays: 2/2
```

## Canonical build

Toolchain: pdfTeX `3.141592653-2.6-1.40.22` and BibTeX `0.99d`.

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The retained logs are `build_pdflatex_1.log`, `build_bibtex.log`,
`build_pdflatex_2.log`, and `build_pdflatex_3.log`.  The settled final log
and BibTeX log contain zero warnings, bad boxes, unresolved references or
citations, rerun requests, duplicate destinations, and fatal errors.

Two additional builds were run in distinct fresh directories that initially
contained only `main.tex` and `references.bib`.  Their settled logs are
`build_cold1_settled.log` and `build_cold2_settled.log`, with BibTeX logs
retained separately.  Both PDFs match the canonical artifact byte for byte.

## Round-0 PDF freeze

```text
canonical PDF: main.pdf
frozen copy: main_round0_original.pdf
pages: 4
bytes: 294,007
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c
round-copy byte match: YES
font rows: 24
unembedded/unsubsetted/non-Unicode font rows: 0
encrypted: no
forms: none
JavaScript: no
```

All four pages passed 144-dpi visual inspection.  PDF metadata fields are
blank, the byline/running head are anonymous, and `HOLD_EXTERNAL` is visible.

## Frozen core hashes

```text
a709e1b8dc6f50059cf85c8a2c922455b7812b24f4e38ebab88c77123f279ce8  main.tex
fcd2132a399ed5d21d75035aaadc234cce79dc4040613a9c5cc54ca9c896c500  references.bib
bf3d58ffddc3ff41381e08b8eaeaca7bde865733b431c2f35d2e63765ab30038  code/verify.py
7ef213d9334acc39c835f9c9da4b52f4581b423e76de82406d65ece73c55cc06  code/CANONICAL.txt
f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c  main.pdf
f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c  main_round0_original.pdf
```

## Round-1 no-change freeze

Independent Hostile Review A returned `ACCEPT` with
`0 Critical / 0 Major / 0 minor`.  No mathematical, ownership, citation,
source, verifier, build, or PDF repair was requested.

```text
Review-A assertions: 11,795,304
Review-A verifier SHA-256: 2f717ff4cd557e353b94826c85238cff19497d622f4d498b1b549cdc786be4ef
Review-A canonical SHA-256: bee2274c898591173b9fdda41b728f627c7dc30faedbf2eea70efee967ecf46d
Review-A fresh byte-identical replays: 2/2
Review-A findings: 0 Critical / 0 Major / 0 minor
Round-1 copy: main_round1.pdf
Round-0/current/Round-1 byte match: YES
Round-1 PDF SHA-256: f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c
```

The frozen `main.tex`, `references.bib`, author verifier, author canonical,
and `main.pdf` retain their Round-0 hashes.

## Round-2 no-change freeze

Fresh Hostile Review B returned `ACCEPT_INTERNAL` with
`0 Critical / 0 Major / 0 minor`.  It requested no mathematical, ownership,
citation, source, verifier, build, or PDF repair.

```text
Review-B assertions: 14,005,344
Review-B verifier SHA-256: bd00021b6e802fd1fac7654697df826f7d1b0890051910010e5531d2cd06c5cd
Review-B canonical SHA-256: cca342885005ce13989fcd93e8f224b92eae2d13a87856b19cbef9880d7df689
Review-B fresh byte-identical process replays: 2/2
Review-B author-regression replays: 2/2 byte-identical
Review-B findings: 0 Critical / 0 Major / 0 minor
Round-2 copy: main_round2.pdf
Round-0/current/Round-1/Round-2 byte match: YES
Round-2 PDF SHA-256: f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c
```

The artifact is internally accepted after both reviews and remains
`HOLD_EXTERNAL`.  The paper-local `SHA256SUMS` is intentionally deferred
until the final consistency notification.
