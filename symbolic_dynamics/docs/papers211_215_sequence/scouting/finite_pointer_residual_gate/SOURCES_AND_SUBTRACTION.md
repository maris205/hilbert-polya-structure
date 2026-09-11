# Primary-source and old-mechanism boundary

Date: 2026-09-08 UTC. This is a bounded source audit for exactly one
already-known kernel. No search non-hit establishes novelty or priority.

## Primary bodies used

| Primary source | Actual read extent used | Subtraction |
|---|---|---|
| Manna and Waldinger, *The Deductive Synthesis of Imperative LISP Programs*, AAAI 1987, [proceedings PDF](https://cdn.aaai.org/AAAI/1987/AAAI87-028.pdf) | PDF page 5 / printed page 159, extracted lines 384–445: the complete nrev/nrev2 displayed program and the listed input conditions. Surrounding derivation text was returned but is not a claimed full derivation audit. | The current/previous overwrite and advance is established in-place reversal. Its list, finiteness, purity and isolation preconditions are not the arbitrary closed total-function carrier. |
| Loginov, Reps and Sagiv, *Refinement-Based Verification for Possibly-Cyclic Lists*, LNCS 4444 (2007), [author-hosted PDF](https://research.cs.wisc.edu/wpis/papers/festschrift4444.pdf) | PDF pages 14–15, extracted lines 732–866: entire Figure 8 loop, Section 5 acyclic/cyclic/panhandle discussion and formulas (8)–(9); PDF pages 19–20, lines 1056–1091: entire termination-monitor argument. | The previous pointer starts NULL and the loop stops at current=NULL. Cycle reversal, twice-traversed/restored handles and the at-most-two-visits termination argument are owned. These inspected parts do not state the arbitrary-pair no-nil period/orbit census. |
| Berdine, Cook, Distefano and O'Hearn, *Automatic termination proofs for programs with shape-shifting heaps*, CAV 2006, [author-hosted prepublication PDF](https://jberdine.github.io/pub/2006_cav.pdf) | Title/authors at PDF page 1; Example 8 and its entire explanatory paragraph, PDF page 13 / extracted lines 665–679. The general termination-analysis theorem and algorithm were not audited. | The panhandle argument already explicitly uses the doubled-handle linear quantity 2i+j+k. Counting the outbound and restored handle is not a new clock mechanism. |
| Holroyd, Levine, Mészáros, Peres, Propp and Wilson, *Chip-Firing and Rotor-Routing on Directed Graphs*, [arXiv 0801.3306 PDF](https://arxiv.org/pdf/0801.3306) | Definition 3.1, unicycle definition and Lemmas 3.3–3.7/Theorem 3.8, extracted lines 523–612; Lemma 4.9 and Corollary 4.10 complete proof bodies, lines 1177–1226. | Fixed local cyclic-order routing, recurrent unicycles, Euler traversal and the tree/Euler-tour correspondence are established. No such theorem is newly claimed here. |
| Pham, *Orbits of rotor-router operation and stationary distribution of random walks on directed graphs*, [arXiv 1403.5875v8 primary PDF](https://arxiv.org/pdf/1403.5875v8), version stamp 30 June 2015 | Literal model, Theorem 1, loops/multiedges convention, lines 24–35, 62–73, 105–127; Corollary 1/Lemma 5 and full Theorem 1 proof, lines 185–247 and 263–329. No all-page visual audit is claimed. | On each fixed strongly connected digraph all recurrent rotor orbits have the same size, evaluated using the arborescence vector divided by its gcd; the gcd counts the orbits. These complete classical orbit facts must be credited as well as the Eulerian special case. |

For Loginov–Reps–Sagiv the 2007 LNCS publication metadata was cross-checked
against the [publisher's volume contents](https://link.springer.com/book/10.1007/978-3-540-71322-7)
and the authors' institutional records. Mathematical premises use the
author-hosted PDF body, not a secondary summary. The two arXiv entries
above identify the retrieved primary preprint versions; this audit does
not certify their current journal metadata.

The main binding of the first two programs is: old previous=u, old
current=v, stored successor=f. At a loop boundary the next registers
are v and old f(v), while the old cell v now stores u. Removing nil
and the stop supplies exactly the candidate's autonomous completion.
This is an explicit old-kernel identification, not a distinct-name test.

## Stronger comparisons, without universal nonconjugacy claims

A superficial comparison with ordinary rotor routing on the same
bidirected core fails concretely. Consider a loop-free barbell with
cycle lengths (3,3) and bridge length 1. It has six vertices and seven
undirected edges. The candidate anchor dynamics have exact period
2(3+3+2)=16. The ordinary rotor operation on its bidirected graph has
14 directed arcs and exact recurrent period 14 by the Eulerian theorem.
Thus no time-preserving conjugacy identifies these two fixed-core
permutations. The pointer bridge is traversed four times in its full
return; a bidirected rotor tour uses each directed arc once.

This comparison excludes only that natural same-core identification.
It does not exclude a different graph, a suspended or enlarged-state
encoding, a factor, or all abstract rotor representations. In particular,
every finite permutation can be encoded after its cycle decomposition
is already known; that tautological encoding would not transfer the
desired classification or constitute a prior proof.

The author's complete orbit classification still has to supply the
period, degeneration quotient and frozen-complement reconstruction.
None is inferred merely from the difference between the two update
notations. The extra attribution in PTR-G-S1 is required before a
manuscript source account is treated as complete.

## Internal original reads

All workspace paths below are relative to
/root/autodl-tmp/symbolic_dynamics; the sole absolute mirror original is
explicitly pinned. No Git command was run.

| Original | Read extent in this gate | Consequence |
|---|---|---|
| scouting/finite_local_state_fresh_desk/{PROOF_PACKAGE,HANDOFF,SOURCES_AND_SUBTRACTION}.md under the current batch | All three complete | Exact candidate and author claims reviewed. Five-payload manifest checked in its own directory. The two metadata JSON files were pinned; selected pointer-relevant records, not the whole historical archive, were audited. |
| scouting/finite_graph_memory_fresh_desk/{HANDOFF,SOURCES_AND_SUBTRACTION}.md | Both complete | Old thin-remainder rejection remains unchanged. |
| Same desk PROOF_PACKAGE.md | Lines 211–280, complete pointer inverse/invariant/reverser sections | Inverse, fixed count and edge invariant were already present. Other lane proofs are not credited as current audit work. |
| papers/167-minimum-inverse-position-feedback/main.tex | All 385 lines; additionally main.pdf pages 1–3 extracted as text | Least-preimage selection, image-path reversal and recurrent species are already occupied. Its full map has transients for n>=2 and its recurrent periods are only one or two; the closed pointer permutation is not that full map. This does not exclude every factor on a larger carrier. |
| papers/209-ordered-fibre-threading/sections/01_setup.tex and 02_recurrence.tex | All 58 and 111 lines; main.pdf pages 1–3 additionally extracted as text | Ordered-star threading, frozen-height reasoning and backward attachment rotation are occupied. Its full map is noninjective already on two labels: in its 0-based notation, T(00)=10=T(10), whereas R is bijective. This rules out full-map conjugacy at that boundary, not all possible extensions. |
| /root/autodl-tmp/hilbert-polya-structure/henon_dynamics/henon_rotor_router_strong_digraph_route_a/THEOREM_PACKAGE.md | All 70 lines, text only | Exact prior rotor carrier and imported Pham/tree mechanism. The historical HP verdict does not free the finite map for reuse. No old producer was imported or executed. |
| docs/papers197_201_sequence/scouting/fifth_fresh_20260905/period_feedback_reentry/SOURCE_OWNER_AND_COLLISION.md | Only rg context around the pointer-reversal match | A further P167 signpost, not a new original or proof premise. |
| papers/93-random-push-pop-stack-cocycles/{main.tex,README.md,HOSTILE_REVIEW.md} | Only the returned rg contexts | The word bicyclic refers to the monoid relation for random push/pop maps, not a claimed same-core pointer result. No whole-paper review or new collision theorem is asserted. |

The search over current old-paper/scout text deliberately excluded frozen,
QA, source-context and current P211 source trees. It was bounded discovery,
not a full-history certificate. Only the originals above support the
concrete subtraction claims.

### Exact historical read-extent defect

The current author's source table calls P167 lines 1–180 a complete-file
return. Native record c59488 in its NATIVE_READS.json actually requests
sed -n '1,180p' and ends at the table midrule. The unchanged P167 file
has 385 lines, hash
500fdea81499204a92bd3b6e24c5f9fd7b758d29b5c5dcdbf60e5e3f8e861d73.
The erroneous full-file wording must be corrected additively; neither
the old file nor the sealed author package is to be overwritten.
This gate's actual complete cat return supplies the missing current
read scope. It does not retroactively turn the old excerpt into a
complete read. This is PTR-G-D1, a documentary Minor.

## Search and retrieval limits

The exact independent browser requests are retained. Search phrases included
pointer/list reversal with period, permutation, orbit, enumeration, bicyclic,
theta, barbell, closed, dynamical and non-terminating; additional queries
checked the complete rotor theorem and bibliographic attribution. They
mostly returned programming or irrelevant discovery material. Pham and
the CAV paper were followed to actual primary bodies. No search result
alone supplies a new mathematical premise. No closer published full
no-nil classification was identified in these bounded reads, which is
not proof that none exists.

Research-lit's optional Zotero/Obsidian providers were unavailable. The
arXiv helper lookup returned no script; direct primary web reads were
the documented fallback. No PDF was downloaded into this package.
Text extraction of two existing local PDFs is not a visual review.

One combined browser request failed at orchestration with a connection
error and no native return; the same individual source reads succeeded
later and are separate records. Initial combined tool displays were
truncated, and an erroneous inspection of a string's enumerable character
keys produced a large truncated display. These are preserved as disclosed
display/navigation failures, not source or scientific evidence. The
controlling body ranges were subsequently read in bounded returns.

The local jq discovery also returned exit one, so its chained checks did
not run. Standard-library JSON parsing was used instead. An initial
input-pin check warned about an extra blank line even though the command
returned zero; it was not accepted as strict manifest validation. The
unsealed owned file was corrected and checked with --strict. Both actual
returns, and the explicitly reconstructed initial layout, are retained in
DOCUMENT_CHECK_NATIVE.json.

WEB_REQUESTS_AND_METADATA.json retains actual request objects, response
lengths and selected unchanged metadata fragments. It does not claim
full-text redistribution, a local PDF hash, or a fully audited external
proof beyond the stated extents. NATIVE_READS.json retains selected actual
complete documentary command results; it is not a complete session log.
No source body was uploaded to a manuscript-review provider.
