# FTH independent source, proof and value assessment

Assessor: `/root/twentieth_algebra_scout`, 2026-09-06 UTC, current project
model/settings. This is a noncontributor candidate gate. Root and
`nineteenth_finite_scout` are authors. This document does not repair their
proof, write a new lemma, certify priority, or replace either manuscript
review. Verdict scope is exactly the three statements in the pinned
`FTH_PROOF_PACKAGE.md`.

## Deductive audit: what was attacked

The literal state is a labelled function on `{0,...,n-1}`, including the
empty function. For each increasingly ordered old fibre, thread consecutive
members and retain the old destination at its last member. Updates use the
entire old function. The two dynamical levels must remain distinct: cycles
of a vertex map are not cycles of the update on whole functions.

### Recurrent carrier and exact labelled period: PASS

The potentially decisive gap was whether first-image monotonicity alone
could prove the asserted recurrent geometry. It cannot. The actual proof
uses **every iterated vertex-image set**, not merely rank, indegree at most
two, disappearance of backward arrows, or a bounded census.

I checked the following dependencies in author Steps 1–4.

1. Replacing an old arc by its fibre suffix gives a nonempty directed walk,
   including loops and the case in which the retained destination is itself
   in that fibre. Concatenation may repeat vertices, which is harmless:
   its final `r` arcs still witness membership in the new `r`th image.
2. Inclusion around a periodic whole-function orbit forces equality of
   each of those labelled sets. Thus each vertex's finite/infinite backward
   height is constant over that orbit. The argument is not circular: this
   equality precedes the coordinate-height comparison.
3. Along an old arc into a noncycle vertex, backward height rises strictly;
   equality along an arc is possible only with both heights infinite.
   The new head of a coordinate is either retained or the next old sibling,
   whose old head is that coordinate's old head. Its height therefore cannot
   rise. Periodicity eliminates every strict drop. This applies even when
   a selected sibling numerically equals the retained old destination.
4. Every nonfirst fibre member must consequently be a cycle vertex. A
   fibre contains at most one such vertex. Noncycle indegree is at most
   one, and cycle indegree at most two; the latter includes exactly its own
   cycle predecessor. This gives disjoint unbranched feeding paths, with
   at most one attachment at each cycle vertex, not arbitrary rooted trees.
5. Cycle arrows and internal path arrows are retained. Each final path
   label travels one cycle predecessor backwards. To remain the smaller
   member at every epoch it must be below the minimum label of that whole
   cycle. Conversely this strict inequality preserves the geometry and
   prevents attachment collisions. A chosen labelled final vertex first
   returns after the cycle length; different components then synchronize
   by the LCM. Pure cycles do not move, and the empty LCM is one.

Thus the necessity and sufficiency proofs close without assuming the
unproved entrance clock. Ordinary rotation/LCM calculations receive zero
independent contribution credit; identifying exactly which labelled
configurations support them is the substantive recurrent result.

### All-target path-cover inverse: PASS

The tests in author Step 5 are both necessary. Distinct selected heads
prevent a merge inside the selected path graph; distinct endpoint values
prevent two reconstructed source fibres from merging. Increasing edges
exclude selected cycles without an extra acyclicity oracle. Singleton paths
and unsupported targets are covered. Importantly, the code selects all
nonmaximal members of source fibres, **not only coordinates whose numerical
value changes**. Otherwise some valid codes would be lost.

For the converse I checked the exact recovery direction: endpoint values
make the reconstructed fibres precisely the chosen path vertex sets; their
increasing order reproduces the selected arrows and retained endpoint
arrows. Recovering nonmaximal fibre members recovers the code. This proves
injectivity, rather than merely a surjective generator or a source search.

Path-cover terminology, subset counting, and generic inverse coding receive
no novelty credit. The asserted residual is this literal map's necessary
and sufficient all-target compatibility test and nonredundant decoder.
No stronger closed product, general-time fibre law, or new reviewer lemma
is added to the author's contract.

### Sharp maximum and all equality cases: PASS

At most `n-1` coordinates can be eligible. Equality in the two-stage bound
requires all lower coordinates to be eligible and every subset to work.
In particular the empty subset must work, forcing a permutation target.
Downward elimination then forces the cyclic successor permutation. For
that permutation every subset works. This handles both directions of
uniqueness, rather than only exhibiting a witness. The empty/singleton
conventions are explicit and consistent.

The Boolean bound and permutation elimination are elementary. The exact
unique target is credited only in conjunction with the actual inverse of
this map; a repeated power of two in unrelated examples is not a transfer.

## Primary owners: bodies read, not abstract clearance

The browser discovery record is preserved in nine JSON calls under
`source_search/`: seventeen literal/mechanism queries in total, three with
a 180-day filter. Old items returned by that filter are not evidence of
complete recent coverage; crawl/index dates are not publication dates.
The search is bounded and did not establish universal absence of an owner.

