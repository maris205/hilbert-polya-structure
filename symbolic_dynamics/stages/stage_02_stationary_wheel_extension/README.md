# Stage 02 — Wheel-Sieve Stationarization Audit

Status: **THEOREM SCREENING COMPLETE; RECODING SOURCE LOCK PENDING**

Primary family: **Symbolic Dynamics only**

Candidate ID: **not assigned**

Route B: **locked**

## Question

Can a fixed, level-blind symbolic deformation of Stage-01 `SD-C05` preserve
its endogenous consecutive-prime recursion and exact clock

\[
\tau_k=\log(Q_{k+1}/Q_k)=\log q_{k+1},
\]

while producing intrinsic primitive periodic orbits?

## Theorem screening

Three tempting constructions are already excluded or sharply delimited.

1. A strict extension cannot help.  If
   \(\pi\circ S=\sigma\circ\pi\), an \(S\)-periodic point would project to a
   periodic point of the acyclic wheel shift.  The standard inverse-limit
   natural extension is empty.
2. A strong forward-bisimulation quotient of any **finite** wheel DAG remains
   acyclic.  Finite cutoff experiments therefore cannot have a positive
   cycle GO branch in this quotient class.
3. If the exact next multiplier \(q_{k+1}\) is a state-class label, its
   distinct value at every level prevents cross-level merging.  Moreover, a
   finite alphabet with a fixed finite-window decoder cannot recover the
   unbounded exact prime clock.

The proofs and their scope boundaries are in:

- [strict-extension obstruction](G0_STRICT_EXTENSION_OBSTRUCTION.md);
- [bisimulation and clock obstructions](G0B_BISIMULATION_AND_CLOCK_OBSTRUCTIONS.md).

## Live branch

The next admissible object would be a genuinely new **factor or observational
recoding**, not a strict extension and not a full-label strong bisimulation.
It must be defined on the infinite wheel path system before finite cutoffs are
used.  In particular, it must freeze:

- the category and shift-commuting map;
- a level-blind rule, alphabet, coding radius or memory class, and boundary
  convention;
- vertex and edge labels, parallel-edge multiplicity, and the quotient or
  recoded phase space;
- an exact clock decoder and arithmetic decoder;
- a path-lifting rule that distinguishes genuine periodic words from cycles
  manufactured by incompatible representatives.

The incomplete source-lock form is
[here](OBSERVATIONAL_RECODING_SOURCE_LOCK.md).  No implementation run is
authorized until every required field is frozen.  Even after a finite-cutoff
periodic witness, `SD-C07` is withheld until an infinite object and its A0/A1
ledger are defined.

## Plan and scope

- [Stage-02 gate document](STAGE2_PREREGISTRATION.md)
- [Claim-driven experiment plan](refine-logs/EXPERIMENT_PLAN.md)
- [Execution tracker](refine-logs/EXPERIMENT_TRACKER.md)
- [Stage-01 dependency](../stage_01_scope_screening/wheel_sieve_level_shift/README.md)

No Stage-02 numerical experiment has been run and no determinant is defined.
The existing cross-family clue `RC-03` remains only in the
[Stage-01 ROUND2 ledger](../stage_01_scope_screening/ROUND2_CLUES.md); it is not
developed here.

The stage files are frozen by
[`STAGE_MANIFEST.sha256`](STAGE_MANIFEST.sha256), verified from this directory.
