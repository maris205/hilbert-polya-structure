# FDR theorem package — first-descent prefix reversal

**Status:** `THEOREM SPIKE / OWNER AMBER / HOLD_EXTERNAL`.

For `pi in S_n`, fix the increasing permutation.  Otherwise let `d` be the
first descent position and reverse `pi_1,...,pi_{d+1}`.

For `n>=3` the following package is deductive.

1. The image consists exactly of the `n!/2` permutations with
   `pi_1<pi_2`.
2. The recurrent set consists of the identity and the `n!/3` permutations
   with a peak at position two, `pi_1<pi_2>pi_3`.  The identity is fixed and
   the latter states form `n!/6` two-cycles under reversal of the first three
   entries.
3. The exact tail census is
   `tail_0=n!/3+1`, `tail_1=n!/2`, and `tail_2=n!/6-1`.
4. A target outside the image has no predecessor.  For a target `tau` in the
   image, let `r(tau)` be the length of the maximal decreasing run beginning
   at position two.  Its distinct one-step fibre has size
   `r(tau)+1[tau=id]`.  For `n>=4` the maximum fibre is `n-1`, attained by
   exactly the `n-1` permutations with `tau_2=n` and
   `tau_2>tau_3>...>tau_n`.  At `n=3` the identity is one additional
   maximum-fibre target.

The proof reverses the initial increasing run.  Every nonfixed image state
with first descent at position two is paired with its three-prefix reversal;
an image state whose first descent lies later enters that core in one step.
The predecessors of `tau` are precisely the reversals through lengths
`2,...,r(tau)+1`, with the identity acquiring its additional fixed
predecessor.

Generic prefix reversal, pancake sorting, longest-increasing-prefix shuffle
algorithms, descent enumeration, and elementary finite-map bookkeeping are
zero credit.  A source stating this autonomous rule or an equivalent
functional graph kills the spike.
