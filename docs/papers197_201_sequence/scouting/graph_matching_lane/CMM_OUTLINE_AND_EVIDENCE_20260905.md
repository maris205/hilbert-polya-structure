# CMM anonymous short-note outline and evidence map

Date: 2026-09-05 UTC. **OUTLINE ONLY / NO PAPER NUMBER / HOLD_EXTERNAL**.
This is the root-commissioned author planning artifact, not a manuscript,
review, or five-seat freeze. Existing proofs and accepted gate text are
preserved. The plan uses paper-plan claim/evidence mapping and the ARS
outline-only structure role; no outside model has reviewed this outline.

**Working title:** A least-monomer map on odd-cycle matchings and its interval fibres.

**One-sentence contribution:** For a specified least-monomer alternating-arc
update on all matchings of a labelled odd cycle, determine its single
recurrent rotor and classify every target's predecessors by intervals in a
forced dimer prefix, giving a triangular fibre formula with a unique maximum.

**Type:** short deductive finite-dynamics note with bounded exact controls.
**Venue:** unspecified; no ICLR/ICML/NeurIPS target is inferred.
**Planning envelope:** about 2400 words plus displayed proofs, targeting a
compact 6–8 page article including references; this is not a publisher limit.
**Authorship:** anonymous placeholder; no author identity, affiliation,
funding, or human-read declaration is invented.

`criteria_binding_unavailable`: the central mathematical contract is known,
but no author-confirmed venue/track review binding has been supplied.

## 1. Binding inputs and claim boundaries

Read inputs:

- `CMM_THEOREM_CONTRACT.md`, all sections;
- `COLLISION_FIREWALL.md`, including AP1/P90/GCM comparisons;
- `PRIMARY_SOURCE_SUPPLEMENT_20260905.md`;
- `verify_graph_matching_lane.py`, CMM definitions and complete CMM audit;
- `CANONICAL.txt`, complete transcript;
- `../../reviews/stage1_hostile_gate_algebra.md`, CMM rederivation,
  mandatory weakening, and reproducibility sections.

The existing gate's decision is **SELECT_INTERNAL_AMBER**, not external
owner clearance. It accepts only the conjunction of the least-monomer / next-
clockwise scheduler, the odd-cycle rotor splice, and the every-target
triangular interval atlas. It explicitly assigns no standalone credit to
augmentation, the deficiency clock, classical matching counts, the rotating
defect, Fibonacci/Lucas identities, or generic finite-map formulas.

No claim that this introduces a new matching algorithm, traffic model, or
unprecedented period is permitted. The missing historical P51–P56 manuscripts
remain a limitation. Future literal-owner evidence can reopen this slot.

## 2. Claims–evidence matrix

| Planned claim | Deductive evidence | Bounded evidence | Section / standing |
|---|---|---|---|
| The two-branch rule is a total self-map on all matchings of $C_{2m+1}$ | Between consecutive monomers the arc alternates; its flip removes exactly the endpoints. The single-monomer branch replaces the next dimer. | Author CMM audit exhausts every matching for odd $3\le n\le21$; independent gate reimplementation checks odd $3\le n\le17$. | §2; proved, classical local input credited |
| Exact point tail $m-|M|$ and one recurrent $n$-cycle, maximal tail only at the empty state | Each transient step adds one edge; every maximum matching is uniquely determined by its monomer, which advances by two. | Pointwise clocks, cycle decomposition, unique rotor, closure | §3; proved, not a standalone novelty claim |
| Every fibre has size $\binom{\lfloor u/2\rfloor+1}{2}+\mathbf1_{|Y|=m}$, with $u$ the least target monomer | Exhaustive predecessor bijection: one nonempty interval of the forced dimer prefix, plus the disjoint core predecessor | Every target including zero fibres and core/transient overlap | §4; principal inverse theorem |
| The maximum fibre is uniquely at monomer $n-1$, of size $1+\binom{m+1}{2}$ | The triangular term is increasing and only $u=2m$ yields prefix length $m$ | Unique maximum in every exact box | §4 corollary; sharp target classification |
| First image has size $F_{n-1}+F_{n-3}+2=L_{n-2}+2$ | Count targets matching vertices zero and one, then add the two excluded core targets | Every image size in transcript | §5; corollary of atlas, not independent axis |
| Complete depth polynomial from cycle matching numbers | Condition on the wrap edge to prove the classical coefficient count directly, then use the point clock | Every depth coefficient in CMM audit | §3 corollary; background census applied to this map |

The scout transcript's **2,508,857 assertions belong to the entire graph/
matching breadth program**, not CMM alone. Do not relabel that total as a
paper-local CMM assertion count. The independent gate reports 23,116 checks
for its separate CMM reimplementation. A future paper-local CMM verifier and
its own frozen count must be produced after the central freeze.

## 3. Planned structure

### Abstract, about 150 words, not drafted here

Lead with the specified scheduler and its targetwise inverse. Include the
single $n$-cycle, exact deficiency tail, and the displayed triangular fibre
formula only after defining the least unmatched vertex. Mention that the
result includes zero fibres and the unique maximizer. State exact enumeration
as bounded counterexample pressure, without a novelty superlative or a
matching-algorithm performance claim. A bilingual abstract can be planned
at the final writing stage without fabricating any scientific content.

