# Provisional theorem spikes

Only the two survivors from the frozen denominator appear here.  They are
unassigned theorem packages, not papers.  Every statement below is a uniform
claim/proof target suggested by exact finite pressure; neither package has
passed external owner review.

## G01 TRC — transpose after row compression

### Literal object

For `n>=1`, let `X_n={0,1}^{n x n}` with fixed row and column order.  Write
`r_j(A)=sum_k A_{jk}` and define

\[
  F(A)_{ij}={\bf 1}\{i\le r_j(A)\},\qquad 1\le i,j\le n.
\]

Equivalently, left-justify the ones in each source row without permuting rows,
then transpose.  For a height vector `h=(h_1,...,h_n)` in `{0,...,n}^n`, let
`D(h)` denote the column-initial matrix whose column `j` has height `h_j`.
For a partition `lambda` padded to length `n`, let `lambda*` be its conjugate
inside the `n x n` square, and let `m_s(lambda)` count parts equal to `s`,
including zero parts.

### Uniform claim A: complete functional graph and exact clock

If `lambda(A)` is the weakly decreasing rearrangement of the row sums of
`A`, then

\[
 F^2(A)=D(\lambda(A)^*),\qquad
 F^3(A)=D(\lambda(A)),\qquad F^4(A)=F^2(A).
\]

Consequently:

1. the recurrent set is exactly the Ferrers matrices `D(h)` with
   `h_1>=...>=h_n`;
2. conjugation pairs the nonfixed recurrent states into 2-cycles;
3. the fixed states are exactly the self-conjugate Ferrers diagrams;
4. the preperiod is at most two;
5. the states of preperiod at most one are exactly those whose *labelled*
   source row-sum vector is already weakly decreasing.

This also gives exact layer sizes:

\[
\begin{aligned}
N_0(n)&={2n\choose n},\\
N_{\le1}(n)&=\sum_{n\ge\lambda_1\ge\cdots\ge\lambda_n\ge0}
                 \prod_{i=1}^n {n\choose\lambda_i},\\
N_2(n)&=2^{n^2}-N_{\le1}(n).
\end{aligned}
\]

Here `N_0` is the recurrent population and `N_2` is the exact deepest set,
not merely an upper bound.  The recurrent, fixed, and 2-cycle counts are
respectively

\[
 {2n\choose n},\qquad 2^n,\qquad
 \frac{1}{2}\left({2n\choose n}-2^n\right).
\]

### Uniform claim B: every-target inverse laws

For a time-one target `B`, the fibre is zero unless `B=D(h)` for some arbitrary
height vector `h`.  In the latter case

\[
 |F^{-1}(B)|=\prod_{j=1}^n {n\choose h_j}.
\]

For a time-two target `C`, the fibre is zero unless `C=D(h)` is Ferrers.  Put
`lambda=h*`.  Then

\[
 |(F^2)^{-1}(C)|=
 \frac{n!}{\prod_{s=0}^n m_s(\lambda)!}
 \prod_{s=0}^n {n\choose s}^{m_s(\lambda)}.
\]

Thus the first image has `(n+1)^n` states and the second image has
`binom(2n,n)` states.  The inverse laws include zero fibres and all boundary
heights `0,n`; they are not averages over targets.

### Proof route

The first update remembers precisely the labelled row-sum vector as column
heights.  Taking row sums of `D(r_1,...,r_n)` produces the conjugate of the
sorted multiset of the `r_j`.  A second conjugation returns the sorted row-sum
partition, proving `F^4=F^2`.  A Ferrers boundary path gives
`binom(2n,n)` recurrent states; diagonal hooks identify self-conjugate diagrams
with subsets of `{1,3,...,2n-1}`, giving `2^n`.  For fibres, independently
choose each row support at time one; at time two, first assign the prescribed
row-sum multiset to labelled rows and then choose each row support.

### Boundary, second axis, and collision subtraction

- **Boundary:** square binary relations, fixed labels/order, and the one
  synchronous deterministic map above.  Rectangular matrices, row sorting
  inside the update, graph relabelling, asynchronous compression, and random
  schedulers are outside the claim.
- **Second axis:** the every-target time-one and time-two fibres are logically
  separate from the conjugation/clock theorem and include exact image
  recognition.
- **Historical subtraction:** no cut statistic, parity filter, degree pruning,
  coordinate push/toggle, copying conflict, or singleton-isolation scheduler
  appears.  Hence the literal map is not a mechanical migration of
  P145/P159/P177/P179/P183.
- **Owner subtraction:** Ferrers matrices, conjugate partitions, and binary
  line sums are standard and directly adjacent.  The bounded search recorded
  in `OWNER_SEARCH_LOG.md` did not return this exact iterated operator, but
  that non-hit is **not** novelty evidence.  Status is `OWNER_AMBER` and
  `HOLD_EXTERNAL`.

## G02 ECSC — equal-component-size completion

