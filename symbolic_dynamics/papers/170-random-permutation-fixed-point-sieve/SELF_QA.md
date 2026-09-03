# P170 author self-QA (historical Round 0)

**Result:** `PASS / AUTHOR_ROUND0_FREEZE`  
**External lifecycle:** `HOLD_EXTERNAL_OWNER_THIN`

## Mathematical statement audit

- The map is literal: `A -> A ∩ Fix(pi)` with independent uniform
  permutations, and the state space is the labelled Boolean lattice.
- The endpoint formula includes `t=0` and gives zero for noncontained targets.
- The sole positive-time support obstruction—full source to an
  `(n-1)`-point target—is stated in the main theorem and proved in both
  directions.
- The Boolean eigenbasis is explicit, and the only repeated rank eigenvalue
  `lambda_(n-1)=lambda_n` is not hidden.
- The absorption formulas are limited to `n>=2`; the nonabsorbing `n=1`
  state is separate.
- The repaired `n=3` survival formula combines the rank-two and rank-three
  terms.  The two-distinct-scale expansion is stated only for `n>=4`.
- The marked polynomial is defined by literal histories before its
  alternating form, which justifies coefficient nonnegativity.
- Both marked-degree endpoints are proved attainable.  The upper witness
  splits `d=0`, even `d`, odd `d>=3`, and `d=1`; the last case explicitly
  uses a label outside `A` guaranteed by the support criterion.
- The conditional expectation is restricted to supported endpoints, so the
  denominator is positive.

## Proof/verification separation

All parameter-uniform statements have proofs in `main.tex`.  The independent
author program supplies finite exact counterexample pressure only.  Two
fresh verifier processes produced byte-identical stdout with 481,935
assertions.  No floating-point comparison is used.

## Ownership and citation audit

- Five references are necessary and cited in the text.
- Each record was checked against a DOI resolver and a primary arXiv record.
- Common fixed points, fixed-set inclusion--exclusion, semilattice spectra,
  absorption transforms, and the ordinary cycle polynomial are assigned zero
  contribution credit.
- P158/P162 random-intersection proximity is explicitly subtracted.
- The bounded owner-search non-hit is never presented as novelty or priority
  evidence.

## Build, visual, and anonymity audit

- Canonical build: settled with zero warnings, bad boxes, unresolved
  citations/references, or errors.
- Source-only cold builds: 2/2 byte-identical with the canonical PDF.
- Frozen PDF: four A4 pages; canonical and `main_round0_original.pdf` are
  byte-identical.
- Visual inspection: all four pages at 144 dpi, with no clipping, overlap,
  stranded heading, illegible formula, or malformed reference.
- Fonts: 23/23 embedded, subsetted, and Unicode-mapped.
- Metadata: title/author/subject/keywords/creator/producer blank; no forms,
  JavaScript, or encryption.
- Text scan: visible author is `Anonymous`; no personal identifier, TODO,
  placeholder, review verdict, or release claim appears.

No author-side issue remained open at the Round-0 boundary.

Both later hostile manuscript reviews returned
`ACCEPT_INTERNAL / PROVABLE AS STATED / 0 Critical / 0 Major / 0 Minor`,
and neither changed the source or PDF.  The four live/round PDF paths are
byte-identical.  Current dual-review closure is recorded in `README.md`,
`BUILD.md`, `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, and
`IMPROVEMENT_LOG.md`; external status remains `HOLD_EXTERNAL`.
