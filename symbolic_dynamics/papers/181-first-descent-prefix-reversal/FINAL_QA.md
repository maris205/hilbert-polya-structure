# P181 final Round-2 QA

**Decision:** `ROUND2_DUAL_REVIEW_ACCEPTED / 0 OPEN`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

## Exact-control gate

| Process | Representation and scope | Exact assertions | Replay | Open findings |
|---|---|---:|---|---:|
| Author | tuple permutations; literal update, image, incoming sets, tails, cycles, depth-two bijection, maximizers through `S_9` | 6,273,070 | byte-identical | — |
| Review A | factoradic codes; edge arrays, indegree peeling, reverse BFS, fibre histograms, First Sort negative control through `S_9` | 17,364,060 | two fresh byte-identical processes | 0 Critical / 0 Major / 0 Minor |
| Review B | string permutations; direct incoming sets, orbit traversal, complete small boundaries, First Sort negative control through `S_8` | 377,591 | two fresh byte-identical processes | 0 |

The author control is paper-local.  Both reviewer controls are
process-separated and use different representations.  All enumeration is
falsification pressure; the infinite-family claims rest on the manuscript's
all-parameter proofs.

## Round provenance

```text
Round-0 PDF:
1df6b41b097c29cc933123906fa1539a37c0944bd843d007204c07b2dc824ad0

Round-1 PDF:
57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861

Round-2 PDF:
57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861

Live PDF:
57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861
```

Round 1 adds the complete `S_1` atlas requested by Review A.  Round 2 changes
no theorem source: it records Review-A delta acceptance and the independent
Review-B closeout.  The live PDF, `main_round1.pdf`, and `main_round2.pdf` are
byte-identical; the immutable Round-0 receipt remains distinct.

## Mechanical and visual gate

```text
pages: 3
bytes: 345,290
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
font rows: 28
embedded/subsetted/Unicode rows: 28/28/28
bibliography entries: 3
encrypted: no
forms: none
JavaScript: no
identifying metadata fields: blank
```

Both source-only cold builds reproduce the live PDF SHA-256 exactly.  The
three final raster pages were inspected for clipping, overlap, blank pages,
broken glyphs, theorem continuity, bibliography legibility, and running
furniture; no defect was found.

## Claim, source, and lifecycle gate

- The image, recurrent core, depth census, complete target fibres, maximum
  fibre, maximizing set, and `n=1,2,3` atlases agree across manuscript,
  author control, and both hostile reviews.
- The Project Euler First Sort follower-to-front operation remains an
  explicit negative control, not a name or owner for P181.
- All three bibliography entries are cited and retain their verified limited
  roles.  Generic prefix reversal, sorting, descent statistics, and
  finite-map bookkeeping receive zero contribution credit.
- A bounded owner-search non-hit is not novelty, priority, freedom to operate,
  or release permission.  The accepted theorem package remains
  `OWNER_AMBER / HOLD_EXTERNAL`.

**Final internal disposition:** theorem package accepted with zero open
hostile-review findings; external circulation is not authorized.
