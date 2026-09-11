# P188 proof rederivation and counterexample audit

## 1. Pointwise iterate and endpoint

Fix `A subseteq [n]`, let `r_A(k)=|A cap [k]|`, and define
`k_0=|A|`, `k_(t+1)=r_A(k_t)`.  At the first step,

```text
T(A)=A cap [k_0].
```

If `T^t(A)=A cap [k_(t-1)]`, that set has size `k_t`.  Applying the rule
again intersects it with `[k_t]`; since `k_t<=k_(t-1)`, the result is exactly
`A cap [k_t]`.  This proves the displayed all-time identity for every
`t>=1`.  The original source `A` remains the rank reference throughout; no
illegal replacement by the current iterate occurs.

Let `rho` be the longest initial segment contained in `A`.  The rank chain
never falls below `rho`.  If `k>rho`, then `rho+1` is missing from `A cap[k]`,
so `r_A(k)<=k-1`.  Thus the chain reaches `rho`, remains there, and the
pointwise formula gives endpoint `[rho]`.  Hence all recurrence is fixed and
the fixed states are precisely the initial segments.

Endpoint `[r]` requires `[r] subseteq A`, omission of `r+1` when `r<n`, and
arbitrary choices above it.  This yields `2^(n-r-1)` sources for `r<n` and
one source at `r=n`.  The rule and count remain valid at `n=0` and `n=1`.

## 2. Exact tail and unique deepest source

If a size-`k` set lies in `[k]`, it is `[k]` and is fixed.  Therefore every
nonfixed arrow strictly decreases cardinality.  An orbit ending at `[rho]`
has tail at most `|A|-rho`.

- If `rho=0`, omission of `1` implies `|A|<=n-1`.
- If `rho>0` and the state is nonfixed, omission of `rho+1` implies
  `|A|-rho<=n-rho-1<n-1`.

Thus equality in the global bound can occur only at `rho=0`, `|A|=n-1`.
There is only one such source, `{2,...,n}`.  Its update successively removes
`n,n-1,...,2`, giving exactly `n-1` arrows before the empty fixed state.
For `n=0,1`, direct carrier analysis gives only fixed states.  Exhaustion
through `n=16` found no second maximizer or off-by-one clock.

## 3. Every-time labelled target formula

Let the target be `B`, `b=|B|`, `M=max(B)` with `M(empty)=0`, and fix a rank
chain ending in `k_t=b`.  The nested cutoffs partition the carrier into

```text
(k_0,n], (k_1,k_0], ..., (k_(t-1),k_(t-2)], [k_(t-1)].
```

The outside interval contains `k_0-k_1` source elements.  Interval
`(k_j,k_(j-1)]` contains `k_j-k_(j+1)` source elements.  The last interval is
not freely chosen: its source intersection must equal the labelled target
`B`, which requires `k_(t-1)>=M`.  The resulting number for one fixed chain
is therefore

```text
C(n-k_0,k_0-k_1)
  * product_(j=1)^(t-1) C(k_(j-1)-k_j,k_j-k_(j+1)).
```

Every source has one rank chain, and each permitted collection of interval
choices reconstructs one source, so summing the product neither omits nor
duplicates a predecessor.

At `t=1` there is no intermediate interval: setting `k_1=b` leaves exactly
`C(n-k_0,k_0-b)`.  At `t=0` the map is the identity and the fibre is one.
At `t>=n-1`, the sharp-height theorem has already sent every source to its
endpoint, so precisely the terminal basins remain.

The reviewer evaluates this formula backwards from `(k_(t-1),k_t)` through
interval capacities, unlike the author's forward weak-chain enumeration.
Direct frozenset fibres agree for all targets through `n=10` and every time
from zero through `n+2`; every formula slice sums to `2^n`.

## 4. One-step image, Fibonacci counts, and the unique maximum fibre

For a source of size `k` to map to `B`, the target must lie in `[k]` and the
remaining `k-b` source elements must be chosen above `k`.  Thus

```text
max(b,M)<=k<=floor((n+b)/2),
```

and summing `C(n-k,k-b)` over this range gives the stated fibre.  Because
`M>=b` for a nonempty target (and both are zero for the empty target), the
range is nonempty exactly when `2M<=n+b`.

A size-`b` image target can consequently be any `b`-subset of
`[floor((n+b)/2)]`.  Splitting by the parity of `n-b` changes the layer sum
into the two standard binomial forms `F_(n+1)` and `F_n`, giving image size
`F_(n+2)`.  At the empty target the fibre itself is
`sum_k C(n-k,k)=F_(n+1)`.

For nonempty `B`, write `j=k-b` and discard only the lower restriction from
`M(B)`.  This gives

```text
|T^-1(B)| <= sum_(j>=0) C(n-b-j,j)=F_(n-b+1)<=F_n.
```

For `n>=2`, `F_n<F_(n+1)`, so the empty target is the unique maximum.  At
`n=1`, both fibres equal one, exactly as stated; at `n=0`, there is one fibre.

## 5. Counterexample pressure and disposition

The reviewer-owned control is independent code, uses frozensets rather than
bit masks, and uses a backward interval transfer rather than the author's
chain generator.  It records 8,193,247 successful assertions covering all
dangerous quantifiers named in the review request.

| severity | count | rationale |
|---|---:|---|
| Critical | 0 | no false theorem, carrier failure, or counterexample |
| Major | 0 | all-time formula, stabilization, and extremal proofs close uniformly |
| Minor | 0 | boundary conventions and theorem wording need no correction |

Verdict: `PROVABLE AS STATED`.  The finite boxes are not substituted for any
of the deductions above and carry no novelty or ownership implication.
