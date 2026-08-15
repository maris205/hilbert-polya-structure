# Paper 36 derivation package — SD-C38

## 1. Affine normal form and positive source

Fix `r>=2` and

```text
M_r=N_0 semidirect_r N_0,
(b,k)(d,l)=(b+r^k d,k+l),
u=(1,0), v=(0,1).
```

Then `vu=(r,1)=u^r v`, and every pair `(b,k)` is the unique normal form
`u^b v^k`. Right multiplication gives

```text
U(b,k)=(b+r^k,k),  V(b,k)=(b,k+1).
```

The function `b+k` increases on both positive generators. Thus the positive
right Cayley graph is acyclic. Recurrence only appears after adjoining formal
reverse arcs; that enlargement is kept explicit.

## 2. Hashimoto relation polygon

On the formal symmetrization, let `H_r` send an oriented edge to every
compatible successor except its formal reverse. The same exclusion is imposed
at the cyclic join. At `(0,0)`, the relation word traces

```text
(0,0) --v--> (0,1) --u--> (r,1)
      --bar(v)--> (r,0) --bar(u)^r--> (0,0).
```

No adjacent pair is an inverse pair, including the cyclic join. Since the word
contains exactly one `v` and one `bar(v)`, it cannot be a proper positive
temporal power. Hence it is a primitive cyclically nonbacktracking polygon of
length

```text
L_r=r+3.
```

The identical construction at each `x in M_r` is the translated relation
polygon `C_(r,x)`.

## 3. Cellular boundary

Attach at each vertex one cell comparing `vu` and `u^r v`. With the left
`ZM_r` action and edge-orbit basis `e_u,e_v`, the cellular modules are

```text
C_2 = ZM_r,
C_1 = (ZM_r)e_u direct-sum (ZM_r)e_v,
C_0 = ZM_r.
```

The first boundary is

```text
partial_1(e_u)=u-1,  partial_1(e_v)=v-1.
```

The path chains of the two sides are

```text
[vu]       = e_v + v e_u,
[u^r v]    = sum_(j=0)^(r-1) u^j e_u + u^r e_v.
```

Therefore

```text
partial_2(1)
 = (v-sum_(j=0)^(r-1)u^j)e_u + (1-u^r)e_v.
```

Direct substitution yields

```text
partial_1 partial_2(1)
 = v(u-1) - (sum u^j)(u-1) + (1-u^r)(v-1)
 = vu-u^r v
 = 0.
```

This is a cellular identity, not a claim about scalar path multiplicity.

## 4. Contractibility check

The affine realization is injective. If `x=x^m` for `m>=2` and `x=(b,k)`,
comparison of second coordinates gives `k=mk`, hence `k=0`; comparison of
first coordinates then gives `b=mb`, hence `b=0`. Thus the monoid is
torsion-free in the relevant one-relator sense.

The relation sides `vu` and `u^r v` have different first letters and different
last letters. Their longest common prefix-and-suffix is empty, so the
presentation is incompressible in the sense used by Gray and Steinberg.
Their one-relator monoid theorem therefore specializes to the ordinary Cayley
complex and makes `K_r` contractible. Consequently the augmented cellular
sequence

```text
0 -> ZM_r -> (ZM_r)^2 -> ZM_r -> Z -> 0
```

is exact, `pi_1(K_r)=0`, and `H_j(K_r;Z)=0` for `j>=1`.

## 5. Free-marker non-descent

Let an additive degree take values in a torsion-free abelian group and be
constant on the relation cell. Put `alpha=deg(u)` and `beta=deg(v)`. Then

```text
beta+alpha=r alpha+beta,
(r-1)alpha=0,
alpha=0.
```

The original unit marker requires `alpha=beta=1`, so it cannot descend for
`r>=2`. In formal-germ language, descent would require `z^2=z^(r+1)`.
Specializing `z`, assigning `deg(u)=0`, or inducing is a changed clock.

For `r=1`, both sides have length two and the marker obstruction disappears,
but the square-grid fill is still contractible. Clock homogeneity alone does
not retain recurrence.

## 6. Trace-class prequotient operator

For an oriented edge with origin `(b,k)`, set

```text
d_theta(e)=theta^(1+b+k),  0<theta<1,
T_(r,theta)=D_theta H_r D_theta.
```

