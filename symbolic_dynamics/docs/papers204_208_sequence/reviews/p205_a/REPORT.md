# P205 manuscript Review A — frozen Round0

2026-09-05 UTC. Reviewer process: `/root/batch197_fosp_gate`.
Initial verdict: **MATH_VALID / PASS_NARROW_INTERNAL_REVIEW / DELTA_PENDING**.
Current findings: **Critical 0 / Major 0 / Minor 0 / Open 0**.
The manuscript survives unchanged on the evidence inspected in this round.
`OWNER_AMBER / HOLD_EXTERNAL` remains; this is not a venue recommendation,
global priority certification, completed A acceptance, Review B or paper completion.

## Input and independence

The input is the complete physical
[P205 frozen Round0](../../../../papers/205-conflict-triggered-cyclic-increments/frozen_round0/README.md),
including its [three-page PDF](../../../../papers/205-conflict-triggered-cyclic-increments/frozen_round0/main.pdf).
[INPUT_PINS.sha256](INPUT_PINS.sha256) pins all 22 frozen nonself files and
the freeze's own manifest: **23 workspace-root-relative entries**. Their
hashes were actually checked. No original manuscript, frozen file, central
index or Git state was changed by this review.

The proof author is `/root/batch197_fifth_scout`; root is manuscript
author/integrator. This reviewer is neither. The reviewer previously
performed the CCI candidate gate and bibliography/locator QA, without
supplying a missing mathematical lemma, proof repair or manuscript text.
That familiarity is disclosed: this review is process-separated but neither
blind nor external. The current review reread the entire frozen modular
manuscript, complete proof package and documentary claim/source/lifecycle
records; it did not substitute the earlier candidate verdict for manuscript
review. The frozen author implementation, canonical and author run data
were pinned as bytes but deliberately not opened or imported to construct
the independent checker. The author-run count is not relabelled as an
independently rerun author result here; root's author replay obligation is
separate from this new reviewer execution.

The project skill/workflow and this batch's artifact contract control the
review roles. The research-review external MCP endpoint is unavailable;
the authorized current-model internal process-separated fallback was used.
No external thread ID, model call, specialist opinion or model override is
invented. Proof-writer's dependency/assumption checks were used for auditing
the existing proofs, not for authoring a repair. Paper-compile's checks were
applied to a source-only build in this review directory. All four current
agent slots were occupied, so no additional subreview was delegated.

## Claim-by-claim attack and result

| Frozen claim | Attempted failure / check | Result |
|---|---|---|
| C1: permanent conflicts and one-way activation | Old-state synchrony; persistence of each edge rather than just nondecreasing active-set size | Correct. Equal endpoints advance together forever. |
| C2–C3: first-conflict distances and every coordinate | Reverse the oriented residue; confuse first conflict with first increment; competing seeds; zero-weight edges; positive-time spontaneous activation | Both distance inequalities are present and valid. Backward first-event tracing strictly decreases time and reaches a seed. The formula uses `max(0,t-d)`, with no missing unit shift. |
| C4: exact entrance, full core, period | Confuse an upper bound with exact entrance; omit unseeded/disconnected components; allow a shorter nonfixed period | The future strict increase of a monotone active set excludes earlier recurrence. Each component is proper/fixed or fully active/rotating; a single advancing coordinate forces exact period `q`. |
| C5: sharp height for every parameter | Count a seed-to-nonseed path as `n-1` edges; exploit zero cycles or wraparound in the path witness; miss `n≤2` | A shortest route can omit other seeds, leaving at most `n-2` edges. The path witness has exactly the claimed waits. Empty graphs and small orders are handled. |
| C6: exact one-step inverse | Reverse the closure direction; admit held monochromatic edges; permit an advancing vertex with no trigger; prove necessity without sufficiency | All three edge constraints are required and jointly sufficient. The proof reconstructs exactly the advancing set, not merely a superset; mask-to-source injection is valid. |
| C7: static support | Use an induced path when only a subgraph is assured; miscount the six connected four-vertex graphs; lose disconnected equality cases | The path need only be a subgraph. Its extension bound is strict for `k≥5`; the six four-vertex counts and component products are correct. No standalone static originality credit is granted. |
| C8: dynamic maximum and every maximizer | Allow extra nonmonochromatic graph edges at equality; miss the triangle exception or empty state | A spanning monochromatic star/triangle forces the target constant and therefore `H_y=G`. This gives all graph/target maximizers. Small-order maps are permutations. |
| S1–S3: citation and ownership boundary | Treat the conflict-bit model or cover object as new; borrow randomized convergence; upgrade bounded source checking into priority | The four citation contexts match the inspected primary material and explicit deductions. The draft makes none of those upgrades. |
| Presentation/evidence scope | Truncate a proof at the page break; omit a reference; confuse finite checks with all-parameter proof | All three pages were actually viewed. The proofs and all four references are complete. Section 4 identifies finite checks as pressure, not proof. |

