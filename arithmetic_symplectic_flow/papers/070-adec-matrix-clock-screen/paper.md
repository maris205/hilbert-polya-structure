# ADEC's cyclic local matrices do not make its prime-generating global clock recurrent

**Paper ID:** `070-adec-matrix-clock-screen`  
**Record ID:** `ASFS-SCOUT-20260914-47`  
**Date / status:** `2026-09-14; PRE-P0 STOP`  
**Route state:** `No ASFS Route-A coordinate; Route B NOT INVOKED`.

## Source claim and admissible reading

The ADEC preprint describes a list of single-column matrices whose local entries update cyclically as a function of an incremental counter `C`. It claims that a new matrix is self-generated only when its dimension is prime and interprets a negative-synchronization rule as an Eratosthenes-like filter.

This is worth screening because it tries to make arithmetic selection and local cyclic motion coexist. The present record does **not** accept the preprint's claimed prime theorem as a new proof. It uses only the explicit structural description needed for the recurrence audit: `C` increases, and the module list is extended at selected values of `C`.

## Global-state obstruction

Let a faithful state include the current counter `C` and the current list of matrices, since otherwise it cannot say which prospective dimension is being tested or which prime-dimensional modules have already been generated. Each global update advances `C` to a larger value. If a module is appended, the list length also increases; if no module is appended, `C` still advances.

Thus a periodic global state after `q>0` updates would require both `C+q=C` and return of the same growth history, impossible. This is the strict-frontier obstruction of 018 applied directly to the source's own counter. A cyclic phase internal to one already-existing matrix does not repair the failure: it is not the all-system state that owns the asserted prime-generation mechanism.

## Ownership and lineage audit

The source has a possible first-arrow connection only in its stated sieve analogy. It supplies no exact coding from the prior Eratosthenes word or S-adic mechanism, no Logistic-to-Hénon conservative deformation, and no symplectic realization. It also provides no primitive closed-orbit convention for all matrix-list states, roof, mapping torus, operator, or determinant. Importing one of those owners would violate the one-object invariant.

| Gate | Evidence | Status |
| --- | --- | --- |
| source-side A0 | unreviewed self-generation claim; no independent theorem adopted | NOT TESTABLE / not promoted |
| A1 for global arithmetic path | incremental counter cannot return | scoped FAIL |
| P0 geometry | absent | not admitted |
| A2 | no same-object analytic owner | NOT EVALUATED |
| Route B | no Route-A-ready object | NOT INVOKED |

**Decision: `stop/fork`.** A future reopening requires a fixed, independently checkable update law that eliminates the strictly increasing global counter while retaining a prime-symbolic mechanism and gives a complete recurrent state space. The local word “cyclic” is insufficient.

## Evidence index

- Gianluca Remigio Pisano, [*ADEC (Autopoietic Dynamic Entropic Clock): Emergent Behavior of Prime Numbers in Dynamic Matrix Systems*](https://www.researchgate.net/publication/397072453_ADEC_Autopoietic_Dynamic_Entropic_Clock_Emergent_Behavior_of_Prime_Numbers_in_Dynamic_Matrix_Systems)
- [018 monotone sieve-clock obstruction](../018-monotone-sieve-clock-obstruction/paper.md)
- [053 real-time sieve CA control](../053-realtime-sieve-ca-nonrecurrence/paper.md)