Every vertex has at most four incident oriented edges; every Hashimoto row and
column has sum at most three. The Schur test gives `||H_r||<=3`. Moreover,

```text
Tr(D_theta)
 <= 4 sum_(b,k>=0) theta^(1+b+k)
 = 4 theta/(1-theta)^2 < infinity.
```

Thus `D_theta` is trace class. The trace ideal is two-sided, so
`T_(r,theta)` is trace class and owns an ordinary Fredholm determinant on the
full oriented-edge space. For `|z|<||T||^(-1)`, its trace-log is

```text
-log det(I-zT)=sum_(n>=1) z^n Tr(T^n)/n.
```

## 7. Positive relation coefficient

Along the based relation polygon, the origins have coordinate exponents

```text
1, 2, r+2, and (j+1) for j=1,...,r.
```

Their sum is

```text
S_r = 1+2+(r+2)+sum_(j=1)^r(j+1)
    = r(r+1)/2+2r+5.
```

In `DHD`, a closed cycle has the square of the product of its diagonal
weights, here `theta^(2S_r)`. Each of the `L_r=r+3` cyclic starting states
contributes to the diagonal of `T^L_r`. Since all entries are nonnegative,

```text
Tr(T^(r+3)) >= (r+3) theta^(2S_r) > 0.
```

For `r=4`, `theta=1/2`, `S_4=23`, so one oriented cycle has weight `2^-46`
and `Tr(T^7)>=7*2^-46>0`. Immediate reversals have already been excluded; the
coefficient is relation recurrence.

## 8. Finite-trace group control

The enveloping group is

```text
G_r=Z[1/r] semidirect_r Z
   =<u,v | vuv^(-1)=u^r>.
```

Let

```text
A_r=(lambda_u+lambda_(u^-1)+lambda_v+lambda_(v^-1))/4
```

in its group von Neumann algebra, with canonical trace
`tau(X)=<X delta_e,delta_e>`. If `c_r(n)` is the number of length-`n`
identity words on the four oriented generators, then

```text
tau(A_r^n)=c_r(n)/4^n.
```

For real `|z|<1`, `I-zA_r` is positive invertible, and its
Fuglede--Kadison logarithm expands as

```text
log Delta_r(z)=-sum_(n>=1)c_r(n)z^n/(n4^n).
```

The exact audit subtracts free-group counts and sees the first excess at
`n=r+3`. This is an analytic control only; it is not substituted for the
semigroup source or the ordinary Fredholm determinant above.

## 9. Generic scalar superlift

Over the group completion, use one cell orbit in degree two, two generator
orbits in degree one, and one vertex orbit in degree zero. A diagonal scalar
lift of a finite-trace convolution operator `A` commutes with the right-module
boundary maps. With even parity on `C_0 direct-sum C_2` and odd parity on
`C_1`, for every `n>=1`,

```text
Str(A_tilde^n)
 = tau(A^n)-2tau(A^n)+tau(A^n)
 = 0.
```

Hence `SDet(I-z A_tilde)=1`. The relation word never enters the multiplier.
The same result holds for every two-generator one-relator presentation, so the
cancellation is exact, total, and nonselective.

## 10. Exact-control ledger

The frozen prototype verifies:

| `r` | `L_r` | first free-group excess | excess count | one cycle at `theta=1/2` |
|---:|---:|---:|---:|---:|
| 2 | 5 | 5 | 10 | `2^-24` |
| 3 | 6 | 6 | 12 | `2^-34` |
| 4 | 7 | 7 | 14 | `2^-46` |
| 5 | 8 | 8 | 32 | `2^-60` |

Six finite semidirect chain controls pass all twelve boundary-square checks.
Affine-only cell fills leave `H_1` dimensions `2,1,1,1,1,1`; complete
presentation fills give zero in all six cases. All sampled scalar-lift
supertraces through length twelve are exactly zero. These checks corroborate,
but do not prove, the infinite theorem.

## 11. Route consequence

Claim IDs are frozen as:

- `SD-C38-C1`: total chain cancellation;
- `SD-C38-C2`: unit-marker non-descent;
- `SD-C38-C3`: positive prequotient Fredholm relation coefficient;
- `SD-C38-C4`: generic all-orders scalar-superlift cancellation.

Together they force

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL),
overall=ROUTE_A_REJECTED,
route_b_invocation_allowed=false.
```
