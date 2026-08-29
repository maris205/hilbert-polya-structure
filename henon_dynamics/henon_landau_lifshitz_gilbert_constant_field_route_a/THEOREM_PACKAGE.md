# Theorem package

Let \(m\in S^2\), \(e_3=(0,0,1)\), and
\[
 \dot m=-\omega m\times e_3-\alpha\omega m\times(m\times e_3),
 \qquad \alpha,\omega\ge0.
\]
On the chart \(m_3>-1\), put
\(z=(m_1+i m_2)/(1+m_3)\).  Direct component algebra gives
\[
 \dot z=(-\alpha\omega+i\omega)z,
 \quad z(t)=z(0)e^{(-\alpha\omega+i\omega)t},
\]
and the inverse map is
\(m_1+i m_2=2z/(1+|z|^2)\),
\(m_3=(1-|z|^2)/(1+|z|^2)\).  Thus every interior orbit satisfies
\[
 m_3(t)=\tanh(\alpha\omega t+\operatorname{artanh}m_3(0)).
\]
The poles are equilibria.  With (E=1-m_3),
\(\dot E=-\alpha\omega(1-m_3^2)\le0\).  If \(\alpha\omega>0\), the north pole
is asymptotically stable and the south pole is unstable; the transverse
linear modes have real parts \(-\alpha\omega\) and (+\alpha\omega),
respectively, and precession frequency \(\omega\).  If \(\alpha=0,\omega>0\),
every nonpolar latitude is a period-(2\pi/\omega) circle.  If \(\omega=0\),
the whole flow is the identity.

For a sampled time \(\tau>0\), positive damping fixes exactly the two poles.
On the alpha=0 face the sampled map fixes all of (S^2) exactly when
\(\omega\tau\in2\pi\mathbb Z\), and otherwise fixes only the poles; the
omega=0 and tau=0 faces are identity maps.  This fixed-set continuum is the
stopping obstruction for an isolated primitive-orbit Route-A owner.

The certificate records exact formulas and finite regression rows only; no
claim about target arithmetic, a dynamical zeta, or a Hilbert–Pólya operator is
made.
