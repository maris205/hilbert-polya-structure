# Frozen candidate card — ANG-20260918-LFT01

**Paper ID:** 224-log-factor-torus-flow  
**Candidate ID:** ANG-20260918-LFT01  
**Date:** 2026-09-18  
**Version:** 1; frozen before the proof record.  
**Initial status:** PRE-P0 BROADENED SCREEN — SINGLETON/MIXED ORBIT LEDGER OPEN; LOG-SCALE NATURALNESS OPEN.  
**Formal Route coordinates:** UNASSIGNED; **Route B:** NOT INVOKED.

## Frozen carrier and arithmetic source

Let \(\mathsf M=(\mathbb N_{\ge 1},\cdot)\) and let
\(\mathbb R[\mathsf M]\) be its monoid algebra with basis
\(e_n\) and product \(e_m e_n=e_{mn}\).  Define the intrinsic atom set

\[
 \mathsf A=\{a>1:a=bc\text{ with }b,c\in\mathbb N_{\ge1}
 \text{ only when }b=1\text{ or }c=1\}.
\]

By unique factorisation, \(\mathsf A\) is exactly the set of primes.  The
definition is a divisor-admissibility rule, not a supplied prime table.  Let
\(\mathcal J\) be the set of all nonempty finite subsets of \(\mathsf A\).
For \(J\in\mathcal J\), freeze

\[
 T_J=\prod_{a\in J}\mathbb R/(\log a)\mathbb Z,
 \qquad
 X_{\mathrm{LFT}}=\coprod_{J\in\mathcal J}T_J.
\]

The action is the one-owner continuous flow

\[
 \phi^t_J((\theta_a)_{a\in J})
   =(\theta_a+t\pmod{\log a})_{a\in J}.
\]

The logarithmic lattice is a **declared scale design** in this candidate.
Its arithmetic naturalness is OPEN; it is not claimed that the divisor
admissibility rule itself derives a physical \(\log a\) speed.

| Field | Frozen scope |
| --- | --- |
| Carrier/type | Countable graded disjoint coproduct of compact tori with the \(\mathbb R\)-action above; locally compact and second countable; broadened `ANG` action/groupoid carrier |
| Lineage arrow | Prime/composite observable → divisor admissibility → indecomposable monoid-algebra atoms → finite-support symbolic packets → torus flow |
| Arithmetic input | Multiplication and divisibility on positive integers only; no supplied prime list, prime times, von Mangoldt data, or zeros |
| Action/flow | The fixed translation \(\phi^t_J\) on every finite atom-set component |
| Primitive packets | Every actual closed flow orbit of the full coproduct, modulo time phase; no selected representative of a mixed torus |
| Clock | Coordinate periods \(\log a\), explicitly declared design; naturalness OPEN |
| Repetitions | A singleton \(a\)-circle has repeats \(m\log a\), \(m\ge1\); mixed components have no closed repetitions |
| Operator/trace/determinant | NOT SUPPLIED; a future same-object owner would require a new contract |
| Classical symplectic fields | NOT APPLICABLE; no finite-dimensional symplectic map, mapping torus, or Hamiltonian lift is claimed |
| Controls | Two-atom incommensurability; all finite \(J\), not only singleton sectors; full coproduct versus selected prime sector |
| Stop/fork rule | Adding momenta, cotangent fibers, a roof, or a symplectic realization creates a new candidate ID. A new clock cannot inherit this card. |
| Broadened gates | T0 same-object carrier/action: ESTABLISHED at owner level; T1 arithmetic/clock: atom source established, scale naturalness OPEN; T2 packet/repetition: exact classification; T3: NOT SUPPLIED |

## Precommitted discriminators

1. Prove from unique factorisation that \(\mathsf A\) is the prime set; do not
   enumerate primes as input.
2. Classify all closed orbits of every \(T_J\), including mixed \(|J|\ge2\)
   components.  The full coproduct, not a chosen singleton subfamily, owns the
   ledger.
3. Keep the scale declaration separate from the source proof.  Exact periods
   do not by themselves establish naturalness of the logarithmic lattice.
4. Compare only at the boundary level with 193 and 196: neither their carrier,
   completion, cotangent lift, operator, or trace may be imported.
5. Do not add a momentum/cotangent lift in this paper.  Such a lift would make
   continuum momentum packets and is a fresh ownership problem.

The candidate is not a finite-dimensional symplectic or classical Route-A
object.  Its broadened result is limited to the exact action, the full
closed-orbit classification, and the stated naturalness boundary.

## Scope correction after the exact orbit audit

The phrase “mixed nonrecurrent” is not used for this candidate.  Mixed
components have no exact positive period, but their compact translations are
recurrent in the topological/measure-theoretic sense.  The frozen claim is
**nonperiodic**, with two-atom density and higher-rank density left subject to
the reciprocal-log frequency condition recorded in the paper.  This corrects
terminology only; it does not change the carrier, action, source, or owner.
