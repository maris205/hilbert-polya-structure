# Proof package

## Claim

Let `T_2` be the single edge `{1,2}`.  Given `T_n`, add vertex `n+1` and join it to one old vertex `v`, chosen with probability `d_v(n)/[2(n-1)]`.  There are no self-loops or multiple edges.  Write `D_i(n)=d_i(n)`, `N_k(n)=#{v<=n:D_v(n)=k}`, and `s_i=2` for `i=1,2`, while `s_i=i` for `i>=3`.

For `r>=1` and `n>=s_i`,

`E[D_i(n)^{overline r}] = r! Gamma(n-1+r/2) Gamma(s_i-1) / [Gamma(n-1) Gamma(s_i-1+r/2)]`.

Moreover `D_i(n)/sqrt(n)` converges almost surely and in every finite `Lp` to a moment-determinate random variable `Z_i` satisfying

`E[Z_i^r]=r! Gamma(s_i-1)/Gamma(s_i-1+r/2)`.

For every fixed `k>=1`,

`N_k(n)/n -> p_k=4/[k(k+1)(k+2)]`

in `L2`.

## Status

PROVABLE AS STATED.

## Assumptions and notation

- Time `n` is the number of vertices, so the total degree is exactly `2(n-1)`.
- `x^{overline r}=x(x+1)...(x+r-1)` and `x^{overline 0}=1`.
- A fixed vertex and a degree-count population are distinct objects.
- All asymptotic assertions hold with `i` or `k` fixed before `n` tends to infinity.

## Dependency map

1. One Bernoulli degree increment gives the rising-factorial multiplier.
2. Product iteration gives the gamma quotient and a normalized nonnegative martingale.
3. Higher rising moments give uniform `Lp` bounds; gamma asymptotics transfer the martingale limit to `D_i(n)/sqrt(n)`.
4. Polynomial comparison between powers and rising powers gives every limit moment; Carleman's criterion gives moment determinacy.
5. One attachment changes `N_k` by a bounded amount and gives a lower-triangular drift recursion.
6. The stationary drift equation gives `p_k`; a componentwise second-moment induction gives `L2` convergence.

## Proof

### 1. Fixed-vertex factorial closure

Conditionally on `T_n`, a fixed extant vertex of degree `d` receives the new edge with probability `d/[2(n-1)]`.  Since

`(d+1)^{overline r}-d^{overline r}=(r/d)d^{overline r}`,

we have

`E[D_i(n+1)^{overline r}|T_n]=(1+r/[2(n-1)])D_i(n)^{overline r}`.

At time `s_i`, every vertex under the frozen convention has degree one, hence `D_i(s_i)^{overline r}=r!`.  Iterating and using the gamma product proves the displayed exact moment formula.

For `r=1`, put

`a_{s,n}=prod_{t=s}^{n-1}(1+1/[2(t-1)])`.

Then `M_i(n)=D_i(n)/a_{s_i,n}` is a nonnegative martingale.  For each integer `q>=1`, the exact formula at order `q` and the inequality `D^q<=D^{overline q}` show `sup_n E[M_i(n)^q]<infinity`, because both numerator and `a_{s_i,n}^q` have order `n^{q/2}`.  Thus `M_i(n)` converges almost surely and in every finite `Lp` (choose an integer `q>p` and use uniform integrability).  Since

`a_{s,n}/sqrt(n) -> Gamma(s-1)/Gamma(s-1/2)`,

the same modes of convergence hold for `D_i(n)/sqrt(n)`; call its limit `Z_i`.

For fixed `r`, `D^r-D^{overline r}` is a polynomial of degree at most `r-1`.  The exact bounds at all lower orders therefore imply, after division by `n^{r/2}`, that its expectation tends to zero.  Gamma asymptotics in the exact rising-moment formula give

`E[Z_i^r]=r! Gamma(s_i-1)/Gamma(s_i-1+r/2)`.

Uniform integrability follows from the already established order `r+1` bound.  Finally

`m_{2r}^{-1/(2r)} = [(2r)! Gamma(s_i-1)/Gamma(s_i-1+r)]^{-1/(2r)}`

is bounded below by a positive constant times `r^{-1/2}` by Stirling's formula.  Its sum diverges, so Carleman's criterion makes the law of `Z_i` moment determinate.

### 2. Degree-count drift and `L2` law

