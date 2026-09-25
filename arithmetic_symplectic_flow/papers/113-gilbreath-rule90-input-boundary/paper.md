# Gilbreath–Rule-90 analysis begins with a supplied prime-difference row

**Paper ID:** `113-gilbreath-rule90-input-boundary`  
**Record ID:** `ASFS-SCOUT-20260914-80`  
**Date / status:** `2026-09-14; PRE-P0 STOP — PRIME-DIFFERENCE INPUT IS EXTERNAL TO THE RULE-90 ACTION`  
**Route state:** `No formal ASFS Route-A coordinate; Route B NOT INVOKED`

## Frozen construction and lineage location

Gilbreath's construction starts with consecutive primes \(p_n\), forms their
absolute-difference rows, and repeats.  It is therefore directly adjacent to
the project's desired early lineage:

\[
\text{prime distribution}\longrightarrow\text{prime gaps/difference words}
\longrightarrow\text{local symbolic evolution}.
\]

On portions of the difference triangle whose entries are \(0\) or \(2\), the
rescaled binary pattern has a Rule-90 description: each next binary value is
the XOR of its two neighbours.  Rule 90 is a fixed local CA.  This is a useful
symbolic comparator, but it starts after the prime row has already been
supplied.

| Item | Same-object owner | Status |
| --- | --- | --- |
| Prime-side datum | the ordered input \((p_n)\) and its difference rows | external input to CA |
| CA rule | fixed XOR neighbour rule | independent symbolic action |
| Arithmetic assertion | Gilbreath leading-entry condition | conjectural / not used |
| Natural prime-carrying recurrent packet | none supplied | absent |
| Hénon/symplectic base, roof, suspension, operator | none supplied | absent |

## Decisive ownership audit

The Rule-90 local update contains no state operation that selects the next
prime, computes a prime gap, or verifies that its input row came from primes.
Replacing the initial binary row by another \(0,1\) row preserves the rule and
its CA dynamics.  Consequently, any periodic configuration obtained by a
separate periodic boundary condition or selected initial configuration belongs
to Rule 90, not to the prime-difference source.

Nor can the open Gilbreath leading-entry assertion be used as an arithmetic
certificate.  The screen relies only on the definitions, not on its truth or
on any finite computation.  Thus it does not refute the value of Gilbreath
differences as a source-side observable; it rejects the attempted ownership
transfer from a supplied arithmetic row to an independent CA orbit ledger.

## Gate assessment and decision

| Gate | Evidence for this exact screen | Status |
| --- | --- | --- |
| A0 | prime gap/difference row is supplied before the fixed XOR action | scoped FAIL |
| A1 | generic Rule-90 recurrence cannot replace the missing arithmetic owner | NOT USED after A0 fail |
| A2 | no same-object roof, operator, or determinant | NOT EVALUATED |
| Route B | no Route-A readiness | NOT INVOKED |

**Portfolio position: stop and fork.**  The construction preserves a direct
prime-symbolic comparison arrow, but not an endogenous action.  A viable fork
must make the arithmetic difference update itself part of the recurrent state
evolution, without importing the full prime row or selecting unrelated CA
cycles.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source record](evidence/README.md)
- [053 endogenous sieve CA contrast](../053-realtime-sieve-ca-nonrecurrence/paper.md)
- [105 arithmetic-word shift boundary](../105-mobius-liouville-shift-input-boundary/paper.md)
- [108 source-action frontier](../108-source-action-frontier-cycle-11/paper.md)
