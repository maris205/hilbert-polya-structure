# Next-paper roadmap: which spectrum belongs to the area-preserving Hénon map?

Status: **one candidate lane in the breadth-first Hénon search; no theorem or
numerical claim is declared complete**.

This route was initially considered for the immediate next paper. A broader
primary-source audit found extensive prior work on quantized Hénon maps,
including full-plane spectral type and horseshoe-regime WKB/Stokes geometry.
It therefore competes only if G0 identifies a genuinely new certified
trace/determinant theorem. It is neither automatically N+2 nor the selected
next paper. The current selection protocol is in
`../next_paper_henon_candidate_search/`.

Primary legacy source:

- `../docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf`

Working title:

> **Which Spectrum Belongs to the Area-Preserving Hénon Map? A Weyl-Law
> Obstruction for Quartic Surrogates and a Local Trace Formula for a Specified
> Natural Quantization on a Certified Survivor**

## One-sentence thesis

The quartic Schrödinger spectrum used in Paper 5 is not the spectrum of the
area-preserving Hénon map and has an asymptotic counting law incompatible with
Riemann--von Mangoldt; one specified natural spectral object is instead a
known Fourier-integral quantization of the discrete map, whose **localized
fixed-time traces** may be controlled by the certified Hénon periodic orbits,
with generating-function action in the phase and instability data in the
amplitude. The classical map does not select a unique global or subprincipal
quantum phase.

This is a foundations-and-obstructions paper. It is not a new Riemann-zero fit
and it does not claim a Hilbert--Pólya operator.

## What is retained from Paper 5

The project retains only the intrinsic classical family

\[
H_a(q,p)=(1-aq^2-p,q), \qquad \det DH_a=1,
\]

its reversibility, its periodic orbits, and the question of what operator is
naturally associated with this exact discrete dynamics.

The following legacy ingredients are **not inherited**:

- the claimed critical values \(a_c\simeq1.00561\) and \(a\simeq1.02\);
- the stored chaotic-layer coefficient and its match to a fitted
  \(\hbar_{\mathrm{eff}}\);
- the continuum second-difference approximation and chosen \(0.05q^4\)
  confinement as a quantization of the map;
- fitted static or logarithmically driven parameter schedules;
- the 100-zero optimization, phase-unwrapping rule, Markov spectrum, GUE-only
  diagnostics, or hardware analogy.

The detailed reasons are recorded in [SOURCE_AUDIT.md](SOURCE_AUDIT.md).

## Exact mathematical backbone

### 1. Standard-parameter identification

The linear change of coordinates

\[
C_a(q,p)=(-aq,ap)
\]

gives

\[
C_aH_aC_a^{-1}(X,Y)=(X^2+Y-a,-X).
\]

Thus Paper 5's parameter \(a\) is the standard area-preserving Hénon parameter
\(k\) used in the classical homoclinic-bifurcation literature; there is no
hidden rescaling that makes \(1.0056\) a special literature threshold.
Here \(a\ne0\), and \(\det C_a=-a^2\): this is a classical linear conjugacy,
not a symplectic/metaplectic equivalence transporting quantum spectra.

### 2. Weyl-law obstruction to the quartic surrogate

For the static legacy Hamiltonian

\[
\widehat H_\hbar=-\frac{\hbar^2}{2}\frac{d^2}{dq^2}
+\lambda q^4+\frac a3q^3+q^2-q,
\qquad \lambda>0,
\]

the one-dimensional Weyl law gives

\[
N_H(E)\sim
\frac{\sqrt2}{2\pi\hbar}\lambda^{-1/4}
B\!\left(\frac14,\frac32\right)E^{3/4}.
\]

Hence \(E_n\asymp n^{4/3}\). This cannot agree, under any fixed affine energy
rescaling, with

\[
N_\zeta(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}+O(\log T).
\]

The theorem is deliberately narrow: it rules out the static polynomial
Schrödinger surrogate and its fixed affine rescalings. It does not rule out all
noncompact, scattering, or nonlocal operator programs.

### 3. Exact discrete action and known natural quantization

The type-I generating function

