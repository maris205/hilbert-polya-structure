# Root spike R02 — self-cardinality prefix toggles

Status: `PROVISIONAL_SURVIVOR / INTERNAL_HOSTILE_GATE / OWNER_AMBER /
HOLD_EXTERNAL`.

For `A subseteq [n]`, define the literal map

`F_n(A)=A symmetric-difference [|A|]`.

This is deliberately compared against P188's intersection map before any
number is allocated.  The common carrier and endogenous prefix receive zero
contribution credit.  The residual dynamics is nonmonotone: its image is a
whole parity layer and its recurrent part contains long even cycles, whereas
P188 is an absorbing rank recursion.

## Closed theorem axes

1. The image is exactly the even-cardinality subsets.  If `B` has odd size,
   its fibre is empty.  The empty target has `n+1` predecessors, namely all
   prefixes.  If `|B|=2r>0` and
   `B={b_1<...<b_(2r)}`, then

   `|F_n^{-1}(B)|=b_(r+1)-b_r`.

   Indeed a source of size `k` is forced to be `B triangle [k]`, and its size
   is `k` exactly when `|B intersect [k]|=r`.
2. The full nonzero indegree distribution follows: for `r>=1`, the number of
   weight-`2r` targets with fibre `g` is

   `sum_i binom(i-1,r-1) binom(n-i-g,r-1)`,

   over indices for which the binomial factors are defined.  The empty target
   contributes one fibre of size `n+1`; total mass is `2^n`.
3. The empty set is the unique fixed point.  A nonempty state `A` lies on a
   two-cycle iff `k=|A|` is even and
   `|A intersect [k]|=k/2`.  Hence the number of states on exact two-cycles is

   `sum_{even k>=2} binom(k,k/2) binom(n-k,k/2)`.

4. Every nontrivial cycle has even length: coordinate `1` is toggled at every
   step of such a cycle.  The zero-extension embedding and the pair-doubling
   embedding `delta(A)=union_{i in A}{2i-1,2i}` commute with `F`; therefore
   every functional graph occurs inside all larger dimensions and inside its
   doubled dimension.
5. Direct orbit certificates give exact periods `4` at `n=5`, `8` at `n=12`,
   and `16` at `n=30`.  These are existence theorems, not a claim that all
   possible periods or the full recurrent locus have been classified.

The paper contract, if promoted, must say explicitly that it gives a complete
one-step inverse atlas and a complete two-cycle census but not a complete
functional-graph classification.  Search non-hits are not novelty evidence.
