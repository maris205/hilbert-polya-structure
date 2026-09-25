# Quadratic-form toggle sieving is a nonmonotone source deformation, not yet a recurrent arithmetic carrier

**Paper ID:** `064-atkin-toggle-sieve-return-screen`  
**Record ID:** `ASFS-SCOUT-20260914-42`  
**Date / status:** `2026-09-14; PRE-P0 STOP`  
**Route state:** `No P0 or Route-A coordinate; Route B NOT INVOKED`.

## Source and lineage

Atkin and Bernstein enumerate primes up to a requested bound using values of binary quadratic forms. Candidate residue bits are toggled according to parity of representation counts, and square-factor multiples are then removed. This is a genuine deformation of the project’s starting source:

```text
prime/composite classification -> arithmetic sieve symbols -> sequential quadratic-form toggles.
```

Unlike a deletion-only Eratosthenes encoding, an intermediate toggle is not monotone. Therefore 063 does not decide this screen and no monotonicity shortcut is used.

## The recurrence test

The source algorithm is explicitly an enumerator **up to** a bound `N`, or in its practical form over an output segment `[L,L+B)`. To continue producing new prime classifications, the output frontier changes: `N` increases or the segment is replaced by a later one. A faithful global state must retain enough information to identify which output interval has been produced; otherwise a repeated bit vector for two different intervals would identify different integers and would no longer own the claimed prime/composite predicate.

Thus, even though bits may toggle inside a fixed finite job, the exact enumerating trajectory carries an unbounded progress coordinate. If `J` denotes the right endpoint of the completed output interval, continuation has `J -> J'` with `J'>J`. The strict-frontier argument of 018 applies to this whole-job action: it has no periodic point that executes a new output-extension event. Returning to a previously used interval only recomputes a finite task and does not enumerate the next primes; it cannot become a global primitive orbit ledger without externally selecting the interval and its factor data.

This is an A1 stop before P0, not a claim that individual finite toggle circuits lack cycles or that all conceivable reversible quadratic-form arithmetic is impossible.

## Same-object audit

| Requirement | Finding | Status |
| --- | --- | --- |
| Endogenous arithmetic source | quadratic-form parity plus squarefree culling computes the bounded prime set | symbolic positive control |
| Nonmonotone local law | toggles pass the 063 exclusion boundary | established source distinction |
| Recurrent carrier for the complete source | bound/segment frontier advances | scoped A1 FAIL |
| Hénon/conservative lift | none is defined by the source | absent |
| Symplectic base, roof, suspension | none | P0 not admitted |
| Orbit/determinant owner | none | not evaluated |
| Route B | no same-object Route-A readiness | NOT INVOKED |

## Controls and decision

- **Deletion-only control:** this screen does not relabel Atkin toggles as a monotone deletion process; 063 remains inapplicable to its intermediate representation layer.
- **Finite-job control:** fixing one `N` or one segment creates an externally selected finite computation, analogous to a fixed wheel rather than an all-prime arithmetic source.
- **Owner control:** no symbolic circuit cycle is substituted for a closed orbit of an unspecified Hénon or symplectic map.

**Decision: `stop/fork`.** This is a useful broadened source family because it escapes a too-narrow deletion-only model, but it still fails the immediate return test. A future reopening requires an autonomous, boundary-free action that retains the quadratic-form arithmetic predicate and possesses its own nontrivial periodic packet convention.

## Evidence index

- [Atkin and Bernstein, *Prime sieves using binary quadratic forms*](https://cr.yp.to/papers/primesieves-20020329-retypeset20220327.pdf)
- [018 strict frontier obstruction](../018-monotone-sieve-clock-obstruction/paper.md)
- [063 monotone-elimination boundary](../063-monotone-elimination-periodic-rigidity/paper.md)
