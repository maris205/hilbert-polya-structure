# Proof Package: rootward active-pile coalescence on a path

## Claim

Let `S` be a finite subset of the nonnegative integers with `0 in S`. From a
state `S != {0}`, choose `v in S\{0}` uniformly and replace `S` by

$$
C_v(S)=(S\setminus\{v\})\cup\{v-1\}.
$$

Let `T_S` be the number of updates until the state is `{0}`. The promotion
claim consists of the following statements.

1. Absorption is certain and the probability generating functions satisfy

   $$
   G_{\{0\}}(z)=1,\qquad
   G_S(z)=\frac{z}{|S|-1}
   \sum_{v\in S\setminus\{0\}}G_{C_v(S)}(z).
   $$

2. If `S={s_0,s_1,...,s_r}` with
   `0=s_0<s_1<...<s_r`, and `h` is defined by

   $$
   h(a,a)=0,\qquad h(0,b)=b,
   $$

   $$
   h(a,b)=\frac12+
   \frac{h(a-1,b)+h(a,b-1)}2\quad(0<a<b),
   $$

   then

   $$
   \mathbb E[T_S]=\sum_{i=1}^{r}h(s_{i-1},s_i).
   $$

3. For every nonabsorbing rooted state,

   $$
   \operatorname{supp}(T_S)
   =\{\max S,\max S+1,\ldots,\sum_{x\in S}x\}.
   $$

4. For the full state `S_n={0,1,...,n-1}`,

   $$
   \mathbb E[T_{S_n}]
   =\sum_{m=1}^{n-1}\frac{(2m-1)!!}{(2m-2)!!}
   =\frac{4}{3\sqrt\pi}n^{3/2}+O(n^{1/2}),
   $$

   and, for `n>=2`,

   $$
   \Pr(T_{S_n}=n-1)=\frac1{(n-1)!}.
   $$

The separately observed identity

$$
\Pr\!\left(T_{S_n}={n\choose2}\right)
=2^{-{n-1\choose2}}
$$

is not part of the proved promotion claim in this report.

## Status

`PROVABLE AS STATED` for Claims 1--4 above.

The maximum-endpoint probability is retained as exact finite evidence and a
separate proof obligation. It is not used in the GO decision.

## Assumptions

- Occupancy is a set: a collision erases multiplicity.
- Only occupied nonroot sites are eligible; the discrete scheduler is uniform
  over those sites.
- Every update is one deterministic step toward root zero.
- The carrier is a finite path large enough to contain `S`.
- `T_S` counts effective updates, not elapsed continuous time and not lazy
  empty-site clock rings.

## Notation

- `Phi(S)=sum_{x in S}x` is the total-position potential.
- `M(S)=max S` for `S != {0}`.
- `N_t` is the number of occupied nonroot sites after Poissonization.
- `tau_i` is the lifetime of the interface between labels initially at
  `s_{i-1}` and `s_i`.
- `h(a,b)` is the mean continuous meeting time of two ordered rate-one
  pure-death paths started at `a<b`, with zero fixed.
- `S_k` in the simple-walk formula denotes a length-`k` simple symmetric
  random walk, not an occupied set.

## Proof Strategy

Use a strict potential for absorption and the PGF. For the main mean theorem,
Poissonize the uniform-active chain, label initial piles, express the active
pile count as a sum of interface-survival indicators, and apply the counting
process compensator plus Tonelli. Solve the adjacent two-path mean by a
ballot/reflection calculation. Prove the complete support interval by
induction on `Phi`. The minimum endpoint mass then follows from the unique
descending all-collision schedule.

## Dependency Map

1. Absorption and the PGF use only strict decrease of `Phi`.
2. Interface additivity uses the Poissonized graphical construction, the
   identity `N_t=sum_i 1{tau_i>t}`, and the jump-count compensator.
3. The recurrence for `h` uses independent rate-one clocks while two paths
   are at distinct positive sites and a one-clock boundary at zero.
