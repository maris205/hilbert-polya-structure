# Arithmetic billiards geometrize supplied gcd/lcm data but do not generate a prime-symbolic carrier

**Paper ID:** 103-arithmetic-billiard-static-input-boundary  
**Record ID:** ASFS-SCOUT-20260914-71  
**Date / status:** 2026-09-14; PRE-P0 NEGATIVE OWNERSHIP AUDIT  
**Route state:** No formal ASFS Route-A coordinate. Route B NOT INVOKED.

## Screen

An arithmetic billiard starts with a rectangle whose two side lengths are chosen positive integers.  The reflected diagonal path expresses their gcd/lcm, and periodicity properties depend on whether the selected dimensions are coprime.  This gives a concrete geometry-plus-periodicity control, but the arithmetic is already frozen in the table dimensions.

| Requirement | Finding |
| --- | --- |
| Endogenous prime/sieve state | absent: dimensions are supplied inputs |
| Symbolic lineage | gcd/lcm geometry only; no sieve/MSS transition |
| Actual periodicity | yes, for the specified billiard instance |
| One fixed varying-prime action | absent |
| Conservative/Hénon owner and roof | not supplied |

## Controls and decision

Changing the integer pair changes the billiard table before a trajectory evolves.  Selecting prime side lengths would therefore be the prohibited external prime-sized-carrier pattern; selecting arbitrary composite dimensions yields the same billiard architecture and its periodicity.  It consequently fails the label-blind and static-decoration controls, much like a lattice invariant attached to an otherwise arithmetic-blind Hénon map.

**Portfolio position: stop, then fork.** The source is retained as a geometric A1 control only. It does not cross the required prime-symbolic-to-sequential-to-conservative lineage arrow.

| Gate | Status |
| --- | --- |
| A0 | scoped FAIL — static input arithmetic |
| A1 | NOT USED — geometric periodicity cannot rescue A0 |
| A2 | NOT EVALUATED |
| Route B | NOT INVOKED |

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source boundary](evidence/README.md)
