# Round-1 revision integrity record

Date: 2026-08-14  
Paper ID: `finite-additive-arithmetic-capacity-lma-v1`  
Candidate ID: `additive_finite_arithmetic_capacity_v2`  
Status: **ROUND1 REVISION COMPLETE / AWAITING FRESH INDEPENDENT ROUND 2**

## Review closure

Independent Round 1 returned `PASS_WITH_MINORS` (8.4/10, confidence 0.94).
The review is frozen at
`d9dffa9c37fd4eb4151f7953583100c0974407ffefd0eb104672bf8b463bab14`.
The bounded author response is frozen at
`739e851904976b967c774d0ce43737f0f5f13aa04a18428006728bfcde4175c9`.

Both required minors are closed:

1. Class M now uses the proper-and-affine finiteness lemma in a form valid for
   nonreduced schemes and explicitly invokes descent of finiteness.
2. “Sharp” is replaced by rank-plus-support/abstract-attainability language;
   K001 is explicitly target injection, and target independence is identified
   as a provenance condition.

The optional Table-1 float-placement repair is also applied.  These are
manuscript/figure-presentation changes, not a new scientific execution.

## Revision artifacts

| Artifact | SHA-256 | Check |
|---|---|---|
| `paper/manuscript.tex` | `2be0a171cf94b54a58e447bb1922a14880e69c4f80733df5a0882f0302978cb4` | revised source |
| `paper/paper_round1_revision.pdf` | `9c3b395a9d4ec704fb54951bd69d5d0fd6d9db7bb6c857f8fb45ee6e5b69c0f8` | 12 pages; conclusion ends page 9 |
| `paper/paper_pre_review.pdf` | `1be29012762238bd469a2b5e86cbc32a76e9c951ed6e524917c99bf05c0a2810` | immutable Round-1 input retained |
| `paper/figures/figure_reproducibility.json` | `382a3781f90110416610e470f5442e9e25ae040ee78b9523236020e75fbde434` | 9/9 outputs match isolated second generation |
| `paper/figures/fig1_additive_capacity.pdf` | `11f38574c9f28dc923aa5299c0f47a7a3f1c37b5bf70589e40193557eceee196` | revised vector master visually checked |

Two consecutive clean deterministic builds have identical revised-PDF hashes.
The final log has zero errors, package/LaTeX warnings, box warnings, undefined
citations/references, or duplicate labels.  All fonts are embedded and subset.
All 12 pages and the revised Figure 1 passed author-side visual inspection.
The bibliography remains closed at 18 cited records.

## Retrospective indexes

| Index | SHA-256 |
|---|---|
| `paper/PAPER_CONFIGURATION.md` | `c73ea133714aa72336d7d82ebcabe714de50e3c412c45cd51351e2cf1ae638b4` |
| `paper/CLAIM_MANIFEST.json` | `1d57f041cf9cba875a3d76bb2f6a4ecc250bd55b563011ad1da2343152fda734` |
| `paper/EXPERIMENT_PASSPORT.json` | `7096f178c2f0fe4beae4b64162e07daf2c1171977997b0fb6cd01d85a9824f85` |
| `paper/FIGURE_PACKAGE.json` | `cddb618ceea59feb8b38177ac9a9fd53c8fbc41ed33ac9d03f3223a2278e5fda` |
| `paper/PIPELINE_STATE.json` | `3ec5ba07a7376d881b2b5223f1a98e384365faede76bca26950977d7e70a1da1` |

## Immutable official evidence

The source lock, official result, registry, exclusive result manifest, JUnit,
proof/scope ledgers, deployment review, and upstream bindings are unchanged.
In particular, the official audit remains 9/9 gates and 51/51 tests, with one
registered static run, zero numerical candidates, zero target matches, and no
prime-table, target-array, numerical-logarithm, or Riemann-zero access.

## Independence boundary

This record is an author-side revision check.  It is not an independent
Round-2 review and does not finalize the paper.  A fresh reviewer must verify
the two repairs, rebuilt PDF, and retrospective indexes.
