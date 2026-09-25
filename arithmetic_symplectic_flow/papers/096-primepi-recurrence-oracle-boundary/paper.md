# A fixed PrimePi recurrence has a terminal fixed state but imports the whole prime-counting function

**Paper ID:** 096-primepi-recurrence-oracle-boundary  
**Record ID:** ASFS-SCOUT-20260914-65  
**Date / status:** 2026-09-14; PRE-P0 NEGATIVE ORACLE-OWNERSHIP AUDIT  
**Route state:** No formal ASFS Route-A coordinate. Route B NOT INVOKED.

## Frozen object and same-object ledger

Let `pi(N)` count primes at most `N`, and define the autonomous map
`F(x1,x2,x3,x4,x5)=(x2,x3,x4,x5,pi(x1+x2+x3+x4+x5))` on nonnegative five-tuples.  The listed trajectory starts at `(1,1,1,1,1)`.  This is frozen only as a screen, not as a classical P0 candidate.

| Item | Frozen definition / owner | Status |
| --- | --- | --- |
| Phase space | nonnegative integer five-tuples | fixed discrete carrier |
| Base update | `F` above | fixed but noninvertible |
| Arithmetic source | the already-defined global function `pi` | external oracle boundary |
| Symbolic lineage | none supplied | scoped FAIL |
| Closed state | constant five-tuple `66`, since `pi(330)=66` | exact local control |
| Roof, suspension, transfer object | none | NOT SUPPLIED |
| Operator / Route owner | none | NOT SUPPLIED |

## Result

The recurrence has genuine self-map recurrence: the constant state `66` is fixed.  This does not establish A0.  The prime distribution has already been compressed into the update function `pi`; evaluating that function requires exactly the prime predicate/counting information the proposed dynamics is meant to organize.  A finite recurrence wrapped around this oracle does not produce an admissibility rule from a prime-symbolic state.

The fixed point also carries the non-prime integer label `66`, and its existence is not a prime-side primitive closed-orbit dictionary.  Treating its coordinates, the fixed-state equation, or a chosen roof as a prime clock would be a new manually specified object and a prohibited repair.

## Controls

1. **Oracle control.** Replacing `pi` by an arbitrary counting function produces the same recurrence architecture; all prime specificity is supplied in the called function, not in its state transition geometry.
2. **Factor-oracle control.** This is parallel in ownership defect, but not identical in formula, to the GPF fixed-point control 082: one imports prime counting rather than greatest-factor recognition.
3. **Lineage control.** There is no documented arrow from prior sieve/MSS admissibility through a sequential or Hénon deformation to `F`.
4. **A1 non-rescue control.** The 66 fixed state is recorded, but A1 is not evaluated as a route gate because A0 has already failed and no roof/repetition target is supplied.

## Gate assessment

| Gate | Evidence for this exact screen | Status | Limitation / decision |
| --- | --- | --- | --- |
| A0 | `pi` is an explicitly invoked global prime-counting oracle | scoped FAIL | stop before P0 |
| A1 | one fixed state verified | NOT USED | cannot rescue A0 or establish a prime packet |
| A2 | no roof or analytic object | NOT EVALUATED | none |
| Route B | not evaluated | NOT INVOKED | unchanged |

## Decision

**Portfolio position: stop, then fork.** Future candidates may use an arithmetic predicate only if the same state action derives it through a documented prime-symbolic transition; wrapping the completed global count function in a recurrence is excluded.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source and method boundary](evidence/README.md)
- [082 GPF fixed-point oracle boundary](../082-gpf-fixed-point-euler-control/paper.md)