4. The full-start mean uses interface additivity and the adjacent ballot
   lemma.
5. The support interval uses induction on `Phi`; it does not depend on the
   interface representation.
6. The minimum endpoint mass uses the support lower bound and uniqueness of
   the descending collision order.
7. The asymptotic uses only the central-binomial estimate after the exact
   mean has been proved.

## Proof

### Step 1: absorption and PGF recurrence

For an update at `v`, if `v-1` is empty then `Phi` decreases by one. If
`v-1` is occupied, the arriving pile coalesces and `Phi` decreases by `v`.
Thus every update decreases the nonnegative integer `Phi` strictly. The chain
therefore reaches `{0}` after at most `Phi(S)` updates.

Conditioning on the uniformly chosen first site gives

$$
G_S(z)=\frac1{|S|-1}\sum_{v\in S\setminus\{0\}}
zG_{C_v(S)}(z).
$$

The boundary value is `G_{\{0\}}(z)=1`. Strict potential decrease makes this
a finite acyclic recursion, so it uniquely determines the entire law.

### Step 2: Poissonization has the literal embedded chain

Place an independent rate-one Poisson clock at every positive site. When a
clock rings at an occupied site `v`, move that pile to `v-1`; ignore rings at
empty sites. Root zero has no clock. If the current state has `k` nonroot
occupied sites, the next effective ring is the minimum of `k` independent
rate-one exponentials. Its site is uniform among those `k` sites. Hence the
embedded jump chain is exactly the discrete process in the claim.

The construction is nonexplosive: the number of effective jumps is bounded
by the initial integer `Phi(S)` from Step 1.

### Step 3: interfaces count active piles

Label the initial piles in increasing order as `0,1,...,r`. Follow every
label through the site-clock arrows. When two labels meet, retain both labels
on the single resulting graphical path. One-dimensional rootward motion
preserves label order: paths can meet but cannot cross.

For `1<=i<=r`, declare interface `i` open until the graphical paths from
`s_{i-1}` and `s_i` first meet, and call that time `tau_i`. At any time before
absorption, consecutive labels lie in the same current pile exactly when
their interface has closed. Therefore the current piles are the consecutive
blocks obtained by cutting at open interfaces. The block containing label
zero is the root pile, so

$$
N_t=\sum_{i=1}^{r}{\bf1}_{\{\tau_i>t\}}.
$$

This is a pathwise identity. It neither assumes nor implies independence of
the interface lifetimes.

### Step 4: compensator and Tonelli prove additivity

Let `J_t` count effective jumps by continuous time `t`. Conditional on the
current state, its total effective rate is `N_t`; hence

$$
J_t-\int_0^t N_u\,du
$$

is the compensated jump-count martingale. Because `J_infinity<=Phi(S)`, take
expectations and then let `t` increase to infinity. Monotone convergence and
the pathwise identity in Step 3 give

$$
\begin{aligned}
\mathbb E[T_S]
&=\mathbb E[J_\infty]
=\mathbb E\int_0^\infty N_t\,dt\\
&=\mathbb E\int_0^\infty
  \sum_{i=1}^{r}{\bf1}_{\{\tau_i>t\}}\,dt
=\sum_{i=1}^{r}\mathbb E[\tau_i].
\end{aligned}
$$

All integrands are nonnegative, so Tonelli applies without an independence
assumption.

### Step 5: each interface has the two-path recurrence

Before the two paths started at `a<b` meet, they occupy distinct sites. The
Poisson strong Markov property supplies independent fresh rate-one waiting
times at those distinct sites, even if a site was visited earlier. If
`0<a<b`, the first of the two clocks rings after mean `1/2`; with probability
`1/2` the lower path moves to `a-1`, and with probability `1/2` the upper path
moves to `b-1`. Consequently

$$
h(a,b)=\frac12+
\frac{h(a-1,b)+h(a,b-1)}2.
$$

