# P212 nonauthor B — source and deductive audit

Status: SOURCE_REVIEW_READY / SCIENTIFIC_EXECUTION_AND_BUILD_PENDING.
No Critical, Major or Minor manuscript defect is identified in this source
phase. This is not a final Review B verdict, finite-computation PASS, canonical,
strict pair, new page-view report or paper completion.

## Independence and physical input

Reviewer: `/root/p213_manuscript_review_b`, assigned by root as P212 B.
I contributed no P212 proof, manuscript or scientific verifier before this
assignment. Earlier P212 work was bounded dependency/DATA infrastructure
auditing, not mathematical authorship. P213 and fresh55/P214 work is unrelated
to the P212 proof. No child agent was used. This is process-separated current-
model review, not external, cross-model or specialist review.

The scientific manuscript input is the actual root-accepted physical
`papers/212-closed-pointer-orbits/frozen_round1`, whose 25-payload manifest is
1c6993c46eb9e7db32c098e6db60411b60292685f25a6987193c213d91af7cf7.
INPUT_PINS.sha256 binds all 25 payloads and that manifest; unchanged
author/A source is only read for understanding and independence subtraction.
No frozen or live author file, central state, old review, failed evidence or
Git reference was modified. The 12,501,943-byte author canonical is pinned,
not imported as a B computation or newly claimed as independently reconstructed.
The frozen PDF is pinned but has not been visually inspected by B in this
source phase. The separately authorized fresh B build and every actual new
page remain mandatory later.

I read the full paper-local proof, all eight TeX/Bib source files, full source
audit, claim/evidence document, narrative, plan, README, parameters, output
plan/schema, FREEZE_SCOPE and four included author evidence receipts. I read
the full author verifier and full A verifier and A source/proof report for
subtraction, not reuse. A's FINDINGS_FINAL.json is authoritative for its
current zero findings; the historical M1 locator issue and initial01 timing
caveat are preserved, not silently reclassified. The contract and project
proof/artifact/review boundaries control the scope.

## Deductive audit: invariant reduction

Substituting `(g(a),a,g[a:=b])` into the update recovers `(a,b,g)` even when
registers coincide. This proves permutation status without a graph pilot.
Exactly the old extra edge is reversed and exchanges storage/extra roles
with the old edge leaving v, so the complete undirected multiset is invariant.
Stored functional components have equal edge and vertex counts; joining two
by one register edge or adding that edge internally produces excess one in
the active component. Inactive components have no register.

At a leaf of the active graph, the unique incidence must be the vertex's
stored outgoing edge. It cannot carry the active register, which has two
outgoing incidences, including the loop-degree convention. Deleting that leaf
does not remove an outgoing edge of another retained vertex. Induction leaves
both registers and freezes all deleted outgoing pointers. The resulting
connected core has s+1 edges and minimum degree two. Degree excess is two,
forcing either one degree-four branch or two degree-three branches. Contracting
degree-two chains yields precisely figure-eight, barbell or theta, including
loops and parallel edges. No extra recurrent type is missing.

Conversely an arbitrary complementary map either feeds a tree into the core
or eventually cycles wholly outside it. It cannot both join an outside cycle
and subsequently reach the core. Thus every such map is permissible, adds no
active core edge, and remains frozen. Recovering the actual core-label set
and the actual complementary map is unique, not an isomorphism quotient.

## Deductive audit: all seven minimal-period rows

A chain's old stored arrow is the unique continuation of an arrival at an
internal degree-two vertex; the incoming arrow is stored in reverse. Hence
traversal and reversal, including the endpoint roles, are forced. Internal
starting states reach a branch and the stated anchors. This also supplies
exhaustion: classification is not inferred from a total state count.

For a figure-eight anchor, the two cycles alternate. A block of length a+b
returns to the chosen-cycle anchor and reverses both observable orientations.
Length-one/two cycles have no observable reversal bit; a longer labelled cycle
does. Distinct cycle first destinations exclude an earlier branch return
except for the separately fixed double loop. If either cycle is long, a
specified ordered departure at one of its internal vertices occurs exactly
once in the twice-traversed block. A proper period would repeat that ordered
departure, so the full 2(a+b) is minimal. The joint-reversal quotient of the
two actual orientation sets has two classes exactly when both are long.