The full deduction and source-read limits are in
[SOURCE_AND_PROOF.md](SOURCE_AND_PROOF.md). The review supplies no new
mathematical premise: these are checks of arguments already in the frozen
paper, including its existing finite four-vertex boundary calculation.

## Is the two-axis contribution still defensible?

Yes, under the already narrow internal short-theorem standard. The existing
model and general methods receive zero credit. What remains in the complete
draft is the literal rule's exact source-colour arrival geometry and sharp
entrance, together with a target-colour held/advancing constraint geometry
and the dynamical maximum with all equality pairs. The inverse argument does
not use the activation-distance formula. Conversely, knowing shortest
arrival times does not characterize the target's admissible predecessor
sets. No complete classical adapter eliminating one of these statements
was established in the inspected primary/internal originals.

This is a modest conjunction, not a claim that either shortest paths or
binary reconstruction is a new method. The static graph extremum is
elementary supporting material with no separate priority credit. The note
may be too elementary for a demanding external venue. An exact earlier
owner or a complete adapter would reopen this assessment; a source-search
non-hit alone was not used as the positive justification for PASS.

## New verification and actual build/view evidence

The new [verify.py](verify.py) was written from scratch for this manuscript
round. It uses an event priority queue rather than the author's described
Floyd representation, full-functional-graph leaf removal for entrance and
period, and held independent sets with successor closure for inverse sets.
It reads no files and imports only Python's standard library; neither old
candidate code nor data is reused.

The initial producer passed **11,265,033 assertions**. Two additional fresh
producer processes both exited zero, and each complete stdout was compared
by raw-byte `cmp` with the new [CANONICAL.json](CANONICAL.json), both exit
zero. They cover **315,093 complete dynamical states/targets**, **2,880,650
literal orbit times**, **33,868 static graphs**, and **319 sharp paths**.
All graph boxes, histograms, equality counts, negative controls and the
record digest are in the complete canonical. These finite boxes pressure
the all-parameter proofs; they do not replace them. Exact commands and
hashes are in [REPLAY_LOG.md](REPLAY_LOG.md).

One actual source-only build from frozen inputs completed with exit zero.
Its three-page PDF is raw-byte identical to frozen Round0. All three page
images were actually opened and checked; none had clipping, missing text,
overlap or unresolved citations. Final diagnostics were empty and all
fonts embedded. Full logs, source/environment/engine records and viewing
details are in [BUILD_REPORT.md](BUILD_REPORT.md).

## Findings and required next action

[FINDINGS.json](FINDINGS.json) is a real empty finding census after the
attacks and executions above, not a prefilled acceptance template. There
are no requested mathematical, citation or layout changes. There are no
unresolved mathematical/evidence findings to hide in a no-change label.

**No DELTA.md has been created at this stage.** Root must first inspect this
initial report and propose the exact no-change or repaired delta. Only
after that response will the reviewer check the relevant before/after
bytes and accept or reject it. The review directory's nonself manifest
covers the artifacts that actually exist now; missing acceptance is
explicitly `DELTA_PENDING`, not an already completed A gate.

Frozen documentary links retain their original live-paper-relative
spellings; when reading those archived documents, their source origin was
used for external documentary references. They were not rewritten in the
immutable freeze. Link checks asserted for this package concern the newly
authored review documents, while scientific source resolution was actually
tested by the clean build. External source inspection is bounded as stated
in the source report; no exhaustive priority or machine plagiarism service
is claimed.
