# HCS-C32 Research Question Brief

## Topic Area

Arithmetic quantization of the integral area-preserving Hénon map, with
chronology-preserving quantum traces and Artin--Schreier Frobenius spectra.

The source map is

\[
H_6(q,p)=(1-6q^2-p,q),
\]

and its integral type-I generating function is

\[
S_6(q,Q)=qQ-q+2q^3.
\]

This stage does not inherit target zeros, prime-fitted weights, averaged
transition matrices, or an identification of dynamical time with Frobenius
degree.

## Primary Research Question

For each prime \(p>3\), can all Hénon-time powers of the finite-field \(H_6\) cubic-phase unitary be realized as categorical traces of convolution powers of one gauge-projective Artin--Schreier kernel, whose fixed-time nontrivial-character cohomology has rank \(2^n\), pure weight \(n\), and the required \((-1)^n\) Frobenius supertrace?

## FINER Assessment

| Criterion | Score | Justification |
|---|---:|---|
| Feasible | 4/5 | Unitarity, the path-sum trace, the critical equations, and gauge covariance are exact algebra.  The highest homogeneous cubic is smooth at infinity for \(p>3\), placing the fixed-time cohomology claim within a sharply identifiable theorem class.  The fixed-kernel convolution and categorical-trace conventions still require a primary-source proof audit. |
| Interesting | 5/5 | The same object contains a Hénon canonical relation, genuine ordered time, an exact finite-dimensional unitary, and nonzero-dimensional arithmetic cohomology. |
| Novel | 4/5 provisional | No repository project implements this finite-field Fourier--cubic Hénon trace package.  The individual Fourier and Deligne ingredients are classical, so Phase 2 must test whether the combined Hénon trace-duality theorem already exists. |
| Ethical | 5/5 | This is target-blind mathematical research using no human subjects or personal data.  The main ethical obligation is accurate claim scope. |
| Relevant | 5/5 | It directly addresses the missing canonical arithmetic-fibre gate after HCS-C31 while remaining inside the Hénon family and preserving chronology. |
| **Average** | **4.6/5** | The direction passes the FINER threshold, subject to the Phase-2 novelty and categorical-trace gates. |

## Scope Boundaries

### In Scope

- The integral map \(H_6\) and the source-normalized phase
  \(S_6(q,Q)=qQ-q+2q^3\).
- Prime-power fields \(k_r=\mathbb F_{p^r}\) with \(p>3\), equipped with
  the trace-compatible additive character
  \[
  \psi_r(x)=\exp\!\left(
  \frac{2\pi i}{p}\operatorname{Tr}_{k_r/\mathbb F_p}(x)
  \right).
  \]
- The complex Hilbert space \(\ell^2(k_r)\) and the kernel
  \[
  U_r(Q,q)=|k_r|^{-1/2}\psi_r(qQ-q+2q^3).
  \]
- One sheaf kernel
  \[
  \mathcal K_p=\mathcal L_{\psi(S_6)}
  \quad\text{on}\quad
  \mathbb A^1\times\mathbb A^1,
  \]
  its chronological convolution powers, and the explicitly defined diagonal
  compact-support trace complex.
- Exact matrix chronology in \(\operatorname{Tr}(U_r^n)\), including the
  collided-variable conventions at \(n=1\) and doubled neighbor occurrence
  at \(n=2\).
