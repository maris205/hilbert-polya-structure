# P212 source audit and contribution subtraction

Status: author source preparation, not a new literature search, manuscript
review or novelty certificate. The mathematical premises below use the exact
primary-source scopes received in the accepted original gate and its deltas.
No new external fetch, PDF download, external upload or specialist contact
was performed for this source preparation. Source metadata and primary body
extents are inherited provenance, not a claim that this author newly read
every external PDF in full. References omit unverified journal pagination
and use the accepted author/preprint versions where appropriate.

## Primary references and exact received boundaries

| Reference / primary URL | Received body extent | Owned mechanism subtracted / article use |
|---|---|---|
| Manna–Waldinger, *The Deductive Synthesis of Imperative LISP Programs*, AAAI 1987, https://cdn.aaai.org/AAAI/1987/AAAI87-028.pdf | PDF p.5, printed p.159, extracted lines 384–445: complete nrev/nrev2 programs and listed input conditions; not a full derivation audit | The previous/current overwrite and advance is established reversal. Identifying previous=u, current=v and successor=f gives the exact kernel after removing nil and stopping. No kernel-invention credit. |
| Loginov–Reps–Sagiv, *Refinement-Based Verification for Possibly-Cyclic Lists*, LNCS 4444 (2007), https://research.cs.wisc.edu/wpis/papers/festschrift4444.pdf | PDF pp.14–15, lines 732–866: Figure 8, Section 5 and formulas (8)–(9); pp.19–20, lines 1056–1091: complete termination-monitor argument | Previous starts NULL and the loop stops at current=NULL. Reversal on cyclic/panhandle inputs, restored twice-traversed handles and at-most-two-visit termination reasoning are owned. No arbitrary nil-free orbit census is inferred from those inspected parts. |
| Berdine–Cook–Distefano–O'Hearn, *Automatic Termination Proofs for Programs with Shape-Shifting Heaps*, CAV 2006, https://jberdine.github.io/pub/2006_cav.pdf | Title/authors and complete Example 8 explanatory paragraph, PDF p.13, lines 665–679; not the general analysis theorem/algorithm | The panhandle argument explicitly uses 2i+j+k as a decreasing quantity; the analyzer missed that proof in the example. A doubled-handle clock is therefore not a new mechanism. |
| Holroyd–Levine–Mészáros–Peres–Propp–Wilson, *Chip-Firing and Rotor-Routing on Directed Graphs*, arXiv:0801.3306, https://arxiv.org/pdf/0801.3306 | Definition 3.1, unicycle definition, Lemmas 3.3–3.7 and Theorem 3.8, lines 523–612; Lemma 4.9 and Corollary 4.10 complete proofs, lines 1177–1226 | Fixed local cyclic orders, recurrent unicycles, Euler traversal and tree/Euler-tour correspondence are owned. |
| Pham Trung Van, *Orbits of Rotor-Router Operation and Stationary Distribution of Random Walks on Directed Graphs*, arXiv:1403.5875v8, 30 June 2015, https://arxiv.org/pdf/1403.5875v8 | Model/Theorem 1/conventions lines 24–35, 62–73, 105–127; Corollary 1/Lemma 5 lines 185–247; full Theorem 1 proof and Eulerian discussion lines 263–329 | On a fixed strongly connected directed multigraph, loops and parallel arcs allowed, with fixed cyclic orders, let T_G(v) count inward arborescences and M=gcd_v T_G(v). All recurrent rotor orbits have common length Σ_v d⁺(v)T_G(v)/M, and there are M of them. The common size is independent of cyclic order, although orbit membership may change. This full theorem, not only its Eulerian special case, is credited. |

The LNCS volume attribution was cross-checked in the received source audit
against the publisher's volume page
https://link.springer.com/book/10.1007/978-3-540-71322-7 and institutional
records. No current journal metadata is claimed for the two arXiv citations.
This source preparation inspected selected unchanged metadata records for
the bibliography, not a new external full-body retrieval or all-page view.

## What the comparison proves, and what it does not

