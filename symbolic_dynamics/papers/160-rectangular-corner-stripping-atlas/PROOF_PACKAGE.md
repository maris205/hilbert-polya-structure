# Proof package — P160 RCS Round 2

## Claim and status

Prove the temporal, arbitrary-target, and identifiability statements in
`main.tex` for positive `a,b` and nonnegative `t,N`.

**Status:** `ANONYMOUS ROUND-2 / INTERNAL ACCEPT / HOLD_EXTERNAL`

Review B independently accepted the proof with `0 Critical / 0 Major /
0 Minor`. Its 11,287,366-assertion control is evidence pressure, not a proof
premise. Round 2 changes no mathematical text; the only manuscript addition is
the visible `HOLD_EXTERNAL` lifecycle sentence.

## Assumptions

Partitions are finite weakly decreasing positive sequences, with the empty
partition allowed and missing parts set to zero. Cells are `(i,j)` with
`1<=j<=lambda_i`. Put `h=at,w=bt`; all series are formal.

## Dependency map

```text
literal fixed crop -> coordinate induction -> all iterates
  -> corner survival -> point clock and sharp cap height
  -> empty condition -> disjoint hook slices
  -> arbitrary prescribed nonempty target -> forced-core inverse bijection
     -> exact fibres -> valid one-part excess witness -> cap support
     -> three target thresholds -> ordered recovery.
```

## Proof

### 1. Iterates and clock

One update retains exactly original cells with `i>a,j>b` and sends them to
`(i-a,j-b)`. Induction yields

```text
T_(a,b)^t(lambda)=(lambda_(at+1)-bt,lambda_(at+2)-bt,...)_+.
```

The iterate is nonempty exactly when cell `(at+1,bt+1)` exists. Every
nonempty state loses `(1,1)`, so empty is the unique recurrent state. Survival
through rank `t` forces an `(at+1)×(bt+1)` rectangle, and that rectangle is a
witness whenever its area is at most `N`. Hence

```text
H_(a,b)(N)=min{t>=0:(at+1)(bt+1)>N},
```

including `H_(a,b)(0)=0`.

### 2. Empty target

`T^t(lambda)=empty` iff `lambda_(h+1)<=w`. Slice by
`k=lambda_(h+1)`. The `k=0` slice has series `1/(q;q)_h`. For `1<=k<=w`,
remove a `k×(h+1)` rectangle; the first-`h` excess and lower remainder have
series `1/(q;q)_h` and `1/(q;q)_k`. The disjoint reversible sum is

```text
E_(h,w)(q)=1/(q;q)_h sum_(k=0)^w q^(k(h+1))/(q;q)_k.
```

### 3. Arbitrary nonempty target

Fix `mu=(mu_1,...,mu_r)`. A source maps to it exactly when

```text
lambda_(h+j)=mu_j+w (1<=j<=r),  lambda_(h+r+1)<=w.
```

The first `h` rows have baseline `mu_1+w`; their excess is a partition
`gamma` with at most `h` parts. The lower rows form a partition `beta` with
largest part at most `w`. Padding `gamma`, inserting the forced middle rows,
and appending `beta` is a reversible construction; both joins are weakly
decreasing. Its forced weight is

```text
M_(h,w)(mu)=|mu|+h(mu_1+w)+wr,
```

and the exact fibre series is

```text
q^M/((q;q)_h(q;q)_w).
```

At `t=0`, `h=w=0` and the sole source is `mu`. The empty target is never
substituted into this formula.

### 4. Exact cap support — repaired witness

Let `t>=1`, so `h,w>=1`. For every desired excess `d>=0`, take

```text
gamma=(d), beta=empty                   if d>0,
gamma=empty, beta=empty                 if d=0.
```

For `d>0`, `gamma` has exactly one part, hence at most `h` parts. Its weight is
`d`; therefore the fibre has a source at every exact weight `M+d`, and no
source below `M`. This proves the iff cap threshold. The alternative witness
`beta=(1^d)` is also valid because its largest part is at most `w`, but is not
needed. The invalid Round-0 phrase “put arbitrarily many unit parts in
gamma” is expressly withdrawn: it can violate `length(gamma)<=h`.

### 5. Duality and ordered recovery

Conjugation swaps coordinates and gives
`T_(a,b)(lambda)'=T_(b,a)(lambda')`. At one step,

```text
m((1))=(a+1)(b+1),
m((2))=m((1))+a+1,
m((1,1))=m((1))+b+1.
```

The two differences recover the ordered pair.

## Proof and source boundaries

The proof does not depend on enumeration. Generalized/rational-slope Durfee
rectangles, static two-boundary symbols/decompositions, their area-plus-weight
identity, and two-Pochhammer factorization are classical zero-credit inputs.
The residual starts only with fixed-crop all-time dynamics, arbitrary target,
separate empty branch, exact cap support, and ordered recovery. Direct-owner
risk remains bibliographic and is the reason for `HOLD_EXTERNAL`.
