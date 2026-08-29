# Frozen theorem contracts — P107–P111

## P107: annihilator–power ideal dynamics

For `r>=2` on ideals of `Z/NZ`, with `T_r(I)=Ann(I)^r`, the paper must prove:

1. the prime-power coordinate map `e -> min(a,r(a-e))`;
2. the pre-clipping deviation law `Delta -> -r Delta`;
3. the endpoint two-cycle and the interior fixed-point resonance exactly when
   `(r+1)|a`;
4. the pointwise parity-threshold depth formula and closed depth CDF;
5. CRT product formulas for transient layers, fixed points, two-cycles, and
   the Artin–Mazur zeta function.

Routes: valuation/CRT proof; literal divisor-ideal gcd arithmetic.

## P108: capped Fibonacci dynamics

For `T_a(x,y)=(y,min(a,x+y))` on `{0,...,a}^2`, the paper must prove:

1. the exact capped Fibonacci iterate for every time;
2. the two fixed attractors and absence of every other cycle;
3. the pointwise half-plane hitting time and exact lattice-point CDF;
4. sharp maximum depth `1+min{k:F_k>=a}` and its attaining state;
5. the triangular one-step image, every fibre size, and all Garden-of-Eden
   states.

Routes: nonnegative-integer clipping/Fibonacci induction; direct inverse-equation and
literal-orbit control.

## P109: regular-nilpotent image dynamics

For a regular nilpotent block `N` on `F_q^d` and `T(U)=N(U)` on the full
subspace lattice, the paper must prove:

1. `T^t(U)=N^t(U)` and unique absorption at zero;
2. `#{U:depth(U)<=t}=sum_r [t r]_q`;
3. the exact joint transition count
   `[t,r-s]_q [d-t,s]_q q^((t-r+s)s)`;
4. sharp depth `d`, unique recurrence, and zeta `(1-z)^-1`;
5. the stated `(q,d)` recovery boundary, including `d=1`.

Routes: prescribed intersection with `ker N^t`; exhaustive unique-RREF
subspace generation and literal Jordan shift.

## P110: cyclic shift–join partition dynamics

For `J(pi)=pi join rho(pi)` on partitions of `Z/nZ`, the paper must prove:

1. `J^t(pi)=join_{j=0}^t rho^j(pi)` and the subgroup-coset endpoint;
2. recurrent equals fixed, with `tau(n)` fixed partitions and zeta
   `(1-z)^(-tau(n))`;
3. the exact order-`h` basin formula by divisor Möbius inversion of Bell
   powers;
4. sharp maximum depth `max(0,n-2)`;
5. for `n>=3`, deepest states are exactly primitive two-block atoms and
   number `n phi(n)/2`.

Routes: translated equivalence graphs; subgroup incidence inversion and full
restricted-growth-string enumeration.

## P111: positive Heisenberg word-area cocycle

For iid positive generators `X=I+E_12`, `Y=I+E_23`, the paper must prove:

1. the exact finite-word matrix normal form and conditional Gaussian-
   binomial area law;
2. exact biased mean and variance for the central coordinate;
3. the strong law and explicit `n^(3/2)` CLT after isolating the linear
   projection;
4. the norm-growth exponent `2` for `0<p<1` versus `1` at the endpoints;
5. the `n^2` annealed pressure kink `theta/4` for positive `theta` and zero
   otherwise, with endpoint branches explicit.

Routes: literal matrix-word induction; binary word statistics, triangular-
array limit theory, extremal ordered words, and independent finite-word DP.

All contracts are internal.  Classical components receive zero novelty
credit and external release remains **HOLD**.
