# Second combinatorial intake — closed, zero admissions

2026-09-05 UTC. Author and scoped owner: `batch197_fosp_gate`.
Status: `BOUNDED_INTAKE_CLOSED / NO_ADMISSION / HOLD_EXTERNAL`.
Six literal finite autonomous maps, 75 prebounded boxes, 214,988 enumerated
states in total. No bound was enlarged to rescue a weak candidate. No
paper number, reserve, external novelty certificate or manuscript review
is created by this package.

| Key | Literal map and carrier | Complete pilot bound | Disposition |
|---|---|---|---|
| PR | All functions [n]→[n]; each vertex selects its least old predecessor, keeping its old image if none | n=1,…,6 | Kill: edge descent does not close temporal/inverse theorem |
| ZR | Rooted cyclic binary words; synchronous disjoint 001→110, identity for n<3 | n=1,…,14 | No admission: exact inverse retained, stronger time formula open; carry primitive deducted |
| BS | Partitions of n; balanced split each part, sort, conjugate | n=1,…,30 | Kill: 2-modular conjugation after one normalization |
| BA | Cyclic words over {−1,0,1}; velocities ±1 annihilate on crossing or same-site landing | n=1,…,9 | Kill: classic ballistic mechanism and no separate inverse atlas |
| AZ | All subsets of Z/n; A↦(Z/n)\(A−A) | n=1,…,12 | Kill: symmetric complete sum-free fixed sets do not close dynamics |
| MA | All L⊆{0,1}^n; reverse the absent words whose prefix/suffix are endpoints of L | n=1,…,4 | Kill: both axes transfer to generic induced-edge closure |

The first four were precommitted and implemented together in
[pilot_initial.py](pilot_initial.py); AZ and MA were added only after root
confirmed no overlap with its active lane and were separately prebounded in
[pilot_additional.py](pilot_additional.py). The additional script imports
the same-lane functional-graph analyzer from the initial script.

## Terminal-box observations, not all-parameter proofs

| Key | Size | States | First image | Recurrent | Height | Largest fibre | Cycle counts |
|---|---:|---:|---:|---:|---:|---:|---|
| PR | 6 | 46,656 | 8,924 | 4,949 | 6 | 128 | 1:1539, 2:1705 |
| ZR | 14 | 16,384 | 5,072 | 844 | 7 | 16 | 1:844 |
| BS | 30 | 5,604 | 1,016 | 1,016 | 1 | 41 | 1:12, 2:502 |
| BA | 9 | 19,683 | 2,787 | 1,023 | 4 | 241 | See full canonical for all divisors |
| AZ | 12 | 4,096 | 32 | 4 | 4 | 3,002 | 1:2, 2:1 |
| MA | 4 | 65,536 | 36,585 | 25,759 | 8 | 202 | 1:3, 2:12878 |

Every intermediate box, full cycle census and deterministic height witness
appears in [initial full stdout](INITIAL_CANONICAL.jsonl) or
[additional full stdout](ADDITIONAL_CANONICAL.jsonl). No truncated terminal
excerpt serves as canonical evidence.

## Theorem-level progress retained without promotion

[Proof notes](PROOF_NOTES.md) give complete deductions for PR's edge-set
descent; ZR's termination, fixed count, target hitting-set inverse and sharp
maximum fibre; BS's T²=C and exact core inverse; BA's sharp half-ring clock
and recurrent classification; AZ's precise fixed-set equivalence; and MA's
generic two-step erosion and support-sum inverse. In particular, ZR's
observed floor(n/2) height and PR/AZ's observed 1/2-period census are **not**
promoted to universal theorems.

[Source and collision notes](SOURCE_AND_COLLISION_NOTES.md) separate literal
reductions from nearby-but-different internal systems and record exactly
which primary-source passages were read. The four source/mechanism failures
and two unclosed candidates do not become reserve seats.

[verify_controls.py](verify_controls.py) contributes 655,223 actual passing
checks within the original bounds. It imports the author's literal maps;
it is an author-level pressure test, not an independent candidate gate.
The full [control canonical](CONTROLS_CANONICAL.json),
[actual replay log](REPLAY_LOG.md), runtime/input pins and complete nonself
manifest close the local evidence. Root remains responsible for central
indices and any private Git synchronization. This agent may not later act
as an independent reviewer of these six proof fragments.
