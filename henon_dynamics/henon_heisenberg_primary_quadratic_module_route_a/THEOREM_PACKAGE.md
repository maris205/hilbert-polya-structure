# C156 proof package

## Status, assumptions, and strategy

**Status: PROVABLE AS STATED.**  Let
`A=((2,1),(1,1))`, let `F_n,L_n` denote Fibonacci and Lucas numbers, and use
the C151 Heisenberg automorphism with one-step correction
`q(x,y)=x(x-1)+xy+y(y-1)/2`.  For `B=A^n`, put `M=B-I`; if `m=Mv`, set

```text
rho_n([m])=q_n(v)-m_1 v_2  (mod 1),
q_n(v)=sum_(j=0)^(n-1) q(A^j v).
```

The dependency order is: matrix factorization -> Smith exponent -> canonical
cocycle and parity lemma -> quadratic polarization -> primary orthogonality ->
zero-count product.

## Theorem 1: all-iterate Smith type

For odd `n`,

```text
M=L_n [[F_(n+1),F_n],[F_n,F_(n-1)]],            (1)
Z^2/MZ^2 = (Z/L_n Z)^2.
```

For even `n`,

```text
M=F_n [[L_(n+1),L_n],[L_n,L_(n-1)]],            (2)
Z^2/MZ^2 = Z/F_n Z x Z/(5F_n)Z.
```

**Proof.**  Writing `A=Q^2` for
`Q=((1,1),(1,0))` gives
`A^n=((F_(2n+1),F_(2n)),(F_(2n),F_(2n-1)))`.
The Fibonacci doubling identities and Cassini identity split `A^n-I` as
(1) for odd `n` and (2) for even `n`.  The odd cofactor has determinant
`F_(n+1)F_(n-1)-F_n^2=(-1)^n=-1`, so it is unimodular.  The even cofactor has
determinant `L_(n+1)L_(n-1)-L_n^2=5(-1)^(n-1)=-5`; for even `n` its entries
have gcd one, so its Smith invariants are `(1,5)`.  Scaling supplies the
displayed Smith types.  Their exponents are

```text
h_n=L_n (n odd),        h_n=5F_n (n even).       (3)
```

## Theorem 2: exponent denominator

For every `n` and every horizontal class,

```text
h_n rho_n([m])=0 in Q/Z.                          (4)
```

**Proof.**  For any `B=((a,b),(c,d))` in `SL(2,Z)`, the canonical integral
correction is

```text
q_B(x,y)=ac*x(x-1)/2+bc*xy+bd*y(y-1)/2.          (5)
```

Its polarization is `(Bv)_1(Bw)_2-v_1w_2`.  Therefore `q_n-q_(A^n)` has zero
polarization and vanishes at zero; because both corrections are integral on
`Z^2`, it is an integer linear form `ell_n`.

It remains to prove (4) for `q_(A^n)`.  Uniformly write
`M=gU`, `U=((r,s),(s,t))`.  In the odd branch `g=L_n`, `det U=-1`, and
`h=g`; in the even branch `g=F_n`, `det U=-5`, and `h=5g`.  In both cases
`W=hv=(X,Y)` is integral by Theorem 1.  From

```text
q_B(v)=((Bv)_1(Bv)_2-v_1v_2-ac*v_1-bd*v_2)/2
```

one obtains the integer

```text
N=2h(q_B(v)-m_1v_2)
 =X(m_2-ac)-Y(m_1+bd)+h*m_1*m_2.                 (6)
```

We now prove that `N` is even.  In the even branch
`m=UW/5`; reduction modulo two is legitimate because five is odd.  Hence both
branches reduce to the same calculation with `B=I+gU`.  Using
`X^2=X` and `Y^2=Y` modulo two, substitution into (6) gives

```text
N = s(gr+1)(g+1)X+s(gt+1)(g+1)Y
    +[g(rt+s^2)+r+t]XY                 (mod 2).  (7)
```

Both `F_k` and `L_k` modulo two follow the period-three sequence `0,1,1`.
If `3` divides `n`, then `g=s=0` and `r=t=1`, so (7) vanishes.  Otherwise
`g=1`, the first two terms vanish, `rt+s^2=1` because `det U` is odd, and
exactly one of the neighbouring indices `n-1,n+1` is divisible by three, so
`r+t=1`; the last coefficient also vanishes.  Thus `N` is even.  Finally,
`h ell_n(v)` is integral because `ell_n` has integer coefficients and `hv` is
integral.  This proves (4).  No assertion that `h_n` is always sharp is used.

## Theorem 3: orthogonal primary zero product

The map `rho_n:G_n=Z^2/MZ^2 -> Q/Z` is quadratic with bilinear polarization

```text
beta_n([m],[u])=v_1u_2-u_1v_2+m_1u_2  (mod 1),  (8)
```

where `v=M^(-1)m` and `w=M^(-1)u`.  If
`G_n` is decomposed into its group-theoretic primary components `G_(n,p)`,
then different components are orthogonal.  Moreover `rho_n` restricted to a
component whose exponent is `p^e` takes values in `(1/p^e)Z/Z`, and

```text
C_n=product_(p divides h_n) C_(n,p),              (9)
C_(n,p)=1/p^e sum_(a mod p^e) sum_(x in G_(n,p))
          exp(2*pi*i*a*rho_n(x)).                 (10)
```

**Proof.**  Expanding the cocycle polarization and the three `-m_1v_2`
terms gives (8).  Bilinearity implies that `beta(x,y)` is killed by the order
of each argument.  Coprime primary orders therefore force it to vanish.
For odd `p`, the quadratic identity
`rho(kx)=k rho(x)+binom(k,2)beta(x,x)` shows that a `p^e`-torsion element has
`p`-primary rotation.  For `p=2` it first gives a possible extra factor two;
Theorem 2 removes that factor.  Thus each local rotation is `p`-primary.
Orthogonality gives `rho(sum_p x_p)=sum_p rho(x_p)`.  Uniqueness of the
primary decomposition in `Q/Z` makes this sum zero exactly when every term is
zero, proving (9).  Root-of-unity orthogonality proves (10).  This is not an
arithmetic local or Euler product.  ∎

## Exact certificate and Route-A boundary

CRT idempotents and HNF reduction enumerate every primary component through
`n=14`.  The certified counts are

```text
C_n: 1,1,4,1,21,4,57,1,148,105,397,144,1041,57.
```

The observed denominator lcm equals `h_n` for `2<=n<=14`; this finite fact is
not extrapolated.  The fixed sets remain clean circles and the isolated
stability factor remains singular.  The strict tuple is
`(A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.  No target divisor, target
functional equation/counting law, arithmetic local/Euler factor, root number,
automorphy, Hilbert--Polya construction, or Route-B authorization is claimed.
