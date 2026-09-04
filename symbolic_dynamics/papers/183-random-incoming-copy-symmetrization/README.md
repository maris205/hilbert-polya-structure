# P183 — Random incoming-copy symmetrization

**Final status:** `ROUND2_DUAL_REVIEW_FREEZE / OWNER_AMBER / HOLD_EXTERNAL`.

The chain selects a uniform vertex of a loopless labelled directed graph and
copies its incoming star to its outgoing star.  The paper proves exact conflict
deletion, the independent-set absorption CDF, the first-occurrence-order
source-to-target kernel, and labelled/distinct one-step fibre formulas.

Artifacts:

- `main.tex`, `references.bib`: anonymous manuscript source;
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `FIGURE_PLAN.md`: claim architecture;
- `PROOF_PACKAGE.md`: normalized assumptions and complete deductive route;
- `CLAIMS_EVIDENCE.md`, `SOURCE_VERIFICATION.md`: evidence and owner ledgers;
- `code/verify_p183.py`, `code/CANONICAL.txt`: exact author-side controls;
- `BUILD.md`, `SELF_QA.md`, `IMPROVEMENT_LOG.md`, `FINAL_QA.md`: build,
  dual-review, and terminal-QA receipts.

The author control contributes 47,033 exact assertions.  Two
process-separated hostile reviews contribute 2,784,180 more, with zero open
finding.  All three immutable receipts and the four-page live PDF are
byte-identical with SHA-256
`6834170a0ee554a9f4c75040aad762326e24fa5a532e7987c57025be02bd235b`.
Two source-only cold builds reproduce those bytes.

No external circulation, posting, submission, or authorship action is
authorized.
