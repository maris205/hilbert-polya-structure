# A sieve-based primality automaton is not a prime orbit carrier

**Paper ID:** `031-primality-automaton-attractor-screen`  
**Record ID:** `ASFS-SCOUT-20260914-23`  
**Date / status:** `2026-09-14; PRE-P0 STOP — INPUT-FAMILY OWNERSHIP; PRIME FIXED-POINT COLLAPSE`  
**Route state:** `No frozen candidate; Route A not evaluated; Route B NOT INVOKED`

## Audit

The source describes a sieve-based automaton for a separately encoded integer
`n`: prime inputs reach `(0,0)` while composites reach a `4p+2` cycle labelled
by least prime factor `p`. It is a real prime/composite symbolic computation,
but each `n` requires a new initial input. Distinct primes are not different
primitive packets: all collapse to the same fixed point. Nontrivial cycles are
instead associated with composites and a factor of that separate input.

Treating this family as one prime flow would silently assemble independently
selected computations and would work for any decidable predicate. No global
sequential carrier, conservative lift, symplectic map, roof, or trace owner is
specified.

**Portfolio decision: stop/fork.** Keep it as a `PROVES_TOO_MUCH` ownership
control. A viable object must generate its state without separately supplied
integer instances and preserve distinct prime data on its own closed packets.

## Evidence index

- [Scope card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source boundary](evidence/README.md)
