# Integrity after Round-1 revision

**Status:** `POST_ROUND1_AUTHOR_INTEGRITY_PASS`  
**Document date:** 2026-08-14  
**Integrity runtime:** 2026-08-13 UTC container clock  
**Scope:** author-side verification after implementing the independent
Round-1 `MINOR_REVISION`; this is **not** an independent Round-2 verdict and
does not claim final submission readiness.

## Review closure

- Independent Round-1 review:
  `paper/reviews/round1_review.md`, SHA-256
  `7eae9c589e61521fb9829c560f971dea3483c724f39899da004de2338b6ee016`.
- Author response:
  `paper/reviews/round1_response.md`, SHA-256
  `3c8b88dd630d0c8b45a7589b25b21294a2bc4164b5c85d43ff6d58e0f9a5ca6b`.
- Required repairs: **2/2 implemented**.
- Minor repairs: **5/5 implemented**.
- Pipeline state:
  `ROUND1_REVISION_COMPLETE`, SHA-256
  `1f644c6d5a9193c1b1c48f737477b8454e143820c79cbb508e1d002b9f50276c`.
- A fresh independent Round 2 remains mandatory.

## Scientific correction and provenance

The corrected Figure-2 `log|A|` row is

```text
EDGE | STOP/OUT | STOP/OUT
```

for `formula applies | algebraicity retained | target-log conclusion`.
No cell now claims algebraicity or target-log exclusion for this
post-processed observable.

Every Figure-2 cell is produced by
`paper/figures/scope_matrix_ledger.py` and classified as either:

- `FROZEN_JSON_DERIVED`, based on a named predicate over the official frozen
  result package; or
- `THEOREM_DEFINED`, based on a named hypothesis, deduction, edge case, or
  explicit nonclaim and never described as raw computation.

The machine-readable 27-cell record is
`paper/figures/fig2_scope_matrix_provenance.json`, SHA-256
`944dc0eed6d1b6640058eb1bb2131260832e402c30ef5a3f752a5f12414819af`.
Five mutation/assertion tests pass.  Consecutive regeneration reproduced all
nine visual outputs and the provenance record byte for byte (10/10).

Claims C4 and C8 now name the deductive proof package as primary evidence and
the static JSON only as supporting implementation evidence.  The Hénon
zero-dimensional proof now names the fixed hyperplane `Z=0` explicitly.  The
bibliography prints the arXiv identifier as bibliographic metadata without a
raw URL, and Figure 1 uses a readable human countercontrol label.

## Frozen experiment closure

- Source lock v3 is unchanged at SHA-256
  `d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7`.
- All 35 official inputs in `results/final_result_manifest.json` rehash
  correctly and were not rewritten by this manuscript revision.
- The official JUnit remains unchanged at 82 tests, zero failures, and zero
  errors; a fresh safe execution also passed 82/82.
- Candidate parameter substitution, periodic-point computation, candidate
  action computation, external prime-table access, and Riemann-zero-data
  access remain false.
- The all-period conclusion remains deductive; no static cell or audited
  period is used as its proof.

## Compilation integrity

Two consecutive clean prescribed builds produced identical PDFs.

| Check | Result |
|---|---|
| Revised snapshot | `paper/paper_round1_revision.pdf` |
| PDF SHA-256 | `871197f5a385f68accf6d3ba7876e5df830e9eef43b4bf9e9ae52a3edb7bc996` |
| Pages | 13 total; conclusion and References heading on page 10 |
| Page size | letter, 612 x 792 pt |
| LaTeX errors / warnings | 0 / 0 |
| Overfull / underfull boxes | 0 / 0 |
| Undefined references / citations | 0 / 0 |
| Fonts embedded and subset | PASS |
| Changed figures and affected revised pages visually inspected | PASS |
| Deterministic repeat-build hash | PASS |

The immutable Round-1 input snapshot remains
`paper/paper_pre_review.pdf`, SHA-256
`2e8f2cef866f06e219fb0d582aec8ad4a1403b26e61cf8f44549dbc4f8399742`.
The one-page increase is due to the revised flow of references/appendices; the
main text through the conclusion still ends on page 10.

## Revised artifact hashes

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `41ed1c1492da4f1cc8ff1cb7747c97c2ecf1f313c2390469219485b5c1d087aa` |
| `paper/references.bib` | `e0b0c45f5fc65b6938652a3365dab95906d4fb4312a2cc6b16665bec3d9b05b7` |
| `paper/paper_round1_revision.pdf` | `871197f5a385f68accf6d3ba7876e5df830e9eef43b4bf9e9ae52a3edb7bc996` |
| `paper/FIGURE_PACKAGE.json` | `1ff4314af146746c79e9f9b608f5ad913994f30c1c70c4c9c52bb2f7a9321b50` |
| `paper/CLAIM_MANIFEST.json` | `09719787a52315d27a5dadaff74971290c4977d09b224d8a86d84b8e3f0ed10f` |
| `paper/PAPER_CONFIGURATION.md` | `a144291913984ddffa9af2ba467b16442e535ddbbe4177dfe616d00d2dad05e4` |
| `paper/PIPELINE_STATE.json` | `1f644c6d5a9193c1b1c48f737477b8454e143820c79cbb508e1d002b9f50276c` |
| `results/final_result_manifest.json` | `6b3dbfed68dbd058056c35139756d5ccbb4e9f3b9a263ccaddef64bb183326e7` |

## Handoff

The bounded Round-1 revision is complete and ready for an independent Round 2.
No final acceptance, final integrity, or repository-sync status is asserted
here.
