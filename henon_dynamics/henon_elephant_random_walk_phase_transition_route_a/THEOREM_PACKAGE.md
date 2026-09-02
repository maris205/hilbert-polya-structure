# Theorem package

Let `X_1` be `+1` with probability `q` and `-1` otherwise. Given `X_1,...,X_n`, choose `K` uniformly from `{1,...,n}` and put `X_{n+1}=X_K` with probability `p`, otherwise `X_{n+1}=-X_K`. Set `S_n=sum_{j<=n}X_j`, `a=2p-1`, `b=2q-1`, and

`G_n(c)=prod_{j=1}^{n-1}(1+c/j)`.

## Boundary-complete theorem

1. `P(X_{n+1}=1 | F_n)=(1+aS_n/n)/2`, hence `E[X_{n+1}|F_n]=aS_n/n`.
2. `E S_n=bG_n(a)`. Moreover

   `E S_n^2=(2aG_n(2a)-n)/(2a-1)` if `a != 1/2`, and `E S_n^2=nH_n` if `a=1/2`.

3. If `p>0`, `S_n/G_n(a)` is a martingale. If `p=0`, then `S_2=0` and `((n-1)S_n)_{n>=2}` is a martingale.
4. If `p<3/4`, `S_n/sqrt(n)` converges in law to `N(0,1/(3-4p))`. If `p=3/4`, `S_n/sqrt(n log n)` converges in law to `N(0,1)`.
5. If `p>3/4`, `S_n/n^(2p-1)` converges almost surely and in `L^4` to `L`. Its first four moments are

   `E L=b/Gamma(2p)`,

   `E L^2=1/((4p-3)Gamma(4p-2))`,

   `E L^3=2pb/((2p-1)(4p-3)Gamma(6p-3))`,

   `E L^4=6(8p^2-4p-1)/((8p-5)(4p-3)^2 Gamma(8p-4))`.

6. At `p=1`, `S_n=nX_1`; thus `L=X_1`, deterministic when `q=0` or `1` and two-point when `0<q<1`.

## Proof skeleton

Conditioning on the recalled index gives item 1. Then

`E[S_{n+1}|F_n]=(1+a/n)S_n`

and

`E[S_{n+1}^2|F_n]=(1+2a/n)S_n^2+1`.

Iteration gives the first product. Variation of constants gives the second; at `2a=1`, the quotient sum is harmonic. Dividing the conditional mean by `G_{n+1}(a)=(1+a/n)G_n(a)` proves the generic martingale. When `a=-1`, direct substitution gives `E[nS_{n+1}|F_n]=(n-1)S_n`, while the first update forces `S_2=0`.

For the limit laws, center the normalized martingale and use the standard martingale central limit theorem: bounded increments give Lindeberg, while the predictable quadratic-variation sum is asymptotic to the convergent/divergent power sum whose exponent changes sign at `a=1/2`. At equality it grows logarithmically. For `a>1/2`, the normalized martingale has summable fourth-moment increments and hence converges in `L^4`; multiplying by `G_n(a)/n^a -> 1/Gamma(a+1)` gives `L`. Iterating the exact moment recurrences through order four yields the displayed constants. These asymptotic steps follow the cited martingale treatment; finite enumeration is not their proof.

## Scope

Route-A tuple: `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`. Overall: `ROUTE_A_REJECTED`. Route B is locked. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
