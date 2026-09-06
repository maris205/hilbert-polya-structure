# Candidate contract: thin Cantor orbit-limit sets for hyperbolic FAD systems

2026-09-06. Admitted as C407 for manuscript development after independent
internal mathematical/source review; not yet a finalized paper release.

## Exact owner

Let `(X,f)` be any finite-adelically distorted (FAD) dynamical system in
Byszewski–Cornelissen–Houben (BCH), Definition 7.1.2, with positive entropy
`log Lambda > 0` and exactly one dominant root in the sense of their
Definition 10.3.9. The observable is the accumulation set of
`Pi_f(N) = N pi_f(N) / Lambda^N`, where `pi_f(N)` counts primitive orbits of
integer length at most `N`. Time is the native iteration integer, not a
rational-prime clock.

The FAD formula is

`Fix(f^n) = |det(A^n-I)| c^n r_n product_{p in S}
             |n|_p^(s_{p,n}) p^(-t_{p,n}|n|_p^(-1))`.

`S` is finite; `A` is integral; `c>0`; `r_n>0` is a gcd sequence; and
`s_{p,n},t_{p,n}` are nonnegative real-valued gcd sequences with periods
coprime to `p`. Real exponents, wild terms, and multiple primes remain in scope.
The fixed-point counts must genuinely come from the stated system.

## Proposed theorem

If every distortion exponent vanishes, the accumulation set is the already
known finite periodic image. Otherwise it is a Cantor set, has zero upper box
dimension (hence zero Hausdorff dimension), and obeys the quantitative bound

`N_epsilon(L_f) <= C (1+log(1/epsilon))^(2d)`

for `0<epsilon<epsilon_0`, where `d` is the number of active distortion primes
and `C,epsilon_0` may depend on the fixed system.

The central source problem is BCH Problem 14.1.1, specifically its previously
unclassified hyperbolic cases: multiple distortion primes and/or nonzero wild
`t` terms. No claim is made to classify the whole nonhyperbolic case, for which
BCH already prove the presence of an interval.

## Classical inputs, explicitly deducted

1. BCH's FAD fixed-point formula and the examples realizing it.
2. BCH Theorem 12.4.3 and equation (12.4): the accumulation set is the image
   of the detector group under its explicit uniformly convergent series.
3. BCH hyperbolicity means exactly one dominant root; their text preceding
   Theorem 12.4.3 proves that its phase function is identically one.
4. BCH's negative-integer slice choice in the proof of Theorem 12.5.1
   (printed pp. 132–133), which keeps the other-coordinate coefficients nonzero.
5. CRT, Haar integration on `Z_p`, and the elementary topological
   characterization of a nonempty compact perfect totally disconnected metric
   space as a Cantor space.

## Proposed new proof work

1. An adaptive valuation partition has only `O(LK)` atoms for `L` integer
   centers truncated at valuation depth `K`. It yields a polylogarithmic
   covering bound even with several primes and nonconstant wild exponents.
2. A positive radial-kernel Fourier lemma proves nonconstancy on every
   admissible cylinder. It handles nonnegative real exponents directly and
   requires no injectivity of the detector map.
3. The new Fourier lemma applies on every cylinder: the coprime-period
   condition supplies an active center, and BCH's classical negative-integer
   slice choice keeps all kernel coefficients positive. This yields the
   every-cylinder nonconstancy needed to exclude isolated image values;
   the negative-integer choice itself is not a new contribution.

## Prohibited promotions

No rational-prime Euler product, target-zero identification, self-adjoint
target operator, or Route-B claim. This is a source-local arithmetic-dynamical
orbit-counting theorem, not a new fixed-point formula, a C404 corollary split,
or a renaming of BCH's cardinality dichotomy.

Source status and bounded novelty search are recorded separately. Independent
review found no mathematical blocker for the checked 2024 source scope;
the final-book priority gap and manuscript/release gates remain explicit.
