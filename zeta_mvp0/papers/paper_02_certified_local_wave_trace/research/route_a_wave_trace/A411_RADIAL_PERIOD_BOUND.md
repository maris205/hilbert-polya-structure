# A4.11a — Quantitative Radial Short-Period Exclusion

## Statement

Let

\[
 h_0(q,p)=\frac{|p|^2}{2}+V_0(q),
 \qquad
 V_0(q)=2\pi e^{\pi|q|^2}.
\]

For every energy

\[
 2\pi<E\le 2\pi+0.010201,
\]

every nonconstant periodic orbit on \(h_0^{-1}(E)\) has primitive period

\[
 T\ge
 \frac{2\pi}
 {\sqrt{E\{2\pi+4\pi\log(E/(2\pi))\}}}
 \ge
 \frac{2\pi}
 {\sqrt{(2\pi+0.010201)(2\pi+0.020402)}}
 >0.99.
\]

Consequently the radial reference has no return with
\(0<T\le0.75\) anywhere in the complete band
\(0<\delta=E-2\pi\le0.010201\).  In the notation of A4.9, the radial threshold
may therefore be chosen with

\[
 \boxed{\bar\delta(0.75)\ge0.010201.}
\]

This is an analytic bound, not a floating-point orbit census.
The only constant solution is the equilibrium at energy \(2\pi\), so no
constant trajectory lies on any shell covered by the statement.

## Period inequality

Let \(q(t)\) be any nonconstant \(T\)-periodic solution of

\[
 q''(t)=-\nabla V(q(t))
\]

whose image lies in a convex set on which
\(\|\nabla^2V\|_{\rm op}\le L\).  Write
\(\bar q=T^{-1}\int_0^Tq(t)\,dt\).  Periodic integration by parts and
\(\int_0^T(q-\bar q)\,dt=0\) give

\[
 \begin{aligned}
 \int_0^T|q'|^2\,dt
 &=\int_0^T(q-\bar q)\cdot\nabla V(q)\,dt\\
 &=\int_0^T(q-\bar q)\cdot
   \{\nabla V(q)-\nabla V(\bar q)\}\,dt\\
 &\le L\int_0^T|q-\bar q|^2\,dt.
 \end{aligned}
\]

The periodic Wirtinger inequality yields

\[
 \int_0^T|q-\bar q|^2\,dt
 \le\left(\frac{T}{2\pi}\right)^2
 \int_0^T|q'|^2\,dt.
\]

Since \(q\) is nonconstant, its kinetic integral is positive and cancellation
gives the dimension-independent lower bound

\[
 T\ge\frac{2\pi}{\sqrt L}.
\]

## Explicit radial Hessian bound

For the radial exponential potential,

\[
 \nabla^2V_0(q)
 =V_0(q)\bigl(2\pi I+4\pi^2qq^T\bigr).
\]

If a trajectory lies on \(h_0=E\), then

\[
 V_0(q)\le E,
 \qquad
 |q|^2\le\frac1\pi\log\frac{E}{2\pi}.
\]

The entire configuration image lies in this convex disk, and hence

\[
 L(E)\le E\left(2\pi+4\pi\log\frac{E}{2\pi}\right).
\]

For \(E=2\pi+\delta\), monotonicity and
\(\log(1+x)\le x\) imply, uniformly for
\(0<\delta\le0.010201\),

\[
 L(E)\le(2\pi+0.010201)(2\pi+0.020402).
\]

Substitution into the period inequality proves the statement.  The final
strict estimate \(T>0.99\) follows directly after squaring; it has ample
margin over \(0.75\) and does not depend on a rounded decimal evaluation.

## Scope

This result quantitatively closes only the radial component of

\[
 \delta_{\rm tr}
 =\min\{\delta_*,\bar\delta(0.75),\delta_{\rm nd}\}.
\]

It does not quantify the warped whole-shell threshold \(\delta_*\), does not
certify warped transverse nondegeneracy through \(\delta=0.010201\), and does not
turn the R401 numerical agreement into a proof.  Those two warped conditions
are the remaining A4.11/R401-VAL tasks.
