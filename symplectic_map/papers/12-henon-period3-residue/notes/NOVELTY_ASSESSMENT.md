# Novelty Assessment

## Verdict

**GO_BORDERLINE_STANDALONE_SPECIALIST_NOTE**.

- Literature cutoff: 2026-08-16 UTC
- Final post-proof novelty score: 6.2/10
- Final post-proof standalone-size score: 5.8/10
- Earlier candidate-stage novelty scores: 6.1/10 and 6.5/10
- Earlier candidate-stage standalone-size scores: 5.7/10 and 5.5/10
- Direct-collision gap confidence after bounded search: approximately 0.82
- Safe lead: sharp quartic full-fiber classification and minimal period-three
  separator
- Supporting lead: all-\(m\) period-three two-term residue law and exact
  nested-binomial slope certificate
- Explicit open problem: \(D_m\ne0\) for every \(m\ge2\)

The paper is above the Batch-04 gate, but not by enough to tolerate inflated
positioning. The quartic obstruction family and its period-one/two blindness
are already in Cantat--Dujardin. Global residue methods, formal periodic
cycles, and multiplier invariants are also prior art. The defensible delta is
the exact formal-period-three law, its all-degree coefficient certificate, and
the sharp quartic consequence on the complete normalized fiber whose formal
fixed-point trace multiset is \(0^4\).

No historical-priority claim is made. Bounded search establishes only that no
direct collision was found in the queried primary-source neighborhood.

## Component-level map

| Component | Novelty estimate | Safe assessment |
|---|---:|---|
| Family \(f_{m,a}\) and period-one/two blindness | 4.0/10 | natural generalization of the direct quartic obstruction; setup, not headline |
| Quotient coordinate \(a^{2m-1}\) | 4.2/10 | clean normalized conjugacy calculation; useful but not sufficient alone |
| Uniform law \(S_m=C_m+D_ma^{2m-1}\) | 6.1/10 | main conceptual theorem, proved by global residue and degeneration in bound Steps 4--8 |
| Exact nested-binomial \(D_m\) certificate | 6.2/10 | strongest all-degree theorem, transparently derived in bound Step 9 |
| Odd-\(m\) identity \(C_m=0\) | 4.5/10 | symmetry corollary |
| Quartic full-fiber classification and exact period-three cutoff | 5.5--6.5/10 | sharp effective resolution of the known obstruction |
| Combined package | 6.2/10 | coherent but borderline standalone specialist note |

The bare two-term shape may look forced after invariance and a sharp degree
bound are known. The paper's mathematical work must therefore visibly include:

1. the scheme-theoretic cyclic formal-period setup;
2. freeness and complete-intersection trace/residue control;
3. the Step-7 local degeneration eliminating the two higher invariant powers;
4. the Step-9 recurrence, Laurent/admissible-tuple extraction, local binomial
   identity (9.14), and distinguished-coordinate/transfer-flow bijection;
5. both the Step-10 zero fixed moment and the separate Step-13 local
   fixed-branch multiplicity needed for exact length subtraction;
6. the quartic full-fiber and conjugacy classification.

If the coefficient formula appears only as an opaque computer expansion, the
standalone-size assessment falls to approximately 4.8/10 and the package no
longer clears the paper gate. The current bound proof retains the transparent
derivation.

## Dominant direct collision

### Cantat--Dujardin, 2026

The direct source is Serge Cantat and Romain Dujardin, **Multiplier rigidity
for complex Henon maps**, arXiv:2603.09445 (2026).

What it already provides:

- full marked unstable-spectrum rigidity for complex Henon maps;
- a Noetherian finite-period, finite-fiber statement in fixed degree;
- the quartic Jacobian-minus-one family
  \[
  (y+(x^2-\lambda^2)^2,x);
  \]
- explicit failure of period-one and period-two traces to distinguish that
  family;
- normalized-form background needed for the conjugacy quotient.

What it does not provide:

- the formal-period-three trace moment;
- the exact integer identity recovering \(\lambda^6=L^3\);
- a minimal separator on the full normalized fiber whose formal fixed-point
  trace multiset is \(0^4\);
- the all-\(m\) exceptional family theorem;
- the two-term residue law or the nested-binomial coefficient certificate.

The paper must state that \(a=\lambda^2\) in the quartic comparison, so the
quotient coordinate \(a^3\) is \(\lambda^6\).

## Method collisions

### Multidimensional residues

Cattani--Dickenstein--Sturmfels develops global residues, traces on
zero-dimensional complete intersections, deformations to initial forms, and
coefficient-computation methods. These are the methodological foundation, not
a Paper-12 invention.

Safe delta: applying that machinery to the formal period-three Henon cyclic
scheme, proving the two-term law, and extracting the specific \(D_m\).

### Periodic-orbit contour sum rules

Cvitanovic--Hansen--Rolf--Vattay develops multidimensional contour
representations and exact periodic-orbit sum rules, including a
volume-preserving Henon setting. Its standard quantities are
transfer/Fredholm-type sums weighted by determinant factors. It does not give
the raw formal-period-three trace power sum or the moduli-coordinate recovery
here.

### Low-period generalized Henon calculations

Dullin--Meiss gives explicit low-period equations, period-three stability, and
trace calculations for conservative cubic generalized Henon maps. This blocks
any broad claim that exact period-three Henon algebra is new, but it does not
contain the selected even-degree exceptional family or residue law.

## Adjacent invariant literature

### Friedland--Milnor

The classification and normal forms for polynomial automorphisms of the plane
are foundational. Paper 12 uses the normalized Henon moduli category and must
not claim that normal form or root-of-unity conjugacy machinery as new.

