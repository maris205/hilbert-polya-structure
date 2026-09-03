# Narrative report — first-descent prefix reversal

**Paper:** P181  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

## One-sentence result

Reversing exactly the prefix that ends one position after a permutation's
first descent produces a depth-two functional graph whose image, recurrent
two-cycle core, every depth population, every target fibre, and all
maximum-fibre targets have closed descriptions.

## Literal map

For a permutation `pi in S_n`, let `d(pi)` be the first position with
`pi_d > pi_(d+1)`.  The increasing permutation is fixed.  Otherwise reverse
the prefix of length `d(pi)+1`:

```text
F(pi_1 ... pi_d pi_(d+1) ...) =
  pi_(d+1) pi_d ... pi_1 pi_(d+2) ... .
```

The trigger and the action are both part of the definition.  In particular,
this is not the Project Euler “First Sort” rule, which moves only the smaller
follower to the front.

## Frozen five-claim contract

1. For `n>=3`—in fact already for `n=2`—the image is exactly
   `I_n={tau:tau_1<tau_2}`, so it has `n!/2` elements.
2. For `n>=3`, the recurrent set is the identity together with the `n!/3`
   permutations satisfying `tau_1<tau_2>tau_3`.  The identity is fixed; the
   peak-at-two states form `n!/6` two-cycles under three-prefix reversal.
3. With tail equal to distance to recurrence, the exact census for `n>=3`
   is

   ```text
   tail 0: n!/3 + 1,
   tail 1: n!/2,
   tail 2: n!/6 - 1.
   ```

   There is no larger tail.
4. A target outside `I_n` has no predecessor.  For `tau in I_n`, let
   `r(tau)` be the length of the maximal decreasing run starting at position
   two.  Its predecessors are exactly the prefix reversals of lengths
   `2,...,r(tau)+1`, plus the identity itself when `tau` is the identity.
   Thus the distinct fibre size is `r(tau)+1[tau=id]`.
5. For `n>=4`, the maximum fibre is `n-1`.  It is attained at exactly the
   `n-1` targets with `tau_2=n` and
   `tau_2>tau_3>...>tau_n`.  At `n=3`, those two targets and the identity all
   have maximum fibre two.  At `n=2`, the identity alone has fibre two.  At
   `n=1`, the sole state is fixed, has depth zero, and has fibre one.

## Proof spine

Every nonfixed output begins with the reversed descent pair, hence with an
ascent.  Conversely, swapping the first two entries of any target beginning
with an ascent gives a predecessor, proving the image theorem.

Inside the image, a peak at position two triggers a three-prefix reversal;
its reversal is another peak and the next step returns.  Any other
nonidentity image state begins with at least three increasing entries.  Its
first-descent reversal has a peak at position two, so it enters the recurrent
core in one step.  Since all states enter the image in one step, every tail
has length at most two.

For the inverse atlas, reverse the first `k` entries of a target.  The result
has its first descent at `k-1` exactly when the target decreases from position
two through position `k`.  This turns the local decreasing run into the full
predecessor set.  Image states outside the recurrent core have run length
one, so each has one predecessor outside the image; this bijection supplies
the depth-two census.

## Claim ceiling and evidence

Arbitrary prefix reversal, pancake sorting, longest-increasing-prefix cuts,
elementary descent counting, and finite-map bookkeeping receive zero
contribution credit.  P122 already uses deterministic permutation block
reversal and target-local fibres; that general proof vocabulary is also zero
credit.  The retained conjunction is only the autonomous first-descent
choice with the five-part atlas above.

The paper-local verifier reconstructs the complete map, inverse table, orbit
coordinates, and maximizer set through `S_9`, including the `n=1,2,3`
boundaries.  Its integer assertions are counterexample pressure rather than
an all-`n` proof or novelty evidence.  A bounded source non-hit leaves the
paper `OWNER_AMBER / HOLD_EXTERNAL`.
