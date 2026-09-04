# Theorem package — HCS-C357

## Status and frozen conventions

**PROVABLE AS STATED.** Let

\[
 x_+=\max\{x,0\},\qquad x_-=\min\{x,0\},\qquad
 V(x)=\frac{\omega_+^2x_+^2+\omega_-^2x_-^2}{2},
\]

and use the classical Hamiltonian \(H(x,p)=p^2/2+V(x)\) with symplectic
form \(dx\wedge dp\). In the main chamber \(\omega_+,\omega_->0\). The
quantum operator is the Friedrichs operator associated with

\[
 \mathfrak q[\psi]=\frac12\int_{\mathbb R}|\psi'|^2\,dx
                  +\int_{\mathbb R}V|\psi|^2\,dx .
\]

Primes on \(D_\nu\) below mean differentiation with respect to its argument,
not differentiation in \(x\). Units are \(m=\hbar=1\).

## Main theorem

For \(\omega_+,\omega_->0\), the following assertions hold.

1. The classical vector field has a complete flow. Every nonzero orbit is a
   periodic energy curve, all such curves have the same least period
   \[
      T=\pi\left(\frac1{\omega_+}+\frac1{\omega_-}\right).
   \]
   Among nonnegative stiffnesses, positivity of both frequencies is also
   necessary for every nonzero trajectory to be bounded and periodic.
2. For energy \(E>0\), the turning amplitudes, section speed, enclosed action,
   and angular frequency are
   \[
   a_+=\frac{\sqrt{2E}}{\omega_+},\quad
   a_-=\frac{\sqrt{2E}}{\omega_-},\quad
   |p|_{x=0}=\sqrt{2E},\quad
   J(E)=\frac E2\left(\frac1{\omega_+}+\frac1{\omega_-}\right),
   \quad \Omega=\frac{dE}{dJ}=\frac{2}{1/\omega_++1/\omega_-}.
   \]
3. The punctured plane admits a global \(C^1\), piecewise-analytic
   action--angle chart \((J,\theta)\), with
   \(dx\wedge dp=d\theta\wedge dJ\) and
   \(\dot J=0,\ \dot\theta=\Omega\). It is not \(C^2\) across either seam when
   \(\omega_+\ne\omega_-\). The time-\(T\) map is the identity; its derivative,
   hence the classical monodromy, is \(I_2\).
4. The Friedrichs operator is self-adjoint, bounded below, and has compact
   resolvent. Put
   \[
      \nu_\pm(\lambda)=\frac{\lambda}{\omega_\pm}-\frac12 .
   \]
   Its spectrum is a sequence of simple real eigenvalues tending to infinity,
   and a real number \(\lambda\) is an eigenvalue if and only if
   \[
   F(\lambda):=
   \sqrt{\omega_+}\,D'_{\nu_+(\lambda)}(0)D_{\nu_-(\lambda)}(0)
   +\sqrt{\omega_-}\,D'_{\nu_-(\lambda)}(0)D_{\nu_+(\lambda)}(0)=0.       \tag{1}
   \]
   This is a complete implicit characterization, not a claim that the
   asymmetric levels are equally spaced.

If \(\omega_+=\omega_-=\omega>0\), (1) reduces to the harmonic-oscillator
ladder \(\lambda_n=\omega(n+1/2)\), \(n\ge0\).

## Proof

### 1. Complete classical flow and exact excursions

