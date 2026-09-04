# P184 — Co-gcd translation on prime-power residues

**Final status:** `ROUND2_DUAL_REVIEW_FREEZE / OWNER_AMBER / HOLD_EXTERNAL`.

For `N=p^a`, the paper determines
`T(x)=x+N/gcd(x,N) mod N`.  It proves every valuation-stratum orbit, the
even-exponent middle conveyor, complete cycle and tail censuses, and an exact
`0/1/2` fibre atlas with double/empty targets parametrized explicitly.

Artifacts:

- `main.tex`, `references.bib`: anonymous manuscript source;
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `FIGURE_PLAN.md`: claim architecture;
- `PROOF_PACKAGE.md`: normalized assumptions and complete deductive route;
- `CLAIMS_EVIDENCE.md`, `SOURCE_VERIFICATION.md`: evidence and owner ledgers;
- `code/verify_p184.py`, `code/CANONICAL.txt`: exact author-side controls;
- `BUILD.md`, `SELF_QA.md`, `IMPROVEMENT_LOG.md`, `FINAL_QA.md`: build,
  dual-review, and terminal-QA receipts.

The author control contributes 109,478 exact assertions.  Two
process-separated hostile reviews contribute 4,509,168 more, with zero open
finding.  All three immutable receipts and the four-page live PDF are
byte-identical with SHA-256
`991e9eae521268083d5eabb02d5ff536a40eefe000aa970ce23d6c97ea8888ab`.
Two source-only cold builds reproduce those bytes.

No external circulation, posting, submission, or authorship action is
authorized.