### Huguin

Huguin studies one-dimensional polynomial moduli and small-cycle multiplier
maps. This is the closest current small-cycle multiplier comparison, but it is
not a plane-automorphism or quartic Henon result.

### Hutz

Hutz supplies dynatomic-cycle and multiplier-invariant machinery for
projective dynamical systems. Formal periodic schemes and symmetric multiplier
invariants are therefore background, not a novel formalism.

### Guillot--Ramirez and Ueda

These works supply fixed-point multiplier and index/residue background for
projective and polynomial-automorphism settings. They are methodological
neighbors, not direct instances of the selected theorem.

### Bianchi--He

The 2026 thermodynamic-path work cites Cantat--Dujardin for multiplier rigidity
but does not close the finite-period obstruction, compute the quartic
period-three moment, or give the all-\(m\) law.

## Search boundaries

The search used combinations of:

- exact family expressions involving \((x^m-a)^2\);
- Henon period-three trace moment, multiplier moment, and formal period
  queries;
- global residue and complete-intersection trace queries;
- citations to and citing records of Cantat--Dujardin;
- recent 2024--2026 multiplier-moduli and complex-Henon literature;
- known generalized-Henon period-three calculations.

No primary source was found containing the all-\(m\) law, the frozen
nested-binomial \(D_m\) formula, or the exact quartic minimal-separator
statement. This is a bounded absence inference, not proof that no such source
exists.

## Why the arithmetic/dynamical content is intrinsic

The recovered quantity \(L^3\) is not inserted as a target label:

1. \(L^3\) is independently the normalized polynomial-conjugacy coordinate;
2. the period-three moment is defined from the derivative along the intrinsic
   formal periodic scheme;
3. the trace-residue identity computes that moment without fitting a target;
4. the coefficient is a nonzero exact integer in the quartic theorem;
5. period one and two are proved blind, so minimality is structural.

The uniform law similarly uses \(a^{2m-1}\) because it is the invariant
quotient coordinate forced by normalization, not because a desired answer was
encoded into spectral entries or weights.

## Source-stage disposition

The final author proof-package candidate is frozen at SHA-256
`36f2edd5a1a25960a2c656adaeb07fbd4251c61b51c9e0a0382200460b589ba9`.
Within that candidate, Step 7 closes the degeneration branches, Step 9 closes
the recurrence-to-binomial reduction using (9.14) and the transfer-flow
bijection, Step 12 provides an independent direct quartic-slope derivation,
and Step 13 proves the local fixed-branch multiplicity. These facts satisfy
the mathematical-mass condition used in the final 6.2/5.8 assessment. They do
not constitute `SOURCE_LOCK_PASS`; a fresh hash-bound correctness and citation
review remains mandatory.

## Independent-review synthesis

Two independent pre-source-package reviews agreed on GO, and a final
post-proof audit retained GO at novelty 6.2/10 and standalone size 5.8/10.

### Review A

- Novelty: 6.5/10
- Standalone size: 5.5/10
- Main judgment: lead with the quartic theorem and present the all-\(m\)
  construction as a broader mechanism with open nonvanishing.

### Review B

- Novelty: 6.1/10
- Standalone size: 5.7/10
- Collision-gap confidence: about 0.85
- Main judgment: the global-residue method is mature; the Hénon-specific
  two-term law, coefficient certificate, and quartic application are the delta.

These scores measure novelty and paper mass, not the correctness authority of
the frozen proof package. A fresh hash-bound reviewer must still verify every
theorem and citation before implementation.

## Safe positioning

Recommended abstract-level claim:

> On the complete normalized quartic Henon fiber whose formal fixed-point trace
> multiset is \(0^4\), periods one and two are blind while a formal
> period-three trace moment is an affine coordinate on conjugacy moduli. In
> every even degree, the same
> exceptional family satisfies a two-term period-three residue law whose slope
> has an explicit finite binomial certificate.

Safe verbs:

- prove;
- compute exactly;
- classify within the normalized fiber;
- derive;
- certify;
- reduce universal recovery to an explicit open combinatorial nonvanishing
  problem.

## Forbidden positioning

The project must not say:

- first use of global residues in dynamics;
- first exact Henon period-three calculation;
- discovery of the quartic obstruction family;
- period three resolves all even degrees;
- \(D_m\ne0\) for every \(m\);
- \(P(4)=3\) globally;
- all quartic Henon maps lie in the selected fiber;
- all positive-dimensional low-period fibers are classified;
- full multiplier rigidity follows;
- finite symbolic checks prove an all-\(m\) theorem.

## Paper-size rationale

The standalone paper has one dominant contribution and one supporting
mechanism:

1. **Dominant:** full quartic fiber with formal fixed-point trace multiset
   \(0^4\), exact period-three
   identity, and minimal conjugacy recovery.
2. **Supporting:** uniform all-\(m\) residue law and coefficient certificate,
   ending in a concrete nonvanishing problem.

The proof requires normal-form algebra, nonreduced formal cycles,
zero-dimensional trace/residue theory, weighted degeneration, explicit
coefficient extraction, and a sharp fiber argument. That is enough for a
specialist note, but not enough to justify adding unrelated height, arithmetic,
or unstable-spectrum claims.

## Gate conclusion

The candidate passes the novelty and size gates under the frozen scope.
Implementation remains forbidden until:

1. every design artifact is frozen and hash-bound;
2. a reviewer independent of the source authors checks the full proof,
   literature roles, coefficient formula, normalization, and nonclaims;
3. the exact verdict is SOURCE_LOCK_PASS.
