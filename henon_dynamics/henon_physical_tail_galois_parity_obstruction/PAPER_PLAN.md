# Paper plan

**Working title:** Physical Stable Tails Do Not Control H\'enon Galois
Excess: Exact Period-Eight and Period-Nine Parity Falsifiers

**One-sentence contribution:** The negative fixed-point tail controls the
physical embedding, but exact degree-six, degree-twelve, and degree-twenty-eight
trace fields show that Galois excess is an all-conjugate reflection ensemble;
integer inequalities certify \(\Delta_6<0<\Delta_7\), so physical
linearization alone is not a valid whole-object compiler.

**Type:** theory plus exact computer algebra

## Claims--evidence matrix

| Claim | Evidence | Initial status | Planned section |
|---|---|---|---|
| The negative fixed point has a positive stable eigenvalue and the signed inverse recurrence is uniformly contractive | exact radicals and derivative bounds | PROVED | \S2 |
| Period eight splits into inequivalent vertex--vertex and edge--edge trace fields | exact closing factorizations and resultants | needs certificate | \S3 |
| The new trace polynomials are irreducible and totally real | modular tests and Sturm intervals | needs certificate | \S4 |
| \(\Delta_6<0<\Delta_7\) exactly | integer-product inequalities | needs certificate | \S5 |
| Physical-tail control does not imply Galois-height control | one-embedding versus all-conjugate identity | PROVED_INTERFACE | \S6 |
| No unrestricted H\"older conclusion follows yet | evaluator firewall | OPEN | \S7 |

## Structure

1. Introduction and claim boundary.
2. Fixed-point tail and the one-embedding theorem.
3. Three reflection boundary types.
4. Exact period-eight/nine trace fields.
5. Integer parity falsifiers.
6. The physical/Galois non-commutation obstruction.
7. Route-A consequences and next theorem.
8. Reproducibility and limitations.

Appendix: coefficient ledgers, root intervals, dependency hashes, and mutation
audit.  The primary figure is a three-column schematic comparing the
vertex--vertex, vertex--edge, and edge--edge palindromic chains; it is optional
because the exact tables carry the evidence.

## Citation plan

- H\'enon for the map;
- Bowen and Parry--Pollicott for hyperbolic coding and periodic-orbit
  potentials;
- HCS-P54--P57 for the frozen pressure, excess, and incidence definitions.

All external metadata are inherited from the already verified P57 bibliography.
No new bibliographic record will be generated from memory.

## Internal review

Cross-model upload is not used because the draft is unpublished and no
external-model consent was requested.  Review is performed locally through an
independent implementation, two hostile rounds, and a claim/evidence audit.
