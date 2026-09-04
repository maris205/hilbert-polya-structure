# P185 proof package

**Status:** `ROUND2_DUAL_REVIEW_FREEZE`; all findings closed  
**Lifecycle:** `OWNER_AMBER / HOLD_EXTERNAL`

## Lemma chain

1. `d=P(w)` starts at zero and has increments in `{0,1}`; the increment at
   `i` is the novelty of source letter `w_{i-1}`.
2. Every prefix of such a path contains all levels from zero to its endpoint,
   so `P(d)_i=d_{i-1}+1`.  Iteration yields the pointwise delay formula.
3. The formula forces identity coordinates `0..t`, leaving exactly
   `n-t-1` free binary rises.  Conversely every such path is realised by
   choosing fresh/old letters.
4. The time-`t` state is the identity exactly when the first `n-t` source
   letters are distinct.  Taking the least time proves the point clock.
5. For `n>=3`, a source has depth `n-1` exactly when its first two letters
   agree, giving the full sharp set and `n^(n-1)` count.  The `n=2` carrier
   instead has all three nonidentity words at its unit maximum depth.
6. The target exposes each visible novelty bit.  With `d_q` letters already
   seen, a rise has `n-d_q` choices and a flat has `d_q`; the first and last
   invisible positions supply the remaining powers of `n`.
7. The identity target forces all visible rises, so its fibre equals the
   falling-factorial depth CDF.

## Boundary checks

- `n=1`: the only word `(0)` is fixed and has depth zero.
- `n=2`: `01` is fixed and the other three words have depth one; this is the
  sole exception to the `n^(n-1)` deepest count.
- `t=n-1`: the image is the singleton identity and the fibre is the full
  carrier of size `n^n`.
- Nonidentity permutations have `rho=n` but depth one, explaining the
  `max(1,n-rho)` clause.
- The already-fixed identity is separated from the positive-time distinct
  prefix criterion.

No finite enumeration is used in the proofs.
