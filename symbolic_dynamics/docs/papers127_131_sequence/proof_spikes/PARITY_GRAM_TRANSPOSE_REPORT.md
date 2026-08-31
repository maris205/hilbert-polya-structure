# Proof spike: binary parity--Gram transpose

**Candidate:** root X07.  **Status:** conditional promotion to the global
owner/value gate; no paper number frozen.  **External status:**
`HOLD_EXTERNAL`.

## Literal system

Let `1` denote the all-one column and work in `M_n(F_2)`.  For

```text
r(A) = A 1,
```

define

```text
Phi(A) = A^T + r(A) r(A)^T.
```

Thus the update is transpose followed by a rank-one correction determined by
the current row-parity vector.  The correction is recomputed at every step.

## Exact theorem contract supported by the spike

Write `r=A1`, `c=A^T1`, and `tau=1^T A 1`.

1. Every image has even total parity.  More precisely, the quotient update is
   `tau'=0`; if `tau=0`, then `(r,c)->(c,r)`, while if `tau=1`, then
   `(r,c)->(c+r,0)`.
2. The even-total hyperplane is the complete recurrent set.  Every odd-total
   matrix has exact entrance time one.
3. On the even hyperplane,
   `Phi^2(A)=A+rr^T+cc^T`, hence every period is in `{1,2,4}`.  Unequal margins
   give exact period four; equal margins give period one or two.
4. The image has `2^(n^2-1)` elements.  A target with nonzero column parity has
   one preimage; a target with zero column parity has `2^(n-1)+1` preimages.
   There are `2^(n(n-1))` targets of the second kind.
5. The component census is

   ```text
   fixed points = 2^(n(n-1)/2),
   2-cycles = (2^(n(n-1)) - 2^(n(n-1)/2))/2,
   4-cycles = (2^(n^2-1) - 2^(n(n-1)))/4,
   depth-one states = 2^(n^2-1).
   ```

   Consequently the finite Artin--Mazur zeta function follows immediately
   from the three cycle counts.

## Proof route

The row/column/total parity quotient proves the image and fourth-iterate law.
For a prescribed even-total target `B`, solving
`B=A^T+rr^T` gives the unique even preimage
`A=B^T+c(B)c(B)^T`.  Odd preimages exist exactly when `c(B)=0`, in which case
every odd-weight `r` supplies one.  Fixed points force `r=0` by comparing the
diagonal of `A+A^T=rr^T`; symmetric zero-row-sum matrices then form a space of
dimension `n(n-1)/2`.  Standard binary margin counting supplies the remaining
cycle counts.

## Exact evidence

`verify_parity_gram_transpose.py` exhausts every binary matrix through `n=4`.
It checks the quotient law, second/fourth iterate identities, exact entrance
times and periods, every feasible margin fibre, every one-step target fibre,
and all census formulas.  Its canonical run passes the assertion count stored
in `PARITY_GRAM_TRANSPOSE_CANONICAL.txt`.

## Owner and collision posture

Owner-direct searches on 2026-08-31 for the exact formula and its row-parity,
transpose, finite-field, and rank-one interfaces produced only generic
rank-one perturbation and transpose literature, not a literal-map match.  This
is a bounded non-hit, not a novelty conclusion.  Transpose, binary margin
counting, rank-one outer products, and finite functional-graph/zeta bookkeeping
receive zero contribution credit.

The closest internal risks are P102 (involution-norm language), P103 (a matrix
transpose/adjugate iterate), and P125 (a quadratic finite-state shear).  No
theorem transfers: X07 acts on all square binary matrices, falls onto one
parity hyperplane, and is classified by row/column margins.  Nevertheless the
immediate P125 quadratic-state silhouette requires a hostile collision gate
before any paper freeze.
