# C161 theorem package

## Theorem 1: Birkhoff polynomial

For `R_q(x)=x+1`, `phi(x)=a x^2+b x`, and `n>=1`,

```text
S_n phi(x)=A_n x^2+B_n x+C_n  (mod q),
A_n=an,
B_n=an(n-1)+bn,
C_n=an(n-1)(2n-1)/6+bn(n-1)/2.                 (1)
```

This follows by summing `1`, `j`, and `j^2`; the displayed quotients are
integers before reduction.

## Theorem 2: every-iterate Gauss evaluation

Let `d=gcd(A_n,q)` and `Q=q/d`, with `q` odd.  If `d` does not divide `B_n`,
then `G_(q,n)(a,b)=0`.  If `d|B_n` and `Q>1`, put `A'=A_n/d`, `B'=B_n/d` and

```text
h=-(4A')^(-1)(B')^2  (mod Q),
r=C_n+d h             (mod q).
```

Then

```text
G_(q,n)(a,b)=d (A'|Q) epsilon_Q sqrt(Q) exp(2*pi*i*r/q),        (2)
epsilon_Q=1 if Q=1 mod 4, and i if Q=3 mod 4.                  (3)
```

Here `(A'|Q)` is the Jacobi symbol internal to the finite source ring.  If
`Q=1`, the separate constant branch is
`G=q exp(2*pi*i*C_n/q)`.

**Proof.**  Translation by `Q` multiplies the sum by
`exp(2*pi*i*B_n/d)`, proving exact vanishing when `d` does not divide `B_n`.
When it does, reduction modulo `Q` gives `d` copies of a primitive quadratic
sum.  Since `2A'` is invertible modulo odd `Q`, completing the square produces
the phase `h`.  The primitive lemma

```text
sum_(x mod Q) exp(2*pi*i*A'x^2/Q)
  =(A'|Q) epsilon_Q sqrt(Q)                                  (4)
```

follows first for odd prime powers by pairing the units in the square map and
lifting one exponent at a time; CRT multiplication, with its quadratic
reciprocity sign, gives (4) for odd composite `Q`.  This is an identity of
finite sums; the floating checks are not used in its proof.  Substitution gives
(2).

## Theorem 3: prime zero-level law

For an odd prime `p`, reduce `(A_n,B_n,C_n)` modulo `p`.  If `A_n` is nonzero,

```text
#{x:S_n phi(x)=0}=1+(Delta|p),  Delta=B_n^2-4A_nC_n.          (5)
```

If `A_n=0` and `B_n!=0`, the count is one.  If both vanish, it is `p` or zero
according as `C_n` vanishes or not.  This is completion of the square followed
by the elementary square-root count.

For the frozen pure quadratic subfamily `a=1,b=0`, `p>=5`, and `n!=0 mod p`,

```text
Delta=n^2(1-n^2)/3,
#{x:S_n x^2=0}=1+(Delta|p).                                  (6)
```

Thus `n congruent to plus_or_minus 1 mod p` gives the single double
root, while `n=0 mod p`
makes all three coefficients vanish and gives `p` roots.

## Same-clock finite unitary

On `H_q=ell^2(Z/qZ)`, let `(K_q f)(x)=f(x+1)`, let `M_phi` multiply by
`exp(2*pi*i*phi(x)/q)`, and put `U_phi=M_phi K_q`.  Direct iteration gives

```text
G_(q,n)(a,b)=Tr(U_phi^n K_q^(-n)).                            (7)
```

The compensating shift is essential; we do not replace (7) by `Tr(U_phi^n)`.

There is also an exact source time reversal.  Let `P f(x)=f(-x)`, let `J`
be complex conjugation, put `g(x)=(a-b)x^2`, and let `D_g` multiply by
`exp(2*pi*i*g(x)/q)`.  Then the antiunitary

```text
Theta=D_g P J
```

satisfies `Theta^2=I` and
`Theta U_phi Theta^(-1)=U_phi^(-1)`.  Indeed, `g(-x)=g(x)` proves the
involution, while

```text
g(x)-g(x-1)=phi(-x)-phi(x-1)=(a-b)(2x-1)
```

is precisely the multiplier identity after reversing the shift.

## Route-A boundary

The strict tuple is `(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.
This is a finite source dynamical theorem with a natural unitary realization,
not a target trace identity or isolated stability determinant.  No target
divisor/counting law, arithmetic local/Euler factor, root number, automorphy,
Hilbert--Polya construction, or Route-B authorization is claimed.
