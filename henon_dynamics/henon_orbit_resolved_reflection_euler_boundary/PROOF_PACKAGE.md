# HCS-P70 proof package

## 1. Orbit-resolved product

For q>0 define

    Z_orb(z,q)=product_(n odd) product_(omega in A_n)
               (1-z^n q^(S_n chi(omega)))^(-1).

P69's primitive polynomial is

    E_n(q)=sum_(omega in A_n) q^(S_n chi(omega)).

Absolute expansion gives

    log Z_orb(z,q)=sum_(r>=1) E(z^r,q^r)/r,
    E(z,q)=sum_(n odd)E_n(q)z^n,

and

    [z^m] z partial_z log Z_orb
      =sum_(n|m,n odd) n E_n(q^(m/n)).

This is the exact primitive/repetition law with individual orbit weights.

## 2. Two-variable primitive generating series

P69 gives F_(2m+1)(q)=2q(1+q^2)^m and
E_n(q)=sum_(k|n)mu(k)F_(n/k)(q^k). Therefore

    E(z,q)=sum_(k odd) mu(k)
           2(qz)^k/[1-(1+q^(2k))z^(2k)].

The k=1 denominator vanishes at

    R(q)=(1+q^2)^(-1/2).

For every odd k>=3,

    (1+q^(2k))^(1/k) < 1+q^2,

by the strict binomial inequality. Hence all other k terms are analytic near
the positive point R(q).

## 3. Repetition terms and boundary type

The r-th term E(z^r,q^r)/r has first positive singular radius

    (1+q^(2r))^(-1/(2r)).

For r>=2 it is strictly larger than R(q). The k=r=1 term has partial
fraction principal part

    [q/sqrt(1+q^2)]/[1-sqrt(1+q^2)z].

Thus

    log Z_orb(z,q)
      = q/[sqrt(1+q^2)(1-sqrt(1+q^2)z)] + G_q(z),

with G_q analytic near R(q). Exponentiation proves an essential singularity
for every q>0.

## 4. Exact mean-field radius shift

P68's aggregate mean pressure for chi is

    P_mf(s)=(1/2)log2-s/2.

With q=e^(-s), its radius is R_mf(q)=(2q)^(-1/2). P69/P70 give

    R(q)/R_mf(q)
      =sqrt(2q/(1+q^2))
      =1/sqrt((q+q^(-1))/2).

By arithmetic--geometric mean, this ratio is at most one, with equality only
at q=1. Thus mean-field weighting predicts a strictly too-large disk for
every nontrivial positive weight.

## 5. Claim boundary

PROVED: full orbit-resolved product in its disk; exact log derivative; moving
boundary; essential singularity; strict mean-field radius shift.

OPEN: a relative Lind/transfer counterterm, arithmetic labels, meromorphic
continuation after renormalization, and an operator.
