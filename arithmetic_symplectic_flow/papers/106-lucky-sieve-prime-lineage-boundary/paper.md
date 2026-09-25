# The self-selected lucky sieve is not a prime-symbolic recurrent carrier

**Paper ID:** 106-lucky-sieve-prime-lineage-boundary  
**Record ID:** ASFS-SCOUT-20260914-74  
**Date / status:** 2026-09-14; PRE-P0 NEGATIVE LINEAGE / RECURRENCE AUDIT  
**Route state:** No formal ASFS Route-A coordinate. Route B NOT INVOKED.

## Screen

The lucky sieve begins with positive integers, deletes every second survivor, then uses the next surviving number as the spacing for the next *positional* deletion. Thus the survivor state selects its next filter:

```text
survivor word -> internally selected positional filter -> next survivor word.
```

This is a real sequential sieve deformation, unlike a prime table supplied as input. But its survivors are lucky numbers, not the prime/composite classification. The source distinguishes its rank-based deletion from Eratosthenes divisibility deletion. Prime-number-theorem-type asymptotics do not provide an intertwiner between the two sequences.

## Decisive stop tests

1. **Target/lineage.** The action’s endogenous output is a distinct arithmetic sequence. Relabelling lucky survivors as primes would replace the programme’s prime-side observable rather than define a justified deformation.
2. **Recurrence.** With `E` the cumulative effective deletions (or a state-faithful equivalent), each effective update strictly enlarges `E`. The monotone-elimination theorem in 063 rules out a nontrivial periodic orbit that executes that same update law.
3. **Geometry owner.** The source supplies no Hénon/symplectic base, roof, suspension, primitive packet convention, or analytic owner. Fixing a finite stage would select an external finite computation.

## Gate assessment and decision

| Gate | Status | Reason |
| --- | --- | --- |
| A0 | scoped FAIL | endogenous rule outputs lucky, not prime-symbolic, classification |
| A1 | scoped FAIL | state-faithful effective deletion is nonrecurrent |
| A2 | NOT EVALUATED | no same-object roof/operator/determinant |
| Route B | NOT INVOKED | unchanged |

**Portfolio position: stop, then fork.** A valid future deformation must retain a precise prime-side observable while replacing monotone deletion with an auditable recurrent rule.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source boundary](evidence/README.md)
- [063 monotone-elimination theorem](../063-monotone-elimination-periodic-rigidity/paper.md)
- [064 Atkin comparator](../064-atkin-toggle-sieve-return-screen/paper.md)
