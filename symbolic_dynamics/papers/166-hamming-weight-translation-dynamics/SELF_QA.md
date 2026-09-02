# P166 author-side Round-2 QA

**Verdict:** `PASS / HOLD_EXTERNAL`.

Independent Hostile Review A returned `ACCEPT` with
`0 Critical / 0 Major / 0 minor` after `11,795,304` assertions.  It required
no mathematical, source, code, typesetting, or metadata repair.  Round 1 is
therefore a no-change freeze: `main_round0_original.pdf`, `main.pdf`, and
`main_round1.pdf` are byte-identical.

Independent Hostile Review B subsequently returned `ACCEPT_INTERNAL` with
`0 Critical / 0 Major / 0 minor` after `14,005,344` assertions.  It also
required no change.  `main_round2.pdf` is the no-change Round-2 freeze.

## Mathematical and scope QA

- The literal map states that Hamming weight is an integer before reduction.
- The diagonal-orbit reduction is an exact conjugacy, not an unproved
  quotient or lumping.
- The recurrent proof distinguishes fixed phases from the unique possible
  nontrivial cycle and proves mass exhaustion.
- The transient proof explicitly establishes the no-wrap inequality, the
  full Stirling depth sum, the sharp equality structure, and the last-shell
  count.
- The one-step proof separates integer weights zero and `n`, which yield the
  same residue shift but mutually exclusive source conditions.
- The marked EGF's `(u-1)` correction changes only the otherwise unmarked
  all-zero target; exact expansion agrees with all target distributions
  through `n=7`.
- The maximum-fibre construction covers all triangular and nontriangular
  `n`; a remainder is placed in a provably nonmarked, nonhitting symbol.
- `n=2` is an exact direct-owner boundary and receives zero credit.
- The every-time result is called only a target-local `n`-phase oracle.

## Exact replay

Two fresh executions of
`PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py` matched
`code/CANONICAL.txt` byte for byte.  Each reports `17,017,929` assertions
and `RESULT=PASS`.  No `__pycache__` directory is retained.

## Build and PDF QA

- canonical source build: `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`;
- two further source-only cold builds, each initially containing only
  `main.tex` and `references.bib`: both passed and matched `main.pdf` byte
  for byte;
- canonical and both cold settled logs, plus all BibTeX logs: zero warning,
  undefined reference/citation, rerun request, overfull/underfull box,
  duplicate destination, or fatal error;
- PDF: 4 A4 pages, 294,007 bytes, SHA-256
  `f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c`;
- `main_round0_original.pdf` is byte-identical to `main.pdf`;
- `main_round1.pdf` is also byte-identical to both Round-0 artifacts;
- `main_round2.pdf` is byte-identical to the canonical, Round-0, and Round-1
  PDFs;
- all 24 font rows are embedded, subsetted, and Unicode mapped;
- title, author, subject, keywords, creator, and producer metadata are empty;
- PDF is unencrypted and has no form or JavaScript.

## Visual and anonymity QA

All four pages were rendered at 144 dpi and inspected.  Equations,
indicator symbols, theorem blocks, running heads, page numbers, references,
and the status line are legible and inside the page box; no collision,
clipping, overflow, or orphaned heading was found.

The byline and running heads are anonymous.  Extracted text contains no
email address, affiliation, acknowledgment, filesystem path, user handle,
TODO/FIXME marker, or unresolved citation.  `HOLD_EXTERNAL` is visible on
page 4.

Both hostile reviews are complete with zero findings.  The lifecycle is
`ROUND2 INTERNAL ACCEPT / HOLD_EXTERNAL`.
