# P195 Review-A delta

**Decision:** `PASS`  
**Round-0 mathematical delta:** none.  
**Round-0 source/status delta:** one historical Major and one historical Minor,
both repaired.  
**Acceptance:** accepted after author repair and same-reviewer recheck.  
**Open findings:** `Critical 0 / Major 0 / Minor 0`.

| ID | Severity | Surface | Required change | State |
|---|---|---|---|---|
| P195-A1 | Major | `main.tex`, `SOURCE_VERIFICATION.md` | Name and subtract P123 odd-component complementation and P159 parallel odd-vertex pruning.  Explicitly zero-credit the shared parity/tail/zeta/species/fibre silhouette and state the literal map distinctions. | CLOSED — installed and accepted |
| P195-A2 | Minor | abstract and closing status surface in `main.tex` | Replace the incomplete status wording with exact `OWNER_AMBER/HOLD_EXTERNAL`. | CLOSED — exact dual state appears twice |

The accepted delta did not change:

- theorem statements and formulas;
- `code/verify.py` or its canonical transcript;
- `main_round0_original.pdf`.

Post-repair author replay, reviewer replay, cold build, and visual QA all pass;
the repaired PDF is `d5dbac8e...f9c0a`.

Historical Round-0 source hashes retained for delta provenance:

```text
main.tex            d36225b96442c9581521cacbfc0d936dcd5ce2db5e4786825413b0749c5aaa10
references.bib      ad96da431dddbff6eb32642b3d24da6337356fba23d9e717c686f29974cd11f4
SOURCE_VERIFICATION e79073ee89249a6aff9de726caa89ba92c7b743ead3cd4b53feadfd2d8756941
```
