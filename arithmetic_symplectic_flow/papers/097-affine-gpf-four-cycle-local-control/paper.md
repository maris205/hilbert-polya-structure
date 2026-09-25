# A fixed affine-GPF map supplies one exact prime four-cycle, but not a complete orbit ledger

**Paper ID:** 097-affine-gpf-four-cycle-local-control  
**Record ID:** ASFS-SCOUT-20260914-66  
**Date / status:** 2026-09-14; OWNER-LEVEL A0 WITH LOCAL A1 PACKET  
**Route state:** No formal ASFS Route-A coordinate. Route B NOT INVOKED.

## Frozen object and same-object ledger

On positive integers define `T(n)=gpf(5n+1)`, where `gpf` returns the greatest prime factor.  The coefficient 5 is frozen because this exact map and its four-cycle appeared as a public scouting example; it was not selected after an in-project parameter scan.  This is a discrete factor-recurrence control, not a classical ASFS candidate.

| Item | Frozen definition / owner | Status |
| --- | --- | --- |
| Carrier | positive integers | discrete, not symplectic |
| Base update | `T(n)=gpf(5n+1)` | fixed, noninjectivity not resolved |
| Arithmetic source | factor operation on the current state | same-object control |
| Coding / lineage arrow | prime/composite observable to autonomous recurrence | direct first-arrow control |
| Packet | `(2,11,7,3)` with its orientation | exact local result |
| Repetitions | `r` traversals have length `4r` | exact for this packet |
| Full orbit ledger / roof / zeta / operator | none | OPEN or NOT SUPPLIED |

## Exact packet proof

Directly,

`T(2)=gpf(11)=11`, `T(11)=gpf(56)=7`, `T(7)=gpf(36)=3`, and `T(3)=gpf(16)=2`.

The four entries are distinct, so this is one primitive oriented period-four orbit.  Its repetitions are simply the `r`-fold concatenations of that oriented traversal, of length `4r` before reducing to the primitive packet.  The proof makes no assertion about any other starting state or cycle.

## Scope and controls

1. **No parameter tuning.** The coefficient 5 is a source-supplied, frozen example.  Nearby coefficients are neither enumerated nor credited.
2. **No completeness inflation.** The available source explicitly asks about general periodic behavior rather than proving it.  This record therefore labels the full periodic set `OPEN` rather than turning one packet into an A1 ledger.
3. **Arithmetic-owner control.** The rule factors `5n+1` from its own current state; no prime list, von Mangoldt weight, zero datum, or prescribed logarithmic time is inserted.
4. **Lineage/geometry control.** The construction reaches only the project’s prime-observable-to-recurrence arrow.  It supplies neither a sieve/MSS admissibility derivation nor a Hénon/conservative/symplectic realization.
5. **Cross-object control.** No unit roof, groupoid path space, or zeta from 078, 084, 087, or 094 is borrowed.

## Gate assessment

| Gate | Evidence for this exact object | Status | Limitation |
| --- | --- | --- | --- |
| A0 | fixed state-dependent prime-factor rule | owner-level positive control | no later lineage arrows |
| A1 | one primitive four-packet and exact repetitions | local packet established; global ledger OPEN | no enumeration/completeness theorem |
| A2 | no roof or analytic object | NOT EVALUATED | none |
| Route B | not evaluated | NOT INVOKED | unchanged |

## Decision

**Portfolio position: stop, then fork.** The local packet is more than a wandering prime output, but it is not a complete same-object A1 ledger and the carrier is discrete/noninvertible.  The next screen must seek a proof-level reversible or symplectic realization of a prime-symbolic return law, not a new roof or selected parameter for this map.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source and exact calculation](evidence/README.md)
- [084 affine-GPF complete two-cycle control](../084-affine-gpf-two-cycle-control/paper.md)
- [086 direct-factor frontier](../086-prime-factor-recurrence-frontier/paper.md)
