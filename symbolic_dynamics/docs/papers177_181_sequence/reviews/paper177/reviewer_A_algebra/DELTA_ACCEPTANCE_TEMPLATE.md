# P177 Review-A Round-1 delta acceptance

**Author baseline reviewed:** `main.tex`
`3309beca09a6b0d1502913590906a46804b107385249cb629e2ef744e2c2a763`  
**Accepted live `main.tex`:**
`fb4cf3eb309e97724a53e037aaf6888881a3f57de6f1e035dc350c7dd40dc06a`  
**Accepted live `main.pdf`:**
`ff93b3bf239536ad2256948c6c2877b27435d437f71f2df7f411771a0420516c`  
**External status:** `HOLD_EXTERNAL`

| ID | Required delta | Author evidence/location | Reviewer status |
|---|---|---|---|
| P177-A-M01 | Replace the false bare endpoint-support biconditional by `a_t(L)>0`, or spell out `t=0`, `t=1`, `t>=2`; synchronize proof, claims/evidence, and self-QA; add both zero-count boundary controls | `main.tex` 111--127 and 238--251; `CLAIMS_EVIDENCE.md` C4; `SELF_QA.md` 19--21; `verify_p177.py` boundary sentinels; author canonical `boundary=history_support_t0_t1_and_t_ge_2 PASS` | **CLOSED** |
| P177-A-m01 | Synchronize the plan's theorem/lemma/remark locations with the live manuscript, preferably using labels and section names | `PAPER_PLAN.md` 19--27 uses main-theorem parts and section labels | **CLOSED** |

## Mandatory replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_A.py | cmp - CANONICAL.txt
```

Acceptance requires `0 Critical / 0 Major / 0 Minor`, a byte-identical
reviewer replay, preserved anonymity, and continued `OWNER_AMBER /
HOLD_EXTERNAL`.  Two fresh reviewer processes reproduced the canonical with
36,510 assertions.  The paper manifest passes 16/16; live `main.pdf` equals
`main_round1.pdf`, differs from the preserved Round-0 receipt, and has blank
identifying metadata.

## Disposition

`ACCEPTED / 0 Critical / 0 Major / 0 Minor open / HOLD_EXTERNAL`.
Discovery of a direct owner still overrides this repair closure.
