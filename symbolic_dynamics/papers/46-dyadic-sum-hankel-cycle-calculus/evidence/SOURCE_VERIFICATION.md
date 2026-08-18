# P46 primary-source verification — WRITER PREFLIGHT

Verification date: 2026-08-18 UTC.

This is a source-location and ownership check for the eventual manuscript.
It does not rerun the frozen collision search and does not turn a bounded
search absence into novelty evidence. Metadata was checked against primary
publisher/repository records and DOI content negotiation.

## Verified records

1. **V. V. Peller**, “A Description of Hankel Operators of Class
   `S_p` for `p>0`, an Investigation of the Rate of Rational Approximation,
   and Other Applications,” *Mathematics of the USSR-Sbornik* 50(2)
   (1985), 465--494, DOI
   `10.1070/SM1985v050n02ABEH002840`.
   - Checked at MathNet (`https://www.mathnet.ru/eng/sm2310`) and through
     DOI BibTeX content negotiation.
   - Verified scope: classical Hankel Schatten/Besov and
     Schatten--Lorentz classification machinery.
   - Manuscript use: generic operator-ideal background only; no ownership
     attribution for the frozen dyadic-weighted phase diagram.

2. **Vladimir Peller**, *Hankel Operators and Their Applications*,
   Springer Monographs in Mathematics, Springer New York (2003), DOI
   `10.1007/978-0-387-21681-2`.
   - Checked at the official Springer book record
     (`https://link.springer.com/book/10.1007/978-0-387-21681-2`) and through
     DOI BibTeX content negotiation.
   - Verified scope: general Hankel operators, singular values, and
     Schatten--von Neumann classes.
   - Manuscript use: standard context, not a source for the arithmetic
     support, valuation blocks, or cycle theorem.

3. **John J. F. Fournier and Bradley G. Wagner**, “Paley's theorem for
   Hankel matrices via the Schur test,” arXiv:1505.01760 (2015).
   - Checked against the primary arXiv record and API
     (`https://arxiv.org/abs/1505.01760`). The author list, title, date, and
     abstract match the frozen audit.
   - Verified scope: lacunary Hankel boundedness through Schur-test
     arguments in the Paley setting.
   - Manuscript use: preserve ownership of Schur/reflection/folding/
     alternating lacunary machinery exactly as frozen; novelty credit for
     P46 on those ingredients is zero.

4. **Max A. Alekseyev**, “Maximizing the number of integer pairs summing to
   powers of 2 via graph labeling and solving restricted systems of linear
   (in)equations,” *Journal of Computer and System Sciences* 157 (2026),
   article 103735, DOI `10.1016/j.jcss.2025.103735`.
   - Checked at the official Elsevier record and DOI BibTeX endpoint; the
     related preprint is arXiv:2303.02872 under its earlier title.
   - Verified scope: finite distinct-integer graph labeling and restricted
     linear systems in powers of two.
   - Manuscript use: finite combinatorial context only; it does not own the
     canonical infinite weighted operator, its Schatten walls, or the trace
     determinant ledger.

5. **Ying-Jun Guo**, “On the regularity of the Hankel determinant sequence
   of the characteristic sequence of powers of 2,” *Advances in Applied
   Mathematics* 104 (2019), 100--116, DOI
   `10.1016/j.aam.2018.12.001`.
   - Checked at the official Elsevier record and DOI BibTeX endpoint.
   - Verified scope: regularity of a finite Hankel-determinant sequence
     formed from the characteristic sequence of powers of two.
   - Manuscript use: finite determinant context only; it does not authorize
     claims about the present infinite Dirichlet-weighted operator.

6. **Barry Simon**, *Trace Ideals and Their Applications*, 2nd ed.,
   Mathematical Surveys and Monographs 120, American Mathematical Society,
   Providence, RI (2005), DOI `10.1090/surv/120`.
   - Checked at the official AMS record
     (`https://bookstore.ams.org/surv-120-s`); Chapter 9 is the regularized
     determinant chapter.
   - Manuscript use: standard trace-ideal and regularized-determinant
     machinery. The paper should reproduce the exact `det_2` direct-sum
     argument and use the citation only for the standard definition and
     convergence framework.

## Claim-level citation firewall

- Peller and Simon may support general definitions and standard theorems;
  neither is cited as proving the exact `0,1/2,1` walls for this matrix.
- Fournier--Wagner is credited for its lacunary Schur machinery, not treated
  as an exact collision with the two-sided Dirichlet weighting.
- Guo's finite determinant sequence is not the Fredholm or
  Hilbert--Carleman determinant of `H_s`.
- Alekseyev's finite distinct-label problem is not the same object as a
  closed walk in the looped countable graph.
- No sentence may claim external priority. The admissible wording is that
  the bounded search did not find the exact combined theorem.

## Completed source-location checks

- The official AMS record identifies Simon's Chapter 9 as “Regularized
  determinants and renormalization in quantum field theory,” pp. 75--80.
- The full Fournier--Wagner arXiv PDF was checked directly. Sections 2--4
  develop the Schur-test route, while Section 6 is explicitly “Folding
  patterns” and defines alternating representations and `Fold(K)`.

## Remaining bibliography checks

1. Retain a self-contained proof of the specialized `det_2` direct-sum
   identity and cite Simon only for standard machinery.
2. Reuse DOI/arXiv-derived metadata to build a filtered `references.bib`;
   normalize capitalization and en-dashes without changing metadata.
3. Ensure every bibliography entry is cited and every in-text source claim
   maps to a verified passage. Any unresolved item remains visibly marked
   and blocks final compilation/release.