The derivative \(V'\) is continuous and piecewise linear, and is globally
Lipschitz. Consequently \((\dot x,\dot p)=(p,-V'(x))\) has a unique global
solution; linear growth rules out finite-time escape. Along it, the chain
rule gives \(\dot H=pV'(x)-V'(x)p=0\).

Fix \(E>0\), write \(B=\sqrt{2E}\), and start at the positive section
\((x,p)=(0,B)\). On the right half-excursion,

\[
 x(t)=\frac B{\omega_+}\sin(\omega_+t),\qquad
 p(t)=B\cos(\omega_+t),\qquad 0\le t\le\frac\pi{\omega_+}.
\]

The state then equals \((0,-B)\). With
\(s=t-\pi/\omega_+\), the left half-excursion is

\[
 x(t)=-\frac B{\omega_-}\sin(\omega_-s),\qquad
 p(t)=-B\cos(\omega_-s),\qquad 0\le s\le\frac\pi{\omega_-}.
\]

It returns to \((0,B)\), proving the period formula. Neither half-excursion
can return to the section earlier, so this is the least period. Every nonzero
state has \(E>0\) and lies on one of these closed curves.

Conversely, if exactly one frequency vanishes, a trajectory entering its flat
half-axis with nonzero velocity continues linearly and is unbounded. If both
vanish, every nonzero-momentum trajectory is free and unbounded. Thus the
all-nonzero-orbit property holds exactly in the positive chamber.

### 2. Action, global chart, and seam regularity

The right and left halves of the phase-plane loop enclose areas
\(\pi E/\omega_+\) and \(\pi E/\omega_-\), respectively. Therefore
\(J=(2\pi)^{-1}\oint p\,dx\) has the stated value and \(E=\Omega J\).

Set \(\theta=\Omega t\pmod {2\pi}\) from the section \((0,p>0)\), and define
\(\theta_+=\pi\Omega/\omega_+\). With
\(B=\sqrt{2\Omega J}\), the inverse chart is

\[
\begin{array}{ll}
0\le\theta\le\theta_+:&
x=\dfrac B{\omega_+}\sin\dfrac{\omega_+\theta}{\Omega},\quad
p=B\cos\dfrac{\omega_+\theta}{\Omega},\\[6pt]
\theta_+\le\theta\le2\pi:&
x=-\dfrac B{\omega_-}\sin\dfrac{\omega_-(\theta-\theta_+)}{\Omega},\quad
p=-B\cos\dfrac{\omega_-(\theta-\theta_+)}{\Omega}.
\end{array}                                                    \tag{2}
\]

The values and first derivatives in \(J,\theta\) agree at both seams. On each
open half-chart a direct determinant calculation gives

\[
 x_\theta p_J-x_Jp_\theta=1,
\]

so (2) is a global \(C^1\) symplectic chart from
\((0,\infty)\times(\mathbb R/2\pi\mathbb Z)\) onto the punctured plane. At
\(\theta=\theta_+\), the two one-sided values of \(p_{\theta\theta}\) are
\(B(\omega_+/\Omega)^2\) and \(B(\omega_-/\Omega)^2\). Hence the chart is not
\(C^2\) unless the frequencies agree. Formula (2) also gives
\(\theta(t)=\theta(0)+\Omega t\), so the time-\(T\) map is exactly the identity
and its derivative is \(I_2\). Equivalently, each normalized half-flow matrix
is \(-I_2\), and their product is \(I_2\).

### 3. Friedrichs operator and the interface equation

The displayed quadratic form is densely defined, closed, and nonnegative.
Since

\[
 V(x)\ge\frac12\min(\omega_+^2,\omega_-^2)x^2,
\]

its form-domain unit ball embeds compactly into \(L^2(\mathbb R)\): use
Rellich compactness on a bounded interval and the potential term to control
the tails. The associated Friedrichs operator consequently has compact
resolvent. Its eigenfunctions and first derivatives are continuous at zero,
because the potential is locally bounded and the distributional equation has
no delta interaction.

For real \(\lambda\), the unique decaying solution on each half-line, up to a
scalar, is

\[
 D_{\nu_+(\lambda)}(\sqrt{2\omega_+}\,x)\quad(x>0),\qquad
 D_{\nu_-(\lambda)}(-\sqrt{2\omega_-}\,x)\quad(x<0).
\]

Continuity of the function and derivative has a nonzero pair of amplitudes
exactly when the determinant vanishes. Cancelling the common factor
\(\sqrt2\) gives precisely (1), including its plus sign. Thus (1) is both
necessary and sufficient. Compact self-adjointness gives completeness and
divergence of the eigenvalues. If two \(L^2\) eigenfunctions shared an
eigenvalue, their Wronskian would be constant and would vanish at infinity;
it is therefore zero, so the eigenfunctions are proportional. Every
eigenvalue is simple.

For equal frequencies, (1) becomes
\(2\sqrt\omega\,D_\nu(0)D'_\nu(0)=0\). The exact values
\[
 D_\nu(0)=\frac{2^{\nu/2}\sqrt\pi}{\Gamma((1-\nu)/2)},\qquad
 D'_\nu(0)=-\frac{2^{(\nu+1)/2}\sqrt\pi}{\Gamma(-\nu/2)}
\]
show that their real zeros are respectively the positive odd and the
nonnegative even integers. Thus the union is exactly
\(\nu=0,1,2,\ldots\), yielding the harmonic ladder.

## Boundary atlas

- **Zero energy, positive chamber.** \(E=0\) is only the origin equilibrium;
  the action--angle chart intentionally excludes it.
- **Equal stiffness.** The seam becomes artificial, the chart is smooth, and
  both the classical and quantum formulas reduce to the ordinary harmonic
  oscillator.
- **Exactly one zero stiffness.** The flat half-axis contains a continuum of
  rest equilibria, while every other trajectory that reaches it with nonzero
  momentum escapes linearly. Quantum compact resolvent fails. The spectrum
  as a set is \([0,\infty)\): Weyl sequences supported farther out on the flat
  side supply \([0,\infty)\), nonnegativity excludes negative spectrum, and
  no eigenfunction can be square-integrable on the flat half-line. No finer
  spectral-type claim is needed here.
- **Both stiffnesses zero.** This is the free particle; \(p=0\) gives the
  equilibrium continuum and \(p\ne0\) gives linear escape.
- **Regularity boundary.** The force is Lipschitz, not differentiable at the
  seam for unequal stiffnesses. Neither the Hamiltonian nor the action--angle
  chart is advertised as globally \(C^\infty\).

## Evidence and scope boundary

The finite evidence locks rational period/action conventions, seam matrices,
equal-frequency parity, the plus sign in (1), and degenerations. It does not
prove the continuum theorem or the operator theorem; the proof above does.
The source interface Wronskian is not an orbit Euler product or a target
determinant. The scope is NO_BAD_EULER_OR_ROOT_NUMBER; Route B is false.
