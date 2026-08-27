# Theorem package

Let `A` have invariant factors `f_1|...|f_r` over `F_q`.  Write
`f_i=X^{e_i}g_i`, with `g_i(0) != 0`, and put
`F_n=q^(sum_i deg gcd(f_i,X^n-1))`.

## Main theorem

For every `n>=1`:

1. `|Fix(A^n)|=F_n`.
2. The periodic points form an `A`-invariant vector subspace of dimension
   `sum_i deg g_i`; the maximal preperiod is `max_i e_i`.
3. The number of points of least period `n` is
   `P_n=sum_{d|n} mu(n/d)F_d`, and the number of `n`-cycles is `C_n=P_n/n`.
4. `zeta_A(z)=product_{n>=1}(1-z^n)^(-C_n)`.
5. For `U_A phi=phi o A` on all complex functions on `V`,
   `chi_U(X)=X^(|V|-|Per(A)|) product_n (X^n-1)^(C_n)`.

## Proof ledger

On `F_q[X]/(f_i)`, multiplication by `X^n-1` has kernel dimension
`deg gcd(f_i,X^n-1)`; direct sums prove (1).  Coprime primary decomposition
splits the nilpotent `X`-primary part from the invertible part, proving (2).
Möbius inversion and orbit division prove (3), and the standard exponential
fixed-point identity proves (4).  Order a functional-graph component by its
cycle followed by tree vertices.  The composition matrix is block triangular;
the cycle block contributes `X^d-1` and every tree vertex contributes `X`,
proving (5).  The argument includes inseparable `X^n-1` without a square-free
assumption.

The registered route record is exactly `overall=ROUTE_A_REJECTED` with
`route_b_invocation_allowed=false`.
