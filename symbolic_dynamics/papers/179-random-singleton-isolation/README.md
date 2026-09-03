# P179 — Random singleton isolation on set partitions

**Round-2 result:** dual-review-frozen anonymous three-page short paper.

**Status:** `ROUND2_DUAL_REVIEW_FREEZE / OWNER_AMBER / HOLD_EXTERNAL`.

The chain chooses a uniform label and isolates it from its current block.  The
paper proves a complete diagonal spectrum, arbitrary-initial-block absorption
CDF, every labelled source-to-target probability, and two exact one-step
inverse censuses.  The impossible `n-1` singleton layer and `n=1` boundary are
included.

Artifacts:

- `main.tex`, `references.bib`: anonymous manuscript source;
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `FIGURE_PLAN.md`: claim architecture;
- `CLAIMS_EVIDENCE.md`: proof/control traceability;
- `SOURCE_VERIFICATION.md`: bounded source audit and contribution subtraction;
- `code/verify_p179.py`: standard-library exact regression control;
- `IMPROVEMENT_LOG.md`, `BUILD.md`, `SELF_QA.md`: repair, build, and author
  QA receipts.
- `FINAL_QA.md`: final review, cold-build, and PDF gate.

The paper-local verifier makes **252,320 exact assertions**, including an
exhaustive formula-versus-literal check for one-label residual blocks.  The immutable
Round-0 PDF has SHA-256
`c0a97f79c22799e90b3c2bd95d0060b4b75b38b28536332e5d60fe38f2a5f923`;
the immutable Round-1 PDF has SHA-256
`9c6018baa87f9e772a46e70cafb59cc804f6711c3a1b82852327df4b00f8bd7d`.
After the final science audit corrected the statement of the support lemma,
the Round-2 and live PDFs have SHA-256
`6c93451aa6116c32164ee0d255315f88e0299b60c2ba17879d73c75309e1773c`.

No external circulation, posting, submission, or authorship action is
authorized.
