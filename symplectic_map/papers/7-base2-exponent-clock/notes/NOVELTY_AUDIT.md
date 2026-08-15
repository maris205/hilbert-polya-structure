# Novelty Audit

Audit date: 2026-08-14.  Search scope: primary papers and official metadata
available through that date.  Verdict: `GO_SCOPED_TECHNICAL_NOTE`.

## Closest results

1. Juan Rivera--Letelier, *Locating critical points attracted to p-adic
   attracting cycles*, arXiv:2601.12163 (2026), Theorem A.  It proves that a
   degree-\(d\) attracting cycle with multiplier strictly below
   \(\lambda(d)^n\) attracts a critical point.  At \(d=p=2\) the threshold is
   \(|2|_2^n\), and the paper explicitly supplies equality examples.  It does
   not classify the frozen equality case.
2. Benedetto--Ingram--Jones--Levy, *Attracting cycles in p-adic dynamics and
   height bounds for postcritically finite maps*, arXiv:1201.1605, Duke Math.
   J. 163 (2014), supplies the main earlier PCF/non-Archimedean background.
3. Hutz, *Good Reduction of Periodic Points*, arXiv:0801.3645, studies exact
   period versus reduced period for good-reduction maps.  Rajagopal--Zhang,
   *Uniform bounds on periodic points of polynomials with good reduction*,
   arXiv:2510.26119, is a recent nearby good-reduction result.
4. Buff--Gauthier, *Quadratic polynomials, multipliers and equidistribution*,
   arXiv:1306.2736, DOI 10.1090/S0002-9939-2015-12506-3, studies quadratic
   parameter loci with prescribed multipliers.  A target \(2^n\) is not a new
   object in parameter-space literature.
5. Ji--Xie--Zhang, *Space spanned by characteristic exponents*,
   arXiv:2308.00289, DOI 10.1007/s00208-026-03361-4, fixes the standard
   multiplier/length/exponent semantics and proves an infinite-dimensional
   span result for nonexceptional maps.  It does not decide one exact value.
6. Murakami--Sano--Takehira, *Arithmetic properties of multiplier
   polynomials for certain polynomial maps*, arXiv:2403.17315, gives
   universal multiplier-polynomial tools for \(z^d+c\), but no all-period
   answer for this frozen type-\((3,1)\) parameter.
7. Benedetto--Goksel's work on Misiurewicz polynomials and dynamical units
   (arXiv:2201.07868, arXiv:2203.14431) includes, in Part II, evaluations of
   certain parameter polynomials related to associated periodic multipliers.
   Their 2025 non-unit paper (arXiv:2506.05254) primarily studies differences
   of Misiurewicz parameters.  None of these results may be transferred to
   arbitrary primitive cycles of the frozen map.
8. Morton--Silverman's dynatomic formalism, DOI
   10.1155/S1073792894000127, is the original exact-period background used to
   separate formal from least period.  No novelty is claimed for that
   machinery.

## Collision assessment

The unit-circle and exact-valuation argument is a short standard
non-Archimedean contraction argument, not a deep new general theorem.  The
publishable contribution is the narrowly scoped synthesis:

- the inherited global derivative-content divisibility theorem gives only
  \(2^n\mathbb Z\);
- exact local dynamics upgrades the normalized rational quotient to an odd
  integer at every period;
- a Frobenius--norm model and a concrete mod-2 obstruction locate precisely
  why the remaining \(\pm1\) equality is harder;
- the finite exact ledger is separated from the all-period result.

Estimated novelty: 3/10 for the local lemma, 4.5/10 for the frozen equality-
boundary certificate as a whole.  An all-period proof that \(B_C\ne\pm1\)
would be materially stronger (estimated 7/10), but no such proof or direct
prior result was found.

## Safe positioning

Preferred title: **Exact 2-Adic Valuation of Higher-Period Multipliers for a
Frozen PCF Quadratic**.

Do not use “base-2 obstruction,” “exclusion of \(2^n\),” or
“characteristic-exponent gap.”  Power and Chebyshev maps are equality
controls, and the current theorem deliberately leaves the equality open.

Paper 5's finite-capacity theorem is silent here: it counts distinct rational
primes, so arbitrarily many cycles using the single supported prime \(2\)
still consume only one support slot.
