# `RCS`: rank-compression support theorem spike

**Status:** `FROZEN_INTERNAL_CANDIDATE / HOLD_EXTERNAL`  
**Carrier:** all subsets of `[0,n-1]`

## Literal map

For `A={a_0<...<a_(k-1)}`, set

```text
R(A) = supp{a_j-j:0<=j<k},       R(empty)=empty.              (1)
```

The values `a_j-j` are weakly increasing and remain in `[0,n-1]`, so (1) is
a total self-map.

## Gap theorem and pointwise dynamics

For nonempty `A`, write `m=a_0` and let
`g_j=a_j-a_(j-1)` (`1<=j<k`) be its ordered positive gap word.  Then for
every `t>=0`, the ordered positive gaps of `R^t(A)` are exactly

```text
(g_j-t : g_j>t),                                                   (2)
```

in their original order; the minimum remains `m`.  Equivalently, start at
`m` and cumulatively add the entries in (2) to recover `R^t(A)`.

Hence:

1. every nonempty state is absorbed at `{min A}`;
2. the exact pointwise tail is
   `tau(A)=max_j g_j` for `|A|>=2`, and zero for `|A|<=1`;
3. the fixed set is the empty set and the `n` singletons;
4. the sharp height is `n-1`, attained uniquely by `{0,n-1}`;
5. the basin of `{m}` has size `2^(n-m-1)`, while the empty basin has size 1.

### Proof of (2)

Put `b_j=a_j-j`.  Then

```text
b_j-b_(j-1)=g_j-1.
```

Passing from the weakly increasing list `(b_j)` to its support deletes
exactly the zero differences and retains every positive difference in its
original order.  Thus one application subtracts one from every old gap and
deletes the gaps that reach zero.  Induction proves (2), and all five
consequences follow immediately.

## All-time image and every-target fibres

For `t>=1`, a nonempty target `B` occurs at time `t` if and only if

```text
max(B) + t(|B|-1) < n.                                      (3)
```

The empty target always occurs and has the unique source `empty`.

For a nonempty target `B={b_0<...<b_r}`, put

```text
S_t(z)=z+z^2+...+z^t,
L_t(B)=max(B)-min(B)+tr,
N_B=n-1-min(B).
```

Then the complete time-`t` fibre is

```text
|(R^t)^-1(B)| = sum_(s=0)^(N_B-L_t(B))
                  [z^s] (1-S_t(z))^(-(r+1)).                 (4)
```

An upper limit below zero means zero.  In particular, at `t=1`,

```text
|R^-1(B)| = binom(n-max(B), |B|).                             (5)
```

### Proof of (3)--(4)

By (2), every target gap `h_j=b_j-b_(j-1)` must come from the long source gap
`h_j+t`.  Between, before, and after these `r` distinguished long gaps, the
source may contain arbitrary ordered sequences of short gaps from
`{1,...,t}`; those gaps disappear by time `t`.  There are `r+1` slots, each
with generating function `(1-S_t(z))^-1`.  The long gaps consume
`L_t(B)` units of span and the available span after the invariant minimum is
`N_B`.  This proves (4).  Feasibility with no short gaps is precisely (3).
For `t=1`, stars and bars (or the hockey-stick identity) reduces (4) to (5).

## Enumerative corollaries

At time one, (3) says `max(B)+|B|<=n`.  Therefore

```text
|im R| = 1 + sum_(r>=1) binom(n-r+1,r) = F_(n+2).             (6)
```

Formula (2) also converts the complete depth census into the enumeration of
subsets by their maximum consecutive gap; this is a bounded-composition or
finite automaton count, not an observed-tail conjecture.

## Exact control

[`verify_combinatorial_lane.py`](verify_combinatorial_lane.py) independently
checks the literal iterate against (2), the pointwise clock, (3), and every
coefficient sum in (4) for every subset through `n=18`.  The RCS block makes
**12,103,993 assertions**.  At `n=18`, it verifies 262,144 states, 6,765
first-image targets, 19 fixed points, maximum fibre 2,002, and the unique
depth-17 source `{0,17}`.

## Residual and kill switch

The classical weak-to-strict sequence shift `x_j -> x_j+j`, stars and bars,
beta-set language, and Fibonacci counting receive zero credit.  The retained
residual is the support self-map (1), gap evolution (2), and all-time inverse
(4).  Any direct owner or routine internal transfer for that conjunction
reopens the decision.  Bounded non-hits are not novelty or release evidence.

