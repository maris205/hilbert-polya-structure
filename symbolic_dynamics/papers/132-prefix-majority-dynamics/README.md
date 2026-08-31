# P132 — synchronous prefix-majority dynamics

Status: **GO_INTERNAL / ROUND 2 FROZEN / HOLD_EXTERNAL**.

Internal anonymous short-paper package.  External release, novelty, priority,
authorship, posting, and submission are all on hold.

Core files:

- `main.tex`, `references.bib`: manuscript source;
- `code/verify.py`, `code/verification_output.txt`: deterministic exact audit;
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`: claim design;
- `BUILD.md`, `CONTROL_RESULTS.md`: reproduction and control record;
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, `HOSTILE_REVIEW.md`: two
  independent review rounds and their consolidated verdict;
- `FINAL_QA.md`, `SHA256SUMS`: terminal artifact audit and frozen manifest.

The exact-control replay is:

```bash
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)
```
