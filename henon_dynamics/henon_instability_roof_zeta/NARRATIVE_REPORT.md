# Narrative Report

The prior Hénon project certified a local hyperbolic survivor of

\[
H_6(x,y)=(1-6x^2-y,x)
\]

and conjugated it to the four-state subshift with adjacency matrix

\[
A=\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix}.
\]

Its earlier weighted zeta calculations used integer map period. That clock has
an exact Hilbert--Pólya obstruction: substituting \(z=e^{-s}\) into
\(\det(I-zA)=1-z-z^3-z^4\) produces a \(2\pi i\)-periodic divisor and hence
only \(O(T)\) zeros in a bounded real strip. The stored generating-function
action is not a replacement because the explicit primitive period-four cycle

\[
(-1/\sqrt6,-1/\sqrt6,1/\sqrt6,1/\sqrt6)
\]

has total action zero.

The direction explored here uses the intrinsic periodic instability length

\[
T_p=\log |\Lambda_{u,p}|.
\]

The inherited cone theorem gives \(J^u\ge773/224>1\), so
\(\tau=\log J^u\) is a positive Hölder roof and sums to \(T_p\) on periodic
orbits. Different adapted norms change the pointwise roof by a Hölder
coboundary and leave every periodic length unchanged. The negative fixed orbit
has unstable multiplier with minimal polynomial

\[
X^4-4X^3-22X^2-4X+1,
\]

while the explicit period-four multiplier is \(289+24\sqrt{145}\), with
polynomial \(X^2-578X+1\). The four conjugates of every positive power of the
fixed multiplier remain distinct because their moduli are distinct. Such a
power therefore still has degree four, whereas every power of the period-four
multiplier has degree at most two. The two instability periods have irrational
ratio, proving that the roof is non-lattice.

The numerical question was frozen before periods 13--20 were opened. For
orientation sector \(\kappa\in\{0,1\}\), the experiment evaluated

\[
D_{\kappa,N}(s)=
\left[\prod_p(1-\sigma_p^\kappa e^{-sT_p}z^{n_p})
\right]_{\deg z\le N}\bigg|_{z=1}
\]

inside \(-0.25\le\Re s\le0.30\), \(|\Im s|\le20\). Periods 1--8 were
development, 9--12 validation, 13--16 sealed test, and 17--20 post-test
robustness. No prime table, Riemann-zero table, zeta/xi evaluation, target
fitting, affine clock adjustment, or Ulam matrix entered the experiment.

The independent catalogue contains all 2,170 primitive symbolic cycles through
period 20. All symbolic count, recurrence, contraction, guard-precision
determinant-one, and hyperbolicity gates pass. Primitive-factor multiplication
and a fixed-point trace recurrence agree below \(10^{-75}\) at the reported
roots. The explicit root census and three sampled numerical winding resolutions
agree at every cutoff; these are not interval-certified contour counts.

The untwisted sector has 43 roots in the frozen rectangle at every tested
cutoff from 7 through 20. Its 39 boundary-filtered training roots are all
retained at cutoff 12 and cutoff 16; the validation median drift is
\(1.873\times10^{-4}\), and the sealed-test median drift is
\(1.759\times10^{-6}\). The positive real finite-section zero reaches

\[
0.2779829816761890234883231168318\ldots
\]

at cutoff 20. These are finite-section numerical observations, not certified
zeros of a limiting determinant.

At the cutoff-16 positive zero, the Hénon degree-9--16 coefficient tail is
\(6.866\times10^{-7}\). At the same frozen Hénon probe, valid random weight,
phase, and same-density length controls have mean tails between
\(2.86\times10^4\) and \(3.20\times10^5\) times larger and retain only a
small fraction of cutoff-8 roots. This comparison demonstrates structured
cancellation relative to those orbit-level controls, but it does not identify
shadowing as the cause. Global period/length shuffles create high-frequency
exponential terms for which the frozen contour sampler fails, so their sampled
root statistics are explicitly NOT_TESTABLE; the underlying entire functions
still have well-defined zero counts. An exact constant-roof parent is even more
stable than Hénon, and its recorded nonzero tail is floating-point roundoff.
Finite-section stability is therefore not an arithmetic signature. Numerical
continuations at \(a=5.9\) and \(a=6.1\) are also internally stable, so the
tested behavior does not isolate \(a=6\).

The defensible endpoint is a positive non-lattice geometric clock plus a
reproducible finite-section cancellation phenomenon. The construction has no
limiting determinant theorem, analytic continuation, functional equation,
gamma factor, trivial-zero structure, Riemann--von Mangoldt law, prime
correspondence, or self-adjoint operator. Its Route-A status is exploratory,
and Route B is not authorized.
