# Paper 6 independent peer review — Round 1 and final gate

**Manuscript:** *Which Operator Owns the Zeta? Koopman and Frobenius
Ledgers of an Arithmetic Suspension*  
**Review date:** 2026-08-13  
**Review mode:** independent adversarial mathematical, operator, Route,
source, artifact, and release review  
**Final recommendation:** **ACCEPT**  
**Confidence:** **5/5**  
**Issue count:** **0 critical / 0 major / 0 residual required minor**

## 1. Final submission lock

- `paper/manuscript.tex` SHA-256:
  `d36783ebbfabd67fdda7f04d1aae3556e72b137e51985b7cd6448a35f0cb8219`.
- `paper/references.bib` SHA-256:
  `9cae6271cefad92c78de9a4cb9533fb12503760e11f05b3f06d240cef1c67e05`.
- `paper/manuscript.pdf` and `paper/paper.pdf` SHA-256:
  `f8eccdd7d486a10885d6f5502ad929f08d5ce27b14cb2457f1de8999b9f14573`.
- The release PDFs are byte-identical and have nine US-Letter pages.
- `results/manifest.sha256.json` SHA-256:
  `4a78e430d08134bca09b88b4e5f3adf25b68692212893f6abeaad407d1711c16`.

## 2. Mathematical verdict

The complete theorem chain passes independent checking.

1. Möbius inversion gives
   \(a_1=3\) and
   \(d a_d=\sum_{e\mid d}\mu(e)2^{d/e}\) for \(d>1\). The lower bound
   \[
   d a_d\ge 2^d-\sum_{m=1}^{\lfloor d/2\rfloor}2^m
   =2^d-2^{\lfloor d/2\rfloor+1}+2>0
   \]
   is valid for every \(d\ge2\), so the later use of a closed-point circle
   in every degree is theorem-level and not inferred from a cutoff.
2. The point, primitive-cycle, and cohomological ledgers are correctly kept
   distinct and then related by Deligne's theorem:
   \[
   \sum_{d\mid n}d a_d=\#\mathbb P^1(\mathbb F_{2^n})
   =1+2^n=\sum_i(-1)^i\operatorname{Tr}(\Phi^n\mid H^i_{\rm et}).
   \]
   Logarithmic expansion gives the stated Euler product and alternating
   graded determinant, with signs, repetitions, and the convergence region
   \(|t|<1/2\) correct. For the frozen projective line the two nonzero trace
   eigenvalues are \(1\) and \(2\), hence
   \(Z(X,t)=((1-t)(1-2t))^{-1}\).
3. The Hilbert direct sum, weighted inner products, translation action,
   periodic boundary conditions, and maximal square-summable graph domain
   of \(A_w=-i\,d/du\) are explicit. Component Fourier transform and the
   countable orthogonal-sum theorem prove self-adjointness on exactly that
   domain. The sign agrees with the frozen Stone convention
   \(U_t=e^{-itA_w}\), and multiplication by \(\sqrt{w_x}\) proves unitary
   equivalence for every family \(0<w_x<\infty\).
4. The component Fourier lattices have union
   \((2\pi/\log2)\mathbb Q\). For a reduced rational \(a/b\), degrees \(kb\)
   and modes \(ka\) yield infinitely many orthogonal witnesses, so every
   point eigenvalue has countably infinite multiplicity. Closure gives the
   full spectrum \(\mathbb R\); infinite-multiplicity rational eigenspaces
   and singular Weyl sequences at irrational limits give
   \(\sigma_{\rm ess}(A_w)=\mathbb R\) and
   \(\sigma_{\rm disc}(A_w)=\varnothing\). The manuscript correctly
   distinguishes pure-point vector spectral measures from the set-theoretic
   continuous spectrum at irrational accumulation points.
5. The infinite-dimensional zero eigenspace proves noncompact resolvent and
   non-trace-class Gaussian heat. Repeating the argument on any nonzero
   rational eigenspace proves that deleting the kernel repairs neither
   defect. Every positive-width interval contains such an eigenvalue and
   therefore has infinite-rank spectral projection.
6. Operator ownership is stated at the right type level. The exact native
   determinant belongs to finite-dimensional graded \(\mathbb Q_\ell\)-linear
   Frobenius \(\Phi\), while suspension time belongs to the complex
   self-adjoint operator \(A_w\). Their scalar provenance does not produce a
   unitary equivalence. A finite-dimensional complex realization added as a
   direct summand cannot remove the infinite-multiplicity eigenspaces,
   essential spectrum, noncompact resolvent, or heat obstruction of
   \(A_w\).
7. Solving \(1-\alpha2^{-s}=0\) gives
   \(s=(\log\alpha+2\pi i k)/\log2\), after renaming the integer sign. Thus
   the inverse factors have pole preimage lattices on real parts zero and one
   with period \(2\pi i/\log2\). The manuscript correctly refuses to call
   these preimages new Frobenius eigenvalues or self-adjoint energies.

## 3. Strongest counter-argument and adjudication

The strongest attempted repair is to treat the common arithmetic parent as
permission to take self-adjointness from \(A_w\) and the exact trace or
determinant from \(\Phi\). That does not satisfy Route B: the scalar fields,
spaces, domains, spectra, trace operations, and determinant notions belong to
different operators. A finite-dimensional block sum makes the two ledgers
coexist but supplies no intertwining trace theorem and leaves the entire
Koopman essential-spectrum obstruction intact.