- The two independent axes
  \[
  n=\text{H\'enon dynamical time},\qquad
  r=\text{Frobenius extension degree}.
  \]
- Gauge covariance under
  \(S\mapsto S+G(Q)-G(q)+C\).
- Artin--Schreier cohomology of the chronological phase
  \[
  \Phi_n(x_0,\ldots,x_{n-1})
  =\sum_{i\in\mathbb Z/n\mathbb Z}
  (x_ix_{i+1}-x_i+2x_i^3).
  \]
- One fixed nontrivial \(\ell\)-adic character
  \(\psi_0:\mathbb F_p\to\overline{\mathbb Q}_\ell^\times\) and the
  nontrivial isotypic sheaf
  \(\Phi_n^*\mathcal L_{\psi_0}\), not the cohomology of the full
  Artin--Schreier cover.
- A theorem-level comparison with the already certified rank-\(2^n\)
  Hénon fixed scheme and cyclic Hill identity.
- Exact low-degree computational checks used as theorem-interface tests, not
  as evidence for Riemann-zero matching.

### Out of Scope

- Primes \(2\) and \(3\); the cubic-at-infinity hypothesis and the source
  Hénon degree change there.
- Any diagonal identification \(r=n\), including
  \(\operatorname{Tr}(U_{p^r}^n)=\operatorname{Tr}(U_p^{rn})\).
- Averaging chronological couplings or replacing \(x_ix_{i+1}\) by a
  transition-frequency statistic.
- Claiming that the normalized Frobenius phases are the complete spectrum of
  \(U_{p^r}\).  They belong to a fixed-\((p,n)\) cohomology group.
- A global Euler product over \(p\), a cross-prime compatible system, or a
  single infinite-dimensional Hilbert--Pólya operator.
- Inferring that the changing groups \(H_c^n\) form the powers of one fixed
  finite-dimensional Frobenius representation.  Their cross-time relation
  must come only from convolution powers of the single kernel
  \(\mathcal K_p\).
- Equating finite-flat scheme length \(2^n\) with
  \(\#\operatorname{Fix}(H_6^n)(\mathbb F_p)\), or claiming a canonical
  orbit-indexed cohomology basis.  Rational point counts vary, and some
  \((p,n)\) critical schemes may be Hessian-degenerate.
- Treating purity as Frobenius semisimplicity, a positive Hilbert structure,
  or a self-reciprocal local polynomial.  Duality pairs the \(\psi_0\) and
  \(\psi_0^{-1}\) sectors in general.
- Riemann-zero data, zero fitting, prime fitting, or Route B.
- A full exact Egorov theorem for nonlinear observables.
- Identification with the real four-state survivor of HCS-C31.  The same
  integral Hénon map is used, but the finite-field phase space is a distinct
  realization.
- Treating an absolute eigenphase as a classical invariant.  The source map
  determines a projective gauge class unless an extra quantum normalization
  is supplied.

### Key Assumptions

- The standard smooth-at-infinity theorem for degree-three
  Artin--Schreier exponential sums applies exactly after its hypotheses and
  Frobenius convention are verified from primary sources in Phase 2.
- Algebraic and geometric Frobenius will be distinguished explicitly; no
  sign or reciprocal-root convention will be inferred from memory.
- The Grothendieck trace sign \((-1)^n\) is part of the object.  For odd
  \(n\), the cohomological expression is a supertrace/virtual sign, not the
  ordinary power trace of a newly declared positive-rank operator.
- Division by \(p^{n/2}\) is an analytic normalization of complex absolute
  values.  For odd \(n\), it is not silently promoted to a canonical
  half-Tate twist.
- The equality of the fixed-scheme length and the cohomology dimension,
  both \(2^n\), is initially a structural lead rather than proof of a
  canonical basis correspondence.
- Standard Fourier--chirp unitarity and standard purity are baselines.  A
  promotable Hénon result must also retain the exact critical-scheme and
  Hill-determinant bridge.
- The phrase "categorical trace" means the displayed diagonal
  compact-support construction, not an unspecified categorical determinant.

## Sub-questions

1. Does one Artin--Schreier kernel \(\mathcal K_p\) produce the kernels of all
   powers \(U_r^n\) by chronological convolution, with exact unitarity,
   canonical relation, and projective gauge covariance at the function
   level?
2. Is the diagonal compact-support trace of \(\mathcal K_p^{\star n}\)
   exactly the Artin--Schreier complex of \(\Phi_n\), with concentration in
   degree \(n\), dimension \(2^n\), purity of weight \(n\), and the correctly
   signed \((-1)^n\) two-axis Frobenius supertrace identity?
3. Does the identification
   \(\operatorname{Crit}(\Phi_n)=\operatorname{Fix}(H_6^n)\), together with
   the cyclic Hill identity, provide a Hénon-specific theorem delta that is
   not reproduced by uncoupled or generic cubic-chirp controls?

## Sub-Question Bindings

1. **Inherits:** map \(H_6\); primes \(p>3\); all \(r,n\geq1\); standard
   additive character; projective gauge class; exact chronology.
   **Deviations:** none.
2. **Inherits:** the same \((p,r,n)\) axes and phase \(\Phi_n\); primary-source
   theorem verification; no global Euler product. **Deviations:** none.
3. **Inherits:** the same map, phase, prime range, gauge, and no-target-data
   firewall.  Computational controls may be evaluated only on the frozen
   low-degree grid. **Deviations:** none.

## Candidate Questions Considered

| # | Candidate | FINER average | Why not selected |
|---:|---|---:|---|
| 1 | Finite-field \(H_6\) unitary--Artin--Schreier kernel trace duality | **4.6** | Selected: it asks for one kernel across all Hénon times, an exact operator, and a nonzero-dimensional arithmetic fibre. |
| 2 | Classify all finite-dimensional algebraic \(mathrm{SL}_2\) derivative twists | 4.4 | High-feasibility negative theorem, but characters of \(\operatorname{Sym}^k\) are expected to collapse to shifted instability factors and add no arithmetic object.  Retain as the first pivot. |
| 3 | Prove the real action cocycle is nonzero modulo \(1\), the instability roof, and Livšic coboundaries | 4.2 | Nonduplicative reopening of C05, and likely quickly certifiable, but it produces only a new Hölder phase direction.  Retain as a real-side auxiliary gate. |
| 4 | Construct an all-period dynatomic Frobenius--Hénon compatible tower | 3.7 | Highest arithmetic ambition but presently lacks a frozen cross-period correspondence and risks repeating C12A--C23 obstructions. |

## Stage-1 Decision

Proceed to a primary-source and equivalence audit before implementation.  The
candidate advances only if the combined Hénon--Artin--Schreier trace theorem
is not a direct prior-work collision and if the Hénon-specific
critical/Hill bridge survives the generic cubic controls.
