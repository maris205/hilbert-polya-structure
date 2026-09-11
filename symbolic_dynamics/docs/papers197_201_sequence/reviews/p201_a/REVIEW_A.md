# P201 manuscript Review A — rejected new-system admission

Date: 2026-09-05 UTC. Target: the physically frozen Round-0 manuscript
`papers/201-eventual-period-feedback/round0_frozen/` and its original PDF.

**Verdict: `REJECT_ADMISSION_EXACT_HISTORICAL_CONJUGACY`.**
Mathematical audit: no defect found in the stated all-parameter package.
Open finding census: **Critical 1 / Major 0 / Minor 0**. This is not a
Review-A pass and cannot authorize Round 1 or an accepted Review B.
External disposition remains `HOLD_EXTERNAL`; no originality certificate.

## C1 — the literal operator is conjugate to an explicitly killed predecessor

Severity: Critical. Confidence: 5/5, based on the historical implementation,
an all-size algebraic proof, and exhaustive independent checks through seven
labels. This is a project-admission finding, not an appeal to an undocumented
disciplinary norm.

Evidence anchor: equation: frozen manuscript (1), compared with
`docs/papers162_166_sequence/scouting/replacement_adaptive_maps/verify_scout.py`
lines 427–438 and its `SCOUT.md` row OCL, line 81. The central
`PROBLEM_ANCHOR.md` excludes relabelled/conjugate earlier killed systems.

Write the manuscript operator as `P(f)(i)=ell_f(i)-1`. The earlier code
implements exactly `O(f)(i)=ell_f(i) mod n`, using the eventual cycle reached
from the **starting label i**, not a target label, a cycle containing i, or a
basin size. Let `sigma(i)=i+1 mod n` and
`H(f)=sigma o f o sigma^{-1}`. Relabelling the functional graph preserves
periods, so

```
ell_(H f)(i) = ell_f(sigma^{-1}(i)),
O(H f)(i)   = ell_f(sigma^{-1}(i)) mod n
            = sigma(P(f)(sigma^{-1}(i)))
            = H(P f)(i).
```

Thus `O o H = H o P` on the entire carrier, for every `n>=1`.
The two output codings are not merely similar: this explicit bijection
conjugates their complete dynamics. It preserves function rank and carries
all iterates, cycle/tail statistics, target fibres, and extremal equality
classes. The zero constant of P maps to the one constant of O when `n>=2`;
at `n=1` there is just the same zero state. The n=5 historical signature
60 / unique fixed point / tail 3 / largest fibre 1296 is consistent with,
but is not the proof of, this equivalence.

The old disposition is **`KILL_FUNCTIONAL_GRAPH_SUMMARY_THIN`**, not a
reserve. The historical ledger explicitly states that the other 25 systems
are killed and that none is a hidden reserve. New deductions about this old
map may be useful, but they do not meet this batch's requirement for a new
literal system beyond occupied, killed, and reserved predecessors. This
collision is strictly stronger than the manuscript's comparisons with P137
and P167. A citation-only patch does not remove it.

Minimum remedy under the current anchor: remove EPF from the selected five,
retain the frozen P201 manuscript and this rejected review as historical
evidence, and reopen the seat. Any separate project on revisiting killed
maps needs an explicit change of scope, not a reviewer-created exception.
The root coordinator checked the conjugacy algebra and requested this
durable rejection record. The reviewer has not edited author files or
rewritten the freeze/index on the coordinator's behalf.

## What survived skeptical mathematical checking

1. Equations (2)–(6): strict rank packing, unique zero attractor, positive-time
   core-extension equivalence, threshold ceiling, and sharpness at every
   feasible rank. The `n=1` and rank-one boundaries are explicit.
2. Theorem 4.1: the critical-size permutation criterion is necessary and
   sufficient, and the factorial factor counts each labelled extremizer
   once. This is not a classification at noncritical sizes.
3. Equations (9)–(13): the prescribed-root forest coding is bijective, target
   blocks are invariant in both directions, and unsupported targets are
   included in the fibre/image assertions.
4. Theorem 5.2: the componentwise inequality is strict where required, and
   joining prescribed blocks excludes genuine cross-block forests. Therefore
   the zero target is the unique largest fibre, including `n=1`.

Full independent deductions are in `PROOF_REDERIVATION.md`. These are actual
mathematical merits, not grounds for waiving C1. In particular the old scout
ledger did not itself contain the present all-size threshold and critical
count proofs; the review does not falsely attribute those proofs to it.

## Independent execution and build

The reviewer did not read, copy, or import the P201 author verifier or the
EPF Stage-1 verifier. Their frozen bytes are pinned as submitted artifacts,
not claimed as executed review code. The new verifier uses per-label Floyd
chases, small-box Boolean reachability, a reverse-BFS whole-graph height
calculation, and a pointed-component counting recurrence. Historical OCL is
independently reimplemented by n-step landing on a cycle. The actual old
implementation was read only to settle its literal definition/orientation.

Two fresh processes are byte-identical: **9,726,250 assertions**. They check
all 873,612 states at sizes 1 through 7; every labelled target count through
7; complete inverse source sets through 5; the exact OCL conjugacy on every
one of those states; 1,441 prescribed-root codes; 4,821 core extensions;
critical witnesses through size 26,796; and all-rank witnesses through 32.
Finite checking is bounded pressure, not a replacement for proof.

A source-only cold build was already completed before C1 was received. Its
PDF equals both frozen PDFs byte for byte, and all five pages were actually
viewed. The detailed build/visual record is `BUILD_PDF_QA.md`.

## Process and scope disclosure

This is one separately invoked reviewer process using the same configured
model family as the author pipeline, not an external human referee or a
cross-model panel. The reviewer authored P199/P200 but did not author P201
or its Stage-1 proof/gate. No manuscript was uploaded to an external model.
Calibration: `NOT_CALIBRATED`; venue criteria binding unavailable. The
project's supplied hostile-review contract governs this single seat; no
five-person ARS panel is simulated. The research-review, proof-writer,
paper-compile and phase-scoped ARS domain-review disciplines informed the
audit, especially separating validity from admission and keeping Critical
evidence visible. Public-source verification is bounded as documented in
`SOURCE_OWNER_AUDIT.md`; the P51–P56 missing-manuscript caveat is preserved.
