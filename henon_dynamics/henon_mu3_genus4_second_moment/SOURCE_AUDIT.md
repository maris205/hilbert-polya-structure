# HCS-C48 source and novelty audit

## Classical inputs

- Projective direction counting is elementary.
- The point count of a split cubic surface follows from its realization as the
  blow-up of \(\mathbf P^2\) in six rational points.  A direct frozen locator
  is Massarenti, *Trans. London Math. Soc.* 13 (2026), Corollary 8.3,
  DOI `10.1112/tlm3.70028`, arXiv `2406.07223`.
- A smooth split quadric surface is \(\mathbf P^1\times\mathbf P^1\).
- Adjunction gives genus \((a-1)(b-1)\) for a smooth \((a,b)\) curve on
  \(\mathbf P^1\times\mathbf P^1\).
- The Hasse--Weil bound gives \(|a_p|\le2g\sqrt p\); see Stichtenoth,
  *Algebraic Function Fields and Codes*, second edition, Theorem 5.2.3,
  DOI `10.1007/978-3-540-76878-4`.
- Schatten regularized determinants and prime-series comparison are standard.

The operator terminology follows the inherited C47 convention.  The symbols
\(L^q(\mathcal M,\tau)\) refer to noncommutative \(L^q\)-spaces for the
field-degree-normalized faithful semifinite trace, whereas
\(S^q(\mathcal H)\) refers to the classical Schatten ideal for the ordinary
Hilbert-space trace.  They are deliberately not identified: their sharp
thresholds are respectively \(q\Re s>2\) and \(q\Re s>3\).

Exact locators used in the paper are:

- Massarenti, Corollary 8.3, for
  \(\#S(\mathbf F_p)=p^2+7p+1\) for the split Fermat cubic surface;
- Hartshorne, Chapter V, Section 1, Proposition 1.5 and Example 1.5.2,
  for adjunction and \(g=(a-1)(b-1)\) on a smooth quadric;
- Stichtenoth, Chapter 5, Section 5.2, Theorem 5.2.3, for the
  Hasse--Weil bound; and
- Simon, Chapter 9, for regularized determinant background.

The frozen Hénon identities and the uniform four-chart smoothness
certificate are proved directly.

## Search-bounded novelty statement

Searches through 2026-08-13 found no source identifying the Galois-normalized
second moment of the Fourier--cubic Hénon sector determinant with this explicit
genus-four \((3,3)\) curve, nor using that identity to move the corresponding
Euler/regularized-determinant abscissa from \(1/2\) to \(1/3\).  Novelty is
therefore claimed only for that source-locked bridge and its analytic
consequence, not for the classical algebraic-geometry or determinant inputs.

## Firewall

The result does not claim a natural boundary, functional equation, Gamma
factor, Riemann-zero match, or self-adjoint Hilbert--Pólya operator.  It does
not infer an all-(n) motive from the single genus-four calculation.
