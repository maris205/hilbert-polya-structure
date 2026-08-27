# C190 hostile audit

This is an internal artifact-bound audit, not external peer review and not an
independent error process.

The suite recomputes the canonical payload hash after each semantic attack.
It rejects 118 repaired-hash mutations covering identity, date, source commit,
scope, evaluator provenance, every source-lock and attribution field, all nine
theorem statements, all six stopping boundaries, finite totals, every layer
of the N=1 evidence row, the complete Route-A tuple and qualifications, all
scope flags, both source records, and every nonclaim.  One additional
stale-hash mutation is rejected before semantic validation.

High-risk rejected attacks include:

- claiming the package owns Brandt's recurrent theorem;
- changing right rotation or the binary-word layer;
- using `T^0` rather than a positive multiple of `k` for residue zero;
- treating finite census as the all-`N` proof;
- removing the transient zero eigenvalue;
- claiming nilpotent Jordan sizes or a global reversor;
- treating `k` phase-labelled reflection formulas as a target operator;
- promoting A0, A2, A3, or A4 beyond the frozen tuple;
- enabling Route B or any forbidden target-data flag.

The direct checker is algorithmically independent of the producer and uses
the full partition phase space.  SymPy supplies a third exact symbolic path.
These layers strengthen implementation confidence without becoming a new
proof, novelty certificate, or external review of the classical theorem.