Accordingly, the no-merger result is proved for the two frozen operators and
their finite-block repair. It is not a universal no-go theorem for a new
cohomological flow, anisotropic completion, coupling, relative trace, or
source-derived operator bridge. The manuscript states this boundary
consistently.

## 4. Frobenius convention and Route audit

The final manuscript fixes an auxiliary \(\ell\ne2\), defines
\(\Phi=F^*\) to be exactly the pullback in Deligne equations
(1.5.1)--(1.5.4), and distinguishes this geometric-Frobenius cohomological
convention from the displayed square point map \(a\mapsto a^2\). Inverting
the point permutation only reverses finite cycles and does not change degrees
or suspension lengths. The trace eigenvalue \(2\) on \(H^2\), rather than
\(1/2\), is therefore conventionally and algebraically correct.

Both Stage-6 YAML files parse and preserve the target scopes:

- native finite-field Route A:
  `ROUTE_A_SUCCESS_ROUTE_B_NOT_READY` as a scoped positive control;
- unchanged construction against the Riemann target:
  `ROUTE_A_REJECTED`;
- project-lead-authorized limited Route-B audit:
  `(B1_COMPLETE_OPERATOR_DEFINITION, B2_SELF_ADJOINT, B3_FAIL,
  B4_FAIL, B5_FAIL)`, overall `ROUTE_B_REJECTED`, with
  `hilbert_polya_claim_allowed: false`.

Unlike Paper 5's B1--B3-only audit, Stage 6 explicitly authorizes evaluation
through B5. The B4 failure is scoped to the missing **same-operator
rational-prime/von-Mangoldt trace and Weil bridge** for \(A_w\); it does not
deny the native characteristic-two Lefschetz trace owned by \(\Phi\), and it
does not assert that every conceivable regularized trace is impossible. B5
fails because no determinant of the same self-adjoint operator equals
completed \(\xi\), while the native cohomological determinant has the proved
wrong divisor. No coordinatewise Route certificate is assembled across the
two owners.

## 5. Required minor revisions — closed before final lock

1. The manuscript now introduces \(\ell\ne2\) and \(\Phi\) before their use
   and explicitly fixes Deligne's pullback/geometric-Frobenius convention
   against the square point map. **Addressed.**
2. The Koopman 1931 bibliography title now reads “Hamiltonian Systems and
   Transformations in Hilbert Space,” matching the local original scan.
   **Addressed.**

No required action remains.

## 6. Citation and source-claim verdict

All six bibliography entries are cited, and the final BibTeX log is clean.
The local source hashes agree with `source_audit.md`. Direct source inspection
confirms the load-bearing mappings: Deligne Section 1.4 and equations
(1.5.1)--(1.5.4) support the closed-point, trace, and graded-determinant
ledger; the Stacks trace chapter confirms the Frobenius convention and the
degree-two action on \(\mathbb P^1\); Teschl Theorem 2.23 supports
self-adjoint orthogonal sums and spectral closure; Teschl Theorems 5.1--5.2
support the Stone convention; and Koopman/ter Elst--Lemanczyk support only the
unitary pullback framework.

The candidate-specific degree, multiplicity, Weyl-sequence, heat, and
finite-block results are proved in the manuscript rather than delegated to
citations. No source is used to turn an \(\ell\)-adic vector space into a
canonical complex Hilbert space or to promote the native determinant to a
Hilbert--Pólya determinant. **Citation verdict: PASS.**

## 7. Reproduction and release checks

- `bash experiments/reproduce.sh`: **10/10 tests passed**; rerunning it left
  every generated output hash unchanged.
- All five artifacts match `results/manifest.sha256.json`; the cycle, point,
  and cohomological rows agree through degree/iterate 24.
- The controls use exact integer/rational arithmetic and no target zeros,
  fitting, randomness, network input, or floating root finder. Finite tables
  are correctly described as regressions rather than proofs of the infinite
  spectral theorems.
- A clean independent XeLaTeX/BibTeX build succeeds at nine pages. Extracted
  text agrees with the release; there is no unresolved citation/reference,
  missing character, overfull box, or compilation error. One underfull-box
  notice in the deterministic-controls paragraph is nonblocking.
- `pdfinfo` and `pdftotext` succeed. All nine final pages were rasterized and
  inspected; the title page, ownership figure, tables, domains, theorem
  displays, status tokens, CJK text, artifact map, bibliography, and URLs are
  legible with no clipping or overlap. The status-adjacency scan is clean.
- The ARS parser preflight remains **UNAVAILABLE** solely because `pypdf` is
  not installed; this was not promoted to a pass. The review instead uses
  verified source equation/theorem locators and independent Poppler checks.

## 8. Final adjudication

No critical, major, or residual required minor issue remains. The paper gives
a correct native Lefschetz positive control and a complete self-adjoint
Koopman operator, then proves that their analytic ownership cannot be merged
into one Route-B certificate. The spectral obstruction, divisor calculation,
source conventions, Route scopes, deterministic artifacts, and release PDF
are mutually consistent.

**FINAL GATE: ACCEPT.**
