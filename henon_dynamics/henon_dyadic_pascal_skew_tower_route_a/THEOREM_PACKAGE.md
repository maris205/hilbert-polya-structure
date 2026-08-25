# C166 theorem package

## Definition and Pascal coordinates

Let `q=2^r` with `r>=1`, let `d>=2`, and put

```text
T(x_1,...,x_d)=(x_1+x_2,...,x_(d-1)+x_d,x_d+1) mod q.       (1)
```

Work in `R=(Z/qZ)[t]/(t^(d+1))` and identify a state with the unit

```text
p_x(t)=1+x_d*t+x_(d-1)*t^2+...+x_1*t^d.                    (2)
```

Multiplication by `1+t` sends the coefficient vector in (2) exactly as (1).
Consequently

```text
p_(T^n x)(t)=(1+t)^n p_x(t),                               (3)
```

and the displacement coefficients are `binom(n,k)`, `1<=k<=d`.

## Theorem 1: exact fixed-point dichotomy

Put

```text
a=floor(log_2 d),                 M=2^(r+a).                (4)
```

For every `n>=1`,

```text
Fix(T^n)=(Z/qZ)^d  if M divides n,
Fix(T^n)=empty     otherwise.                              (5)
```

**Proof.**  The polynomial `p_x` has constant coefficient one and is therefore
a unit of `R`.  By (3), `T^n x=x` is equivalent to

```text
(1+t)^n=1 mod (q,t^(d+1)),
```

independently of `x`.  This is equivalent to

```text
q divides binom(n,k) for every 1<=k<=d.                    (6)
```

It remains to classify (6).  For every `1<=k<=n`,

```text
binom(n,k)=(n/k) binom(n-1,k-1),
v_2(binomial(n,k)) >= v_2(n)-v_2(k).                       (7)
```

For `k>n`, the coefficient `binom(n,k)` is zero and is automatically
divisible by `q`, so no valuation of zero is needed.

If `M|n`, then `v_2(n)>=r+a`; since `k<=d` gives `v_2(k)<=a`,
(7) proves `v_2(binomial(n,k))>=r` for all required `k`.

Conversely, if `q` does not divide `n`, the coefficient `binom(n,1)=n`
already violates (6).  Suppose `q|n` but `M` does not divide `n`.  Write

```text
v_2(n)=r+b,                       0<=b<a,
```

and choose the required witness

```text
k=2^(b+1)<=2^a<=d.                                         (8)
```

The lowest `r+b` binary digits of `n-1` are all one, while the lowest `b+1`
digits of `k-1` are all one.  Lucas reduction modulo two therefore makes
`binom(n-1,k-1)` odd.  The equality in (7) at this `k` is

```text
v_2(binomial(n,k))=r+b-(b+1)=r-1,                           (9)
```

so (6) fails.  This proves (5) for every parameter; no finite cutoff is used.

## Corollary 2: periods, cycles, zeta, and determinant

Equation (5) says that every one of the `q^d` states has exact least period
`M`.  Thus there are exactly `q^d/M` primitive cycles.  Writing
`N_n=#Fix(T^n)`, one obtains

```text
sum_(n>=1) N_n*z^n/n
 =q^d sum_(j>=1) z^(jM)/(jM)
 =-(q^d/M) log(1-z^M).
```

Hence, as a formal identity and as a rational function near zero,

```text
zeta_T(z)=(1-z^M)^(-q^d/M).                                (10)
```

The Koopman permutation `U_T f=f composed with T` is the direct sum of
`q^d/M` cyclic permutations of length `M`, so

```text
det(I-z U_T)=(1-z^M)^(q^d/M)=zeta_T(z)^(-1).                (11)
```

This is a finite source determinant, not a target determinant comparison.

## Theorem 3: source-derived reversor

Because `t` is nilpotent in `R`, the substitution

```text
sigma(t)=-t/(1+t)=-t+t^2-...+(-1)^d*t^d                    (12)
```

is a well-defined ring automorphism and preserves the constant-term-one
state hyperplane.  Direct rational composition gives

```text
sigma(sigma(t))=t,                 1+sigma(t)=(1+t)^(-1).   (13)
```

Therefore, if `L_(1+t)` denotes multiplication by `1+t`,

```text
sigma L_(1+t) sigma=L_((1+t)^(-1)).                         (14)
```

In state coordinates, `sigma` is an involution and
`sigma T sigma=T^(-1)`.  Let `P_sigma f=f composed with sigma` and let `J`
be coefficientwise complex conjugation.  Then

```text
Theta=P_sigma J,                   Theta^2=I,
Theta U_T Theta^(-1)=U_T^(-1).                              (15)
```

Thus the same finite source supplies both the Koopman unitary and its exact
antiunitary reversal at the unchanged clock.

## Progress and Route-A boundary

The `d=2` even-modulus shear is absorbed as one row of the theorem, while the
odd product-rotation branch is not recycled as a paper.  The new result is
the exact dimension-dependent clock and reversor for all `r>=1,d>=2`; it is
not a complexity claim.

The strict tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, the overall verdict is
`ROUTE_A_EXPLORATORY`, and Route B is unauthorized.  We claim no target
trace/divisor/counting law, arithmetic local or Euler data, root number,
automorphy, Hilbert--Polya operator, or cross-candidate coordinate synthesis.
