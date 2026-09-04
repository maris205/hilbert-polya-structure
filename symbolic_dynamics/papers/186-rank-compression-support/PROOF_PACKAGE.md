# P186 proof package

**Status:** `ROUND2_DUAL_REVIEW_FREEZE`; all findings closed  
**Lifecycle:** `OWNER_AMBER / HOLD_EXTERNAL`

## Lemma chain

1. For `A={a_0<...<a_{k-1}}`, the weak list `b_j=a_j-j` has differences
   `b_j-b_{j-1}=g_j-1`.
2. Taking its support deletes zero differences and preserves positive
   differences in order.  Induction gives the time-`t` gap word
   `(g_j-t:g_j>t)`.
3. The least singleton epoch is therefore `max g_j`.  A gap `n-1` is possible
   only for `{0,n-1}`, proving the sharp unique global extremal.
4. A time-`t` source of `B={b_0<...<b_r}` has a unique gap factorisation
   `U_0,h_1+t,U_1,...,h_r+t,U_r`, where every letter in every `U_i` lies in
   `[1,t]`.
5. The long gaps consume `max(B)-min(B)+tr`; the `r+1` ordered short-word
   slots contribute `(1-(z+...+z^t))^{-(r+1)}`.  Cumulative coefficients up
   to the remaining ambient span give the full fibre.
6. Empty short slots prove the image criterion.  Choosing targets of fixed
   size proves the all-time image count; `t=1` yields the binomial fibre and
   Fibonacci image.
7. Independently, sets with clock at most `h` are a minimum plus a word of
   gaps in `[1,h]`.  Summing over total span proves the depth CDF.

## Boundary checks

- `n=1`: both states are fixed; height zero; first image has `F_3=2` states.
- `t=0`: `S_0=0`, the image is the full carrier, and every fibre is one.
- Empty target: only the empty source; it is separated from the nonempty
  generating-function formula.
- Singleton target: `r=0`; short gaps may all disappear, and the basin count
  is recovered at sufficiently large time.
- Negative coefficient upper limit: interpreted as zero, exactly matching
  failure of the image inequality.

No finite enumeration is used in these proofs.
