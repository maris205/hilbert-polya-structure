# C158 proof package

## Status and frozen notation

**Status: PROVABLE AS STATED.**  Let

```text
F3[j,l]=omega^(jl)/sqrt(3),  P=diag(1,0,1),  A=F3^*P,
B_k(v0,...,v_(k-1))=(v1,...,v_(k-1),Av0).
```

One `B_k` application is one tick.  Define the `k`-tick full cycle
`C_k=B_k^k` and use only the secular convention
`E_k(z)=det(I_(3^k)-zC_k)`.

The one-site polynomial is

```text
chi_A(lambda)=lambda(lambda^2-tau lambda+q),
tau=sqrt(3)/6-i/2,  q=-1/2-sqrt(3)i/6.            (1)
```

Its discriminant is `11/6+sqrt(3)i/2`, so all three roots are distinct.
Label the nonzero roots so `|lambda_+|>|lambda_-|>0`.

## Theorem 1: full-cycle secular factorization

For every `k>=1`,

```text
C_k=A^(tensor k),
E_k(z)=product_(j=0)^k
 (1-z lambda_+^j lambda_-^(k-j))^binom(k,j).      (2)
```

Thus `deg E_k=2^k`; the generalized zero eigenspace of `C_k` has dimension
`3^k-2^k`.

**Proof.**  During `k` cyclic shifts every original tensor factor passes
through `A` once and returns to its original position, giving the first
identity.  Since (1) has distinct roots, `A` is diagonalizable with diagonal
entries `0,lambda_+,lambda_-`.  Tensoring this diagonalization gives one
eigenvalue for every word of length `k` in those three symbols.  A word is
nonzero exactly when it avoids zero.  Among the surviving binary words,
exactly `binom(k,j)` contain `j` plus symbols, proving (2).  There are `2^k`
survivors and `3^k-2^k` zero words.  Diagonalizability makes the latter count
the generalized zero space as well as algebraic multiplicity. ∎

Colliding products, if any, remain listed with their summed algebraic
multiplicity; no distinct-value deduplication changes (2).  Also

```text
Tr(C_k^n)=Tr(A^n)^k,                              (3)
```

which gives independent Newton coefficients in `Q(sqrt(3),i)`.

## Lemma 2: unequal one-site moduli

Put `p_+/-=|lambda_+/-|^2`.  Then

```text
p_++p_-=(1+sqrt(37))/6,    p_+p_-=1/3,
(p_+-p_-)^2=(sqrt(37)-5)/18>0.                   (4)
```

In particular,

```text
p_+/-=(1+sqrt(37))/12 +/- sqrt((sqrt(37)-5)/72).
```

**Proof.**  Let `delta=lambda_+-lambda_-`, so `delta^2=tau^2-4q`.
Parallelogram identity gives
`2(p_++p_-)=|tau|^2+|delta|^2`.  Directly,
`|tau|^2=1/3` and `|delta|^2=|tau^2-4q|=sqrt(37)/3`, proving the sum.
The product is `|q|^2=1/3`.  Subtracting four times the product from the
square of the sum gives the last identity, which is positive since
`sqrt(37)>5`. ∎

## Theorem 3: surviving log-modulus law

For each nonzero eigenvalue `rho` of `C_k`, counted with algebraic
multiplicity, put `X_k=k^(-1)log|rho|`.  Its empirical probability measure is

```text
nu_k=2^(-k) sum_(j=0)^k binom(k,j)
 delta_((j a+(k-j)b)/k),                          (5)
```

where `a=log|lambda_+|` and `b=log|lambda_-|`.  Equivalently, if
`J_k~Binomial(k,1/2)`, then `X_k=b+(J_k/k)(a-b)`.  Consequently,

```text
E X_k=mu=-log(3)/4,
Var(X_k)=sigma^2/k,
sigma^2=(log(|lambda_+|/|lambda_-|))^2/4.         (6)
```

For every `epsilon>0`,

```text
nu_k(|X-mu|>=epsilon)
 <=2 exp(-k epsilon^2/(2 sigma^2)).               (7)
```

Hence `nu_k` converges weakly to `delta_mu`, and

```text
sqrt(k)(X_k-mu) => Normal(0,sigma^2).             (8)
```

**Proof.**  Formula (5) is (2) with multiplicities normalized by `2^k`.
The binomial mean and variance give (6), while
`a+b=log|lambda_+lambda_-|=log|q|=-log(3)/2` fixes `mu`.
The two-sided Bernoulli Hoeffding estimate
`P(|J_k/k-1/2|>=s)<=2e^(-2ks^2)` with
`s=epsilon/|a-b|` gives (7).  Since the support stays in the compact interval
`[b,a]`, (7) implies weak convergence against every continuous test function.

For a self-contained central-limit receipt, let `Y_l` be independent signs.
Then

```text
sqrt(k)(X_k-mu)=(a-b)/(2sqrt(k)) sum_(l=1)^k Y_l.
```

Its characteristic function is
`cos(t(a-b)/(2sqrt(k)))^k`, which tends to
`exp(-t^2(a-b)^2/8)=exp(-sigma^2t^2/2)`.  This proves (8). ∎

## Controls and Route-A boundary

With `P=I_3`, the closed one-site gate is unitary; the full-cycle degree is
`3^k` and its normalized log-modulus measure is exactly `delta_0`.
Putting the projector on the other side gives
`A_right=F3 A F3^*`, so uniform tensor conjugacy preserves (2)--(8).

Moving the hole to `P0=diag(0,1,1)` gives nonzero roots `-i` and
`-1/sqrt(3)`.  Rank and degree remain unchanged.  Their product modulus is
again `1/sqrt(3)`, so the mean remains `-log(3)/4`; it does **not** change.
The variance coefficient becomes `(log 3)^2/16`, which differs from the
frozen value: equality would force `p_+/p_-=3`, hence sum `4/3`, contradicting
(4).  Thus rank and mean do not determine spectral spread.

The strict tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`, overall
`ROUTE_A_EXPLORATORY`.  C158 proves no phase limit, secular-zero inverse-radius
limit, self-adjoint or antiunitary limit, target divisor, functional equation,
counting law, arithmetic/local factor, Euler factor, root number, automorphy,
Hilbert--Polya operator, or Route-B authorization.
