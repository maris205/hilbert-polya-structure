# Literature and Novelty Audit

## Scope

This audit asks whether the exact Paper05 synthesis already exists inside
Symbolic Dynamics:

1. tensor atoms of finite full shifts;
2. factorization-poset or exterior grading on those atoms;
3. a graded Fredholm/Berezinian Euler realization;
4. an intrinsic \(s\leftrightarrow1-s\) completion.

The search found strong prior art for each generic ingredient but did not
locate this exact source-locked synthesis. The absence claim is deliberately
limited to the sources searched on 2026-08-13.

## Closest same-family collisions

### Exterior automata and alternating determinants

Marie-Pierre Béal constructs exterior powers of deterministic automata and
uses an alternating product of determinants to calculate sofic zeta
functions. This is the closest direct collision. Paper05 therefore does not
claim the first exterior-power or alternating-determinant zeta in symbolic
dynamics.

The distinction is the grading source. Béal's exterior degree belongs to
presentation states and performs inclusion--exclusion among labeled paths.
Paper05's degree belongs to finite subsets of categorical tensor atoms of the
full-shift product monoid and produces the number-theoretic Möbius ledger.

Primary record:
[Béal, RAIRO ITA 29(2), 85--103 (1995)](https://www.numdam.org/item/ITA_1995__29_2_85_0/).

### Signed homology and Lefschetz zeta

Putnam's homology for Smale spaces gives a Lefschetz formula relating
periodic points to traces on homology. Deeley develops a signed version and
a signed zeta. These works prevent any broad claim that graded homology,
signed periodic counting, or alternating Lefschetz determinants are new.

For signed shifts of finite type, the nonzero homology is concentrated in
degree zero. Thus the established signed Putnam theory does not automatically
produce Paper05's tensor-subset grading.

Primary records:

- [Putnam, Memoirs AMS 232 no. 1094 (2014)](https://bookstore.ams.org/memo-232-1094).
- [Deeley, MATRIX Annals (2018)](https://arxiv.org/abs/1612.02066),
  DOI 10.1007/978-3-319-72299-3_13.

### Products and Künneth structure

Product/Künneth theorems for groupoid and Smale-space homology are known.
Paper05 does not claim the first monoidal or product-compatible homology for
symbolic systems. Its narrower contribution is to attach a factorization
complex to the object monoid of finite full shifts and audit its Riemann
Euler ledger under Route A.

Primary record:
[Proietti--Yamashita, ETDS 45(1), 247--273](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/homology-and-ktheory-of-dynamical-systems-iv-further-structural-results-on-groupoid-homology/8064B453B6EEE0F594DA88561DA67796),
DOI 10.1017/etds.2024.37.

## Algebraic background and the decisive distinction

Rota's Möbius theory identifies poset Möbius functions with reduced Euler
characteristics. Applied to the divisor lattice, it gives the standard
number-theoretic \(\mu(n)\). Priddy's Koszul resolutions supply the standard
algebraic complex. Neither fact is claimed as new.

Primary records:

- Rota, “On the Foundations of Combinatorial Theory I. Theory of Möbius
  Functions,” DOI 10.1007/BF00531932.
- Priddy, “Koszul Resolutions,” DOI
  10.1090/S0002-9947-1970-0265437-8.

The literature audit exposed a key correction to the initial hypothesis.
The zero-differential exterior transfer module has

\[
\operatorname{Str}\Gamma_-(L_s)=\prod_p(1-p^{-s}),
\]

but the honest equivariant Koszul resolution includes the symmetric algebra
coefficient factor. Its bosonic and fermionic contributions cancel, so the
total supertrace is \(1\). Paper05 makes this obstruction a central theorem
instead of calling the exterior module a Koszul resolution.

## Symbolic reversal and duality

Bowen--Lanford gives the standard SFT determinant. Transposition/reversal
preserves \(\det(I-zA)\), but that is invariance at the same variable, not a
Riemann-type \(s\leftrightarrow1-s\) functional equation.

Flip-system zeta functions and K-theoretic stable/unstable dualities are also
known. They motivate the Paper05 tests but do not supply the missing
half-density character on the tensor-prime transfer.

Primary records:

- Bowen--Lanford, “Zeta Functions of Restrictions of the Shift
  Transformation,” DOI 10.1090/pspum/014/9985.
- Kim--Lee--Park, “A Zeta Function for Flip Systems,” DOI
  10.2140/pjm.2003.209.289.
- Kaminker--Putnam, “K-Theoretic Duality for Shifts of Finite Type,” DOI
  10.1007/s002200050147.

## Legal novelty statement

The following statement is supportable:

> In the primary sources located in this audit, we did not find the exact
> combination of the finite-full-shift tensor monoid, its categorical atoms,
> factorization-poset/exterior grading, and a Route-A audit of the resulting
> Riemann Euler determinant and symbolic duality obstruction.

The following claims are not supportable and are not made:

- first graded or signed symbolic zeta;
- first exterior-power determinant formula in symbolic dynamics;
- first homology or Künneth theorem for symbolic/Smale systems;
- first Möbius or Koszul interpretation of a monoid Euler product;
- a proof of analytic continuation or the zeta functional equation;
- an intrinsic Gamma factor or completed-\(\xi\) determinant.

## Current novelty boundary

Paper05's defensible contribution is a synthesis plus an obstruction:

1. factorization topology canonically identifies the parity needed by
   SD-C07;
2. exterior transfer and odd Berezinian give exact reciprocal orientations
   in the Euler half-plane;
3. an honest Koszul lift erases the Euler data rather than completing it;
4. natural reversal and group completion implement the wrong spectral
   involutions;
5. the first adversarial critical-strip regularization is zero-free and
   removes the decisive low-order traces.
