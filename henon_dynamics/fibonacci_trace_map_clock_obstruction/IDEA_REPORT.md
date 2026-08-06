# Breadth-first idea report: system-level pivot after HCS-C12C

Date: 2026-08-06

## Executive decision

The provisional Hénon dihedral-quotient candidate HCS-C12C was stopped before
a broad genus scan.  Its low-period orbit-marker construction collides with
2002--2007 orbital-polynomial work, and its coarse dihedral quotient retains
only the trivial isotypic sector unless reversal/chiral data are restored.
That is a scoped information-loss result, not a theorem against ordinary
autonomous dynamical zeta functions.

The highest-upside replacement in the breadth scan was the Fibonacci
Schrödinger trace map because it supplies, without fitting, both reversible
polynomial dynamics and a canonical self-adjoint operator.  Its first exact
gate refuted a naive incidence identification; a stronger all-level analysis
then found a dimension-independent passive-parameter degree/clock obstruction
for uniformly bounded polynomial weights.  Casdagli's explicit
large-coupling coding yielded a positive structural result: source-faithful
ten-state marked spectral-band paths have boundary series
\((1+z)/(1-z-z^2)\), distinct from the closed-orbit zeta.  Finally, the exact
escape witnesses yielded a second all-level theorem: the coefficient and
logarithmic-trace series have radius zero, excluding any literal realization
by a scalar germ analytic at the orbit variable's origin.

## Candidate landscape

| Rank | Candidate | Structural gain | Decisive first gate | Decision |
|---:|---|---|---|---|
| 1 | Fibonacci Schrödinger trace map | reversible trace dynamics + Fricke surface + self-adjoint Hamiltonian | section-return gcd audit, then all-level energy-degree growth | **SCOPED THEOREM**; general Fredholm bridge not testable |
| 2 | noncommuting \(S\)-integer solenoid skew product | ordered arithmetic products at every place; preserves non-autonomous chronology | equal-abelianization words with distinct ordered products and fixed-point data | **NEXT SYSTEM** after paper closure |
| 3 | arithmetic congruence/Ihara graph tower | exact Bass determinant + self-adjoint adjacency + graph RH analogue | isolate universal-tree bulk from arithmetic representation factors | baseline/high collision risk |
| 4 | primitive \(S\)-adic Jacobi cocycle | chronological directive sequence + self-adjoint family | equal-incidence, order-distinct directive towers | reserve |
| 5 | adelic Berkovich rational dynamics | canonical local dynamical systems at all places | product-formula behavior on exact low cycles | reserve/high risk |
| 6 | thin \(SL_2(\mathbb Z)\) continued-fraction cocycle | arithmetic length spectrum and congruence twists | source-equivalence test against Mayer/Selberg operators | reject absent a new uniform theorem |
| 7 | modular geodesic/scattering dynamics | complete positive determinant/operator control | established theory | positive control only |
| 8 | Bost--Connes system | canonical \(\log n\) Hamiltonian and zeta partition trace | partition trace versus spectral determinant | negative control only |

The registry was deduplicated against prior Hénon Ulam, ordinary weighted
zeta, finite-field permutation, Maslov, quantized-Hénon, pinning, and
parameter-fit experiments.

## Frozen mathematical question

For Fibonacci words \(w_k\), can the finite Bloch discriminants

\[
d_k(E)=\operatorname{tr}M(w_k;E)
\]

be recovered from a short-clock weighted transfer model in trace-map
renormalization time \(k\)?  Three progressively stronger forms were tested:

1. identify a spectral-section hit with a trace-map return at \(m=k\) or
   \(m=q_k\);
2. encode \(d_k(E)\) as a closed-path trace, uniformly bounded-degree
   boundary coefficient, or order-\(k\) determinant coefficient using
   uniformly bounded polynomial energy weights, while allowing arbitrary
   finite state dimension \(N_k\); and
3. encode the witness values \(d_k(E_*)\) literally as coefficients of a
   scalar germ analytic at \(z=0\), or as signed logarithmic traces of an
   analytic normalized determinant.

