# Refinement Report

**Date:** 2026-08-06  
**Final verdict:** `READY FOR PROOF PHASE`  
**External numeric score:** unavailable and not fabricated

## Outputs

- final proposal: `FINAL_PROPOSAL.md`
- review summary: `REVIEW_SUMMARY.md`
- experiment/proof plan: `EXPERIMENT_PLAN.md`
- tracker: `EXPERIMENT_TRACKER.md`

## Main refinement

The dominant claim changed from a conditional Wigner--Kirkwood heat
asymptotic to an unconditional strict ground-state rearrangement theorem.  The
exact heat coefficient remains a supporting contribution and determines the
next proof task.

## Evidence added

- R300 production identity: maximum discrepancy \(5.03\times10^{-15}\).
- independent 60-digit checker: passed.
- independent proof review: strict ground-state theorem survived unchanged.
- full project regression: 54 tests passed.

## Pushback/drift log

| Temptation | Decision | Reason |
|---|---|---|
| entropy-divisor operator containing \(\zeta(s)^2\) | rejected | arithmetic is installed and Hénon coupling risks being decorative |
| global \(a=1.02\) cycle zeta | rejected | mixed phase and prior negative operator evidence |
| individual-zero validation | forbidden | P remains open |
| large FEM rerun | rejected | R108 branch is terminal and unnecessary for the theorem |

## Remaining open lemma

Prove a relative, noncompact heat-kernel remainder
\(R_{a,h}(t)=o(\log^2(1/t))\), ideally \(O(t\log^4(1/t))\).

