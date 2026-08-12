# A4.11b — Quantitative Warped Period Floor

## Statement

For the exact parameter

\[
 a=\frac{51}{50},
 \qquad
 c=2\left(\sqrt{\frac{101}{50}}-1\right),
\]

let

\[
 V_a(q)=2\pi e^{\pi|\Psi_a(q)|^2},
 \qquad
 \Psi_a(x,y)=(-cx-ax^2-y,x).
\]

Every nonconstant periodic orbit of

\[
 h_a(q,p)=\frac{|p|^2}{2}+V_a(q)
\]

with energy \(2\pi<E\le2\pi+0.010201\) has period

\[
 \boxed{T>0.60.}
\]

Thus the remaining A4.11 validated return search may be restricted from
\(0<T\le0.75\) to \(0.60<T\le0.75\).

## A convex configuration enclosure

If \(V_a(q)\le E\le2\pi+0.010201\) and \(u=\Psi_a(q)\), then

\[
 |u|^2
 \le\frac1\pi\log\left(1+\frac{0.010201}{2\pi}\right)
 \le\frac{0.010201}{2\pi^2}.
\]

Put

\[
 r_0=\frac{0.101}{\sqrt2\,\pi}<0.02274.
\]

The exact inverse map

\[
 q=(u_2,-cu_2-au_2^2-u_1)
\]

therefore places the entire allowed configuration domain in the convex box

\[
 \mathcal B=\left\{(x,y):
 |x|\le r_0,
 \quad |y|\le(1+c)r_0+ar_0^2\right\}.
\]

Using \(c<0.84254\), this gives the rational outward bounds

\[
 |x|<0.02274,
 \qquad |y|<0.042427.
\]

Every trajectory under consideration lies in \(\mathcal B\).  Since
\(\mathcal B\) is convex, its time average and every segment joining the
trajectory to that average also lie in \(\mathcal B\), as required by the
vector period inequality.

## Hessian enclosure on the convex box

Write \(u=(f,x)=\Psi_a(x,y)\), \(J=D\Psi_a\), and
\(\phi=\pi|u|^2\).  Throughout \(\mathcal B\), elementary outward estimates
give

\[
 |f|<0.062114,
 \qquad |u|^2<0.004376,
\]

and

\[
 J=
 \begin{pmatrix}-(c+2ax)&-1\\1&0\end{pmatrix},
 \qquad |c+2ax|<0.88893.
\]

The larger eigenvalue of \(J^TJ\) is

\[
 \frac{d^2+2+\sqrt{(d^2+2)^2-4}}{2},
 \qquad d=|c+2ax|,
\]

so direct rational substitution gives

\[
 \|J\|_{\rm op}^2<2.368.
\]

Only the first component of \(u\) is nonlinear, with
\(\nabla^2f=-2a e_1e_1^T\).  Hence

\[
 \nabla\phi=2\pi J^Tu,
 \qquad
 \nabla^2\phi
 =2\pi\left(J^TJ+f\nabla^2f\right),
\]

and

\[
 \|\nabla^2V_a\|_{\rm op}
 \le V_a\left[
 2\pi\{\|J\|_{\rm op}^2+2a|f|\}
 +4\pi^2\|J\|_{\rm op}^2|u|^2
 \right].
\]

For completeness, use \(3.1415<\pi<3.142\) and
\(e^s\le(1-s)^{-1}\) for \(0\le s<1\).  The preceding bounds imply

\[
 V_a<6.3716
\]

on \(\mathcal B\), and entirely rational outward arithmetic gives

\[
 \begin{aligned}
 \|\nabla^2V_a\|_{\rm op}
 &<6.3716\left[
 6.284\{2.368+2.04(0.062114)\}
 +39.489(2.368)(0.004376)
 \right]\\
 &<102.494<103.
 \end{aligned}
\]

The decimal endpoints here are terminating rationals used outward; they are
not sampled maxima.

## Period conclusion

Apply the vector periodic-orbit inequality proved in A4.11a on the convex
box \(\mathcal B\):

\[
 T\ge\frac{2\pi}{\sqrt{103}}>0.60.
\]

The last strict inequality follows already from \(\pi>3.1415\) after
squaring.  The equilibrium is at energy \(2\pi\), so every orbit on the
stated positive-excess shells is nonconstant.

## Boundary

This proposition removes the complete short-time interval
\(0<T\le0.60\) analytically.  It does not exclude additional warped returns
in \((0.60,0.75]\), does not continue the fast branch, and does not certify
its transverse determinant.  Those are the computer-assisted components of
A4.11/R401-VAL.
