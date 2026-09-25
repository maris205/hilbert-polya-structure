# Independent derivation review — ASFS-20260915-WKC01

**Date:** 2026-09-15  
**Candidate status:** STOP — PRIME-ONLY PERIODIC SUPPORT; CONTINUUM PACKETS AND ORDINARY PRODUCT FAILURE.  
**Review result:** no substantive blocker found in the five propositions;
one minor measure-description clarification is requested below.  
**Calibration:** NOT_CALIBRATED.

## Scope and provenance

This is a separate-agent mathematical check of the complete
[paper](../paper.md), [frozen card](../candidate-card.md),
[claim ledger](../claim-ledger.md), [package overview](../README.md) and
[evidence index](README.md). The inverse, periodic classification, packet
quotient and divergence argument were derived from the frozen card before
the paper became available, and then checked against the complete paper.
The author was shown those preliminary findings before this final check.
No other review report was consulted. The reviewer uses the inherited
model setting; separate invocation does not establish statistically
independent error processes. This is not human peer review or a calibrated
correctness certificate.

The ARS theoretical-review discipline is used only to anchor claims,
retain adverse evidence and distinguish a stopped candidate from an
incorrect proof. No journal-fit assessment, external upload, numerical
experiment or manuscript edit is part of this review.

## Anchored checks

| Criterion | Evidence anchor | Judgement and independent check | Scope |
| --- | --- | --- | --- |
| Full inverse and symplectic form | equation: paper (3)--(4), Proposition 1 | MEETS: recovering the preceding phase, then p=P-b and q=Q-P+b, inverts both coordinates; the shear pullback is dq wedge dp | Complete cylinder, no removed momentum or point |
| Complete owned unit suspension | equation: paper (5), Section 3 | MEETS: every finite real time requires only finitely many iterates of the global inverse or map | Three-dimensional suspension; no Hamiltonian conclusion |
| Exact prime support | equation: paper (6), Proposition 2 | MEETS: a full return has m=r K_n and real momentum increment r a(n); nonnegative proper-divisor counts vanish exactly for prime labels | All n, including n=2 |
| Least periods and complete multiplicity | equation: paper (7)--(9), Proposition 3 | MEETS: simultaneous conditions K_n divides m and denominator(p) divides m give the lcm; the residual section rotation has finite order | Rational momenta of either sign, all q; irrational momenta excluded by the exact equation |
| Repetition and monodromy | equation: paper (10), Proposition 4 | MEETS: unit-roof lengths are m and r m, and powers of the shear derivative retain eigenvalue one | Parabolic degeneracy retained |
| Ordinary-product obstruction | equation: paper (11)--(12), Proposition 5 | MEETS: arbitrarily many distinct n=2, p=0 packets yield (1-exp(-s)) to the power -L, diverging for every real s>0 | Ordinary unweighted counting only; no universal regularization claim |
| Arithmetic controls and edge cases | table: paper Section 6, followed by shifted-test proof | MEETS: zero force admits every label; block cardinality excludes n>=3; shifted divisibility selects n+1 prime, including the n=2 empty-block edge | Comparators, not changes to the candidate |
| Same-object and Route boundaries | table: paper Section 7; appended candidate-card result | MEETS: source, full carrier, unit roof and counting convention remain unchanged | Formal coordinates UNASSIGNED; Route B NOT INVOKED |

## Strengths

The complete periodic equation separates arithmetic support from finite
packet multiplicity. In particular, quotienting a circle by the finite
rotation group in equation (9) leaves a circle of different packets; it
does not turn all positions into one orbit.
Evidence anchor: equation: paper (9), Proposition 3.

The divergence proof uses finite subcollections only as lower bounds
inside the complete counting convention. It does not quietly replace
the full ledger with a selected subset.
Evidence anchor: equation: paper (12), Proposition 5.

The stopped outcome preserves the genuinely positive all-integer
prime-support mechanism and does not extend the obstruction to every
scattering geometry.
Evidence anchor: text: paper Section 7, "The exact positive prime-support
result remains a reusable control."

## W1 — Clarify the measure row

**Severity:** Minor.  
**Evidence anchor:** table: paper Section 1, Measure row, result/boundary
cell.  
**Confidence:** 5 — distinction follows from the paper's own fixed points.

The row currently says "No finite invariant probability or trace
normalization". Read as a nonexistence claim, this is false: a Dirac mass
on any n=2, p=0 base fixed point is an invariant probability; the
corresponding length-one flow orbit also supports its normalized invariant
probability. The natural componentwise area has infinite total mass and
has not been assigned a finite normalization, which is the relevant
claim. Suggested minimal wording: "No finite normalization of canonical
area or trace normalization is supplied."

This clarification changes no periodic classification, divergence proof,
candidate identity or stop decision. The reviewer has not edited the
submitted manuscript. Author adjudication remains explicit.

## Reproduction and disposition

No finite sample or floating-point calculation was used. The elementary
arguments cover every label, every real momentum and every possible
positive period. There are no empirical statistics to recompute.

The evidence supports the recorded portfolio decision: **stop this
candidate, then fork**. The decisive reason is continuous short-period
packet multiplicity, not arithmetic-support failure. The same-object
ledger remains intact; no formal Route coordinate was evaluated and
Route B remains NOT INVOKED. The separate question of another scattering
map with isolated complete packets remains open.
