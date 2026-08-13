# HCS-C35: the adelic Hénon--theta route

Status: `EXACT_MOTHER_COMPATIBILITY_PROVED; SCALING_COVARIANCE_GATE_OPEN`

This project takes a deliberately larger step than the preceding finite-field
experiments. It puts the integral area-preserving Hénon map on one global
adelic Hilbert space and tests whether it can be coupled, rather than merely
juxtaposed, with the prime closed orbits of the scaling site.

The source map is

\[
H_6(q,p)=(1-6q^2-p,q),
\]

with type-I generating function

\[
S_6(q,Q)=qQ-q+2q^3.
\]

Let \(\mathbb A=\mathbb A_{\mathbb Q}\), let
\(\psi:\mathbb A/\mathbb Q\to\mathbb T\) be the standard global additive
character, and use self-dual additive Haar measure.  On
\(L^2(\mathbb A)\), define

\[
\mathcal U_H=\mathcal F_{\mathbb A}\mathcal M_P,
\qquad
(\mathcal M_Pf)(q)=\psi(2q^3-q)f(q).
\]

This is a genuine unitary quantization of \(H_6\), not a prime-indexed direct
sum of unrelated finite matrices.

## Exact structural result

Three exact facts hold.

1. For every finite prime \(p\), the standard spherical vector
   \(e_p=1_{\mathbb Z_p}\) is fixed:

   \[
   \mathcal U_{H,p}e_p=e_p.
   \]

2. The rational theta distribution

   \[
   \Theta(f)=\sum_{r\in\mathbb Q}f(r)
   \]

   is fixed by the nonlinear Hénon quantization:

   \[
   \boxed{\Theta(\mathcal U_Hf)=\Theta(f).}
   \]

   Indeed, adelic Poisson summation gives
   \(\Theta(\mathcal Fg)=\Theta(g)\), while
   \(\psi(P(r))=1\) for every \(r\in\mathbb Q\).

3. If

   \[
   \mathcal S_0=
   \{g\in\mathcal S(\mathbb A):g(0)=\widehat g(0)=0\}
   \]

   is the standard Poisson/Connes test space and

   \[
   \mathcal S_H=
   \{f\in\mathcal S(\mathbb A):f(0)=0,
     \widehat{\mathcal M_Pf}(0)=0\},
   \]

   then \(\mathcal M_P:\mathcal S_H\to\mathcal S_0\) is a bijection. Here
   \(E=E_\times\) is the full adelic map
   \[
   E_\times(g)(x)=|x|^{1/2}\sum_{r\in\mathbb Q^\times}g(rx).
   \]
   The positive-integer real shorthand is only an even-sector half-model,
   and the odd cubic chirp does not preserve that sector. With the full map,
   Poisson summation yields

   \[
   E\mathcal U_H(\mathcal S_H)
   =I E\mathcal M_P(\mathcal S_H)
   =I E(\mathcal S_0)
   =E(\mathcal S_0).
   \]

Thus the known Riemann spectral range has an exact Hénon presentation.  This
is a mother-model compatibility theorem; it is not yet a positive Route-A
score for the Hénon increment.

## The Route-A mother architecture and its missing arrow

Two exact structures now live on the same arithmetic phase space:

\[
\boxed{
\begin{array}{c}
\text{scaling-site primitive orbit }C_p,
\quad \ell(C_p)=\log p
\\[2mm]
\Downarrow
\\[-1mm]
\text{separate local fact }\mathcal U_{H,p}1_{\mathbb Z_p}=1_{\mathbb Z_p}
\\[2mm]
\Downarrow
\\[-1mm]
\text{inherited mother zeta }
\displaystyle\prod_p(1-e^{-s\ell(C_p)})^{-1}
=\zeta(s)
\\[2mm]
\Downarrow
\\[-1mm]
\text{Poisson/Tate completion and scaling spectral range}
\\[2mm]
\Downarrow
\\[-1mm]
\text{adelic unitary Hénon quantization.}
\end{array}}
\]

This displays the conditional architecture without using a prime or zero
table. It is not yet a combined dynamical zeta: no scaling-site
bundle/cocycle has been constructed whose holonomy around \(C_p\) is the
Hénon local unitary. The prime orbits and A2--A3 data come from the scaling
mother system while Hénon supplies A4. Those entries cannot be maximized
coordinatewise until one scaling-covariant object carries all four.

## What this does and does not mean

The theorem is not a new proof of the Riemann hypothesis.  More sharply, the
simpler-parent control is decisive:

\[
\mathcal U_H\longmapsto\mathcal F_{\mathbb A}
\]

leaves the inherited scaling zeta and the adapted spectral range unchanged. The first
bridge therefore proves compatibility, not Hénon essentiality.  All Riemann
analytic information is inherited from the Tate/Connes mother system.

The result nevertheless changes the research position in two ways.

- C05's additive-constant phase ambiguity disappears globally: for
  \(C\in\mathbb Q\), \(\psi(C)=1\) on \(\mathbb A/\mathbb Q\).
- C32's varying \(p\)-dimensional fibres are replaced by one canonical
  Hilbert space \(L^2(\mathbb A)\) and one restricted-tensor-product unitary.

## The next genuinely new gate

The next target is a non-vacuum graded or scattering channel with weights
\(w_{p,r}^{H}\) such that

