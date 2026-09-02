# RCD exact replacement scout

Date: 2026-09-03  
Decision: **KILL_OWNER_AND_INTERNAL_ENGINE_COLLISION**  
External status: **HOLD_EXTERNAL**

## Outcome first

Random cycle deletion (RCD) has a clean exact law, but it does not pass the
two-axis paper threshold.  Once cycle supports are exposed, its forward chain
is exactly an unequal-probability coupon collector with idle draws, and the
order of deleted cycles is the standard size-biased/Plackett--Luce order.  Its
reverse count `r(m-1)!` is correct but is a one-line marked-cycle permutation
identity.  Internally, P136 and P158 already occupy the size-biased/history
inclusion--exclusion architecture, while P105, the permanently killed S06,
and P155 occupy cycle deletion/species/fibre interfaces.  No independent
second axis survives these subtractions.

## Literal system

Fix `n>=1`.  A state is a permutation `sigma:S->S` on an arbitrary subset
`S subseteq [n]`; the empty permutation is allowed.  At each epoch sample a
uniform label `X in [n]`.  If `X` is inactive, hold.  If `X` is active, delete
the entire cycle of `sigma` containing `X`, retaining the restriction to all
other cycles.

Let the source cycles be `C_1,...,C_k`, with sizes `c_i`.  A target `tau` is
reachable from `sigma` iff it is the restriction to a union of source cycles.
Write `A` for its active set and `D` for the deleted source cycles.

## Exact t-step kernel

For every `t>=0`, the exact history count is

`H_t(sigma,tau) = sum_(J subseteq D) (-1)^|J|
                   (n-|A|-sum_(C in J)|C|)^t`,

when `tau` is a cycle-union restriction of `sigma`, and is zero otherwise.
The transition probability is `H_t/n^t`.

Proof: a successful word avoids all retained labels, may use inactive labels
freely, and must hit every deleted cycle at least once.  Inclusion--exclusion
over the missed deleted cycles gives the formula.  It includes:

- `t=0`: the identity kernel;
- holds caused by labels outside the current active set;
- zero transitions to targets which cut through a source cycle;
- all arbitrary source/target pairs, not only absorption.

## Absorption and last-survivor laws

Let `T_sigma` be the first time all source cycles have been deleted, and for
`J subseteq [k]` put `c(J)=sum_(j in J)c_j`.  Then

`P(T_sigma<=t)=n^(-t) sum_(J subseteq [k])
                         (-1)^|J| (n-c(J))^t`,

and

`P(T_sigma>t)=sum_(empty!=J subseteq [k])
                 (-1)^(|J|+1)(1-c(J)/n)^t`.

Consequently

`E T_sigma = sum_(empty!=J subseteq [k])
                (-1)^(|J|+1) n/c(J)`.

If the smallest cycle size is `s<n` and it occurs `h` times, the tail is
sharp:

`P(T_sigma>t) ~ h(1-s/n)^t`.

For the single full `n`-cycle, absorption occurs at time one almost surely.

For a specified cycle `i`, the probability that it is the last cycle deleted
is

`L_i=sum_(J subseteq [k]\{i}) (-1)^|J| c_i/(c_i+c(J))`.

This follows equivalently by ordering the first hit of the cycles: the order
is Plackett--Luce with weights `(c_1,...,c_k)`.  The verifier compares this
formula against the sum over every size-biased order and checks `sum_i L_i=1`.

These are sharp and exact, but they are standard unequal-coupon/size-biased
facts after the deterministic source cycle sizes are exposed.

## Extension-history census

Fix a target permutation `tau` on `A` and a disjoint `m`-label complement
`M`.  A full extension source capable of reaching `tau` is

`sigma=tau disjoint_union rho`, with `rho in S_M`.

Fix a nonempty history support `R subseteq M`, `|R|=r`.  The history deletes
the whole complement exactly iff every cycle of `rho` meets `R`.  The exact
number of such extensions is

`#{rho in S_M: every cycle meets R}=r(m-1)!`.

One proof distinguishes the first marked label encountered after rooting the
cycle construction; equivalently, labelled cycle species with cycles
forbidden to be entirely unmarked simplify to the same coefficient.  The
identity includes `r=m`, where all `m!` permutations qualify.

There are

`Surj(t,r)=sum_(j=0)^r (-1)^j binom(r,j)(r-j)^t`

history words with support exactly a prescribed `R`.  Hence the number of
full-extension/history pairs of length `t` leading to any fixed target with
an `m`-label complement is

`E_(m,t)=(m-1)! sum_(r=1)^min(m,t)
             binom(m,r) Surj(t,r) r`.

This extends to **all partial sources**, not just full sources.  For fixed
`R subseteq M`, `|R|=r`, the number of partial permutations `rho` on arbitrary
subsets of `M` whose every active cycle meets `R` is

`N_(m,r)=1+sum_(q=1)^r sum_(s=0)^(m-r)
                 binom(r,q) binom(m-r,s) q(q+s-1)!`.

Here `q` marked and `s` unmarked labels are active, and the leading one is the
empty extension.  Therefore, including every partial source extension, the
length-`t` source/history census is

`PE_(m,0)=1`, and for `t>=1`,

`PE_(m,t)=sum_(r=1)^min(m,t)
              binom(m,r) Surj(t,r) N_(m,r)`.

Both the full-source and all-partial-source counts are independent of the
target permutation.  This uniformity is a weakness, not a new target
geometry: all target dependence has disappeared once the complement size is
fixed.

## Exact evidence

The independent verifier uses literal partial permutations and enumerated
history words.  It imports no earlier project code.

- all 414 partial-permutation states for `n<=5`;
- 1,368,232 literal source/history executions;
- every arbitrary source/target transition through time five;
- 96 cycle-size profiles for the last-survivor law;
- 247 marked-support identities through `m=7`;
- 25 full-extension/history boxes and 30 all-partial-source boxes;
- **8,910,671 assertions**.

Two fresh runs were byte-identical to `CANONICAL.txt`; both transcript hashes
are
`889f36f6cec495983bacd942747ae4882b259717b5b698912d3ae8e8f5b5b08f`.
The verifier hash is
`67c6fb6b5aa8170f4b38349fba00065a32ea63e138d73e1a846456b0ef6b1b34`.

## Paper-threshold decision

**KILL.**  Formula correctness is not the issue.  The proposed temporal axis
is an unequal coupon collector on the source cycles; the last-survivor law is
the same size-biased ordering; and the reverse axis is ordinary marked-cycle
enumeration combined with surjection counts.  That reverse identity is too
thin and too close to P155's cycle-support fibre species to remain logically
independent.  P158 already contains the stronger same-batch pattern of a
history-support inclusion--exclusion plus every-labelled-target fibres.

No paper, reserve, or novelty claim is authorized.

## One genuinely different replacement suggestion

Scout, but do not pre-promote, the **degree-feedback jump (DFJ)** on labelled
endofunctions `f:[n]->[n]`:

`T(f)(v)=f^(1+indeg_f(v))(v)` for every `v` simultaneously.

DFJ preserves the full label set, is non-monotone, and couples cycle motion to
in-tree indegrees; it is not deletion, sampling, coupon collection,
standardization, or a fixed power map.  The first probe should ask whether a
nontrivial invariant freezes an explicit permutation action and whether
target fibres see in-tree geometry.  It is only a replacement lead, not a
survivor claim.
