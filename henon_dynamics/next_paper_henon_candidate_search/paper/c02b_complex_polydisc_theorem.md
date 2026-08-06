# A complex-polydisc contraction theorem for the signed Hénon recurrence

## Theorem

Let \(I=\mathbb Z\) or \(I=\mathbb Z/n\mathbb Z\).  Let
\(\varepsilon=(\varepsilon_i)_{i\in I}\in\{-1,+1\}^I\) satisfy

\[
 \neg(\varepsilon_{i-1}=\varepsilon_{i+1}=+1)
 \quad\text{for every }i.
\]

For cyclic \(I\), the two neighbor occurrences are chronological occurrences
with indices taken modulo \(n\), even when \(n=1\) or \(2\) makes them refer to
the same coordinate. Set

\[
 c=\frac{23}{48},\qquad \rho=\frac7{48},\qquad
 K_\varepsilon=
 \left\{q\in\ell^\infty(I):
 |q_i-\varepsilon_i c|\le\rho\text{ for all }i\right\}.
\]

Define

\[
 (T_\varepsilon q)_i
 =\varepsilon_i\sqrt{\frac{1-q_{i-1}-q_{i+1}}6},
\]

using the principal square root. Then:

1. \(T_\varepsilon\) is holomorphic on an open complex neighborhood of
   \(K_\varepsilon\);
2. it maps \(K_\varepsilon\) strictly into its coordinatewise interior, with
   uniform margin at least

   \[
   \mu=\min\left\{
   \frac{\sqrt{17}-4}{12},
   \frac58+\frac{\sqrt{10}-\sqrt{47}}6
   \right\}>0;
   \]

3. it is a contraction in the sup norm:

   \[
   \|T_\varepsilon q-T_\varepsilon q'\|_\infty
   \le \frac2{\sqrt{17}}\|q-q'\|_\infty;
   \]

4. consequently, it has a unique fixed point in \(K_\varepsilon\).

The fixed-point recurrence is exactly

\[
 q_{i+1}=1-6q_i^2-q_{i-1},
\]

so the result is a complex extension of the genuine Hénon orbit-coordinate
solver, not a fitted Möbius system.

## Proof

### 1. Radicand disks

Write

\[
 q_j=\varepsilon_jc+u_j,\qquad |u_j|\le\rho.
\]

Admissibility leaves two neighbor cases.

If one neighbor is positive and one is negative, their centers cancel. Hence

\[
 \frac{1-q_{i-1}-q_{i+1}}6
 \in \overline D\left(\frac16,\frac{2\rho}{6}\right)
 =\overline D\left(\frac16,\frac7{144}\right).
\]

If both neighbors are negative, their centers sum to \(-2c\). Hence

\[
 \frac{1-q_{i-1}-q_{i+1}}6
 \in \overline D\left(\frac{1+2c}{6},\frac{2\rho}{6}\right)
 =\overline D\left(\frac{47}{144},\frac7{144}\right).
\]

The left real edges of these disks are respectively

\[
 \frac16-\frac7{144}=\frac{17}{144}>0,
 \qquad
 \frac{47}{144}-\frac7{144}=\frac5{18}>0.
\]

Thus both disks lie strictly in the right half-plane.  The principal square
root is analytic on a common neighborhood of them.  Because the radicand is
a bounded nearest-neighbor linear map and the square-root derivatives are
uniformly bounded there, the coordinatewise composition is holomorphic as a
map on the corresponding open subset of \(\ell^\infty(I)\).

### 2. Strict self-mapping and radical margins

We use the following elementary bound. If
\(z\in\overline D(a,r)\), \(a>r>0\), and \(w=\sqrt z\) is principal, then

\[
 |w-\sqrt a|
 =\frac{|z-a|}{|w+\sqrt a|}
 \le\frac{r}{\sqrt{a-r}+\sqrt a}
 =\sqrt a-\sqrt{a-r}.
\]

Indeed, \(\Re z\ge a-r>0\), and the principal-root formula gives
\(\Re w\ge\sqrt{\Re z}\ge\sqrt{a-r}\).

For mixed neighbors, \(a=1/6\), \(r=7/144\), and
\(\sqrt a<c\). Therefore

