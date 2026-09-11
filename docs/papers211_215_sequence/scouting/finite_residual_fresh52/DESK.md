# Fresh52: equal-diameter coarsening of labelled partitions

2026-09-11. **AUTHOR THEOREM PACKAGE / INDEPENDENT GATE REQUIRED.**
One literal, no padding candidate, no scientific code or execution,
no seat/count/central edit and no admission. All external use remains held.

## Authorship and scope

`current_round_independent_scout` proposed the diameter rule, the causal
spine upper bound, the eight-label witness, the endpoint-matching inverse
description, the pair-target evaluation, and the completed coefficient/DP
proof below. `current_round_two_seats_scout` supplied the linear cascade
and its all-size padding in
`../finite_residual_fresh52_challenge/PROOF_PACKAGE.md`, read completely
before use here. Root proposed the explicit endpoint-factor coefficient
formula and requested its proof/evaluation analysis. All three are proof
contributors and cannot supply nonauthor review of this package.

The project workflow, current anchor, inherited promotion criteria,
proof-writer and research-lit skills were used. There is no added condition
that two proof mechanisms must both be globally new, or that a temporal
theorem must simultaneously give exact pointwise time and a sharp leading
constant. Correct claims and unproved refinements are separated below.

## 1. Literal map and proposed bounded theorem contract

For $n\ge0$, let $\Pi_n$ be the set of all set partitions of the ordered
labelled set $[n]$. Blocks need not be intervals. For a nonempty block $B$,
put $\delta(B)=\max B-\min B$. Define $D(\pi)$ by simultaneously uniting
all blocks with each common value of $\delta$. Thus all singleton blocks
are united; no newly equal diameters are merged until the next update.
The empty partition maps to itself. Write $h(\pi)$ for its fixed-point
entrance time and $H(n)=\max_{\pi\in\Pi_n}h(\pi)$.

**Status: PROVABLE AS STATED, author deductions pending independent gate.**

1. The recurrent states are exactly partitions with pairwise distinct
   block diameters. Every state is eventually fixed, and
   $H(n)\le\lfloor n/2\rfloor$.
2. For every $m\ge1$ there is an exact $2m$-round cascade on $5m+5$
   labels; for all $n\ge10$,
   $$2\left\lfloor\frac{n-5}{5}\right\rfloor\le H(n)\le\lfloor n/2\rfloor.$$
   Hence the worst time is $\Theta(n)$. Also $H(8)=4$.
3. Section 4 gives the complete one-step fibre for every target as
   explicit finite coefficient products, with a finite arithmetic
   evaluation algorithm and no iteration of $D$ or enumeration of all
   predecessor partitions. Section 5 evaluates the whole pair-target
   stratum in closed form, including its sharp maximum and all zero cases.

For $n\ge2$ the map is intrinsically noninjective: the singleton partition
and the one-block partition both map to the latter. For $n=0,1$ it is the
identity on a singleton carrier. No global exact formula for $H(n)$,
pointwise formula for $h(\pi)$, or global maximum fibre is asserted.

## 2. Causal-spine upper bound

Each nonfixed step strictly reduces the number of blocks; hence every
orbit reaches a fixed partition and has no strict cycle. A partition is
fixed precisely when its diameters are pairwise distinct.

The following observation is stronger than the raw block-count budget.
If a merger occurs at round $t\ge2$, at least one participating input
block was newly formed at round $t-1$. Otherwise all participating blocks
already existed, unchanged and with their present equal diameters, before
round $t-1$, so they would have merged at that earlier round. This is a
contradiction.

Starting from a merger at the last nonfixed round $h$, repeatedly select
such a newly formed parent. This yields nested merger outputs at every
round $1,\ldots,h$, not merely an arbitrary ancestral tree with gaps.
The first output contains at least two labels, and therefore has positive
diameter. At every later merger, the selected parent has positive diameter;
at least one other participating block has that same positive diameter,
so it contains at least two labels. These additional blocks are disjoint
from the parent and from all labels previously accumulated on the spine.
The final spine block therefore contains at least $2+2(h-1)=2h$ labels.
Since it is a subset of $[n]$, $h\le\lfloor n/2\rfloor$. This proof
covers singleton mergers at the first round and arbitrarily many
simultaneous mergers off the selected spine. For a fixed initial state,
$h=0$ and the bound is immediate. ∎

