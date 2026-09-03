# P169 author-side Round-0 QA (historical)

**Verdict:** `PASS / HOLD_EXTERNAL`  
**Scope:** theorem, evidence, source boundary, executable replay, build,
anonymity, and rendered PDF

## Mathematical QA

- The literal map names the canonical minimum order, simultaneity, maximum
  donation, cyclic successor, and singleton convention.
- The proof that canonical order is preserved compares every linear adjacent
  pair and separately notes that the `k-1 -> 0` donation creates no cyclic
  order inequality.
- The restricted-growth translation changes exactly the final occurrence of
  every repeated letter and proves preservation of both the RGF condition and
  the block count.
- The load equation uses `z_i=|B_i|-1`; its max-plus lift, explicit solution,
  shared-maxima argument, and both cone implications are printed.
- Sparse smoothing handles `m=1`; dense smoothing handles `m=k`; the zero-mass
  boundary is excluded from the lemma and handled as `k=n`.
- The dense suffix and sparse prefix window proofs retain labels beyond the
  chip-firing quotient and prove forward invariance.
- The sharp family is defined without an ellipsis ambiguity in its zero run.
  Both sparse and dense trajectories show that neither phase ends early.
- The recurrent proof gives necessity, converse invariance, exact period, and
  counts.  The interface `n=2k` and the boundaries `n=1`, `k=1`, and `k=n`
  are explicit.
- The five states are ordered and their candidate sets, admissibility
  conditions, retained sizes/extrema, threshold counts, and every matrix entry
  are printed.  Empty remainders are set to zero before an undefined maximum
  could be evaluated.
- The source reconstruction treats inactive deletion/addition correctly.  An
  absent outgoing token is equivalent to a singleton source; a present token
  is forced to be a strict maximum.
- Canonical minimum comparisons are imposed only for `i<k-1`.  Matrix trace
  closure handles the donation wrap without adding a false order condition.
- Singleton-target deletion gives a zero outgoing row, while the all-singleton
  target has the unique all-absent path.
- All four matrices for the interlacing pair are printed.  Their traces and
  literal predecessor sets give fibres two and one despite identical ordered
  `(size,minimum,maximum)` data.

The proof status is `PROVABLE AS STATED`; no empirical premise is used in a
uniform theorem.

## Source and claim-boundary QA

- `references.bib` has exactly eight entries and every entry is cited.
- Each record was checked against a DOI/publisher or primary arXiv metadata
  surface; Brandt's full page range was separately cross-checked after the
  machine DOI response truncated it.
- RGF encoding/whirling and the complete directed-cycle load factor are
  explicitly zero-credit background.
- Bulgarian solitaire, promotion/jeu de taquin/rowmotion, box-ball systems,
  set-partition stack sorting, Stirling counts, and generic matrix algebra are
  also explicitly subtracted.
- The bounded search result is described only as a lifecycle limitation and
  does not authorize posting or submission.
- No uncited BibTeX entry or unverified-citation placeholder remains.

## Verifier QA

Two fresh processes produced identical 1,785-byte stdout files, each with
`1,217,025` exact assertions.  Both match `verification_output.txt` byte for
byte.  The standard-library script parses, imports no scout, and leaves no
`__pycache__` directory in the frozen artifact.

```text
verify_p169.py SHA-256:
e4566e997ec656f3eaa41fa4f23953773222293cf23189ebd6c7d9a64aab950b

verification_output.txt SHA-256:
e59891873e682c0a271a28197e681f6ba813f394f4104140b02d5eb4e5ce258f
```

## Historical Round-0 build and PDF QA

- canonical settling sequence: `pdflatex`, `bibtex`, `pdflatex`,
  `pdflatex`;
- two additional source-only cold builds: both passed and matched the
  canonical PDF byte for byte;
- canonical settled log, both cold settled logs, and all three BibTeX logs:
  zero warnings, bad boxes, unresolved references/citations, rerun requests,
  or fatal errors;
- PDF: 5 A4 pages, 392,917 bytes, SHA-256
  `df03b864b47ae963c467831ba7f5b47231663f1e369facf21eee1d468b17c9c2`;
- `main_round0_original.pdf` was byte-identical to the Round-0 `main.pdf` at
  author freeze.  The live `main.pdf` is now the repaired Round-2 artifact
  and is intentionally different;
- all 28 font rows are embedded, subsetted, and Unicode mapped;
- PDF metadata title, author, subject, keywords, creator, and producer are
  blank; the file is unencrypted and contains no form or JavaScript;
- extracted text contains no unresolved marker, email address, filesystem
  path, affiliation, acknowledgement, or review content.

## Visual and anonymity QA

All five pages were rendered at 144 dpi and inspected.  No clipping,
collision, overflow, malformed glyph, orphan bibliography page, or missing
symbol was found.  The two long state tables, boxed entry rule, theorem page
break, four numerical matrices, and final bibliography were specifically
checked after final typesetting.

The visible byline and running heads say only `Anonymous`.  The lifecycle
line `HOLD_EXTERNAL` is visible on page 5.  This file records historical
author QA; the two later hostile reviews and repaired artifact hashes are
recorded in `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`,
`IMPROVEMENT_LOG.md`, and `BUILD.md`.
