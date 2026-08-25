# C150 proof package

## Claim and status

Let `L=2^r-1`, `R_L=F_2[x,x^(-1)]/(x^L-1)`, and let Rule 90 be multiplication
by `a=x+x^(-1)`.  Then

```text
a^(L+1)=a,  dim ker(a)=1,  dim im(a)=L-1.
```

Every state enters `im(a)` after one update; the periodic states are exactly
`im(a)`, so exactly half of all states are periodic, and every least period
divides `L`.  Exact fixed and primitive counts follow from polynomial gcd and
Möbius inversion.  For the matched circumference `L=2^s`, Rule 90 is
nilpotent and zero is the only periodic state.  **PROVABLE AS STATED.**

## Theorem 1: Mersenne Frobenius identity

In characteristic two, Frobenius gives

```text
a^(2^r)=x^(2^r)+x^(-2^r).
```

Because `2^r=L+1` and `x^L=1`, both exponents reduce modulo `L` to `1` and
`-1`, respectively.  Hence `a^(2^r)=a`, equivalently `a^(L+1)=a`.

Multiplication by the invertible monomial `x` turns `a` into
`x*a=x^2+1=(x+1)^2`.  Since `L` is odd, the derivative of `x^L+1` is
`x^(L-1)`, coprime to `x^L+1`; thus the modulus is squarefree.  It has `x+1`
as a factor, so

```text
gcd(x^L+1,(x+1)^2)=x+1.
```

The multiplication-kernel lemma gives kernel dimension one and image
dimension `L-1`.

## Theorem 2: one-step eventual image and periodic partition

Every updated state is in `im(a)`.  If `y=a u` belongs to the image, Theorem 1
gives

```text
a^L y=a^(L+1)u=a u=y.
```

Thus the restriction to the image is a permutation whose order divides `L`,
and every image state is periodic.  Conversely, if `a^n u=u` for some
`n>=1`, then `u=a(a^(n-1)u)` lies in the image.  Hence the periodic set equals
the image.  It has `2^(L-1)` points among `2^L`, exactly one half; the other
half enters it after the first update.  Every least cycle period divides `L`.
This does not say that every divisor of `L` actually occurs.

## Theorem 3: divisor-resolved counts

For a monic `f` and multiplier `h`, multiplication by `h` on `k[x]/(f)` has
kernel dimension `deg gcd(f,h)`: after writing `f=g f_1`, `h=g h_1` with
coprime `f_1,h_1`, the condition `f|h q` is equivalent to `f_1|q`.
Clearing the Laurent denominator by `x^n` therefore yields, for all `n>=1`,

```text
Fix_L(n)=2^deg gcd(x^L+1,(x^2+1)^n+x^n).
P_L(n)=sum_(d|n) mu(n/d) Fix_L(d),   C_L(n)=P_L(n)/n.
```

The exact-period support is contained among divisors of `L`, and summing it
recovers `2^(L-1)` periodic points.

## Proposition 4: power-of-two negative control

For `L=2^s`, Frobenius at exponent `2^(s-1)` gives

```text
a^(2^(s-1))=x^(2^(s-1))+x^(-2^(s-1))=0,
```

because the two exponents are congruent modulo `2^s`.  Thus the map is
nilpotent.  A periodic state of a nilpotent map must be zero: iterate its
period equation until a nilpotent power annihilates both sides.

## Route-A conclusion

This is a genuine all-scale finite-volume theorem, earning `A1_WEAK`, but it
provides no frozen target determinant, global analytic comparison, arithmetic
factorization, or natural operator lift.  The strict tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall `ROUTE_A_EXPLORATORY`, and
`route_b_invocation_allowed=false`.