For a barbell anchor, the directed bridge departure at the smaller branch
recurs only after the block bridge/B-cycle/reverse-bridge/A-cycle. Its length
is a+b+2c and both cycle orientations reverse. Bridge and cycle departure
destinations differ even for loops or double cycles. Therefore its first
return is that block when both reversals are invisible and two blocks
otherwise; the same joint-reversal decoration quotient is complete.

For theta, one chain traversal changes roles (i,j,k) to (k,i,j) at the other
branch. Six traversals use every path both ways and restore the state.
Any nondirect path supplies a uniquely occurring ordered internal departure,
so period is 2(a+b+c). Three direct paths instead have no identities and
only two register states, giving period two. At a fixed branch the role
triples are quotiented by cyclic rotation. Three distinguishable tokens give
two classes; two identical empty/direct tokens identify those classes.
Nondirect tokens cannot coincide because their labelled internal sets are
nonempty and disjoint. This closes all degenerations, not only generic cores.

The both-long figure-eight/barbell and all-nondirect theta proofs work without
size bounds. They first need s=5,6,5 respectively and are not finitely exercised
by the n<=4 checker. No enlargement is proposed to disguise that limitation.

## Deductive audit: period set and sharp witnesses

For a core on s labels, the short barbell has period at most 2s and its odd
period is 2s-1; the other odd possibilities are one and three. Long figure-eight
and theta periods are 2s+2, and long barbell periods are at most 4s-4.
Together with the small n=1,2 cases this excludes every period outside the
claimed interval and even tail.

The manuscript's short barbells realize all even periods 4..2n and odd
periods 5..2n-1; the double loop, triple-direct theta and (1,2) figure-eight
supply 1,2,3. Theta (1,1,s-1) supplies the needed initial even tail. For the
remaining half-period k, c=max(1,k-n-1) and r=k-2c give r>=4 and a legal
barbell (1,r-1,c) of size at most n. The two cases k<=n+2 and k>n+2 verify
the size inequality explicitly. The stated sharp n=2, n=3 and n>=4 witnesses
therefore work, with inactive loops as padding. No asymptotic bound is being
substituted for exact attainment.

## Deductive audit: decoration weights and rational census

For a rooted cycle, reversal identifies two ordered internal-label lists
only when there are at least two internal labels. Thus the cycle weights are
1,1,1/2 for lengths one, two, and at least three. Multiplying by the actual
joint-reversal class count gives weight one for two short cycles and one-half
otherwise. Figure-eight interchange is free except for two loops; barbell
endpoint interchange is always free because its two branch labels differ.
These facts give exactly the displayed exceptional short terms and the
nonshort D terms, with no hidden labelled-edge factorial.

Theta's unordered endpoint pair has weight t^2/2. For k=1,2,3 nondirect
paths the internal-label set partitions have weight Q^k/k!, and decoration
multipliers 1,2,2 give Q+Q^2+Q^3/3. The all-direct q^2 exception replaces
the generic q^6 baseline rather than being counted twice. This establishes
each rational piece and the all-period interpretation of q.

Choosing the labelled core subset, then its orbit, then the full frozen
complement gives binomial(n,s)*s!*n^(n-s) extensions of an EGF coefficient.
The inverse recovery above establishes a bijection on orbits. This is stronger
than equal-period timing: the stated length pairs (1,5) and (3,3), on five
labels, have equal period twelve but one versus two classes per fixed core.
The two axes share their return map and are not claimed logically disjoint.

For a separate algebra check, D=(2x^2-x^4)/(1-x)^2 and
Q+Q^2+Q^3/3=(x-x^2+x^3/3)/(1-x)^3. These give the submitted integer
denominator recurrences directly. At q=1, the common numerator is
t-t^2+t^4/2-t^5/12. The binomial-coefficient expansion yields 1 and 2
at s=1,2, then (5s^2+s+24)/24, including the separately checked s=3,4.
The formal weighted derivative gives s^2(s+1)/2. The fixed-point count and
fixed-iterate divisor sum are standard consequences, credited as such.

## Primary literature: fresh bounded body reads

The following are my own source reads for this review. No entire literature
corpus, generic no-factor theorem or global novelty certificate is claimed.
The precise fetch/extraction provenance is in SOURCE_FETCH_PROVENANCE.md.