\[
S_a(q,Q)=qQ-q+\frac a3q^3
\]

satisfies

\[
p=-\partial_qS_a=1-aq^2-Q,
\qquad P=\partial_QS_a=q,
\]

so it generates exactly \((Q,P)=H_a(q,p)\). With the fixed branch
\(\sqrt{i}=e^{i\pi/4}\),

\[
(U_{a,\hbar}\psi)(Q)=
\frac{1}{\sqrt{2\pi i\hbar}}
\int_{\mathbb R}
e^{iS_a(q,Q)/\hbar}\psi(q)\,dq
\]

is a unitary Fourier transform composed with a unit-modulus cubic phase. This
kind of quantized Hénon map was already constructed by Fornæss and Weickert
(2000); the new paper will cite that prior result and will not claim the
quantization itself as novel. “Natural” does not mean unique: global and
subprincipal phase choices can preserve the same classical canonical relation
while changing quantum spectral data. Those choices must be frozen and their
effect separated from the leading periodic-orbit term.

### 4. New periodic-orbit bridge

Let \(\Lambda_*\) be the already certified **local four-state survivor** for
\(H_6\). It is not the full bounded repeller and not the full binary horseshoe.
Index symbolic states by \(w=(s,t)\), choose smooth position cutoffs
\(\chi_s(q)\) for the two certified current-coordinate intervals, and use the
four-state history label to retain chronology. Before implementation one must
prove that the cutoffs equal one on a neighborhood of the full projected local
survivor and that their stationary support contains no extra closed paths; if
only a finite-period margin is proved, the theorem is restricted to that
frozen period bound. The candidate block convention is

