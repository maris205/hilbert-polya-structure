# Next breadth-first roadmap after C02D

Date: 2026-08-06  
Status: **C12A completed and closed; historical pre-registration retained**  
Provisional ID: **HCS-C12A**

## Outcome update: C12A/C12B closure

The authorized C12A work is complete in the sibling project
henon_frobenius_scheme_obstruction.

- Over \(\mathbb Z[A,A^{-1}]\), the cyclic fixed scheme is finite flat of
  rank \(2^n\).
- For fixed \(n\), every finite zero-dimensional fiber has a
  nilpotent-blind Frobenius permutation determinant.  Local rationality and a
  finite recurrence in \(r\) are universal, so the registered mechanism
  closes as C12A_NO_GO_ZERO_DIMENSIONAL_FROBENIUS_COLLAPSE.
- A reversible ten-point control proves that ordinary rectangular traces do
  not determine the joint Frobenius/Hénon action in the structural category.
- The apparent \(a=6,n=5\) \(S_6\) signal is the \(Z\)-sextic already
  published by Endler--Gallas (2006), hence
  C12B_N5_PRIOR_WORK_COLLISION.

The negative conclusion is scoped: classical global Dedekind/Artin factors
can have nontrivial zeros and can inherit \(\zeta(s)\).  What fails is their
use as distinctive new Hénon Route-A evidence.

## Next breadth-first source lock

Provisional **HCS-C12C** should retain the parameter direction rather than
freeze \(A=a\).  For a source-locked period \(n>5\), form the
parameter-varying exact-period scheme and quotient its chronological
dihedral action:

\[
\mathcal C_n=
\mathcal P_n/\langle H_A,R\rangle
\longrightarrow \operatorname{Spec}\mathbb Z[A,A^{-1}].
\]

The first question is whether a compactified good-prime fiber has a
canonically defined, genuinely nontrivial \(H_c^1\) representation whose
Frobenius factors are not already standard Hénon dynatomic-curve or orbital
polynomial results.  This changes the geometry from the zero-dimensional
fixed-\(a\) fibers killed by C12A while preserving chronological orbit data.

Only WP0 is authorized next:

1. audit Hénon dynatomic/modular curves, exact-period quotients, orbital
   polynomials, reversor quotients, and arithmetic monodromy;
2. freeze scheme-level exact-period conventions at characteristics dividing
   \(n\);
3. prove that the proposed quotient and compactification are canonical before
   computing genus or zeta factors;
4. kill C12C immediately if it is a relabeling of known orbital-polynomial
   curves or if the quotient discards the dihedral/Galois action being tested.

No larger fixed-\(n\) scan, diagonal \(r=n\), target-zero fit, or global Euler
product is authorized by this roadmap.

## Selected direction

**Two-axis Frobenius--dynamical orbit schemes for the integral
area-preserving Hénon family.**

The next search should return to the exact Paper-5 recurrence

\[
H_a(q,p)=(1-aq^2-p,q)
\]

and keep the parameter arithmetic when \(a\in\mathbb Z\). For each dynamical
iterate \(n\), define the periodic-point scheme

\[
X_{a,n}=\operatorname{Fix}(H_a^n)
\]

over an integral base. At a good prime \(p\), retain the two independent
indices

\[
N_{a,p}(r,n)
=
\#X_{a,n}(\mathbb F_{p^r}),
\]

where \(r\) is Frobenius extension degree and \(n\) is chronological Hénon
time.

This directly addresses the missing arrow found in C03. It does not make the
invalid diagonal substitution \(r=n\), and it does not replace chronological
dynamics by an averaged transition matrix.

## Specific mathematical question

For fixed \(n\), does the Frobenius sequence \(r\mapsto N_{a,p}(r,n)\), after
removing explicitly identified degree/compactification pieces, admit a
canonical finite trace decomposition

\[
N_{a,p}(r,n)
=
\sum_j (-1)^{\nu_j}\alpha_{a,p,n,j}^{\,r},
\]

whose factors vary compatibly with dynamical repetition in \(n\) and are not
reproduced by generic reversible polynomial-automorphism controls?

A positive result would be an actual cohomological/arithmetic bridge rather
than a numerical Euler-product analogy. A negative result could prove that
only algebraic-stability, degree-growth, or reversibility data survive, which
would be a useful obstruction.

