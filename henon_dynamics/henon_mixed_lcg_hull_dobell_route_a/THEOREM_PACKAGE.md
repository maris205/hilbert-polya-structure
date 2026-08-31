# Theorem package

## Frozen owner

Let m be an integer at least two and let

    F(x) = a x + c (mod m)

act on Z/mZ.  One application of F is one unit of time.  Parameters are
residue classes a,c; no target table or fitted arithmetic datum enters.

Write rad(m) for the product of the distinct primes dividing m and set

    L(m) = lcm(rad(m), 4) if 4 divides m,
    L(m) = rad(m) otherwise.

## Theorem 1: full-period classification

The following are equivalent.

1. F is one cycle of length m.
2. gcd(c,m)=1; every prime p dividing m also divides a-1; and, if 4 divides
   m, then 4 divides a-1.

Consequently exactly phi(m)m/L(m) residue pairs (a,c) give full period.

### Necessity

If F is one m-cycle, every equivariant quotient is transitive.  On Z/pZ,
an affine map with a not congruent to one has a fixed point (or is not a
permutation), so it cannot be a p-cycle.  Hence a is one modulo every p
dividing m.  The induced translation must have nonzero increment, giving
gcd(c,m)=1.

If 4 divides m, the quotient modulo four must be a four-cycle.  Here a and c
are odd.  Were a congruent to three modulo four, then

    F squared(x) = a squared x + c(a+1) = x (mod 4),

contradicting period four.  Thus a is one modulo four.

### Sufficiency

Fix p to exponent e exactly dividing m and put

    S_n = 1+a+...+a^(n-1),   d_x = (a-1)x+c.

The iterate identity gives F^n(x)-x=S_n d_x.  Since p divides a-1 and does
not divide c, d_x is a p-adic unit for every x.  For odd p, the elementary
lifting-the-exponent identity gives v_p(S_n)=v_p(n).  For p=2 and e at least
two, the mod-four condition gives the same equality.  When e=1, oddness of
a,c directly gives exact period two.  Therefore a state returns modulo p^e
exactly when p^e divides n.

CRT now says a state returns modulo m exactly when every p^e dividing m
divides n, equivalently when m divides n.  Every state has period m, so the
m-point set is one cycle.

The multiplier congruences specify one residue class modulo L(m), hence
m/L(m) multipliers.  There are phi(m) unit increments, proving the parameter
count.

## Corollary 2: orbit, zeta, and Koopman ledgers

For an admissible pair:

- there is exactly one primitive orbit, of length m;
- the number of fixed points of F^n is m if m divides n and zero otherwise;
- the source Artin--Mazur zeta is

      exp(sum_{n>=1} #Fix(F^n)t^n/n) = 1/(1-t^m);

- on l2(Z/mZ), composition with F is a unitary m-cycle permutation whose
  eigenvalues are all m-th roots of unity once each and whose characteristic
  polynomial is u^m-1.

These formulas classify the source map.  They do not define a target
determinant or a Hilbert--Polya operator.

## Boundary and stopping theorem

Failure of unit increment is visible on a prime quotient.  Failure of a prime
multiplier congruence leaves a fixed point on that quotient.  Failure of the
mod-four condition makes the square identity modulo four.  These are exact
obstructions, but a general nonadmissible cycle decomposition is outside the
claim.

The strict Route-A tuple is

    (A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL,
     A4_NATURAL_QUANTIZATION).

Prime-power quotient structure is intrinsic, but there is no rational-prime
primitive-orbit dictionary, log-prime clock, target divisor, global target
analytic structure, or target operator identification.  The overall verdict
is ROUTE_A_EXPLORATORY and Route B is not authorized.
