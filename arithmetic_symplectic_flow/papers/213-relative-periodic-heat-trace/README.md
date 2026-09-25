# Relative periodic-channel heat trace

**Paper ID:** 213-relative-periodic-heat-trace  
**Candidate ID:** AQC-20260916-RHT01  
**Status:** CONTROL ADVANCE — RELATIVE PERIODIC-CHANNEL TRACE RECOVERS THE POSITIVE-TIME ORBIT COMB; FULL-STATE TRACE NOT SUPPLIED; NATURALNESS OPEN.  
**Type:** EXTERNAL REPRESENTATION CONTROL.  
**Formal Route coordinates:** UNASSIGNED. **Route B:** NOT INVOKED.

For each actual circle of the [194 flow](../194-rapid-decay-cone-completion/README.md),
subtract its windowed covering-line heat trace from its circle heat trace.
Both operators are genuinely trace class at a finite atom cutoff.
The paired difference cancels zero winding and leaves Gaussian peaks
at the actual repeat times. Removing the atom cutoff first and then
letting the heat parameter vanish gives, on open positive time,

    sum_a sum_(m>=1) (log a) delta_(m log a).

The coefficients and repeats follow from the actual circle-cover kernel
trace, not added prime-power weights. Exact Gaussian bounds justify the
infinite sum without a prime-distribution estimate.

This is not an ordinary trace of either infinite sector. It is also not
a full-state trace: the [205 invariant-measure channel](../205-invariant-measure-support/README.md)
already loses mixed-state observations. It does not act on 204 H or
borrow 201's determinant. Advance the relative localization benchmark;
stop its promotion to a full-state or natural-arithmetic realization.

- [Full proof and controls](paper.md)
- [Frozen card and appended outcome](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence and actual review](evidence/README.md)

Review bindings and actual verification receipts belong to the evidence
record, not to this navigation summary or a formal Route assessment.
