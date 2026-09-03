# Value-index stable reranking: proved descent, unresolved sharp clock

**Lifecycle:** `HOLD_EXTERNAL`.  **Decision:** `KILL_UNCLOSED_CLOCK_SCORE_RERANK`.

For `pi in S_n`, set

```text
F(pi)_i = stable rank of pi_i+i among (pi_j+j)_(j=1)^n,
```

with lower position breaking ties.  This preserves rank and is neither an
extractor nor a pruning map.

For `i<j`, the output has an inversion at `(i,j)` exactly when

```text
pi_i-pi_j > j-i.                                  (1)
```

Hence `Inv(F(pi))` is contained in `Inv(pi)`.  The containment is strict for
every nonidentity permutation: a nonidentity permutation reverses some pair
of consecutive values, and that pair cannot satisfy (1).  Thus the identity
is the unique recurrent state and every orbit converges to it.  This is a
genuine all-parameter result, stronger than a raw finite signature.

The identity fibre is also exact.  `F(pi)=id` iff

```text
pi_i+i <= pi_(i+1)+(i+1) for every i,
```

or equivalently every adjacent descent of `pi` drops by exactly one.
Successively locating `1` shows that such a permutation is uniquely obtained
by cutting `1,2,...,n` into consecutive intervals and reversing each
interval.  Therefore

```text
|F^(-1)(id)| = 2^(n-1).
```

Exhaustive functional graphs through `S_8` have unique identity recurrence,
maximum tails

```text
1,2,3,3,4,4,5       for n=2,...,8,
```

and maximum fibre `2^(n-1)`, attained at the identity.  The tail suggests a
short clock near `floor(n/2)+1`, but no sharp proof or every-target inverse
was closed.  General target fibres are linear extensions of a system of
difference inequalities prescribed by the target order; no compact transfer
matrix emerged.  Since score reranking is already a dense internal
neighbourhood and the requested second axis is missing, the candidate is
killed rather than promoted from a pattern.
