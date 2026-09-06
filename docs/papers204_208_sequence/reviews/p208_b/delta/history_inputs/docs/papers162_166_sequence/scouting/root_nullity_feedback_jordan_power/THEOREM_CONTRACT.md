# Candidate theorem ceiling — not frozen for a paper

Decision: `KILL_INTERNAL_P137_PLUS_ROOT_OWNER`  
External lifecycle: `HOLD_EXTERNAL`

This file records the strongest correct theorem package found.  It is a kill
record, not a P166 allocation and not a novelty statement.

For nilpotent similarity classes of size `n>=1` under

`F([A])=[A^(1+dim ker A)]`, the following can be proved for all parameters:

1. **All-time transport.**  If `A` has type `lambda`, then
   `F^t([A])=[A^K_t]`, where
   `K_0=1` and
   `K_(t+1)=K_t(1+sum_i min(K_t,lambda_i))`.
2. **Temporal classification.**  The zero type `(1^n)` is the unique recurrent
   type and the point clock is the first `t` with `K_t>=lambda_1`.
3. **Sharp global clock.**  With `s_0=1`, `s_(t+1)=s_t(s_t+1)`, the maximum
   clock is the first `t` with `s_t>=n`, attained by `(n)`.
4. **Exact deepest boundary.**  For `lambda=(L,mu)`, the tail recursion in
   `DERIVATION_PACKAGE.md` classifies every deepest type.  If the global depth
   is `D>=1`, `(n)` is the unique deepest type iff
   `n<=2^(2^(D-1))`; `(n-1,1)` is the first extra witness after the boundary.
5. **One-step every-target inverse.**  For fixed source length, a finite
   quotient/residue flow gives a necessary and sufficient image criterion and
   an exact multiset-product fibre count for every target.
6. **Extremal zero fibre.**  Its exact Gaussian-rectangle series is (6.1), and
   it is a maximum one-step fibre by conjugation.

Items 1, 2, and the cyclic threshold form a clean feedback clock.  Items 5
and 6 do not form a sufficiently independent residual: the fixed-exponent
inverse is directly within nilpotent-root classification, while P137 already
contains the same current-length partition-feedback/clock/every-target-fibre
architecture.  No all-time closed target criterion survived.  Therefore this
contract is deliberately not promoted.

