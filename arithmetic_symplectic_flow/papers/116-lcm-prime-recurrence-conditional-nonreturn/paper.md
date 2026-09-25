# A conditional LCM prime recurrence cannot supply a recurrent arithmetic owner

**Paper ID:** `116-lcm-prime-recurrence-conditional-nonreturn`  
**Record ID:** `ASFS-SCOUT-20260914-83`  
**Date / status:** `2026-09-14; PRE-P0 STOP — CONDITIONAL PRIME-INCREMENT CLAIM AND STRICTLY ADVANCING ARITHMETIC OWNER`  
**Route state:** `No formal ASFS Route-A coordinate; Route B NOT INVOKED`

## 1. Frozen source construction

The source defines the fixed arithmetic recurrence

\[
a_1=1,\qquad a_n=a_{n-1}+\operatorname{lcm}(n,a_{n-1})\quad(n\ge2),
\]

and its relative increment \(b_n=a_n/a_{n-1}-1\).  Its exact identity is

\[
b_n=\frac{\operatorname{lcm}(n,a_{n-1})}{a_{n-1}}
=\frac{n}{\gcd(n,a_{n-1})},
\]

so \(b_n\mid n\).  No prime list, prime-indexed parameter, or selected
cutoff is part of this rule.

The tempting stronger interpretation must remain conditional: the source
describes the statement that every \(b_n\) is \(1\) or prime as a conjecture
and connects it to a strong version of Linnik's theorem which it says is
unproved.  Consequently this screen does not use finite examples or the
source's prime-index observations as an A0 closure.

## 2. Exact owner and nonreturn

The recurrence cannot be made autonomous by forgetting where it is in the
sequence.  A faithful state includes the current step and accumulator.  With
a consistent shifted convention its update has the form

\[
(n,a)\longmapsto\bigl(n+1,\,a+\operatorname{lcm}(n+1,a)\bigr).
\]

For every positive number of updates, the first coordinate has increased by
that number.  Therefore this exact arithmetic-generating action has no
periodic point.  Quotienting or resetting the step coordinate would change the
source action and would not preserve the data needed to evaluate its next LCM
update.  A prospective periodic orbit of another quotient or extension cannot
be borrowed as a primitive packet here.

## 3. Lineage and gate assessment

This is a direct arithmetic-divisibility recurrence, not a documented
deformation of the project's prime/composite symbolic observable or
admissibility constraint through sequential Logistic-type dynamics and the
area-preserving Hénon/conservative bridge.  Its fixed update is useful as a
breadth control near the source end of that lineage, but it has no stated
symplectic base-map realization.

| Gate | Evidence for this exact screen | Status |
| --- | --- | --- |
| A0 | fixed endogenous divisibility update, but its global prime-or-one interpretation is conditional and the required symbolic-to-geometric lineage is absent | `NOT_TESTABLE` / scoped admission FAIL |
| A1 | the step coordinate strictly increases on every faithful update | scoped FAIL |
| A2 | no roof, transfer operator, or determinant belongs to this object | NOT EVALUATED |
| Route B | no Route-A readiness | NOT INVOKED |

**Portfolio position: stop and fork.**  This screen sharpens the difference
between a self-contained arithmetic update and an arithmetic mechanism with a
prime-carrying recurrent packet.  A next architecture must provide a proved or
otherwise independently auditable prime-symbolic mechanism, retain enough
state to define its update, and still admit nontrivial return before any
Hénon/conservative lift is investigated.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source record](evidence/README.md)
- [090 Rowland GCD recurrence control](../090-rowland-gcd-recurrence-nonreturn/paper.md)
- [063 monotone-elimination rule](../063-monotone-elimination-periodic-rigidity/paper.md)
- [108 source-action frontier](../108-source-action-frontier-cycle-11/paper.md)
