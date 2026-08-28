# Theorem package

Let \(u=(u_1,u_2)\) and \(\phi\) be complex-valued fields on the
\(2\pi\)-torus.  The constant-\(f\) system is
\[
 u_t+fJu+c\nabla\phi=0,\qquad
 \phi_t+c\nabla\!\cdot u=0,\qquad
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]
with \(f\in\mathbb R\), \(c\ge0\), and physical time \(t\).  For
\(n=(n_1,n_2)\in\mathbb Z^2\), put \(\rho=|n|^2\) and
\[
 G_n=\begin{pmatrix}
 0&f&-icn_1\\
 -f&0&-icn_2\\
 -icn_1&-icn_2&0
 \end{pmatrix},\qquad
 \omega_n=(f^2+c^2\rho)^{1/2}.
\]
For \(c>0\), the full multiplier has maximal graph domain
\[
D(G)=\left\{X\in L^2:\sum_{n\in\mathbb Z^2}\|G_nX_n\|^2<\infty\right\},
\]
with trigonometric polynomials as a core (and \(H^1\) contained in this
domain); its closure is skew-adjoint.  This includes the infinite
zero/geostrophic branch.

## Main theorem (Fourier spectral atlas)

If \(\omega_n>0\), then \(G_n^*=-G_n\),
\[
 G_n^3+\omega_n^2G_n=0,
\]
and the mutually orthogonal spectral projectors are
\[
 P_0=I+\frac{G_n^2}{\omega_n^2},\qquad
 P_+=\frac12\left(-\frac{G_n^2}{\omega_n^2}-\frac{iG_n}{\omega_n}\right),\qquad
 P_-=\frac12\left(-\frac{G_n^2}{\omega_n^2}+\frac{iG_n}{\omega_n}\right).
\]
Each has rank one and
\[
 e^{tG_n}=P_0+\cos(\omega_nt)(I-P_0)
       +\frac{\sin(\omega_nt)}{\omega_n}G_n .
\]
The \(P_0\) branch is stationary and is the linear potential-vorticity/
geostrophic branch; \(P_\pm\) are the two inertia--gravity branches.  At
\(n=0\) and \(f\ne0\), the eigenvalues are \(0,\pm i|f|\); if \(f=0\), the
block is zero.

For \(c>0\), define
\[
 \widehat\zeta_n=i(n_1\widehat u_{2,n}-n_2\widehat u_{1,n}).
\]
Then \(\widehat\zeta_n-(f/c)\widehat\phi_n\) is constant in time.  For
\(q>0\), the shell \(\rho=q\) has
\[
 r_2(q)=4\bigl(d_1(q)-d_3(q)\bigr)
\]
integer modes, where \(d_j(q)\) counts divisors congruent to \(j\) modulo
four.  A finite Fourier-support state is \(T\)-periodic if and only if every
participating nonzero branch satisfies \(\omega_nT\in2\pi\mathbb Z\).

The global group on \(L^2(\mathbb T^2;\mathbb C^3)\) is unitary.  For every
\(t\), including \(t=0\), it is neither compact nor in any Schatten class.

## Proof ledger

Fourier transformation gives the displayed blocks.  Direct multiplication
gives the cubic and inspection gives skew-Hermiticity.  Lagrange interpolation
at \(0,\pm i\omega_n\) gives the projectors and reduction of the exponential
series gives the closed propagator.  Taking the curl gives
\(\zeta_t=-f\nabla\!\cdot u\), while \(\phi_t=-c\nabla\!\cdot u\), proving the
potential-vorticity identity for \(c>0\).  The shell formula is the
sum-of-two-squares theorem.  Applying each projector proves the finite-support
periodicity equivalence.  Finally, skew-adjointness gives unitarity; distinct
high Fourier modes form an orthonormal sequence whose images have norm one,
which proves noncompactness and failure of every Schatten condition, including
the identity at \(t=0\).  The \(c=0\) face is a bounded pointwise rotation and
is checked separately rather than being hidden in the \(H^1\) statement.
