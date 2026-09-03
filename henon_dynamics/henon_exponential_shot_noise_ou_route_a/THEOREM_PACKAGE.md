# Theorem package — exponential shot-noise OU process

## Frozen process

Let \(\gamma,\kappa,\beta>0\).  Let \(N\) be a Poisson process of rate \(\kappa\), with jump times \(T_j\), and let \(Y_j\) be iid exponential random variables of rate \(\beta\), independent of \(N\).  On \([0,\infty)\), define
\[
dX_t=-\gamma X_t\,dt+dJ_t,\qquad J_t=\sum_{T_j\leq t}Y_j.
\]

## Main theorem

For every \(x\geq0\), \(t,s\geq0\), and \(\alpha=\kappa/\gamma\):

1. Pathwise,
   \[
   X_t=e^{-\gamma t}x+\sum_{T_j\leq t}e^{-\gamma(t-T_j)}Y_j.
   \]
   Consequently
   \[
   \mathbb E_x e^{-sX_t}=e^{-se^{-\gamma t}x}
   \left(\frac{\beta+se^{-\gamma t}}{\beta+s}\right)^\alpha.
   \]
2. The unique invariant probability is \(\operatorname{Gamma}(\alpha,\text{rate }\beta)\).  Synchronous coupling gives, for every \(p\geq1\),
   \[
   W_p(P_t(x,\cdot),P_t(y,\cdot))=e^{-\gamma t}|x-y|.
   \]
3. In stationarity,
   \[
   \mathbb E X^n=(\alpha)_n/\beta^n,\quad
   \operatorname{cum}_n(X)=\alpha(n-1)!/\beta^n,\quad
   \operatorname{Cov}(X_t,X_0)=\alpha\beta^{-2}e^{-\gamma|t|}.
   \]
4. The generator
   \[
   Lf=-\gamma x f'(x)+\kappa\int_0^\infty\beta e^{-\beta y}[f(x+y)-f(x)]\,dy
   \]
   preserves \(\mathcal P_m=\operatorname{span}(1,x,\ldots,x^m)\).  Its restriction to \(\mathcal P_m\) has exactly the simple eigenvalues \(0,-\gamma,\ldots,-m\gamma\) and therefore a unique monic eigenpolynomial at each degree after normalization.  This statement is only about each finite filtration; it says nothing about the full \(L^2\) spectrum, spectral completeness, normality, or reversibility.

## Proof

Variation of constants across the finitely many jumps on a compact time interval gives the pathwise formula.  The Laplace functional of a marked Poisson process then gives
\[
\log\mathbb E e^{-s\sum_{T_j\leq t}e^{-\gamma(t-T_j)}Y_j}
=\kappa\int_0^t\left(\frac{\beta}{\beta+se^{-\gamma u}}-1\right)du
=\frac\kappa\gamma\log\frac{\beta+se^{-\gamma t}}{\beta+s},
\]
which proves the transform and, by direct multiplication with two decay factors, the semigroup law.

Letting \(t\to\infty\) gives \((\beta/(\beta+s))^\alpha\), the Gamma transform.  It is invariant by the same transform identity.  If two paths use the same jumps, their difference is deterministically \(e^{-\gamma t}(x-y)\).  Thus the translation coupling gives the upper Wasserstein bound.  The mean difference and Jensen's inequality give the matching lower bound.  This contraction proves uniqueness among invariant probabilities with finite first moment; any invariant probability has the displayed Laplace transform by applying invariance and sending \(t\to\infty\), so uniqueness is unrestricted.

Expanding the logarithm of the Gamma transform yields the cumulants, and differentiating yields the rising-factorial moments.  Moreover
\[
\mathbb E[X_t\mid X_0]=e^{-\gamma t}X_0+\frac{\kappa}{\gamma\beta}(1-e^{-\gamma t}),
\]
so stationary centering gives the covariance for positive lags; stationarity and symmetry of scalar covariance supply \(|t|\).

Finally, exponential marks satisfy \(\mathbb EY^r=r!/\beta^r\), hence
\[
Lx^n=-n\gamma x^n+
\kappa\sum_{j=0}^{n-1}\binom nj\frac{(n-j)!}{\beta^{n-j}}x^j.
\]
Thus every \(\mathcal P_m\) is invariant and the monomial matrix is triangular with pairwise distinct diagonal \(0,-\gamma,\ldots,-m\gamma\).  Elementary finite-dimensional linear algebra proves the exact simple spectrum and the monic eigenpolynomials.  No closure over \(m\) is taken.

## Boundary atlas

- \(\kappa=0,\gamma>0\): deterministic decay and unique invariant \(\delta_0\).
- \(\gamma=0,\kappa>0\): a nondecreasing compound-Poisson subordinator and no invariant probability.
- \(\gamma=\kappa=0\): the process is static and every initial law is invariant.
- \(\beta=0\): invalid, because there is no exponential probability law with rate zero; \(\beta\to\infty\) is only a weak limit.
- Only finite polynomial restrictions are spectrally classified.

## Proof/evidence boundary

The theorem is analytic.  The finite JSON grid is an exact convention and regression certificate, not a proof of the all-time or all-degree statement.
