# Independent Formal Plan Review — Raw Record

**Reviewer:** GPT-5.4, `model_reasoning_effort=xhigh`
**Invocation:** ephemeral, read-only sandbox; all reviewed bytes supplied through standard input
**Date:** 2026-08-18

The review below is preserved verbatim from the reviewer agent message.

---

VERDICT: HOLD

SCORE: 7/10

BLOCKERS
- `MAJOR` Binary paired-shell necessity is phrased too narrowly.
Location: `PLAN §5.4` bullet 3 ("Use the exact adjacent-shell formula to reject equality.") and `CLAIMS C4` ("Equality at the digit wall is rejected for b=2...").
Why it blocks: the main theorem is an iff for all `\kappa_{2,q}2^{-\sigma} >= 1`, but the dedicated binary-necessity subsection is written as endpoint-only. Equality is the delicate case, not the whole binary bad range.
Smallest repair: change §5.4/C4 wording to "reject at and below the digit wall; equality is the repaired endpoint because same-shell pinching is unavailable," and add one sentence that the same paired-shell lower bound also covers the strict-below case.

- `MAJOR` Phase/status gating is ambiguous.
Location: `PLAN` status line (`DRAFT_FOR_INDEPENDENT_PLAN_REVIEW`) versus `Appendix D` final sentence ("Until that manifest exists and replays independently, the writer state is `WAIT_PROTECTED_AUTHORITY`.")
Why it blocks: the record does not say whether `PLAN_READY` is a manuscript-plan gate or is being made contingent on a later protected-authority replay artifact. That is a phase leak into the paper plan.
Smallest repair: define the phase split explicitly (`PLAN_READY` = manuscript plan/proof structure ready; `WAIT_PROTECTED_AUTHORITY` = later external replay gate), or remove the latter from the manuscript-plan state machine.

- `MAJOR` The 15–18 page budget is not yet credible on the current outline.
Location: `PLAN` target length line, section allocations in `§§1–8`, and the `Figure and table plan`.
Why it blocks: the section minima already total about `15.25` pages and the maxima about `18.5`, before any explicit allowance for abstract space, float friction, and transition overhead. With `3` figures and `2` tables, §§5–6 are at risk of losing essential proof intuition.
Smallest repair: either trim named sections by about `1–1.5` pages total (most naturally `§2` and `§7`), or widen the target range and state that float space is included in each section estimate.

MINIMUM_FIXES
- Rewrite the binary necessity language so the `b=2` subsection covers the full nonmembership range, with equality called out only as the repaired endpoint.
- Separate manuscript-readiness status from protected-authority replay status.
- Reconcile the page budget numerically: either cut scope or raise the stated range.

NONBLOCKING_NOTES
- The theorem quantifiers are otherwise clean and consistent across `PLAN`, `CLAIMS`, `FROZEN PROOF`, and `SOURCE LOCK`: `b >= 2`, `1 <= q < infinity`, `s in C`, `sigma = Re s`, strict threshold.
- Active endpoints are otherwise correctly separated: `sigma <= 1` by the column wall, `b >= 3` by same-shell pinching, `b=2` by paired adjacent-shell pinching.
- The proof-vs-finite firewall is strong overall. Finite lanes, hostile tests, and auditor `P` are consistently described as validation/audit, not proof.
- Zero deletion is correctly handled: the positive vertex set excludes `0`, the all-zero word is removed before trace passage, and binary trace vanishing is structural rather than accidental.
- Trace-power and determinant domains are internally coherent: `r >= 2`, `sigma > 1` for trace powers and `det_2`, `sigma > alpha_b` for ordinary trace/Fredholm determinant, and only a local logarithm near `z=0` is claimed.
- The least-period ledger is correctly fenced off from complex-trace cancellation arguments.
- Ownership and bounded-search wording are disciplined. The record consistently says bounded search found no exact hit and does not claim priority or exhaustiveness.

RECHECK_CRITERIA
- `PLAN_READY` can be reconsidered once §5.4/C4 explicitly prove the full binary bad range `\kappa_{2,q}2^{-\sigma} >= 1`, not just equality.
- The status model must clearly distinguish paper-plan readiness from later protected-authority replay.
- The page budget must be arithmetically believable with the planned floats and with §§5–6 still carrying the main proof intuition in the body.
- No prose may regress on the finite-proof firewall, zero-deletion rule, determinant-domain split, or bounded-search/non-priority wording.
