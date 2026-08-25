# C168 proof package

## Frozen notation

Let `F4=(i^(jl)/2)_(0<=j,l<4)`.  For `h in {0,1,2,3}`, put
`P_h=diag(p_0,p_1,p_2,p_3)`, where `p_j=1-delta_(j,h)`, and set
`A_h=F4^*P_h`; throughout, `A=A_1`.  At register length `k`, one tick is the
cyclic register map

```text
B_k(v_0 tensor ... tensor v_(k-1))
  =v_1 tensor ... tensor v_(k-1) tensor A v_0.
```

Every original tensor factor therefore passes through `A` exactly once in
`k` ticks, so one complete cycle is `C_k=B_k^k=A^(tensor k)`.  Nonzero
eigenvalues are counted with algebraic multiplicity.

## Lemma 1: one-site algebra and nontorsion

The characteristic polynomial is

```text
chi_A(x)=x(x-1)(x^2+i x/2-1/2).                                 (1)
```

Thus the nonzero eigenvalues are

```text
1,  lambda_+=(sqrt(7)-i)/4,  lambda_-=(-sqrt(7)-i)/4,            (2)
```

with `|lambda_+|=|lambda_-|=1/sqrt(2)`.  Put

```text
u_+=(sqrt(7)-i)/(2sqrt(2)),  u_-=(-sqrt(7)-i)/(2sqrt(2)).        (3)
```

Then `u_++u_-=-i/sqrt(2)`, `u_+u_-=-1`, and

```text
r=u_+/u_-=(-3+i sqrt(7))/4,       r+r^(-1)=-3/2.                (4)
```

In particular, `r` is not a root of unity.

**Proof.**  Direct determinant expansion gives (1), whose four roots are
distinct, hence `A` is diagonalizable.  Equations (2)--(4) follow by exact
radical arithmetic.  If `r` were a root of unity, then `r+r^(-1)` would be
an algebraic integer.  A rational algebraic integer is an integer, whereas
`-3/2` is not. ∎

## Theorem 2: exact all-`k` secular product

For `a+b+c=k`, let `M_k(a,b,c)=k!/(a!b!c!)`.  Then

```text
det(I-z C_k)
 = product_(a+b+c=k) (1-z lambda_+^b lambda_-^c)^M_k(a,b,c).    (5)
```

Its degree in `z` is `3^k`, while the generalized zero eigenspace of `C_k`
has dimension `4^k-3^k`.

**Proof.**  Tensor products of the four distinct one-site eigenvectors form
an eigenbasis.  A nonzero tensor eigenvalue uses only the three nonzero
one-site roots.  Counting words with contents `(a,b,c)` proves (5) and the
multinomial identity gives degree `3^k`.  All remaining `4^k-3^k` basis
vectors contain a zero factor. ∎

The labels in (5) are retained with multiplicity.  We do **not** assert that
all phase labels from different triples are distinct.

## Theorem 3: rank-three Haar phase law

Let `mu_k` be the multiplicity-weighted probability measure on phases of
the nonzero spectrum.  Then

```text
mu_k=3^(-k) sum_(a+b+c=k) M_k(a,b,c) delta_(u_+^b u_-^c),       (6)
mu_hat_k(m)=((1+u_+^m+u_-^m)/3)^k,       m in Z.                (7)
```

For every fixed `m!=0`, the base in (7) has modulus strictly below one.
Consequently `mu_k` converges weakly to normalized Haar measure on the
circle.

**Proof.**  Formula (7) is the multinomial theorem.  Equality in the triangle
inequality for the average of `1,u_+^m,u_-^m` would require all three unit
numbers to agree.  That would imply `r^m=1`, contradicting Lemma 1.  Hence
every fixed nonzero Fourier coefficient tends to zero; density of
trigonometric polynomials proves weak convergence. ∎

This is a fixed-mode statement.  No contraction gap uniform in all `m` is
claimed.  Moreover every finite-`k` measure is atomic and continuous Haar
measure is nonatomic, so their total-variation distance is exactly one.

## Theorem 4: joint Gaussian--Haar limit

Under the normalized nonzero spectral law, one tensor factor contributes

```text
X=0 with probability 1/3,
X=-log(2)/2 with probability 2/3.                               (8)
```

Thus `E X=-log(2)/3` and `Var X=log(2)^2/18`.  Set

```text
Y_k=(log|rho|+k log(2)/3)/sqrt(k).
```

For real `t` and integer `m`, the exact mixed transform is

```text
E[e^(itY_k) phase(rho)^m]
=e^(it log(2)sqrt(k)/3)
 ((1+e^(-it log(2)/(2sqrt(k)))(u_+^m+u_-^m))/3)^k.              (9)
```

It follows that

```text
(Y_k,phase(rho)) => Normal(0,log(2)^2/18) tensor Haar.          (10)
```

**Proof.**  For `m=0`, (9) is the characteristic function of the centered
iid sum in (8) and converges to the stated Gaussian transform.  For fixed
`m!=0`, the bracket tends to the strictly contracting base in (7), so the
mixed transform tends to zero.  Tightness follows from the scalar CLT, and
Fourier--characteristic uniqueness identifies the product limit. ∎

## Proposition 5: torsion and antiunitary controls

For the already defined `A_0=F4^*diag(0,1,1,1)`,

```text
chi_A0(x)=x(x-1)(x+1/2)(x+i),
phase steps={1,-1,-i} subset <i>.
```

Let `nu_k` be the algebraic-multiplicity-weighted nonzero phase law of
`A_0^(tensor k)`, equivalently the `k`-fold convolution of the uniform
one-step law on `{1,-1,-i}`.  Every nontrivial Fourier coefficient of the
one-step law on `Z/4Z` has modulus `1/3`, hence the corresponding coefficient
of `nu_k` has modulus `3^(-k)`.  Finite Fourier inversion therefore gives

```text
TV(nu_k,Uniform(<i>)) <= (3/2)3^(-k).                           (11)
```

Let `R=F4^2`, so `R A_1 R=A_3`.  With coordinate conjugation `K`, the
antiunitary `Theta=F4 K` satisfies

```text
Theta A_1 Theta^(-1)=A_3^*=diag(1,1,1,0)F4.                    (12)
```

Equation (12) exchanges holes `1` and `3` while reversing propagation and
projector order.  It is a finite-dimensional control, not a fixed-hole
self-adjoint or antiunitary limiting operator.

## Route-A boundary

The verdict is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`, overall
`ROUTE_A_EXPLORATORY`.  These are source-side secular and limit theorems.
They establish no target divisor, functional equation, counting law,
prime-like correspondence, arithmetic local data, Euler factor, root
number, automorphy, Hilbert--Polya operator, or Route-B authorization.
