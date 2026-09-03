# P168 author-side Round-0 QA (historical)

**Verdict:** `PASS / HOLD_EXTERNAL`  
**Scope:** theorem, evidence, ownership boundary, exact replay, build,
anonymity, and rendered PDF

## Mathematical QA

- The carrier is the complete `F_p`-subspace lattice of `F_{p^4}`, and the
  zero branch of `J` is explicit.
- Rank monotonicity follows from the cardinality of the inverse set, not from
  an unsupported linearity assertion.
- Equality of ranks is shown to make patched inversion fill `J(A)` and hence
  to imply `J^2(A)=A`; monotonic rank then excludes transient recurrence.
- The recurrent classification is invoked at exactly the strength supplied
  by Kolomeec--Bykov, with size-one and full-field boundaries handled in the
  manuscript.
- The plane calculation separates scaled quadratic-subfield planes from
  degree-four planes.  Denominator clearing proves rank `min(p+1,4)` for the
  latter.
- The binary case has exactly three inverse projective representatives, so a
  non-subfield plane goes first to a hyperplane; at odd primes it reaches the
  full field immediately.
- A hyperplane cannot retain rank three without becoming recurrent, so it
  maps to the full field.
- Lines and scaled quadratic planes reduce to inversion on the correct cyclic
  scalar quotients.  The fixed and two-cycle formulas include zero and the
  full field separately.
- The zeta formula uses the fixed/two-cycle decomposition, and the image and
  depth formulae use the complete transition partition.
- Fibre exclusions follow from rank monotonicity and the classified image
  ranks.  The binary two-to-one plane-to-hyperplane count uses twisted scalar
  equivariance plus transitivity on trace hyperplanes and a total mass check.
- The theorem states fibres for every target and every positive time, not
  merely full-field aggregate fibres.
- The full component description follows from those target-local fibres and
  has no unstated transient branch.

The analytic proof status is `PROVABLE AS STATED`; the exhaustive program is
kept as independent falsification evidence rather than substituted for a
proof.

## Source and claim-boundary QA

- `references.bib` contains exactly six records, every record is cited, and
  each DOI/publisher record was checked on a primary surface.
- Print-issue years are used consistently for the two online-first records.
- The patched inverse-subspace classification is visibly attributed to
  Kolomeec--Bykov and assigned zero contribution credit.
- Inverse-line normal-rational-curve and small-field independence geometry is
  visibly attributed to Faina--Kiss--Marcugini--Pambianco and
  Lavrauw--Zanella and assigned zero contribution credit.
- Mattarei, Csajbók, Gaussian counts, cyclic-quotient inversion, and the
  Artin--Mazur conversion are background only.
- The bounded owner search is stated to have no positive novelty or priority
  force.  No posting, submission, freedom-to-operate, or release claim is
  made.
- No uncited BibTeX record, unverified placeholder, or `[VERIFY]` marker
  remains.

## Verifier QA

Two fresh processes produced the same 827-byte output, and both match
`verification_output.txt` byte for byte.  Each run reports 32,754 explicit
checks, partitioned as `1,486`, `18,456`, and `12,812` for `p=2,3,5`.
The transcript records all three complete-edge hashes and ends with
`AUTHOR_ROUND0_PASS / HOLD_EXTERNAL_OWNER_THIN`.

The script parses as Python, uses only the standard library, imports no
scouting or paper module, and leaves no `__pycache__` directory.

## Build and PDF QA

- canonical settling sequence: `pdflatex`, `bibtex`, `pdflatex`,
  `pdflatex`;
- two additional source-only cold builds: both passed and matched the
  canonical PDF byte for byte;
- canonical and cold settled logs: zero warnings, bad boxes, unresolved
  references/citations, rerun requests, or fatal errors;
- PDF: 5 A4 pages, 322,829 bytes, SHA-256
  `846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e`;
- `main_round0_original.pdf` is byte-identical to `main.pdf`;
- all 23 font rows are embedded, subsetted, and Unicode mapped;
- PDF metadata fields are blank; the file is unencrypted and contains no
  form or JavaScript;
- extracted text contains no unresolved marker, email address, filesystem
  path, affiliation, acknowledgment, or nonanonymous author identifier.

## Visual and anonymity QA

All five pages were rendered at 144 dpi and inspected.  No clipping,
collision, overflow, orphaned heading, malformed formula, missing glyph, or
unreadable table cell was found.  The long theorem transition table, fibre
atlas, exact-control table, proof endings, and bibliography were specifically
checked.

The visible byline and running heads are anonymous.  The
`GREEN_OWNER_THIN / HOLD_EXTERNAL` boundary is visible in the final section.
This artifact is ready for coordinator handoff, not external circulation.

The two later manuscript reviews are recorded separately.  Both returned
`PROVABLE AS STATED / 0 Critical / 0 Major / 0 Minor`; no source or PDF
changed.  `main_round0_original.pdf`, `main_round1.pdf`, `main_round2.pdf`,
and the live `main.pdf` are consequently byte-identical.  Current dual-review
status is documented in `README.md`, `BUILD.md`, `HOSTILE_REVIEW_A.md`,
`HOSTILE_REVIEW_B.md`, and `IMPROVEMENT_LOG.md`.
