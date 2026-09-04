# Proof package — P188

## Normalized objects

- `[k]={1,...,k}` and `[0]=empty`.
- `T(A)=A intersect [|A|]` on all subsets of `[n]`.
- `r_A(k)=|A intersect [k]|`, `k_0=|A|`, `k_{t+1}=r_A(k_t)`.

## Deductive chain

1. Induction gives `T^t(A)=A intersect [k_{t-1}]`.
2. The scalar sequence decreases to the first missing-position statistic
   `rho(A)`, so the endpoint is `[rho(A)]`.
3. Every nonfixed step strictly reduces cardinality. The bound
   `tail<=|A|-rho(A)` has equality `n-1` only for `{2,...,n}`.
4. Endpoint `[r]` means: contain `[r]`, omit `r+1`, choose freely above.
5. A time-`t` rank chain partitions `[n]` into nested cutoff intervals; each
   interval contributes one binomial factor and the final interval is pinned
   to the labelled target.
6. At one step, a source of size `k` contains exactly target `B` below `k`
   and chooses its other `k-|B|` elements above `k`.
7. Nonempty summation range gives the image inequality; parity splitting
   gives the Fibonacci image count.
8. Removing a target's maximum restriction bounds every nonempty fibre by a
   smaller Fibonacci number, making the empty fibre uniquely extremal.

## Failure modes excluded

- Confusing current size with original size after the first update.
- Claiming terminal time equals the number of scalar rank decreases in every
  case; the pointwise set formula is the authoritative clock.
- Counting a rank profile without enforcing all nested interval capacities.
- Omitting `n=0`, the empty target, or empty summation ranges.
- Treating a bounded non-hit as ownership clearance.