If `a=b`, the paths have met and `h(a,a)=0`. If `a=0<b`, only the upper path
moves and it requires exactly `b` independent mean-one holding times, so
`h(0,b)=b`. Interactions with labels outside this pair do not change either
graphical path; they merely attach extra labels to it. Thus
`E[tau_i]=h(s_{i-1},s_i)`. Substitution into Step 4 proves

$$
\mathbb E[T_S]=\sum_{i=1}^{r}h(s_{i-1},s_i).
$$

### Step 6: adjacent-interface evaluation

Let `R_m=h(m-1,m)`. The case `m=1` gives `R_1=h(0,1)=1`. For `m>=2`, put
`p=m-1`. Until meeting or the lower path reaches zero, superpose the two
rate-one clocks. Each event has mean waiting time `1/2`; its type is a fair
coin. Write an up-step when the lower path moves, increasing the gap, and a
down-step when the upper path moves, decreasing the gap. The gap starts at
one. Stop either when a down-step first makes the gap zero or when the
`p`-th up-step occurs.

If meeting occurs after `j` up-steps and `j+1` down-steps, where
`0<=j<=p-1`, the number of legal event words is the Catalan number

$$
A_j=\frac1{j+1}{2j\choose j}.
$$

If the lower path reaches zero with `q` down-steps already seen, where
`0<=q<=p-1`, the last event is the `p`-th up-step and the reflection
principle gives

$$
B_{p,q}={p+q-1\choose q}-{p+q-1\choose q-1}
$$

legal prefixes; the second binomial coefficient is zero for `q=0`. At that
boundary the upper path is still `p+1-q` steps from zero. Therefore

$$
\begin{aligned}
R_m={}&\sum_{j=0}^{p-1}
\frac{A_j}{2^{2j+1}}\frac{2j+1}{2}\\
&+\sum_{q=0}^{p-1}
\frac{B_{p,q}}{2^{p+q}}
\left(\frac{p+q}{2}+p+1-q\right).
\end{aligned}
$$

This finite sum has no probabilistic approximation. Substituting

$$
B_{p,q}=\frac{p-q}{p+q}{p+q\choose q}
$$

and Pascal's identity into the displayed expression shows, after shifting
the two boundary terms, that its values obey

$$
R_1=1,\qquad 2mR_{m+1}=(2m+1)R_m.
$$

The cancellation is termwise between the `q` term at level `p+1` and the
`q-1` term at level `p`; the uncancelled boundary term is the Catalan term
`A_p/2^{2p+1}`. Solving the first-order recurrence gives

$$
R_m=\frac{(2m-1)!!}{(2m-2)!!}
=\frac{2m}{4^m}{2m\choose m}.
$$

The last expression is also `E|S_{2m}|`, by pairing the positive and
negative endpoints of a length-`2m` simple symmetric walk and applying
`k*binom(2m,k)=2m*binom(2m-1,k-1)` to the positive half.

For `S_n={0,1,...,n-1}`, Step 5 now telescopes over its adjacent interfaces:

$$
\mathbb E[T_{S_n}]
=\sum_{m=1}^{n-1}R_m
=\sum_{m=1}^{n-1}\frac{(2m-1)!!}{(2m-2)!!}.
$$

Finally, the central-binomial estimate

$$
{2m\choose m}=\frac{4^m}{\sqrt{\pi m}}
\left(1+O(m^{-1})\right)
$$

gives `R_m=2sqrt(m/pi)+O(m^{-1/2})`. Summing this estimate from `1` to
`n-1` yields

$$
\mathbb E[T_{S_n}]
=\frac4{3\sqrt\pi}n^{3/2}+O(n^{1/2}).
$$

### Step 7: exact support for every initial state

We prove by induction on `Phi(S)` that every nonabsorbing rooted state has

$$
\operatorname{supp}(T_S)=\{M(S),M(S)+1,\ldots,\Phi(S)\}.
$$

