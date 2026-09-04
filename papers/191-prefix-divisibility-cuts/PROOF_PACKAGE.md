# Proof package — P191 Round 0

## Claim

For every positive total `N`, the prefix-divisibility cut filter has the stated
fixed-state recurrence, only fixed recurrence, sharp transient height with a
unique extremizer, and complete every-target one-step fibre/image atlas.

## Status

`PROVABLE AS STATED / OWNER_AMBER / HOLD_EXTERNAL`

## Assumptions and conventions

- `Comp_N` consists of ordered positive parts summing to `N`.
- A composition `a=(a_1,...,a_k)` has internal endpoints
  `s_i=a_1+...+a_i`, `i<k`.
- The final endpoint `N` is never tested as a cut.
- Every divisibility statement uses positive divisors; all source path steps
  are positive.
- Tail is the least nonnegative time at which the orbit reaches a recurrent
  state.  The proof shows that all recurrent states are fixed.

## Proof dependency

1. The literal rule makes the next cut set a subset of the current cut set.
2. Strict cut loss rules out nontrivial cycles and characterizes fixed states.
3. Last-cut decomposition counts fixed states.
4. The permanently retained first cut bounds every nonfixed tail by `N-3`.
5. The witness `(1,2,1^(N-3))` grows its middle part by one per round.
6. Equality in the cut bound forces exactly one part two; counting the cuts to
   its right forces one leading one, proving uniqueness.
7. Source compositions are increasing paths through cut positions.
8. Prescribing retained versus deleted path vertices gives the target-local
   DP and an inverse bijection.
9. Mandatory target vertices split paths into independent intervals, giving
   the product formula.
10. Determinism partitions the source carrier and proves fibre-mass
    conservation.

## Complete proof

### 1. Coarsening and recurrence

Let `D(a)` be the internal cut set.  By definition,

`D(F(a))={s_i in D(a): a_i divides s_i}`.

Thus `D(F(a))` is a subset of `D(a)`.  Equality holds exactly when every
nonfinal part divides its endpoint.  Otherwise at least one cut is lost.
Since a finite orbit cannot regain a cut, no nontrivial cycle exists; all
recurrent states are precisely the fixed states.

### 2. Fixed-state recurrence

Set `A(0)=1`.  For `1<=v<N`, let `A(v)` count admissible cut paths ending at
`v`.  If the preceding endpoint is `u`, the last part is `v-u` and fixedness
requires `(v-u)|v`; hence

`A(v)=sum_{0<=u<v, (v-u)|v} A(u)`.

A fixed composition either has no internal cut (`v=0`) or has a unique last
internal cut `v<N`, after which the final part is unconstrained.  Its number
is therefore `sum_{v=0}^{N-1} A(v)`.

### 3. Universal clock bound

The first internal cut, when present, always survives because its part equals
its endpoint.  A composition with `k` parts therefore has at most `k-2`
deletable cuts.  A nonfixed composition cannot have `k=N`, because the unique
length-`N` composition consists entirely of ones and is fixed.  Hence
`k<=N-1`, and every nonfixed epoch deletes at least one of at most `N-3`
eligible cuts.  This proves the upper bound.  All compositions for `N<=3`
are checked directly from the rule and are fixed.

### 4. Attainment and unique extremizer

For `N>=4`, let `omega=(1,2,1^(N-3))`.  At time `t`, `0<=t<=N-3`, induction
gives

`F^t(omega)=(1,2+t,1^(N-3-t))`.

While the middle part is nonfinal, it ends at prefix `3+t`; if it divided that
prefix, it would divide the difference `(3+t)-(2+t)=1`, impossible because
`2+t>=2`.  Exactly the cut following this part disappears.  Thus the tail is
`N-3`.

Suppose another source has tail `N-3`.  Equality in both universal bounds
forces `N-1` parts and exactly one deletion per nonfixed epoch.  A positive
composition of `N` into `N-1` parts has one part two and all remaining parts
one.  If the two is first, its cut is retained; if it is final, it is not
tested.  Either placement is fixed.  Let `r>=1` be the number of leading ones
and assume the two is nonfinal.  All cuts ending parts one are always retained,
so only the growing part can remove cuts, and there are `N-r-2` such cuts to
its right.  A tail of `N-3` forces `r=1`.  The source is `omega`, proving
uniqueness.

### 5. Every-target global path DP

Fix a target with cut set `T`.  A source is uniquely a path
`0=x_0<x_1<...<x_m=N`.  Its nonfinal vertex `v=x_j` is retained exactly when
the incoming step `v-x_(j-1)` divides `v`.  A source edge cannot jump over a
target cut, because every target cut must already be a source vertex.

Declare `u->v` admissible when no member of `T` lies strictly between `u` and
`v`, and, for `v<N`, when

`[v in T] = [(v-u) divides v]`.

At `v=N` impose no divisibility condition.  With `P(0)=1`, last-edge
decomposition gives

`P(v)=sum_{u<v, u->v admissible} P(u)`.

Every source mapping to the target yields one admissible path.  Conversely,
every admissible path has retained cut set exactly `T`, so it yields one
source in the fibre.  The constructions are inverse; the fibre is `P(N)`.

### 6. Interval factorization

List target endpoints as `0=t_0<t_1<...<t_m=N`.  Between consecutive target
endpoints, every extra source vertex must be deleted.  Starting at `p`, define
`h_p(p)=1` and, for `p<v<q`,

`h_p(v)=sum_{p<=u<v, (v-u) does not divide v} h_p(u)`.

If `q<N`, the interval factor is

`K(p,q)=sum_{p<=u<q, (q-u) divides q} h_p(u)`;

for the final endpoint define

`K_*(p,N)=sum_{p<=u<N} h_p(u)`.

Every target cut is mandatory, so restriction and concatenation give a
bijection between a global admissible path and one admissible path in each
target interval.  The fibre therefore equals

`product_{j=1}^{m-1} K(t_(j-1),t_j) * K_*(t_(m-1),N)`.

This factorization includes the one-part target (`m=1`) as the sole final
factor.  Positivity is equivalent to target image membership.

### 7. Fibre mass

Every source composition has a unique image.  The fibres over all target
compositions therefore partition `Comp_N`; their sum is
`|Comp_N|=2^(N-1)`.  The verifier checks every target equality first and then
checks this mass identity, so mass is not used to hide an incorrect target
distribution.

## Boundary audit

- `N=1`: `(1)` is the only source, target, and fixed state.
- `N=2`: `(2)` and `(1,1)` are fixed; height zero.
- `N=3`: all four compositions are fixed; height zero.
- A one-part target has no internal target cut; its fibre uses only `K_*`.
- The first source cut is always retained, even after earlier cuts have been
  deleted, because the first part itself is unchanged.
- The final endpoint is never subjected to the divisibility rule.

No finite enumeration is used in these proofs.

## Open risks

- No closed scalar formula is claimed for the full image size, arbitrary
  pointwise tails, or time-`t` fibres.
- The owner search is bounded.  Non-hit is not novelty, priority, or
  freedom-to-operate evidence.