## 3. Linear lower bound and concrete separation from EQC

The challenge contributor's complete original proof is linked above.
For a self-contained statement of its main construction, work on
$I_m=[-3m,4+2m]\cap\mathbb Z$. Start with endpoint blocks

$$A=\{0,4\},\quad P_k=\{2-3k,6+2k\},\quad
Q_k=\{-3k-3,3+2k\},\qquad0\le k<m.$$

Left endpoints are disjoint by their residue classes modulo three;
right endpoints are disjoint by parity and the isolated endpoint four.
Left endpoints are at most two and right endpoints at least three, so
cross-collisions do not occur. Place every unused label at most $2m+1$
inside $Q_{m-1}$, and every unused larger label inside $P_{m-1}$. Their
hulls cover $I_m$, and these assignments preserve all block endpoints.
The result is a partition, not a partial matching with uncontrolled
singleton padding.

At time $2k$ the active block has hull $[-3k,4+2k]$, diameter $4+5k$.
Its unique matching partner is $P_k$; their merger has diameter $6+5k$
and unique matching partner $Q_k$. The latter merger produces the active
hull for $k+1$. All unconsumed partner diameters are distinct, in the two
different residue classes four and one modulo five. Thus exactly one
merger occurs at each round until time $2m$, when one block remains.
Translation yields a partition of $[5m+5]$ with exact time $2m$.

For $n\ge10$, put $m=\lfloor(n-5)/5\rfloor$ and $N=5m+5$. If needed,
adjoin the single residual block $\{N+1,\ldots,n\}$. Its diameter is at
most three, whereas every cascade diameter is at least four. It never
interacts. This proves the lower bound in Section 1 and, with Section 2,
the linear order for every sufficiently large size. ∎

A smaller hand witness is

$$\pi=\{2\}\mid\{5\}\mid\{3,6\}\mid\{4,8\}\mid\{1,7\}\in\Pi_8.$$

The active blocks in its four nonfixed rounds are respectively
$\{2,5\}$ (diameter three), $\{2,3,5,6\}$ (diameter four),
$\{2,3,4,5,6,8\}$ (diameter six), and $[8]$. All other blocks wait until
their indicated diameter is matched. Thus $h(\pi)=4$, and Section 2 gives
$H(8)=4$. This is a hand proof, not a pilot.

For old EQC, equal-cardinality merging, the same causal-spine argument
doubles the parent size at every round, giving time at most
$\lfloor\log_2 n\rfloor$. Therefore EQC on $\Pi_8$ has height at most
three, whereas the present map has height four. These two same-carrier
maps are **not dynamically conjugate**. This is stronger than comparing
their literal statistics, but is not a claim to have excluded every
other archived system.

## 4. Full inverse: explicit coefficient products and evaluation

Let $Y\subseteq[n]$ be nonempty. For $d\ge1$ set

$$E_d(Y)=\{(a,b)\in Y^2:a<b,\ b-a=d\},\qquad
J_{ab}=\{v\in Y:a<v<b\}.$$

For a finite set $S$, abbreviate $x_S=\prod_{v\in S}x_v$. Define

$$C(Y,0)=1,$$
$$C(Y,d)=[x_Y]\prod_{(a,b)\in E_d(Y)}
\left(1+x_a x_b\prod_{v\in J_{ab}}(1+x_v)\right)\quad(d\ge1).$$

An empty factor product is one. Thus for $Y\ne\varnothing$, $C(Y,d)=0$
when there is no way to cover it, in particular if $d>\delta(Y)$.