The first is refuted by exact escaping examples and the 48-case gcd audit.
The second is refuted for all levels by polynomial degree growth:

\[
\deg_E d_k=q_k=F_{k+2},
\qquad
\deg_E\operatorname{tr}B_k(E)^k\le kD.
\]

The third is refuted because the escape recurrence gives

\[
|d_k(E_*)|^{1/k}\longrightarrow\infty,
\]

so \(\sum_kd_k(E_*)z^k\) and
\(\sum_{k\ge1}d_k(E_*)z^k/k\) both have radius zero.  Fixed bounded-resolvent
matrix elements and standard analytic Fredholm determinants are covered, not
only finite matrices.

## Why this is a large step

The finite audit alone would only reject two tempting equations.  The degree
theorem identifies the precise resource mismatch: a uniformly bounded-degree
local weight adds only bounded energy complexity per renormalization step,
while the
chronological Schrödinger word contains \(F_{k+2}\) sites.  Any exact model
must therefore do at least one of the following visibly:

- use physical time \(q_k\);
- allow exponentially growing level-dependent weights;
- retain nonlinear/composition dynamics or moving energy evaluation;
- change to a growing-order full characteristic determinant (state growth
  alone does not alter the short-clock trace, boundary, or order-\(k\)
  coefficient bound); or
- use a \(k\)-dependent, nonanalytic, or witness-singular construction, or an
  indirect energy-divisor map rather than literal \(z^k\) coefficients or
  logarithmic traces.

This is the preserved-dynamics content of the two-clock obstruction.  It is
not obtained by averaging transition matrices.

## Novelty boundary

Established ingredients, not claimed as new, include hyperbolic trace-map
coding, periodic orbits and multipliers, thermodynamic formalism, standard
subshift zeta formulas, and absence of eigenvalues for the infinite Fibonacci
Hamiltonian.  The new project-level contribution is their combination with:

1. a fully reproducible section-hit/return incidence audit; and
2. an exact source-faithful ten-state boundary/closed generating-function
   comparison for Casdagli's band paths, together with its decorated
   unweighted six-state quotient;
3. the dimension-independent passive-parameter bounded-polynomial
   degree/clock no-go theorem; and
4. the zero-radius analytic-germ obstruction for literal coefficient and
   logarithmic-trace matching at two exact finite-approximant section
   energies.

The Casdagli statement is confined to
\(V_{\rm C}\ge8\), equivalently \(\lambda\ge16\) after centering.  The escape,
gcd, and zero-radius witnesses are at \(\lambda=1\); \(E=0,-1\) are finite
periodic-approximant section energies, not asserted infinite-Hamiltonian
spectral points.  The degree theorem uses only monicity and applies for
arbitrary fixed coupling.  These regimes are not merged.

The project does not claim that every weighted Fredholm construction is
impossible.  In particular, zeros of an energy-dependent Fredholm determinant
could arise by global trace cancellations without making
\(\ell_\lambda(E)\) periodic.

## Route-A decision

The unweighted Artin--Mazur zeta is a well-defined function of its orbit
variable \(z\), but it has no frozen, type-correct identification with the
energy polynomial \(d_k(E)\).  A general energy-dependent Fredholm determinant
is `NOT_TESTABLE` because no operator or normalization has been defined.
Meanwhile the natural Fibonacci Hamiltonian has no point spectrum and cannot
itself provide a discrete Hilbert--Pólya eigenvalue list.

Thus C13 is not a Route-A candidate.  C13B is retained as a positive symbolic
boundary identity, not a spectral determinant.  C13P and C13G are retained as
proved reusable screening obstructions, not as positive RH constructions.

## Next large-step rule

Complete the scoped negative paper.  Do not tune coupling or compare against
Riemann zeros.  The next positive exploration should switch system class to
the ordered noncommuting \(S\)-integer solenoid cocycle, beginning with an
exact same-abelianization/order-sensitive fixed-point gate.
