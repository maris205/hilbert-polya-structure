# B's backward-charge and inverse-incidence deductions

Status: PROVABLE AS STATED under the exact positive integer, ordered,
synchronous OLD-part contract. This is a review reconstruction after reading
the mathematical manuscript, not a claim to have invented its core lemma.
No author/A program or canonical scientific body has been read at this point.

## 1. Reconstructing the map from inverse incidence

For a proposed target $s=(s_1,\ldots,s_m)$ choose an integer partition
$\lambda_i$ of $s_i$, written in nondecreasing order. Concatenate these
partitions only if $\max\lambda_i>\min\lambda_{i+1}$ at every boundary.
The partitions then are precisely the maximal weakly increasing runs of
the concatenated source. Conversely, any source admits exactly one such
target: positivity makes the required cumulative target sums unique, and
the maximal runs determine the target. Thus this relation has exactly one
outgoing incidence per source. This proves what B's inverse enumerator
tests; it does not assume an imported forward-update function.

If a source is not fixed, its target has fewer parts. Ordering states by
length makes the non-loop graph acyclic. Loops are exactly the strictly
decreasing compositions. These are generic coarsening facts, not credit.

## 2. Backward causal chain for a late erased boundary

Use consecutive groups of original parts solely in this proof, with their
positive masses; B's computational carrier does not encode unit-cell cuts.
Consider a boundary erased in round $t\ge2$, between old groups $A,B$.
At time $t-2$, let $a$ be the rightmost constituent of $A$ and $c$ the
leftmost constituent of $B$. The same boundary survived round $t-1$,
so $|a|>|c|$. If $B$ had not changed during that round, then $B=c$ and
$|A|\ge|a|>|B|$, contradicting erasure. Thus $B$ was newly formed.
Its first internal boundary was erased in round $t-1$, with old left
group $c$. Consequently the earlier erased boundary has left mass
strictly smaller than $|A|$: $|A|\ge|a|>|c|$.

Repeat this backward choice until round 1. It produces $t$ positive
integer left masses in a strictly descending chain. Therefore the left
mass at any round-$t$ erasure is at least $t$. This is a finite backward
certificate, rather than an induction asserting a minimum mass for all
births. It uses the same indispensable oriented inequality as the author;
that overlap is explicit and receives no methodological novelty credit.

## 3. Disjoint charging inside one late birth

Let $J_t$ be any group first formed in round $t$. Choose its first two old
constituents $G_t,J_{t-1}$. For $t\ge2$, the preceding backward argument
forces $J_{t-1}$ to be a round-$(t-1)$ birth and gives $|G_t|\ge t$.
Inside $J_{t-1}$ repeat, selecting its first two constituents. After $t$
steps this constructs pairwise disjoint groups $G_t,G_{t-1},\ldots,G_1$
and one remaining positive group $J_0$, all contained in $J_t$. Other
constituents are discarded from the estimate, not counted twice. Each
$|G_i|\ge i$ by the backward boundary certificate, including positivity
for $i=1$. Therefore
$$|J_t|\ge |J_0|+\sum_{i=1}^t|G_i|\ge1+t(t+1)/2.$$
The last nonfixed update creates such a group, which proves the global
upper bound without confusing first fixation with an extra fixed update.

For $h\ge1$ and any surplus $r\ge0$, the initial state
$(h,h-1,\ldots,1,1+r)$ has, at time $j\in\{1,\ldots,h\}$, the state
$(h,h-1,\ldots,j+1,1+r+j(j+1)/2)$. The prefix's OLD comparisons are
strict descents and its last part is at most the suffix mass; exactly
that last part merges with the suffix in the next update. This proves
the formula and exactly $h$ nonfixed updates. For $N=1$ the singleton
has time zero. Taking maximal $h$ with $1+h(h+1)/2\le N$ and the remaining
surplus proves the sharp formula for every integer $N\ge1$.

## 4. Attained endpoint minimum, not an interval hypothesis

For a feasible target suffix let $r$ be the least first part among its
inverse refinements. This minimum exists because all parts are positive
integers of a fixed finite mass. To prepend a partition of total $s$, its
last part must be greater than an attainable suffix first part, hence at
least $r+1$. Attainment means this necessary lower bound is sufficient
for attachment. Minimize the prepended partition's first part:

* $s\le r$: no such last part exists, so the whole suffix fails.
* $s=r+1$: all mass is needed for that last part, so the partition is the
  singleton and the new attained minimum is $r+1$.
* $s\ge r+2$: $(1,s-1)$ is nondecreasing and attachable, so the new
  attained minimum is 1.

The final target part starts with minimum 1 via all ones. Backward
application proves the full image iff test; nowhere is the set of all
attainable first parts assumed contiguous. The order-sensitive targets
$(2,3,2)$ and $(2,2,3)$ respectively pass and fail.

## 5. Explicit code audit

Let $T_k=k(k+1)/2$. Scanning an image from right to left starts at part
$b$ and threshold 1. Between resets the forced increments are
$2,3,\ldots,k$; a reset has value $k+2+u$, $u\ge0$. Encode initial $b$
as $b-1$ ones, every complete increment/reset cycle as $T_{k+1}$ followed
by $u$ ones, and the final increment-only string as $T_k$. The cycle
weight is $(T_k-1)+(k+2+u)=T_{k+1}+u$; the initial part plus terminal
string contributes $(b-1)+T_k$. Thus the code preserves total mass.

For the inverse reserve the **last** triangular part first, even when it
is 1. The remaining word splits uniquely into initial ones, then each
triangular part $T_j\ge3$ and its maximal following ones. Initial ones
give $b-1$. Each later group gives increments $2,\ldots,j-1$ then reset
$j+1+u$. The reserved $T_k$ gives terminal increments $2,\ldots,k$.
Reverse to obtain the target. These are legal threshold transitions and
the two unique parsings undo one another. This verifies the given codec
directly; generic reset coding and triangular composition counts remain
deducted. The new relationship to this image is the sole image axis.

## 6. Supporting fibres and boundaries

A partition of $s$ with equal first and last value $a$ consists only of
$a$'s, and exists once iff $a\mid s$. With unequal endpoints $a<b$,
reserve one of each and independently choose nonnegative multiplicities
of every integer in $[a,b]$. This gives
$[z^s]z^{a+b}\prod_{j=a}^b(1-z^j)^{-1}$. Summing endpoint products with
strict inter-partition descent indicators counts the inverse incidences
without overcounting. This is ordinary partition transfer, zero separate
novelty credit. No max-fibre, pointwise closed clock, higher iterate inverse,
asymptotic, arbitrary-conjugacy exclusion or all-deepest-state theorem follows.

Dependency map: unique inverse segmentation → graph/support; backward
erasure chain → disjoint charging → sharp clock with explicit witness;
attained suffix minimum → threshold → unique reset parse → image bijection.
The two retained axes do not derive from the finite N=1..12 observations.
The finite verifier pressures each separately. No unresolved proof gap was
found in these deductions; owner uncertainty remains OWNER_AMBER/HOLD_EXTERNAL.
