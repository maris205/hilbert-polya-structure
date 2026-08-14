# HCS-C49 — Fano threefold third moment

HCS-C49 resolves the third chronological-moment wall left by C48.  For the
ordered six-variable Hénon phase

\[
2\sum_{i=0}^5x_i^3+x_0x_1+x_1x_2+x_2x_3+x_3x_4+x_4x_5+\rho x_5x_0,
\]

projective directions split into a Fermat cubic fourfold \(S\), a split
quadric fourfold \(Q_\rho\), and their \((2,3)\) Fano threefold intersection
\(X_\rho\).

At every smooth split fibre,

\[
C_{p,3}=-2-\frac{2A_p}{p^2}-\frac{2B_p}{p},
\]

where \(A_p\) is the rank-22 primitive \(H^4\) trace of \(S\) and \(B_p\)
is the rank-40 \(H^3\) trace of \(X_\rho\).  More precisely,

\[
A_p=20p^2+pa_p,\qquad B_p=pb_p,
\]

with \(|a_p|\le2p\), \(b_p\in\mathbf Z\), and
\(|b_p|\le40\sqrt p\).  Therefore

\[
c_{p,3}=-\frac4{p-1}(21+b_p+a_p/p)=O(p^{-1/2}).
\]

The normalized \(O(1)\) obstruction does not occur.  Combining this with
C48 moves the canonical Euler germ and its normalized-semifinite operator
realization from \(\Re s>1/3\) to

\[
\boxed{\Re s>1/4},
\]

where the natural regularized object is
\(\operatorname{Det}_{8,\tau,\mathrm{gr}}\).

The theorem-level smoothness statement allows finitely many bad reductions;
finite local factors do not alter the half-plane.  An exact resultant and
leading-coefficient audit is designed to promote this to smoothness at
every split prime \(p>3\), but that all-split sentence remains a release
gate until the independent certificate is replayed.

## Route A

\[
(\mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

Overall: `ROUTE_A_EXPLORATORY_FANO_THREEFOLD_QUARTER_ABSCISSA`.

This is not continuation through \(\Re s=1/4\), a functional equation, a
Riemann divisor, or a self-adjoint Hilbert--Pólya generator.

## Files

* `THEOREM_PACKAGE.md` — frozen statements and normalizations.
* `PROOF_PACKAGE.md` — full radial, character-sum, smoothness, and
  convergence derivations.
* `SOURCE_AUDIT.md` — primary-source locators and claim mapping.
* `METHODOLOGY_BLUEPRINT.md` and `EXPERIMENT_PLAN.md` — exact replay plan.
* `NARRATIVE_REPORT.md` and `PAPER_PLAN.md` — research interpretation and
  manuscript structure.
