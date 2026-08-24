# C135 theorem package

## Definition 1: edge-roof suspension

Let `Sigma` be the two-sided full binary shift and set

```text
tau = [[1,sqrt(2)],[sqrt(3),sqrt(6)]].
```

The roof is `tau(x)=tau_(x0,x1)`, and

```text
X^tau=(Sigma x R)/((x,t+tau(x))~(sigma(x),t)).
```

For formal edge variables define

```text
M(x)=[[x00,x01],[x10,x11]].
```

## Theorem 1: exact determinant and all-period primitive product

Direct calculation gives

```text
Delta(x)=det(I-M(x))
        =1-x00-x11+x00*x11-x01*x10.
```

For every `n>=1`,

```text
Tr(M(x)^n)=sum_(rooted closed words w, |w|=n)
 x00^N00(w) x01^N01(w) x10^N10(w) x11^N11(w).
```

Hence, in the total-edge-degree completion,

```text
Delta(x)=product_[gamma primitive]
 (1-x00^N00(gamma)x01^N01(gamma)
    x10^N10(gamma)x11^N11(gamma)).
```

The proof expands `-log det(I-M)=sum_n Tr(M^n)/n` and groups rooted words by
their unique primitive root and repetition.

## Theorem 2: nonlattice specialization

Under

```text
x00=exp(-s), x01=exp(-sqrt(2)s),
x10=exp(-sqrt(3)s), x11=exp(-sqrt(6)s),
```

one obtains

```text
d_tau(s)=1-exp(-s)-exp(-sqrt(6)s)
 +exp(-(1+sqrt(6))s)-exp(-(sqrt(2)+sqrt(3))s).
```

For a primitive orbit,

```text
ell=N00+sqrt(2)N01+sqrt(3)N10+sqrt(6)N11,
d_tau(s)=product_[gamma](1-exp(-s ell(gamma))).
```

If `h>0` is the unique solution of `spectral_radius(M_tau(h))=1`, the trace
and primitive expansions converge absolutely for `Re(s)>h`.  The explicit
left side is entire, and its reciprocal is meromorphic.  The fixed cycles
`[0]` and `[1]` have lengths `1` and `sqrt(6)`, proving the roof is nonlattice.

## Theorem 3: edge-sector separation

The four numbers `1,sqrt(2),sqrt(3),sqrt(6)` are the rational basis of
`Q(sqrt(2),sqrt(3))`.  Equality of two roof times therefore forces equality
of their complete directed-edge-count vectors.

For `000111`,

```text
N=(2,1,1,2),
ell=2+sqrt(2)+sqrt(3)+2sqrt(6).
```

For `001011`,

```text
N=(1,2,2,1),
ell=1+2sqrt(2)+2sqrt(3)+sqrt(6).
```

Their difference is

```text
1-sqrt(2)-sqrt(3)+sqrt(6) != 0.
```

Thus the C130 symbol-count collision is separated.  In `Tr(M^6)`, the two
sectors have exact rooted multiplicities `6` and `12`.

## Theorem 4: remaining collision and orientation obstruction

The words `001011` and `001101` are primitive and not cyclic rotations, but
both have edge vector `(1,2,2,1)`.  Their roof times agree exactly.  They are
the first same-edge-count primitive collision, at period six.

Every closed binary word satisfies `N01=N10`: each crossing from state zero
to state one must be balanced by a crossing back.  Consequently every
periodic trace and determinant coefficient depends on the off-diagonal roof
only through `tau01+tau10`.  The antisymmetric component `tau01-tau10` is
invisible to all periodic data.

## Progress and strict boundary

C130 separated symbol-population sectors but left `000111` and `001011`
aggregated.  C135 separates every distinct admissible edge-count vector and
the displayed pair.  It does not separate primitive orbits inside one vector
or recover off-diagonal orientation.  No target, arithmetic, global analytic,
or natural-lift claim is made.  The strict tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` and Route B is unauthorized.
