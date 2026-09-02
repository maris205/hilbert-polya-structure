# Derivation Package

## Target

Derive a complete temporal and inverse atlas for rectangular-corner stripping
on integer partitions, uniformly in positive `a,b`, time `t`, target `mu`, and
weight cap `N`.

## Status

`COHERENT AS STATED / ROUND1 REVIEW A REPAIRED`.

## Invariant Object

The invariant object is the southeast Ferrers subdiagram.  One update shifts
the retained cell `(i,j)` to `(i-a,j-b)`; iteration therefore adds the row and
column offsets rather than creating a new local configuration.

## Assumptions

- `a,b` are positive integers.
- Partitions are finite weakly decreasing sequences of positive integers; the
  empty sequence is admitted.
- Weight is the number of Ferrers cells.
- Formal power series are coefficientwise; no analytic convergence is used.

## Notation

- `T=T_(a,b)` is rectangular-corner stripping.
- `h=at`, `w=bt` are the accumulated row and column offsets.
- `tau(lambda)` is the least `t` with `T^t(lambda)=empty`.
- `(q;q)_r=product_(j=1)^r(1-q^j)`.
- `M_(h,w)(mu)=|mu|+h(mu_1+w)+w ell(mu)` for nonempty `mu`.

## Derivation Strategy

First follow individual cells to obtain all iterates and the clock.  Then run
the same cell picture backward from a fixed target.  A source decomposes into
a forced core, a freely varying top excess partition, and a freely varying
bottom partition.  The last two pieces yield independent Pochhammer factors.

## Derivation Map

1. Coordinate translation gives the iterate identity.
2. Nonemptiness becomes membership of one southeast corner cell, yielding the
   pointwise clock and the sharp capped height.
3. Empty-target sources are Ferrers diagrams inside an `(h,w)` hook; slicing
   by row `h+1` gives their series.
4. A nonempty target forces `h` top rows and `ell(mu)` middle rows; the two
   remaining free boundary partitions factor.
5. The valid one-part witness `gamma=(d)` gives every excess past the forced
   weight and hence the exact capped image criterion.
6. Three small target thresholds solve for `a,b`.

## Main Derivation

### 1. Forward coordinates

A cell survives one step exactly when its row exceeds `a` and its column
exceeds `b`.  A surviving cell is translated by `(-a,-b)`.  After `t` steps,
the original survivors are exactly the cells southeast of `(at,bt)`, which
gives

```text
T^t(lambda)_j=max(lambda_(at+j)-bt,0).
```

The result is nonempty precisely when `lambda_(at+1)>=bt+1`.

### 2. Sharp clock

Survival past time `t` requires the entire rectangle
`[1,at+1] x [1,bt+1]`, hence at least `(at+1)(bt+1)` cells.  This proves the
upper bound on `P_(<=N)`.  The rectangle partition
`(bt+1)^(at+1)` attains the boundary whenever its area is at most `N`, proving
sharpness.

### 3. Empty-target series

The condition `T^t(lambda)=empty` is `lambda_(h+1)<=w`.  Slice by
`k=lambda_(h+1)`.

- For `k=0`, there are at most `h` rows, with series `1/(q;q)_h`.
- For `1<=k<=w`, remove a rectangle of width `k` and height `h+1`.
  The excess in the first `h` rows is an arbitrary partition with at most
  `h` parts; the remaining lower rows form a partition with largest part at
  most `k`.  Their series is
  `q^(k(h+1))/((q;q)_h(q;q)_k)`.

Summing gives `E_(h,w)`.

### 4. Nonempty target series

Fix nonempty `mu`.  A source mapping to `mu` has middle rows

```text
lambda_(h+j)=mu_j+w,  1<=j<=ell(mu).
```

The first `h` rows have baseline `mu_1+w`; their excesses are an arbitrary
partition `gamma` with at most `h` parts.  Rows below the displayed middle
block have length at most `w`; they form an arbitrary partition `beta` with
largest part at most `w`.  The forced weight is

```text
h(mu_1+w)+|mu|+w ell(mu)=M_(h,w)(mu).
```

The choices of `gamma` and `beta` are independent and have series
`1/(q;q)_h` and `1/(q;q)_w`.  Multiplication gives Contract B.

### 5. Image and identifiability

When `t>=1`, `h,w>=1`. For excess `d>0`, take `gamma=(d)` and
`beta=empty`; at `d=0` take both empty. The one-part `gamma` has length at
most `h`, so a target has a source at every weight at least `M`. (Equivalently,
`beta=(1^d)` is valid because its largest part is one.) The Round-0 witness
`gamma=(1^d)` is invalid in general and is not used. Substitution of `(1)`,
`(2)`, and `(1,1)` into `M` gives the three recovery equations.

## Remarks and Interpretation

The clock and inverse theorem use the same geometric offset but different
information.  The clock sees one southeast corner cell.  The inverse theorem
sees two independent boundaries around an arbitrary prescribed target.  The
ordered parameters are detectable because a row target stresses the deleted
row count while a column target stresses the deleted column count.

## Boundaries and Non-Claims

- Generalized/rational-slope Durfee rectangles, static two-boundary
  symbols/decompositions, the `a=b=1` decrement, and the two-Pochhammer
  factorization are not presented as contributions.
- The residual begins only at fixed-parameter all-time literal cropping,
  arbitrary targets, separate empty branch, exact cap support, and recovery.
- The derivation is formal and enumerative; it makes no asymptotic claim.
- Exact computation tests coefficients only and is not part of the proof.
- The source search is bounded and supports no novelty or ownership claim.

## Open Risks

The main remaining risk is bibliographic rather than mathematical: a source
may formulate the same two-parameter target-resolved atlas in different hook-
partition language.  The manuscript therefore uses explicit subtraction and
an external hold.
