# Narrative report — P157

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## One-sentence result

After treating the idempotent-lifting cubic and its quadratic error
improvement as zero-credit prior material, the residual result is a complete
temporal and one-step inverse atlas modulo `2^n`: exact temporal shells plus a
normalized-unit image classification and every-target nonuniform fibre law.

## What the dynamics does

For `F_n(x)=3x^2-2x^3 mod 2^n`, parity is preserved.  At an even state the
selected endpoint error is `x`; at an odd state it is `1-x`.  The two exact
factorizations make the selected error valuation double at every step.  This
immediately gives the pointwise time to `0` or `1`, all temporal shells, and
the sharp height `ceil(log_2 n)`.

That forward coordinate is insufficient for inversion.  Writing an even
source as `x=2^v w` leaves

~~~text
F_n(x)=2^(2v) h_v(w),
h_v(w)=w^2(3-2^(v+1)w).
~~~

The output valuation is `2v`, but its normalized odd unit has a further
restriction.  For quotient size `N=n-2v`, it is the only odd class for `N=1`,
`3 mod 4` for `N=2`, and for `N>=3` it is `7 mod 8` at `v=1` but `3 mod 8`
at every later stratum.  Splitting inputs into the two odd branches modulo
four and using an exact cubic difference proves four reduced predecessors for
`N>=3`; restoring forgotten high bits yields the full fibre formula.

## Prior-art boundary

Burban and Drozd explicitly give the same polynomial in Lemma A.4 of their
2004 *Journal of Algebra* paper while presenting the construction as known
and pointing to classical background.  Their paper is therefore a direct
prior/foundation record, not an attribution of origination.  The cubic, its
purpose, error factorizations, and quadratic improvement receive zero credit.
The paper retains only the temporal and one-step inverse residue-class atlas.
A bounded non-hit for that atlas is not a novelty, priority, or release claim.

## Evidence and limits

The symbolic proof closes the theorem for every `n>=1`, including `N=1,2`.
The paper-local exact falsifier checks all states and targets through `n=17`
and the normalized unit maps for `v=1..6`, `N=1..11`.  Its 2,563,880
assertions end in PASS; transcript SHA-256 is
`f5f1884f809110ca8ec3a954af1783c774896708495d626f694bbfb23f7876f1`.

No odd-prime, general-ring, novelty, priority, or external-release statement
is made.
