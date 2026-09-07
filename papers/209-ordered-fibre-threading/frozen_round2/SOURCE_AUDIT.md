# P209 source and internal-adapter audit

2026-09-07 UTC. Author-level scope check by the P209 writer. This is neither
manuscript A/B nor a new independent novelty clearance. The complete
[admission](source_context/workspace/docs/papers204_208_sequence/P209_ROOT_ADMISSION.md),
[original author proof](source_context/workspace/docs/papers204_208_sequence/scouting/finite_systems_nineteenth/FTH_PROOF_PACKAGE.md),
[gate decision](source_context/workspace/docs/papers204_208_sequence/scouting/FTH_GATE/CANDIDATE_GATE.md)
and [gate source/deduction audit](source_context/workspace/docs/papers204_208_sequence/scouting/FTH_GATE/SOURCE_AND_PROOF.md)
were read in full. Their candidate recommendation and later root admission
are different dated events, not a contradictory current manuscript verdict.

## Exact surviving claim and zero-credit ingredients

The three admitted statements are unchanged: the label-sensitive recurrent
cycle/path geometry and attached-cycle LCM; the all-target one-step path
decoder; and its unique global fibre maximizer. These are the whole scope
of [PROOF_PACKAGE.md](PROOF_PACKAGE.md).

Ordered star-to-chain replacement, connectivity by walk substitution,
rooted tree-to-path rewiring, kernel-class bookkeeping, ordinary path
covers, Boolean subset bounds, rotation/LCM and finite-map orbit enumeration
receive no independent novelty credit. The recurrent proof uses **every**
vertex-image set before its head-height comparison. The independent inverse
proof needs both distinct selected heads and distinct endpoint values.

## Primary algorithm bodies actually read

The following are the writer's own reads of the saved primary text, not
claims inherited merely from the gate. The raw bodies and exact text copies
are retained under `source_context/workspace/`, with original/snapshot pins
in [the context mapping](source_context/MAPPING.json). Saved text line
numbers identify the copy, not certified PDF-page visual anchors.

| Source | Actual body read in this author task | Subtracted primitive and precise remaining distinction |
|---|---|---|
| Onus, Richa, Scheideler, *Linearization: Locally Self-Stabilizing Sorting in Graphs* | Saved `linearization-ALENEX07.txt` lines 1–470, in two complete chunks; this includes the model, complete pure-linearization algorithm and proofs in §2, and the memory variant in §3. Also the displayed reference to Shaker–Reeves at lines 619–621 was inspected. No full experimental-section read is claimed. | Ordered star replacement and old-edge path substitution are prior primitives. PL has undirected connected graphs, left/right phases and add-wins conflict resolution. Its sorted-list convergence theorem is not a theorem about this directed old-fibre update on all endofunctions. |
| Cramer, Fuhrmann, *Self-Stabilizing Ring Networks on Connected Graphs*, 2005-5 | Saved `isprp_correctness_2005.txt` lines 1–595: model, §4 rules, complete §§5.1–5.3 including flooding and ordered-tree arguments, and opening conclusions. | Every successor-pointer repair shortens its clockwise interval. The loop-free transition `(1,2,1) -> (2,2,1)` increases vertex 0's successor distance from 1 to 2, so cannot be a literal repair or a batch of only shortening repairs. Flooding preserves the required no-increase condition; a direction typo in the final displayed inequality of its Lemma 7 proof is not used as a premise—the preceding rule-level cases give the comparison. This is not an arbitrary-factor nonexistence theorem. |
| Shaker, Reeves, *Self-Stabilizing Structured Ring Topology P2P Systems*, TR-2005-25 | Saved `rn_TR2005_25.txt` lines 1–414, with the initially truncated 175–224 region reread separately: complete model, §4 and Figure 3 pseudocode, complete §5.1 analysis; not the complete experiments. The departmental PDF was independently opened by the browser. | Figure 3 action a1 selects a closest candidate from a set containing the current successor. Its distance cannot increase. The same two-cycle defeats the stated literal/successive-shortening adapter. Neighbour arrays, searches, bootstrap data and messages are not erased to invent a conjugacy. |
| Aradhya, Scheideler, *Towards Learning-Augmented Peer-to-Peer Networks: Self-Stabilizing Graph Linearization with Untrusted Advice*, arXiv:2504.02448v1 | The entire 259-line saved `tree_path_selected_sections.txt`: §1.3, §3.4, Appendix A.2 Algorithms 10–13 and complete Appendix B proof. The truncated Algorithm 13/Appendix B region was reread in explicit smaller chunks. The exact versioned HTML body was also independently opened, but not linearly read in full. | Local sibling rewiring and the rooted tree-to-path construction are prior work. Algorithm 10 takes a rooted tree with depth-parity labels and uses parent/grandchild cases; the distributed version adds advice, supervisor, timers and messages. The full endofunction carrier of P209 allows arbitrary vertex cycles, and is not that tree input or those augmented configurations. No theorem excludes all imaginable projections of a larger system. |

