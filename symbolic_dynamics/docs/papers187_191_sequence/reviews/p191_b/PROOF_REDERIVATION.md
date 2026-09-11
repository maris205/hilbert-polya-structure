# P191 Review B — proof rederivation

## Status

`PROVABLE AS STATED / C=0 M=0 m=0 / OWNER_AMBER / HOLD_EXTERNAL`

Review B rederived the mathematical package directly from the literal
prefix-divisibility cut rule and used the finite verifier only as a separate
regression receipt.

## 1. Coarsening monotonicity and fixed states

For a composition `a=(a_1,...,a_k)` of `N`, let the internal cut after part
`a_i` have old endpoint `s_i=a_1+...+a_i`. The update retains exactly those
old cuts with `a_i | s_i`. Therefore the new cut set is always a subset of
the old cut set.

Equality holds exactly when every nonfinal part divides its endpoint, so
those states are fixed. A nonfixed step strictly loses at least one cut and
can never regain it. Because the carrier is finite, every recurrent state is
fixed and only fixed.

## 2. Fixed-state recurrence

Let `A(v)` count admissible retained-cut paths ending at internal endpoint
`v`, with `A(0)=1`. If the previous retained endpoint is `u<v`, then the
incoming part has size `v-u`, and fixedness requires `(v-u) | v`. Hence

`A(v) = sum_{0<=u<v, v-u | v} A(u)`.

A fixed composition of `N` either has no internal cut or has a unique last
internal cut `v<N`; the terminal part `N-v` is not tested. Summing over all
possible last retained internal cuts gives the fixed-state count in the
paper.

## 3. Sharp clock and unique deepest state

If a composition has a first internal cut, that cut always survives because
its part equals its endpoint. A nonfixed composition with `k` parts
therefore has at most `k-2` deletable cuts. The unique composition with
`k=N` is `(1^N)`, which is fixed, so every nonfixed state has `k<=N-1` and
tail at most `N-3`.

The witness `omega_N=(1,2,1^(N-3))` attains this bound. After `t` steps,
while the middle part is nonfinal, the state is

`(1,2+t,1^(N-3-t))`.

Its middle part ends at `3+t` and cannot divide that endpoint, because it
would then divide their difference `1`. Thus exactly the following cut is
deleted at each nonfixed epoch, so the tail is `N-3`.

Uniqueness follows from equality in both bounds. A state of tail `N-3` must
start with `N-1` parts and lose exactly one cut per nonfixed epoch. Such a
composition has one part `2` and all remaining parts `1`. If the `2` is
first or last, the state is fixed. If it is internal and preceded by `r`
leading ones, then only cuts to the right of the growing block can disappear,
so the tail is at most `N-r-2`. Equality with `N-3` forces `r=1`, giving
exactly `omega_N`.

## 4. Global inverse characterization

Fix a target cut set `T`. A source composition is uniquely an increasing path
`0=x_0<...<x_l=N` through cut positions. Such a path maps to `T` exactly
when:

- no edge jumps over a mandatory target cut;
- at each nonfinal source endpoint `v`, the incoming step `v-u` divides `v`
  iff `v` is in `T`; and
- the final endpoint `N` is untested.

These conditions are necessary by the literal update rule and sufficient
because they make exactly the target cuts survive while all extra cuts are
deleted. That gives the paper's global path recurrence and the positivity
image criterion.

## 5. Interval factorization

List target endpoints as `0=t_0<t_1<...<t_m=N`. Inside a single open
interval `(p,q)`, every extra source cut must be deleted, so its incoming
step must fail divisibility. Let `h_p(v)` count deleted-cut paths from `p`
to interior point `v` under that rule. Then:

- for an internal target endpoint `q<N`, the final step into `q` must divide
  `q`, giving the internal factor `K(p,q)`;
- for the terminal endpoint `N`, no divisibility test is applied, giving the
  terminal factor `K_*(p,N)`.

Restriction to consecutive target intervals and concatenation are inverse
bijections, so the full fibre is the product of the internal `K` factors and
the final `K_*` factor.

The final endpoint exception is essential. Targets such as `(1,N-1)` are
fixed even though the final part need not divide `N`; any control that tests
the terminal endpoint undercounts those fibres.

## 6. Image and mass

Because every factor counts a set of literal interval refinements, the
product is positive exactly when the target lies in the image. Determinism
then partitions the full source carrier `Comp_N`, so the labelled fibres sum
to `2^(N-1)`.

The review verifier separately checks every carrier through `N=15` and
`164,049` exact assertions. Those computations support regression and
boundary pressure only; they do not replace the proof, and they do not
upgrade the bounded owner search into novelty or release clearance.
