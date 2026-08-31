# Theorem package

## Claim

Let `b>0`, `a,nu>=0`, and let `N` be a simple point process whose predictable
intensity is `lambda_(t-)`, where

`d lambda_t = -b(lambda_t-nu)dt + a dN_t`.

For `0<=z<=1`, `s>=0`, and `lambda_0=x>=0`, the joint transform is affine:

`E_x[z^(N_t-N_0) exp(-s lambda_t)] = exp(-A_t-B_t x)`,

where `B(0)=s`, `A(0)=0`,

`B'=1-bB-z exp(-aB)`, `A'=b nu B`.

If `nu>0`, a finite-intensity stationary Hawkes law exists exactly when
`a<b`.  Put `delta=b-a` and `mu=b nu/delta`.  Its Laplace transform is the
unique normalized solution

`L'/L=-b nu s/(b s+exp(-a s)-1)`, `L(0)=1`.

Writing `m_n=E lambda^n`, `m_0=1`, every stationary moment obeys

`m_n = [n b nu m_(n-1) + sum_(k=0)^(n-2) binom(n,k) a^(n-k)m_(k+1)]/[n delta]`.

The following three covariance objects are distinct:

1. `Cov(lambda_t,lambda_0)=mu a^2 exp(-delta|t|)/(2delta)`;
2. the complete counting covariance measure is
   `Gamma(dt)=mu delta_0(dt)+mu a(2b-a)exp(-delta|t|)dt/(2delta)`;
3. under `S(omega)=integral exp(-i omega t) Gamma(dt)`, with no
   `1/(2*pi)`,
   `S(omega)=mu(b^2+omega^2)/(delta^2+omega^2)`.

Consequently

`Var N_T = mu T + mu a(2b-a)[T/delta^2-(1-exp(-delta T))/delta^3]`.

For `m=a/b<1`, one immigrant's total cluster size `K` has

`P(K=n)=exp(-mn)(mn)^(n-1)/n!`, `n>=1`.

The faces `a=0`, `nu=0`, `a=b`, and `a>b` are handled without extending a
subcritical stationary formula through a zero denominator.

## Status

`PROVABLE AS STATED`.

The critical/supercritical negative statement is deliberately finite-
intensity: with `nu>0`, the mean equation rules out a stationary law having a
finite intensity.  No stronger assertion about exotic infinite-mean objects
is needed.

## Assumptions and notation

- The event rate is the predictable left limit `lambda_(t-)`; the post-event
  intensity is larger by `a`.
- `N_t-N_0` counts events in `(0,t]`.
- The stationary theorem uses `delta=b-a>0`.
- The Fourier transform carries no `1/(2*pi)` prefactor.  A convention using
  that prefactor rescales the displayed spectrum, not the covariance measure.
- `delta_0` denotes unit Dirac mass at zero; it is not a function value.

## Dependency map

1. The Markov generator gives the affine Riccati system and the moment
   recurrence.
2. The subcritical Poisson-cluster construction gives existence and
   uniqueness of the finite-intensity stationary process.
3. Stationarity applied to `exp(-s lambda)` gives the Laplace ODE.
4. Conditional first moments plus the generator second-moment equation give
   intensity covariance.
5. Hawkes's complete point spectrum gives the counting covariance measure;
   elementary rational decomposition gives its exponential density.
6. Double integration of that measure gives window variance.
7. Poisson Galton--Watson Lagrange inversion gives the Borel law.

## Proof

### 1. Generator and affine transform

For differentiable `f`, the intensity process has generator

`Gf(x)=b(nu-x)f'(x)+x[f(x+a)-f(x)]`.

For the joint count transform, a jump additionally contributes `z`.  Insert
`F(t,x)=exp(-A_t-B_t x)` into the backward equation.  The constant coefficient
is `-b nu B_t`, while the coefficient of `x` is
`bB_t+z exp(-aB_t)-1`.  Equating these with
`-A'_t-B'_t x` proves the displayed ODEs.  For `z in [0,1]` and `s>=0`, the
transform is bounded, so the standard localization limit introduces no extra
term.

### 2. Stationarity and Laplace transform

The kernel is `h(t)=a exp(-bt)1_(t>0)` and has mass `a/b`.  If `a<b`, the
immigration--Poisson-cluster construction is subcritical: every immigrant has
an almost surely finite family, and the superposition over immigrants in the
past is locally finite.  This constructs the stationary law; the cluster
genealogy also gives its uniqueness among finite-intensity stationary Hawkes
processes.

For `f_s(x)=exp(-sx)`, stationary generator expectation gives

`0=-b nu s L(s)-(b s+exp(-a s)-1)L'(s)`.

The denominator has expansion `(b-a)s+O(s^2)` and is positive for `s>0`
when `a<b`, because its derivative is `b-a exp(-as)>0`.  Thus the normalized
ODE has a unique solution.

### 3. Every moment

For `f(x)=x^n`,

`Gx^n=n b nu x^(n-1)-n b x^n + x[(x+a)^n-x^n]`.

Expanding the last term, its top contribution is `n a x^n`; all lower
contributions are `binom(n,k)a^(n-k)x^(k+1)`, `0<=k<=n-2`.
Stationary expectation and division by `n(b-a)` give the recurrence.  It is
triangular, hence determines every finite moment.  In particular

`E lambda=mu`, `Var lambda=mu a^2/(2delta)`.

### 4. Intensity covariance

Conditional expectation obeys

`d E(lambda_t|lambda_0=x)/dt=b nu-delta E(lambda_t|lambda_0=x)`.

Therefore it equals `mu+(x-mu)exp(-delta t)`.  Multiply by
`lambda_0-mu`, average in stationarity, and insert the variance from Step 3.

### 5. Counting covariance and spectrum

The complete covariance of a simple stationary point process contains the
same-event atom `mu delta_0`.  For a linear Hawkes process its Fourier
transform is

`S(omega)=mu/|1-a/(b+i omega)|^2`.

Algebra gives

`S(omega)=mu(b^2+omega^2)/(delta^2+omega^2)`

`=mu + mu a(2b-a)/(delta^2+omega^2)`.

Under the frozen Fourier convention,
`exp(-delta|t|)` transforms to `2delta/(delta^2+omega^2)`.  Inversion therefore
gives the stated continuous coefficient.  Its factor differs from the
intensity-covariance coefficient; the atom is additional.

### 6. Window variance

For an interval of length `T`, integrate the complete covariance measure over
the square.  The atom contributes `mu T`; symmetry gives

`2 C integral_0^T (T-t)exp(-delta t)dt`,

where `C=mu a(2b-a)/(2delta)`.  Direct integration gives the formula.  Its
long-window slope is `S(0)=mu b^2/delta^2`.

### 7. Borel cluster and boundaries

Each event has Poisson(`m=a/b`) direct offspring.  The total-family generating
function satisfies `T(z)=z exp(m(T(z)-1))`.  Lagrange inversion yields the
Borel coefficient.  Subcriticality gives mean `1/(1-m)` and variance
`m/(1-m)^3`.

If `a=0`, stationary intensity is the constant `nu` and `N` is homogeneous
Poisson.  If `nu=0`, the empty process is stationary.  With `nu>0`, the mean
equation is `r'=b nu+(a-b)r`; at `a=b` it grows linearly and at `a>b` it grows
exponentially, excluding finite-intensity stationarity.  This completes all
declared faces. ∎

## Route-A boundary

The tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and the verdict is
`ROUTE_A_REJECTED`.  Cluster indices and event times do not supply rational-
prime ownership, a logarithmic prime clock, a target divisor, or a determinant-
class Hilbert--Pólya operator.  Route B is disabled.