The two proofs in this note use no unquoted external theorem as a hidden
premise. The cited works provide explicit attribution and model comparison,
not an imported FTH convergence theorem.

## Metadata and retrieval record

Only four entries occur in [references.bib](references.bib), and all four are
cited in the manuscript. No author list, report number, year or venue was
generated from memory. [The saved metadata calls](metadata_web_01.json) and
[the additional institutional record](metadata_web_02.json) preserve actual
retrieval output. Entries were transcribed from verified primary/institutional
metadata; they were not claimed to be a successful DBLP export.

- PL: the [SIAM proceedings record](https://epubs.siam.org/doi/10.1137/1.9781611972870.10)
  verifies all three authors, title, 2007 ALENEX proceedings, pp. 99–108,
  SIAM publisher and DOI. Its later online date, 18 December 2013, is not
  substituted for the 2007 proceedings year. The saved author PDF's title
  and author block agree. The `/doi/abs/` route timed out and the Bilkent
  browser PDF route failed; neither is relabelled a successful live fetch.
- ISPRP: the [KIT institutional record](https://publikationen.bibliothek.kit.edu/1000003169)
  supplies title, Curt Cramer/Thomas Fuhrmann, year 2005, Karlsruhe publisher,
  report series 2005,5 and DOI 10.5445/IR/1000003169. The saved primary first
  page confirms authors/title and the date 31 January 2005. The attempted
  browser BibTeX export returned unsupported content type, not usable BibTeX.
- RN: the [institutional catalogue record](https://repository.lib.ncsu.edu/items/d97f06ff-3ba3-4e7e-8bcd-9abbe5c8b12d)
  is available as its indexed full metadata record in `metadata_web_02.json`:
  Ayman Shaker, Douglas S. Reeves, 2005, TR-2005-25, Department of Computer
  Science, North Carolina State University. Direct page opening showed bot
  detection; the [departmental original](https://techrep.csc.ncsu.edu/2005/TR-2005-25.pdf)
  opened successfully and confirms title, authors and institution. The
  exact report version is cited to bind the Figure 3/§5.1 comparison to the
  inspected body. The PL bibliography also mentions a conference version;
  its metadata and report body are not silently merged into one entry.
- Tree-to-path: the [versioned arXiv primary record](https://arxiv.org/abs/2504.02448v1)
  verifies Vijeth Aradhya and Christian Scheideler, the complete title,
  version 1 and 3 April 2025. The cited algorithm comparison uses that
  exact version, not a claim about a current published revision. The
  matching versioned primary HTML was opened.

The department year-index route was unavailable and a later `find` call
did not locate the report; the successful indexed institutional record and
departmental body are the evidence actually used. The candidate gate's
older unavailable PDF structural preflight remains its own documented tool
limitation, not a new successful author preflight or page-view claim.
No source-body download is described as reading all of that body.

## Internal comparisons: exact originals and limited adapter conclusions

These are the writer's actual focused original reads. Historical finite
tables were not rerun or promoted to new author numerical evidence.

| Original and read extent | Literal comparison and subtraction |
|---|---|
| `fresh_geometry_automata/SCOUT_AND_KILL_LEDGER.md`, full file, especially D03/FSP | FSP closes each ordered fibre to its minimum and then maps every permutation to identity. Threading retains its old destination and fixes every permutation. For `(0,0)` and `(1,1)`, equal old kernels yield respective outputs `(1,0)` and `(1,1)`, with different output kernels. Thus the update, and even its next kernel, are not functions of the old kernel alone. Kernel encoding and falling-factorial inverse counts are subtracted. |
| `combinatorial_lane/SCOUT_AND_KILL_LEDGER.md`, lines 1–26, exact C05/NOG row with surrounding definitions | NOG is a cyclic next-equal-distance kernel encoding. P209 uses absolute next positions within linear fibres and retains destination labels. The same-kernel witness defeats this particular sufficient statistic. This is not a claim to have rereviewed the whole lane. |
| `combinatorial_second/PROOF_NOTES.md`, lines 1–70, complete PR section | PR only reverses or retains old unordered edges. Threading `(2,2,2)` gives `(1,2,2)` and creates the edge `{0,1}`, absent from the old edge set. This rules out the literal old-edge adapter, not every abstract factor. |
| P167 `minimum-inverse-position-feedback/main.tex`, lines 1–255 | Its rule selects the least preimage at the target coordinate, defaulting to that coordinate. The complete component/recurrent proof in this scope gives cycle inversion and reversible/splitting loop-rooted paths; recurrent whole-function periods divide two. P209 fixes all permutations and has period three on `(1,2,3,1)` by Theorem 1. This rules out a same-size full-carrier conjugacy. Selecting kernel extrema and functional-graph decomposition remain old. This read does not claim P167's complete inverse or all remaining manuscript proofs. |
| `degree_feedback_jump/SCOUT.md`, lines 1–130 | The DFJ update stays on each source vertex's old forward orbit and restricts to permutation squaring. In the displayed all-2 source, P209 moves vertex 0 to 1, outside its old forward orbit `{0,2}`, and fixes permutations. Forward powers, pointer jumping, support monotonicity and permutation-root counts are deducted. No arbitrary conjugacy exclusion follows. |
| P169 `successor-transfer-set-partitions/main.tex`, lines 1–462 | Complete literal/temporal and five-state inverse proof read. P169 replaces only the last occurrence of a repeated restricted-growth letter by the next block label, preserving its set-partition carrier and block count. P209 rewires nonlast positions to next absolute positions and retains the last destination. Its `00 -> 10` already leaves restricted-growth words. Canonical partition encodings, cyclic load smoothing and generic transfer matrices receive no P209 credit. |
| `focused_nonextractive/IDEA_LEDGER.md`, full file, C01/MOC | MOC is the matching/pair-partition restriction of P169 with the stated direction adapter. It does not turn P209's non-kernel-determined rule into a partition transfer. Ordinary token rotation is background, not the recurrent classification proved here. |

The actual snapshot mapping identifies the full original paths. This task
does not rerun the candidate gate's 3,160-file/21-command discovery or claim
to read that corpus. Its exact bounded discovery and original subtraction
are existing admission evidence. The writer has checked the specified
nearest comparisons and cited metadata, not certified the nonexistence of
all literature owners. The historical P51–P56 gaps and split Git paths in
[the unchanged caveat record](source_context/workspace/docs/research_state/HISTORY_AND_CAVEATS.md)
remain visible. Gate-only P139/P188 false-positive reads are not relabelled
new author full-paper readings.

## Result and reopener

The modest short-note claim is the exact labelled recurrent carrier forced
by all backward-image sets, together with the independently derived
all-target inverse and unique extremizer for this literal update. No
checked specified adapter consumes that conjunction. The all-size sharp
entrance clock, general-time inverse, recurrent EGF, arbitrary-size period
census and global priority remain excluded. A complete applicable owner
adapter or substantive manuscript finding reopens the gate. All external
uploads, submissions, specialist contact and release remain `HOLD_EXTERNAL`.
