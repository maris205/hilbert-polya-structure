# Author response to independent manuscript review — Round 1

**Review verdict received:** `MINOR_REVISION` (7.4/10)  
**Response date:** 2026-08-14  
**Status:** `ALL_ROUND1_ITEMS_IMPLEMENTED_AWAITING_INDEPENDENT_ROUND2`  
**Independence boundary:** this response and its checks are author-side; they
do not constitute an independent Round-2 review.

We thank the reviewer for locating the false categorical cell in Figure 2 and
the deeper provenance weakness that allowed it.  We accepted every required
item and all five minor suggestions.

## Required repairs

### R1 — `log|A|` cell

**Implemented.**  The Figure-2 row is now exactly

```text
log|A| : EDGE | STOP/OUT | STOP/OUT
```

under `formula applies | algebraicity retained | target-log conclusion`.
Thus the paper no longer suggests that `log|A|` is certified algebraic or
that the target-log exclusion applies to it.

### R2 — literal cell-level provenance

**Implemented.**  `paper/figures/scope_matrix_ledger.py` now derives all 27
cells through named, fail-closed predicates.  Every cell carries one of two
explicit provenance classes:

- `FROZEN_JSON_DERIVED`: obtained from named predicates in the official
  source-locked JSON records;
- `THEOREM_DEFINED`: a stated theorem hypothesis/consequence, edge case, or
  explicit nonclaim, never represented as a raw computational result.

The complete record is
`paper/figures/fig2_scope_matrix_provenance.json`.  Figure 2 consumes only this
derived ledger.  Five paper-stage assertions verify all 27 statuses and named
evidence, the corrected `log|A|` row, and fail-closed mutations of the
`log|A|`, algebraic-gauge, and `beta=0` predicates.

The manuscript caption and figure package now describe this mixed provenance
literally.  The final column was renamed from `prime-log conclusion` to
`target-log conclusion` so that the `beta=0,1` edge rows are semantically
accurate.

## Minor items

### M1 — deductive primary evidence

**Implemented.**  Claims C4 and C8 now use `notes/PROOF_PACKAGE.md` as primary
evidence.  `control_audit.json` and `henon_static_audit.json` are explicitly
listed as supporting implementation evidence.

### M2 — projective hyperplane wording

**Implemented.**  Theorem 5.1 now says that a positive-dimensional projective
component would intersect the fixed hyperplane `Z=0`, where the preceding
argument shows there is no point.  This removes the ambiguous phrase “meet a
hyperplane.”

### M3 — arXiv identifier

**Implemented.**  The compiled bibliography now prints
`arXiv:2412.01668 [math.DS], v2` as plain bibliographic metadata, with no raw
URL rendered in the PDF.

### M4 — Figure-1 orange label

**Implemented.**  The long machine classification was replaced by the larger,
two-line human label “Map-only countercontrol: transcendental normalization.”

### M5 — conservative novelty position

**Retained.**  The paper continues to disclaim a historical first or new
transcendence theorem and retains
`MERGE_IF_STANDALONE_DEPTH_IS_REQUIRED`.

## Author-side validation

- Figure-2 assertion suite: **5/5 PASS**.
- Unmodified official safe code suite: **82/82 PASS**.
- Consecutive full figure regenerations: **10/10 artifacts identical** (nine
  visual outputs plus the 27-cell provenance JSON).
- Consecutive manuscript builds: **identical SHA-256**.
- Revised PDF: **13 pages**, conclusion ends on page 10; all fonts embedded
  and subset; zero errors, warnings, box warnings, undefined references, or
  undefined citations.
- Revised PDF SHA-256:
  `871197f5a385f68accf6d3ba7876e5df830e9eef43b4bf9e9ae52a3edb7bc996`.
- Immutable Round-1 input snapshot retained at
  `paper/paper_pre_review.pdf`, SHA-256
  `2e8f2cef866f06e219fb0d582aec8ad4a1403b26e61cf8f44549dbc4f8399742`.
- Source lock and all 35 official result-manifest inputs remain unchanged;
  candidate parameter/orbit/action execution and prime/zero access remain
  zero.

The revised manuscript is ready for a fresh independent Round 2.  No author
self-check in this response is offered as an independent acceptance verdict.