On the loop-free labelled barbell (a,b,c)=(3,3,1), the closed pointer theorem
gives period 16. The same bidirected undirected core has 14 arcs and is
Eulerian, so its recurrent rotor period is 14. This separates only those
two natural fixed-core, time-preserving models. It does not exclude a
different graph, a suspension, enlarged states, a factor or an arbitrary
abstract encoding. The pointer classification and its decoration census
are proved directly; notation differences and a bounded search non-hit
are not proofs of priority or universal nonconjugacy.

The inverse, zero preperiod, unit fibres, fixed count n^n, augmented-edge
invariant and generic labelled set/list/reversal operations are zero-credit
background. Fixed-iterate counts and the state-weighted identity are only
consistency corollaries. The two accepted axes share the branch return map;
they are different information, not logically disjoint theories.

## Original documents actually used for this author preparation

All paths below are relative to /root/autodl-tmp/symbolic_dynamics. The exact
immutable inputs and received provenance records are listed with hashes in
ORIGINAL_INPUT_PINS.sha256. Hash pinning a record is not a claim of reading
every body it references. No mutable central STATE/PIPELINE bytes are pinned.

Completely read original mathematical and decision documents:

- docs/papers211_215_sequence/P212_THEOREM_CONTRACT.md and PROBLEM_ANCHOR.md;
  inherited docs/papers197_201_sequence/{PROBLEM_ANCHOR,HOSTILE_REVIEW_PROTOCOL}.md
  and docs/papers204_208_sequence/ARTIFACT_CONTRACT.md.
- scouting/finite_local_state_fresh_desk/{PROOF_PACKAGE,HANDOFF,SOURCES_AND_SUBTRACTION}.md
  within the current batch: the full 352-line author proof, not a summary.
- scouting/finite_pointer_residual_gate/{REPORT,MATHEMATICAL_AUDIT,SOURCES_AND_SUBTRACTION}.md
  and FINDINGS.json: the original mathematical/value gate and its full audit.
- scouting/finite_pointer_gate_response01/RESPONSE.md and the complete
  WEB_REQUESTS_AND_READ_BOUNDARIES.json; scouting/finite_pointer_gate_minor_delta01/DECISION.md
  and FINDINGS.json; scouting/finite_pointer_gate_e1_delta01/DECISION.md and
  all 414 lines of FINDINGS.json; qa/pointer_e1_root_reception01/RECEPTION.md.

The larger residual-gate WEB_REQUESTS_AND_METADATA.json was inspected only
in selected relevant ranges/metadata matches during this authoring task.
The archived record preserves exact requests and selected response metadata,
not a redistributed copy of every source body. Its original failed combined
request, truncations, later bounded successful reads, and documentary-check
failures remain where received. They are not rewritten as successful fresh
source reads. The corresponding Minor and E1 records are the exact additive
closures; a historical pending file is not silently overwritten.

## Internal subtraction and read-extent correction

The accepted gate, not a newly performed full-paper audit in this task,
supplies the following bounded historical comparisons. P167's full map
has transients and recurrent periods only 1 or 2. P209's full map is
noninjective already at n=2, unlike R. These rule out those specified
full-map identifications, not every extension or factor. The root/scout's
old augmented-edge proof and the fixed-digraph rotor lane remain owned.
No old paper, pilot or reviewer scientific module was imported, copied
as the verifier implementation, or executed.

The old scout P167 statement called lines 1–180 a full-file read, but
the original file has 385 lines. The accepted same-reviewer D1 delta
withdraws that historical wording additively. The mathematical gate's
actual full 385-line read supplies the current comparison, without
retroactively upgrading the old excerpt. This paper does not repeat
the erroneous full-read assertion or claim a new full P167 read.

## Authorship, review and evidence status

The root and original pointer scout contributed proof ideas. The present
paper-source author and the independent-source verifier coauthor are also
authors; none may serve as an independent P212 manuscript reviewer.
The original mathematical gate and accepted same-reviewer deltas concern
candidate admission, not manuscript A or B. See README.md for the actual
role ledger. No new outline panel or unavailable-provider review is claimed.

The accepted candidate pilot comprises n=1…4, 4,356 states and 50,392 checks.
It is not the paper's canonical or strict author pair. This source package
does not run anything scientific. Its new verifier is independent source,
awaiting exact root receipt and a separate runtime binding. No external
release or manuscript upload is authorized; HOLD_EXTERNAL remains in force.