### §1. The question and its background, about 400 words

**Purpose:** distinguish an exact inverse problem for a fixed deterministic
scheduler from the classical task of finding a maximum matching.

Open with the fact that augmenting paths explain rank increase but do not
specify the predecessor sets of a chosen scheduling rule. Describe the odd
cycle and the change from transient augmentation to a recurrent monomer
rotor. State the literal conjunction accepted by the gate, preview the fibre
formula, and explicitly credit classical augmentation and monomer/dimer
enumeration.

Place a compact related-work paragraph here: augmentation background via
Berge; perfect-matching alternating-cycle reconfiguration via Ito et al.;
one paragraph on the distinct scope of global least-label scheduling. Do not
pad a short proof note to a one-page literature section simply to meet an ML
conference template. Internal P90/GCM/AP1 subtraction belongs in the project
companion evidence and can be summarized without treating unpublished
catalog identifiers as conventional external citations.

**Sources:** verified Berge metadata; primary Ito et al. abstract; retained
collision firewall and independent gate for internal selection boundaries.
**Transition:** from the question to the exact two-branch update.

### §2. The labelled matching map, about 350 words

**Purpose:** define the carrier and rule without hidden choices.

Let $n=2m+1\ge3$, vertices $0,\ldots,n-1$, and $e_i=\{i,i+1\pmod n\}$.
A matching is an edge subset with no common endpoints. A monomer is an
unmatched vertex. Distinguish the ordinary least label from the cyclic order.
With at least three monomers flip the arc from the least monomer to its next
clockwise monomer; with exactly one flip its first two clockwise edges.

State a closure lemma with the explicit alternating pattern
$0,1,\ldots,0\mapsto1,0,\ldots,1$. The proof should state why internal
vertices cannot be matched outside their arc and why no wrap/tie case is
missing. The theorem assumes $n\ge3$; do not silently add the degenerate
one-vertex loop as another parameter case. Do not introduce the contract's
unreachable failure branch as a genuine branch in the mathematical map.

**Evidence:** contract §1–2; verifier `cycle_monomers` and `cmm_step`.
**Transition:** closure establishes the rank increase used in the temporal
classification, with no general matching theorem left as a black box.

### §3. Exact entry time and recurrent rotor, about 400 words

**Purpose:** give the complete temporal classification succinctly and credit
the elementary inputs.

Main temporal theorem: $\tau(M)=m-|M|$; the empty matching alone has tail
$m$; the $n$ maximum matchings form one directed $n$-cycle under monomer
advance $a\mapsto a+2$. The proof is rank increase followed by the coprime
rotor, not a new augmenting-path principle. Explain uniqueness of the maximum
matching for a prescribed monomer by removing that vertex and tiling the
remaining even path.

Give the depth polynomial as a corollary. A short self-contained background
count splits on the wrap edge: for rank $r$, the two counts are
$\binom{n-r}{r}$ and $\binom{n-r-1}{r-1}$, with the second zero at $r=0$.
Their sum is $n\binom{n-r}{r}/(n-r)$. Mark this static formula classical.

**Evidence:** contract §2 and gate cold rederivation.
**Transition:** the forward clock classifies when a state enters the rotor;
the next section independently reconstructs all states that enter a given
target in one step.

### §4. Prefix intervals give every predecessor, about 750 words

**Purpose:** carry the principal inverse theorem and its sharp extremality
without hiding parity or core-overlap cases.

For target $Y$, define $u$ as its least monomer and
$r=\lfloor u/2\rfloor$. Prove the forced prefix structure separately for
even and odd $u$. In the odd case the wrap dimer uses vertex zero; it is not
one of the $r$ reversible internal prefix dimers.

Every transient predecessor removes two target-matched endpoints $a<b<u$.
These were the first two monomers of its source. Hence its flipped target
segment is a nonempty consecutive block of the $r$ prefix dimers. Conversely,
flipping such a block backwards gives a valid source with precisely those
first two monomers, so the scheduler selects it. This is a bijection, not
only a bound. Count its intervals by $r(r+1)/2$.

Add exactly one disjoint predecessor when $Y$ is maximum: the rotor state
whose monomer is $u-2\pmod n$. Targets with $u=0$ or $1$ have no transient
predecessors, which explicitly handles zero fibres. Derive the unique fibre
maximum from $u=2m$. Include the $n=3$ boundary by direct inspection in one
sentence.

**Evidence:** contract §3, gate rederivation, all-target exact audit.
**Transition:** the fibre formula yields the first-image support, whose
size can be counted without further dynamics.

### §5. Image census, exact controls, and limits, about 500 words

**Purpose:** present the atlas consequences and distinguish proofs from
reproducibility checks.

For nonmaximum $Y$, image membership is equivalent to $u\ge2$, or both
vertices zero and one being matched. Split into presence of $e_0$ and presence
of both $e_{n-1}$ and $e_1$. Count remaining paths, then add core targets with
monomer zero or one. At $n=3$, the second edge pair is impossible: explain
this directly, then identify its count with $F_0=0$, rather than invoking a
path on a negative number of vertices.

