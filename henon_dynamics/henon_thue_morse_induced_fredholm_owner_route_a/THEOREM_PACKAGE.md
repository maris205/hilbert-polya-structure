# C164 proof package

## Source and branch Hilbert space

Let `t_s` be the parity of the binary digit sum of `s`, let
`S={s>=0:t_s=1}`, and put

```text
F(z)=sum_(s in S) z^(s+1).
```

C159 proves for the associated S-gap shift `X_S` that

```text
zeta_X(z)^(-1)=(1-z)(1-F(z)),
```

and that `F` has no meromorphic continuation through any arc of the unit
circle.  We now retain the branch label rather than collapsing `F` to a
scalar formula.

On `H=l2(S)` take its orthonormal basis `(e_s)`.  Freeze

```text
q_s=exp(-sqrt(s+1)),     u=(q_s)_(s in S),
ell_z(f)=sum_(s in S) q_s^(-1) z^(s+1) f_s,
K_z f=ell_z(f)u,         L_z=[z] direct_sum K_z.
```

## Theorem 1: trace-norm holomorphic first-return owner

For every `|z|<1`, `K_z` is trace class of rank at most one, the map
`z -> K_z` is trace-norm holomorphic, and for every integer `m>=1`,

```text
Tr(K_z^m)=F(z)^m,
det_F(I-L_z)=(1-z)(1-F(z))=zeta_X(z)^(-1).                 (1)
```

**Proof.**  First, `u` is square summable.  On every closed disk
`|z|<=rho<1`, the coefficient vector of `ell_z` is square summable because

```text
sum_(s in S) exp(2 sqrt(s+1)) rho^(2s+2) < infinity.
```

More is true.  Resolve the source branch `s` as

```text
B_s(z)f=q_s^(-1) z^(s+1) f_s u.
```

It is rank one and

```text
||B_s(z)||_1=||u||_2 exp(sqrt(s+1)) |z|^(s+1).
```

The sum of these norms converges uniformly on `|z|<=rho`; the differentiated
series does as well after any fixed number of derivatives.  Thus
`K_z=sum_s B_s(z)` in trace norm and is trace-norm holomorphic.

Now `ell_z(u)=F(z)`.  Hence `K_z^m=F(z)^(m-1)K_z` and
`Tr(K_z^m)=F(z)^m`.  The sole possible nonzero eigenvalue is `F(z)`, so
`det_F(I-K_z)=1-F(z)`.  Multiplicativity over the direct sum with `[z]`
proves (1).  Each branch also satisfies `Tr B_s(z)=z^(s+1)`: the gauge
cancels, exposing the frozen return duration.  This branch resolution and
the all-power trace law are the ownership data absent from a post-hoc scalar
determinant.  QED.

## Theorem 2: the uninduced adjacency cannot be compact

Let positive weights `w_n` define `H_w=l2(N0,w)`, and freeze the time-one
renewal adjacency

```text
A delta_n=delta_(n+1)+t_n delta_0.                         (2)
```

Whenever (2) defines a bounded operator on `H_w`, it is noncompact and is in
no Schatten class `S_p`, `0<p<infinity`.

**Proof.**  The normalized coordinate vectors
`e_n=delta_n/sqrt(w_n)` are an orthonormal, hence weakly null, sequence.  In
this basis

```text
A e_n=sqrt(w_(n+1)/w_n)e_(n+1)
      +t_n sqrt(w_0/w_n)e_0.                               (3)
```

The two summands are orthogonal.  If `A` were compact, weak-to-norm
continuity on this bounded sequence would imply `||Ae_n|| -> 0`.  The first
coefficient in (3) would then tend to zero.  Eventually it is below `1/2`,
so `w_(n+1)<=w_n/4` and consequently `w_n -> 0`.

The set `S` is infinite.  Along `n in S`, the second coefficient in (3)
would also tend to zero, forcing `w_n -> infinity`.  This contradicts the
first conclusion.  Every Schatten operator is compact, proving the final
claim.  The quantifier is nonvacuous: for `w_n=2^n`, the advance is bounded
with norm `sqrt(2)` and the return functional has squared norm
`sum_(s in S)2^(-s)<infinity`.  QED.

## Theorem 3: maximal trace-class domain

Neither `K_z` nor `L_z` admits a trace-class meromorphic extension through
an open arc of `|z|=1`.

**Proof.**  The scalar trace is a continuous linear functional on trace
class.  A trace-class meromorphic continuation of `K_z` would therefore
continue `Tr K_z=F(z)` meromorphically.  A continuation of `L_z` would
continue `z+F(z)`, hence again `F`.  Either conclusion contradicts C159's
unit-circle natural-boundary theorem (one may shrink any arc to avoid the
single point `z=1`).  QED.

## Boundary

The induced family is a natural first-return transfer owner; it is not the
time-one adjacency.  The latter has a universal compactness obstruction.
No unitary, Hamiltonian, self-adjoint, target-facing, or Hilbert--Pólya
operator follows.  The strict tuple remains

```text
(A1_WEAK,A2_FAIL,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL),
overall=ROUTE_A_EXPLORATORY,
route_b_invocation_allowed=false.
```
