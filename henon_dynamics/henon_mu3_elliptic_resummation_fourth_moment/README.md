# HCS-C50: elliptic resummation and the fourth Hénon moment

Status: **theorem, paper, certificate, and provenance frozen**

Implementation commit: `c5e21168576f90ad12296849c7e9817a2d608c26`.

HCS-C50 removes the second-moment absolute-convergence wall of the
Galois-normalized Fourier--cubic Hénon Euler germ and resolves the fourth
chronological moment. The two advances must be used together.

For the C48 genus-four curve over

\[
K=\mathbf Q(\rho)=\mathbf Q(\sqrt{-3}),\qquad \rho^2+\rho+1=0,
\]

explicit \(K\)-rational automorphisms generate \(C_2\times S_3\), and their
rational group-algebra idempotents give

\[
\operatorname{Jac}(C)\sim_K E_+^2\times E_-^2
\]

for elliptic curves \(E_\pm/K\). This is an isogeny, not a polarized
isomorphism. It turns the complete second logarithmic counterterm into the
integer-power Hasse--Weil factorization

\[
\exp\!\left(-\frac{\ell_2(s)}2\right)
=\zeta_K(2s+1)^7 L(H^1(C/K),2s+1)H_2(s),
\]

where \(H_2\) is holomorphic and nonzero on \(\Re s>0\). Modularity of
elliptic curves over \(K\) supplies entire continuation of the curve
\(L\)-function. The continued product can have zeros; no global logarithm
or zero-free statement is made after crossing \(\Re s=1/4\).

The fourth moment keeps the ordered eight-step phase

\[
\Phi_{p,4}=2\sum_{i=0}^7x_i^3+\sum_{i=0}^6x_ix_{i+1}+\rho x_7x_0.
\]

Its projective direction count involves a cubic sixfold \(S\), a split
quadric sixfold \(Q\), and the \((2,3)\) fivefold \(X=S\cap Q\). An exact
characteristic-zero Gröbner certificate proves that \(X/K\) is smooth.
At every good split prime,

\[
C_{p,4}=-2-\frac{2A_p}{p^3}-\frac{2B_p}{p^2},\qquad
c_{p,4}=\frac{2C_{p,4}}{p-1},
\]

where the primitive ranks are \(86\) and \(168\). Deligne's bounds yield

\[
|c_{p,4}|\le \frac{348+672\sqrt p}{p-1}=O(p^{-1/2}).
\]

The finite-bad-prime qualifier is essential: at \(p=181,\rho=48\), an
explicit nonzero singular point disproves all-split smoothness.

Combining the exact elliptic resummation with the fourth-moment estimate
gives

\[
\boxed{\mathcal G^{\mathrm{cont}}(s)\text{ holomorphic on }\Re s>1/5.}
\]

Zeros are allowed. In the inherited normalized semifinite category this
has a tenth-order graded regularized determinant with nine chronological
counterterms. It is not a classical Fredholm determinant. On the ordinary
Hilbert direct sum the corresponding fixed integer Schatten order is
\(15\), and the classical trace records the unnormalized Galois norm.

## Route A

The evaluator-compatible tuple is

\[
(\mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

The overall status is **ROUTE_A_EXPLORATORY**, and Route B is not authorized.
The A3 evidence records
**holomorphic_continuation: PROVED_RE_GT_1_5**;
only the extracted elliptic factor has a known functional equation. The
project proves neither a full Hénon functional equation, a Gamma factor, a
Riemann divisor, nor a self-adjoint Hilbert--Pólya operator.

## Files

- **THEOREM_PACKAGE.md**: theorem statements and precise scope;
- **DERIVATION_PACKAGE.md**: chronological, arithmetic, and analytic derivation;
- **PROOF_PACKAGE.md**: exact automorphism, Gröbner, and convergence proofs;
- **SOURCE_AUDIT.md**: primary-source and novelty firewall;
- **NARRATIVE_REPORT.md**: concise research narrative;
- **PAPER_PLAN.md**: claim-to-section map;
- **METHODOLOGY_BLUEPRINT.md**: reproducibility and kill gates;
- **INTEGRITY_REPORT.md**: proof/source/checker/PDF scope audit;
- **paper/main.pdf**: compiled manuscript;
- **paper/COMPILATION_REPORT.md**: release-grade PDF build audit;
- **route_a_evaluation.yaml**: evaluator-compatible Route-A record;
- **evaluations/route_a/HCS-C50/20260814T040000Z.yaml**: byte-identical
  archived Route-A record.