Give one small exact table and a verifier-scope paragraph. End by stating
the limitations: only odd simple cycles, fixed numeric least-label scheduler,
no claim about arbitrary graphs or matching optimization, no independent
credit for static matching counts, and an explicit external owner hold.
No generic zeta function, orbit-count wrapper, or larger brute-force cutoff
is to be added merely to lengthen the note.

**Evidence:** contract §4–6, canonical transcript, independent gate.
**Transition:** finish with the precisely scoped conclusion and companion
reproducibility statement, not a broad novelty assertion.

## 4. Figure and table plan

One inverse diagram is useful because it makes seven predecessor branches
of one target materially easier to inspect. It is optional if it crowds the
short note; the exact table remains sufficient for computational reporting.

| Item | Planned content | Evidence source |
|---|---|---|
| Figure 1, vector schematic | On $C_7$, target edges $\{e_0,e_2,e_4\}$ with monomer six. Mark its three prefix dimers. Show the six nonempty dimer intervals and the separate rotor predecessor with monomer four, demonstrating why its fibre is $6+1=7$. No competing algorithm speed claim. | §4 bijection; construct directly from the literal rule and verify before rendering |
| Table 1, bounded exact atlas | Rows $n=3,7,11,15,21$; columns carrier, first image, recurrent states, maximum tail, maximum fibre | Existing `CANONICAL.txt`; later paper-local verifier must reproduce the same entries |

Proposed Figure 1 caption content: six transient predecessors are obtained by
reversing the nonempty intervals of the three forced prefix dimers; a seventh
predecessor belongs to the rotor. Edge status must be distinguished by solid/
dashed line style as well as color, so the figure is readable in grayscale.

Exact planned table rows:

| $n$ | Matchings | First image | Recurrent | Max tail | Max fibre |
|---:|---:|---:|---:|---:|---:|
| 3 | 4 | 3 | 3 | 1 | 2 |
| 7 | 29 | 13 | 7 | 3 | 7 |
| 11 | 199 | 78 | 11 | 5 | 16 |
| 15 | 1364 | 523 | 15 | 7 | 29 |
| 21 | 24476 | 9351 | 21 | 10 | 56 |

## 5. Citation and source-completion plan

1. **Berge background:** Claude Berge, *Two Theorems in Graph Theory*,
   Proceedings of the National Academy of Sciences 43(9) (1957), 842–844,
   DOI [10.1073/pnas.43.9.842](https://doi.org/10.1073/pnas.43.9.842).
   The official [PMC record](https://pmc.ncbi.nlm.nih.gov/articles/PMC534337/?page=-1)
   indexed metadata confirms this record. Direct DOI transport failed and
   PMC full-page access presents a browser check; no complete article read is
   claimed. The map's augmentation fact will be proved directly, so no
   unread theorem is used as an unsupported black box. Role: background.
2. **Reconfiguration neighbor:** Takehiro Ito, Naonori Kakimura, Naoyuki
   Kamiyama, Yusuke Kobayashi and Yoshio Okamoto,
   [*Shortest Reconfiguration of Perfect Matchings via Alternating Cycles*](https://arxiv.org/abs/1907.01700).
   Official abstract/metadata read. Its problem uses perfect matchings and
   alternating cycles, not CMM's rank-raising path scheduler on all matchings
   of an odd cycle. Journal DOI 10.1137/20M1364370 is recorded there; verify
   complete publication metadata before emitting a final journal BibTeX.
   Role: scope comparison, abstract-bounded.
3. **Internal adjacency:** retain project evidence for P90/GCM/AP1 in the
   claims/evidence and review packages. Do not turn unpublished internal
   identifiers into invented public sources. Role: opposes overbroad novelty
   framing and constrains the contribution.

No bibliography entry will be synthesized from memory. The source
supplement's older access failures are historical evidence and should not
be erased; any later successful full-text access is an additive dated delta.

## 6. Review state and writing handoff

Existing Stage-1 hostile feedback is accepted with the narrow contribution
wording above. No review of this new outline has been performed and no
external GPT-5.4 call is implied by using the paper-plan skill. Later paper
Review A/B must be process-separated from author drafting; this author lane
will not review its own CMM or period-feedback manuscript.

After the root explicitly freezes exactly five seats:

- create the numbered anonymous manuscript only in the root-assigned path;
- extract a paper-local dependency-free CMM verifier, preserving the original
  multi-candidate scout and its 2,508,857-assertion transcript unchanged;
- freeze that verifier's own stdout and replay it;
- draft the five sections with main-text proofs and the explicit background
  subtraction, with no evidence inflation;
- arrange the separate reviews, accepted deltas, two cold builds and visual
  QA under the root workflow;
- carry an honest data/code availability statement and AI-use disclosure;
  author contributions, conflicts and funding remain author-owned and must
  not be fabricated for an anonymous internal note.

The next action in this lane is awaiting that **root freeze**, not a routine
user confirmation and not permission inferred from an outline file.
