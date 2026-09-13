# Paper20 — Novelty, Collision, and Stop Assessment

## Proposed contribution

The defensible contribution is a **fixed, explicit, asymmetric family** of
canonical polynomial automorphisms of \(\mathbb A^4\), indexed by \(g\ge5\),
for which a two-phase Newton-face calculation gives the closed form
\[
 \lambda_1(F_g)=(\sqrt g+1)^2.
\]
The word “non-product” refers to the strict comparison with the product of the
two elementary shear degrees, \((g-1)^2\), and to the connected mixed support in
the displayed coordinates. It does **not** assert a universal non-conjugacy-to-
product theorem.

The novelty case is therefore structural and proof-based:

1. a canonical (symplectic) shear word is fixed before degree analysis;
2. the two shears select different asymmetric Newton faces;
3. the complete-step matrix \(BA\), rather than a half-step off-diagonal
   matrix, controls degree growth;
4. an explicit invariant ratio cone proves that the selectors persist for every
   iterate; and
5. Perron reachability and total-degree visibility turn the matrix root into the
   dynamical degree.

This is narrower than “new high-dimensional degree growth,” a claim excluded by
the bounded source refresh.

## Collision matrix

`Ø` means no shared primary object or proof target was found in the bounded
Paper12–19 ledger. `NEAR` means a neighboring vocabulary is acknowledged but
is not a theorem collision. Every row remains subject to an independent review.

| Prior paper | Occupied object | Paper20 object | Verdict | Boundary / anti-claim |
|---|---|---|---|---|
| P12 | Residue/period-three arithmetic and clock strata | Degree vectors, Newton faces, Perron root | Ø | No residue classes, period-three data, or arithmetic clocks. |
| P13 | Primitive exact-period covers and cyclic orbit quotients | Iterated polynomial degrees | Ø | No periodic points, orbit quotients, or dynatomic schemes. |
| P14 | Support-one torus escape and finite-rank map geometry | Coupled canonical shears on \(\mathbb A^4\) | Ø | No torus survivors, character lattices, or escape classification. |
| P15 | Pure-trace/Jacobian fibers and quasi-finite loci | Newton support degrees and matrix products | Ø | No trace coordinates, Jacobian fibers, or ramification. |
| P16 | Support-size torus escape bounds | Explicit degree recurrence | Ø | No support-size counting or finite-rank torus map. |
| P17 | Fixed-lag shift-like recurrence and torus-coset dimension | Symplectic shear degree matrix | Ø | No recurrence variety, lag word, character extinction, or coset dimension. |
| P18 | Marked trace coordinates and scheme-theoretic boundary ramification | Positive-coefficient degree growth | Ø | No trace marking, boundary scheme, or branch divisor. |
| P19 | Maximum-dimensional translates, coefficientwise moduli, support-one GCD obstruction | Canonical shear/Newton-face recurrence | Ø | No translates, GCD obstruction, effective height, or periodic classification. |

For completeness, P1–P11 remain outside the object boundary (prime-clock,
cat-map, centralizer, zeta, and quantization lines). A later reviewer may
reclassify a neighboring result; the response is to narrow the claim, never to
erase the collision.

## External-neighbor comparison

- The planar generalized-Hénon degree-product picture is acknowledged as
  background (S01 and S07 in `CITATION_VERIFICATION.md`). Paper20 does not claim to
  overturn its classification.
- Déserti's higher-dimensional examples (S02) show that degree growth has a
  broad landscape. Paper20 contributes neither a classification nor a claim of
  priority; it isolates one canonical, coupled, positive-coefficient family and
  proves its exact matrix recurrence.
- The four-dimensional coupled-Hénon hyperbolicity literature (S06) is a
  neighboring dynamical setting. Paper20 studies algebraic degree, not
  horseshoes, hyperbolicity, or topological entropy.

## Conservative scores

| Dimension | Score | Reason |
|---|---:|---|
| Novelty | 8.1/10 (at most 8.3 after a clean support-coupling proof) | Explicit asymmetric canonical family and non-product closed form; no broad priority claim. |
| Standalone | 8.0/10 | Definitions, selectors, cone, recurrence, and Perron proof fit in one self-contained package. |
| Proof | 9.2/10 | Symbolic inequalities are short and uniform in \(g\ge5\), but visibility and no-cancellation wording must remain literal. |

## Anti-claims

The package does not claim:

- a theorem for arbitrary sparse potentials or arbitrary shear words;
- a finite Newton fan for every symplectic polynomial automorphism;
- a classification of four-dimensional polynomial automorphisms;
- equality of algebraic, topological, arithmetic, or measure-theoretic entropy;
- integrability, invariant curves, periodic-point counts, traces, multipliers,
  centralizers, torus translates, or arithmetic specializations;
- non-conjugacy to a product in every coordinate system;
- validity in positive characteristic or under sign-changing coefficients;
- a numerical or CAS search as a proof certificate.

## Hard STOP rules

STOP the candidate if any of the following occurs:

1. A reviewer finds a selector tie at an iterate or an untracked carried term.
2. The claimed cone is written as one strict two-shear cone and ignores the
   phase-return equality \(v_{n+1}=Au_n\).
3. The half-step matrix is used without a phase-period correction.
4. A coefficient specialization permits cancellation, or the field has positive
   characteristic.
5. \(e_2\) is not shown to see the Perron class / total degree.
6. The mixed support is removed and the map becomes a product, or a stronger
   non-conjugacy claim is introduced.
7. A source is cited as proof of the new formula or a priority claim is made.

The current status is `CONDITIONAL DESIGN GO`, not publication readiness.