**Local coefficient proof.** A positive-diameter block has unique endpoints
$a,b$, and its remaining members are a subset of $J_{ab}$. Choosing the
nonconstant term from an endpoint factor selects exactly such a block;
choosing one from that factor does not select it. The coefficient of the
squarefree monomial $x_Y$ keeps exactly choices with disjoint vertex sets
covering $Y$. Conversely every partition of $Y$ into diameter-$d$ blocks
has exactly these endpoint choices and interior subsets. There is no
factorial overcount: blocks with the same endpoints cannot be distinct
blocks of a partition, and each possible endpoint pair has only one
factor. Consequently $C(Y,d)$ is precisely the number of such partitions.
For $d=0$ the only local partition is all singletons, justifying one. ∎

For a target $\tau=Y_1|\cdots|Y_k$, write $c_{i,d}=C(Y_i,d)$ and set

$$\boxed{\ |D^{-1}(\tau)|=
\sum_{\substack{d_1,\ldots,d_k\in\{0,\ldots,n-1\}\\
                         d_i\text{ pairwise distinct}}}
\prod_{i=1}^k c_{i,d_i}
=[z_1\cdots z_k]\prod_{d=0}^{n-1}
\left(1+\sum_{i=1}^k c_{i,d}z_i\right).\ }$$

Every predecessor refines the target. Its blocks inside one $Y_i$ must
all have one common diameter $d_i$, since precisely one equality class
is merged to $Y_i$. Different target blocks require different diameters;
otherwise they would be merged together. These conditions are sufficient
as well as necessary, proving the first expression. In the second
expression one diameter factor can supply at most one target index;
the squarefree coefficient supplies every index once. This proves the
second expression. For $n=k=0$ the empty product and coefficient both
equal one, the correct fibre of the empty partition. ∎

### What “explicitly evaluated” means here

The display is an explicit coefficient formula, not a claim of a simple
factored integer for every target. Its inputs are only the labelled target
and integer endpoint differences. It has no unknown orbit statistic and
does not sum over all predecessor partitions. For fixed $Y,d$, the
endpoint graph consists of paths along arithmetic progressions, hence
$|E_d(Y)|\le |Y|-1$. Across all positive $d$, there are at most
$\binom{|Y|}{2}$ endpoint factors.

A concrete exact arithmetic evaluation is available. Work modulo
$x_v^2=0$ and represent a polynomial by its coefficients indexed by subsets
of $Y$. Initialize the empty coefficient to one. At factor $(a,b)$, retain
each coefficient at $S$, and for every $T\subseteq J_{ab}\setminus S$
with $a,b\notin S$, add that coefficient at
$S\cup\{a,b\}\cup T$. This is multiplication by the displayed factor,
with all repeated-variable monomials discarded. After the last factor,
the full-set coefficient is $C(Y,d)$. It uses at most
$O(|E_d(Y)|3^{|Y|})$ arithmetic updates and $O(2^{|Y|})$ coefficient storage.

After computing $c_{i,d}$, maintain an array on subsets $S\subseteq[k]$.
Scanning diameters $d=0,\ldots,n-1$, replace its array $b$ by

$$b_{\mathrm{new}}(S)=b(S)+\sum_{i\in S}c_{i,d}\,b(S\setminus\{i\}),$$

using only the old array on the right; initialize $b(\varnothing)=1$ and
the other entries to zero. Its final full-set entry is the complete fibre.
This stage uses $O(nk2^k)$ arithmetic operations. The algorithms are
mathematical evaluation prescriptions only; no source has been executed.
They do not claim polynomial bit complexity.

The generic squarefree-cover product and distinct-colour assignment
principles receive no novelty credit. Their compact endpoint realization
and the closed stratum below make the formula more than a restatement of
“count all predecessors,” but an independent gate must still assess its
research value. No uncomputed general maximum is hidden in this notation.

## 5. Closed pair-target stratum and its sharp maximum

Suppose $n=2k$ and every target block $Y_i$ is a pair, with diameter
$\delta_i>0$. It has exactly two local predecessor partitions: the
unsplit pair with diameter $\delta_i$, and its two singleton blocks with
common diameter zero. Hence at most one target pair can be split, since
different target blocks must use distinct diameters.

It follows that the complete fibre in the full carrier $\Pi_{2k}$ is

