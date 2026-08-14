# Hostile review — round 2

Date: 2026-08-14

Input: round-one revised HCS-P56 manuscript, primary certificate and
independent checker

Decision: **PASS**

## Independent stress test

The revised paper was attacked at the four load-bearing interfaces:

1. the all-\(m\) insertion formula was recomputed from cyclic windows rather
   than imported from the primary producer;
2. the period-six radical orbit, trace conjugate and reciprocal quartic were
   recomputed symbolically;
3. the strict excess inequality was reduced to its integer comparison rather
   than accepted numerically; and
4. the width-five interpolation matrix was inverted directly.

All four attacks agree with the manuscript.  In particular, the modulo-13
test now closes the multiplier-field claim; the inequality
\(709^2>104\cdot3902\) certifies the direction of the four-block obstruction;
and the selected width-five minor has determinant \(+1\).  The constant-row
and family notation are now disjoint.

## Strongest surviving objection

The relation
\[
 \Delta_m=\Egal_{A_m}+\Egal_{B_{m+2}}
 -\Egal_{A_{m+1}}-\Egal_{B_{m+1}}
\]
has only two currently evaluated values.  Therefore no asymptotic behavior,
recurrence, or Hölder contradiction is established.  This is not a defect in
the revised claim: §7 explicitly presents exponential decay as a necessary
condition and names its verification or refutation as the open theorem.

## Findings

### CRITICAL

None.

### MAJOR

None.

### MINOR

None unresolved.

## Verification receipt

- exact all-width proof: PASS;
- direct finite check for \(3\leq m\leq64\): PASS;
- period-six recurrence residuals and sign word: PASS;
- trace and multiplier polynomials: PASS;
- modulo-13 irreducibility witness: PASS;
- exact four-block separation: PASS;
- width-five determinant and interpolation values: PASS;
- one-sided/two-sided Hölder scope firewall: PASS;
- Route A/B non-promotion: PASS;
- primary/independent/test suite: PASS.

No unresolved Critical or Major finding remains.
