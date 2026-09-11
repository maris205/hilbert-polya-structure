# P209 A — deductive and source review

Reviewer `/root/p209_a_reviewer`, 2026-09-07 UTC. This is the actual
nonauthor Round0 manuscript read, not a candidate gate, author recap, broad
literature census, or numerical proof. All locators below refer to the physical
`papers/209-ordered-fibre-threading/frozen_round0/` input, whose complete seal
and 1,989 payloads are in INPUT_PINS.sha256. Reading extracted text is not
represented as a visual reading of its source PDF pages.

## Deductive attacks, independent of finite checks

**Definition.** The old fibres partition the whole domain, including members
whose labels equal the destination. Thus simultaneous star replacement is a
total autonomous map. A self-loop does not create a conflicting prescription:
each coordinate belongs to exactly one old fibre. The empty function is the
sole function on the empty set. The manuscript consistently distinguishes
composition of f on vertices from iteration of T on functions.

**Theorem 1, necessity.** I attacked the use of height as a Lyapunov quantity:
height cannot simply be held fixed while f changes. The proof avoids that
error. Every old arrow is replaced by a positive-length new *walk*, including
when the destination is a member of the fibre. Concatenating replacements
and taking a suffix proves inclusion for every I_r, not just first-image
rank. Periodicity forces equality of each labelled I_r around the entire
orbit. Only then is the single epoch-independent height function available.
Infinite height is exactly a cycle vertex: an arbitrarily long backward walk
repeats, and a functional cycle has no forward exit. For a finite-height head,
extending the maximal incoming path strictly raises height. Consequently a
nonmaximal old fibre member can change its head to the next sibling without
lowering head height only when that sibling is cyclic. Periodicity forbids
strict decrease, including the self-target/numerically-unchanged case.

A fibre has at most one cycle vertex. All its members after the first must
be cyclic, hence its size is at most two; the second member, if any, is cyclic
and larger than the first. Off-cycle indegree is at most one, and a cycle
vertex has at most one extra predecessor. This produces disjoint unbranched
paths without silently assuming monotone internal path labels. Cycle arrows
are retained because their sources are fibre maxima; internal path arrows
are retained because their targets have singleton fibres. A final path
vertex then moves to the old cycle predecessor. The same deduction holds
at every recurrent epoch, so its fixed label is below every cycle label.
There is no circular appeal to the sufficiency direction.

**Theorem 1, sufficiency and exactness.** The below-cycle-minimum condition
makes every attached target's two incoming sources ordered correctly.
Simultaneous predecessor motion preserves distinct attachment targets.
Every internal/cycle arrow remains unchanged. Choosing one fixed *labelled*
final path vertex on a nonempty attached component forces its head to visit
all cycle vertices before return; graph symmetry cannot shorten the period.
An unattached component is a fixed permutation, not a cycle of T with the
vertex-cycle length. Disjoint invariant component vertex sets justify LCM;
the empty LCM and loop cases give period one. This proves recurrence, not
a sharp entrance clock. Finiteness gives eventual recurrence but does not
upgrade the theorem to an exact all-time trajectory formula.

**Theorem 2.** I separately reconstructed inverses as set partitions of the
domain. In every old fibre, consecutive increasing members must follow
target arrows, and the last member retains the old value. Conversely a
partition with these consecutive-link constraints is a source precisely
when distinct block maxima have distinct target values; otherwise blocks
merge and the proposed source is invalid. A selected-head collision cannot
be permitted because the blocks would intersect. Strictly increasing links
exclude selected cycles. These observations establish the manuscript's
two-condition path decoder independently of recurrence. Every predecessor
recovers its unique selected set as its nonmaximal fibre members. In
particular `(1,1)` selects coordinate 0 despite no numerical change. Singleton
paths, empty inverse fibres, and n=0 require no omitted exception.

**Theorem 3.** The eligible set omits the largest label. Equality in the
Boolean bound requires both n-1 eligible arrows and *every* subset admissible.
The empty subset forces g to be a permutation. Descending elimination of
the injective increasing arrows forces g(n-2)=n-1, ..., g(0)=1, and the last
value 0. The increasing full cycle attains the bound because arbitrary cuts
give disjoint paths with distinct endpoint values. n=1 is treated separately
from the descending-index argument; n=0 has one inverse. I found no missed
equality family. This is a consequence of the inverse axis, not a third
independent proof mechanism.

## Primary algorithm bodies actually read in this process

The full saved text ranges below were read directly, in bounded chunks.
Their hashes are bound by INPUT_PINS; source_context/MAPPING preserves the
original locations. No author/gate assertion substitutes for these reads.

| Primary body and actual saved-text scope | Literal subtraction and scope |
|---|---|
| `source_context/workspace/docs/papers204_208_sequence/scouting/finite_systems_nineteenth/public_sources/linearization-ALENEX07.txt`, lines 1–470 | Complete PL Algorithm 1, §2 model/proofs and §3 memory variant, plus beginning §4. The carrier is a connected undirected graph, with separate left/right linearizations and add-wins conflicts. Ordered star-to-chain replacement and old-edge path substitution are prior primitives. Their convergence does not classify this directed full-endofunction recurrence. |
| Same directory, `isprp_correctness_2005.txt`, lines 1–595 | Complete §4 rules and §§5.1–5.3, with model and start of conclusions. Every actual pointer repair chooses b in the clockwise interval from a to its previous successor c. Flooding likewise changes only to a closer successor. The printed final inequality in Lemma 7 has the opposite sign to its preceding rule-level cases; I use the cases, not that inequality or the source's whole correctness theorem. |
| `source_context/workspace/docs/papers204_208_sequence/scouting/FTH_GATE/public_sources/rn_TR2005_25.txt`, lines 1–414 | Complete model, §4 including Figure 3, and §5.1; opening §5.2 only. Action a1 minimizes distance over a candidate set containing the current successor; other actions do not replace Γ0. Therefore no fixed-peer successor change increases that distance. The source's acyclic-graph subcase is unnecessary for this rule-level exclusion and supplies no hidden theorem premise. |
| Same directory, all 259 lines of `tree_path_selected_sections.txt` | §1.3, §3.4, Appendix A.2 Algorithms 10–13 and full Appendix B. Sequential input is a rooted undirected tree with alternating depth labels; cases use parent, siblings, and grandchildren. Distributed input adds supervisor, advice, channel and timer state. Credit sibling rewiring and rooted-tree path construction. These assumptions and output are not repeated T on arbitrary endofunctions with vertex cycles. The extraction's apparent `u`/`v` pseudocode typo is not silently repaired into a P209 proof premise. |

