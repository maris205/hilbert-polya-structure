# Narrative report: the positive H6 zeta signal lies in a certified pressure bracket

## Starting point

The previous H6 instability-roof project found a positive, non-lattice
periodic clock

\[
T_p=\log |\Lambda_{u,p}|
\]

on the certified local survivor of

\[
H_6(q,p)=(1-6q^2-p,q).
\]

Its degree-truncated primitive products displayed a highly stable positive
real zero,

\[
s_{20}=0.27798298167618902348\ldots .
\]

That calculation was intentionally reported only as a finite-section
observation.  It lacked a limiting transfer theorem or a uniform tail estimate
at the zero.

## The large-gate question

The next question is not whether the same finite products remain stable for a
few more periods.  It is whether the positive signal has an intrinsic
infinite-system meaning.  The source-locked candidate is the pressure function

\[
s\longmapsto P_{\Sigma_A}(-s\tau),
\]

where \(\tau\) is the one-step unstable expansion roof pulled back to the
four-state symbolic system.  Its unique positive root \(h_*\) is the entropy
of the corresponding suspension.  Standard hyperbolic dimension theory also
identifies \(h_*\) with the unstable-slice Hausdorff dimension.

## Exact geometric strengthening

The inherited cone certificate used the normalized unstable slope bound
\(|\mu|\le 1/2\).  The invariant graph equation improves this without a scan.
Let

\[
r=\frac{123}{112},\qquad a_0=r^{-1},\qquad
\rho=\frac{\sqrt{17}-\sqrt{13}}2.
\]

The recurrence

\[
\mu(H_6z)=\frac{a_0}{-12q(z)-r\mu(z)}
\]

and the exact survivor inequality \(12|q|\ge\sqrt{17}\) imply

\[
\sup|\mu|\le a_0\rho.
\]

Consequently the adapted unstable expansion obeys

\[
J^u_{\rm ad}\ge
\sqrt{17}-\rho
=\frac1\rho
=\frac{\sqrt{17}+\sqrt{13}}2.
\]

This raises the source-certified absolute Euler radius from
\((773/224)/\varphi\) to

\[
\frac{\sqrt{17}+\sqrt{13}}{1+\sqrt5}
=2.38828632613\ldots .
\]

The improved radius is useful infrastructure, but it still does not certify a
pressure zero by an absolute Euler tail.  At \(z=1\), the old uniform estimate
only reaches \(s\ge 0.35598\ldots\), above the observed signal.

## Certified cylinder experiment

The decisive computation encloses the roof on every admissible state cylinder
of length 13.  A word

\[
(x_{-6},\ldots,x_6)
\]

fixes the signs \(\varepsilon_{-7},\ldots,\varepsilon_6\).  Starting from the
exact sign intervals, outward rational square-root iteration encloses
\(q_{-6},\ldots,q_5\).  The inherited cone interval is then propagated from
time \(-6\) to time zero through the projective slope recurrence.  This gives
two rational numbers

\[
J_-(w)\le J^u_{\rm ad}(x)\le J_+(w)
\]

for every bi-infinite sequence whose central word is \(w\).

The length-12 words form 714 higher-block vertices, and the length-13 words
form 1156 chronological edges.  Weighting each edge by
\(J_+(w)^{-s}\) and \(J_-(w)^{-s}\) produces lower and upper pressure
matrices.  Rational enclosures for logarithms and exponentials, followed by
Collatz inequalities with positive rational vectors, certify

\[
0.277980<h_*<0.277987.
\]

The proof uses no prime table, Riemann-zero table, fitted scaling, floating
point eigenvalue as evidence, or averaged transition matrix.  Floating point
is allowed only to propose the positive Collatz vectors; the checker accepts
only the final rational inequalities.

## Interpretation

The certified interval contains the old finite-section value.  More
importantly, the Euler product used in that project is precisely the Ruelle
zeta product for the roof \(\tau\).  For a mixing subshift with a positive
Hölder roof, the leading real singularity occurs where

\[
P(-s\tau)=0.
\]

Thus the certified infinite-system root is a geometric pressure boundary, and
the conspicuous finite-section value is consistent with it at the certified
resolution rather than furnishing independent arithmetic evidence.  This
containment does not prove equality or convergence of the old sections.
Because the H6 survivor is a locally maximal hyperbolic surface set with
one-dimensional unstable bundle, \(h_*\) is its unstable-slice Hausdorff
dimension.  Area preservation makes the stable geometric potential
cohomologous to the unstable one; the standard surface basic-set product
formula then gives total dimension \(2h_*\).

## Research outcome

The result is mathematically positive and Hilbert--Pólya-negative.  It places
one finite numerical signal inside a computer-assisted pressure bracket
without promoting the finite sections to a limiting determinant.  This
supplies a strong generic-geometric control against treating the signal as an
arithmetic anomaly.  The next large move should keep the genuine H6
hyperbolic base but introduce a
canonical, independently motivated arithmetic fibre or twist.  Extending the
period cutoff or reimplementing generic BPS nuclearity would not address that
missing structure.
