# Theorem package

Let \(\omega>0\), \(\kappa\ge0\), and \(x(0)=x_0>0\), \(\dot x(0)=v_0\).

**Theorem (positive isotonic atlas).** Put
\[
 E=\frac12(v_0^2+\omega^2x_0^2+\kappa/x_0^2),\quad
 a=x_0^2,\quad b=x_0v_0,\quad c=v_0^2+\kappa/x_0^2.
\]
For \(u=\cos\omega t\) and \(z=\sin(\omega t)/\omega\),
\[
 x(t)^2=a u^2+2buz+cz^2,\qquad ac-b^2=\kappa.                 \tag{1}
\]
For \(\kappa>0\), (1) is strictly positive for all real \(t\), hence gives
the unique global positive solution.  With \(r=x^2\),
\[
 r''+4\omega^2r=4E,qquad
 r_\pm=\frac{E\pm\sqrt{E^2-\omega^2\kappa}}{\omega^2}.       \tag{2}
\]
If \(E>\omega\sqrt\kappa\), the primitive period is \(T=\pi/\omega\);
at equality the equilibrium is \(x=\kappa^{1/4}/\sqrt\omega\), \(v=0\).
The positive-component action is
\[
 J=\frac{E}{2\omega}-\frac{\sqrt\kappa}{2}.                  \tag{3}
\]
For any normalized linear solution \(q''+\omega^2q=0\),
\[
 I_q=\tfrac12[(q\dot x-\dot q x)^2+\kappa(q/x)^2]
\]
is constant.  When \(\kappa=0\), the formula is valid up to the collision
with \(x=0\); no continuation across the singular face is asserted.

The JSON receipt contains nine rational parameter rows, four boundary rows,
ten exact identities, and high-precision evaluations of (1)--(3).  The
independent checker, SymPy identities, byte replay, and hostile mutations are
separate from the producer.