- [Manna–Waldinger, AAAI 1987](https://cdn.aaai.org/AAAI/1987/AAAI87-028.pdf):
  title/authors and complete nrev/nrev2 passage with its input conditions,
  PDF page 5 / printed 159, extracted lines 384–445. Previous/current reversal
  is established; removing initialization/stopping is not kernel invention.
- [Loginov–Reps–Sagiv](https://research.cs.wisc.edu/wpis/papers/festschrift4444.pdf):
  title/authors plus complete extracted PDF pages 14–15 and 19–20, including
  Figure 8, Section 5, formulas (8)–(9) and the full visit-monitor termination
  argument. The initialized NULL-terminated program restores a twice-visited
  handle. These parts do not assert arbitrary nil-free closed-state orbit
  counts. Browser body/screenshot failures were resolved by an actual direct
  download and ordinary extraction, not by rephrasing the inherited audit.
- [Berdine et al., CAV 2006](https://jberdine.github.io/pub/2006_cav.pdf):
  title/authors and complete Example 8 explanatory paragraph, lines 665–679,
  PDF page 13. Its decreasing quantity 2i+j+k and twice-traversed handle
  are owned; its analyzer's reported limitation is not evidence of novelty.
- [Holroyd et al.](https://arxiv.org/pdf/0801.3306): title/authors, Definition
  3.1 through Theorem 3.8 and the complete Lemma 4.9/Corollary 4.10 proofs,
  lines 523–612 and 1177–1226. Fixed cyclic rotor orders and recurrent
  unicycles, Euler tours and their tree correspondence are correctly credited.
  The corrected Eulerian locator really is Lemma 4.9, not Theorem 3.8.
- [Pham, v8](https://arxiv.org/pdf/1403.5875v8): title/version, model,
  Theorem 1, loops/multiedges conventions and full proof through its Eulerian
  discussion, lines 24–35, 62–73, 105–127 and 263–329. The full strongly
  connected fixed-digraph orbit formula, not only the Eulerian case, is
  credited. This result fixes common orbit size and count, not membership
  under changing cyclic orders.

The [Springer volume page](https://link.springer.com/book/10.1007/978-3-540-71322-7)
was also opened to check the Loginov volume attribution; no unavailable
chapter pagination was inserted. The downloaded Loginov PDF's first-page
title/authors agree with the bibliography. The Holroyd live PDF is arXiv v4
(2013 revision); the bibliography's 2008 key is the original preprint year,
not an assertion that this fetched revision was released in 2008.

For the natural loop-free (3,3,1) barbell, the pointer period is sixteen;
the same bidirected Eulerian core has fourteen arcs and rotor period fourteen.
This excludes that particular same-core time-preserving identification.
It does not exclude other graphs, encodings, suspensions or factors. The
manuscript preserves this exact modest boundary.

I also read P167 main.tex lines 1–190 (literal map and main theorem, not its
full 385-line paper) and P209 PROOF_PACKAGE.md lines 1–145 (literal map,
theorem statements and beginning of proof). P167's full map is nonbijective
with transients and recurrent periods at most two. Independently at n=2,
P209 maps both (0,0) and (1,0) to (1,0), from its displayed fibre-threading
rule. These suffice to separate those full maps from this permutation, not
to exclude every possible restriction, factor or enlarged representation.
I do not repeat the old P167 excerpt-as-full-file claim.

## Implementation separation and pending evidence

Author: forward literal graph, edge-multiplicity compositions, direct
chain/anchor constructors, Fraction generating series. A: two slot swaps,
subset/core construction, path-list catalogue, primitive visit words with
last-arrival reconstruction, length-parameter scaled sums. B: arithmetic
inverse graph/DSU, Prüfer-tree/two-cotree catalogue, global degree-two edge
contraction, exhaustive static destination assignments, and denominator
recurrences. Zero-based little-endian encoding is shared with A and is not
itself counted as a distinct scientific idea. All three necessarily use the
same literal carrier and theorem statement. No author/A scientific code is
imported, copied as B implementation, or executed by this source phase.

The B finite design tests complete class-to-orbit sets and all fixed complement
keys, not only orbit totals. Its own shared anchor decoder is disclosed in
OUTPUT_PLAN.md. Deductive coverage independently handles the unreachable
5/6/5 cases. I have not run or parsed this proposed code; syntax, runtime,
all-field output reception, exclusive canonical adoption, strict pair, fresh
build and every actual page view remain pending root's separate gates.

The project research/proof/review skills supplied these proof-first and
evidence boundaries. No unavailable-provider result or extra review panel
was substituted. This package alone authorizes no scientific invocation or
manuscript change. Provisional manuscript delta is empty, subject to the
required later B evidence. OWNER_AMBER / HOLD_EXTERNAL.
