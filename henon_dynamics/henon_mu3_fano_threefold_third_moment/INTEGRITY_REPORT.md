# HCS-C49 research-integrity report

**Audit date:** 2026-08-14 UTC

## Mathematical and computational integrity

- The six-step Hénon phase is composed chronologically; no transition
  averaging or period/Frobenius identification is used.
- The finite-field and projective counts use exact integer arithmetic.  No
  fitted parameter, floating threshold, or Riemann-zero table enters the
  certificate.
- The released ledger contains all 21 split primes through 199 and literal
  six-step chronological controls for the seven split primes through 61.
- The independent checker does not import the producer.  It uses different
  affine charts, a reverse chronological recurrence, and a separate
  dictionary dynamic program.
- The certificate SHA-256 before the final artifact-manifest freeze is
  `b3ec1bf12ea0f05469054fda37bd34ee4b6748030813c8c6407752035a3c25d2`;
  its payload SHA-256 is
  `fc29fccc6a7281008b211a7c8b8e34d4a03e6cfe42c4d4f0bafe628eadcc5791`.
- The independent-check SHA-256 is
  `e26749a89341c66c41bac31ee80da1623e6641bead123222ed932b16d50d15f2`.
  The checker reports 13/13 gates and the regression suite reports 55/55
  passing tests, including deliberate mutations.

## Source and citation integrity

The manuscript bibliography contains six entries.  Every entry is cited;
there are no dangling citations or unused bibliography rows.  Each was
checked against a primary or official source:

- Deligne, Théorème 1.6, for Frobenius weights;
- Weil, pp. 499--502 and 505--506, and Brünjes, Definition 4.4,
  Proposition 4.5, Theorem 4.6, and Example 4.7, for the diagonal/Jacobi
  framework;
- Warning's original theorem, with the needed divisibility also reproved in
  `PROOF_PACKAGE.md`;
- Bloch--Murre only for classical quadric--cubic Fano context;
- Simon, Chapter 9, only for classical regularized-determinant background.

The coefficient twenty, the sign and normalization of the six-variable
specialization, the Fano Betti number, the normalized semifinite trace, the
seven counterterms, and the graded `Det_8` identity are internal derivations;
the package does not outsource them to those references.  Exact links and
locators are frozen in `SOURCE_AUDIT.md`.

## Smoothness and evidence boundary

The released theorem requires only characteristic-zero smoothness and the
resulting finite set of bad reductions.  The finite prime ledger is a
control, not a proof that every split prime is good.  A stronger all-split
elimination is retained as an explicit open release strengthening and is
not used in the Euler-convergence theorem.

## Search-bounded novelty audit

Searches of arXiv and the open web covered 1 January 2024 through 14 August
2026 and were last run on 14 August 2026.  They found no work combining this
exact six-step Hénon third moment with the Fermat cubic-fourfold/
quadric--cubic Fano stratification and the resulting `Re(s)>1/4`
normalized-semifinite `Det_8` realization.  This is a bounded search result,
not a claim of global priority.

The closest components found separately were recent work on Fermat motives
and Jacobi sums, arithmetic Hénon periodic points, rational points on
even-dimensional Fermat cubics, and a repository preprint coupling Hénon
bifurcation pictures to RH.  None contained the complete finite-field
moment--Fano--Euler--operator chain above.  Classical Jacobi sums, Weil
bounds, Chevalley--Warning, Fano geometry, and regularized determinants are
credited as prior theory rather than novelty.

## Originality sampling

Eleven of 21 substantive prose blocks (52.4 percent) were randomly sampled.
Twelve distinctive 6--12-word fragments from those blocks were searched on
the public web; no exact or close textual match was found.  This is a
heuristic public-web check and does not replace iThenticate or Turnitin.

## Claim firewall

The project proves an exact third-moment cohomological cancellation, normal
convergence of the normalized Euler germ on `Re(s)>1/4`, and its canonical
eighth-order normalized-semifinite graded determinant realization.  It does
not prove a functional equation, meromorphic continuation through that
half-plane boundary, a Riemann-zero divisor, or a self-adjoint
Hilbert--Pólya operator.  Route A therefore remains exploratory.

## Manuscript integrity

The manuscript was rebuilt after its final source revisions.  It has six A4
pages, all fonts embedded, no undefined citation/reference, no box warning,
and no unresolved verification marker.  Its PDF SHA-256 is
`3968a846b236b3395dac2cb855b48a568793c16b8cc5c3c73011b6136196818a`;
the detailed build ledger is `paper/COMPILATION_REPORT.md`.
