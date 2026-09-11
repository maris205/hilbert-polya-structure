# P187--P191 combinatorial theorem spikes

Status: `C21_PDCF` is the sole survivor, with
`OWNER_AMBER / HOLD_EXTERNAL`.  `C16_MGBF` has a complete mathematical spike
but is killed by a direct largest-gap split owner.  Neither entry is a novelty,
priority, authorship, or release claim.

## Survivor: C21_PDCF, prefix-divisibility cut filter

### Definition and boundary conventions

Fix `N>=1`.  Let `Comp_N` be the positive compositions

`a=(a_1,...,a_k),     a_1+...+a_k=N`,

and put `s_i=a_1+...+a_i`.  The internal cut set is
`D(a)={s_1,...,s_(k-1)}`.  Define `F_N(a)` by retaining an old internal cut
`s_i` if and only if `a_i | s_i`, deleting every other old cut
simultaneously, and reading the unique composition determined by the retained
cut set.  Thus

`D(F_N(a))={s_i in D(a): a_i | s_i}`.                         (1)

The final endpoint `N` is not tested.  The first cut, when it exists, is
always retained because `a_1|s_1=a_1`.  For `N=1`, the only state is `(1)`.

### Theorem C21-A: recurrence, fixed enumeration, and sharp clock

For every `N>=1`:

1. `F_N` is a total self-map and every orbit is eventually fixed.
2. A composition is fixed exactly when `a_i|s_i` for every `i<k`.
3. Define `A(0)=1` and, for `1<=v<N`,

   `A(v)=sum_{0<=u<v, (v-u)|v} A(u)`.                         (2)

   Then the exact number of fixed states is

   `f_N=sum_{v=0}^{N-1} A(v)`.                               (3)

4. The largest tail is

   `M_N=0` for `N<=3`, and `M_N=N-3` for `N>=4`.              (4)

   For every `N>=4`, the unique state attaining `M_N` is

   `omega_N=(1,2,1^(N-3))`.                                  (5)

#### Proof

Equation (1) shows that the cut set never increases.  If a state is not fixed,
at least one of its cuts is deleted; hence no nontrivial cycle is possible and
the fixed-state criterion follows.  A fixed composition is equivalently a
path

`0=x_0<x_1<...<x_r<N`

whose step `x_j-x_(j-1)` divides its endpoint `x_j`, followed by the
unconstrained final step to `N`.  Last-cut decomposition gives (2) and (3).

Now let a nonfixed composition have `k` parts.  Its first cut is permanent, so
at most `k-2` cuts can be deleted.  The only length-`N` composition is all
ones and is fixed, so a nonfixed state has `k<=N-1`.  Every nonterminal
iteration deletes at least one cut, proving `tail(a)<=N-3`.  Direct inspection
settles `N<=3`.

For `N>=4`, start with `omega_N`.  After `t` steps, for
`0<=t<=N-3`, the state is

`F_N^t(omega_N)=(1,2+t,1^(N-3-t))`.                           (6)

Indeed, while the middle part is nonfinal, its ending prefix is `3+t`, and
`2+t` cannot divide `3+t` because it cannot divide their difference one.
Exactly its following cut is therefore deleted.  This proves the lower bound
in (4).

If equality holds in the upper bound, the initial state has `N-1` parts and
exactly one cut disappears in each of `N-3` rounds.  A positive composition
of `N` with `N-1` parts has one part two and all other parts one.  The two
cannot be first or final, because either placement is fixed.  If it has `r>=1`
leading ones, there are only `N-r-2` cuts to its right that its growing merged
part can consume.  Equality with `N-3` forces `r=1`, hence the state is (5).
This also proves strictness of every other extremizer candidate.

### Theorem C21-B: every-target one-step fibres and the image

Fix a target `b in Comp_N` and let `T=D(b)`.  Make a directed acyclic graph on
the vertices `0,1,...,N`.  An edge `u->v`, with `u<v`, is admissible precisely
when:

1. no target cut lies strictly between its endpoints:
   `T intersect {u+1,...,v-1}` is empty; and
2. if `v<N`, then

   `(v in T)  iff  (v-u)|v`;                                  (7)

   at `v=N` there is no divisibility test.

Put `P_b(0)=1` and compute

`P_b(v)=sum_{u<v, u->v admissible} P_b(u)`.                    (8)

Then

`|F_N^{-1}(b)|=P_b(N)`,                                      (9)

and `b` belongs to the one-step image exactly when `P_b(N)>0`.  The recurrence
uses `O(N^3)` elementary operations as written (or `O(N^2)` after prefixing
the no-skipped-target test).  Moreover,

`sum_{b in Comp_N} P_b(N)=2^(N-1)`.                           (10)

#### Proof

A source composition is uniquely a path
`0=x_0<x_1<...<x_m=N`; each nonfinal vertex is one of its old cuts, and the
incoming edge length is the corresponding source part.  Since output cuts are
a subset of source cuts, a source edge cannot skip a member of `T`, giving
condition 1.  At a nonfinal source cut `v`, rule (1) retains it exactly when
its incoming part `v-u` divides `v`; requiring the retained cuts to be exactly
`T` gives (7).  Conversely, every admissible path defines a unique source and
maps to `b`.  This is a bijection, so last-edge decomposition proves (8)--(9),
and positivity proves the image criterion.  Finally, every one of the
`2^(N-1)` source cut sets has exactly one target under a function, proving
(10).  The verifier checks both each target fibre and (10), rather than using
mass conservation as a substitute for target-local equality.

