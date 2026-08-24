# C130 paper plan

**Title:** An All-Period Nonlattice Suspension Determinant with Exact Clock-Sector Separation

**Type:** compact theory/certificate note

**Date:** 2026-08-24

**Target length:** two pages
**One-sentence contribution:** A mixing two-state suspension with roof
`(1,sqrt(2))` has an exact primitive Euler/trace determinant and injective
symbol-count clock sectors, while roof `(1,2)` restores lattice collision and
vertical periodicity.

## Claims--evidence matrix

| Claim | Evidence | Status | Paper location |
|---|---|---|---|
| mixing finite-type source | positive `B` | proved | Sec. 1 |
| explicit determinant | `det(I-M)=1-u-v` and exponential specialization | proved | Sec. 2 |
| all-period primitive identity | trace-log regrouping by primitive root | proved | Sec. 2 |
| clock-sector separation | Q-linear independence of `1,sqrt(2)` | proved | Sec. 3 |
| no orbit-level injectivity | two period-six necklaces in sector `(3,3)` | proved | Sec. 3 |
| rational lattice recovery | collision at time 2 and `2*pi*i` period | proved | Sec. 4 |
| Route-A boundary | no target comparison or natural lift | audited | Sec. 5 |

## Structure

1. **Abstract.** State the source, determinant, all-period identity, sector
   separation, rational control, and target boundary.
2. **Frozen mixing suspension.** Define the full shift, suspension, roof, and
   population-vector length.
3. **Bivariate owner and primitive identity.** Derive the matrix determinant,
   all-order traces, formal primitive product, and its analytic convergence
   domain after specialization.
4. **What irrationality separates.** Prove vector-level injectivity, retain
   the same-sector orbit collision, and rule out nonzero imaginary periods.
5. **Rational-roof control.** Exhibit the cross-sector collision and recovered
   lattice polynomial/periodicity.
6. **Replay and Route-A boundary.** Give the exact prefix table, independent
   tests, strict tuple, and nonclaims.

## Figure/table plan

No decorative or data plot is needed: every relation is exact and the compact
note is clearer without a hero diagram.  One table reports rooted words,
primitive cycles, and sector counts for periods 1--10.  Its data source is
`results/c130_suspension_evidence.json`; the producer and checker reconstruct
every entry.  This completes the figure phase with zero manual figures and one
reproducible exact table embedded directly in LaTeX.

## Citation plan

No external priority or literature claim is made, so the note uses no
citations and needs no bibliography.  The source audit records this choice.

## Review risks and minimum fixes

- **Risk:** overstate Q-linear independence as orbit injectivity.  **Fix:** add
  the two primitive period-six necklaces sharing `(3,3)`.
- **Risk:** state the infinite product globally.  **Fix:** give the absolute
  convergence half-plane and separate it from entire continuation of `d_tau`.
- **Risk:** call the product arithmetic.  **Fix:** consistently say
  “intrinsic dynamical Euler product” and repeat the scope firewall.
- **Risk:** rational control changes too much.  **Fix:** state that only the
  roof pair changes.

## Reverse-outline check

The section topic sentences read in order as: freeze one mixing suspension;
derive its exact all-period owner; delimit sector separation; reverse it with a
rational control; report replay and stop at the Route-A boundary.  Every
section serves the same claim.
