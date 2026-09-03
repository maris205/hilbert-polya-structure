# P167 author-side Round-0 QA (historical)

**Verdict:** `PASS / HOLD_EXTERNAL`  
**Scope:** theorem, evidence, source boundary, executable replay, build,
anonymity, and rendered PDF

## Mathematical QA

- The displayed definition states both branches of the map: least preimage
  for a present symbol and the symbol itself for a missing symbol.
- The text distinguishes feedback powers of `M` from composition powers of
  the input endofunction.
- The one-sided inner-inverse/KRR identity is separated from mutual inverse
  selection; the `f=(0,0)` counterexample is explicit.
- First-image off-diagonal injection is used only as a necessary structural
  condition.  The fibre product is stated as the exact support test.
- The path action covers `s>1` and explicitly fixes singletons.
- The recurrence proof treats both endpoint inequalities and uses permanent
  splitting for the converse.
- The `2s-2` path clock is proved by a complete three-case induction; the
  equality condition is the unique decreasing order.
- The first-image height proof uses the mandatory value zero to exclude only
  that full decreasing path, handles every other full path by integrality,
  and handles smaller components separately.
- The global witness is defined coordinate by coordinate, so its `n=2`
  boundary is unambiguous.
- The connected census treats sizes 1, 2, and 3 separately before the
  disjoint-pair quartering argument for `s>=4`.
- Fixed components are classified before odd/even iterate counts and the
  formal zeta conversion are applied.
- The every-target fibre proof covers repeated forced positions, fixed
  coordinates occupied by another symbol, zero factors, and the converse
  construction.
- The Bell proof establishes at most one source per target/kernel partition
  and constructs every partition over the identity.  It does not assert a
  unique maximizing target.
- The main theorem itself contains the complete `n=1,2,3` table.  The text
  gives the full `n=2` graph and the `n=3` nonzero-fibre histogram.

No theorem repair or weakening was required after the hostile candidate
gate.  The proof status is `PROVABLE AS STATED`.

## Source and claim-boundary QA

- `references.bib` has exactly five entries and every entry is cited.
- Every citation was rechecked against a DOI/publisher record; the
  proceedings metadata for Flajolet--Odlyzko was also checked against DBLP.
- Least transversals/inverse matchings, RGF/first-occurrence encodings,
  functional graphs, Bell/involution counts, labelled species, and zeta
  algebra are explicitly zero-credit background.
- The identity-on-missing completion is distinguished from arbitrary section
  extensions.
- The bounded literal-owner non-hit is described only as owner-thin and does
  not authorize a novelty, priority, posting, or submission statement.
- No uncited BibTeX entry and no unverified-citation placeholder remains.

## Verifier QA

Two fresh processes produced identical 9,831-byte stdout files, each with
`12,603,676` exact assertions.  Both match
`verification_output.txt` byte for byte.  The transcript embeds the same
SHA-256 as the frozen `verify_p167.py`:

```text
b7c10bd3738362397a97361ca3780c4f53c7297efbe3e1885175634b345b457b
```

The script parses as Python, uses only the standard library, imports no
scout, and leaves no `__pycache__` directory.

## Historical Round-0 build and PDF QA

- canonical settling sequence: `pdflatex`, `bibtex`, `pdflatex`,
  `pdflatex`;
- two additional source-only cold builds: both passed and matched the
  canonical PDF byte for byte;
- canonical settled log, both cold settled logs, and all three BibTeX logs:
  zero warnings, bad boxes, unresolved references/citations, rerun requests,
  or fatal errors;
- PDF: 4 A4 pages, 285,798 bytes, SHA-256
  `81bfa2ed4944f2750558f06cbb3a09d7081fc0361a0361f05f91869368faf379`;
- `main_round0_original.pdf` was byte-identical to the Round-0 `main.pdf` at
  author freeze.  The live `main.pdf` is now the repaired Round-2 artifact
  and is intentionally different;
- all 21 font rows are embedded, subsetted, and Unicode mapped;
- PDF metadata fields are blank; the file is unencrypted and contains no
  form or JavaScript;
- extracted text contains no unresolved marker, email address, filesystem
  path, affiliation, or acknowledgment.

## Visual and anonymity QA

All four pages were rendered at 144 dpi and inspected.  No clipping,
collision, overflow, orphaned heading, malformed symbol, or missing glyph
was found.  The long main-theorem statement and boundary table remain inside
the text block.  The witness sentence, proof endings, Section 5 transition,
and bibliography were specifically rechecked after the final typesetting
repair.

The visible byline and running heads say only `Anonymous`.  The
`HOLD_EXTERNAL` lifecycle is visible on page 4.  This file records the
historical author QA; the two later hostile-review verdicts and repaired
artifact hashes are recorded in `HOSTILE_REVIEW_A.md`,
`HOSTILE_REVIEW_B.md`, `IMPROVEMENT_LOG.md`, and `BUILD.md`.
