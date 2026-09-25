# Reversible computation can implement a finite sieve without becoming a recurrent arithmetic flow

**Paper ID:** 099-reversible-sieve-computation-boundary  
**Record ID:** ASFS-SCOUT-20260914-67  
**Date / status:** 2026-09-14; PRE-P0 NEGATIVE OWNERSHIP AUDIT  
**Route state:** No formal ASFS Route-A coordinate. Route B NOT INVOKED.

## Objects screened

This record compares, but does not merge, two computation-level formulations.

| Object | Arithmetic owner | Reversibility owner | Decisive boundary |
| --- | --- | --- | --- |
| Quantum E-state sieve | a finite register/cutoff and divisor relation | generic reversible classical-to-quantum compilation | finite computation, not an autonomous phase-space return map |
| Process-calculus sieve | initial candidate and value sets bounded by `l` | oracle-supported reversible reductions | externally initialized finite instance; no progress guarantee in pure reversibility |

The first source describes E-states structurally analogous to a sieve and an implementation on a universal quantum computer.  It does not define a single prime-symbolic dynamical orbit whose return data is intrinsic.  The second source starts with `{2,...,l}`, successively removes multiples, and makes the oracle responsible for the update context.  Thus the primes are the output of a specified finite algorithm, rather than a recurrent state observable of one fixed action.

## Controls

1. **Cutoff control.** Changing `n` or `l` changes the finite computational instance before dynamics; finite instances cannot be pooled as one orbit ledger.
2. **Universal-compilation control.** That an arbitrary reversible classical function can be compiled into a quantum calculation is precisely the generic-programming mechanism ruled out by 011; it does not make prime selection endogenous.
3. **Progress control.** The process-calculus source says pure causal reversibility permits endless forward/backward looping and does not ensure eventual sieve completion.
4. **Lineage/geometry control.** An Eratosthenes algorithm gives genuine prime-symbolic ancestry, but no specified Hénon, conservative, symplectic, roofed, or closed-orbit owner connects it to later arrows.

## Gate assessment

| Gate | Evidence for this screen | Status | Decision |
| --- | --- | --- | --- |
| A0 | finite external sieve state or generic compilation supplies prime output | scoped FAIL | stop before P0 |
| A1 | no intrinsic closed packets/repetitions | NOT TESTABLE | no rescue after A0 failure |
| A2 | no roof or same-object analytic object | NOT EVALUATED | none |
| Route B | not evaluated | NOT INVOKED | unchanged |

## Decision

**Portfolio position: stop, then fork.** Reversibility at the level of a compiler, oracle, or history-bearing algorithm is not the required reversible prime-symbolic action.  Continue only with sources in which both arithmetic selection and recurrence are properties of the same fixed state evolution.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source boundary](evidence/README.md)
- [011 related universal-simulation boundary](../011-reversible-sieve-simulation-control/paper.md)
