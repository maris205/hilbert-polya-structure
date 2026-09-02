# P163 Review B — independent proof rederivation

**Role:** Hostile Review B (neither author nor Review A)  
**Frozen manuscript:** Round 1, pinned in `PINNED_INPUTS.sha256`  
**Literal map:**
`S_n(F) = { complement(A - {a}) : A in F, a in A }` on labelled set
families over `[n]`, with `n >= 2`.

No author or Review-A verifier is imported by the Review-B control.  The
derivation below starts from the displayed literal map.

## 1. Atomic calculation

Let `A` be a nonempty `k`-set.  Its one-step successors are

```text
complement(A - {a}) = complement(A) union {a},  a in A,
```

all of rank `phi(k)=n-k+1`.  Apply the map again.  Deleting the restored
label `a` returns `A`; deleting `b in complement(A)` returns
`(A - {a}) union {b}`.  Thus `S_n^2({A})` is exactly the closed
neighbourhood of `A` in `J(n,k)`.

Boolean union preservation then identifies every even atomic iterate with a
closed Johnson ball:

```text
K_(2s)(A) = {B: |B|=k and k-|A intersect B| <= s}.
```

For a rank-`phi(k)` target `C`, its one-step predecessors in rank `k` are
`complement(C) union {c}`, `c in C`.  Every `k`-set meets `C` because
`k+phi(k)=n+1`; minimizing the Johnson distance from `A` over these
predecessors gives `|A intersect C|-1`.  Hence

```text
K_(2s+1)(A) = {C: |C|=phi(k) and |A intersect C| <= s+1}.
```

The empty atom is present at time zero and has no positive-time successor.
The formulas therefore have the exact boundary stated in the manuscript:
nonempty atoms for the two threshold formulas, the empty atom split off, and
arbitrary families obtained by union.

## 2. Mixed-rank clock and recurrent core

At even time `2s`, a nonempty rank-`k` slice fills its whole rank exactly
when `s >= e_k`; at odd time `2s+1`, it fills the dual rank exactly when
`s >= o_k`.  Distinct occupied ranks remain distinct because `phi` is a
bijection.  Consequently all slices must saturate at the same parity, giving

```text
mu(F) = max( 1_{empty in F}, min(2 max_k e_k, 2 max_k o_k + 1) ).
```

The empty family has tail zero; the singleton silent family has tail one.
These cases cannot be folded into the nonempty-support formula without the
explicit split used in the paper.

On each nonzero rank, `S_n^2` is inflationary closed-neighbourhood expansion
in a connected Johnson graph.  A periodic slice is therefore empty or the
whole layer.  Every recurrent family is precisely `U_R`, the union of the
ranks in `R`, and `S_n(U_R)=U_phi(R)`.  The rank involution has
`ceil(n/2)` orbits, so:

```text
recurrent states = 2^n,
fixed states = 2^ceil(n/2),
all remaining recurrent states form strict two-cycles.
```

This yields the stated fixed-iterate census and zeta product.

## 3. Atomic depths

The maximum Johnson distance from one `k`-set is `min(k,n-k)`.  The largest
odd defect is `min(k,n-k+1)-1=min(k-1,n-k)`.  Therefore

```text
delta_n(k) = min(2 min(k,n-k), 2 min(k-1,n-k)+1).
```

Solving by parity gives the unique rank realizing depth `d`:

```text
k_n(d) = n-d/2       if d is even,
k_n(d) = (d+1)/2     if d is odd,
```

for `0 <= d <= n-1`.  Symmetry of binomial coefficients gives exactly
`binom(n,ceil(d/2))` atomic singleton families at depth `d`.

## 4. Sharp height and central-slice rigidity

Write `k*=ceil(n/2)`.

### Even `n=2m`

Tail `2m-1` forces `e=m` and `o=m-1`; only rank `m` can attain the even
bound.  In `J(2m,m)`, the unique vertex at distance `m` from a fixed vertex
is its complement.  A nonempty rank-`m` family has covering radius `m`
exactly when it is a singleton.  Such a singleton also attains the odd
bound, proving both directions.

