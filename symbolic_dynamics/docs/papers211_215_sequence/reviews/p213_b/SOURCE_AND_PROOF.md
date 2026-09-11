# P213 B deductive and source review — source-preparation stage

2026-09-11 UTC. Reviewer /root/p213_manuscript_review_b. First scientific
input: physical frozen_round1, manifest cd24d1ae5960456a7ed29978c9dbfac9794243b6bb913f19c6de1fb47d7479ce.
No prior proof, manuscript or verifier contribution and no prior candidate
familiarity. Familiarity acquired here: full frozen manuscript TeX and proof
package, authorship, source audit, references, scope and contracts; full UUC
and MNA proof bodies; initial 80 author-verifier lines and initial 100 A
verifier lines, solely to establish representation independence. These code
reads are disclosed, not a blind review. No code or results were copied,
imported, executed or adopted. A's root acceptance was read as lifecycle
evidence, not a substitute for this review. A canonical was not read.

The project symbolic-dynamics-research and research-review skills govern.
This is actual process-separated current-model review, not an external
specialist or cross-model review. The generic provider/model/panel instructions
are overridden by project scope. No children were created. Both named
authors and A are different processes and ineligible for this B role.
SOURCE_ONLY is not a final manuscript verdict, accepted delta, Round2 or
completion. No PDF build or actual visual inspection has occurred in B.

## C1: independent deductive attack

The nonnegative carrier includes n=1, n=2 and N=0. A synchronous old-state
current cannot exceed its sender, so closure is immediate, and each edge's
outflow is the next site's inflow. Adding c to every coordinate adds c to
every current, which cancels in the increment. At a zero both incident
currents vanish. Applied after subtracting the minimum, these facts establish
exact minimum invariance; mere monotonicity would not suffice for the later
uniform-target argument.

Within one original residual run, a positive coordinate with a positive
predecessor has positive next inflow and cannot vanish. Only its head can
vanish, and the old right endpoint never moves because its next site is
permanently zero. While at least two sites remain, that endpoint gains an
integer at least one. It is bounded by the original interval's conserved
mass. Consequently there is a finite time when only this endpoint survives,
and its value is exactly the original run sum. This rules out both an
internally split run and a hidden recurrent orbit. Isolated residual spikes
give zero residual currents and hence all fixed states. Uniform residual
zero is handled without choosing a nonexistent run.

For n=1 each edge is self-returning; for n=2 the opposite currents coincide.
The isolated-residual criterion still describes all states on these small
carriers: on two sites at least one residual coordinate is zero. The clock
is zero, including all N, rather than an erroneous N-1 extrapolation.
For n=3 the residual has a zero and therefore each nontrivial run has two
sites. Its receiver recursion is B' = min(2B,A+B); the sender is the remaining
mass, including saturation. The least t with 2^t B >= A+B yields the stated
upper bound, attained with B=1 and total residual N. N=1 gives time zero.
For n>=4, each endpoint grows for at most M-b <= N-1 nonfixed updates.
The witness (N-2,1,1,0,...) keeps its middle coordinate one for N-2 updates;
the next update removes that coordinate. This gives N-1, not N-2. N=2 uses
a two-site unit pair; N=0 and N=1 are separate fixed cases. This is a sharp
worst-carrier clock, not a pointwise clock for arbitrary n>=4.

## C2: full inverse, including empty words and integrality

I rederived the four local table equations directly from incoming/outgoing
minima. In order (s_previous,s_current) = 01,11,00,10, they are a_i,
a_previous, 2a_i-a_next, and a_i+a_previous-a_next. Equality has only bit 1.
A cyclic strict descent everywhere is impossible. Weak ascent everywhere
forces a constant vector, giving a singleton only for a uniform target.

For a mixed word each valley is fixed by y_v. Descending interior coordinates
are uniquely determined, backwards, by twice the coordinate equal to its
target plus the next coordinate. A nonintegral numerator cannot be repaired
by choosing another peak, because the entire descent interior is already
anchored by the next valley. Negative or nonstrict values also genuinely
exclude the word. There is no descent interior when d=1; its right neighbor
is the next valley. These are iff tests, not merely necessary heuristics.

For r=1 the prepeak is the valley itself, so the peak equation gives a unique
peak. Both comparisons must be checked: weak ascent into it and strict
descent out. These imply its nonnegativity. For r>=2 the ascending interior
equations shift the target back one place. Agreement at the valley gives
y_(v+1)=y_v; the remaining forced ascent comparisons give exactly the stated
order chain. For r=2 this chain is vacuous, but the equality is not.

The two remaining variables have sum S=y_p+A_(p+1). If t is the prepeak,
its left neighbor gives t>=y_(p-1); the allowed prepeak/peak tie gives
2t<=S; the STRICT peak descent gives t<=y_p-1. The latter subtracts an
integer one, not an index. Hence the asserted closed integer interval is
exact. Odd S causes flooring, not rejection: only descent-interior division
requires even numerators. When the upper bound is below the lower bound,
there is no solution; omission of the strict upper bound would create false
sources at ties with the descent neighbor.

Each block's free pair is disjoint from every other block's free pair.
The remaining coordinate roles partition the cycle, with only the already
checked redundant valley assignment on a longer ascent. Thus satisfying
every forced test and choosing one value in every nonempty interval solves
EVERY local equation with precisely the declared word. Summing these local
equations telescopes to source mass = target mass, so no separate hidden
mass constraint couples the intervals. This also proves that every failed
test or empty interval excludes all sources, even in an empty chamber not
sampled in a finite check. Conversely each actual source forces precisely
those choices. Distinct words cannot share a source and distinct parameter
tuples differ at a prepeak coordinate. This proves the full image iff and
source-set equality, not merely total counts. Cyclic wraparound introduces
no new equation or rotation quotient.