\[
Z_H^{\mathrm{new}}(s)
=\prod_p\exp\!\left(
\sum_{r\ge1}\frac{w_{p,r}^{H}}{r}p^{-rs}
\right)
=\zeta(s)e^{g_H(s)},
\]

where \(e^{g_H}\) is globally zero-free, but the Hénon deformation cannot be
removed by a unitary change of test space.  This is the
`HENON_ESSENTIALITY_GATE`.

The first functional-analytic gate now has a sharp answer. The naive operator
difference is noncompact, while one fixed-phase algebraic range pair has a
conditional static rank bound.

For \(p>3\) and \(m\geq0\), exact stationary-phase descent gives

\[
\int_{p^{-m}\mathbb Z_p}\psi_p(2x^3-x)\,dx=1.
\]

Hence, for the normalized dilation vectors
\(e_{p,m}=p^{-m/2}1_{p^{-m}\mathbb Z_p}\),

\[
\langle e_{p,m},M_{P_6}e_{p,m}\rangle=p^{-m},
\qquad
\|(M_{P_6}-I)e_{p,m}\|^2=2-2p^{-m}.
\]

Since \(e_{p,m}\rightharpoonup0\), \(M_{P_6}-I\) is not compact.  Ordinary
same-space relative Fredholm theory is therefore closed.

On the other hand, within
\(V=\{f:f(0)=0\}\), the standard space and chirped space are the two
hyperplanes

\[
S_0=\ker\!\int f,
\qquad
M_PS_0=\ker\!\int\psi(-P)f.
\]

They share a common codimension-two subspace, so after any common linear map
their algebraic images differ by at most one direction on each side. If both
images extend to closed subspaces of one Hilbert completion, their
projections satisfy

\[
\operatorname{rank}(P_H-P_0)\leq2.
\]

This is a static fixed-phase statement only. It does not imply a scalar or
two-channel dynamical scattering problem.

Indeed, dilation conjugates the chirp to

\[
D_aM_{P_6}D_a^{-1}=M_{P_a},
\qquad
P_a(x)=2a^3x^3-ax.
\]

The corresponding boundary functionals \(\Lambda_{-P_a}\) have
infinite-dimensional span before applying \(E\). At the real place, the
entire kernels

\[
\phi_a(z)=\exp[-2\pi i(2a^3z^3-az)]
\]

are linearly independent: on \(z=re^{i\pi/6}\), the largest \(a\) has the
unique dominant growth \(e^{4\pi a^3r^3+O(r)}\). Thus static rank two cannot
be promoted to dynamic finite-channel scattering.

There is nevertheless one exact escape mechanism. For the full adelic
nonzero-rational scaling map, Poisson summation gives

\[
E_\times(\widehat g)(x)=E_\times(g)(x^{-1})
+|x|^{-1/2}g(0)-|x|^{1/2}\widehat g(0).
\]

With \(g=M_{P_a}f\) and \(f(0)=0\), the failure of exact inversion is always
a scalar multiple of the same outgoing mode \(|x|^{1/2}\). The input
coefficient functionals still span infinitely many directions, so this is
not yet finite-channel scattering; it is the concrete Poisson boundary
anomaly that the next crossed-product construction must promote to a
determinant. The static comparison uses \(\Lambda_{-P_a}\), while this
formula contains \(\Lambda_{+P_a}\); the two infinite families are not
silently identified. The mode \(|x|^{1/2}\) is also only an asymptotic
boundary mode until membership in the scaling Hilbert completion is proved.

The minimum acceptable advance is one of the following:

1. a scaling-site Hilbert bundle/cocycle with chronological Hénon holonomy;
2. a theorem that the exact rank-one Poisson boundary defect extends to a
   determinant-class cocycle despite its infinite family of coefficients;
3. a crossed-product determinant with the same \(\log p\) clock and a
   reciprocal zero-free relative factor;
4. or a rigidity theorem proving that every such Hénon decoration is a
   removable coboundary.

The immediate next gate is the scaling-covariance/orbit-closure theorem. Its
three outcomes are decisive:

- the Poisson quotient kills the infinite orbit: construct the anomaly
  determinant and test its divisor;
- a crossed-product trace controls it without extra zeros: promote Route A;
- no determinant-class quotient exists: close the adelic Hénon route and
  pivot to a different all-period arithmetic dynamics.

## Reproducibility

The exact arithmetic pilot verifies the global additive-character product
formula on a frozen rational grid, the Hénon polynomial phase, the
constant-gauge cancellation, and the theorem-level zero-accumulation kill of
the discarded raw finite-field Euler product.  It also verifies the exact
cubic-sum recurrence behind the local dilation theorem.

```bash
python code/c35_adelic_theta_producer.py --output results/c35_certificate.json
python code/c35_adelic_theta_checker.py results/c35_certificate.json
python -m unittest discover -s code -p 'test_c35.py'
```

The code uses only the Python standard library and exact rational arithmetic.

## Literature boundary

The ingredients from Tate's thesis, adelic Poisson summation, the Connes
scaling spectral realization, and the scaling-site prime orbits are prior
art.  The Hénon specialization and its exact theta-stabilizer calculation
were not found as a packaged construction within the bounded search.  The
novelty claim is search-bounded and modest: this project is primarily a
Route-A architecture theorem and a precise new research gate.
