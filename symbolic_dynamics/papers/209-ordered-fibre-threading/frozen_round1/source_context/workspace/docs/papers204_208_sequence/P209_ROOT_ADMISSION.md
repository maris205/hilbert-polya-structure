# P209 root admission: ordered fibre threading

2026-09-07 UTC. **ADMITTED_NARROW_THREE_THEOREM_CONTRACT / WRITING_PENDING /
OWNER_AMBER / HOLD_EXTERNAL.** This assigns P209 within the existing five-seat
batch. It is not a manuscript acceptance, paper completion or new batch.

## Exact admitted map and theorem ceiling

The state is a labelled endofunction on the ordered set
$[n]=\{0,\ldots,n-1\}$, including $n=0$. For each **old** nonempty fibre
$f^{-1}(v)=\{i_1<\cdots<i_k\}$, the simultaneous update sets
$T(f)(i_j)=i_{j+1}$ for $j<k$ and $T(f)(i_k)=v$. Destination labels are
retained; this is not a map of equality partitions alone.

1. **Exact recurrent carrier and labelled period.** Each weak functional-graph
   component is a directed cycle with disjoint unbranched feeding paths, at
   most one path per cycle vertex. Every final path vertex has label below
   the minimum label of its cycle. These conditions are necessary and
   sufficient for recurrence under the update on whole functions. Cycle and
   internal-path arrows remain unchanged; attachments move one cycle
   predecessor backwards. The exact period is the LCM of lengths of cycles
   carrying nonempty paths, with empty LCM one. Pure cycles are fixed.
2. **All-target one-step inverse.** For any target $g$, select a subset
   $S\subseteq\{i:i<g(i)\}$. It is admissible exactly when selected heads
   $g(i)$ are pairwise distinct and endpoint values $g(j)$ for $j\notin S$
   are pairwise distinct. Selected arrows form increasing paths, including
   singletons. If $e_S(i)$ is the endpoint of the path containing $i$, then
   $f_S(i)=g(e_S(i))$ bijects admissible codes with all predecessors of $g$.
   This includes empty fibres and selected arrows whose numerical value
   happens not to change under threading.
3. **Unique global fibre maximum.** For $n\ge1$ the maximum is $2^{n-1}$,
   attained only by $g_*(i)=i+1$ for $i<n-1$, $g_*(n-1)=0$. The empty
   target has one predecessor; singleton conventions agree.

No all-size sharp entrance clock, general-time inverse, recurrent EGF,
unrestricted period census or publication-priority statement is admitted.
The short note must keep these exclusions visible.

## Original proof and source inspection

Root read the complete [author proof](scouting/finite_systems_nineteenth/FTH_PROOF_PACKAGE.md),
the independent [gate](scouting/FTH_GATE/CANDIDATE_GATE.md), its complete
[deductive/source audit](scouting/FTH_GATE/SOURCE_AND_PROOF.md), findings,
pre-author-code commitment, standalone kernel and execution/closure sources.
The proof first freezes **every** backward image set on a periodic orbit;
only then does coordinate-head height monotonicity force the path/cycle
geometry. First-image/rank monotonicity alone is not used as a substitute.
The inverse proof is independent of this recurrent argument, and equality
in its Boolean bound forces the unique cyclic-successor permutation.

