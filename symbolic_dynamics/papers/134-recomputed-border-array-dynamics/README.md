# P134 — whole-array recomputation of border arrays

Status: **GO_INTERNAL / ROUND 2 FROZEN / HOLD_EXTERNAL**.

Internal anonymous Stage-2 short-paper package.  The map treats an ordinary
border table as a new integer word and recomputes its **entire** border table at
each step.  It is not classical composition along the failure links of one
fixed word.

The manuscript proves:

- image equals the valid border arrays;
- one fixed point at `n=1` and exactly `n-1` two-cycles for `n>=2`;
- the indexed mismatch amplifier and sharp maximum depth
  `0,0,1,2n-4` for `n=1,2,3,n>=4`;
- the all-target fibre bound `(n-1)!`, attained only by `0^n` and
  `010^(n-2)` for `n>=2`.

Core files:

- `main.tex`, `references.bib`: anonymous manuscript source;
- `code/verify.py`, `code/verification_output.txt`: deterministic paper-local
  audit and raw canonical stdout;
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`: claim design;
- `BUILD.md`, `CONTROL_RESULTS.md`: build and control records;
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, `HOSTILE_REVIEW.md`: two
  independent review rounds and their consolidated verdict;
- `FINAL_QA.md`, `SHA256SUMS`: terminal artifact audit and frozen manifest.

Replay the exact control with:

```bash
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)
```

`main_round0_original.pdf` is the frozen initial draft and
`main_round1.pdf` records the Review-A repair.  Hostile Reviews A and B are
complete; Round B requested one manuscript cross-reference repair and two
package-index updates.  External novelty, priority, authorship, posting,
submission, and release remain `HOLD_EXTERNAL`.

Round-zero audit: 1,694,506 exact verifier assertions; raw stdout `cmp=0`;
5 A4 pages; 322,388 bytes; PDF SHA-256
`958d05206b1b5a50456bddf9533d65c757b407a54728d79f3308da5f5e74c829`.
