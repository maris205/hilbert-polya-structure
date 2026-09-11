# LFAS reserve contract: least alternating-rectangle switch

**Disposition:** `RESERVE_AMBER / NOT SELECTED / HOLD_EXTERNAL`.

This is the strongest independent non-Kempe signal in this replacement lane,
but it is not promotion-grade: the exact sharp maximum tail and a closed
fibre extremum have not been proved.  The contract below records only the
claims that are already rigorous.

## Literal map

Fix `r,s>=2`.  A state is a binary `r x s` matrix.  Order rectangles
`(i,k,j,l)`, with `i<k` and `j<l`, lexicographically.  A rectangle is
alternating when its four entries are

```text
1 0        0 1
0 1   or   1 0.
```

If no alternating rectangle exists, hold.  Otherwise complement all four
entries in the least alternating rectangle.  Equivalently, reverse the least
directed four-cycle in the corresponding bipartite tournament.

## Closed theorem surface

Let `R=binom(r,2)binom(s,2)` and let `sigma(A)` be the index of the least
alternating rectangle, with infinity for a fixed matrix.

1. Every update preserves every row sum and column sum.
2. The switched rectangle remains alternating, while no earlier rectangle
   existed before the switch.  Hence
   `sigma(F(A))<=sigma(A)`.  If equality holds, the next step returns to
   `A`; otherwise the selector strictly descends.
3. Every periodic orbit is a fixed point or a strict two-cycle.  Every
   transient tail has length at most `R-1`.
4. Fixed points are precisely lonesum matrices, equivalently matrices with no
   `2 x 2` permutation submatrix.  Their number is

   ```text
   L(r,s)=sum_{k=0}^{min(r,s)} (k!)^2 S(r+1,k+1)S(s+1,k+1).
   ```

5. For a target `Y`, let `Alt(Y)` be its alternating rectangles and let
   `flip_Q(Y)` complement rectangle `Q`.  The complete one-step inverse atlas
   is

   ```text
   |F^{-1}(Y)|
     = 1{Alt(Y)=empty}
       + #{Q in Alt(Y): sigma(flip_Q(Y))=Q}.              (1)
   ```

Equation (1) is an iff statement: a nonfixed source identifies its scheduled
rectangle uniquely, and rectangle flipping is involutive.

## Why this remains reserve

The switch itself is the standard margin-preserving binary-matrix
`2`-switch, and fixed lonesum enumeration is classical; both receive zero
credit.  The least-defect scheduler yields a real finite functional graph and
nonuniform target atlas, but its current clock bound is selector-counting,
not a sharp structural theorem.  Exact pilots through `4 x 4` show maximum
tails `0,1,2,3,4` on the boxes `2x2,2x4,3x3,3x4,4x4`, but these data are not
promoted to an all-parameter formula.  No paper slot or novelty claim is
permitted from this reserve contract.

