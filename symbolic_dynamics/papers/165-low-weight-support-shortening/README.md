# P165 — iterated low-weight support shortening

**Status:** `ROUND-2 ACCEPT_INTERNAL / 0C-0M-0m TWICE / OWNER_THIN / HOLD_EXTERNAL`.

This anonymous AMS note studies the autonomous code map that shortens the
current code on the union of supports of all words of weight strictly below
twice its current minimum distance, retaining those ambient coordinates as
zeros.  After subtracting the entire one-step hitting-set shortening
principle, the frozen residual consists of:

- the unique zero recurrent state and sharp height
  `floor(log2(n+1))`;
- an every-time image equivalence for every prescribed nonzero target;
- universal dimension and new-support lower bounds for every such source;
- the exact structure and count of the sources simultaneously attaining both
  bounds.

The package does not give a complete target-fibre formula.  In particular,
the zero-target exact-depth minimal layer is kept separate from the full
zero fibre.

## Artifact map

- `main.tex`, `references.bib` — anonymous manuscript source and verified
  bibliography.
- `main.pdf` — current settled canonical PDF.
- `main_round0_original.pdf`, `main_round1.pdf`, `main_round2.pdf` —
  byte-identical Round-0, Round-1, and Round-2 freezes.
- `HOSTILE_REVIEW_A.md` — process-separated first hostile review.
- `HOSTILE_REVIEW_B.md` — process-separated second hostile review.
- `PAPER_PLAN.md` — page and claim architecture.
- `NARRATIVE_REPORT.md` — residual mathematical story.
- `PROOF_PACKAGE.md` — full dependency map and boundary-aware proof.
- `CLAIMS_EVIDENCE.md` — claim/proof/control ledger.
- `SOURCE_VERIFICATION.md` — primary-source verification and mandatory
  owner subtraction.
- `CONTROL_RESULTS.md` — exact assertion inventory.
- `SELF_QA.md` — mathematical, build, font, metadata, anonymity, and visual
  audit.
- `FINAL_QA.md` — final verifier, review, build, PDF, and lifecycle closure.
- `code/verify.py`, `code/CANONICAL.txt` — independent deterministic
  verifier and frozen transcript.
- `BUILD.md` and retained build logs — replay and PDF freeze record.

## Replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
cmp code/CANONICAL.txt <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)
```

Hostile Review A independently rederived the complete residual contract and
returned `0 Critical / 0 Major / 0 minor`.  Its 1,574,098-assertion verifier
used independent finite-field and code enumeration implementations, and two
fresh replays were byte-identical.  Because no change was requested,
`main_round1.pdf` is byte-identical to both Round 0 and the current PDF.
Hostile Review B independently returned `0 Critical / 0 Major / 0 minor`.
Its 1,220,460-assertion verifier used true finite-field arithmetic over
`F_2`, `F_3`, `F_4`, and `F_5`; two fresh replays were byte-identical.  It
also repeated the owner subtraction and two source-only cold builds.  No
repair was requested, so `main_round2.pdf` is byte-identical to every prior
freeze and to the current PDF.

Internal completion does not authorize posting, submission, circulation, or
author contact.
