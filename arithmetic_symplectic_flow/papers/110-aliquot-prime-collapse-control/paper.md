# Aliquot dynamics internally recognizes primes but sends every prime state to a terminating branch

**Paper ID:** 110-aliquot-prime-collapse-control  
**Record ID:** ASFS-SCOUT-20260914-77  
**Date / status:** 2026-09-14; PRE-P0 ARITHMETIC A0 / A1 NEGATIVE CONTROL  
**Route state:** No formal ASFS Route-A coordinate. Route B NOT INVOKED.

## Frozen action

On positive integers define the aliquot map \(s(n)=\sigma(n)-n\), the sum of proper positive divisors. The usual forward convention terminates after reaching \(1\) because \(s(1)=0\). This one fixed rule is arithmetic-state internal; no prime table or per-prime parameter is supplied.

For every \(n>1\),

\[
s(n)=1 \quad\Longleftrightarrow\quad n\text{ is prime}.
\]

Indeed a prime has only the proper divisor \(1\); conversely a composite \(n>1\) has the distinct proper divisors \(1\) and a nontrivial divisor, so its proper-divisor sum exceeds \(1\). Thus the map has a genuine endogenous prime/composite observable.

## Exact prime-packet obstruction

If \(p\) is prime, then \(p\mapsto1\mapsto0\) under the stated convention. Therefore no prime state lies on a periodic orbit of this same action. In contrast, \(6\) is a composite fixed point and \(220\leftrightarrow284\) is an amicable composite 2-cycle; longer sociable cycles are also known. The action has real periodic packets, but none is a prime packet. Selecting those composite cycles as prime representatives would violate the arithmetic-owner condition.

## Lineage and geometry boundary

This gives an owner-level arithmetic control but is not a documented deformation of the prior Eratosthenes/MSS word through the Logistic-to-Hénon route. It uses divisor sums rather than a sieve survivor update. It also defines no reversible map, Hénon/conservative lift, symplectic base, roof, suspension, or same-object analytic owner.

| Gate | Status | Reason |
| --- | --- | --- |
| A0 | owner-level arithmetic control | primality is exactly a state-internal branch test |
| A1 | scoped FAIL for prime relevance | every prime terminates; known cycles are composite |
| A2 | NOT EVALUATED | no roof/operator/determinant |
| Route B | NOT INVOKED | unchanged |

**Portfolio position: stop, then fork.** Do not re-label perfect, amicable, or sociable composite cycles as prime orbits, and do not add a return from \(1\) to a chosen prime; either would change the frozen action. A later candidate must retain the desirable internal arithmetic test while making prime-side states recurrent under the same documented action.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source boundary](evidence/README.md)
- [031 primality-automaton collapse control](../031-primality-automaton-attractor-screen/paper.md)
