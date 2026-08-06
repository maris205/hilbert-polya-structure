# A4.8 Whole-Shell Fast-Orbit Uniqueness

## Result

Let

\[
 h_a(q,p)=\frac{|p|^2}{2}+2\pi e^{\pi|\Psi_a(q)|^2},
 \qquad
 \Psi_a(x,y)=(-c_ax-ax^2-y,x),
\]

with \(a=1.02\) and \(c_a=2(\sqrt{1+a}-1)\).  There is
\(\delta_*>0\) such that, for every \(0<\delta<\delta_*\), the energy shell
\(h_a=2\pi+\delta\) has exactly one geometric periodic orbit with a positive
return time at most \(0.75\).  It is the fast Lyapunov orbit, its only return
in this range is its primitive period, and

\[
 T_+(2\pi+\delta)\longrightarrow
 T_+^0=0.6638439766792985.
\]

This is a theorem about the complete shrinking energy shell, not a numerical
orbit census and not a statement restricted to the R400 shooting section.

## Exact blow-up

Set

\[
 \epsilon=\sqrt\delta,\qquad q=\epsilon Q,\qquad p=\epsilon P,
\]

and divide the energy excess by \(\epsilon^2\):

\[
 K_\epsilon(Q,P)
 =\frac{h_a(\epsilon Q,\epsilon P)-2\pi}{\epsilon^2}.
\]

Since

\[
 \Psi_a(\epsilon Q)
 =\epsilon(A_aQ+\epsilon B_a(Q)),
 \qquad
 A_a=\begin{pmatrix}-c_a&-1\\1&0\end{pmatrix},
 \qquad B_a(Q)=(-aQ_x^2,0),
\]

we have the exact expression

\[
 K_\epsilon
 =\frac{|P|^2}{2}
 +\frac{2\pi}{\epsilon^2}
 \left(e^{\pi\epsilon^2|A_aQ+\epsilon B_a(Q)|^2}-1\right).
\]

The apparent singularity at \(\epsilon=0\) is removable.  On every compact
set the family is smooth in \((\epsilon,Q,P)\) and

\[
 K_0(Q,P)=\frac{|P|^2}{2}+2\pi^2|A_aQ|^2.
\]

The rescaling leaves physical time unchanged because

\[
 \dot Q=\partial_PK_\epsilon,
 \qquad
 \dot P=-\partial_QK_\epsilon.
\]

## Global compactness of the normalized shells

Write \(\Sigma_\epsilon=\{K_\epsilon=1\}\).  On the corresponding original
shell,

\[
 |p|\le\sqrt2\,\epsilon,
 \qquad
 |\Psi_a(q)|^2
 \le\frac1\pi\log\left(1+\frac{\epsilon^2}{2\pi}\right).
\]

The inverse polynomial automorphism is

\[
 \Psi_a^{-1}(u,v)=(v,-c_av-av^2-u).
\]

Thus \(|q|=O(\epsilon)\) uniformly over the entire original shell.  It
follows that all \(\Sigma_\epsilon\) lie in one compact subset of
\((Q,P)\)-space and that

\[
 K_\epsilon\to K_0\quad\text{in }C^2,\qquad
 X_{K_\epsilon}\to X_{K_0}\quad\text{in }C^1
\]

on a common neighborhood.  The family is in fact \(C^\infty\) there.
Consequently the bounded-time flows converge uniformly together with their
first derivatives.

## Limiting return classification

After an orthogonal normal-coordinate change,

\[
 K_0=\frac12(P_-^2+\omega_-^2Q_-^2+P_+^2+\omega_+^2Q_+^2).
\]

The two primitive linear periods are

\[
 T_+^0=0.6638439766792985,\qquad
 T_-^0=1.5063780573896775.
\]

They obey

\[
 T_+^0<0.75<\min(2T_+^0,T_-^0).
\]

Consider any sequence of normalized-shell returns

\[
 Z_n\in\Sigma_{\epsilon_n},\qquad
 \Phi_{\epsilon_n}^{T_n}(Z_n)=Z_n,\qquad
 0<T_n\le0.75,\qquad \epsilon_n\downarrow0.
\]

Compactness gives subsequential limits \(Z_n\to Z_0\in\Sigma_0\) and
\(T_n\to T_*\in[0,0.75]\).  If \(T_*=0\), then

\[
 0=\frac1{T_n}\int_0^{T_n}
 X_{K_{\epsilon_n}}(\Phi_{\epsilon_n}^s(Z_n))\,ds
 \longrightarrow X_{K_0}(Z_0),
\]

which is impossible because \(K_0(Z_0)=1\) and the origin is the only
equilibrium.  If \(T_*>0\), linear return classification gives

\[
 T_*=T_+^0,\qquad
 Z_0\in\Gamma_0:=\Sigma_0\cap\{Q_-=P_-=0\}.
\]

The set \(\Gamma_0\) is the phase circle of one fast harmonic orbit.

## Local uniqueness by a Poincaré map

Fix the positive fast turning point

