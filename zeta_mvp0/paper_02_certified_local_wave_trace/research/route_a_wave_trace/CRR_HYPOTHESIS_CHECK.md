# Combescure--Ralston--Robert Hypothesis Check

## Purpose

This note maps the model to Theorem 2.3 of M. Combescure, J. Ralston, and
D. Robert, “A proof of the Gutzwiller semiclassical trace formula using
coherent states decomposition,” *Communications in Mathematical Physics*
**202** (1999), 463--480,
[arXiv:math-ph/9807005](https://arxiv.org/abs/math-ph/9807005),
[DOI](https://doi.org/10.1007/s002200050591).

Let

\[
 \delta_{\mathrm{tr}}
 =\min\{\delta_*,\bar\delta(0.75),\delta_{\mathrm{nd}}\},
\]

where the three thresholds respectively control whole-shell warped
uniqueness, radial short-time exclusion, and transverse nondegeneracy.  The
check is for each fixed \(E=2\pi+\delta\) with
\(0<\delta<\delta_{\mathrm{tr}}\), followed by \(\hbar\downarrow0\).  It is
not uniform as \(\delta\downarrow0\).

Proposition A4.11a now makes the radial component quantitative:

\[
 \bar\delta(0.75)\ge0.010201,
\]

because every nonconstant radial orbit in that band has period greater than
\(0.99\).  The full threshold remains nonquantitative until the warped
whole-shell and transverse-nondegeneracy bounds \(\delta_*\) and
\(\delta_{\rm nd}\) are certified.

## Trace data

Choose

\[
 \chi\in C_c^\infty(\mathbb R;\mathbb R),
 \qquad \chi=1\ \text{near }E,
\]

with support in a compact regular energy band, and

\[
 \widehat g\in C_c^\infty((0,0.75)),\qquad
 0\notin\operatorname{supp}\widehat g,\qquad
 g\in\mathcal S(\mathbb R).
\]

For the eigenvalue-only result take the observable symbol \(A=1\), so
\(\widehat A=I\) and

\[
 \rho_j(E;g)=\operatorname{Tr}\left[
 \chi(P_{j,\hbar})^2
 g\left(\frac{E-P_{j,\hbar}}\hbar\right)\right].
\]

## Assumption map

CRR phrase H.2--H.3 for every time bound.  The version needed here is their
finite-time corollary: if
\(\operatorname{supp}\widehat g\subset[-T_0,T_0]\), inspection of the
stationary-phase proof shows that discreteness of geometric periodic orbits
modulo time translation and transverse nondegeneracy are used only for
\(0<|T_\gamma|\le T_0\).  The corresponding flow fixed components are clean
one-dimensional orbit components, not isolated points.  The time integral
is identically zero outside that support.  We take \(T_0=0.75\), so no
hypothesis about longer warped trajectories is asserted.

| CRR item | Requirement | Model verification |
|---|---|---|
| H.0 / Schrödinger remark | Symbol calculus, or a smooth potential on a compact energy surface below its limit at infinity | \(V_a\) is smooth, confining, and tends to infinity. CRR Remark 2.5 explicitly permits this fixed-energy Schrödinger setting without global temperate growth. |
| H.1 | Compact energy band and regular value | Proposition A4.1 proves every \(E>2\pi\) regular and every compact energy band compact. |
| finite-time H.2 | Periodic orbits with \(0<|T_\gamma|\le0.75\) form a discrete set | A4.8 gives exactly the fast orbit with its two time orientations on the warped shell; A4.6b gives the empty set on the radial shell. |
| finite-time H.3 | Every orbit in that time range is nondegenerate | A4.4 and A4.8 give \(\det(I-P_+)>0\) for small \(\delta\); the radial condition is vacuous. |
| H.4 | Observable symbol has controlled derivatives | \(A=1\) satisfies the condition with order zero. |
| H.5 | \(\widehat g\) has compact support in \([-T,T]\) | The selected support lies in \((0,0.75)\). |
| Cutoff | \(\chi\) compactly supported in the regular band and equal to one near \(E\) | Imposed explicitly above. |

The fast orbit's second repetition has period greater than \(0.75\), so no
iterate is missing from H.2--H.3.  Negative periods are the opposite time
orientation of the same geometric orbit and inherit nondegeneracy.

## Normalization check

The project fixes the unnormalized forward transform

\[
 \widehat g_{\mathrm{proj}}(t)=\int e^{-its}g(s)\,ds,
 \qquad
 g(s)=\frac1{2\pi}\int e^{its}\widehat g_{\mathrm{proj}}(t)\,dt.
\]

CRR's printed leading orbit coefficient is

\[
 (2\pi)^{n/2-1}\widehat g(T_\gamma)
 \frac{e^{i(S_\gamma/\hbar+\pi\sigma_\gamma^{\mathrm{CRR}}/2)}}
 {|\det(I-P_\gamma)|^{1/2}}
 \int_0^{T_\gamma^\#}A(\gamma(s))\,ds.
\]

To remove the source paper's implicit Fourier-normalization ambiguity, write
its transform as

\[
 \widehat g_{\mathrm{CRR}}
 :=\frac1{2\pi}\widehat g_{\mathrm{proj}}.
\]

Here \(n=2\), so \((2\pi)^{n/2-1}=1\), and \(A=1\) makes the orbit integral
equal to the primitive period.  Translation to the declared project
convention therefore gives

\[
 \widehat g_{\mathrm{proj}}(T_\gamma)
 \frac{T_\gamma^\#}
 {2\pi\sqrt{|\det(I-P_\gamma)|}}
 e^{i(S_\gamma/\hbar+\pi\sigma_\gamma^{\mathrm{CRR}}/2)}.
\]

This \(1/(2\pi)\) is independently forced by exact Poisson summation for the
anisotropic harmonic oscillator: the one-fold fast recurrence has
longitudinal coefficient
\(-1/\omega_+=-T_+^0/(2\pi)\).  That coefficient already contains the
complete longitudinal orbit measure, so multiplying by another period
would double count it.  This exact solvable-model check is the project's
normalization lock.

The zero-time coefficients in CRR are distributions supported at
\(T=0\).  They vanish against the chosen \(\widehat g\).  The remaining
orbit series starts with the displayed term and then powers
\(\hbar^j\), \(j\ge1\), giving the fixed-data remainder

\[
 O_{\delta,\chi,g}(\hbar).
\]

## Relative subtraction

Apply the theorem separately to the warped and radial operators.  A4.8
leaves one positive-time warped contribution, whereas A4.6b makes the radial
contribution \(O(\hbar^\infty)\) for the selected support.  Subtracting gives
A4.9 with the sign fixed by

\[
 \rho_{\mathrm{rel}}=\rho_a-\rho_0.
\]

Because \(A=1\), both traces are functions only of their eigenvalues.  The
staircase identity in Proposition A4.3 consequently applies without any
eigenfunction matrix elements.

## Still open

- an absolute Conley--Zehnder lift beyond the trace-relevant result
  \(\sigma_+^{\mathrm{CRR}}=1\bmod4\), if a separate convention ever needs
  it;
- a uniform joint \((\delta,\hbar)\to(0,0)\) expansion;
- the fixed-operator high-energy regime \(E\to\infty\), \(\hbar=1\);
- any prime-power period or von-Mangoldt amplitude mechanism.
