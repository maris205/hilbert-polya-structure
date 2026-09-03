# Theorem package — Morse action and complete bound spectrum

## Assumptions and conventions

Let \(m,D,a,\hbar>0\),
\[
V(x)=D(e^{-2ax}-2e^{-ax}),\quad
H_{\rm cl}=p^2/(2m)+V(x),\quad
\lambda=\frac{\sqrt{2mD}}{a\hbar}.
\]
The action is normalized by \(J(E)=(2\pi)^{-1}\oint p\,dx\).  Quantum mechanically, \(H_q=-(\hbar^2/2m)d^2/dx^2+V\) denotes the self-adjoint operator associated with its lower-bounded closed quadratic form on \(L^2(\mathbb R)\).

## Main theorem

1. For every \(-D<E<0\), the energy curve is periodic and
   \[
   J(E)=\frac{\sqrt{2mD}}a\left(1-\sqrt{-E/D}\right),\qquad
   T(E)=\frac{2\pi}{a\sqrt{-2E/m}},\qquad J'(E)=T(E)/(2\pi).
   \]
2. The essential spectrum of \(H_q\) is \([0,\infty)\).  Its point spectrum consists exactly of
   \[
   E_n=-\frac{a^2\hbar^2}{2m}(\lambda-n-\tfrac12)^2,\qquad
   n\in\mathbb N_0,\quad n<\lambda-\tfrac12,
   \]
   each simple.  With \(z=2\lambda e^{-ax}\), an eigenfunction is proportional to
   \[
   z^{\lambda-n-1/2}e^{-z/2}L_n^{(2\lambda-2n-1)}(z).
   \]
   There are \(\max(0,\lceil\lambda-\tfrac12\rceil)\) bound states.  Equality \(n=\lambda-\tfrac12\) gives a zero-energy constant tail and is not in \(L^2\); there are no nonnegative eigenvalues.

## Proof

Put \(y=e^{-ax}\) and \(\delta=\sqrt{1+E/D}\).  The turning values are \(1\pm\delta\).  The full period is
\[
T=\sqrt{2m}\int_{x_-}^{x_+}\frac{dx}{\sqrt{E-V(x)}}
=\frac{\sqrt{2m}}{a\sqrt D}\int_0^\pi\frac{d\theta}{1+\delta\cos\theta}.
\]
The elementary tangent-half-angle integral equals \(\pi/\sqrt{1-\delta^2}\), yielding the displayed period.  The standard differentiation-under-the-integral identity \(J'(E)=T/(2\pi)\) has no endpoint terms because \(p=0\) at both turning points.  Integrating from the equilibrium \(E=-D\), where \(J=0\), gives the action formula.  This also fixes the factor \(2\pi\), rather than leaving an unnormalized closed integral.

For the quantum statement, write \(E=-(a^2\hbar^2/2m)s^2\) for a prospective negative level and set \(z=2\lambda e^{-ax}\).  The equation becomes
\[
z^2\psi_{zz}+z\psi_z+(-z^2/4+\lambda z-s^2)\psi=0.
\]
With \(\psi=z^se^{-z/2}F\), it reduces to
\[
zF''+(2s+1-z)F'+(\lambda-s-\tfrac12)F=0.
\]
Square integrability at \(x\to-\infty\), equivalently \(z\to\infty\), selects the recessive Whittaker solution.  Its small-\(z\) nonintegrable coefficient is proportional to \(1/\Gamma(s-\lambda+1/2)\).  It vanishes exactly when \(\lambda-s-1/2=n\in\mathbb N_0\).  Since \(dx=-(az)^{-1}dz\), the remaining endpoint integral is \(\int_0 z^{2s-1}dz\), so the strict condition is \(s>0\).  The Kummer series then terminates as the stated Laguerre polynomial.  This proves both inclusion and exhaustion of negative eigenvalues; one-dimensional Sturm oscillation gives simplicity and the node count \(n\).

Finally, \(V(x)\to0\) exponentially as \(x\to+\infty\) and \(V(x)\to+\infty\) as \(x\to-\infty\).  Weyl sequences supported far to the right give \([0,\infty)\subset\sigma_{\rm ess}\).  Dirichlet bracketing gives compact resolvent on a left half-line, while the right restriction is a short-range perturbation of the free half-line; hence no other essential spectrum occurs.  The same short-range Volterra asymptotics rule out a nonzero \(L^2\) solution at positive energy and at zero energy.  At the formal terminating equality \(s=0\), the displayed solution visibly tends to a nonzero constant.  Thus the threshold is not an eigenvalue.

## Boundary atlas

- \(E=-D\): equilibrium and zero action.
- \(-D<E<0\): periodic chamber.
- \(E=0\): nonperiodic dissociation separatrix, infinite period, finite limiting action.
- \(E>0\): scattering; \(E<-D\): empty energy shell.
- \(\lambda\leq1/2\): no bound states.
- \(n=\lambda-1/2\): non-\(L^2\) threshold, never counted.
- A nonpositive \(m,D,a\), or \(\hbar\) is outside the frozen model.

## Proof/evidence boundary

The proof above establishes the all-parameter theorem.  The JSON grid only checks conventions, exact coefficients, strict inequalities, and implementation reproducibility.  It is not an exhaustive numerical proof.
