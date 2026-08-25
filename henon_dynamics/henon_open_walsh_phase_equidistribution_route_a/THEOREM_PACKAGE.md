# C163 proof package

## Frozen notation

Let `A=F3^*diag(1,0,1)`, let `B_k` be the frozen cyclic register shift, and
put `C_k=B_k^k=A^(tensor k)`.  The two nonzero roots of

```text
lambda^2-tau lambda+q=0,
tau=sqrt(3)/6-i/2,   q=-1/2-sqrt(3)i/6
```

are labelled by `|lambda_+|>|lambda_-|`.  Write
`u_+/-=lambda_+/-/|lambda_+/-|`, `r=u_+/u_-=exp(i delta)`, and count every
nonzero eigenvalue with algebraic multiplicity.

## Lemma 1: exact non-torsion obstruction

The phase difference satisfies

```text
c:=r+r^(-1)=2cos(delta)=(sqrt(3)-sqrt(111))/6,     (1)
c^2=(19-sqrt(37))/6,
3c^4-19c^2+27=0.                                  (2)
```

Moreover `3x^4-19x^2+27` is the primitive irreducible integer polynomial of
`c`, while its monic rational minimal polynomial is
`x^4-(19/3)x^2+9`.  Hence `c` is not an algebraic integer and `r` is not a
root of unity.

**Proof.**  C158 gives

```text
|tau|^2=1/3,
|lambda_+|^2+|lambda_-|^2=(1+sqrt(37))/6,
|lambda_+ lambda_-|=1/sqrt(3).
```

Expanding `|lambda_++lambda_-|^2=|tau|^2` and dividing by the product of
the moduli yields (1).  Squaring gives (2).  The quadratic equation for
`c^2` is `3y^2-19y+27`, whose discriminant `37` is not a rational square.
Thus `Q(c^2)=Q(sqrt(37))`.  Also `c` is not in that quadratic field: from
`c=sqrt(3)(1-sqrt(37))/6`, membership would imply
`sqrt(3) in Q(sqrt(37))`, impossible for the distinct quadratic fields.
Therefore the displayed primitive integer quartic is irreducible.  Dividing
by `3` gives the monic rational minimal polynomial
`x^4-(19/3)x^2+9`, whose coefficient `-19/3` is not integral.  An algebraic
integer has a monic rational minimal polynomial in `Z[x]`; equivalently, its
primitive integer associate has unit leading coefficient.  Thus `c` is not
an algebraic integer.  If `r` were a root of unity, both `r` and `r^(-1)` and
hence their sum `c` would be algebraic integers, a contradiction. ∎

## Theorem 2: exact Fourier law and Haar phase limit

Let `mu_k` be the multiplicity-weighted probability measure on the unit
phases of the nonzero spectrum of `C_k`.  For every `k>=1`,

```text
mu_k=2^(-k) sum_(j=0)^k binom(k,j) delta_(u_-^k r^j),              (3)
mu_hat_k(m)=u_-^(mk) ((1+r^m)/2)^k,       m in Z.                 (4)
```

Consequently, for every nonzero fixed `m`,

```text
|mu_hat_k(m)|=|cos(m delta/2)|^k -> 0,                            (5)
```

and `mu_k` converges weakly to normalized Haar measure on the circle.  More
quantitatively, if `p(z)=sum_(|m|<=M) a_m z^m`, then

```text
|mu_k(p)-Haar(p)|
 <= sum_(0<|m|<=M) |a_m| |cos(m delta/2)|^k.                      (6)
```

**Proof.**  The tensor spectrum has products
`lambda_+^j lambda_-^(k-j)` with multiplicity `binom(k,j)`, giving (3).
The binomial theorem gives (4).  Lemma 1 makes `r^m != 1` for every
`m!=0`, so each contraction factor in (5) is strictly below one.  Equation
(6) is termwise, and density of trigonometric polynomials in the continuous
functions on the circle proves weak convergence. ∎

## Theorem 3: joint Gaussian--Haar limit

Set `d=log(|lambda_+|/|lambda_-|)`,
`sigma^2=d^2/4`, and

```text
Y_k=sqrt(k)((1/k)log|rho|+log(3)/4).
```

For real `t` and integer `m`, the exact mixed transform is

```text
E[e^(itY_k) phase(rho)^m]
=u_-^(mk)e^(-it d sqrt(k)/2)
 ((1+r^m e^(itd/sqrt(k)))/2)^k.                                 (7)
```

Thus `(Y_k,phase(rho))` converges jointly to
`Normal(0,sigma^2) tensor Haar`; in particular, the central-limit modulus
fluctuation and phase are asymptotically independent.

**Proof.**  If `J_k` is fair binomial, then
`Y_k=d(J_k-k/2)/sqrt(k)` and the phase is `u_-^k r^(J_k)`, which gives (7).
For `m=0`, (7) is the usual Bernoulli characteristic function and tends to
`exp(-sigma^2t^2/2)`.  For `m!=0`, its base tends to `(1+r^m)/2`, of modulus
strictly below one, so the transform tends to zero.  Tightness follows from
the one-dimensional CLT; Fourier--characteristic uniqueness identifies the
product limit. ∎

## Proposition 4: binary phase dichotomy and control

For any two phases with ratio `r`, the same binomial measures have two
branches.  If `r` is non-torsion they converge weakly to Haar.  If `r` has
exact order `h`, they converge in total variation to the uniform measure on
the moving coset `u_-^k<r>`, with

```text
TV <= (h-1)/2 max_(1<=m<h)|cos(pi m/h)|^k.                        (8)
```

This is finite Fourier inversion on `Z/hZ`.  The frozen gate occupies the
non-torsion branch.  Moving the hole to `diag(0,1,1)` gives nonzero roots
`-i,-1/sqrt(3)` and phase ratio `i`, hence the order-four branch with
`TV<=(3/2)(sqrt(2)/2)^k`.  Projector order is a unitary similarity and
preserves the frozen branch.  The closed parent has three surviving phases
and is stated as outside this binary proposition.

## Route-A boundary

This clears C158's source-native phase-limit gate and gives a new joint
limit, but the tuple remains
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`, overall
`ROUTE_A_EXPLORATORY`.  It proves no self-adjoint or antiunitary limit, target
divisor, target functional equation/counting law, prime correspondence,
arithmetic local factor, Euler factor, root number, automorphy,
Hilbert--Polya operator, or Route-B authorization.
