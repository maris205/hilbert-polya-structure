# P166 Review B: replay, build, and artifact QA

## Independent verifier

`verify_review_b.py` is standard-library only and imports no author, Gate-A,
or Review-A module.  It starts from the literal update and checks:

- every state and complete functional graph for `2<=n<=7`;
- every target's one-step fibre, image membership, EGF histogram, fibre-mass
  identities, maximum, and equality criterion in the same box;
- every target and time `0<=t<=2n+2` through `n=6` against an independently
  iterated phase map;
- every weak composition through `n=10`, including mass exhaustion, depth,
  periods, anchor multiplicity, and the last-shell profile;
- triangular and nontriangular maximum-fibre witnesses through `n=150`.

The canonical transcript records `14,005,344` assertions and `PASS`.

```text
verifier SHA-256: bd00021b6e802fd1fac7654697df826f7d1b0890051910010e5531d2cd06c5cd
canonical SHA-256: cca342885005ce13989fcd93e8f224b92eae2d13a87856b19cbef9880d7df689
fresh replay 1: exit 0; byte match YES; transcript SHA-256 cca342885005ce13989fcd93e8f224b92eae2d13a87856b19cbef9880d7df689
fresh replay 2: exit 0; byte match YES; transcript SHA-256 cca342885005ce13989fcd93e8f224b92eae2d13a87856b19cbef9880d7df689
```

As a secondary non-independent regression control, the author verifier also
had two fresh byte-identical replays:

```text
author assertions: 17,017,929
author verifier SHA-256: bf3d58ffddc3ff41381e08b8eaeaca7bde865733b431c2f35d2e63765ab30038
author canonical/replay SHA-256: 7ef213d9334acc39c835f9c9da4b52f4581b423e76de82406d65ece73c55cc06
fresh replays: 2/2 exit 0 and byte-identical
```

## Two source-only cold builds

Two distinct `mktemp` directories were seeded only with the pinned
`main.tex` and `references.bib`.  Each ran `pdflatex`, `bibtex`, `pdflatex`,
`pdflatex` with halt-on-error.  Both exited zero and produced a 294,007-byte
PDF of SHA-256
`f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c`.
Each PDF is byte-identical to `main_round1.pdf`, and the two cold PDFs are
byte-identical to each other.

Settled LaTeX/BibTeX logs in both builds have zero genuine LaTeX/package or
BibTeX warnings, errors, undefined citations/references, rerun requests,
overfull/underfull boxes, and fatal markers.  Literal substring scans did
find only the package-identification lines for `infwarerr` and
`rerunfilecheck`; these are package names, not emitted diagnostics.

## PDF and source surface

```text
main.pdf == main_round1.pdf: YES
pages: 4
bytes: 294,007
SHA-256: f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c
page size: 595.276 x 841.89 pt (A4)
PDF version: 1.5
encrypted: no
forms: none
JavaScript: no
metadata stream: no
standard title/author/subject/keywords/creator/producer: blank
font rows: 24
unembedded/unsubsetted/non-Unicode font rows: 0
bibliography entries visible: 6/6
visible HOLD_EXTERNAL tokens: 1
```

Extracted text contains the anonymous byline and running head, no personal
name, affiliation, email, acknowledgement, grant identifier, local path, or
editing marker.  All four pages were rendered independently at 144 dpi and
visually inspected.  Page 1 title/abstract/equations, pages 2--3 proofs and
displays, and page 4 lifecycle/references are legible with no clipping,
overlap, missing glyph, malformed formula, bad break, or stray mark.

## Frozen input recheck

At the end of QA the pinned hashes remained:

```text
a709e1b8dc6f50059cf85c8a2c922455b7812b24f4e38ebab88c77123f279ce8  main.tex
fcd2132a399ed5d21d75035aaadc234cce79dc4040613a9c5cc54ca9c896c500  references.bib
f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c  main_round1.pdf
```

No author source, verifier, PDF, review, or central ledger was modified.
