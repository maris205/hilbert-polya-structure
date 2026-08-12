# CRR Phase Index of the Fast Lyapunov Orbit

## Result

For the positive-time, once-traversed fast orbit and the Fourier convention

\[
 \widehat g(t)=\int e^{-its}g(s)\,ds,\qquad
 g(s)=\frac1{2\pi}\int e^{its}\widehat g(t)\,dt,
\]

the Combescure--Ralston--Robert phase is

\[
 \boxed{
 e^{i\pi\sigma_+^{\mathrm{CRR}}/2}=+i,\qquad
 \sigma_+^{\mathrm{CRR}}\equiv1\pmod4.}
\]

We choose the representative \(\sigma_+^{\mathrm{CRR}}=1\) from CRR's own
two candidates.  The negative-time contribution is the complex conjugate:

\[
 \boxed{
 e^{i\pi\sigma_-^{\mathrm{CRR}}/2}=-i,\qquad
 \sigma_-^{\mathrm{CRR}}\equiv3\pmod4.}
\]

The trace formula only observes the index modulo four; no separate absolute
Conley--Zehnder lift is needed.

## The two CRR candidates

CRR equations (58) state that

\[
 \sigma_\gamma\in
 \{n-1+\sigma',\,n+1+\sigma'\},
\]

where \(\sigma'\) counts real eigenvalues of the reduced Poincaré map greater
than \(1\).  Here \(n=2\), while the limiting transverse multipliers are

\[
 e^{\pm i\theta_0},\qquad
 \theta_0=\frac{2\pi}{\rho_a}
 =2.76892955262428\ldots\in(0,2\pi).
\]

Thus \(\sigma'=0\) and CRR leave only

\[
 \sigma_+^{\mathrm{CRR}}\in\{1,3\},
 \qquad e^{i\pi\sigma/2}\in\{+i,-i\}.
\]

The continuous metaplectic square root must choose the sign.

## Exact harmonic-limit sign

At the bottom, the quadratic Hamiltonian is

\[
 H_{\mathrm{har}}
 =2\pi+
 \frac12(P_+^2+\omega_+^2Q_+^2)
 +\frac12(P_-^2+\omega_-^2Q_-^2).
\]

Its exact spectrum is

\[
 2\pi+\hbar\omega_+(n_++1/2)+\hbar\omega_-(n_-+1/2).
\]

At the positive fast recurrence \(T_+^0=2\pi/\omega_+\), the transverse
series is defined by Abel regularization:

\[
 \lim_{r\uparrow1}\sum_{n_-=0}^\infty
 r^{n_-}e^{-i\theta_0(n_-+1/2)}
 =\frac{e^{-i\theta_0/2}}{1-e^{-i\theta_0}}
 =\frac1{2i\sin(\theta_0/2)}
 =-\frac{i}{2\sin(\theta_0/2)}.
\]

Because \(0<\theta_0<2\pi\),

\[
 2\sin(\theta_0/2)
 =\sqrt{\det(I-P_+^0)}>0.
\]

Under the declared Fourier convention, Poisson summation in the fast
quantum number gives the full positive once-traversed longitudinal
coefficient

\[
 -\frac1{\omega_+}=-\frac{T_+^0}{2\pi}.
\]

The Jacobian \(1/\omega_+\) is positive and real.  After stripping it off
when choosing between CRR's two phase candidates, the longitudinal phase is
\(e^{-i\pi}=-1\).  Multiplication therefore gives

\[
 (-1)\left(-\frac{i}{\sqrt{\det(I-P_+^0)}}\right)
 =\frac{+i}{\sqrt{\det(I-P_+^0)}}.
\]

The longitudinal Poisson coefficient already contains the entire
positive real orbit-measure factor \(1/\omega_+=T_+^0/(2\pi)\); there is
no second multiplication by the primitive period.  Hence the positive-time
harmonic orbit term, in the declared project Fourier convention, is

\[
 i\,\widehat g(T_+^0)
 \frac{T_+^0}{2\pi\sqrt{D_+^0}}
 e^{iS_+/\hbar},
\]

which selects \(\sigma_+^{\mathrm{CRR}}=1\), not \(3\).

## Persistence on the nonlinear branch

The nonlinear variational path converges to the harmonic path as
\(\delta\downarrow0\), and

\[
 |\det(I-P_\delta)|
 \longrightarrow
 4\sin^2\frac{\pi}{\rho_a}
 =3.8627220445155036>0.
\]

The metaplectic/Maslov phase is locally constant under a nondegenerate
homotopy.  Therefore, after reducing the common threshold if necessary,

\[
 \sigma_+^{\mathrm{CRR}}(\delta)=1\pmod4
\]

for every fixed \(0<\delta<\delta_{\mathrm{tr}}\).

## Explicit A4.9 coefficient

The positive-time eigenvalue-only relative trace can now be written without
an unspecified phase integer:

\[
 \boxed{
 \rho_{\mathrm{rel},\hbar}(E;g)
 =
 i\,\widehat g(T_+(E))
 \frac{T_+(E)}{2\pi\sqrt{|\det(I-P_+(E))|}}
 e^{iS_+(E)/\hbar}
 +O_{\delta,\chi,g}(\hbar).}
\]

For a test function with symmetric positive and negative time support, add
the complex-conjugate negative-orientation term.

## Boundary

This calculation fixes the CRR trace phase.  It does not:

- establish a uniform joint \((\delta,\hbar)\) limit;
- extend the theorem to high energy at physical \(\hbar=1\);
- attach a rational prime to \(T_+(E)\);
- supply a von-Mangoldt amplitude or any zeta-zero conclusion.
