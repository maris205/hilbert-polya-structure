# C91 theorem package

## Definitions

Let `L` be the sixteen frozen C75 labels and let `A_k` be the support of the
first `k` labels in a uniformly random permutation.  For each C88 target
`H_i`, set

`T_i = min{k : H_i <= Phi(A_k)}`.

For an unordered C88 pair `(i,j)` with neither target contained in the other,
define the three outcomes `i-first` (`T_i<T_j`), `tie` (`T_i=T_j`), and
`j-first` (`T_j<T_i`).

## Theorem

For every one of the 108 unordered incomparable target pairs, the C91 receipt
contains exact integer counts for the three outcomes, exact rational
probabilities, and a decomposition by common first-passage rank `k=0,...,16`.
The three counts sum to `16! = 20,922,789,888,000`.

If `S` is a support of size `k` and `x` is a label such that `S\\{x}` has not
hit a target while `S` has, then that boundary edge represents exactly
`(k-1)!(16-k)!` permutations.  Left-only pivotal edges are counted as `i`
first when `j` has not hit on `S`; right-only edges are counted symmetrically;
simultaneous pivotal edges are ties.  These three disjoint edge classes
partition all permutations and establish the reported race law.

The checker reconstructs every edge class from the C88 bitsets, the SymPy
cross-check verifies all rank weights and normalized outcome generating
functions, and clean replay preserves the evidence digest.  The result is
finite and combinatorial under `NO_BAD_EULER_OR_ROOT_NUMBER`.
