# Eratosthenes gap cycles are stage data, not closed packets of the advancing sieve

**Paper ID:** `120-eratosthenes-gap-cycle-stage-owner-boundary`  
**Record ID:** `ASFS-SCOUT-20260914-87`  
**Date / status:** `2026-09-14; PRE-P0 STOP — A WHEEL-GAP CYCLE AT ONE SIEVE STAGE IS NOT A RETURN OF THE STAGE-ADVANCING SIEVE ACTION`  
**Route state:** `No formal ASFS Route-A coordinate; Route B NOT INVOKED`

## Frozen construction and direct lineage

The source treats the Eratosthenes sieve as a discrete dynamical system whose objects at stage \(p_k\) are the wheel-gap cycles \(\mathcal G(p_k^\#)\). It gives a three-step recursion from the current gap cycle to \(\mathcal G(p_{k+1}^\#)\) and analyzes admissible constellations through stagewise transfer/Markov models. This is a direct realization of the project source lineage from sieve survivors to sequential symbolic gap admissibility.

The word “cycle” here names the cyclic ordering of residues/gaps around one fixed wheel of span \(p_k^\#\). It is a valid finite combinatorial feature, not automatically a time-periodic orbit of the map that advances sieve stages.

## Same-object audit

The source update replaces \(p_k^\#\) by \(p_{k+1}^\#=p_{k+1}p_k^\#\). Thus the full stage carries a different primorial span after each advance; the source also describes changing and generally growing populations of admissible instances. The stage-advancing state cannot equal its earlier state after a positive update.

Rotating a fixed \(\mathcal G(p^\#)\) around its wheel would define a distinct, fixed-stage cyclic action. It does not apply the recursion, choose the next sieve stage, or retain the full data that owns the prime-generating update. Combining that rotation with the advancing recursion would violate the one-object ledger.

| Gate | Evidence for this screen | Status |
| --- | --- | --- |
| A0 | genuine Eratosthenes sieve and sequential gap-admissibility mechanism | direct source control |
| A1 | fixed-stage cyclic datum but strictly changing stage owner | scoped owner FAIL |
| A2 | no one-object roof, transfer operator, or determinant | NOT EVALUATED |
| Route B | no Route-A readiness | NOT INVOKED |

No Logistic-type deformation, area-preserving Hénon map, symplectic base, or suspension belongs to this source object. **Portfolio position: stop and fork.** The next source must preserve direct sieve lineage while making the complete arithmetic-update state recurrent; a wheel's internal cyclic order is not enough.

## Evidence index

- [Candidate card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Source record](evidence/README.md)
- [117 Secondary Sieve Map](../117-secondary-sieving-map-generation-nonreturn/paper.md)
- [108 source-action frontier](../108-source-action-frontier-cycle-11/paper.md)
