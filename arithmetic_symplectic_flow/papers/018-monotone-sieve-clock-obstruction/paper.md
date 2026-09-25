# Strict sieve progression is incompatible with same-carrier closed orbits

**Paper ID:** `018-monotone-sieve-clock-obstruction`  
**Record ID:** `ASFS-SCOUT-20260913-15`  
**Date / status:** `2026-09-13; METHODOLOGICAL THEOREM / PRE-P0 STOP RULE`  
**Route state:** `No frozen candidate; Route A coordinates not evaluated; Route B NOT INVOKED`

## Statement and proof

Let `F:X -> X` and let `L:X -> Z` satisfy `L(F(x)) > L(x)` for every `x` in an
`F`-invariant proposed arithmetic source `Y`. Then `F` has no periodic point
in `Y`: if `F^n(x)=x`, repeated strict inequality gives
`L(F^n(x)) > ... > L(x)`, a contradiction.

## Consequence for the programme lineage

The prior-work route treats sieve-stage growth and parameter drift as genuine
chronological evolution. If an autonomous lift preserves an exact frontier—such
as stage number, largest admitted prime, or sieve horizon—then the source
carrying that prime mechanism cannot itself furnish the A1 orbit ledger. Record
010 realizes this as `q -> q+1`; record 014 realizes the same nonreturning
mechanism on a profinite clock.

This does not prohibit all arithmetic dynamics. A viable candidate must derive
its arithmetic information from a recurrent global state rather than a
chronological frontier, or give a justified return that is not a finite,
externally selected wheel. Forgetting the frontier in a quotient changes the
arithmetic owner and does not retain its prime claim automatically.

## Stop rule

Before freezing a sequential-to-autonomous lift, ask whether its claimed prime
mechanism requires an integer-valued strict frontier on the same periodic
carrier. If yes, stop before A1 orbit computation. If no, the P0 card must say
which recurrent arithmetic state replaced it and how the prime-symbolic lineage
survives.

## Evidence index

- [Scope card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Sequential Hénon control](../010-sequential-henon-cotangent-lift/paper.md)
- [Profinite-clock screen](../014-profinite-sieve-clock-screen/paper.md)