Let `Delta N_k=N_k(n+1)-N_k(n)` and set `N_0=0`.  The new leaf contributes to `N_1`; selecting a degree-`k-1` vertex moves it into class `k`, while selecting a degree-`k` vertex moves it out.  Therefore

`E[Delta N_k|T_n]=1_{k=1}+[(k-1)N_{k-1}(n)-kN_k(n)]/[2(n-1)]`.

Also `|Delta N_k|<=1`.  The equilibrium equation

`p_k=1_{k=1}+[(k-1)p_{k-1}-kp_k]/2`

gives `p_1=2/3` and `p_k=(k-1)p_{k-1}/(k+2)`, hence

`p_k=4/[k(k+1)(k+2)]`.

For completeness, define the centered innovation

`xi_{k,n+1}=Delta N_k-E[Delta N_k|T_n]`,

so `E[xi_{k,n+1}|T_n]=0` and `|xi_{k,n+1}|<=2`.  Put `U_{k,n}=N_k(n)-np_k`.  Direct substitution yields

`U_{k,n+1}=(1-k/[2(n-1)])U_{k,n}+[(k-1)/(2(n-1))]U_{k-1,n}+(p_k-1_{k=1})/(n-1)+xi_{k,n+1}`.

We prove `E[U_{k,n}^2]=O(n)` by induction on `k`.  Fix `k` and begin at a finite `n_0(k)` large enough that all coefficients below are nonnegative; the omitted initial segment is absorbed into the final constant.  Write

`a_n=1-k/[2(n-1)]`, `b_n=(k-1)/[2(n-1)]`, and `r_n=(p_k-1_{k=1})/(n-1)`.

After conditioning, the cross term containing `xi` vanishes and `E[xi^2|T_n]<=4`, so

`E[U_{k,n+1}^2|T_n]=(a_n U_{k,n}+b_n U_{k-1,n}+r_n)^2+E[xi^2|T_n]`.

For `k=1`, the `b_n` term is absent.  Use Young's inequality on the cross term with parameter `eta/n`, where `0<eta<k/2` is fixed.  Since `a_n^2=1-k/n+O_k(n^-2)`, for all `n>=n_0(k)` the coefficient of `U_{k,n}^2` is at most `1-c_k/n` for some `c_k>0`.  This gives

`E U_{1,n+1}^2 <= (1-c_1/n) E U_{1,n}^2+C_1`.

For the induction step, assume `E[U_{k-1,n}^2]<=C_{k-1}n`.  Young's inequality gives explicitly

`2|a_n U_{k,n}(b_n U_{k-1,n}+r_n)| <= (eta/n)U_{k,n}^2 + (n/eta)(b_n U_{k-1,n}+r_n)^2`.

Now `b_n=O_k(1/n)` and `r_n=O_k(1/n)`, so

`E[(b_n U_{k-1,n}+r_n)^2] <= 2b_n^2 C_{k-1}n+2r_n^2=O_k(1/n)`.

Multiplication by `n/eta` contributes only `O_k(1)`.  The uncrossed forcing square is itself `O_k(1/n)`, and the innovation variance is at most four.  Combining these estimates with `a_n^2+eta/n<=1-c_k/n` yields, after enlarging constants,

`E U_{k,n+1}^2 <= (1-c_k/n) E U_{k,n}^2+C_k`.

Induction on `n` now gives `E U_{k,n}^2<=C'_k n`.  Consequently

`E[(N_k(n)/n-p_k)^2]<=C'_k/n -> 0`,

which is the claimed `L2` convergence.  The masses also satisfy `sum_k p_k=1` and `sum_k k p_k=2`, by telescoping partial fractions, matching the vertex and degree conservation laws.

## Boundary and nonclaim audit

- At `n=2`, vertices `1,2` are symmetric roots of degree one; for `i>=3`, birth time is `s_i=i`.
- A newborn at time `n` has degree one; formulas are not evaluated before birth.
- For a fixed finite tree, `N_k(n)=0` when `k>n-1`.
- No statement is made about the maximum degree, joint hub limits, finite-size tail uniformity in `k`, or an `m>1` attachment process.
- Finite exact enumeration is not an asymptotic proof.

## Route-A boundary

The tuple is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` and the overall verdict is `ROUTE_A_REJECTED`.  The stochastic attachment clock has no rational-prime carrier, primitive-orbit ledger, dynamical zeta/divisor bridge, target functional equation, or natural quantization.  Route B is locked.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