Root also read the decisive primary bodies: PL's algorithm and proof
sections (saved layout 1–470, not the whole experimental section); ISPRP's
model/rules and complete sections 5.1–5.3; RN's model, Figure 3 pseudocode
and section 5.1 (saved layout 1–414); and the 2025 tree-to-path version's
sections 1.3/3.4, Appendix A.2 algorithms 10–13 and complete Appendix B
proof. The RN [departmental original](https://techrep.csc.ncsu.edu/2005/TR-2005-25.pdf)
and [versioned 2025 primary body](https://arxiv.org/html/2504.02448v1)
were also actually opened by root. The gate's unavailable PDF structural
preflight remains an explicit tool limitation; named-section text reads
are not relabelled as certified page anchors.

Ordered star-to-chain replacement, path-substitution connectivity,
tree-to-path rewiring, ordinary path covers and rotation/LCM calculations
receive no independent novelty credit. The ring algorithms' successor
distance cannot increase; the loop-free FTH transition
$(1,2,1)\mapsto(2,2,1)\mapsto(1,2,1)$ defeats that literal or
shortening-repair-batch adapter. It is not a general nonconjugacy theorem.
The 2025 algorithm has rooted-tree/depth-parity/supervisor/message state,
not the full endofunction carrier with arbitrary vertex cycles.

Internal subtraction follows the exact originals and witnesses in the
gate: FSP/NOG kernel encoding, PR old-edge rewiring, P167/MIP,
DFJ forward-orbit updates, and P169/MOC. Root read the complete P169
temporal/inverse body and MOC ledger; its P167 and DFJ readings were the
literal/recurrent and forward-orbit portions needed for the displayed
tests, not a claim to have rereviewed every inverse theorem. P139/P188
were literal false-positive checks only. The 3,160-file discovery corpus
and its 21 command results are bounded search evidence, not full-paper
reads or a global owner-nonexistence certificate. Historical numbering and
split-path caveats are unchanged.

The surviving contribution is this literal update's label-sensitive
recurrent classification together with its independent all-target inverse
and unique extremizer. This meets the modest anonymous short-note gate;
a complete owner adapter or substantive manuscript finding reopens it.

## Actual evidence and root reproduction

Root's [original-evidence inspection](qa/FTH_GATE_ROOT_ORIGINAL_INSPECTION.actual.json)
checked the full 1,053-payload independent package, preserved initial and
interrupted-attempt evidence, all reviewed originals/snapshots, history
inputs, two original independent capsules and full author reconciliation.
The gate seal is
`6989fad02d78655482d50a1eb18e6e099b44e016f1cec4478e7e94e88a483940`.

Root then actually executed the unchanged independent kernel twice in new
physical code-only capsules at the original $n=0,\ldots,5$ cutoff.
Each run has 3,414 states, 147,091 checks and complete 5,605,960-byte stdout,
SHA256 `3898b7c2957d47388366f0eb21740349ab8a2fcb5301f68576705b7e74cd4177`.
All three producer-pair/canonical raw comparisons exited zero. These finite
checks pressure the proofs; they do not establish the all-parameter results.

The [root pair and complete closure receipt](qa/FTH_ROOT_STRICT_PAIR.actual.json)
records actual commands and exit zero. The complete [520-payload pair](qa/root_fth_gate_pair_01/SHA256SUMS)
has seal `702c9105e276c7fd02224897510a660fcac87e1b803c911ea471ae84349bf761`.
All 5,309 known scientific/runtime/capsule inputs were rechecked twice;
945 runtime files, 29 optional-presence checks and five configuration
directories were unchanged. All 119 recorded child commands exited zero,
including 114 actual dependency commands, two producers and three raw
comparisons. A later root closure made three additional actual raw
comparisons, all zero. Parent/child module, map and observed-open coverage
has no uncovered file or bytecode cache; generated receipt reads are
distinguished from prior inputs. These are sampled observations plus a
conservative inventory, not continuous tracing or an OS-hermetic claim.

## Authorship and next gate

Root and nineteenth_finite_scout are proof contributors and cannot be
independent manuscript reviewers. The candidate assessor
twentieth_algebra_scout supplied no new lemma and disclosed reading a
theorem/proof summary before its kernel commitment; its later manuscript
eligibility requires that familiarity to remain explicit. The candidate
gate is neither manuscript review A nor B.

The author package will be written at
`papers/209-ordered-fibre-threading/`, with a fresh paper-local verifier,
full canonical stdout, proof/source/claim documents and anonymous LaTeX.
Round0 must follow actual author evidence and source-only build/view checks.
Exactly two later process-separated nonauthor manuscript reviews, accepted
deltas, Round1/2 and terminal build/view/artifact gates remain required.
No public upload, submission, external contact or release is authorized.
