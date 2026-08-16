# HCS-P72 proof package

## Definitions

Let

    Phi(x) = 2x/(1-2x^2),
    E(t) = sum_{k odd} mu(k) Phi(t^k),
    log Z_orb(t,1) = sum_{r>=1} E(t^r)/r.

The first equality is the odd reflection-word generating function followed
by primitive dilation Möbius inversion; the second is the Euler repetition
identity proved and certified in P68--P70.

## Theorem 1: exact regrouping

For `|t|<2^(-1/2)`, absolute convergence permits grouping by `m=kr`:

    log Z_orb(t,1) = sum_{m>=1} c_m Phi(t^m),
    c_m = (1/m) sum_{k|m, k odd} k mu(k).

The divisor sum factors over the odd radical:

    c_m = (1/m) product_{p|m, p odd} (1-p).

Every factor is nonzero, so `c_m != 0` for all `m`.

## Theorem 2: exact relative continuation

Put `u=1-sqrt(2)t`. P71's counterterm is

    C_rel(t)=u^(1/2) exp(-3/(4u)) zeta_flip(t)/Z_orb(t,1).

The source formula and the first channel give the exact cancellation

    (1/2)log u + log zeta_flip(t) - 3/(4u) - Phi(t)
      = H_rel(u),
    H_rel(u)=-(1/2)log(2-u)-3(2u-3)/[4(u-2)].

Therefore

    log C_rel(t)=H_rel(1-sqrt(2)t)-sum_{m>=2}c_m Phi(t^m).

Since `|c_m|<=1` and `Phi(t^m)=O_K(r^m)` on compact punctured sets
`|t|<=r<1`, the sum is normally convergent there.

## Theorem 3: infinite positive essential ladder

For `rho_m=2^(-1/(2m))` and `v=1-t/rho_m`,

    Phi(t^m)=1/[sqrt(2)m v]+O(1).

At the positive point `rho_m`, no channel `j != m` has a vanishing
denominator. Thus for every `m>=2`,

    log C_rel(t)=-c_m/[sqrt(2)m(1-t/rho_m)]+holomorphic.

Because `c_m != 0`, exponentiation gives an essential singularity.
Furthermore `rho_m` increases strictly to one.

## Corollary and firewall

`C_rel` is not meromorphic on the unit disk and hence cannot equal a
finite-dimensional determinant or a quotient of holomorphic trace-class
Fredholm determinants there. This does not exclude a punctured-domain,
non-trace-class, or infinitely renormalized operator. No rational-prime
semantics or Route-B result follows.