\[
(\mathcal M_\hbar)_{w',w}
=\mathbf 1_{\{A_{w,w'}=1\}}\,\chi_{s'}U_{6,\hbar}\chi_s,
\qquad w=(s,t),\quad w'=(s',s).
\]

The inherited adjacency uses rows as sources and columns as targets. A
non-palindromic itinerary is a mandatory transpose test.

The target theorem, initially for every fixed \(n\), is

\[
\operatorname{tr}\mathcal M_\hbar^n
=
\sum_{x\in\operatorname{Fix}(H_6^n)\cap\Lambda_*}
\frac{e^{iS_n(x)/\hbar-i\pi\mu_x/2}}
{\sqrt{|\det(I-DH_6^n(x))|}}
+O_n(\hbar).
\]

The existing symbolic conjugacy identifies the stationary points, and the
existing hyperbolicity certificate makes them nondegenerate.

With the stated Fourier branch, \(\mu_x\) is the negative inertia index of the
cyclic Hessian. The implementation must verify the signed identity

\[
\det D^2\Phi_n(x)=(-1)^{n-1}\det(I-DH_6^n(x)),
\]

with separate formulas/tests for \(n=1,2\), where cyclic variables coincide.

For a primitive orbit \(p\), write

\[
\Lambda_{u,p}=\sigma_p e^{T_p},
\qquad T_p=\log|\Lambda_{u,p}|,
\qquad \sigma_p\in\{\pm1\}.
\]

Then its \(r\)-fold trace amplitude is

\[
\frac1{\sqrt{|\det(I-DH_6^{rn_p})|}}
=\frac{e^{-rT_p/2}}{|1-\sigma_p^r e^{-rT_p}|}.
\]

This is the clean connection to the completed instability-roof project:
instability time, multiplier sign, and repetition correction jointly determine
the **amplitude**, while discrete action belongs in the **phase**. Neither
quantity is to be relabeled as a Riemann zero.

## Paper-level success criterion

The paper is viable if it delivers all of the following:

1. a checked proof of the quartic Weyl-law obstruction;
2. an exact convention-by-convention derivation of the Hénon generating
   function and unitary kernel, explicitly positioned relative to prior work;
3. a theorem for localized traces on the certified survivor, with either a
   rigorous fixed-period remainder or computer-assisted error bounds;
4. a reproducible Nyström/microlocal computation showing decreasing
   quantum--orbit trace error as \(\hbar\to0\), with cutoff and quadrature
   controls;
5. a Route-A evaluation that clearly states why this still does not provide a
   self-adjoint Hilbert--Pólya operator or an arithmetic trace identity.

The determinant and Ehrenfest-time extensions are stretch goals. No plot of
Riemann zeros can compensate for failure of items 1--4.

## Route-A position

| Criterion | Intended advance | Remaining limitation |
|---|---|---|
| A1: primitive orbits | Improves phase, multiplicity, repetition, and monodromy bookkeeping on certified local cycles | Still no prime-like correspondence or intrinsic arithmetic weights; remains A1_WEAK |
| A2: dynamical zeta | No intended advance from a fixed-time quantum trace | A target-free local trace check is not a \(\xi\)-divisor validation; retain the prior A2 status only for its original frozen object |
| A3: analytic structure | Proves a negative Weyl obstruction for the quartic surrogate | Fixed-time traces do not supply functional equation, Gamma factor, continuation, or \(T\log T\); remains A3_FAIL for an HP candidate |
| A4: natural lift | Specifies a natural unitary \(U_{a,\hbar}\) and chronological open localization | Quantization has phase/subprincipal choices; full-plane spectral type and open/cutoff dependence must be audited; at most A4_NATURAL_QUANTIZATION |

Expected verdict after a successful paper: an A4/operator clarification and a
sharper A3 obstruction, not a Route-A zeta success. **Route B remains
unauthorized**.

## Project files

- [SOURCE_AUDIT.md](SOURCE_AUDIT.md): claim-by-claim legacy and duplication audit.
- [PAPER_ROADMAP.md](PAPER_ROADMAP.md): theorem ladder, paper outline, and timeline.
- [refine-logs/FINAL_PROPOSAL.md](refine-logs/FINAL_PROPOSAL.md): frozen research proposal.
- [refine-logs/EXPERIMENT_PLAN.md](refine-logs/EXPERIMENT_PLAN.md): claim-driven computational plan.
- [refine-logs/EXPERIMENT_TRACKER.md](refine-logs/EXPERIMENT_TRACKER.md): run ledger and gates.
- [code/README.md](code/README.md): planned code interface.
- [results/README.md](results/README.md): artifact contract.
- [paper/README.md](paper/README.md): manuscript contract.
- [REPOSITORY_UPDATE.md](REPOSITORY_UPDATE.md): files added and current
  authorization boundary.

## Primary external references

- J. E. Fornæss and B. Weickert, *A quantized Hénon map*, DCDS 6
  (2000), 723--740. <https://doi.org/10.3934/dcds.2000.6.723>
- B. Weickert, *Spectral properties and dynamics of quantized Hénon maps*,
  Trans. AMS 356 (2004), 4951--4968.
  <https://doi.org/10.1090/S0002-9947-04-03475-0>
- R. H. G. Helleman, *Quantum levels of area-preserving maps*, Physica D 33
  (1988), 121--131. <https://doi.org/10.1016/S0167-2789(98)90014-8>
- A. Shudo and K. S. Ikeda, *Stokes geometry for the quantum Hénon map*,
  Nonlinearity 21 (2008), 1831--1850.
  <https://doi.org/10.1088/0951-7715/21/8/007>
- A. Shudo and K. S. Ikeda, *Toward pruning theory of the Stokes geometry for
  the quantum Hénon map*, Nonlinearity 29 (2016), 375--425.
  <https://doi.org/10.1088/0951-7715/29/2/375>
- D. G. Sterling, H. R. Dullin, and J. D. Meiss, *Homoclinic
  Bifurcations for the Hénon Map*, Physica D 134 (1999), 153--184.
  <https://arxiv.org/abs/chao-dyn/9904019>
- F. Faure, *Semi-classical formula beyond the Ehrenfest time in quantum
  chaos. (I) Trace formula*, Ann. Inst. Fourier 57 (2007), 2525--2599.
  <https://eudml.org/doc/10305>
- S. Nonnenmacher, J. Sjöstrand, and M. Zworski, *Fractal Weyl law for open
  quantum chaotic maps*. <https://arxiv.org/abs/1105.3128>
