# HCS-P68 proof package

## 1. Frozen input

For odd `n`, P64–P67 provide the primitive marked reflection packet `A_n`,

```text
D_n = |A_n| = sum_(d|n) mu(n/d) 2^((d+1)/2),
```

and the unique gauge-invariant packet mean

```text
b_n(f) = (n D_n)^(-1) sum_(omega in A_n) sum_(j mod n) f(sigma^j omega).
```

Thus `b_n(f+u-u o sigma)=b_n(f)` exactly.

## 2. Canonical packet Euler product

For bounded continuous `f` and parameters in an absolute-convergence disk,
define

```text
Z_f(z,s) = product_(n odd) (1-z^n exp(-s n b_n(f)))^(-D_n).
```

Absolute convergence follows from `D_n <= 2^((n+1)/2)` and
`|b_n(f)| <= ||f||_infinity`; for example it holds whenever
`sqrt(2)|z| exp(|s| ||f||_infinity) < 1`. Each factor is invariant under
continuous coboundaries because `b_n` is.

Expanding `-log(1-w)` gives the exact primitive/repetition ledger

```text
log Z_f = sum_(n odd) D_n sum_(r>=1)
          z^(nr) exp(-s r n b_n(f))/r,

[z^m] z partial_z log Z_f
  = sum_(n|m, n odd) n D_n exp(-s m b_n(f)).
```

This preserves primitive versus repeated packet bookkeeping. It does not
recover individual orbit weights: every marked element of one period is
assigned the same aggregate mean.

## 3. Unweighted convergence radius

Set `s=0`. Möbius inversion gives

```text
D(z) := sum_(n odd) D_n z^n
      = sum_(k odd) mu(k) 2 z^k/(1-2 z^(2k)).
```

Indeed, write `n=km`, interchange the divisor sum, and sum
`sum_(m odd) 2^((m+1)/2) z^(km)`. The `k=1` term has the partial fraction

```text
2z/(1-2z^2)
 = 1/[sqrt(2)(1-sqrt(2)z)]
   - 1/[sqrt(2)(1+sqrt(2)z)].
```

All `k>=3` terms are analytic in a neighborhood of the positive point
`R=2^(-1/2)`, so `D(z)` has there one simple pole with principal part
`1/[sqrt(2)(1-sqrt(2)z)]`. Positivity and the same formula give radius `R`.

## 4. Essential boundary theorem

The unweighted product obeys

```text
log Z_0(z) = D(z) + sum_(n odd) D_n sum_(r>=2) z^(nr)/r.
```

The repeated-term remainder is analytic for `|z|<2^(-1/4)`. Therefore near
the positive entropy boundary,

```text
log Z_0(z)
 = 1/[sqrt(2)(1-sqrt(2)z)] + G(z),
```

where `G` is analytic. Exponentiation yields

```text
Z_0(z) = exp(G(z))
         exp(1/[sqrt(2)(1-sqrt(2)z)]).
```

The first factor is analytic and nonzero; the second has an essential
singularity at `R`. Hence this product is not meromorphic at its entropy
boundary and cannot, without a new renormalization theorem, be promoted to a
standard Fredholm determinant there.

## 5. Lind-zeta firewall

The Lind zeta of a flip system is the group-action zeta summing fixed points
over **all** finite-index subgroups of the infinite dihedral group. The
Kim–Lee–Park formula contains a square root of the ordinary zeta and
additional odd/even flip fixed-point series. The present object uses only
the odd primitive reflection packet and the P67 aggregate mean. Equality is
therefore neither defined nor claimed.

## 6. Claim boundary

**PROVED:** canonical packet Euler product in its convergence disk; exact
repetition law; unweighted radius; essential boundary singularity.

**OPEN:** an orbit-resolved exponential-moment product, a relative Lind or
transfer determinant, rational-prime labels, von Mangoldt amplitudes, and an
operator.

**REFUTED AS AN IDENTIFICATION:** treating the aggregate packet product as
the full Lind zeta or as a meromorphic Fredholm determinant at `R`.
