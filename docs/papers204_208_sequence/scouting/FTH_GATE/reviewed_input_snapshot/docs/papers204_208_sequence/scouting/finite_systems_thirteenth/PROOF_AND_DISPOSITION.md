# Thirteenth lane: proved deductions and closed boundary

2026-09-06 UTC. Author: `batch197_lzk_gate`. This is a closed author scout,
not an independent candidate gate or manuscript. **NO_PROMOTION** on all
six desk literals. No paper ID, reserve or new external clearance results.
The fixed original intake and both successful pilot snapshots are unchanged.

The project proof-writing discipline is used below: state the carrier and
quantifiers, give complete deductions, and separate a proved generic
mechanism from the all-parameter statement still missing. No numerical
census is used as a proof of an unbounded claim.

## 1. HMP: hook-multiplicity dominance, but no complete retained axes

Let `T` be HMP on partitions of a fixed nonnegative mass `N`. The empty
partition is fixed. For a nonempty partition `lambda`, let `m_h` count
the Ferrers cells having hook length `h`; `T(lambda)` is the decreasing
list of its positive `m_h`. The cell partition by hook lengths proves
mass preservation and well-definedness.

### Complete generic descent deduction

Within a fixed row, moving one step right strictly reduces hook length:
the arm decreases by one and the leg cannot increase. Within a fixed
column, moving one step down gives the analogous strict decrease. Thus
any collection of `k` distinct hook lengths occupies at most `k` cells
in each column and at most `k` in each row. Consequently, writing missing
partition parts as zero,

    sum_{i<=k} T(lambda)_i <= sum_j min(k,lambda'_j)
                               = sum_{i<=k} lambda_i,
    sum_{i<=k} T(lambda)_i <= sum_i min(k,lambda_i)
                               = sum_{j<=k} lambda'_j.

The left side maximizes the total multiplicity over choices of `k`
hook lengths. The inequalities hold also beyond the number of distinct
hooks. They prove `T(lambda) <=dom lambda` and `T(lambda) <=dom lambda'`.
Transposing every cell preserves its hook length, proving
`T(lambda')=T(lambda)`.

For `N>=1`, set `W(lambda)=sum_i i lambda_i`, padding to `N` parts.
If `P_k(lambda)=sum_{i<=k}lambda_i`, then

    W(lambda)=N^2-sum_{k=1}^{N-1} P_k(lambda).

Strict dominance therefore raises this integer potential by at least
one whenever the partition changes. Also `N<=W(lambda)<=N(N+1)/2`:
the lower bound follows from `i>=1`; the upper bound follows from
`P_k(lambda)>=k` for `1<=k<N`. Hence every orbit reaches a fixed point
after at most `N(N-1)/2` arrows. There are no nontrivial cycles. The
separate empty case has depth zero. This was deducted before execution;
it is generic finite strict-dominance descent, not a new sharp clock.

### Actual fixed-box boundary

All partitions at `N=0,...,20` were checked, exactly 2,714 states.
The observed maximum depths for those masses are

    0,0,1,1,1,2,1,2,2,2,3,3,3,5,6,4,4,6,4,7,6.

For example the complete seven-arrow tail at `N=19` is

    (7,4,3,2,1,1,1)
    -> (5,4,3,2,2,2,1)
    -> (5,4,3,2,2,1,1,1)
    -> (5,3,2,2,2,2,1,1,1)
    -> (4,3,2,2,2,1,1,1,1,1,1)
    -> (4,3,2,2,1,1,1,1,1,1,1,1)
    -> (4,2,2,2,2,1,1,1,1,1,1,1)
    -> (3,3,2,2,2,1,1,1,1,1,1,1,1),

whose last term is fixed. These are actual original-box values, not a
chosen smaller favourable family. No all-`N` sharp height, complete fixed
language, evaluated full inverse, or all-target fibre extremum was proved.
At `N=20` the largest fibre is 90; this finite number is not an extremal
formula. A sorted hook-multiplicity constraint is not an evaluated inverse.

**Disposition:** `HOLD_PROOF / NO_PROMOTION`. P113 principal hooks,
frequency projection and the generic dominance mechanism remain deducted.
Hook-multiset source access remains bounded as recorded separately.

## 2. FBT: complete cohort-merger adapter, no pilot

Write a partition by distinct positive sizes and multiplicities
`{(a,m_a)}`. FBT creates `a` copies of size `m_a`, aggregating equal
new sizes. If `d(lambda)` is the number of distinct sizes, then
`d(T lambda)<=d(lambda)` and mass is preserved.

If equality holds, the old multiplicities `m_a` are distinct. In the
output, the multiplicity of new size `m_a` is exactly `a`; those `a`
values are distinct too. The next update therefore returns exactly
`lambda`. If equality fails, `d` strictly decreases. Thus an orbit has
at most `d(lambda)-1` strict support-drop arrows before reaching a
one- or two-cycle, for every nonempty partition; the empty state is fixed.
Every actual transient arrow is a strict support drop: equality at that
arrow already gives `T^2(lambda)=lambda`. This is an exact generic
cohort-merger argument, not a new independent temporal engine.

For a target with distinct sizes `b` and multiplicities `n_b`, a source
is exactly a choice, for each `b`, of a nonempty set `S_b` of distinct
positive old sizes such that

    sum_{a in S_b} a = n_b,

with the `S_b` pairwise disjoint. The source has multiplicity `b` at
each selected old size `a`. Necessity follows by grouping all old sizes
with old multiplicity `b`; sufficiency and uniqueness follow by reversing
that grouping. This is weighted subset assignment, not a new inverse
mechanism. Exactly `FBT(lambda)=DGR(lambda')`; this one-sided composition
is not a claimed conjugacy. **Desk kill / no pilot / no promotion.**

## 3. SSC: solvable derived-series bound does not give an all-S_n atlas

Use `[a,b]=aba^{-1}b^{-1}` and rightmost composition first, as in the
intake. Fix the `n`-cycle `c` (identity at the empty and singleton
boundaries), and put `T(sigma)=[sigma,c sigma c^{-1}]`.

Every commutator has sign `+1`. For `G=<sigma,c>`, let `G^(j)` be its
derived series. If `T^j(sigma)` belongs to `G^(j)`, its conjugate by
`c` also does, because derived subgroups are characteristic in `G` and
thus normal. Their commutator belongs to `G^(j+1)`. Induction proves
`T^j(sigma) in G^(j)` for every `j>=0`. If `G` has derived length `d`,
`T^d(sigma)=1`. No solvability is assumed for an arbitrary `S_n`.

For the small boundary, `S_2` is abelian, `[S_3,S_3]=A_3` is abelian,
and `[S_4,S_4]=A_4`, `[A_4,A_4]=V_4`, with `V_4` abelian.
These yield upper bounds `1,2,3` respectively; `S_0,S_1` are trivial.
The finite pilot reaches all three bounds. Equivariance under conjugation
by powers of `c` follows by conjugating the displayed commutator word;
it does not force every period to divide `n`.

The original full `n=5` box contains the following genuine five-cycle,
with permutations listed by their values at `0,...,4`:

    (1,2,4,0,3) -> (2,0,3,4,1) -> (1,3,4,2,0)
    -> (4,2,3,0,1) -> (2,3,1,4,0) -> (1,2,4,0,3).

Thus extrapolated global erasure is false already there. The cycle census
is `{1:1,5:2}` at `n=5`, `{1:1,2:3,6:2,12:1}` at `n=6`, and
`{1:1,7:2,14:4}` at `n=7`; these are numbers of cycles. Maximum depths
are `5,9,27`, and maximum target-fibre sizes `10,30,42`, respectively.
Complete cycle and deepest-tail witnesses are in the preserved raw output.

The recursive conjugate-commutator primitive in Bandman et al. was charged
before these executions. Their prescribed initial word is not an arbitrary
initial permutation here. We have no complete all-`n` clock/recurrent
language or full target-fibre/extremal theorem. **HOLD_PROOF / NO_PROMOTION.**

## 4. CSP: exact fixed-slot conjugacy, no pilot

For each cycle support, write the minimum first. Its remaining distinct
labels occupy a fixed ordered tuple of slots. The update permutes those
slots in the fixed odd-then-even order from the intake, leaving the cycle
supports and their minima invariant. These canonical tuples are a bijective
coordinate chart: no two tuples encode the same cycle after the minimum
has been fixed first. Inverting the slot permutation on every tuple gives
the unique predecessor of any target.

Because the tuple labels are distinct, a tuple returns exactly when the
slot permutation raised to that power is the identity. Thus every state
has depth zero, singleton fibre, and period the least common multiple of
the slot-permutation orders of its cycles. Length-one cycles and the
empty permutation use order one. Both axes are completely transported
from a fixed permutation action. **Desk kill / no pilot / no promotion.**

## 5. AMC: generic two-step stabilization and classical DAG fibre extrema

Let `E=[r]x[c]`, with `0<=r<=c`, and let `U(A)` be the union of all
maximum-cardinality matchings contained in `A`. Put `T(A)=E\U(A)`.
Write `q=r` and `m=rc`. Both the maximum-matching family and `U(A)` are
defined at rank zero; there the former contains just the empty matching.

### 5.1 Generic time mechanism, proved before the pilot

The optimum rank of `U(A)` equals that of `A`: it contains every optimum
of `A` and is a subset of `A`. The two optimum-matching families are
therefore identical, so `U(U(A))=U(A)`.

More generally take any hereditary feasible family of subsets of a finite
`m`-element ground set with maximum feasible size at most `q`, and define
`U` by the same union of cardinality optima. This includes matchings.
Along any orbit put `B_t=U(A_t)` and `rho_t=rank(A_t)`. Since
`B_{t+1} subseteq A_{t+1}=E\B_t`,

    B_t subseteq E\B_{t+1}=A_{t+2},  rho_{t+2}>=rho_t.

If the ranks are equal, every old optimum in `A_t` is still contained in
`A_{t+2}` and is still optimum, proving `B_t subseteq B_{t+2}`.
Consequently `(rho_{2s},|B_{2s}|)` strictly increases lexicographically
unless `B_{2s+2}=B_{2s}`. Equality of both coordinates when ranks are
equal forces equality of the sets; that implies
`A_{2s+3}=A_{2s+1}`, after which the orbit is two-periodic.
There are at most `(q+1)(m+1)` possible coordinate pairs. With
`L=q(m+1)+m=(q+1)(m+1)-1`, equality therefore occurs for some `s<=L`,
and every orbit reaches a period-at-most-two state by time `2L+1`.
This is the coarse checked bound, not a sharp matching-specific theorem.

If `E` is nonempty, a fixed point is impossible: `U(A) subseteq A` and
`A=E\U(A)` would force `U(A)` to be empty, then `A=E`, contradicting
the existence of an edge in a maximum matching of the nonempty rectangle.
Hence every recurrent orbit has exact period two. If `E` is empty its
only state is fixed. This entire temporal deduction is generic finite
optimization plus complementation; no new sharp clock is claimed.

### 5.2 A complete all-parameter fibre extremum, derived after the pilot

Let `a_k` be the number of loopless directed acyclic graphs on a fixed
labelled `k`-element vertex set, allowing either direction between two
different vertices but no directed cycles. Then `a_0=a_1=1`, and

    a_k = sum_{j=1}^k (-1)^(j+1) binom(k,j) 2^(j(k-j)) a_(k-j).

Indeed every nonempty DAG has a source. If a specified set of `j`
vertices are all sources, there are no edges into them or between them,
arbitrary edges from them to the other vertices, and an arbitrary DAG on
the remaining vertices. Inclusion-exclusion over the events that each
vertex is a source proves the formula. The first values are
`a_0,...,a_4=1,1,3,25,543`. This is classical DAG counting, not a new
enumeration primitive attributed to AMC.

**Theorem.** If `r>=2`, the largest AMC fibre is exactly `a_r`. Its
targets are exactly `E\M`, where `M` is a matching saturating all `r`
rows. Thus there are `c!/(c-r)!` maximum-fibre targets. If `r=1`, AMC
is ordinary complementation and every target has fibre one; if `r=0`,
the unique target has fibre one. These statements cover every rectangle
in the stated carrier family, not only the pilot boxes.

**Proof of the upper bound.** Fix a nonempty fibre with target `Y`, set
`B=E\Y`, and choose once and for all a maximum matching
`M={(u_i,v_i):1<=i<=k}` of `B`. If `U(A)=B`, then `B subseteq A` and
`rank(A)=rank(B)=k`, so this same `M` is a maximum matching of `A`.

An edge `e in A\B` cannot touch an unmatched row and a matched column:
replacing that column's edge of `M` by `e` gives a size-`k` matching
containing `e`, making it allowed, a contradiction. The symmetric
argument excludes a matched row and unmatched column. An edge between
two unmatched endpoints would augment `M`. Thus every extra edge has
the form `(u_i,v_j)`, with `i!=j`. Encode it as a directed edge `i->j`.
These extra edges cannot contain a directed cycle: rotating the matching
along that cycle gives another size-`k` matching containing its edges,
again contradicting their absence from `B`. The assignment

    A -> D(A)= {i->j : (u_i,v_j) in A\B}

is injective, since `A=B` plus those encoded edges, and lands in labelled
DAGs on `k` vertices. Every fibre is therefore at most `a_k<=a_r`.

**Attainment and exact inverse at extremal targets.** Suppose `B=M`
saturates all rows. For each DAG `D` on `[r]`, add its encoded edges
to `M` and leave every unmatched column isolated. Any other row-saturating
matching on the same matched columns differs from `M` by a nontrivial
permutation cycle, which would be a directed cycle in `D`. Hence `M`
is the unique maximum matching. Conversely the injection just proved
shows that every source with `U(A)=M` arises in exactly this way.
Thus this whole fibre is bijective with the `a_r` labelled DAGs.

**No other equality target when `r>=2`.** For `k<r`, `a_k<a_r`:
isolating an added vertex is an injection into the next labelled DAG
set, strict from size one onward, while `a_0=a_1<a_2`. So equality
requires `k=r` and every row is matched by `M`. If `B!=M`, take
`f in B\M`. If its column is matched, it is some `(u_i,v_j)` with
`i!=j`; the singleton DAG `{i->j}` cannot be an extra-edge graph,
since `f` is already in `B`. Our injection is then not surjective and
the fibre is strictly smaller than `a_r`.

Otherwise `f=(u_i,w)` uses an unmatched column. Choose `j!=i`, possible
because `r>=2`. The singleton DAG `{j->i}` also cannot arise. If
`(u_j,v_i)` is already in `B` this is immediate. If it were an extra
edge, replacing `(u_i,v_i),(u_j,v_j)` in `M` by
`(u_i,w),(u_j,v_i)` would give another size-`r` matching containing
that extra edge; the distinctness of rows and columns is explicit, so
it would be allowed after all. This contradiction again excludes one
DAG and makes the fibre strictly smaller. Therefore `B=M` is necessary.
For `r=1`, every edge of `A` individually is a maximum matching whenever
`A` is nonempty, so `U(A)=A`; the empty case gives the same identity.
The `r=0` statement is immediate. This completes the theorem.

### 5.3 What the theorem does not close

The theorem evaluates the global maximum, all equality targets and their
complete inverses. It does **not** evaluate every nonextremal target
fibre, nor supply a matching-specific sharp height or a new recurrent
mechanism after the generic optimization deduction. The source identity
`T^{-1}(Y)=U^{-1}(E\Y)` remains exact. The DAG adapter uses the classical
unique-perfect-matching/alternating-cycle encoding already present in old
UPC/UPA background; it is not claimed globally new because the literal
ambient-complement iteration was not located in a bounded source search.

The observed heights are `r` for every tested rectangle with `r>=2`,
and zero for `r<=1`. We did not prove this proposed sharp bound for
all rectangles. In particular the observed `4x4` depth-four tail

    989 -> 64546 -> 9181 -> 56883 -> 13260

uses the intake's low-bit-first row-major encoding and ends on a two-cycle;
it refutes a universal height-at-most-three extrapolation. The full pilot
is preserved rather than replaced by a smaller favourable rectangle.

**Disposition:** `GENERIC_TEMPORAL_ADAPTER / CLASSICAL_DAG_EXTREMA /
HOLD_SHARP_MATCHING_CLOCK / NO_PROMOTION`. A true static theorem does
not supply the missing materially new conjunction. No candidate admission
is requested on the strength of these finite heights or the DAG formula.

## 6. EIM: exact idempotent image, no pilot

Let `I(A)` be the intersection of all maximum matchings in `A`. That
family is nonempty. Its intersection is a subset of any member, hence
is itself a matching. On a matching `M`, the unique cardinality-optimal
matching is `M` itself, so `I(M)=M`. Therefore `I^2=I` on every finite
rectangle, including the empty one. The image is exactly the set of
matchings, all recurrent states are fixed, and depth is at most one.
This consensus-image projection completely consumes the proposed time
axis; an inverse constraint on forced matching edges cannot change it.
**Desk kill / no pilot / no promotion.**

## Evidence, authorship and source boundary

HMP, SSC and AMC were actually executed twice from fresh source-only
copies with `python -I -B`, no imported historical/producer code, no
input-data reads and no randomness. Each produced the complete 4,871,812
bytes, 44 boxes, 79,143 state-map pairs and 699,516 checks. Both actual
`cmp` commands against `CANONICAL.json` exited zero. The canonical SHA-256
is `b0e7a2aee8a6afa8f9e3488647364d08638612eb06d2d86a8048ed1ea0e2dd75`.
The two raw stderr files are empty. No failed mathematical execution
occurred; rejected hypotheses, source access limitations and killed desk
literals remain documented rather than labelled execution failures.

The new AMC extremal deduction postdates the immutable pilot and is not
retroactively counted among its 699,516 checks. A separately named
artifact-consuming extrema audit checks that deduction against the same
complete bounded output. It is author evidence, not a new map pilot,
source-only full-map replay, enlarged cutoff or independent review.

Read [SOURCE_AND_COLLISION.md](SOURCE_AND_COLLISION.md) for exact primary
access and historical-read limits and [desk/HISTORY.md](desk/HISTORY.md)
for the original literal comparisons. The DAG proof above is self-contained
author reasoning, not an assertion that an unread source proved AMC's
extremum. No source non-hit proves novelty. `HOLD_EXTERNAL` remains.
