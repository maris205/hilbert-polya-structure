# P203 — Least monochromatic-triangle complementation

Date: 2026-09-05 UTC. **ROUND2_FROZEN / INDIVIDUAL_TERMINAL_PASS /
OWNER_AMBER / HOLD_EXTERNAL**. Actual A accepted a scope-only repair;
actual B accepted unchanged after full proof/source/build work. Root's
fresh double replay and package gate passed before Round2. Two terminal
cold builds, all four final page views and the full five-paper artifact
audit have passed. PAPER_IMPROVEMENT_STATE.md and the batch FINAL_QA_REPORT.md
control completion, not historical author-stage labels.

## Main result

On all simple labelled graphs, complement the three edges of the least
monochromatic triple and hold if none exists. The maximum entrance time is
max(0,n−3), with a no-return structural proof and an all-size witness.
Complete target-local D/C clauses give every inverse fibre. Its maximum is
1 for n≤3 and max(4,n−2) for n≥4; S/K certificates characterize every
maximizing target, with both star and four-face alternatives at n=6.

The manuscript is four pages with all proofs included. Classical induced
complementation, minimum-involution recurrence, Ramsey facts and the
Johnson static classification/capacity receive zero contribution credit.

## Files and reproducibility

- main.pdf, main_round1.pdf and main_round2.pdf: accepted repaired four-page PDF.
- main_round0_original.pdf: preserved original four-page author PDF.
- main.tex, references.bib, BUILD.sh: standalone source-only build inputs
  and executable deterministic build recipe; details in BUILD.md.
- verify_p203.py, CANONICAL.txt, REPLAY_LOG.md: standalone author verifier,
  two actual byte-identical runs of374,812 assertions on33,868 states n≤6.
- PAPER_PLAN.md, NARRATIVE_REPORT.md, FIGURE_PLAN.md, PROOF_PACKAGE.md,
  CLAIMS_EVIDENCE.md: exact narrative, full proof transcription and scope.
- SOURCE_VERIFICATION.md, PROVENANCE.md: primary-source credit, internal
  owner boundary and the explicitly unrepaired historical archival defect.
- current_inputs/: physical exact current mathematical/archival snapshots,
  checked by CURRENT_INPUTS_SHA256SUMS; no upstream runtime import.
- sources/: actual downloaded primary bytes and their manifest.
- qa/: preserved author draft/build evidence, not the later terminal builds.
- qa_final/, FINAL_QA.md: two new terminal builds and four actual final views.
- frozen_round0/: physical source, verifier, PDF, memos and current inputs,
  with its own complete manifest. ROUND0_RECEIPT.md identifies exact pins.
- revision_a/, A_RESPONSE.md: preserved author repair before A acceptance.
- frozen_round1/, ROUND1_RECEIPT.md: actual accepted A version and transition.
- frozen_round2/, ROUND2_RECEIPT.md: actual unchanged B version and transition.
- SHA256SUMS: complete current artifact tree except that manifest
  itself; this is evidence integrity, not reviewer acceptance.

## Non-negotiable provenance and review boundary

One intermediate Stage1 author probe was not physically retained. The old
temporal input list still gives3PASS/1FAIL; the historical Stage1 Minor1 is
not repaired. The current manuscript and code use no missing program as
runtime or proof dependency. Its actual snapshots are supplied, and both
actual paper reviews adjudicated their own complete current inputs.

Fifth/LZK are mathematical co-contributors, not independent reviewers.
temporal_author_audit.md is specifically an author-side compression check.
The optional independent-gate vertex-zero lemma is not used. The two actual
manuscript reviews and actual terminal PASS are separately recorded.
No external upload, notification, novelty clearance or release is authorized.
