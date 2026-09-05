# Recovery state — candidate batch after P196

Checkpoint: 2026-09-05 UTC, three individually complete papers, P202 Round1.
Status: **THREE_INDIVIDUALLY_COMPLETE / P202_REVIEW_B / ONE_SEAT_OPEN / HOLD_EXTERNAL**.
This file is a recovery index. FIVE_SEAT_FREEZE.md allocates the numbers and
links the historically accepted evidence; it is not current five-seat
acceptance or completion. Later P198_REOPEN_ADJUDICATION.md and
P201_REOPEN_ADJUDICATION.md control the two withdrawals.

## Evidence-backed stage state

| Stage | Status | Evidence |
|---|---|---|
| Problem anchor and standing authorization | present | root files in this batch |
| Breadth and internal collision search | in progress | five lane breadth ledgers, four hostile-gate reports |
| Five selected contracts / central freeze | REOPENED | historical freeze retained; P198/P201 later rejected |
| Paper drafting / Round 0 | six numbered drafts frozen | five historical drafts plus four-page replacement P202; P198/P201 rejected |
| Paper Review A / Round 1 | four accepted, two rejected | P197/P199/P200/P202 A accepted/replayed/Round1; P198/P201 admission kills |
| Paper Review B / Round 2 | three Round2 frozen | P197/P199/P200 B accepted, root-replayed, no-change deltas |
| Paper cold builds / visual QA / terminal manifests | three individual PASS | RETAINED_FINAL_QA_REPORT.md; six physical cold builds, all12 final-page views, complete manifests and two actual full subset audits; NOT full batch |

Before this recovery file was added, the batch contained 50 non-cache files,
all absent from the Git mirror. Their SHA-256 inventory is frozen in
`../research_state/ARTIFACT_SNAPSHOT_2026-09-05.json`. Any history/WIP commit
backs up unfinished research; it is not a five-paper completion commit.

## Candidate state

| Candidate | Package under scouting/ | Recorded verifier count | Gate state |
|---|---|---:|---|
| TCSD | word_poset_lane | 3,238,990 | SELECT in both stage1_hostile_gate_algebra.md and stage1_hostile_gate_graph.md |
| CMM | graph_matching_lane | 2,508,857 | historical SELECT superseded by P198 manuscript contribution kill |
| LZK | replacement_lane | 1,526,365 | KILL_COMPONENTWISE_P100_HF1_ERASURE; reviews/lzk_stage1_20260905/GATE_REPORT.md |
| FOSP | replacement_stirling_lane | 71,614,800 | SELECT_INTERNAL_AMBER; accepted source delta in reviews/fosp_stage1_20260905/DELTA_ACCEPTANCE.md; root author replay pair saved |
| LFAS | lfas_reentry_20260905 | 1,076,738 | SELECT_INTERNAL_AMBER; reviews/lfas_stage1_20260905/GATE_REPORT.md; not a new breadth row |
| EPF | fifth_fresh_20260905/period_feedback_reentry | 3,366,093 | historical SELECT superseded by exact old OCL conjugacy; not a new system |

Counts belong to the named verifier packages, some of which also test control
systems. They are not counts of proved theorems, validated subclasses, or
independent reviews. The history audit read their transcripts; it did not
rerun all four verifiers. TCSD/LZK transcripts embed replay metadata; compare
recorded stdout hashes with stdout, not blindly with the wrapper file hash.
FOSP's formerly missing durable author replay receipt is now
scouting/replacement_stirling_lane/AUTHOR_REPLAY_RECEIPT_20260905.md:
two fresh exact full-scope runs, stdout hash unchanged. This supersedes only
the recovery task, not the preserved historical transcript.

Candidate claims to re-read before drafting:

- TCSD: `D(x)_i=sgn(x_(i+1)-x_i)`, core `D^4 x=rho^2 x`, parity-sharp attraction, trace counts and Lucas fibre maximum. Its P164 equality shadow must remain disclosed.
- CMM: least-monomer alternating-arc update on odd-cycle matchings, deficiency clock, one recurrent cycle, triangular target fibres.
- LZK: preserved but ineligible. All claimed dynamics and inverse laws transfer from P100 erasure plus isolated two-cycles; HF1 already contains the Boolean inverse atlas. Independent gate: 459,463 assertions per run, two matching runs, no mathematical defect but fatal contribution collapse.
- FOSP: delete the pair of 1s, decrement, reinsert nn at the former first-1 gap; largest nonleaf-label clock, ordered-star recurrence, depth CDF and root-child inverse fibres. Exact factorization T=c∘J_1 identifies Brualdi–Dahl's left-join as the local owner. Read the new STAGE1_SOURCE_SUPPLEMENT.md before using any older firewall language. Independent gate: 1,496,779 assertions per run on n=0,…,7.
- TCSD supplement: scouting/word_poset_lane/TCSD_EXACT_GAP_PROOF.md replaces implicit fibre gap-merging with an explicit Fibonacci product; paper review remains pending.

## Binding exclusions and reserves

