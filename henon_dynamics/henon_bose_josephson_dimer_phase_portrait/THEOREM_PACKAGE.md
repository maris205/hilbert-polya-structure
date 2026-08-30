# C243 theorem package — Bose–Josephson dimer

## Frozen Hamiltonian and coordinate-safe flow

On the Bloch sphere \(x^2+y^2+z^2=1\), use
\[
 x=\sqrt{1-z^2}\cos\phi,\qquad y=\sqrt{1-z^2}\sin\phi,
\]
and the normalized Hamiltonian
\[
 H(z,\phi)=\frac{\Lambda z^2}{2}-\sqrt{1-z^2}\cos\phi,
 \qquad \Lambda\ge0.
\]
The canonical equations are
\[
 \dot z=-\sqrt{1-z^2}\sin\phi,\qquad
 \dot\phi=\Lambda z+\frac{z\cos\phi}{\sqrt{1-z^2}}.
\]
The equivalent Bloch-vector field is
\[
 \dot x=-\Lambda zy,\qquad \dot y=z(1+\Lambda x),\qquad \dot z=-y.
\]
At the north/south poles \((0,0,\pm1)\), this gives
\(\dot y=\pm1\), so the apparent \(\phi\)-singularity is a coordinate
artifact, not an equilibrium.

## Fixed points and pitchfork

For every \(\Lambda\), \((z,\phi)=(0,0)\) has energy \(-1\), linearization
\(\left[\begin{smallmatrix}0&-1\\\Lambda+1&0\end{smallmatrix}\right]\), and
frequency \(\sqrt{\Lambda+1}\).  The point \((0,\pi)\) has energy \(+1\) and
linearization \(\left[\begin{smallmatrix}0&1\\\Lambda-1&0\end{smallmatrix}\right]\):
it is elliptic for \(\Lambda<1\), parabolic at \(\Lambda=1\), and hyperbolic
for \(\Lambda>1\).  When \(\Lambda>1\), two further equilibria occur at
\[
 z=\pm\sqrt{1-\Lambda^{-2}},\qquad \phi=\pi,qquad
 H_{\max}=\frac{\Lambda+\Lambda^{-1}}2.
\]
In the original canonical \((z,\phi-\pi)\) coordinates their linearization
is
\[
 \begin{bmatrix}0&1/\Lambda\\-\Lambda(\Lambda^2-1)&0\end{bmatrix},
\]
so they are elliptic with small-amplitude period
\(2\pi/\sqrt{\Lambda^2-1}\).  The zero-phase crossing limit is
\(2\pi/\sqrt{\Lambda+1}\).  At \(\Lambda=1\) the pair coalesces with
\((0,\pi)\), giving the pitchfork.

## Quartic reduction and roots

On an energy level \(H=h\), eliminating \(\phi\) gives
\[
 \dot z^2=(1-z^2)-\left(\frac{\Lambda z^2}{2}-h\right)^2
 =-\frac{\Lambda^2}{4}z^4+(\Lambda h-1)z^2+1-h^2.
\]
For \(\Lambda>0\), put \(y=z^2\) and
\[
 y_\pm=\frac{2\bigl(\Lambda h-1\pm
 \sqrt{\Lambda^2-2\Lambda h+1}\bigr)}{\Lambda^2}.
\]
Then \(\dot z^2=(\Lambda^2/4)(y_+-z^2)(z^2-y_-)\).

For \(-1<h<1\), \(y_-<0<y_+\), the level is one connected crossing
component and
\[
 T=\frac{8}{\Lambda\sqrt{y_+-y_-}}
 K\!\left(\sqrt{\frac{y_+}{y_+-y_-}}\right).
\]
For \(\Lambda>1\) and \(1<h<H_{\max}\), there are two sign-preserving
components and each has
\[
 T=\frac{4}{\Lambda\sqrt{y_+}}
 K\!\left(\sqrt{1-\frac{y_-}{y_+}}\right).
\]
Here \(K\) is the complete elliptic integral with modulus (the code passes its
square as the numerical parameter).  The displayed periods are regular-level
periods only; no finite period is assigned to a separatrix.

## Separatrix, self-trapping, and boundaries

For \(\Lambda>1,h=1\), the homoclinic profile is
\[
 z(t)=\pm\frac{2\sqrt{\Lambda-1}}{\Lambda}
 \operatorname{sech}(\sqrt{\Lambda-1}\,t).
\]
The full critical level is connected through the saddle at \(z=0\), with two
one-sided homoclinic (punctured sign) branches.  At the turning point,
\(\phi=\pi\) for \(1<\Lambda<2\), the turning point is a Bloch pole at
\(\Lambda=2\), and \(\phi=0\) for \(\Lambda>2\).  The pole statement is made
in Bloch coordinates, not by assigning a value to the singular angle.

For regular \(\Lambda>1\) levels, \(1<h<H_{\max}\) is exactly the
self-trapped regime: each connected component has fixed sign of \(z\), and
the reverse initial sign gives the reflected component.  For \(-1<h<1\), the
single component crosses \(z=0\), so both signs are reached.  At \(h=1\),
crossing occurs only asymptotically along the homoclinic; at \(\Lambda=1,h=1\)
the quartic is \(-z^4/4\), so the level is the isolated degenerate point
\(z=0\), not a regular separatrix.  At \(\Lambda=0\), \(H=-x\) generates
rigid Bloch rotation with period \(2\pi\) on regular circles.

## Route-A boundary and reproducibility

The finite receipt has 14 fixed-point rows, 8 pole rows, 13 level rows and 5
component-criterion rows.  Independent symbolic identities and three
elliptic quadratures pass; byte replay passes and 28/28 repaired-hash hostile
mutations are rejected.  Because regular levels form a continuum, A1 is
`A1_WEAK`, not a discrete primitive-orbit claim.  The locked tuple is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` with
`ROUTE_A_REJECTED` and Route B disabled.  No arithmetic labels, target zeta,
Euler factors, root numbers, or Hilbert–Pólya operator are claimed.
