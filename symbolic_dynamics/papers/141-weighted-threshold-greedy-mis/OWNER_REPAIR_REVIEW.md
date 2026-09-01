# Independent owner-repair review - P141 Round B

**Initial review date:** 2026-09-01 UTC  
**Closure re-review date:** 2026-09-01 UTC  
**Reviewer role:** independent hostile reviewer; did not author the manuscript or repair  
**Scope:** completed Round-B documentary owner repair, re-review of the exact `M-OR-01` closure, package-summary alignment against the frozen batch owner audit, and protected source/artifact hash preservation  
**Disposition:** **PASS / HOLD_EXTERNAL**

No paper-local file was edited during this re-review except this updated review
record.

## 1. Severity-indexed findings

### Critical

None.

### Major

None open.

Historical note: the first owner-repair review opened `M-OR-01` because
`NARRATIVE_REPORT.md` and `PAPER_PLAN.md` still lacked the full owner-thin
closure language then required. That finding is now closed; see Section 5.

### Minor

None.

## 2. Theorem and artifact consistency QA

No theorem/artifact defect was found in either the initial review or this
closure re-review.

- `main.tex` remains narrow on ownership and still assigns zero credit to the
  threshold-graph support, generic RSA/random-greedy process, and
  Plackett/exponential weighted order (`main.tex:59-66`, `main.tex:84-86`,
  `main.tex:319-324`).
- The endpoint law, inverse/simplex theorem, accepted-size PGF, marginal laws,
  and clock firewall remain internally consistent. No new overclaim appeared in
  the updated package summaries.
- `references.bib` still contains the same four owner/input references.

## 3. Protected hashes

The protected source, verifier, canonical stdout, and PDF hashes are unchanged
from the initial review:

| artifact | SHA-256 |
|---|---|
| `main.tex` | `b312ca8becfcc405de8276195058b9876c8631ae0119b882a5bf4973db2d7f6e` |
| `references.bib` | `7a9bad554745322727fac587e773a862622e7f35d5e486bbf3e6f216376f1286` |
| `code/verify.py` | `25c3a0ba8d9f8134aeee42dd98176faedc84c5d7de8852afa527df8ae3b2b5e6` |
| `code/verification_output.txt` | `bcb2e2f68121a3c13e79e0987fcd1ee5e985b225f4a948357424ed70ee695502` |
| `main.pdf` | `e87ba3878dc55e24b90c135ef2b356aae0a0ef8d33274354213c25c0d5d2b0f6` |
| `main_round0_original.pdf` | `e87ba3878dc55e24b90c135ef2b356aae0a0ef8d33274354213c25c0d5d2b0f6` |
| `main_round1.pdf` | `e87ba3878dc55e24b90c135ef2b356aae0a0ef8d33274354213c25c0d5d2b0f6` |
| `main_round2.pdf` | `e87ba3878dc55e24b90c135ef2b356aae0a0ef8d33274354213c25c0d5d2b0f6` |

PDF byte identity and permissions also remain unchanged:

- `main.pdf`: 254,394 bytes, mode `0644`
- `main_round0_original.pdf`: 254,394 bytes, mode `0444`
- `main_round1.pdf`: 254,394 bytes, mode `0444`
- `main_round2.pdf`: 254,394 bytes, mode `0444`

## 4. Current documentary hashes

| artifact | SHA-256 |
|---|---|
| `OWNER_REPAIR_LOG.md` | `224c2cf92ac9ca991be73212a65195f93f7117eafe9b5e3002b5d0381f26af68` |
| `NARRATIVE_REPORT.md` | `9b16e6755f92df010b1c0cf8d9ae8890d0a3a561f9aa2bdf6e8a476cf1dcfc96` |
| `PAPER_PLAN.md` | `a002f9d7b6debbdba8621e4d03ed9bf46a0cd9af683ebd882e205e99fb661951` |

## 5. Closure re-review - 2026-09-01 UTC

I re-read the updated `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, and
`OWNER_REPAIR_LOG.md` against the exact requirements opened by `M-OR-01`.
Every required documentary item is now present.

- `NARRATIVE_REPORT.md:3-12` and `NARRATIVE_REPORT.md:45-53` now state that the
  package is a specialized exact-law note built on fully owned threshold-graph
  support, RSA/random-greedy process, and Plackett/exponential weighted order;
  that Theorem 3.1 and its inverse/simplex, PGF, and marginal consequences are
  owner-thin and folklore-risky; and that the bounded direct-owner non-hit is
  not novelty, priority, or owner clearance.
- `PAPER_PLAN.md:5-11`, `PAPER_PLAN.md:47-52`, and `PAPER_PLAN.md:99-103` now
  replace the stale Round-1 status with Round-2 owner-summary-repair status and
  carry the same three required owner-boundary statements. It no longer has a
  stale unconditional `GO_INTERNAL / HOLD_EXTERNAL` summary.
- `OWNER_REPAIR_LOG.md:31-39` and `OWNER_REPAIR_LOG.md:62-64` now explicitly
  record the former `M-OR-01` omissions, the repair applied to
  `NARRATIVE_REPORT.md` and `PAPER_PLAN.md`, and the package-wide wording sweep
  that closed the issue.

I also re-swept the active package summaries
(`README.md`, `IMPROVEMENT_LOG.md`, `CLAIMS_EVIDENCE.md`, `FINAL_QA.md`,
`NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, and `OWNER_REPAIR_LOG.md`). Their
status strings are not byte-identical, but they are substantively consistent:
each now presents the package as owner-thin, preserves `HOLD_EXTERNAL`, and
does not recast the bounded non-hit as novelty, priority, or owner clearance.
No new overclaim or stale active status remains.

## 6. Final gate

There are **zero open critical findings, zero open major findings, and zero
open minor findings**. `M-OR-01` is closed. The protected `main.tex`,
`references.bib`, verifier, canonical stdout, and round-PDF hashes are
unchanged. The documentary owner repair now passes a package-wide summary
re-review. The correct disposition is **PASS / HOLD_EXTERNAL**.
