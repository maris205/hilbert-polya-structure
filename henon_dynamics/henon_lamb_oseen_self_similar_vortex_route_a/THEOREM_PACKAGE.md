# HCS-C299 theorem package

**Status:** PROVABLE AS STATED.  The uniqueness assertion is restricted to the declared radial forward-self-similar class; it is not a uniqueness theorem for arbitrary vortex filaments or arbitrary Navier--Stokes data.

## Theorem (complete radial forward-self-similar atlas)

Let \(\nu>0\), \(\tau=t+\tau_0>0\), and suppose a classical radial vorticity has the form

\[
 \omega(x,t)=\tau^{-1}F(\xi),\qquad \xi=|x|/\sqrt\tau,
\]

where \(F\in C^2([0,\infty))\) is bounded at zero and
\(\int_0^\infty |F(\xi)|\xi\,d\xi<\infty\).  Normalize its signed circulation to
\(\int_{\mathbb R^2}\omega\,dx=\Gamma\in\mathbb R\).  Then necessarily

\[
 \boxed{\ \omega_{\Gamma,\nu,\tau_0}(x,t)
 =\frac{\Gamma}{4\pi\nu\tau}
   \exp\!\left(-\frac{|x|^2}{4\nu\tau}\right)\ },
\]

and the Biot--Savart velocity is purely tangential,

\[
 u_r=0,\qquad
 u_\theta(r,t)=\frac{\Gamma}{2\pi r}
 \left(1-e^{-r^2/(4\nu\tau)}\right)\quad(r>0),
 \qquad u(0,t)=0.
\]

For a particle starting at radius \(r_0>0\), \(r(t)=r_0\).  Put
\(a=r_0^2/(4\nu)\) and

\[
 \mathcal F_a(\tau)=\tau-\tau e^{-a/\tau}-a\operatorname{Ei}(-a/\tau).
\]

Between ages \(\tau_s<\tau_t\), its exact angular displacement is

\[
 \theta(\tau_t)-\theta(\tau_s)
 =\frac{\Gamma}{2\pi r_0^2}
  [\mathcal F_a(\tau_t)-\mathcal F_a(\tau_s)].
\]

Here \(\theta\) is a continuous real-valued lift of polar angle, rather than
only an element of \(\mathbb R/(2\pi\mathbb Z)\).

The origin is a fixed particle.  For every integer \(k\ge0\) and every finite \(p\ge1\),

\[
 \int_{\mathbb R^2}|x|^{2k}\omega\,dx
 =\Gamma k!(4\nu\tau)^k,
 \qquad
 \|\omega\|_p^p
 =\frac{|\Gamma|^p}{p(4\pi\nu\tau)^{p-1}}.
\]

In particular,

\[
 \int\omega^2dx=\frac{\Gamma^2}{8\pi\nu\tau},\qquad
 \int|\nabla\omega|^2dx=\frac{\Gamma^2}{16\pi\nu^2\tau^2},\qquad
 \frac d{dt}\int\omega^2dx=-2\nu\int|\nabla\omega|^2dx.
\]

If \(\Gamma\ne0\) and \(r_0>0\), then
\(\theta(t)=\Gamma(8\pi\nu)^{-1}\log\tau+O(1)\).  Every finite \(L^p\) norm with \(p>1\) decreases strictly, so the vorticity state cannot recur.  The full-plane kinetic energy is infinite; for the disk-truncated energy,

\[
 \frac12\int_{|x|<R}|u|^2dx
 =\frac{\Gamma^2}{4\pi}\log R+O(1)\qquad(R\to\infty).
\]

## Proof

For a radial scalar \(\omega\), planar Biot--Savart produces a tangential velocity, while \(\nabla\omega\) is radial.  Hence \(u\cdot\nabla\omega=0\) identically.  Substituting the similarity ansatz into the remaining heat equation gives

\[
 \nu(F''+\xi^{-1}F')+F+\frac\xi2F'=0.
\]

After multiplication by \(\xi\), the left side is the derivative of
\(\nu\xi F'+\xi^2F/2\), so

\[
 \nu\xi F'(\xi)+\frac{\xi^2}{2}F(\xi)=C.
\]

Because \(F\in C^2([0,\infty))\) and is bounded at the origin, both terms tend to zero as \(\xi\downarrow0\); therefore \(C=0\).  The first-order equation yields
\(F(\xi)=A e^{-\xi^2/(4\nu)}\).  Finally,
\(\Gamma=2\pi\int_0^\infty F(\xi)\xi\,d\xi=4\pi\nu A\), proving uniqueness in the declared class.

Polar circulation gives
\(2\pi r u_\theta=2\pi\int_0^r s\omega(s,t)ds\), which proves the velocity formula and its continuous origin limit.  Thus \(\dot r=0\) and
\(\dot\theta=\Gamma(2\pi r_0^2)^{-1}(1-e^{-a/\tau})\).  Direct differentiation gives
\(\mathcal F_a'(\tau)=1-e^{-a/\tau}\), proving the trajectory formula.  Since
\(1-e^{-a/\tau}=a/\tau+O(\tau^{-2})\), integration gives the logarithmic angle.

The substitution \(y=r^2/(4\nu\tau)\) reduces all stated moments and norms to Gamma integrals.  Differentiating the Gaussian radially gives the palinstrophy formula; differentiating enstrophy gives the same quantity with factor \(-2\nu\).  Strict norm decay follows immediately for \(p>1\).  Finally \(u_\theta=\Gamma/(2\pi r)+o(r^{-1})\), and radial integration with the kinetic-energy factor \(1/2\) gives the logarithmic coefficient.

## Boundary ledger

- \(\Gamma=0\): the exact zero vorticity and velocity.
- \(\tau_0>0\): a smooth finite-enstrophy initial state.
- \(\tau_0=0\): weak initial trace \(\Gamma\delta_0\), smooth for every \(t>0\).
- \(\nu>0\): theorem domain; \(\nu=0\) is not inserted into the Gaussian formula.
- \(\nu\downarrow0\): weak vorticity limit \(\Gamma\delta_0\) and point-vortex velocity off the origin.
- \(r_0=0\): fixed separately; the positive-radius angle formula is not divided by zero.
- Long time: logarithmic angular drift, not a periodic orbit theorem.
- \(p>1\): strict norm decay excludes recurrent fluid states when \(\Gamma\ne0\).
- Kinetic energy: logarithmically divergent on the whole plane, even though enstrophy and palinstrophy are finite at positive age.

## Route-A outcome

Obstruction `HEN-O283` records
\((A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL})\).
The logarithm in a particle angle is a viscous-time asymptotic, not an arithmetic length.  No target local datum, Euler factor, root number, automorphy statement, divisor law, functional equation, target-zero match, or Hilbert--Polya operator is claimed, and Route B remains locked.