### Odd `n=2m+1`

Tail `2m` forces `e=o=m`.  The odd equality rules out rank `m`, so only
rank `m+1=k*` can attain it.  Equality supplies an `(m+1)`-set `C` with
`|A intersect C|-1 >= m` for every central member `A`; hence every such
`A` equals `C`.  Conversely a singleton central slice attains both bounds.

Thus, for every `n>=3`, tail `n-1` is equivalent to the central slice having
exactly one member.  Other rank slices and the silent atom are unrestricted.
With `M=binom(n,k*)`, the total is therefore

```text
M * 2^(2^n-M).
```

If the nonzero rank support is prescribed as `R`, the count is zero unless
`k* in R`; otherwise it is

```text
2 M product_{k in R-{k*}} (2^binom(n,k)-1),
```

where `2` is the optional silent atom.  Summing over supports recovers the
total.

## 5. Period-refined deepest counts

A deepest source eventually has period one exactly when its rank support is
`phi`-invariant.  On a `phi`-orbit not containing `k*`, an invariant support
is either absent (weight `1`) or occupies every rank in the orbit (weight the
product of the nonempty-slice weights).  On the orbit containing `k*`, the
central rank is forced and contributes the already extracted factor `M`; all
other ranks in that orbit must be occupied.  Multiplication over rank orbits,
together with the optional silent atom, gives exactly the manuscript's
`q_O`, `D_n^(1)`, and `D_n^(2)` formulas.

## 6. The `n=2` exception

Literal enumeration has sixteen phase states.  Four are recurrent, so the
other twelve have the sharp tail one.  Six enter a fixed state and six enter
the strict two-cycle.  The central-slice-singleton predicate selects only
eight states, so the manuscript is correct to exclude `n=2` from the
central-slice and product formulas rather than forcing it into the general
statement.

## 7. Every-target positive-time fibres

For `t>=1` and target `G`, let

```text
I_t(G)={nonempty A: K_t(A) subset G},  c_t(G)=|I_t(G)|.
```

A source maps to `G` precisely when its selected nonempty atoms lie in
`I_t(G)` and their kernels cover every target atom.  The initial empty atom is
optional and supplies the factor two.  Inclusion--exclusion over a missed
subfamily `J subset G` gives

```text
|S_n^(-t)(G)| = 2 sum_{J subset G} (-1)^|J| 2^c_t(G-J).
```

The same description proves the image criterion: `G` is an image exactly
when it is the union of all admissible kernels.  The formula is intentionally
restricted to `t>=1`.  It correctly gives fibre two for the empty target and
zero for every target containing the silent atom.

For `t>=n-1`, every nonempty source rank has saturated.  A recurrent target
`U_R` therefore has fibre

```text
2 product_{k in phi^t(R)} (2^binom(n,k)-1),
```

and every nonrecurrent target has fibre zero.

## 8. Independent falsification envelope

`verify_review_b.py` checks the literal update without importing any other
verifier.  Its frozen scope is:

- atomic kernel identities and exact atomic depths for `2<=n<=9`;
- the complete functional graph for every family at `n=2,3,4`;
- clocks, recurrent/fixed censuses, central singleton equivalence,
  support-resolved and period-resolved deepest counts;
- every target and every source for positive times through `n+1` in the full
  `n<=4` boxes, including empty/silent/`t=0` sentinels;
- symbolic support-product identities and central singleton/pair equality
  sentinels through `n=12`.

The frozen transcript reports **1,041,401 assertions**, status `PASS`.  Two
fresh runs byte-match `CANONICAL.txt`.

## Mathematical disposition

No counterexample, omitted boundary, sign/orientation error, or inconsistency
between the abstract and theorem statements was found.  The proofs are
adequate once all classical shadow, Johnson-ball, Boolean-relation, and
cover-inclusion--exclusion mechanisms receive zero contribution credit.

