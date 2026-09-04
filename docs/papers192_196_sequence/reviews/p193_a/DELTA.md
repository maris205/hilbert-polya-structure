# P193 Review-A delta

**Decision:** `PASS`  
**Round-0 mathematical delta:** none.  
**Round-0 source delta:** one historical Major, repaired.  
**Acceptance:** accepted after author repair and same-reviewer recheck.  
**Open findings:** `Critical 0 / Major 0 / Minor 0`.

| ID | Severity | Surface | Required change | State |
|---|---|---|---|---|
| P193-A1 | Major | `main.tex`, `references.bib`, `SOURCE_VERIFICATION.md` | Cite Schipper--Zhang, arXiv:2504.01280; zero-credit mutual-best blocking-pair dynamics; distinguish its stochastic/sequential process from P193's fixed-order simultaneous permutation map; retain `OWNER_AMBER/HOLD_EXTERNAL` and no novelty language. | CLOSED — installed and accepted; repaired PDF `b5b2f4e7...ad0d9` |

The accepted delta did not change:

- theorem statements and formulas;
- `code/verify.py` or its canonical transcript;
- `main_round0_original.pdf`.

Post-repair author replay, reviewer replay, cold build, and visual QA all pass.

Historical Round-0 source hashes retained for delta provenance:

```text
main.tex            3a217db814e618e445eaa7591daf4962432a36f5f9e5530b9d66a5b1947a9841
references.bib      a427a43b8adf6142661ff0763cb6af6b50a31af09b8657120763c8f5a89625c4
SOURCE_VERIFICATION ac6a81439cd8e059a6c3d394a27563f40c927599726ee73451e3303004c48233
```