The ARS source-verification workflow required PDF structural preflight.
All three actual preflight invocations returned `UNAVAILABLE` because
`pypdf` is not installed. No page-count or page-anchor certification is
claimed. Comparisons below cite named sections/algorithms and saved text
line scopes, with the raw PDFs retained. This does not leave an inaccessible
directly applicable theorem: the comparison bodies were actually read.

| Primary original and actual read | Exact subtraction and boundary |
|---|---|
| Onus–Richa–Scheideler, *Linearization: Locally Self-Stabilizing Sorting in Graphs*, ALENEX 2007. [Author PDF](https://www.cs.bilkent.edu.tr/~onus/yayinlar/linearization-ALENEX07.pdf). Pinned author-preserved PDF/layout; layout lines 1–470 and 548–end: complete §2 algorithm/proofs, §3 and later conclusions, not a complete experimental-section reading. Browser PDF open failed again. | Ordered star-to-chain replacement and connectivity by path substitution are owned primitives. PL uses connected undirected graphs, smaller/larger-neighbour phases and an add-wins conflict rule. Its sorted-list convergence theorem does not transfer to FTH, which fixes all permutations and can rotate labelled attachments forever. The phase/memory variants read in the body retain different state and rules. |
| Cramer–Fuhrmann, *Self-Stabilizing Ring Networks on Connected Graphs*, TR 2005-5. [Institutional record](https://publikationen.bibliothek.kit.edu/1000003169) and [full text](https://publikationen.bibliothek.kit.edu/1000003169/2846). Pinned author-preserved PDF/layout, lines 1–590: model, rules and complete §§5.1–5.3 including flooding/ordered-tree arguments. | ISPRP shortens each changed clockwise successor interval; flooding retains that monotonicity. FTH's loop-free `(1,2,1) -> (2,2,1)` lengthens vertex 0's successor interval, and returns in the next step. This is neither an allowed individual pointer repair nor any batch of only such shortening repairs. Address wrap, routing state and floods are not discarded to manufacture an identity. |
| Shaker–Reeves, *Self-Stabilizing Structured Ring Topology P2P Systems*, TR-2005-25. [Institutional metadata](https://repository.lib.ncsu.edu/items/d97f06ff-3ba3-4e7e-8bcd-9abbe5c8b12d), [departmental original](https://techrep.csc.ncsu.edu/2005/TR-2005-25.pdf). New saved 97,406-byte PDF and layout; lines 1–414 cover model, §4, complete Figure 3 pseudocode and §5.1 proof. | The first repository PDF response was later replaced by a bot-detection page, so it supplied no proof read. The departmental original succeeded. Action a1 chooses a closest candidate from a set containing the current successor; every successor change strictly shortens its circular distance. Its random searches, bootstrapping, messages and neighbour arrays are extra state, and the same FTH two-cycle violates its necessary successor monotonicity. No literal or schedule adapter survives this test. |
| Aradhya–Scheideler, *Towards Learning-Augmented Peer-to-Peer Networks: Self-Stabilizing Graph Linearization with Untrusted Advice*, arXiv:2504.02448v1. [Versioned primary body](https://arxiv.org/html/2504.02448v1). Raw HTML retained; selected extraction read in full, 259 lines: §1.3, §3.4, Appendix A.2 algorithms 10–13, complete Appendix B theorem/proof. Browser also supplied the sorted-path problem definition and §2 primitives. | This closer sibling/tree-path variant uses a rooted, depth-parity-labelled tree, grandchild/parent cases, a supervisor, certificates, timers and messages. Algorithm 10 constructs a directed path in one transformation, with orientation depending on depth parity. It is not repeated FTH on all endofunctions; in particular it excludes initial vertex cycles in its input tree. Its local sibling rewiring and tree-to-path construction receive owner credit. A model-erasing projection is not a proved conjugacy. |

The three successful PDF/HTML retrieval/extraction facts and the failed
browser routes are preserved, not silently substituted. No ResearchGate,
search snippet, inaccessible abstract, patent result or unspecified theorem
is used as a proof premise. No paper was uploaded to an external service.

## Internal adapters and exact read limits

The independent `search_history.py` run selected 3,160 manuscript/desk
files across the workspace and both documented mirror layouts, excluding
review/build/frozen copies and the current FTH/P208 lanes. Twenty-one actual
`rg` chunks cover three literal/mechanism families. Raw output totals
11,200 bytes and was read in full; every selected-file and tool pin is
unchanged before/after. This is discovery, not reading 3,160 full files.
The author's separate 4,244-file search remains author evidence only.
Missing P51–P56 and split/local-only historical paths remain unresolved as
recorded in `HISTORY_AND_CAVEATS.md`.

| Original examined | Adapter test and result |
|---|---|
| FSP: full `fresh_geometry_automata/SCOUT_AND_KILL_LEDGER.md`, D03 row and decision context. | FSP closes each old fibre cyclically to its minimum and then collapses permutations to identity. FTH retains destination labels and fixes every permutation. The same-kernel sources `(0,0)` and `(1,1)` have FTH images `(1,0)` and `(1,1)`, whose equality partitions also differ. Thus neither FTH nor its next equality partition is determined by the old kernel alone. Static kernel reconstruction and falling-factorial counts are fully subtracted. |
| NOG: exact C05 row with surrounding comparison context in `combinatorial_lane/SCOUT_AND_KILL_LEDGER.md`; not a full rereview of that lane. | NOG encodes cyclic next-equal distances from an equality partition. The same-kernel witness above rules out this specified sufficient statistic for FTH. Noncyclic absolute next positions and retained destinations are not renamed cyclic distances. |
| PR: complete definition and deduction in `combinatorial_second/PROOF_NOTES.md`, first section; report read in full earlier. | PR reverses or retains old unordered edges. FTH sends `(2,2,2)` to `(1,2,2)`, creating sibling edge `{0,1}`. This defeats the proposed literal edge-descent adapter, not arbitrary abstract factors. |
| MIP/P167: `main.tex` lines 1–370, including literal, full main theorem, component/clock/recurrent/inverse proofs and start of exact-controls section. | MIP selects a least preimage at the *target* coordinate and defaults to itself. Its whole-function recurrent periods divide two and fixed states are involutions. FTH fixes all permutations and already has exact period three on the four-label tail/three-cycle example `(1,2,3,1)`. Same-size whole-carrier conjugacy is therefore impossible. Functional-graph decomposition and selecting extrema inside kernel classes are old. |
| DFJ: complete `degree_feedback_jump/SCOUT.md`. | Every updated coordinate lies on its old forward orbit; permutation dynamics is squaring. For `(2,2,2)`, FTH moves coordinate 0 to 1, outside `{0,2}`. FTH also fixes the full permutation carrier. Generic forward powers, pointer jumping, support monotonicity and cycle-root enumeration do not explain this update. |
| P169 and MOC: `169-successor-transfer-set-partitions/main.tex` lines 1–462, covering literal, temporal proof and complete five-state inverse proof; full focused matching/word idea ledger including C01/MOC. | P169 changes only the last occurrence of each repeated RGF letter by incrementing its block label, with fixed block count and a directed-cycle load factor. MOC is its matching restriction. FTH changes nonlast members to next positions, retains the last destination, and is not even kernel-determined. The RGF carrier is not preserved, since `00 -> 10`. Canonical partition encodings, load smoothing, ordinary cyclic token rotation and transfer-matrix counting receive no FTH credit. No claimed FTH axis is obtained by this literal restriction or reversal. |
| Search false positives P139 and P188: P139 `main.tex` lines 1–95, P188 lines 40–95, enough to read complete literals and stated contexts, not their full proofs. | P139 feeds back a binary Lyndon-start mask; P188 is `A -> A intersect [|A|]`. Their “chain” fibre wording is not the FTH rule. Neither is used as a general nonconjugacy theorem or a source of FTH claims. Other irrelevant discovery rows were not promoted to owner evidence. |

The original seventeen author historical pins, full author package and root
proof observations are physically archived in `reviewed_input_snapshot/`.
The six additional source/criterion originals are separately pinned and
copied in `supplementary_source_snapshot/`; these were documentary checks
after the two science runs and were not imported into those runs.

## Value decision after subtraction

The strongest kill argument is that both “LCM of rotations” and “count
increasing path covers” are standard. I agree and assign them zero standalone
credit. The surviving first axis is the exact, label-sensitive recurrent
carrier forced by every backward-image set; it is not a finite-map census
or convergence statement. The second axis reconstructs every possible
one-step source by necessary/sufficient target constraints and classifies
the unique global fibre maximizer. It does not use the recurrent proof,
while the recurrent proof does not use the inverse atlas.

No checked owner or internal map transfers that pair of model-specific
conclusions by the stated literal/conjugacy/factor/parameter adapters. On
the inherited **anonymous short theorem-note** threshold this is enough for
`GO_BOUNDED_CONTRACT`, with restrained claims; it is not a claim of a new
general counting method, a deep clock theorem, or publication-level priority.
The mathematical work is modest and the literature search remains bounded.
An actual complete owner adapter or substantive manuscript defect must reopen
the decision. Root admission and both later manuscript reviews remain
separate obligations. `OWNER_AMBER / HOLD_EXTERNAL` persists.
