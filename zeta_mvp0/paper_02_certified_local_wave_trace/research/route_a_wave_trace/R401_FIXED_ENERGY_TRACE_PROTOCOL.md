# R401-SC Fixed-Energy Relative-Trace Protocol

## 1. Purpose and claim boundary

R401-SC is the first eigenvalue-only numerical audit of Theorem A4.9 and
Proposition A4.10.  It evaluates one preregistered complex spectral
functional at a fixed energy and a descending semiclassical ladder.  It does
not scan time, fit an orbit phase, select a peak, use prime data, or compare
with zeta zeros.

The theorem provides an unspecified threshold

\[
 0<\delta<\delta_{\mathrm{tr}}.
\]

No quantitative proof currently places the selected \(\delta=0.01\) below
that threshold.  Consequently a numerical pass is reported only as an
**A4.9-guided fixed-energy audit**, not as a proof that this numerical energy
lies in the theorem's unknown interval.

## 2. Frozen classical cell and theory oracle

Take

\[
 a=1.02,
 \qquad E=2\pi+0.01.
\]

The immutable R400 cell
`results/r400_local_period_smoke/cells/delta_0p01.json` fixes

\[
 T=0.6635697917937936,
 \qquad
 S=0.006637068399523644,
 \qquad
 D=3.863271395157721.
\]

Its file hash must remain

```text
90184ec48d55986deb2b67ff6ac1fca3ae9f30b40e812181865f892a5920438b
```

With the project Fourier convention and the accepted A4.10 phase,

\[
 A=\frac{T}{2\pi\sqrt D}=0.05373152038174756,
\]

and the sole nonlinear theory oracle is

\[
 \boxed{
 \rho_{\mathrm{pred}}(\hbar)
 =iA e^{iS/\hbar}.}
\]

No fitted phase, action, scale, or offset is allowed.

## 3. Frozen test functions

Let

\[
 \eta(x)=
 \begin{cases}
 0,&x\le0,\\
 \dfrac{e^{-1/x}}{e^{-1/x}+e^{-1/(1-x)}},&0<x<1,\\
 1,&x\ge1.
 \end{cases}
\]

The energy cutoff is

\[
 \chi(\lambda)=
 \eta\!\left(\frac{\lambda-(2\pi+0.002)}{0.002}\right)
 \eta\!\left(\frac{(2\pi+0.018)-\lambda}{0.002}\right).
\]

Thus \(\chi=1\) on \(2\pi+[0.004,0.016]\), in particular at the target
energy.  The positive-time cutoff is

\[
 \widehat g(t)=
 \eta\!\left(\frac{t-0.05}{0.10}\right)
 \eta\!\left(\frac{0.745-t}{0.065}\right).
\]

It is supported in \((0.05,0.745)\), equals one on \([0.15,0.68]\), and
therefore obeys \(\widehat g(T)=1\).  Define

\[
 g(s)=\frac1{2\pi}\int e^{its}\widehat g(t)\,dt.
\]

The reported observable is exactly

\[
 \rho_{\mathrm{rel},\hbar}
 =\sum_k\chi(\lambda_{a,k})^2
 g\!\left(\frac{E-\lambda_{a,k}}\hbar\right)
 -\sum_k\chi(\lambda_{0,k})^2
 g\!\left(\frac{E-\lambda_{0,k}}\hbar\right).
\]

Gauss--Legendre orders 512 and 1024 are both evaluated.  Their trace values
must differ by at most \(10^{-10}\).

## 4. Frozen semiclassical ladder

The complete smoke ladder is

\[
 \boxed{
 \hbar\in
 \{4,3,2,1.5,1,0.75,0.5,0.4\}\times10^{-4}.}
\]

The first five cells deliberately record the pre-asymptotic region.  They
may not be dropped from plots or fits.  The last three were added only after
an exact harmonic oracle showed that the original five-point ladder was too
coarse to expose the asymptotic coefficient.

## 5. Exact coordinate change and valid Ritz space

Direct Hermite functions in the original \(q\) coordinates are forbidden:
the warped potential grows like \(e^{c x^4}\), so their potential matrix
elements diverge.  R401 first applies the exact area-preserving unitary
change

\[
 u=\Psi_a(q),\qquad dq=du.
\]

Writing \(J=D\Psi_a\) gives the quadratic form

\[
 \frac{\hbar^2}{2}\int
 \nabla_u f(u)^T G(u)\nabla_u f(u)\,du,
 \qquad
 G(u)=J(\Psi_a^{-1}u)J(\Psi_a^{-1}u)^T.
\]

For \(u=(u,v)\), \(c=2ar_a\), and \(d=c+2av\),

\[
 G(u,v)=
 \begin{pmatrix}1+d^2&-d\\-d&1\end{pmatrix}.
\]

