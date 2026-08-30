# R3 proof spike: maximal permutation-bond-run contraction

**Status:** theorem spike passed; independent owner gate still required  
**External status:** `HOLD_EXTERNAL`

## Literal map

For a permutation `pi`, a bond is a pair of adjacent positions whose values
differ by one.  Cut `pi` into maximal bond runs.  Distinctness forces every
such run to be monotone, and its values form a consecutive interval.  Replace
each run by its minimum and standardize the resulting word.  Denote the map
by `K` on the disjoint union of all finite symmetric groups.

Bond terminology, static bond enumeration, and one-deletion pattern facts are
classical and receive zero credit; see Homberger's
[Counting Fixed-Length Permutation Patterns](https://arxiv.org/abs/1211.7117).
Monotone interval inflation is also standard permutation-pattern machinery.
The residual proposed here is the **iteration** of simultaneous maximal-run
contraction, its sharp deepest family, and a target-local fibre partition
function.

## Exact length loss and recurrence

If `b(pi)` is the number of bonds, each maximal run of length `s` contributes
`s-1` bonds and contracts to one symbol.  Therefore

\[
  |K(\pi)|=|\pi|-b(\pi).
\]

The fixed points are exactly the bond-free permutations.  Every other step
strictly lowers length, so all recurrent states are fixed and every
permutation of length `n` has depth at most `n-1`.

## Sharp depth and deepest census

Depth `n-1` is possible only if every one of the first `n-1` updates lowers
length by exactly one.  Equivalently, every nonterminal state on the orbit
has exactly one bond.

If a target permutation `sigma` has exactly one bond, then it has exactly two
length-`|sigma|+1` preimages having exactly one bond.  In interval-inflation
coordinates, the sole target bond joins consecutive values `j,j+1`; the only
admissible single two-letter inflation expands one or the other endpoint,
with its orientation forced so that the old target bond is broken while the
new internal bond is retained.  Every other choice either preserves the old
bond as a second bond or creates an additional boundary bond.

Starting from the unique length-one state, the two lifts at each level give

\[
  D_1=1,\qquad D_n=2D_{n-1}=2^{n-1}.
\]

Thus the global depth is exactly `n-1`, and precisely `2^(n-1)` states attain
it.

## Complete target-local fibre series

Fix `sigma in S_k`.  A preimage is obtained by inflating each value `j` to a
nonempty monotone interval `I_j`, with the intervals ordered by value and the
blocks ordered in positions according to `sigma`.  Give block `j` one of
three states:

- `0`: a singleton, with weight `x`;
- `+`: an increasing block of length at least two, with weight
  `x^2/(1-x)`;
- `-`: a decreasing block of length at least two, with the same weight.

Only a positional adjacency of the consecutive target values `j,j+1` can
accidentally join two inflated blocks into one larger bond run.

- If `j` occurs immediately before `j+1` in `sigma`, forbid both states from
  lying in `{0,+}`.
- If `j+1` occurs immediately before `j`, forbid both states from lying in
  `{0,-}`.

Let `A(sigma)` be the resulting admissible set of three-state assignments and
let `h(eta)` be the number of nonzero states.  The exact fibre OGF is

\[
  P_\sigma(x)=
  \sum_{\eta\in A(\sigma)}
  x^{k+h(\eta)}(1-x)^{-h(\eta)}.
\]

Consequently

\[
  \#\{\pi\in S_n:K(\pi)=\sigma\}=[x^n]P_\sigma(x).
\]

The admissibility graph is the signed subgraph of the value path
`0--1--...--(k-1)` selected by positional adjacencies in `sigma`.  Hence the
series also has an explicit three-state transfer-matrix evaluation, component
by component.  This signed value-path fibre law is the second proof engine;
it is not used to prove monotone length loss.

For a target with exactly one bond, extracting `[x^(k+1)]` from this formula
recovers the two-lift lemma independently.

## Exact control

`r3_fibre_verify.py` exhausts all source permutations through length seven,
compares every target fibre with the three-state coefficient formula, checks
the exact length-loss identity, sharp depth, deepest census, and the two-lift
corollary.  The fresh run passed **14,778 assertions**.

The computation is falsification/control evidence, not proof and not a
novelty certificate.  A bounded exact-string and synonym search found the
classical bond/consecutive-run and inflation literature, but no direct owner
for this iterated contraction; that bounded no-hit is insufficient for
promotion.  A separate hostile owner audit must still decide whether the
residual clears the permutation-pattern literature and internal P105.

## Internal separation from P105

P105 keeps the ground set fixed and peels the least label from each cycle of
a permutation in cycle notation.  R3 works in one-line notation, contracts
all maximal interval-valued bond runs, changes the symmetric-group rank, has
many bond-free recurrent states, and has a signed interval-inflation fibre
model.  The common words `permutation`, `contraction`, and sharp depth
`n-1` are therefore not an identity of updates or proof engines.  This
separation remains a claim for the independent gate to attack, not a
pre-authorized paper slot.
