# C80 experiment plan

1. Bind the C75 coordinate and twenty-subgroup rows, C76 support count/minimal
   support count, and C78's canonical evidence and manifest bytes.
2. Reconstruct the named closure transition table from the point-set group law.
3. For each target row (H) and each of all 65536 masks, compute
   \(τ_H(D)\) by a minimum over restorations.  A dynamic-programming recurrence
   over retained masks is used by the producer; the checker uses the complete
   target-containing minimal supports obtained independently by enumeration.
4. Record the twenty-component profile for every deletion mask, target
   threshold distributions, and \((|D|,\tau_H)\) coefficient tables.
5. Check \(τ_Q=ρ\) byte-for-byte against C78's all-mask repair atlas,
   marginal totals, monotonicity in (H), and the exact polynomial tables.
6. Run a separate integer/combinatorial cross-check, clean replay, hostile
   semantic mutations, two isolated LaTeX builds, visual inspection, and a
   prefreeze manifest.

No arithmetic/local, Euler-factor, root-number, automorphy, Burnside-ring,
table-of-marks, or Hilbert--Polya claim is made.
