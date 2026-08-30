# Theorem package

## Model and jump skeleton

Let (X_t>0) rise with (dot X_t=a>0).  Jumps occur at rate (rho X_t),
(rho>0), and send (X\mapstobeta X), (0<beta<1).  If (Y_n) is the
pre-jump value and (T_{n+1}) the next waiting time, then
\[
 rho(beta Y_nT_{n+1}+aT_{n+1}^2/2)=E_{n+1},\quad E_{n+1}\sim\mathrm{Exp}(1),
 \qquad Y_{n+1}=beta Y_n+aT_{n+1}.
\]

### Theorem 1 (square-affine recurrence)

Completing the square gives
\[
 Y_{n+1}^2=beta^2Y_n^2+\frac{2a}{rho}E_{n+1}. \tag{1}
\]

*Proof.* Expand ((beta Y_n+aT)^2-beta^2Y_n^2) and substitute the
integrated hazard.  The coefficient is (2a/rho), including the increase
rate (a). ∎

### Theorem 2 (perpetuity, uniqueness, and q-product)

With (Z_n=Y_n^2), synchronous coupling gives
(|Z_n-Z'_n|=beta^{2n}|Z_0-Z'_0|).  Hence the perpetuity
\[
 Z_\infty=\frac{2a}{rho}\sum_{j\ge0}beta^{2j}E_{-j}
\]
converges almost surely and is the unique stationary jump-chain law; every
finite initial (Z_0) converges to it.  Its source-local Laplace transform is
\[
 \psi(s)=\prod_{j\ge0}\left(1+\frac{2a}{rho}beta^{2j}s\right)^{-1}. \tag{2}
\]

The release records exact rational prefixes and spot values of (2).  This is
not an Euler product or a target determinant.

For the continuous-time stationary law, writing
(\varphi(s)=\mathbb E[e^{-sX}]) and applying the generator to
(e^{-sx}) gives the independent functional identity
\[
 \varphi'(s)-\varphi'(beta s)=\frac{a}{rho}s\,\varphi(s). \tag{3}
\]
This is a source-local Laplace-generator equation; it is not a target
continuation or functional equation.

### Theorem 3 (all squared moments)

Writing (c=2a/rho), (m_k=\mathbb E[Z^k]), (m_0=1),
\[
 (1-beta^{2k})m_k=\sum_{j=0}^{k-1}\binom{k}{j}beta^{2j}c^{k-j}(k-j)!m_j. \tag{4}
\]
The right side is rational for the frozen grid, so all recorded squared
moments are exact.

### Theorem 4 (generator and occupation moments)

For a stationary continuous-time law with (M_m=\mathbb E[X^m]), the generator
(Lf=a f'+rho x[f(beta x)-f(x)]) yields
\[
 rho(1-beta^m)M_{m+1}=amM_{m-1},\qquad m\ge1. \tag{5}
\]
Thus (M_0=1), (M_1=\mu), and every (M_m) is an exact affine expression in
(mu).  Let (pi) be the stationary pre-jump law.  The stationary
Markov-renewal/Palm reward formula is
\[
 M_m=\frac{1-beta^{m+1}}{(m+1)(1-beta)}
      \frac{\mathbb E_\pi[Y^{m+1}]}{\mathbb E_\pi[Y]},
 \qquad \mu=\frac{a}{rho(1-beta)\mathbb E_\pi[Y]}. \tag{6}
\]

Indeed, one cycle reward is
(\int_0^T(beta Y+at)^m dt=[Y_{n+1}^{m+1}-(beta Y_n)^{m+1}]/[a(m+1)]),
and its duration is (T=(Y_{n+1}-beta Y_n)/a).  For (beta>0) this is a
stationary Markov-renewal/Palm identity, not an iid regeneration assertion.

## Boundary faces and Route-A verdict

(beta=0) resets to zero and gives iid exponential cycles (the genuine
regeneration face).  In that face the pre-jump density is
(f_Y(y)=(rho/a)y\exp[-rho y^2/(2a)]), while the continuous-time occupation
density is the half-normal
(f_X(x)=\sqrt{2rho/(\pi a)}\exp[-rho x^2/(2a)]), with
(\mathbb E[X]=\sqrt{2a/(\pi rho)}).  (beta=1,a>0,rho>0) removes
contraction and has no finite stationary law.  On the closed half-line,
(a=0,0<=beta<1,rho>0) has only the invariant atom delta_0, hence no invariant
probability on X>0; (a=0,beta=1,rho>0) leaves every law invariant.  If
(a=rho=0), every law is invariant; if (rho=0,a>0), linear escape gives no
invariant law.  The strict tuple is
\[
(\mathtt{A0\_FAIL},\mathtt{A1\_FAIL},\mathtt{A2\_FAIL},\mathtt{A3\_FAIL},
 \mathtt{A4\_FORMAL\_HINT}),
\]
with `ROUTE_A_REJECTED`, `NO_BAD_EULER_OR_ROOT_NUMBER`, and Route B disabled.