### Independent axes and exact evidence

The clock/extremizer proof uses the monotone loss of old cuts.  The fibre proof
uses a source-path/target-cut bijection and does not follow from the clock.
The deterministic complete boxes `1<=N<=15` verify closure, every orbit,
every fixed state, (2)--(6), every target instance of (7)--(9), and the mass
identity (10).  At `N=15` there are 16,384 states, image 4,906, fixed set
1,763, maximum tail 12 with one deepest state, and maximum fibre 182.

### Internal mechanism subtraction

- P126 refines every part by a balanced binary split.  C21 only coarsens and
  deletes an old cut according to the arithmetic relation between its incoming
  edge length and absolute endpoint.
- P147 consolidates maximal adjacent runs of equal parts.  C21 neither tests
  adjacent equality nor merges an entire run; an arbitrary failed divisibility
  cut may disappear.
- P169 transfers final occurrences between cyclically ordered set-partition
  blocks.  Its carrier, conserved tokens, recurrence, and inverse mechanism do
  not occur here.
- P181 reverses a permutation prefix chosen by its first descent.  C21 changes
  neither a permutation nor order within a prefix and has monotone cut loss.
- P185 writes prefix-diversity values into a word.  C21 uses an absolute prefix
  endpoint only in a divisibility predicate and outputs a coarsening, not a
  prefix statistic word.
- P186 compresses a subset by the support of rank-shifted labels and evolves
  gaps by erosion.  C21's cut set is a standard subset encoding, but its update
  depends jointly on the previous cut and current endpoint; it is not support
  compression or gap erosion.
- P131 rotates canonical Euclidean quotient lists.  Quotient/continuant and
  cyclic-rotation machinery receive no credit here; C21 performs no Euclidean
  division sequence and has only fixed recurrence.

The generic composition--subset bijection, last-cut dynamic programming, and
ordinary divisibility are background and receive zero contribution credit.
The residual is only the literal self-map together with Theorems C21-A/B.

### Limits of the spike

There is not yet a closed formula for the full one-step image size or for
time-`t` fibres.  The DP is an exact computable theorem, not a product formula.
The bounded search recorded in `OWNER_SEARCH.md` is not an ownership clearance.
The candidate remains `OWNER_AMBER / HOLD_EXTERNAL`.

## Killed but mathematically closed: C16_MGBF

### Exact update and Cartesian split tree

For a nonempty sorted block `B=(b_1<...<b_s)`, let `g(B)` be its largest
internal adjacent gap (zero for a singleton).  If `s>=2`, split immediately
after the **leftmost** occurrence of `g(B)`; write the pieces `L(B),R(B)`.
Define a binary tree recursively by rooting it at `B` and attaching the trees
of `L(B),R(B)`; singletons are leaves.  Let `h(B)` be its height, so

`h(B)=0` for `|B|=1`, and
`h(B)=1+max(h(L(B)),h(R(B)))` otherwise.                       (11)

On a set partition `pi`, C16 simultaneously replaces every nonsingleton block
by its two children.

### Theorem C16-A: all iterates and sharp pointwise clocks

At time `t`, each initial block `B` has become exactly the nodes obtained by
cutting its split tree at depth `t`, retaining an earlier leaf when a branch
has already ended.  Consequently

`tail(pi)=max_{B in pi} h(B)`.                                (12)

The discrete partition is the unique recurrent/fixed state.  On `Pi_n`, the
maximum tail is `n-1`, attained uniquely by the indiscrete partition.  The
last assertion follows because `h(B)<=|B|-1`; equality `n-1` requires one
block of size `n`, and the consecutive-label block splits successively at its
leftmost unit gap.  Induction on `t` proves the tree-level description.

### Theorem C16-B: every-target matching fibres

For disjoint target blocks `A,B` with `max A<min B`, put
`d=min B-max A`.  Call the ordered pair compatible when

`g(A)<d` and `g(B)<=d`.                                       (13)

The strict/weak asymmetry is forced by the leftmost tie convention: an equal
gap inside `A` precedes the boundary and steals the split, while an equal gap
inside `B` follows the boundary.  Build a graph on the blocks of a target
partition, joining a pair if one of its two orders satisfies (13).  Then the
one-step fibre size is the number of matchings that cover every nonsingleton
target block and may leave only singleton blocks unmatched.  Hence the target
is in the image exactly when such a matching exists.

To prove this, pair the two target children of each nonsingleton source block;
(13) is exactly the condition that their union splits at their boundary.
Every unpaired source block must be an unchanged singleton.  Conversely,
merge every matched pair and retain every unmatched singleton.  These two
constructions are inverse, so the count is target-local and exact.  Complete
enumeration through `Pi_9` verifies every target: at `n=9`, image 1,320,
maximum tail eight, unique deepest state, and maximum fibre 2,620.

### Fatal owner subtraction

Abbey, Diepenbrock, Langville, Meyer, Race, and Zhou, *Data Clustering via
Principal Direction Gap Partitioning*, arXiv:1211.4142, explicitly sort
projected points and split at the largest adjacent gap.  In one dimension that
is the local C16 block operation.  Their algorithm chooses clusters by a
different global scheduler and includes practical tolerances, whereas C16
splits every current block synchronously and fixes a leftmost tie.  Those
scheduler details do not justify claiming an unowned literal update engine.
The Cartesian-tree and matching consequences are mathematically useful, but
C16 is `KILL_DIRECT_UPDATE_OWNER`, not a reserve or survivor.