## Why this candidate is next

- It is rooted in the exact conservative recurrence of Paper 5.
- It attacks the arithmetic layer absent from the local hyperbolic BPS lane.
- It reuses C03's strongest lesson by keeping Frobenius degree and dynamical
  iteration as separate axes.
- It is structurally different from signed/graded pinning determinants, so
  HEN-O15 and HEN-O16 do not kill it at definition time.
- It has cheap exact falsifiers before any global \(L\)-function or RH claim.

## Work packages

### WP0: source and equivalence lock

1. Audit algebraic Hénon maps, periodic-point schemes, dynamical zeta functions
   over finite fields, compactification, algebraic stability, and étale
   Lefschetz trace formulas using primary sources.
2. Determine whether \(X_{a,n}\) is finite and reduced at each tested good
   prime, recording multiplicities when it is not.
3. Freeze conjugacy, recoding, and reversible-map controls before seeing any
   factorization.

### WP1: exact finite-field engine

1. Implement \(\mathbb F_{p^r}\) with a frozen irreducible-polynomial ledger.
2. Enumerate or solve \(\operatorname{Fix}(H_a^n)\) with both \(r\) and \(n\)
   recorded.
3. Cross-check direct point enumeration against polynomial elimination for the
   smallest cells.
4. Preserve scheme multiplicity and exceptional/bad-prime flags.

Initial cheap grid:

\[
a\in\{5,6,7\},\qquad
p\in\{3,5,7,11,13\}\text{ good},\qquad
1\le r\le4,\qquad 1\le n\le6.
\]

The final grid must be frozen only after WP0 establishes feasibility and
cost.

### WP2: local rationality and trace reconstruction

For each fixed \((a,p,n)\), form only the Frobenius local series

\[
Z_{a,p,n}(u)
=
\exp\left(
\sum_{r\ge1}\frac{N_{a,p}(r,n)}r u^r
\right).
\]

Test exact linear recurrences in \(r\), validate on sealed extension degrees,
and report minimal recurrence order and factorization. Do not identify \(u\)
with \(p^{-s}\) at this stage.

### WP3: compatibility in dynamical time

Test whether the recovered Frobenius factors for \(n\) and its divisors obey a
canonical primitive/repetition relation. Distinguish geometric periodic
points, symbolic words, scheme multiplicity, and exact-period components by
Möbius inversion only when its hypotheses are proved.

### WP4: adversarial controls

- matched involution-product polynomial permutations;
- coefficient-randomized area-preserving maps of the same degree;
- neighboring integer parameters;
- permutation-conjugate presentations;
- compactification/degree-only predicted factors;
- shuffled \(n\)-labels while keeping every \(r\)-sequence intact;
- shuffled \(r\)-labels as an expected-fail chronology control.

### WP5: Route-A gate

A1 can advance only if a canonical primitive-orbit/Galois structure survives
the controls. A2 requires an explicitly defined local or global determinant
with an independently justified Frobenius trace mechanism. A3 and Route B
remain closed unless analytic continuation, normalization, and liftability
are established without target-zero fitting.

## Mechanical kill conditions

Return **NO_GO** immediately if any of the following occurs:

1. the recovered factors are completely explained by degree growth,
   compactification boundary classes, or reversible permutation identities;
2. recurrence order grows with the number of enumerated points and does not
   validate on sealed \(r\);
3. compatibility in \(n\) exists only after setting \(r=n\);
4. a proposed character depends on a noncanonical ordering of algebraic roots;
5. the same signal appears in the matched controls;
6. bad-prime or nonreduced-scheme multiplicities are silently discarded;
7. a global Euler product is introduced before a trace/cohomological theorem.

## Promotion threshold

A paper route requires at least one theorem-level novelty delta:

- an explicit nontrivial Frobenius factor for a Hénon periodic-point scheme
  with a proved dynamical repetition law;
- a uniform obstruction theorem showing that the two-axis data collapse to
  standard algebraic-stability classes;
- or a new effective compatibility theorem not subsumed by existing
  algebraic-dynamical zeta theory.

Finite tables, attractive factorizations, or stable roots alone do not pass.

## First authorized action

Perform WP0 only. Freeze the exact scheme, good-prime conditions, control
family, multiplicity convention, and two-axis data schema before implementing
the finite-field engine.
