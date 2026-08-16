# HCS-P76 proof package

## Definitions and inherited identity

For `q>0`, P70 and the weighted scalar regrouping give

    log Z_orb(z,q)=sum_(m>=1)c_m Psi_m(z,q),
    Psi_m(z,q)=2(qz)^m/[1-(1+q^(2m))z^(2m)],

where

    c_m=(1/m)sum_(k|m,k odd)k mu(k)
       =(1/m)product_(p|m,p odd)(1-p).

Every `c_m` is nonzero.

## Theorem 1: strict moving-radius ladder

The poles of channel `m` have modulus

    rho_m(q)=(1+q^(2m))^(-1/(2m)).

Write `||(1,q)||_p=(1+q^p)^(1/p)`.  The `L^p` norm of a vector with two
positive coordinates is strictly decreasing in `p`.  Hence

    rho_m(q)=||(1,q)||_(2m)^(-1)

is strictly increasing in `m`.  Moreover,

    lim_(m->infinity)rho_m(q)=1/max(1,q)=min(1,q^(-1)).

Thus no two different channels have a pole on the same circle.

## Theorem 2: full complex essential divisor

All roots of the channel denominator are

    alpha_(m,k)(q)=rho_m(q) exp(pi i k/m),  0<=k<2m.

Put `v=1-z/alpha_(m,k)`.  Since

    alpha_(m,k)^m=(-1)^k/[sqrt(1+q^(2m))],

direct expansion gives

    Psi_m(z,q)
      =(-1)^k q^m/[m sqrt(1+q^(2m))] * 1/v + O(1).

Every other channel is holomorphic near this root because its radius is
different.  Therefore

    log Z_orb(z,q)
      =c_m(-1)^k q^m/[m sqrt(1+q^(2m))]
       * 1/(1-z/alpha_(m,k)) + holomorphic.

The coefficient is nonzero, so exponentiation gives an essential
singularity at every `alpha_(m,k)`.

## Theorem 3: natural-boundary circle

The arguments `pi k/m`, `0<=k<2m`, form a uniform mesh of maximum gap
`pi/m`.  As `m` tends to infinity, the mesh becomes dense and the radii tend
to

    L(q)=min(1,q^(-1)).

Consequently every point of `|z|=L(q)` is the limit of genuine essential
singularities from inside the circle.  Suppose a meromorphic continuation
existed on a neighborhood of one boundary point.  That neighborhood would
contain infinitely many of these essential singularities accumulating at an
interior point of the neighborhood, contradicting the discreteness of the
singular set of a meromorphic function.  Thus no boundary point admits a
meromorphic neighborhood.  The circle is a natural boundary for this
explicit punctured continuation.

## Three regimes

- `0<q<1`: the singular circles accumulate at the unit circle;
- `q=1`: the P72 radii accumulate at the unit circle;
- `q>1`: the accumulation circle moves inward to `|z|=q^(-1)`.

The identity `rho_m(q)=q^(-1)rho_m(q^(-1))` relates the first and third
regimes.

## Claim firewall

The natural-boundary statement is for the unrenormalized scalar-channel
continuation.  Multiplying by an all-channel counterterm produces a
different analytic object and is not covered.  No weighted Lind source,
transfer operator, self-adjoint operator, rational-prime labeling,
von-Mangoldt amplitude, explicit formula, or Route-B theorem is proved.