$$|D^{-1}(\tau)|=
\begin{cases}
k+1,&\text{all }\delta_i\text{ are distinct},\\
2,&\text{exactly one diameter occurs twice and all others once},\\
0,&\text{otherwise}.
\end{cases}$$

In the first case there is the unsplit predecessor and one for each
choice of the unique split pair. In the second case one of the two equal
diameters must be removed by splitting that pair, giving two choices.
Every remaining repetition pattern needs at least two split target pairs,
which is impossible. This proves all cases without a transfer recurrence.

For $k\ge1$, the maximum over pair targets is $k+1$, attained exactly
when the pair diameters are distinct. It is attained for every $k$ by
$\{i,2k+1-i\}$, $1\le i\le k$, whose diameters are distinct positive
odd numbers. For $k=0$ there is only the empty partition, with fibre one.
This maximum is explicitly **stratum-restricted**, not a global maximum
over all targets of $\Pi_n$.

## 6. Source/collision subtraction and limitations

Actual local originals read:

- `docs/papers147_151_sequence/scouting/root/SCOUT.md`, full EQC section:
  equal-cardinality merging, its shape factor, logarithmic clock and
  labelled distinct-divisor fibre product. The generic coarsening and
  distinct-statistic assignment template are occupied.
- `docs/papers147_151_sequence/phase1/OWNER_AUDIT_EQC.md`, full original:
  its status is `KILL_UNRESOLVED_DIRECT_OWNER` concerning the integer-
  partition multiplicity dynamics, not an accepted source-clearance result.
- `docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md:624`, the
  fibre-size-feedback exclusion: another exact cardinality quotient, not
  the geometry of arbitrary endpoint spans.

The eight-label height separation above excludes same-size EQC conjugacy.
It does not assert that changing a statistic is automatically novel. The
inverse's distinct-diameter assignment is the old generic template, while
the local endpoint coefficient is a different evaluation problem from
equal-size factorial splitting. The linear cascade cannot be obtained
from the old equal-mass-doubling clock by retaining labels.

Bounded web queries concerned equal-diameter merging/coalescence,
partition spans, and diameter coarsening. Most hits concerned geometric
clustering optimization or physical droplets. The actually opened primary
IBM record, Alpert and Kahng,
[Splitting an ordering into a partition to minimize diameter](https://research.ibm.com/publications/splitting-an-ordering-into-a-partition-to-minimize-diameter),
describes an interval-clustering optimization algorithm, not this finite
autonomous equality-merger map. Only that abstract was read, not its full
paper. Search non-hits, and irrelevant hits not pursued, do not establish
global novelty. The direct-owner audit remains bounded.

An initial local lookup used the wrong historical batch path for the EQC
owner audit and returned a missing-file error; the correct original above
was then located and read in full. Broad navigation outputs are not used
as absence certificates. No source was downloaded or executed.

## 7. Preserved proof boundary and handoff

The initial author found a one-sided $h$-round cascade on
$(h^2+3h+4)/2$ labels. That lower-bound construction did not prove a
square-root upper bound. Root suggested testing the latter heuristic;
the challenge contributor's linear family refuted it. No experiment or
failed output was removed, and no quadratic upper bound is claimed here.

This package now has a proved nonprojection linear temporal order with
an explicit all-size cascade, the stronger universal half-size bound,
complete fixed-state characterization, and a mathematically separate
all-target inverse coefficient theorem with a closed extremal stratum.
**Author recommendation: send this narrow contract to a noncontributor
candidate gate.** The gate should assess the real source/value boundary,
not infer global novelty or require unrequested exact pointwise/leading-
constant results. No admission is asserted by this recommendation.

Remaining refinements, not promised claims: exact $H(n)$ for every $n$,
an explicit pointwise clock, a simple factored general fibre expression,
global maximum-fibre classification, and broader source coverage. A pilot
may pressure the displayed theorems only after source/runtime gates;
none has been prepared or run in this desk. No central/count/number/Git
change occurred. `HOLD_EXTERNAL` remains in force.
