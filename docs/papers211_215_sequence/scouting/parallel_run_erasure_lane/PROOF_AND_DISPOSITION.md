# Parallel whole-run erasure: elementary boundary and negative disposition

2026-09-08 UTC. `NO_PROMOTION / ONE_LITERAL_ATTEMPT / ZERO_RESERVES /
ZERO_SCIENTIFIC_EXECUTIONS / HOLD_EXTERNAL`.

Root contributed the literal rule and the length-bound/nested-witness
direction. This scout supplied the proof details and one-step run-gap
generating function. Both are proof contributors, not reviewers.

## Claim, status and assumptions

Fix integers $q\ge2$ and $N\ge0$. Let $\Sigma$ be a fixed labelled
$q$-letter alphabet and $X_{q,N}=\bigcup_{n=0}^N\Sigma^n$, including
the empty word $\epsilon$. In the old word, identify every maximal
constant run. Delete **every entire run of length at least two** in the
same round, keep singleton runs, and concatenate the survivors. Denote
this autonomous map by $T$.

The following elementary statements are `PROVABLE AS STATED`:

1. All recurrent words are fixed, namely words with no equal adjacent
   letters. The maximum fixed-point entrance time is $\lfloor N/2\rfloor$.
2. For a nonempty target $y=y_1\cdots y_m$, put
   $e(y)=|\{i<m:y_i=y_{i+1}\}|$. Define formal series
   $$L=\frac{z^2}{1-z},\qquad A=1-(q-1)L,\qquad B=1+L.$$
   The source-length generating function of its complete one-step fibre
   over unrestricted finite words is
   $$G_y(z)=\frac{z^m((q-1)L)^{e(y)}}{A^{m+1}B^{m-1}}.$$
   For the empty target, $G_\epsilon(z)=B/A$.
   Its fibre on $X_{q,N}$ is $\sum_{n=0}^N[z^n]G_y(z)$.
3. The complete image criterion on $X_{q,N}$ is
   $$y\in T(X_{q,N})\iff |y|+2e(y)\le N,$$
   with $e(\epsilon)=0$.

These statements do not supply a pointwise entrance formula, entrance-time
distribution, endpoint-basin classification, or a global maximum-fibre
theorem. Those stronger claims are **NOT CURRENTLY JUSTIFIED** by this desk.
There is no pilot or admission: the first statement is a generic deletion
clock and the other two are elementary run segmentation/counting.

## Strategy and dependency map

Length strictly decreases outside fixed words. A nested doubled palindrome
realizes one deletion per round. For inverses, retained singleton runs are
forced by the target; erased long runs occupy the gaps between them. Proper
colour sequences on the complete loopless alphabet graph evaluate every
gap. This is a finite-state transfer calculation with a two-eigenvalue
matrix, not a newly independent inverse mechanism.

1. At least two letters disappear per nonfixed round: termination and
   upper bound.
2. Alternating nested singleton wrappers: matching worst-case witness.
3. Unique run decomposition: inverse bijection and gap products.
4. Complete-graph matrix decomposition: displayed rational functions.
5. Equal target adjacencies force deleted gaps of length at least two:
   minimum source length and the full image criterion.

## Proof

### 1. Fixed/recurrent words and the zero-credit worst-case clock

The update never increases length. A word containing a long run loses at
least two letters, so it cannot recur before becoming fixed. Words whose
runs all have length one are unchanged. Hence the claimed classification
holds, including $\epsilon$. Counting these words gives the elementary
fixed census $1+\sum_{m=1}^Nq(q-1)^{m-1}$; this is not another axis.

If $h$ nonfixed rounds occur, $2h\le|w|\le N$. To attain the bound, set
$k=\lfloor N/2\rfloor$. For $k\ge1$, choose an alternating word
$u=u_1\cdots u_k$ on two distinct letters, and set $w=uu^{\rm rev}$.
Its only nonsingleton run is the doubled central letter. Deleting it leaves
the same form with alternating prefix $u_1\cdots u_{k-1}$. Induction
therefore gives entrance time exactly $k$. The word has length $2k\le N$.
For $N=0,1$, every word is fixed and the maximum is zero. This proves
sharpness on the requested length-at-most carrier without any hidden
exact-length or parity assumption.

