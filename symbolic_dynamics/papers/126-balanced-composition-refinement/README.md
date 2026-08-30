# P126 — Synchronous balanced refinement of compositions

Status: **ANONYMOUS ROUND-2 FINAL FREEZE / GO_INTERNAL /
HOLD_EXTERNAL**.

The literal map synchronously sends each composition part `m>1` to
`(floor(m/2),ceil(m/2))`.  The paper's central advance is not the familiar
logarithmic splitting clock.  For every `t`, with `K=2^t`, it proves a
canonical normal form for the complete kernel of the iterate, a suffix-code
image decoder, a product formula for every nonempty fibre, and a bijection
that enumerates the full iterated image.

Key files:

- `main.tex`, `references.bib`, `main.pdf` — anonymous manuscript;
- `main_round0_original.pdf` — immutable pre-review PDF;
- `main_round1.pdf` — owner/firewall and boundary-condition rewrite;
- `main_round2.pdf` — support-only final-review freeze;
- `code/verify.py` and `code/verification_output.txt` — deterministic exact
  control and canonical transcript;
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`,
  `CONTROL_RESULTS.md`, `BUILD.md` — audit package.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_A_REENTRY.md`,
  `HOSTILE_REVIEW_B.md`, `HOSTILE_REVIEW.md`, `FINAL_QA.md` — two-review
  closure and final sign-off.

The independent pre-paper gate is
`../../docs/papers122_126_sequence/phase1/HOSTILE_GATE_BALANCED_COMPOSITION_REFINEMENT.md`.
It required the canonical-kernel rewrite now implemented here.  Review A then
required explicit primary-source and internal-corpus subtraction before
re-entry.  Parallel morphisms, binary fragmentation and balanced splitting,
generic suffix/unique-decoding theory, restricted-composition machinery,
Chinn--Heubach no-part-2 enumeration, and divide-and-conquer clocks receive
zero contribution credit.  The explicit internal firewall covers
P094/P108/P113/P115/P122/P123/P125.

No novelty, priority, authorship, submission, or external-release decision is
made.
