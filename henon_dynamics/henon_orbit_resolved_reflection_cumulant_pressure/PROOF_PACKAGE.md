# HCS-P69 proof package

## 1. Observable and energy

Let

    chi(s)=1{s[-1]=s[1]},
    S_n chi(s)=sum_(j mod n) chi(sigma^j s).

For odd n, multiplication by 2 permutes the cyclic coordinates and commutes
with reflection. Thus S_n chi becomes the nearest-neighbor equality energy
of another reflection-fixed word.

Write n=2m+1 and a_j=s[j] for 0<=j<=m. Reflection gives s[-j]=s[j]. The
boundary edge is always equal and every path edge occurs twice:

    S_n chi = 1 + 2 sum_(j=0)^(m-1) 1{a_j=a_(j+1)}.

## 2. Exact all-packet polynomial

With q an indeterminate, the transfer matrix is

    T(q) = [[q^2,1],[1,q^2]].

The all-palindrome weighted polynomial is

    F_(2m+1)(q)
      = q (1,1) T(q)^m (1,1)^T
      = 2q(1+q^2)^m.

Equivalently, the number of words with energy 1+2k is 2 binomial(m,k).

## 3. Exact primitive subtraction

If a reflection word of length n has least period d, its n-step energy is
(n/d) times its d-step energy. Therefore

    F_n(q)=sum_(d|n) E_d(q^(n/d)),

where E_d is the primitive polynomial. Dilation Möbius inversion gives

    E_n(q)=sum_(k|n) mu(k) F_(n/k)(q^k).

At q=1 this recovers the primitive count D_n.

## 4. Primitive pressure

Set q=e^(-s), with real fixed s. The k=1 term has exponential rate

    P_orb(s)=(1/2) log(1+e^(-2s)).

Every divisor term k>=3 has strictly smaller rate

    (1/(2k)) log(1+e^(-2ks)) < P_orb(s).

For s>=0 this follows by monotonicity; for s<0 it follows from
1+x^k < (1+x)^k for x>1. The number of divisors is subexponential, so

    lim_(n odd) (1/n) log E_n(e^(-s)) = P_orb(s).

## 5. Exact mean-field gap

P67 gives int chi d mu_B=1/2. P68's aggregate-mean pressure is

    P_mf(s)=(1/2)log2-s/2.

Hence

    P_orb(s)-P_mf(s)
      =(1/2)log((1+e^(-2s))/(2e^(-s)))
      =(1/2)log cosh(s).

It vanishes only at s=0 and is strictly positive otherwise. Moreover
P_orb''(0)=1/2, the asymptotic variance rate.

Finite strictness already holds for every odd n>=5: the palindrome with one
centered 1 has energy n-2, while the centered block 111 has energy n-4. Both
are primitive.

## 6. Claim boundary

PROVED: exact all-packet and primitive polynomials; nonlinear
orbit-resolved pressure; exact all-real-parameter mean-field gap.

REFUTED: replacing the exponential moment by the exponential of the mean for
nonzero s.

OPEN: the full orbit-resolved Euler product, its analytic boundary, rational
prime semantics, and an operator.
