# Independent Review — Round 1

## Review method

The external review MCP was unavailable.  Three independent secondary-agent
audits were therefore used as an explicit fallback: theorem-logic review,
dynamics/formula review, and fixed-energy trace review.  No proprietary
review score or nonexistent model verdict is reported.

## Initial verdicts

| Audit | Initial verdict | Main finding |
|---|---|---|
| Theorem logic | Accept only as conditional microlocal route | Inserting \(A_\hbar\) adds eigenfunction matrix elements, so the initial result was not determined by \(\xi_\hbar\). |
| Dynamics and normal form | Revise, minor proof completion | Every formula, sign, and constant agreed independently; exact Lyapunov-centre hypotheses and the full radial compactness proof had to be written. |
| Trace formula | Revise | Symbol data, fixed-point-set hypotheses, phase convention, remainder dependence, global H.2--H.3, and the exact project-to-CRR Fourier normalization had to be explicit. |

## Corrections implemented

1. Renamed the observable stage \(P^*_{\mathrm{loc,obs}}\) and stated that it
   is not an eigenvalue-only object.
2. Added the exact Lyapunov-centre eigenvalue ratios
   \(\pm1/\rho_a\notin\mathbb Z\), the amplitude-to-energy expansion, and an
   exact Section 4 source lock.
3. Inserted the complete Poincaré--Lindstedt solvability calculation and
   promoted the period slope to a proved proposition.
4. Inserted common-shell bounds and a complete bounded-time flow compactness
   proof for radial exclusion.
5. Specified \(\chi\), Weyl quantization of \(A\), \(g\), the exact stationary
   fixed-point cylinder, the CRR Maslov convention, and the nonuniform
   remainder.
6. Corrected the high-energy statement: the radial characteristic scale is
   exact, but no uniform period law has been proved for warped
   fixed-complexity orbits.
7. Proved A4.8 by a full-shell blow-up, limiting return classification,
   transverse Poincaré-map implicit-function theorem, iterate exclusion, and
   compactness globalization.
8. Used A4.8 and the strengthened radial exclusion to verify CRR H.1--H.5
   with observable symbol \(A_{\rm obs}\equiv1\), producing the
   eigenvalue-only Theorem A4.9.
9. Resolved CRR's two phase candidates by an Abel-regularized exact
   anisotropic-oscillator trace, obtaining \(+i\) at positive time and
   \(-i\) at negative time.
10. A final normalization audit caught a duplicated longitudinal
    orbit-measure factor.  Exact Poisson summation fixes the project-convention
    coefficient as \(T^\#/(2\pi\sqrt{|\det(I-P)|})\), not
    \(T^\#/\sqrt{|\det(I-P)|}\).  A4.7, A4.9, A4.10, the CRR checklist, and
    the refined proposal were corrected together.

## Post-revision status

- A4.4, A4.5, and A4.6: proof text complete; dynamics audit accepted the
  underlying derivations.
- A4.8: **ACCEPT** on focused second pass.  The reviewer confirmed the
  full-shell compactness, \(C^2/C^1\) convergence, limiting return
  classification, normalized Poincaré derivative, varying-section IFT,
  primitivity, globalization, and the strong equality \(T=T_+(E)\).
- A4.9: the theorem architecture, common threshold, finite-time CRR
  corollary, H.0--H.5 mapping, relative sign, determinant,
  eigenvalue-only status, and fixed-data \(O(\hbar)\) remainder were accepted
  on focused second pass.  Its absolute coefficient was then tightened by
  the final exact-oscillator normalization audit described above.
- A4.10: the phase result
  \(\sigma_+^{\mathrm{CRR}}=1\bmod4\) is accepted.  After the joint
  \(1/(2\pi)\) correction, the trace reviewer returned a final
  **ACCEPT** for the A4.9--A4.10 coefficient, sign, and convention.
- R400: unchanged immutable numerical archive; its role remains a
  high-sensitivity convention check, not the proof.
- Review-time regression: 61 tests collected and passed, including the
  positive/negative CRR phase oracle.  The current expanded suite has 65
  passing tests after the R401 implementation.
- Arithmetic P and Z gates: still open/unauthorized.

No numerical review score is assigned or fabricated.

## Final round-1 verdict

\[
\boxed{\text{ACCEPT A4.4--A4.10 AT FIXED ENERGY; ARITHMETIC P REMAINS OPEN.}}
\]

## Subsequent A4.11a focused audit

An independent read-only proof audit accepted the quantitative radial period
bound.  It verified the integration-by-parts sign, subtraction of
\(\nabla V(\bar q)\), use of convexity of the radial allowed disk, the Hessian
norm

\[
 V_0(q)(2\pi+4\pi^2|q|^2),
\]

and the uniform conclusion \(T>0.99\) for
\(0<\delta\le0.010201\).  Thus
\(\bar\delta(0.75)\ge0.010201\) is accepted; the
warped thresholds \(\delta_*\) and \(\delta_{\rm nd}\) remain unquantified.

A second focused audit accepted A4.11b after rejecting an earlier attempt to
apply the same Hessian bound directly on a nonconvex warped sublevel.  The
final proof instead encloses the whole allowed set in a convex box.  The
reviewer independently recomputed every outward endpoint, including

\[
 |f|<0.062114,
 \quad \|D\Psi_a\|_{\rm op}^2<2.368,
 \quad V_a<6.3716,
 \quad \|\nabla^2V_a\|_{\rm op}<102.494<103,
\]

and accepted the uniform conclusion \(T>0.60\) through
\(\delta=0.010201\).  The extension beyond \(0.01\) supplies a positive
endpoint margin for the R401-VAL protocol.  This closes only the
analytic short-time part; the validated global/local cover on
\([0.60,0.75]\) remains prospective.

## R401-VAL protocol review

The first focused protocol review returned **REVISE** because the original
cap \(\epsilon=0.1\) did not place \(\delta=0.01\) strictly inside A4.9's
open theorem domain.  It also required a validated `log1prel`, exact normal
coordinates, a no-gap phase-cover tree, connected \(Q_+\) monotonicity, and a
quantitative determinant/monodromy certificate.

The final protocol extends all analytic and validated targets to

\[
 \epsilon\le0.101,
 \qquad \delta\le0.010201,
\]

and implements each requested specification.  The second focused review
returned **ACCEPT** after four nonmathematical notation/status corrections;
those corrections were applied before freezing SHA-256
`d00d95f32ddfe4420da2cdac46ef1a3bb39bb3ea2277a21a9776652794a20d82`.
This accepts the protocol for a non-claiming implementation smoke, not a
validated full-shell result.