Every update decreases `Phi` by at least one, so `T_S<=Phi(S)`. An update
decreases the maximum occupied coordinate by at most one: if the maximum
moves into a vacancy it becomes `m-1`, if it collides then `m-1` was already
occupied, and a move below the maximum leaves it unchanged. Thus at least
`M(S)` updates are necessary.

Let `m=M(S)`. If `m-1` is empty, choose `m` first. The successor has maximum
`m-1` and potential `Phi(S)-1`; the induction hypothesis for that successor,
followed by the first update, realizes every integer from `m` to `Phi(S)`.

Now suppose `m-1` is occupied. The case `m=1` is immediate. For `m>=2`,
choose `m` first. This collision gives, after restoring the first step, the
interval

$$
[m,\Phi(S)-m+1].
$$

Let `a` be the bottom of the consecutive occupied run ending at `m`. If
`a=1`, moving `a` collides at the root and decreases `Phi` by one; if `a>1`,
then `a-1` is empty and moving `a` also decreases `Phi` by one. In both cases
the maximum remains `m`, so this first choice and induction give

$$
[m+1,\Phi(S)].
$$

Because `m` and `m-1` are occupied, `Phi(S)>=2m-1`; hence the two integer
intervals touch or overlap. Their union is `[m,Phi(S)]`, completing the
induction.

### Step 8: minimum endpoint mass for full occupancy

From the full state, attaining `n-1` updates means every update must reduce
the number of nonroot piles by one. Thus every update must be a collision.
If a site is removed before a larger adjacent site, moving that larger site
later enters the new vacancy and is not a collision. Hence the only
all-collision order is

$$
n-1,n-2,\ldots,1.
$$

At the successive states there are `n-1,n-2,...,1` eligible nonroot sites.
The probability of this unique order is

$$
\frac1{n-1}\frac1{n-2}\cdots\frac11=\frac1{(n-1)!}.
$$

Claims 1--4 follow. ∎

## Exact Verification

The independent dynamic programs in
`scouting/stochastic/code/pilot_exact.py` perform the following checks.

- Every nonempty subset for `n=1..12` is audited for legal transitions and
  strict potential descent: 8,178 states.
- Every root-containing subset for `n=1..12` is checked by two separate
  exact recurrences: the discrete Bellman expectation and the sum of pair
  recurrences: 4,095 identities.
- The adjacent double-factorial identity is checked through `m=12`.
- The full exact PGF is checked through `n=10`, including normalization,
  support, both endpoint masses, and the mean.
- The complete 26-system scouting run has 9,225,587 exact assertions.

Stable artifact hashes at the proof-spike freeze:

```text
8b4db213207189cfd476e6b3d94dfd31c2b7e084aec33ab80bb2563d4d1470d0  code/pilot_exact.py
d62932222b246f93584376d90f59223e4004c10e8c39e915b6681e7022ac2020  code/PILOT_CANONICAL.txt
```

A fresh run on 2026-08-31 matched the canonical stdout byte for byte.

## Corrections or Missing Assumptions

- The theorem must say “uniform among occupied nonroot sites.” Uniform among
  all geometric sites with lazy holds is a different discrete-time law.
- The proof uses site-clock graphical paths. Permanently attaching independent
  clocks to original particles after coalescence would define a different
  process.
- The maximum-endpoint probability `2^{-binom(n-1,2)}` remains outside the
  proved theorem until its noncollision ballot calculation is written in full.

## Open Risks

- The proof status does not certify novelty. Generic graphical construction,
  interface, meeting-time, and simple-walk methods are externally owned and
  receive zero credit.
- The bounded primary-source search found no statement of the same literal
  kernel plus general interface-additive jump count, but absence was not
  established. External status remains `HOLD_EXTERNAL`.
- Any tree extension, different scheduler, multiplicity-retaining collision,
  or unbiased motion needs a new proof and collision audit.