At most n coordinates/tests and product operations occur per mixed word.
The O(n 2^n) statement counts arithmetic operations, not bit complexity or
the time to print the potentially much larger collection of sources.
No defect identified in the evaluated formula or its proof.

## C3: fixed fibres and exponent

A source with a fixed output has the same minimum. Every nonempty residual
source run keeps its endpoint and loses at most one site in one step; since
the output consists of isolated spikes, each source run has length one or
two. Every output spike comes from such an endpoint. With only one target
zero before a spike, a proposed extra head would have a source-positive
predecessor (the preceding target spike), so it cannot disappear. With at
least two target zeros, exactly h=0,...,floor(p/2) is possible. The extra
heads are disjoint and separated, including across the last/first gap.
The sole-spike convention d=n-1 gives the correct n=2 singleton fibre and
n>=3 split family. The uniform target has unique source by minimum and
mass, not by a false assumption that all fixed targets have unique sources.

Each free interval consumes a distinct ascent run of at least two edges
and its following nonempty descent run. These blocks are disjoint, giving
at most floor(n/3) factors. For a positive word, sufficiency already proved
every source coordinate <=N; thus each interval has at most N+1 values.
This logical ordering avoids assuming a mass bound before proving automatic
mass. The constant-word contribution and all mixed words give the upper
bound also at N=0. For n>=3, k>=1; k spikes at cyclic separation at least
three exist because 3k<=n. At N>=2k, q=floor(N/(2k))>=1, ensuring all
spikes are genuinely positive; allocating the residual mass to one spike
does not lower any factor. The product is at least (q+1)^k and hence the
stated real lower bound. These are all-parameter arguments; no finite
N=0..4 run establishes the asymptotic exponent. Exact finite maxima and
all maximizers remain excluded. No defect identified.

## Source deduction and primary-source contexts

Full local original proof reads: UUC at
docs/papers211_215_sequence/scouting/transport_lane/PROOF_PACKAGE.md and MNA at
docs/papers204_208_sequence/scouting/finite_systems_fortieth/MNA_PROOF.md.
UUC uses the binary indicator 1{0<x_i<=x_(i+1)}: its permanent zeros,
quadratic-energy recurrence exclusion and generic current-word feasibility
are deducted. It does not provide this mass-valued current's evaluated
interval atlas or endpoint clock. MNA acts on positive compositions by
merging maximal weakly increasing runs and changes the number of parts.
Its deleted-cut permanence, triangular delayed-merger mass bound, increasing
refinements and threshold inverse are deducted. Neither literal distinction
proves nonconjugacy under arbitrary encodings. No full internal archive scan
or global no-owner statement is made. P211's corrected finite-chain label
is retained; I did not independently review P211/P212 manuscripts here.

Fresh public primary-source reads on 2026-09-11 (text extraction, not PDF
page viewing):

- Boccara–Fuks, https://arxiv.org/pdf/adap-org/9905004: definition and Theorem
  2.1, extracted lines 91–127; a finite-alphabet conservation criterion,
  with a zero-padding necessity proof and telescoping sufficiency. This
  supports the background attribution, not P213's inverse or clock. The
  PDF template year is not used as publication metadata.
- Nishinari–Takahashi, https://hakotama.jp/laboratory/works/public/98nt.pdf:
  equations (16), (21), extracted lines 219–283 and 318–342. The current
  includes L minus the receiver and optionally M; L<=M removes M, not the
  vacancy. Thus the manuscript's literal comparison is supported. No
  Cole–Hopf transfer or all-encoding exclusion follows.
- Fukuda–Segawa–Watanabe, https://arxiv.org/html/2104.14009v2: equations
  (15)–(17), extracted lines 147–184. The vacancy term and an evolving V
  field are explicit. This is the earlier v2 formulation, not a read of
  the published 2023 full body. The published/preprint title distinction
  is correctly stated in the frozen audit. Bibliographic publication
  metadata closure is inherited from accepted A/root, not freshly claimed
  as an independent B publisher-metadata retrieval.

Conservation, zero barriers, ordered chambers, dyadic arithmetic, ordinary
interval products and packing earn no independent novelty credit. After
these deductions, the specific complete endpoint/worst-clock and evaluated
all-target inverse/degree conjunction remains a coherent narrow short note.
This is not a top-venue endorsement, ownership certificate or broad priority
survey. No bibliography/source overstatement identified at this scope.

## Verifier independence and finite limitations

The new B source enumerates sorted multisets of particle locations, moves
particles by their OLD receiver's population, inverts the entire relation,
and builds increasing reachability layers from fixed states. It neither
enumerates inverse currents nor peels indegrees. It does not implement the
author's backwards atlas solver. Every target/word, including both constants
and every empty chamber, is checked against the four declarative local
equations over the complete carrier. Every nonempty mixed chamber is further
tested for forced-coordinate constancy, exact prepeak bounds, projection
injectivity and Cartesian surjectivity. This tests complete source sets,
not only aggregate counts. Empty chambers are explicitly emitted; their
general forced rejection characterization is audited deductively above,
not inferred from observed nonempty chambers. Root explicitly accepted this
representation scope before source handoff, without granting execution.

The token oracle and equation-table checker share only the mathematical
literal. The terminal formula routes each residual site's units separately
to the predecessor of its next zero; layer-derived terminal states and
times are independent observations to be compared. Fixed-target products,
uniform/short-cycle boundaries, saturation and finite bound witnesses are
also checked. Runtime and tests are still unexecuted. This source review
finds zero mathematical/source Critical, Major or Minor defects, but does
not assert a final zero-open artifact census: science, replay pair, build,
all-page views and exact final delta are unfinished obligations.