\[
 z_*=(Q_-=P_-=P_+=0,\ Q_+=\sqrt2/\omega_+)
\]

and use a small neighborhood of \(z_*\) in

\[
 \mathcal S_\epsilon=\{K_\epsilon=1,\ P_+=0,\ Q_+>0\}
\]

as the varying local section.  At \(z_*\),

\[
 \partial_{Q_+}K_0=\sqrt2\,\omega_+\ne0,\qquad
 \dot P_+=-\sqrt2\,\omega_+\ne0.
\]

Thus the energy equation locally eliminates \(Q_+\), the flow is transverse,
and \((Q_-,P_-)\) smoothly identify the nearby sections.

Introduce normalized slow coordinates

\[
 x_-=\sqrt{\omega_-}Q_-,\qquad
 y_-=\frac{P_-}{\sqrt{\omega_-}}.
\]

At \(\epsilon=0\), the derivative of the first-return map is exactly the
slow-mode rotation in these coordinates (and is symplectically conjugate to
it in the raw coordinates):

\[
 D\Pi_0(z_*)=R_{\theta_0},
 \qquad
 \theta_0=\omega_-T_+^0=\frac{2\pi}{\rho_a}.
\]

Hence

\[
 \det(I-D\Pi_0(z_*))
 =4\sin^2\frac{\pi}{\rho_a}
 =3.8627220445155036>0.
\]

The parameter-dependent implicit-function theorem gives one unique fixed
point of \(\Pi_\epsilon\) near \(z_*\).  The resulting orbit is the fast
Lyapunov branch by local uniqueness.  Since its period tends to \(T_+^0\),
shrink \(\delta_*\) so that

\[
 0<T_+(2\pi+\delta)<0.75<2T_+(2\pi+\delta)
\]

throughout \(0<\delta<\delta_*\).

## Unique oriented crossing near the fast turning point

The passage from a geometric orbit near \(\Gamma_0\) to a fixed point of
the local return map uses the following crossing-stability fact.  There are
a section neighborhood \(U\) of \(z_*\), \(\eta>0\), and
\(\epsilon_0>0\) such that any primitive periodic trajectory
\(z_n(t)\), with \(0<\epsilon_n<\epsilon_0\), \(T_n\to T_+^0\), and
phase-aligned \(C^1\) convergence to \(\Gamma_0\), intersects

\[
 U\cap\{K_{\epsilon_n}=1,\ P_+=0,\ Q_+>0\}
\]

exactly once per primitive circuit and with the orientation of the crossing
at \(z_*\).

Indeed, parametrize the limiting circle on the cyclic interval
\([ -\eta,T_+^0-\eta]\).  The limiting function \(P_+(t)\) has a simple
zero at \(t=0\), with \(\dot P_+(0)<0\).  Choose \(\eta\), \(c>0\), and
\(U\) so that \(\dot P_+\le-c\) on the part of \(\Gamma_0\) in \(U\),
the values at \(-\eta\) and \(\eta\) have opposite signs, and the remaining
compact arc of \(\Gamma_0\) is disjoint from the closure of the local
section in \(U\).  Bounded-time \(C^1\) convergence preserves the endpoint
signs and gives \(\dot P_+\le-c/2\) whenever \(z_n(t)\in U\).  The
intermediate-value theorem gives one local zero, strict monotonicity gives at
most one, and uniform position convergence excludes another intersection on
the complementary arc.  Identifying the endpoints of the period interval
counts this crossing once.

## Primitive-period and globalization checks

If \(T_n=m_n\tau_n\), where \(\tau_n\) is primitive, then \(m_n\to\infty\)
would imply \(\tau_n\to0\) and contradict the averaged-vector-field argument
above.  Thus \((m_n)\) is bounded.  If \(m_n=m\) along a subsequence, flow
convergence gives

\[
 \Phi_0^{T_+^0/m}(Z_0)=Z_0.
\]

Since the positive return times on \(\Gamma_0\) are the multiples of
\(T_+^0\), necessarily \(m=1\).

Finally, bounded-time \(C^1\) flow convergence makes a hypothetical second
sequence of geometric orbits converge uniformly over its phase-aligned
periods to \(\Gamma_0\).  The crossing-stability result gives exactly one
oriented intersection with the local section neighborhood per primitive
circuit.  Its return after that circuit is therefore the next local return,
so the intersection is a fixed point of the local first-return map.  That
map has only the continued fast fixed point.  This contradiction completes
the global proof.

## Spectral consequence and boundary

The radial blow-up has first limiting return time \(1\), and the same
compactness argument excludes every radial return with
\(0<|T|\le0.75\) at sufficiently small energy excess.  Therefore:

- the warped shell has one nondegenerate orbit in the complete CRR time
  range \(|T|\le0.75\);
- the radial shell has none;
- a Fourier cutoff supported near \(T_+(E)\) and away from zero needs no
  microlocal observable.

This closes the fixed-energy eigenvalue-only trace bridge.  It does not
identify the orbit period with \(\log p\), does not establish a high-energy
uniform theorem at physical \(\hbar=1\), and does not imply RH.