Choose \(G(0)=LL^T\), \(\det L=1\), and put \(u=Lz\).  Then

\[
 B(z)=L^{-1}G(Lz)L^{-T},\qquad B(0)=I,
\]

and

\[
 V(Lz)=2\pi
 \exp\!\left(\pi(s_-^2z_-^2+s_+^2z_+^2)\right).
\]

The product-Hermite reference has frequencies
\(\omega_\pm=2\pi s_\pm\).  In these coordinates its functions are in the
potential form domain whenever \(\hbar<2/s_+\), a condition satisfied by a
margin greater than one throughout R401.  The residual kinetic form is

\[
 \frac{\hbar^2}{2}
 \int\nabla\phi_m^T(B-I)\nabla\phi_n\,dz,
\]

so no first-derivative term from a strong-form expansion can be omitted.

Every spectrum is retained through excess energy \(0.019\), beyond the
support of \(\chi\).  At the coarsest \(\hbar=4\times10^{-4}\) cell the
retention ceiling is raised to \(0.025\): its wider level spacing otherwise
leaves no eigenvalue in \((0.018,0.019)\), so an explicit zero-weight guard
mode would not be stored.  This remediation changes no active trace term.
For \(\hbar\ge10^{-4}\), use nested oscillator-energy cutoffs \(0.030\) and
\(0.035\).  For the three finer cells use:

| \(\hbar\) | production cutoff | fine cutoff |
|---:|---:|---:|
| \(7.5\times10^{-5}\) | 0.023 | 0.025 |
| \(5.0\times10^{-5}\) | 0.020 | 0.022 |
| \(4.0\times10^{-5}\) | 0.020 | 0.021 |

The Gauss--Hermite order is at least the largest occupied one-dimensional
degree plus 10; the fine audit adds at least 8 more nodes.  `eigh` residuals
are computed against an unmodified copy of the matrix.

## 6. Independent radial and harmonic oracles

The \(a=0\) spectrum is recomputed by an independent angular-momentum
Laguerre decomposition.  It uses degeneracy one for \(m=0\), degeneracy two
for \(|m|>0\), and generalized Gauss--Laguerre weight \(x^m e^{-x}\).  The
transformed Cartesian \(a=0\) spectrum and the Laguerre spectrum must agree
on every active ordered eigenvalue.

In addition, the exact quadratic spectra

\[
 2\pi+\hbar\omega_-(n_-+1/2)
 +\hbar\omega_+(n_++1/2)
\]

and the isotropic radial quadratic spectrum are passed through the identical
\(\chi,g\).  This is a non-tunable finite-\(\hbar\) baseline.  It diagnoses
how much of the approach to one is merely a window effect already present
in the exactly soluble harmonic limit.

## 7. Numerical integrity gates

For eigenvalues below \(2\pi+0.018\):

1. nested-basis phase budget
   \[
   0.745\,\max|\Delta\lambda|/\hbar<5\times10^{-3};
   \]
2. production/fine trace difference at most
   \(\max(0.05\hbar,10^{-9})\);
3. transformed-Cartesian/radial-Laguerre phase budget below \(10^{-6}\);
4. internal Ritz residual below \(10^{-10}\);
5. quadrature orthogonality defect below \(10^{-10}\);
6. all eigenvalue arrays extend past \(2\pi+0.018\), where \(\chi=0\);
7. order-512/order-1024 inverse-Fourier traces agree within \(10^{-10}\).

An independent checker must recompute \(\chi\), \(g\), the theory oracle,
the harmonic spectra, hashes, and all scalar gates without importing the
production trace module.

## 8. Scientific decision rule

Define

\[
 Z_\hbar=\frac{\rho_{\mathrm{rel},\hbar}}
 {iA e^{iS/\hbar}},
 \qquad
 Z_\hbar^{\mathrm{har}}
 =\frac{\rho_{\mathrm{rel},\hbar}^{\mathrm{har}}}
 {iA_0e^{iT_+^0\delta/\hbar}}.
\]

R401-SC receives a **numerical PASS** only if every integrity gate passes and
the finest cell satisfies all of

\[
 |Z_{4\times10^{-5}}-1|\le0.025,
 \qquad
 |\arg Z_{4\times10^{-5}}|\le0.025,
\]

\[
 |Z_{4\times10^{-5}}-Z_{4\times10^{-5}}^{\mathrm{har}}|\le0.02,
\]

and its error is smaller than both errors at \(7.5\times10^{-5}\) and
\(5\times10^{-5}\).  These criteria test the preregistered complex phase and
absolute \(1/(2\pi)\)-normalized amplitude.  Matching only the modulus is a
FAIL.

Even a PASS establishes neither an \(O(\hbar)\) remainder slope on this short
ladder nor a quantitative value of \(\delta_{\mathrm{tr}}\).  It authorizes
only the next, finer semiclassical convergence run.
