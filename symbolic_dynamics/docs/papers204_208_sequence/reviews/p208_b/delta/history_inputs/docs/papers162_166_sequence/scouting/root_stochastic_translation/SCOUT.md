# Root stochastic replacement scout — random translation intersection

**Code:** `RTI`  
**Carrier:** all subsets of `V=F_2^d`  
**Status:** `SELECT_GREEN_PENDING_INDEPENDENT_HOSTILE_GATE`  
**Lifecycle:** `HOLD_EXTERNAL`

## 1. Literal process and the early signal

From a current subset `A subseteq V`, sample `v` uniformly from `V` and set

```text
A <- A intersect (A+v).
```

For a history `v_1,...,v_t`, let `H_t=span(v_1,...,v_t)`.  The decisive
identity is

```text
A_t = E_(H_t)(A_0) := intersection_(h in H_t) (A_0+h).       (1)
```

Indeed erosions compose by addition of their structuring sets, and in
characteristic two the subset sums of the sampled translations are exactly
their linear span.  Thus history order and all linear dependencies disappear,
but the process does **not** reduce to independent coordinate deaths: the
output consists of the whole `H_t`-cosets contained in the source.

## 2. Exact temporal theorem

For a fixed `r`-subspace `H`, the number of ordered length-`t` histories with
span exactly `H` is

```text
S(t,r)=product_(i=0)^(r-1) (2^t-2^i).                        (2)
```

Consequently

```text
P(dim H_t=r)
 = [d choose r]_2 S(t,r) / 2^(dt).                           (3)
```

The only absorbing states for the full random update family are the empty
set and `V`.  Every `A != V` is empty once `H_t=V`, and this synchronization
bound is sharp for `A=V\{0}`: for every proper `H`, a coset disjoint from
`H` survives in `E_H(V\{0})`.  Therefore its exact absorption CDF is

```text
P(T<=t)=0                                      for t<d,
P(T<=t)=product_(i=0)^(d-1)(1-2^(i-t))         for t>=d,       (4)
```

and

```text
E T = sum_(r=0)^(d-1) 1/(1-2^(r-d)).                         (5)
```

This gives an all-parameter sharp stochastic clock, not only an upper bound.

## 3. Every-target, source-size-weighted history fibres

Let `B subseteq V`, put `b=|B|`, and let

```text
Stab(B)={v in V:B+v=B},       s=dim Stab(B).
```

For fixed `H`, equation (1) can equal `B` only when `H<=Stab(B)`.  Then the
source must contain every point of `B`, while on every other `H`-coset it may
choose any proper subset.  Hence the complete polynomial over both sources
and ordered histories is

```text
sum_(A, history: A_t=B) z^|A|
 = z^b sum_(r=0)^s [s choose r]_2 S(t,r)
     ((1+z)^(2^r)-z^(2^r))^(2^(d-r)-b/2^r).                  (6)
```

Formula (6) resolves every target, every time, and every source cardinality.
At `z=1` it gives the unweighted target history fibre.  At `t=0` it reduces
to the identity monomial `z^b`, including the empty and full boundaries.

The target dependence is real.  At one step the unweighted fibre is

```text
F_1(B;1) = 1,                                      if s=0;
           1 + (2^s-1) 3^(2^(d-1)-b/2),            if s>=1.  (7)
```

The separate `s=0` line is essential: then a nonzero translation cannot
stabilize `B`, and the formal half-integer exponent that can occur for odd
`b` is not to be evaluated.  Once `d` and `|B|` are known, the one-step fibre
strictly recovers the translation-stabilizer dimension `s` (with the value
one identifying `s=0`).  The phase size `2^(2^d)` recovers `d`.  This is a
separate inverse-statistical axis beyond the span clock.

## 4. Proof decomposition

The theorem uses three visibly different objects:

1. erosion composition proves the sufficient statistic (1);
2. finite-field matrix rank gives (2)--(5); and
3. a coset-by-coset proper-subset construction plus the subspace lattice of
   `Stab(B)` gives the weighted inverse atlas (6) and recovery law (7).

Removing any one of these leaves the other two intact.  In particular, the
fibre polynomial is not a marginal of the full-rank absorption law.

## 5. Exact falsification pressure

The deterministic standard-library verifier independently:

- applies literal translations and intersections for every subset and every
  history through `d=3`, with histories through time four (and longer smaller
  boxes);
- compares every target and every source-size coefficient with (6);
- checks history order/dependency collapse to (1);
- enumerates fixed-span and full-rank histories through `d=4`;
- checks the sharp witness `V\{0}` for every subspace through `d=6`; and
- checks that the one-step fibre depends exactly on `(|B|,s)` and is strictly
  increasing in `s` wherever two stabilizer dimensions occur.

Result: `1,508,298` assertions, `STATUS PASS`.  Two independent runs produced
the same row digest
`8c4b60461fbb0ea02333a1d120f7dda4e0cd1a46b26a53a98673b6a6f601727a`.
Computation is counterexample pressure only.

## 6. Intake decision

The exact span clock, the target-stabilizer weighted inverse atlas, and the
recovery law make `RTI` paper-sized on the author side.  Its erosion primitive
and rank law are classical and must receive zero credit.  A fresh hostile
review must still attack direct stochastic-morphology ownership and the
P109/P115/P158/CNG boundaries before any paper number is assigned.
