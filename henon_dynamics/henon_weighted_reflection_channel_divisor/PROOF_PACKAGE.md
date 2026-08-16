# HCS-P75 proof package

## 1. Frozen weighted packet

For odd `n`, let `A_n` be P69--P70's primitive marked reflection packet and

    chi(s)=1{s[-1]=s[1]},
    S_n chi(s)=sum_(j mod n) chi(sigma^j s).

P69 proves, for `n=2h+1`,

    F_n(q)=2q(1+q^2)^h,
    E_n(q)=sum_(k|n) mu(k) F_(n/k)(q^k).

P70 defines

    Z_orb(z,q)=product_(n odd) product_(omega in A_n)
               (1-z^n q^(S_n chi(omega)))^(-1)

and proves the Euler repetition identity

    log Z_orb(z,q)=sum_(r>=1) E(z^r,q^r)/r,
    E(z,q)=sum_(n odd) E_n(q)z^n.

These repository objects, rather than a new Lind or operator model, are the
only inputs.

## 2. Two-fugacity lift

Put `w=qz`.  Since `0<=S_n chi<=n`, every orbit monomial lifts as

    z^n q^(S_n chi)=z^(n-S_n chi)w^(S_n chi).

Let `Z_sharp(z,w)` denote the corresponding formal orbit product.  P69's
all-word function lifts exactly to

    F_sharp(z,w)
      =sum_(h>=0) 2w(z^2+w^2)^h
      =2w/(1-z^2-w^2).

Odd dilation Möbius inversion and Euler repetition become

    E_sharp(z,w)=sum_(k odd) mu(k) F_sharp(z^k,w^k),
    log Z_sharp(z,w)=sum_(r>=1) E_sharp(z^r,w^r)/r.

On the fiber `w=qz`, these identities reduce coefficientwise to P70.

## 3. Exact weighted channel regrouping

Define

    Psi_m(z,w)=2w^m/(1-z^(2m)-w^(2m)).

In a sufficiently small polydisk, absolute convergence permits grouping by
`m=kr`:

    log Z_sharp(z,w)=sum_(m>=1) c_m Psi_m(z,w),

where

    c_m=(1/m)sum_(k|m,k odd) k mu(k)
       =(1/m)product_(p|m,p odd)(1-p).

The last formula factors the divisor sum over the odd radical.  Every factor
is nonzero, hence `c_m!=0`.  Moreover

    |c_m| <= product_(p|m,p odd)p / m <= 1.

Restricting to `w=qz` gives the promised P70-family identity

    log Z_orb(z,q)
      =sum_(m>=1) c_m 2(qz)^m
         /[1-(1+q^(2m))z^(2m)].

## 4. Bidisk divisor and normal continuation

Let `B^2={(z,w): |z|<1, |w|<1}` and

    H_m={(z,w) in B^2: z^(2m)+w^(2m)=1}.

The gradient of the defining polynomial is

    (2m z^(2m-1), 2m w^(2m-1)).

It cannot vanish on `H_m`, because simultaneous vanishing would force
`z=w=0`.  Thus every `H_m` is a smooth reduced hypersurface.

The family is locally finite.  Indeed, for a compact `K` in the bidisk choose
`r,s<1` with `|z|<=r` and `|w|<=s` on `K`.  For all sufficiently large `m`,

    |z^(2m)+w^(2m)| <= r^(2m)+s^(2m) < 1,

so `K` does not meet `H_m`.  Consequently `sum_m H_m` is a locally finite
effective analytic divisor.

Put `H=union_m H_m` and `Omega=B^2\H`.  On a compact `K subset Omega`, the
finitely many early denominators are bounded away from zero.  For all large
`m`, their modulus is at least `1/2`, while `|w|<=s<1`.  Using `|c_m|<=1`,

    |c_m Psi_m(z,w)| <= 4s^m.

The Weierstrass test proves normal convergence on `Omega`.  Hence

    L_sharp(z,w)=sum_(m>=1)c_m Psi_m(z,w)

is holomorphic there and agrees with the initial logarithmic germ.  Its
exponential is the resulting nonvanishing scalar continuation.

## 5. Fixed positive-weight roots and principal parts

Fix `q>0`.  In channel `m`, the denominator vanishes at

    alpha_(m,l)(q)=rho_m(q) exp(pi i l/m),  0<=l<2m,
    rho_m(q)=(1+q^(2m))^(-1/(2m)).

The function

    h(x)=log(1+q^(2x))/x

is strictly decreasing for `x>0`: after setting `y=q^(2x)`, the sign of its
derivative is the negative of

    (1+y)log(1+y)-y log y > 0.

Therefore `rho_m(q)` is strictly increasing in `m`.  In particular, roots
from two different channels cannot collide on a fixed positive-`q` fiber.
The radii tend to `min(1,q^(-1))`; no density or natural-boundary conclusion
is drawn here.

Let `alpha=alpha_(m,l)(q)` and `v=1-z/alpha`.  Since

    1-(1+q^(2m))z^(2m)=2mv+O(v^2),
    2(qz)^m=2(-1)^l(q rho_m)^m+O(v),

and `(q rho_m)^m=q^m/sqrt(1+q^(2m))`, normal convergence of the remaining
channels gives

    log Z_orb(z,q)
      = [c_m (-1)^l q^m/(m sqrt(1+q^(2m)))]
        /(1-z/alpha) + G_(m,l,q)(z),

where `G_(m,l,q)` is holomorphic near `alpha`.  The displayed coefficient is
nonzero, so exponentiation gives an essential singularity at each stated
root.  This is an isolated local classification; P75 does not classify the
joint intersections `H_m intersect H_j` for complex two-variable paths.

## 6. Claim boundary

**PROVED:** the exact weighted scalar-channel identity; the two-fugacity
lift; smoothness and local finiteness of the bidisk hypersurface divisor;
normal continuation off that divisor; strict fixed-positive-`q` radius
separation; and every local principal coefficient.

**NOT CLAIMED:** a dense singularity set or natural boundary; a Lind zeta for
`q!=1`; a transfer, nuclear, trace-class, or self-adjoint operator; rational
prime or von-Mangoldt semantics; arithmetic advance; or Route B.

The next scalar question is the boundary accumulation geometry of the full
complex root set.  It must be proved separately rather than inferred from a
finite plot.
