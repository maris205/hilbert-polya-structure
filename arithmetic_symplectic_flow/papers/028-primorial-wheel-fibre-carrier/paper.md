# A fibrewise recurrent carrier for exact primorial gap dynamics

**Paper ID:** `028-primorial-wheel-fibre-carrier`  
**Candidate ID:** `AFC-20260914-PWF01`  
**Date / status:** `2026-09-14; T0/T2 ESTABLISHED; T1 PARTIAL; T3 OPEN`  
**Route state:** `Broadened owner-level audit only; classical Route A not evaluated; Route B NOT INVOKED`

## Construction and lineage

For `P_k=p_k#`, let `W_k=(Z/P_k Z)^times`.  Put its representatives in their
cyclic numerical order and let `next_k` send every reduced residue to its next
one.  On `W=disjoint_union W_k`, define `R(k,a)=(k,next_k(a))`.  The orbit in
fibre `k` is precisely the cyclic wheel encoded by `G(P_k)`.

The carrier also includes the directed relation `E_k` given by the exact sieve
recursion from `G(P_k)` to `G(P_(k+1))`.  This relation is not silently made
invertible.  Its first operation reads `p_(k+1)=g_1+1` from the current cycle.
Thus the construction records the whole intended lineage:

```text
prime/composite sieve -> symbolic gap admissibility -> sequential update
-> cyclic wheel packets -> possible later conservative realization.
```

## T0--T2 audit

The closed packet is not an externally selected single wheel: every `k` is a
component of the frozen carrier, and the transition relation remains visible.
For each `k`, `R_k` is a cyclic permutation of exactly `phi(P_k)` residues.
One traversal has `phi(P_k)` unit steps and an `r`-fold traversal has
`r phi(P_k)` steps.  Packet multiplicity is retained: the `phi(P_k)` marked
basepoints are parametrizations of the same cyclic packet, not `phi(P_k)`
silently selected prime orbits.

This establishes T0 and T2.  T1 is only partial.  The source mechanism reads
the next prime endogenously, but neither `R` nor `E` produces a same-object
prime-time law such as `log p`.  Assigning such a roof would be prohibited
manual insertion.  The object is discrete and fibrewise recurrent, not a
classical symplectic suspension.

## Same-object boundary and decision

No transfer operator, zeta, trace, contact form, symplectic form, or quantum
object is borrowed.  Consequently T3 remains OPEN.  The object advances the
portfolio only as a broadened partial carrier: it demonstrates that the exact
sieve recursion and nondegenerate closed packets can coexist without a terminal
wheel choice, while exposing the unresolved clock bridge.

**Portfolio decision: advance conditionally.** Do not deepen T3 until a
same-object endogenous clock is found.  Fork if a proposed clock uses
`log p`, prime tables, or a different carrier; otherwise a future construction
must define it from `R` and `E` and retain the displayed packet multiplicity.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source/method record](evidence/README.md)
