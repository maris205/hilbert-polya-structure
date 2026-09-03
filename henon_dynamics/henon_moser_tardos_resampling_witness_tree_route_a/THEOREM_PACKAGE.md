# Theorem package

## Claim

Let `X_1,...,X_n` be mutually independent random variables with finite domains and let `A` be a finite family of bad events.  Write `vbl(A)` for the variables determining `A`, and let `Gamma(A)` contain exactly the distinct events sharing a variable with `A`.  Give each variable an independent infinite table of fresh samples.  At every step choose by any rule one currently violated event and advance exactly the tables of its variables.

Assume numbers `x_A in (0,1)` satisfy

`P(A) <= x_A product_{B in Gamma(A)}(1-x_B)`.

Then the algorithm terminates almost surely at an assignment avoiding all bad events, and, if `N_A` is the number of resamplings of `A`,

`E[N_A] <= x_A/(1-x_A)` and

`E[sum_A N_A] <= sum_A x_A/(1-x_A)`.

## Status

PROVABLE AS STATED.

## Dependency map

1. A backward scan of any finite execution prefix produces a proper witness tree.
2. A fixed proper tree can occur only if a collection of independent table entries makes every vertex label true.
3. A multitype branching process assigns total mass at most one to the finite proper trees rooted at a fixed event.
4. Distinct resamplings of one label have distinct trees, so the tree sum bounds `E[N_A]`.
5. Finite total expectation gives almost-sure termination; legality gives avoidance at termination.

## Proof

### 1. Tables and logs

For every variable `X_i`, let `X_i(0),X_i(1),...` be independent copies of `X_i`, with all entries independent across both indices.  The current value is the entry indexed by the number of earlier resamplings involving that variable.  Conditional on all tables, a choice rule fixes the execution log `C(1),C(2),...`.  No argument below assumes how a currently violated event is chosen.

### 2. Backward proper witness trees

Fix a resampling time `t` with `C(t)=A`.  Start a rooted tree with root label `A`.  Scan `C(t-1),...,C(1)` backward.  When `C(s)` shares a variable with at least one label already present, attach a new vertex labelled `C(s)` to a deepest overlapping vertex, using a fixed tie rule only to make the construction unique; otherwise discard it.

Every child label belongs to `Gamma^+(B)=Gamma(B) union {B}` for its parent label `B`.  Siblings have distinct labels: if a second child with the same label were proposed, the previously inserted copy would be a deeper overlapping vertex and would receive the new copy instead.  Thus the tree is proper.

### 3. Witness-tree probability lemma

Define the canonical `T`-check without reference to any execution log.  Order the vertices by non-increasing distance from the root, breaking ties by a frozen label/path order.  Start at the zeroth entry of every variable table.  At a vertex `v`, test `label(v)` on the current entries of its variables and then advance exactly those variables.  Each vertex test uses table cells unused by every other vertex test, so independence gives

`P(the canonical T-check passes) = product_{v in T} P(label(v))`.  (1a)

It remains to connect an occurrence to this fixed check.  Suppose the backward construction at time `t` produces `T`.  Retain from the actual log the resamplings represented by its vertices.  Before a retained vertex `v`, every earlier resampling involving one of its variables is retained: when encountered in the backward scan it overlaps the already present vertex `v`.  Fix a variable `Y`.  When an earlier retained event containing `Y` is scanned, it overlaps every already present `Y`-vertex.  The chosen deepest overlapping parent therefore has depth at least the maximum current depth of all `Y`-vertices, so the new vertex has depth strictly greater than every existing `Y`-vertex.  Consequently chronological order among all vertices using `Y` is exactly decreasing depth, even though those vertices need not form one ancestor chain.  The canonical non-increasing-depth order preserves that relative order for every variable.  Thus every vertex reads the same numbered table cell for each variable in the log and in the canonical check.  The actual successful tests consequently force the canonical `T`-check to pass.

Combining this implication with (1a) gives

`P(T occurs) <= product_{v in T} P(label(v))`.  (1)

### 4. Branching summation

Fix a root label `A`.  Generate a random labelled tree by starting with root `A`; independently for every vertex labelled `B` and every `D in Gamma^+(B)`, add one child labelled `D` with probability `x_D`.  This produces proper trees, possibly infinite.  If `T` is a finite proper tree rooted at `A`, direct multiplication of chosen and omitted child probabilities gives

`P_branch(T) = [(1-x_A)/x_A] product_{v in T} [x_label(v) product_{D in Gamma(label(v))}(1-x_D)]`.  (2)

The assumed criterion and (2) imply

`product_{v in T} P(label(v)) <= [x_A/(1-x_A)] P_branch(T)`.

Summing over every finite proper tree rooted at `A`, and using that their branching probabilities sum to at most one, yields

`sum_T product_{v in T} P(label(v)) <= x_A/(1-x_A)`.  (3)

### 5. Counts, termination, and output

For successive resamplings of `A`, the associated witness trees are distinct: the tree of the `k`-th occurrence contains exactly `k` vertices labelled `A`, because every earlier copy overlaps the existing `A` chain and is inserted.  By (1), monotone convergence, and (3),

`E[N_A] <= sum_T P(T occurs) <= x_A/(1-x_A)`.

Summing over the finite event family gives the asserted total expectation.  A nonnegative extended integer with finite expectation is finite almost surely, so the log terminates almost surely.  A legal rule terminates only when no event is violated; the terminal assignment therefore avoids the whole bad-event family.

## Boundaries and nonclaims

With no bad events the empty algorithm terminates immediately.  Zero-probability bad events cause no resampling and may be retained under any positive witness value.  The proof is sequential and variable-model specific; it does not assert lopsided, permutation, parallel, or outside-criterion extensions.  Finite evidence fixes lexicographic selection only for reproducibility, while the theorem covers every legal rule.