| Candidate | Disposition / reason | File |
|---|---|---|
| CSL | KILL_EXACT_TCSD_FACTOR: `C=rho^{-1}D^2`, so its dynamics transfers from TCSD | reviews/stage1_hostile_gate_csl_graph.md |
| LSPO | KILL_EXACT_INTERNAL_HISTORY | reviews/stage1_hostile_gate_lspo.md |
| GBE | KILL_CANONICAL_BELLMAN_CLOSURE | reviews/stage1_hostile_gate_algebra.md |
| SCT | KILL_LITERAL_REPEAT_RC13_CPT; this exact-history reason is stronger than the other gate's P188 resemblance | reviews/stage1_hostile_gate_algebra.md |
| LZK | KILL_COMPONENTWISE_P100_HF1_ERASURE; all-time inverse atlas also occupied | reviews/lzk_stage1_20260905/GATE_REPORT.md |
| CPD / CSPD | KILL_OWNER_TRANSFER / thin parking marginal; complete circular fibres transport to an already studied site-normalization class | reviews/cpd_cspd_owner_gate_20260905/OWNER_TRANSFER_GATE.md |
| SDD | RESERVE_BOUNDED_CONTRACT: affine-stratum dynamics plus full-carrier fixed locus only | reviews/stage1_hostile_gate_graph.md |
| LFAS | SELECT on re-entry: all-size recurrent criterion and row-tail bound, sharp when s>=r+1; complete inverse and max-fibre equality accepted; narrow/square sharp conjecture excluded | reviews/lfas_stage1_20260905/GATE_REPORT.md |
| Replacement algebra lane | no promotion; incomplete/broken control script | scouting/replacement_algebra_lane/verify_replacement_algebra_lane.py |

The read-only history auditor ran the last script with bytecode disabled. It
failed in `one_runs()` at `i=0` with `ValueError: negative shift count`. There
is no contract/canonical/ledger for that lane. The script is preserved as WIP,
not repaired during history consolidation, and cannot fill the fifth slot.

## Current numbered manuscript handoff

| Paper | Directory under papers/ | Latest milestone |
|---|---|---|
| P197 TCSD | 197-ternary-cyclic-sign-difference | Round2 frozen:4pages; A4,814,623/B4,833,354; root replay and accepted no-change deltas |
| P198 CMM | 198-cyclic-monomer-matching | 4page Round0 preserved; Review A Critical1 contribution kill, seat reopened |
| P199 FOSP | 199-first-one-stirling-splice | 4page Round2 frozen; A1,926,465/B1,026,386; accepted no-change deltas |
| P200 LFAS | 200-lex-first-alternating-switch | 4page Round2 frozen; A3,823,696/B4,026,047; accepted no-change deltas |
| P201 EPF | 201-eventual-period-feedback | 5page Round0 preserved; exact old OCL conjugacy kills fresh-system admission |
| P202 OR | 202-ternary-ordered-reset | four-page Round1; A12,775,204 root-replayed and accepted unchanged; root B in progress |

P197 source/PDF/verifier pins are in ROUND0_RECEIPT.md and frozen_round0/.
The author fixed an overbroad small-size witness statement before freeze:
use0^(n-1)1 at n2,3, not every a^(n-1)b. The maximum-tail theorem is
unchanged; a transparent candidate erratum preserves the old record.

## Next actions

1. Find the remaining genuinely separated replacement candidate. MCT has
   author proof work and an independent Stage1 gate in progress, not admission.
   P202 OR has completed paper A and entered root paper B. Do not rescue P198
   via restricted-erasure variants or P201 via relabelled old feedback maps.
   Stage1 proof/source/mechanism gates are required before fresh numbering.
2. Complete P202 B/delta/Round2 and any newly admitted fifth manuscript's
   two actual rounds; preserve process separation, including LFAS proof
   authorship. Do not manufacture accepted rounds for the two rejected drafts.
3. Run two physical source-only cold builds per paper, all-page visual QA,
   exact author/A/B replays and complete manifests before terminal PASS.
4. Keep scoped Git checkpoints while preserving HOLD_EXTERNAL and the
   latest scientifically completed round P192–P196 until all five close.

STAGE1_BREADTH_INDEX.tsv and BREADTH_RECONCILIATION.md now give57 documented
current attempts:4selected,3reserve,50killed;17historical controls and
8code-only WIP are excluded (82 total records). SECOND_REPLACEMENT_ROOT_ADJUDICATION.md
records fresh root replays and the LGB kill/ND1 reserve/D2G+CCW kills.
Both51 snapshots, corrected50 and first-replacement54 are retained. Active
MCT remains separate until documented and independently adjudicated.

The latest pushed research backup is62bc2108, synchronized by merge97d04aec
with disjoint remote henon_dynamics changes (ahead/behind0/0 verified).
This preserves both histories without force-push. The three final paper
packages, P202 Round1/A and closed new scouts await the next checkpoint;
P202 B and MCT are live WIP. The previous completed research commit remains
`76146ba17eb15beccfc38e625427f8da726db919`. A later history checkpoint changes
the backup state, not this research-completion milestone.
