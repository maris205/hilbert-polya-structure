# Research question

For arbitrary `A in End_Fq(V)`, can the complete finite dynamics be read
directly from the invariant factors, including noninvertible and inseparable
cases, and can that exact result pass a strict Route-A audit without importing
arithmetic meaning?

The answer to the first clause is yes.  If `f_1|...|f_r` are the invariant
factors, then

`|Fix(A^n)| = q^(sum_i deg gcd(f_i,X^n-1))`.

The `X`-primary exponents determine the transient part, Möbius inversion gives
exact periods, and functional-graph components give both zeta and the
full-function Koopman characteristic polynomial.  The answer to the Route-A
clause is negative: none of these identities supplies a target prime-power
carrier or target spectral operator.