### 2. Unique one-step inverse decomposition

Every letter retained from a source was a singleton maximal run, and their
order is exactly the target $y$. Between consecutive retained singleton
letters, and before/after them, lie zero or more deleted maximal runs.
Every such run has an arbitrary length at least two, so one fixed-colour
deleted run has length series $L$. Consecutive run colours must differ,
including their junctions with retained singletons. Conversely, any such
gap construction has exactly the prescribed singleton runs and maps to
$y$. It is unique because maximal-run boundaries of the source are unique.
Thus no hidden segmentation multiplicity remains.

Let $K=J-I$ be the $q\times q$ adjacency matrix for unequal colours, where
$J$ is all ones. A boundary gap with $r$ long runs has $(q-1)^r$ colourings,
because its nearest run differs from the adjacent retained letter and
each subsequent run differs from the previous one. Its series is $A^{-1}$.

For an internal gap with retained endpoint letters $a,b$ and $r$ deleted
runs, the number of colourings is $(K^{r+1})_{ab}$. This includes $r=0$:
the two retained singleton letters may be adjacent precisely when $a\ne b$.
Consequently its series is the $(a,b)$ entry of
$$K(I-LK)^{-1}.$$
All these are formal power series: $L$ has zero constant term, so the
geometric matrix inverse is defined without an analytic convergence claim.

### 3. Evaluating the gap matrix

Put $P=J/q$. Then $P^2=P$ and
$K=(q-1)P-(I-P)$. Multiplying on the two complementary subspaces gives
$$K(I-LK)^{-1}=\frac{q-1}{A}P-\frac1B(I-P).$$
Its off-diagonal entries equal $1/(AB)$, while its diagonal entries equal
$(q-1)L/(AB)$. Multiplying the $m$ retained-letter weights $z$, the two
boundary factors $A^{-1}$, and the $m-1$ internal-gap entries gives the
displayed $G_y(z)$.

For $y=\epsilon$, the source is empty or consists of $r\ge1$ long runs.
Such runs have $q(q-1)^{r-1}$ colourings. Therefore
$$G_\epsilon(z)=1+\sum_{r\ge1}q(q-1)^{r-1}L^r
=1+\frac{qL}{A}=\frac BA.$$
Coefficient truncation at $N$ is precisely the required finite carrier;
no quotient by alphabet relabelling or word reversal is taken.

### 4. Full image threshold

Each of the $m$ retained target letters requires one source letter. If
$y_i=y_{i+1}$, they cannot have been adjacent source singletons: they
would instead lie in one long maximal run. At least one deleted run must
separate them, costing at least two additional letters. These gaps are
disjoint, so every source has length at least $m+2e(y)$.

To attain this lower bound, put no boundary gaps and no gaps between
unequal adjacent target letters. Between each equal pair of letters $a,a$,
insert $bb$ with any chosen $b\ne a$, which exists since $q\ge2$.
The inserted pairs are maximal long runs, each flanked by retained
singleton letters of another colour; every target letter remains a
singleton in the source. Thus this source maps to $y$ and has exactly the
claimed length. The empty word maps to itself. This proves the criterion.
∎

## Source subtraction, missing obligations and disposition

The [source memo](SOURCE_AND_COLLISION.md) distinguishes exact whole-run
serial popping from synchronous deletion, parity cancellation, free-group
reduction, fixed-site BSE and run relabelling. No unproved conjugacy or
priority claim is used to kill this map. The root-specified worst-case
clock is explicitly zero-credit. The evaluated inverse and image follow
from unique run segmentation plus complete-graph colour counting; writing
the two eigenvalues out does not change that proof mechanism.

No genuine pointwise or distributional temporal residual was closed in
this short desk. The conjunction required for promotion is absent, even
though the elementary formulas above are valid. Close this **one literal
attempt** `NO_PROMOTION`, with zero reserves and no scientific execution.
No larger cutoff, parameter variant, manuscript number or self-review
is proposed. The earlier closed packets and all old sources are immutable.