### Literal object

For a labelled simple graph `G` on `[n]`, group its connected components by
their order.  If `U_s(G)` is the union of all components of order `s`, define

\[
 F(G)=\bigsqcup_{s:U_s(G)\ne\varnothing} K_{U_s(G)}.
\]

All equal-size source components are merged *simultaneously* into one clique;
different source sizes are never joined during that step.  If a component-size
multiset `M` contains `m_s` copies of `s`, define

\[
 \Phi(M)=\{s m_s: s\in\operatorname{supp}(M)\}
\]

as a multiset, retaining collisions among the displayed products.

### Uniform claim A: quotient clock, endpoint, and fixed states

The first image is always a cluster graph, and for every `t>=0`,

\[
 M(F^t(G))=\Phi^t(M(G)).
\]

For `t>=1`, the actual clique blocks are obtained by the corresponding nested
unions, so the deterministic terminal graph is unique.  Let

\[
 \kappa(M)=\min\{k\ge0:\Phi^{k+1}(M)=\Phi^k(M)\}
\]

and let `delta(G)=0` when `G` is already a cluster graph and `1` otherwise.
Then the exact stabilization time is

\[
 \tau(G)=\min\{t:F^{t+1}(G)=F^t(G)\}
        =\max\{\kappa(M(G)),\delta(G)\}.
\]

Every nontrivial `Phi` step strictly lowers the number of parts.  Hence
`kappa(M)<=c(G)-1`, and a nonfixed graph satisfies
`tau(G)<=max(1,c(G)-1)`.  The fixed graphs are exactly the cluster graphs with
pairwise distinct component orders.  Therefore their labelled count is

\[
 \sum_{\substack{\lambda\vdash n\\\text{parts of }\lambda\text{ distinct}}}
 \frac{n!}{\prod_{s\in\lambda}s!}.
\]

### Uniform claim B: every-target one-step fibres

Let `H` be a target.  If `H` is not a cluster graph, then `F^{-1}(H)` is empty.
Otherwise write its labelled clique blocks as `B_1,...,B_q`, with
`b_i=|B_i|`.  Let `c_s` be the number of connected labelled simple graphs on
an `s`-element vertex set (`c_1=1`).  Then

\[
 |F^{-1}(H)|=
 \sum_{\substack{s_i\mid b_i\ (1\le i\le q)\\
                  s_1,\ldots,s_q\ \text{pairwise distinct}}}
 \prod_{i=1}^q
 \frac{b_i!}{(s_i!)^{m_i}m_i!}\,c_{s_i}^{m_i},
 \qquad m_i=b_i/s_i.
\]

The formula is an image criterion as well: `H` lies in the first image iff the
displayed sum is positive.  Repeated target block sizes are allowed, but their
chosen source component sizes must remain distinct across target blocks.

### Proof route

At one step, the `m_s` source components of order `s` have vertex union of
order `s m_s`, proving the `Phi` semiconjugacy.  Duplicate part sizes are the
only reason for another merger, so part count is a strict Lyapunov function
until all sizes are distinct.  Completion of nonclique source components
accounts for the separate `delta(G)` term.  For a target block `B_i`, a
preimage chooses a divisor `s_i`, partitions `B_i` into `m_i=b_i/s_i`
unordered blocks of size `s_i`, and chooses a connected graph on every block.
Distinct `s_i` across different target blocks are necessary and sufficient to
prevent a cross-block merger, yielding the product-and-sum fibre formula.

### Boundary, second axis, and collision subtraction

- **Boundary:** labelled finite simple graphs and the simultaneous full
  size-class merger.  Pairwise/asynchronous merges, random schedules, weighted
  graphs, hypergraphs, and unlabeled orbit counts are outside the claim.
- **Second axis:** the graph-decorated every-target fibre formula uses the
  connected labelled graph numbers `c_s`; it is not implied by the
  size-multiset clock.
- **Historical subtraction:** the rule has no cut/parity/pruning/copy/toggle or
  singleton-isolation mechanism and is not a carrier lift of
  P145/P159/P177/P179/P183.  G03 and G11 were killed precisely because they
  *were* statistic-class transfers of this engine.
- **Classical subtraction:** cluster-graph editing/completion normally changes
  edges to obtain disjoint cliques but does not prescribe this equal-component
  batch merger.  The Glaisher bijection repeatedly merges **two** equal
  integer parts; here all `m_s` components merge at once (`s,s,s -> 3s`, not
  `2s,s`) and each inverse part carries an arbitrary connected graph.
  These differences are meaningful but do not establish ownership.  Status
  remains `OWNER_AMBER` and `HOLD_EXTERNAL`.

## Advancement gate

Neither spike may receive a paper number until an independent owner review
checks the exact literal update, scheduler, all-time statement, and fibre
formula.  A later full proof must also replace bounded computation as support
for every uniform claim.  Search non-hits may not be converted into a novelty
statement.
