# HCS-C33 Phase 1: Hénon equal-action collisions and the Hill Kummer gate

**Date:** 2026-08-12  
**Stage:** Phase-1 design freeze; exact pilot passed; Phase 2 awaits user confirmation

This project keeps the area-preserving Hénon family

\[
H_A(q,p)=(1-Aq^2-p,q)
\]

and its cyclic generating action.  It does not extend the C32 prime scan.
Instead, it studies the global parameter geometry behind C32's finite-field
collision: two distinct exact period-five orbits can have the same action
while retaining different Hill determinants.

## The new object

Let \(G_A(q)\) be the exact period-five reversor-line marker and let
\(\Phi_{5,A}\) be the five-step cyclic action.  Eliminating \(q\) from

\[
G_A(q)=0,
\qquad
c=\Phi_{5,A}(q)
\]

gives a degree-six plane curve \(W_5(A,c)=0\).  Its normalization is the old
period-five marker cover, so the normalization and its ordinary Galois group
are not new.  The new datum is the singular embedding by the action map.

The exact pilot gives

\[
\operatorname{Disc}_c W_5
=2^{12}3^{30}A^{60}P_2(A)^5P_5(A)^3P_9(A)^2,
\]

where \(P_2P_5\) is exactly the discriminant support of the old marker cover,
whereas the irreducible degree-nine factor \(P_9\) is coprime to it.  Thus a
generic root of \(P_9\) is not a collision of periodic points.  It is a
collision of the action values of two distinct, nondegenerate periodic
orbits.

The collision parameters themselves have full arithmetic monodromy:

\[
\operatorname{Gal}(P_9/\mathbb Q)\cong S_9.
\]

This follows from exact squarefree factorizations with cycle types \((9)\)
modulo \(7\), \((5,2,1,1)\) modulo \(17\), and \((8,1)\) modulo \(23\).
The claim concerns the new degree-nine collision divisor, not the already
known degree-six orbit-marker normalization.

The two branches have Hill values \(h_1,h_2\).  Their isometry gate is the
square class of \(h_1/h_2\), which equals the square class of the symmetric
product

\[
N_H=h_1h_2.
\]

Therefore this datum descends to the degree-nine collision field.  The pilot
computes \(N_H\) exactly and proves it is not a square by its rational field
norm.  Hence

\[
u^2=N_H
\]

is a genuinely nontrivial quadratic Kummer cover of the equal-action node
locus.  Phase 1 does not claim that the Galois closure of this quadratic
decoration is the full wreath product \(C_2\wr S_9\); independence of all
nine conjugate square classes is a later, separately falsifiable gate.

## Why this is a large door

The cover distinguishes two phenomena that C32 could not separate locally:

- at some primes, an equal-action collision also makes the two Morse-local
  quadratic factors isomorphic;
- at other primes, the action still collides but the Hill square classes
  remain different.

At \(A=6\), the same degree-nine divisor explains both behaviors.  The prime
\(61\) reproduces the exact C32 collision, while the prime \(3203\) is a
matched counter-control where the equal-action node survives but the Hill
ratio is nonsquare.

This is Hénon-specific arithmetic geometry, but it is not yet a
Hilbert--Pólya construction.  No Euler product, critical-line theorem, or
self-adjoint operator is claimed.

## Local duplication firewall

- The repository's
  [candidate registry](../next_paper_henon_candidate_search/CANDIDATE_REGISTRY.md)
  already records the C12B/Endler--Gallas collision for the period-five
  marker sextic.  C33 therefore forbids novelty claims about that sextic's
  ordinary \(S_6\) cover.
- The [C12A project](../henon_frobenius_scheme_obstruction/README.md) already
  treats the low-period Frobenius-scheme obstruction.
- The [C32 Phase-3 project](../phase3_hcs_c32_artin_schreier_quantum_trace/README.md)
  supplies the two equal-action Morse germs at \(p=61\); C33 treats them as a
  regression control, not a prediction.

The unclaimed-before-search candidate is precisely the coupled triple:
degree-nine Maxwell divisor, transverse nonparabolic Hénon node, and
nontrivial Hill Kummer square class.

## Phase-1 files

- `RESEARCH_QUESTION_BRIEF.md`: frozen question, scope, and FINER assessment.
- `METHODOLOGY_BLUEPRINT.md`: exact producer/checker plan and falsifiers.
- `PILOT_LEDGER.md`: theorem-level symbolic pilot and finite-prime controls.
- `DEVILS_ADVOCATE_CHECKPOINT1.md`: mandatory adversarial design review.

## Gate to Phase 2

Phase 2 will begin only after user confirmation.  It will perform the
primary-source novelty audit and implement a fail-closed exact certificate.
The first stop condition is a direct prior-work collision for the specific
degree-nine action-node/Kummer object.
