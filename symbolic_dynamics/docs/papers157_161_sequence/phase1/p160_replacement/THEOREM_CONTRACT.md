# RCS theorem contract

**Handle:** `RCS` — rectangular-corner stripping  
**Status:** `SELECT_REPLACEMENT_P160 / ROUND1 REVIEW A REPAIRED / HOLD_EXTERNAL`  
**Proof status:** `PROVABLE AS STATED`

## Literal system

Let `P` be the set of integer partitions, including the empty partition.  Fix
positive integers `a,b`.  In the Ferrers diagram of `lambda`, delete the first
`a` rows and first `b` columns, retain their southeast complement, and translate
that complement to the northwest corner.  In parts,

```text
T_(a,b)(lambda)=(lambda_(a+1)-b,lambda_(a+2)-b,... )_+,
```

where nonpositive entries are omitted.  The finite paper carrier is
`P_(<=N)`, all partitions of weight at most `N`; the map is closed because
weight never increases.

Write `(q;q)_m=product_(j=1)^m(1-q^j)`, with `(q;q)_0=1`, and extend a
partition by zero parts.  Let `ell(mu)` and `mu_1` denote length and largest
part, with these statistics used only for nonempty `mu`.

## Contract A — all iterates, clock, height, and shells

For every `t>=0`, put `h=at` and `w=bt`.  Then

```text
T_(a,b)^t(lambda)=(lambda_(h+1)-w,lambda_(h+2)-w,...)_+.
```

Consequently

```text
tau_(a,b)(lambda)=min{t>=0: lambda_(at+1)<=bt},
tau>t iff (at+1,bt+1) is a cell of lambda,
H_(a,b)(N)=min{t>=0:(at+1)(bt+1)>N}.
```

Here `tau` is the first rank equal to the empty partition and `H` is the
maximum over `P_(<=N)`.  The empty partition is the unique recurrent state.

Define

```text
E_(h,w)(q)=1/(q;q)_h sum_(k=0)^w q^(k(h+1))/(q;q)_k.
```

The exact weight-refined absorption census is

```text
sum_(lambda:T^t(lambda)=empty) q^|lambda|=E_(at,bt)(q).
```

Thus `[q^n]E_(at,bt)` counts the partitions of weight `n` absorbed by rank
`t`, and `[q^n](E_(at,bt)-E_(a(t-1),b(t-1)))` is the exact rank-`t` shell for
`t>=1`.

## Contract B — every time, every target

For nonempty `mu`, define

```text
M_(h,w)(mu)=|mu|+h(mu_1+w)+w ell(mu).
```

Then for every `t>=0`, with `h=at,w=bt`,

```text
sum_(lambda:T^t(lambda)=mu) q^|lambda|
 = q^M_(h,w)(mu) / ((q;q)_h (q;q)_w),       mu nonempty,
 = E_(h,w)(q),                               mu empty.
```

For `t>=1`, a nonempty target belongs to the rank-`t` image of
`P_(<=N)` exactly when `M_(at,bt)(mu)<=N`; it then has a source of every
weight from its threshold through `N`.  The coefficient of the displayed
series is the exact size-refined fibre.

## Contract C — duality and identifiability

Ferrers conjugation exchanges the parameters:

```text
T_(a,b)(lambda)'=T_(b,a)(lambda').
```

Let `m(mu)` be the minimum source weight of the one-step nonempty target
`mu`.  The three thresholds

```text
m((1))       =(a+1)(b+1),
m((2))       =m((1))+a+1,
m((1,1))     =m((1))+b+1
```

recover the ordered parameter pair:

```text
a=m((2))-m((1))-1,
b=m((1,1))-m((1))-1.
```

## Mandatory boundaries

- `N=0`, `t=0`, the empty partition, and `(q;q)_0=1` are explicit.
- Contract B's nonempty formula is not applied to `mu=empty`.
- The image-threshold equivalence is stated for `t>=1`; at `t=0` the fibre
  is the singleton source `mu` at its exact weight.
- Conjugation swaps `a,b`; it does not identify the ordered pair when row and
  column targets remain distinguished.

## Zero-credit inputs and claim ceiling

Barnes--Savage directly use deletion of the first row and first column and
state the Durfee decrement. Gordon--Houten and Andrews (1971) place
generalized rectangular, including unequal/rational-slope, Durfee viewpoints
in the classical record. Chen--Ji--Zang give a static `m`-Durfee rectangle
symbol with right/below boundary partitions and area-plus-boundary weight
decomposition. Andrews--Eriksson supply standard Ferrers and bounded-product
background. All those facts, every static two-boundary decomposition, and the
two-Pochhammer factorization are zero-credit inputs.

The claim residual begins only with the fixed `(a,b)` literal crop iterated
through every time, arbitrary prescribed targets, a separate empty branch,
exact cap support, and ordered recovery. For exact support the mandatory
witness is `gamma=(d), beta=empty` for `d>0`, with both empty for `d=0`;
`gamma=(1^d)` is forbidden because its length need not be at most `h`. The
manuscript may not say `new`, `first`, `novel`, or infer owner absence from the
bounded search.
