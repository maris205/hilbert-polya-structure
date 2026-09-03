# P179 Review-A Round-2 science re-entry acceptance

**Frozen Round-0 baseline:** `main.tex`
`a5d19d7049f896079d03fe377bcaaff43f7d247545b57946d8c4ca80cf89ac31`  
**Round-1 source previously accepted:** `main.tex`
`cb7886a6846a4a8019c6636f77bbe9faa5cd8fbc342bbde6c822d57286938b7b`  
**Final Round-2 source accepted:** `main.tex`
`94ff9a5e84d50473b9c48afeb79098bd83cec1e848612e18b71b0b24ac03bbb6`  
**Final Round-2/live PDF accepted:**
`6c93451aa6116c32164ee0d255315f88e0299b60c2ba17879d73c75309e1773c`  
**Decision:** `ROUND2_SCIENCE_REENTRY_ACCEPT / THEOREM_ACCEPT / HOLD_EXTERNAL`  
**Current open findings:** `0 Critical / 0 Major / 0 Minor`  
**Owner ceiling:** `OWNER_AMBER`; a later literal or equivalent owner
supersedes this acceptance and activates withdrawal.

## Closure ledger

| ID | Required delta | Final evidence | Status |
|---|---|---|---|
| P179-A-m01 | State `n>=1` before defining the transition operator and retain the `n=1` boundary | `main.tex:52-60` fixes `n>=1`; `main.tex:231-235` retains the full `n=1` evaluation. | **CLOSED** |
| P179-A-m02 | Subtract P169/P110 locally without novelty language and synchronize the owner boundary | `main.tex:62-82`, `SOURCE_VERIFICATION.md:12-26`, and the claims/narrative ledgers distinguish the mechanisms, assign shared shells zero credit, and preserve `OWNER_AMBER / HOLD_EXTERNAL`. | **CLOSED** |
| P179-R2-support | Retain the unselected residual `B\A` whenever nonempty, explicitly including a singleton residual | `main.tex:89-105` states and proves the exact blockwise action. The PDF contains the corrected sentence. The author oracle at `code/verify_p179.py:66-74,174-183` directly compares this block formula with literal isolation for every partition and support through `n=7`. | **CLOSED** |

## Theorem-consistency re-audit

The corrected support lemma says that selected labels in an old block become
singletons and all unselected labels remain together whenever any remain.
Thus a residual of size at least two is the target's unique nonsingleton block,
whereas residual sizes zero and one both give a discrete restriction of the
target to that old block. Consequently:

- absorption is still exactly `|M cap B_j|<=1` in every old block;
- the kernel's nonsingleton alternative still forces `M cap B=C`;
- the kernel's discrete alternative correctly allows `|M cap B|<=1`;
- exact-time positivity remains `r=0=t` or `1<=r<=t`;
- spectrum, recurrence, and both inverse censuses are unaffected.

No formula changes, missing target type, or new boundary counterexample was
found. The `t=0`, `n=1`, and impossible `n-1` singleton layer remain explicit.

## Exact byte and replay ledger

| artifact | SHA-256 |
|---|---|
| final `main.tex` | `94ff9a5e84d50473b9c48afeb79098bd83cec1e848612e18b71b0b24ac03bbb6` |
| final `main.pdf` | `6c93451aa6116c32164ee0d255315f88e0299b60c2ba17879d73c75309e1773c` |
| `main_round2.pdf` | `6c93451aa6116c32164ee0d255315f88e0299b60c2ba17879d73c75309e1773c` |
| immutable `main_round1.pdf` | `9c6018baa87f9e772a46e70cafb59cc804f6711c3a1b82852327df4b00f8bd7d` |
| immutable `main_round0_original.pdf` | `c0a97f79c22799e90b3c2bd95d0060b4b75b38b28536332e5d60fe38f2a5f923` |
| `references.bib` | `29bb56b0b3e4e321659901b704c5823536e7d776e75d9bfffc1dfa7bc26f1afb` |
| author `code/verify_p179.py` | `200b1b2ded1158bff7632ccf8b8cd27403da3757abeb713f82f99c297034a6c5` |
| author `code/CANONICAL.txt` | `e0264ffec9f83da16e45d00ed1801963137c107368c75ef46204addec609f2cf` |
| paper-local `SHA256SUMS` (not self-listed) | `5dca779e23a2c8e1474fd029b023c561e3c2bd7f7f0459f1866672072ae7ee7b` |
| Reviewer-A `verify_review_A.py` | `9a43674c9fec5d757cd147931d474da60ea8d21ffcd16bf2179e3e22f65a7792` |
| Reviewer-A `CANONICAL.txt` | `fc18daa304ffb67d49f8f43ff6488d2b86d140e652ac7ae74567fe4f910272f2` |

On the exact final source/PDF binding above, two fresh Python processes each
produced Reviewer-A output byte-identical to its canonical:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_A.py | cmp - CANONICAL.txt
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_A.py | cmp - CANONICAL.txt
```

Each independent replay made **120,977 assertions** using bit-block
partitions, exact characteristic polynomials, literal count propagation,
inclusion--exclusion support weights, and a separately coded admissible-set
kernel. In particular, its discrete-target branch explicitly includes both
empty and singleton missing residuals. The author verifier separately replayed
byte-identically at **252,320 assertions**, including **127,202** new direct
support-formula comparisons and the canonical sentinel
`SUPPORT_RESIDUAL_SINGLETON=PASS`.

`main.pdf` is byte-identical to `main_round2.pdf` and distinct from the two
immutable earlier receipts. The source says `Anonymous`; `pdfinfo` reports
blank Title, Author, Creator, Producer, Subject, and Keywords, with no metadata
stream or JavaScript. The refreshed non-self-referential paper manifest
verifies all **18/18** listed artifacts, including `FINAL_QA.md`, the final
author control/canonical, and all three immutable PDF receipts.

A final provenance-only synchronization renamed the claims and source-ledger
headers to `Round 2/final`, corrected `FIGURE_PLAN.md` to describe the actual
three-page note, and changed the improvement-log attribution from
“independent” to “late final” science audit. It did not change `main.tex`, any
PDF, either verifier or canonical, any theorem claim, or either assertion
total.

This acceptance is internal only. It does not authorize posting, submission,
external circulation, or any authorship action.