The loop-free P209 witness `(1,2,1) -> (2,2,1)` changes vertex 0's
clockwise distance from 1 to 2 on labels 0,1,2; its return is also explicit.
It defeats a literal successor-repair step or a finite batch consisting
only of non-increasing-distance repairs. It does **not** prove absence of
all conjugacies, state extensions, projections, unfair schedules, or arbitrary
re-encodings. Rooted-tree carrier mismatch likewise defeats the stated
literal tree adapter, not all imaginable enlarged constructions.

The four bibliography entries were also checked against primary live pages
in this process, with full actual tool output in PRIMARY_METADATA_WEB.json:
[SIAM PL proceedings](https://epubs.siam.org/doi/10.1137/1.9781611972870.10),
[KIT Cramer–Fuhrmann report](https://publikationen.bibliothek.kit.edu/1000003169),
[NCSU Shaker–Reeves original](https://techrep.csc.ncsu.edu/2005/TR-2005-25.pdf),
and [versioned Aradhya–Scheideler arXiv record](https://arxiv.org/abs/2504.02448v1).
The last is version 1 of 3 April 2025; no newer-version claim is made.
All four citations are used for attribution/model comparison, not proof
premises. I did not rerun a broad owner search or claim complete coverage.

## Internal comparison originals actually read

All paths below start at frozen `source_context/workspace/`.

| Exact original and read extent | Deduction checked here |
|---|---|
| `docs/papers172_176_sequence/scouting/fresh_geometry_automata/SCOUT_AND_KILL_LEDGER.md`, full file, D03/FSP | FSP closes each fibre cyclically, forgets its destination, and maps permutations to identity. P209 retains destinations and fixes permutations. Inputs `(0,0)` and `(1,1)` have the same kernel but give `(1,0)` and `(1,1)`, even with different next kernels. Thus the stated old-kernel sufficient statistic fails. |
| `docs/papers177_181_sequence/scouting/combinatorial_lane/SCOUT_AND_KILL_LEDGER.md`, lines 1–40, C05/NOG and surrounding definitions | NOG encodes cyclic next-equal distance and factors through equality partitions. P209 uses absolute linear next positions and retained destination values. The same-kernel witness defeats this adapter. |
| `docs/papers204_208_sequence/scouting/combinatorial_second/PROOF_NOTES.md`, lines 1–70, complete PR section | PR reverses or retains an old unordered edge. P209 `(2,2,2) -> (1,2,2)` creates `{0,1}`, absent before. Thus the old-edge adapter fails literally. |
| `papers/167-minimum-inverse-position-feedback/main.tex`, lines 1–255 | P167 takes a minimum inverse position at the target coordinate, defaulting to identity; its first-image path split/reverse proof implies periods at most two. P209's `(1,2,3,1)` has period three by the proved recurrent theorem. This excludes a full same-carrier conjugacy; no full inverse-theory rereview is claimed. |
| `docs/papers162_166_sequence/scouting/degree_feedback_jump/SCOUT.md`, lines 1–130 | DFJ follows old forward orbits and squares permutations. P209's all-2 example sends 0 to 1 outside its old forward orbit `{0,2}`, and fixes permutations. This defeats the literal pointer-jump/power adapter. |
| `papers/169-successor-transfer-set-partitions/main.tex`, lines 1–462 | Complete literal, temporal and five-state inverse arguments in this scope. P169 moves the last repeated RGF symbol to the next block label; P209 changes nonlast positions to absolute positions and leaves the last destination. `00 -> 10` already leaves RGF. The old load rotation/trace machinery is credited, not relabelled as P209. |
| `docs/papers172_176_sequence/scouting/combinatorial_crossdomain/focused_nonextractive/IDEA_LEDGER.md`, full file, C01/MOC | MOC is the matching slice of P169 with a direction adapter. It does not eliminate the destination-sensitive distinction above. |

## Value verdict and reopeners

The strongest objection is that the inverse is elementary ordered path-cover
bookkeeping and the recurrent action, once identified, is just rotation.
Those ingredients get zero separate credit. The remaining short-note result
is the exact full-carrier necessity theorem forced by all backward-image
sets, coupled with a target-complete independent reconstruction/equality
analysis for this literal map. None of the checked explicit adapters transfers
that conjunction. This is sufficient for the assigned narrow internal
theorem-note contract, not evidence of broad novelty or venue fit.

No new scientific cutoff, sharp entrance clock, general-time inverse, EGF,
global priority or owner-nonexistence conclusion is warranted. A concrete
complete owner adapter or proof counterexample reopens the finding census.
All status remains OWNER_AMBER / HOLD_EXTERNAL.
