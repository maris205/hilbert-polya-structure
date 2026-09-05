# Recovery state — candidate batch after P196

Checkpoint: 2026-09-05 UTC, history consolidation after a model switch.
Status: **STAGE1_IN_PROGRESS / FOUR_CANDIDATE_PACKAGES / FIFTH_SLOT_OPEN / HOLD_EXTERNAL**.
This file records work already on disk; it does not allocate paper numbers or approve theorem contracts.

## Evidence-backed stage state

| Stage | Status | Evidence |
|---|---|---|
| Problem anchor and standing authorization | present | root files in this batch |
| Breadth and internal collision search | in progress | five lane breadth ledgers, four hostile-gate reports |
| Five selected contracts / central freeze | absent | TCSD and CMM selected; LZK/FOSP gates pending; fifth open |
| Paper drafting / Round 0 | not started | no main.tex, bibliography, or PDF in the baseline snapshot |
| Paper Review A / Round 1 | not started | Stage-1 gates are not paper reviews |
| Paper Review B / Round 2 | not started | no paper review/delta packages |
| Paper cold builds / visual QA / terminal manifests | not started | cannot precede manuscript/review freeze |

Before this recovery file was added, the batch contained 50 non-cache files,
all absent from the Git mirror. Their SHA-256 inventory is frozen in
`../research_state/ARTIFACT_SNAPSHOT_2026-09-05.json`. Any history/WIP commit
backs up unfinished research; it is not a five-paper completion commit.

## Candidate state

| Candidate | Package under scouting/ | Recorded verifier count | Gate state |
|---|---|---:|---|
| TCSD | word_poset_lane | 3,238,990 | SELECT in both stage1_hostile_gate_algebra.md and stage1_hostile_gate_graph.md |
| CMM | graph_matching_lane | 2,508,857 | SELECT in stage1_hostile_gate_algebra.md |
| LZK | replacement_lane | 1,526,365 | theorem spike only; no independent Stage-1 gate located |
| FOSP | replacement_stirling_lane | 71,614,800 | theorem spike only; no independent Stage-1 gate located |

Counts belong to the named verifier packages, some of which also test control
systems. They are not counts of proved theorems, validated subclasses, or
independent reviews. The history audit read their transcripts; it did not
rerun all four verifiers. TCSD/LZK transcripts embed replay metadata; compare
recorded stdout hashes with stdout, not blindly with the wrapper file hash.
FOSP's two replays were reported in the earlier conversation but no separate
replay receipt is on disk; rerun and save a receipt before manuscript freeze.

Candidate claims to re-read before drafting:

- TCSD: `D(x)_i=sgn(x_(i+1)-x_i)`, core `D^4 x=rho^2 x`, parity-sharp attraction, trace counts and Lucas fibre maximum. Its P164 equality shadow must remain disclosed.
- CMM: least-monomer alternating-arc update on odd-cycle matchings, deficiency clock, one recurrent cycle, triangular target fibres.
- LZK: least-zero Kempe component switch on proper complete-bipartite colourings, support-side classification, depth census and all-time fibres; keep the separate q=2 boundary.
- FOSP: delete the pair of 1s, decrement, reinsert nn at the former first-1 gap; largest nonleaf-label clock, ordered-star recurrence, depth CDF and root-child inverse fibres.

## Binding exclusions and reserves

| Candidate | Disposition / reason | File |
|---|---|---|
| CSL | KILL_EXACT_TCSD_FACTOR: `C=rho^{-1}D^2`, so its dynamics transfers from TCSD | reviews/stage1_hostile_gate_csl_graph.md |
| LSPO | KILL_EXACT_INTERNAL_HISTORY | reviews/stage1_hostile_gate_lspo.md |
| GBE | KILL_CANONICAL_BELLMAN_CLOSURE | reviews/stage1_hostile_gate_algebra.md |
| SCT | KILL_LITERAL_REPEAT_RC13_CPT; this exact-history reason is stronger than the other gate's P188 resemblance | reviews/stage1_hostile_gate_algebra.md |
| SDD | RESERVE_BOUNDED_CONTRACT: affine-stratum dynamics plus full-carrier fixed locus only | reviews/stage1_hostile_gate_graph.md |
| LFAS | reserve: sharp all-size temporal/inverse contract not closed | scouting/replacement_lane/LFAS_RESERVE_CONTRACT.md |
| Replacement algebra lane | no promotion; incomplete/broken control script | scouting/replacement_algebra_lane/verify_replacement_algebra_lane.py |

The read-only history auditor ran the last script with bytecode disabled. It
failed in `one_runs()` at `i=0` with `ValueError: negative shift count`. There
is no contract/canonical/ledger for that lane. The script is preserved as WIP,
not repaired during history consolidation, and cannot fill the fifth slot.

## Next actions

1. Independently gate LZK and FOSP against available on-disk P1--P196 papers
   and kill ledgers, explicitly noting the missing historical interval.
   Document bounded source/owner searches for all four candidates with actual
   primary-source links; TCSD/CMM/LZK especially lack URL-based disk records.
2. Find a fifth separated literal system. SDD/LFAS are not automatic fallback
   promotions. Archived failed worker turns do not count as delivered work.
3. Consolidate a deduplicated current-batch breadth denominator. Do not add
   lane row counts blindly; prior systems and repeated controls are excluded.
4. Freeze exactly five eligible contracts, then assign P197–P201.
5. Follow the existing two-review protocol through papers, QA and Git.

The previous completed research commit remains
`76146ba17eb15beccfc38e625427f8da726db919`. A later history checkpoint changes
the backup state, not this research-completion milestone.