\[
 |w-c|
 \le(\sqrt a-\sqrt{a-r})+(c-\sqrt a)
 =c-\frac{\sqrt{17}}{12}
 =\rho-\frac{\sqrt{17}-4}{12}.
\]

For two negative neighbors, \(a=47/144\), \(r=7/144\), and
\(\sqrt a>c\). Therefore

\[
 \begin{aligned}
 |w-c|
 &\le(\sqrt a-\sqrt{a-r})+(\sqrt a-c)\\
 &=\frac{\sqrt{47}}6-c-\frac{\sqrt{10}}6\\
 &=\rho-\left(\frac58+\frac{\sqrt{10}-\sqrt{47}}6\right).
 \end{aligned}
\]

The mixed margin is positive because \(17>16\).  For the second margin, it is
enough to show

\[
 \sqrt{47}-\sqrt{10}<\frac{15}{4}.
\]

After squaring, this follows from
\(\sqrt{470}>687/32\), and the latter is the exact integer inequality

\[
 470\cdot1024=481280>471969=687^2.
\]

Multiplication by \(\varepsilon_i\) maps the disk centered at \(c\) to the
disk centered at \(\varepsilon_i c\) without changing its radius. This proves
strict self-mapping with the stated uniform margin.

### 3. Uniform contraction

The product \(K_\varepsilon\) is convex. Along the segment between any
\(q,q'\in K_\varepsilon\), every radicand remains in its corresponding disk.
For a variation \(h\),

\[
 (DT_\varepsilon(q)h)_i
 =-\frac{\varepsilon_i}{12\sqrt{r_i(q)}}
 (h_{i-1}+h_{i+1}),
 \qquad
 r_i(q)=\frac{1-q_{i-1}-q_{i+1}}6.
\]

Both radicand cases satisfy

\[
 |r_i(q)|\ge\Re r_i(q)\ge\frac{17}{144},
 \qquad
 \frac1{12|\sqrt{r_i(q)}|}\le\frac1{\sqrt{17}}.
\]

It follows that

\[
 \|DT_\varepsilon(q)h\|_\infty
 \le\frac2{\sqrt{17}}\|h\|_\infty.
\]

Integrating along the segment proves the contraction estimate. Since
\(4<17\), the constant is strictly below one.

For \(n=1\), the only admissible cyclic sign is negative, and the two
chronological neighbors are two occurrences of the same coordinate. For
\(n=2\), admissibility forces both signs negative, and again both occurrences
at a coordinate refer to the other coordinate. In both cases the derivative
contains \(h+h=2h\); the two occurrences have been retained, and the same
\(2/\sqrt{17}\) bound applies rather than an incorrectly halved bound.

### 4. Fixed point

\(K_\varepsilon\) is closed in the complete sup-norm space
\(\ell^\infty(I)\). Strict self-mapping and the contraction theorem give a
unique fixed point by Banach's theorem. Squaring its coordinate equations
gives the Hénon recurrence. The real sign box is invariant, so this complex
fixed point agrees with the real R059 orbit for the same itinerary.

This completes the proof. \(\square\)

## Exact scope

This theorem closes the complex signed-root self-map bridge: the implicit
orbit-coordinate construction now has an explicit source-locked analytic polydisc and a
uniform complex contraction. It does **not** construct a finite Schottky
group, a finite-dimensional graph-directed inverse-branch system, a nuclear
operator, a Fredholm determinant, or a Route-A A2 object.

C02C has now completed the finite-window endpoint, localization,
two-coordinate gluing, matching/Hill and complex-projective steps.  Nuclearity
and a cycle-trace determinant remain open.

The prior-art audit also sharpened this theorem's boundary.  Under
\((x,y)=(-6q,6p)\), Sterling--Dullin--Meiss Theorem 3 already covers the same
real forbidden-neighbor SFT at \(b=1,k=6\) and real signed-root uniqueness.
Thus the real survivor and existence mechanism are not new.  What remains here
is an explicit *complex* project polydisc and constants; its standalone
publishable novelty is unconfirmed.  General analytic pinning/composition and
the absolute-denominator Fredholm mechanism are also prior art.  The current
paper gate is a genuinely new signed, aggregate trace-compatible operator
approximation theorem, not another existence or finite-section calculation.
