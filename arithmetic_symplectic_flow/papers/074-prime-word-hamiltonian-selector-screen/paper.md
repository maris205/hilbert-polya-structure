# A finite prime selector word can drive a Hamiltonian shear construction without becoming an endogenous arithmetic orbit

**Paper ID:** 074-prime-word-hamiltonian-selector-screen  
**Record ID:** ASFS-SCOUT-20260914-50  
**Date / status:** 2026-09-14; PRE-P0 STOP  
**Route state:** No ASFS Route-A coordinate; Route B NOT INVOKED.

## Direct-lineage proposal

The prior-work chain permits a specific finite deformation:

prime/composite sieve word -> finite symbolic selector word -> autonomous
Hamiltonian shear symplectomorphism.

P28 constructs, for every rooted primitive selector-pair word w of length at
least three, an autonomous polynomial symplectomorphism F_w in dimension
2(|w|+1). Its strict selector word and position-weight orbit modulo the diagonal
have least period |w|. This is stronger geometric ownership than an externally
switched matrix sequence: the support data are fixed, then F_w is iterated
autonomously.

To test the arithmetic use, take w to be any finite word extracted from a
prime-wheel or sieve-symbolic construction. This is only a proposed input
specialization; no particular word, prime table, or parameter was computed.

## Same-object audit

| Required owner | P28/source object | Result for the proposed prime-word specialization |
| --- | --- | --- |
| symbolic seed | finite word w supplied to the incidence construction | finite lineage trace retained |
| map | polynomial symplectomorphism F_w | exact geometry for fixed w |
| arithmetic selection | generation of all relevant prime/composite symbols by F_w | absent: w is selected first |
| periodic object | selector and weight-quotient cycles | not a phase-space periodic point |
| primitive orbit/repetition | polynomial-state closed orbits under F_w | not supplied |
| roof, suspension, determinant | none | not supplied |

The key ownership fact is not merely that the word is finite. The construction
changes the map and its dimension when the word changes. Hence no one frozen
F_w can claim to generate the unbounded prime-symbolic source from which w was
extracted. A finite word may be a legitimate control, but it cannot be silently
promoted into endogenous selection.

## Two decisive stops

P28 explicitly distinguishes its cycles from phase-space periodicity: the selector
word and position-weight quotient can be periodic even though this does not make
the polynomial state periodic. Thus it cannot supply the A1 primitive closed
orbit/repetition ledger required by a suspension candidate.

Separately, the prime-related word is external input. Replacing it by any other
rooted finite word produces another valid P28 map. That adversarial substitution
shows that the geometry alone does not discriminate primes, and no unbounded
prime/composite observable is defined by the map. This is the same ownership
logic as finite-wheel controls, but tested here on a genuinely high-dimensional
autonomous symplectomorphism rather than a static finite permutation.

| Gate | Result | Reason |
| --- | --- | --- |
| lineage | partial finite-word preservation | explicit symbolic-to-shear map, but no infinite endogenous source |
| A0 | scoped FAIL | prime word is a construction input |
| A1 | NOT TESTABLE | selector cycle is not a complete phase-state orbit ledger |
| A2 | NOT EVALUATED | no same-object roof/determinant |
| Route B | NOT INVOKED | no Route-A-ready candidate |

## Decision

**Portfolio position: stop/fork.** P28's construction is retained as a geometric
design resource only. A future main candidate must fix one dimension and one
map before any prime word is chosen, define a map-internal prime-symbolic
observable, and prove that actual phase-space closed orbits—not degree or
selector cycles—own its primitive/repetition and roof data.

## Evidence index

- [P28 full-text reading copy](../../../p1_wiki/directions/symplectic_map/papers/symplectic_map--28-primitive-selector-cycle-monodromy/fulltext.md)
- [P1 Symplectic Map conclusions](../../../p1_wiki/directions/symplectic_map/conclusions.md)
- [012 sieve-constrained Hénon horseshoe screen](../012-sieve-constrained-horseshoe-screen/paper.md)
- [052 hyperbolic wheel-packet lift](../052-hyperbolic-wheel-packet-lift/paper.md)
