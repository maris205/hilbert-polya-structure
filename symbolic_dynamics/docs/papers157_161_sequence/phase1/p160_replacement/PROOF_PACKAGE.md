# Proof Package

## Claim

Contracts A--C in `THEOREM_CONTRACT.md`: all iterates and sharp height,
weight-refined clock shells, every-time/every-target fibre series and image
thresholds, conjugation duality, and recovery of `(a,b)`.

## Status

`PROVABLE AS STATED / ROUND1 REVIEW A REPAIRED`.

## Assumptions

`a,b` are positive integers; `t,N` are nonnegative integers; partitions may be
empty; all generating functions are formal.

## Notation

Use the notation fixed in `THEOREM_CONTRACT.md`.  A cell of `lambda` is a pair
`(i,j)` with `1<=j<=lambda_i`.

## Proof Strategy

Track original cell coordinates forward.  For inverse fibres, construct a
bijection between sources and ordered pairs of bounded partitions.  Treat the
empty target separately by a disjoint slice on `lambda_(h+1)`.

## Dependency Map

1. The iterate formula depends only on coordinate translation.
2. Clock and height depend on the iterate formula and a rectangle-area bound.
3. Empty-target census depends on a disjoint boundary-row decomposition.
4. Nonempty fibres depend on a bijective three-region decomposition.
5. Image and recovery depend algebraically on the fibre formula.
6. Conjugation follows by transposing cell coordinates.

## Proof

### Step 1: iterates

One update retains precisely the original cells `(i,j)` with `i>a` and
`j>b`, and sends each to `(i-a,j-b)`.  Suppose after `t` updates a cell
survives precisely when `i>at,j>bt` and then occupies `(i-at,j-bt)`.
Applying one more update imposes `i-at>a,j-bt>b`, equivalently
`i>a(t+1),j>b(t+1)`, and subtracts one further `(a,b)`.  Induction proves the
cell statement for every `t>=0`.  Reading row lengths gives

```text
T^t(lambda)=(lambda_(at+1)-bt,lambda_(at+2)-bt,...)_+.
```

### Step 2: clock, recurrence, and height

The displayed partition is nonempty exactly when
`lambda_(at+1)>=bt+1`.  This proves the pointwise formula for `tau` and the
corner-cell criterion.  Every nonempty partition loses its cell `(1,1)` in
one update, so its weight strictly decreases; hence the empty partition is the
unique recurrent state.

If a partition survives rank `t`, weak decrease of its rows forces it to
contain the rectangle of height `at+1` and width `bt+1`, of area
`(at+1)(bt+1)`.  No partition of weight at most `N` survives once this area
exceeds `N`.  Conversely, whenever the area is at most `N`, that rectangle
itself is a state of `P_(<=N)` surviving rank `t`.  Therefore

```text
H_(a,b)(N)=min{t>=0:(at+1)(bt+1)>N}.
```

For `N=0`, the minimum is `t=0`, so the formula includes the empty carrier.

### Step 3: the empty fibre

Put `h=at,w=bt`.  By Step 1, `T^t(lambda)=empty` if and only if
`lambda_(h+1)<=w`.  Partition this set by `k=lambda_(h+1)`.

If `k=0`, `lambda` has at most `h` parts, whose generating function is
`1/(q;q)_h`.  If `1<=k<=w`, remove `k` cells from each of the first `h+1`
rows.  Since row `h+1` had exactly length `k`, the residual of the first `h`
rows is an arbitrary partition with at most `h` parts.  The rows below row
`h+1` form an arbitrary partition with largest part at most `k`.  This
operation is reversible and changes weight by `k(h+1)`.  Hence the slice has
series

```text
q^(k(h+1))/((q;q)_h(q;q)_k).
```

The slices are disjoint and exhaustive, so their sum is `E_(h,w)`.  Taking
coefficients proves the absorbed census; subtracting the rank-`t-1` absorbed
set from the rank-`t` absorbed set proves the shell formula.

### Step 4: a bijection for every nonempty target

Fix nonempty `mu` of length `r`.  Step 1 shows that a source maps to `mu` if
and only if

```text
lambda_(h+j)=mu_j+w  for 1<=j<=r,
lambda_(h+r+1)<=w.
```

The first `h` rows must be at least `mu_1+w`.  Define

```text
gamma_i=lambda_i-(mu_1+w), 1<=i<=h,
beta=(lambda_(h+r+1),lambda_(h+r+2),...).
```

After trailing zeros are omitted, `gamma` is an arbitrary partition with at
most `h` parts and `beta` is an arbitrary partition with largest part at most
`w`.  Conversely, any such pair reconstructs a unique source by placing
`mu_j+w` in the middle, adding `mu_1+w` to the `h` padded parts of `gamma`,
and appending `beta`.  Weak decrease holds at both joins because
`gamma_h>=0`, `mu_1>=mu_j`, `mu_r>=1`, and every part of `beta` is at most
`w`.  Thus this is a bijection.

The forced cells have weight

```text
M_(h,w)(mu)=|mu|+h(mu_1+w)+wr.
```

The two free partition series are `1/(q;q)_h` and `1/(q;q)_w`; multiplying
them and the forced monomial proves the nonempty fibre formula.  This proof
also covers `t=0`, when `h=w=0` and the sole source is `mu`.

### Step 5: image threshold

For `t>=1`, `h,w>=1`. For excess `d>0`, set `gamma=(d)` and leave
`beta` empty; for `d=0`, leave both empty. This `gamma` has one part and hence
at most `h` parts. Consequently the coefficient of every degree at least
`M_(h,w)(mu)` is positive, and every smaller coefficient is zero because `M`
is forced. (`beta=(1^d)` would also work because its largest part is at most
`w`.) The former phrase using `gamma=(1^d)` is invalid when `d>h` and is
withdrawn. Intersecting with `P_(<=N)` gives the iff image criterion. The
empty target always has the empty source.

### Step 6: duality and parameter recovery

Ferrers conjugation sends cell `(i,j)` to `(j,i)`.  The survival inequalities
`i>a,j>b` become `j>b,i>a`; translation commutes with this swap.  Hence
`T_(a,b)(lambda)'=T_(b,a)(lambda')`.

At one step, substitute the three indicated targets into `M_(a,b)`:

```text
m((1))=1+a(1+b)+b=(a+1)(b+1),
m((2))=2+a(2+b)+b=m((1))+a+1,
m((1,1))=2+a(1+b)+2b=m((1))+b+1.
```

Solving the last two differences proves recovery of the ordered pair.  This
completes Contracts A--C.  QED.

## Corrections or Missing Assumptions

Round-1 repairs the support witness; no theorem statement changes.

## Open Risks

No mathematical gap remains in the repaired contract. Generalized/rational-
slope rectangles, static two-boundary symbols/decompositions, and the
two-Pochhammer factorization are zero credit. Direct-owner risk is handled in
`OWNER_SEARCH_LOG.md` and remains the reason for `HOLD_EXTERNAL`.
