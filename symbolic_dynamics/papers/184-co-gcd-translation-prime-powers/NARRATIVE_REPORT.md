# Narrative report — P184

## Problem

For `N=p^a`, iterate the residue map
`T(x)=x+N/gcd(x,N) mod N`.  The step is the additive order of the current
residue, so the translation changes with the state.  The target is a complete
functional graph and inverse atlas, including the binary and even-exponent
boundaries.

## Mechanism

Write `x=p^v u`.  The two summands have valuations `v` and `a-v`.  Below the
midpoint, a valuation stratum is invariant and the unit coordinate translates
with period `p^v`; above it, one step falls to the complementary low stratum.
At equality `a=2h`, the unit coordinate increments consecutively until it
becomes divisible by `p`, producing a tail conveyor.  Inverting each stratum
reveals one low predecessor plus at most one injected high predecessor.

## Theorem-level progress

- Every state has an explicit tail and eventual period.
- The valuation-`v` recurrent layer has
  `(p-1)p^(a-2v-1)` cycles of length `p^v`.
- For odd `a=2h+1`, exactly `p^h` states have tail one.  For even `a=2h`,
  exactly `p^(h-1)` states occur at each depth `1,...,p`.
- Every fibre has size `0`, `1`, or `2`; empty and double fibres both number
  `p^floor((a-1)/2)`.
- Every double target and every empty target is parametrized explicitly.
- `p=2`, `a=1`, `x=0`, and the equality layer are included.

## Subtraction and status

Generic finite-ring dynamics, valuation algebra, and functional-graph
bookkeeping receive zero contribution credit.  P142 has a divisor carrier and
a divisor-valued gcd map; P128 uses polynomial gcds; P166 uses a
Hamming-weight-selected cube translation.  None transfers the literal
middle-conveyor or residue-fibre proof.

The formula-level owner search is bounded.  The manuscript makes no novelty or
priority claim and remains `HOLD_EXTERNAL`.

