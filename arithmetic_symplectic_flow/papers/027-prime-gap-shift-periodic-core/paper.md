# The consecutive-prime gap shift has no periodic accumulation point

**Paper ID:** `027-prime-gap-shift-periodic-core`  
**Record ID:** `ASFS-SCOUT-20260914-21`  
**Date / status:** `2026-09-14; PRE-P0 STOP — NO PERIODIC PRIME-GAP STATE`  
**Route state:** `No frozen candidate; Route A coordinates not evaluated; Route B NOT INVOKED`

## Lineage question

Set `g_n=p_(n+1)-p_n`, where `p_n` is the increasing prime sequence.  Unlike
the prime-indicator closure in 015, this word is precisely the natural
sequential parameter record that could be offered to a Logistic-type prototype
and then to a Hénon-type conservative lift:

```text
prime distribution -> gap word -> sequential deformation -> proposed geometric lift.
```

The screen asks whether its autonomous shift accumulation set first supplies a
nondegenerate periodic base state.

## Periodic-core theorem

Let `X_g` consist of all coordinatewise limits of shifts `sigma^(i_j)g` (and,
if a shift is repeated, its ordinary limit).  Then `X_g` has no periodic point.

Suppose that `x in X_g` has period `q>0`, and put
`D=x_0+...+x_(q-1)>0`.  Choose a prime `ell` not dividing `D`.  Take shifts
starting at `p_(i_j)` that converge to `x`.  If the indices are unbounded, pass
to a subsequence with `p_(i_j)=c (mod ell)`.  Choose `m>=0` with
`c+mD=0 (mod ell)` and, if needed, add multiples of `ell` so that
`p_(i_j)+mD>ell` for all sufficiently large `j`.

Convergence to the periodic word says that, for these sufficiently large `j`,
the sum of the first `mq` gap coordinates equals `mD`.  Hence
`p_(i_j)+mD` is the prime reached after `mq` successive gaps.  It is also a
multiple of `ell` larger than `ell`, a contradiction.  If the sequence of
starting indices is bounded, pass instead to a constant start and make the
same choice of `m`; the identical contradiction follows.  Therefore no such
periodic `x` exists.

## Gate consequence

This eliminates the most direct autonomous hull of the sequential prime-gap
parameter source as an A1 carrier.  It does not deny the gap word's arithmetic
lineage.  It says that a symplectic skew product over this exact base cannot
have a periodic total point, because any such point projects to a periodic base
point.  No `M`, `omega`, `F`, roof, suspension, primitive convention,
operator, or determinant is defined here, so P0 and A2 remain unavailable.

**Portfolio decision: fork.** Preserve the gap word as a source control, but
do not seek periodic-orbit calculations for a faithful skew product over its
shift hull.  A future candidate needs another recurrent arithmetic carrier
whose periodic states retain—not merely approximate—the prime-gap mechanism.

## Evidence index

- [Scope card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Evidence notes](evidence/README.md)
