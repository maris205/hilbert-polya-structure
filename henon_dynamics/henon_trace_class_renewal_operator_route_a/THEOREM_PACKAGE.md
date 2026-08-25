# Theorem package

## Target

Derive and prove the all-order Fredholm determinant of the frozen countable
renewal operator, then separate this source-owned determinant from a formal
renewal identity whose natural operator is not compact.

## Status

`PROVABLE AS STATED` and `COHERENT AS STATED`.

## Invariant object

The invariant object throughout is the single bounded operator

```text
T=S+R on H=l2(N0),
S e_n=b_n e_{n+1},  R e_n=a_n e_0,
a_n=b_n=2^{-(n+1)}.
```

No finite matrix, scalar renewal function, or primitive ledger silently
replaces `T`.

## Assumptions and notation

- `e_n` is the standard orthonormal basis of `H`.
- `c_m=a_{m-1} product_{j=0}^{m-2} b_j` is the weight of the unique
  first-return excursion of clock `m`.
- `D(z)=det_F(I-zT)` uses the ordinary trace-class determinant.
- A primitive renewal orbit is a primitive cyclic necklace of positive
  excursion lengths.

## Dependency map

1. Summability of `b_n` and square summability of `a_n` imply trace class.
2. The shift is quasinilpotent with determinant one.
3. Factoring `I-zT` through `I-zS` reduces the determinant to rank one.
4. The dyadic normalization turns the first-return weights into triangular
   exponents.
5. The Fredholm logarithm and the unique excursion decomposition give the
   primitive product.
6. A constant-weight shift supplies the ownership obstruction.

## Theorem 1: trace class and exact determinant

The operator `T` is trace class and

```text
||T||_1 <= 1+1/sqrt(3).
```

For every complex `z`,

```text
det_F(I-zT)=1-sum_{m>=1}2^{-m(m+1)/2}z^m.
```

The right-hand side is entire of order zero.

### Proof

The weighted shift has singular values `b_n`, hence
`||S||_1=sum b_n=1`.  The return operator is
`R=|e_0><a|`, so it has rank one and trace norm
`||a||_2=(sum 4^{-(n+1)})^{1/2}=1/sqrt(3)`.

Every power of `S` has zero diagonal and `S` is quasinilpotent; consequently
`det_F(I-zS)=1` and `I-zS` is invertible for every `z`.  The rank-one
determinant identity gives

```text
det_F(I-zT)
 = 1-z<a,(I-zS)^{-1}e_0>
 = 1-sum_{m>=1} a_{m-1} product_{j=0}^{m-2}b_j z^m.
```

The exponent is
`m+(1+...+(m-1))=m(m+1)/2`.  Finally, for coefficients `d_m` of the
nonconstant part,

```text
limsup m log(m) / log(1/|d_m|)=0,
```

which is the coefficient characterization of entire order zero.  This
proves the theorem.

## Theorem 2: primitive renewal product

For `|z|<(1+1/sqrt(3))^{-1}`,

```text
D(z)=product_[p] (1-w_p z^{ell_p}),
```

where `[p]` ranges over primitive cyclic necklaces of positive excursion
lengths, `ell_p` is their total edge clock, and `w_p` is the product of their
first-return weights.

### Proof

Every closed path hits vertex zero: a path that used only advance edges
could never close.  Cutting at successive visits to zero therefore gives a
unique cyclic sequence of first-return excursions.  Rooted closed paths are
obtained from a primitive necklace and a repetition number.  Since `T` is
trace class,

```text
-log D(z)=sum_{n>=1} Tr(T^n)z^n/n
```

converges absolutely when `|z| ||T||_1<1`.  Regrouping the nonnegative
closed-path weights by primitive necklace and repetition gives
`sum_[p] sum_{r>=1} w_p^r z^{r ell_p}/r`, which is the negative logarithm of
the stated product.  Absolute convergence justifies the regrouping.

## Proposition 3: exact finite sections

Let `T_N` be the compression to `span(e_0,...,e_{N-1})`.  Then

```text
det(I-zT_N)=1-sum_{m=1}^N 2^{-m(m+1)/2}z^m,
```

and `Tr(T_N^n)=Tr(T^n)` for every `n<=N`.  A length-`n` closed path cannot
visit a vertex with index at least `n`, so the trace assertion follows; the
determinant follows from the same finite rank-one factorization.

## Proposition 4: formal renewal does not imply Fredholm ownership

Keep `a_n=2^{-(n+1)}` but set every advance weight to `1/2`.  The formal
first-return coefficients are `2^{-(2m-1)}` and the formal scalar expression
is

```text
1-sum_{m>=1}2^{-(2m-1)}z^m=(1-3z/4)/(1-z/4).
```

The weighted shift now has the singular value `1/2` with infinite
multiplicity and is noncompact.  Adding the rank-one return cannot make it
compact.  Thus the natural control operator is not trace class and does not
own an ordinary Fredholm determinant, even though its formal renewal algebra
is elementary.

## Boundaries and nonclaims

The theorem proves a source-native, infinite-rank determinant and primitive
product.  It does not identify any target divisor, target functional
equation, target counting law, prime correspondence, arithmetic local data,
Euler factor, root number, automorphy object, or Hilbert--Polya operator.
Route B remains unauthorized.

## Open risks

- The renewal clock is intrinsic but has no prime-like semantics.
- Entire order zero is a source analytic property, not target analytic
  structure under Route-A layer A3.
- Alternative countable weights require a fresh compactness and determinant
  audit; the theorem is not a classification of all renewal systems.
