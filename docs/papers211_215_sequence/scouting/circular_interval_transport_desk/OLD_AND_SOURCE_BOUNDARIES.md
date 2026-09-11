# Exact old/source boundaries

## 1. Historical literals: read originals, not recovery prose

The seven selected complete files are frozen by `capture.py collect`. The
read scope of the scientific originals is intentionally narrower than the
complete byte-copy scope. A physical copy/hash is not a claim to have read
or independently re-proved every theorem in that file.

1. **P198, least-monomer cycle matching.** In
   `papers/198-cyclic-monomer-matching/main.tex`, lines 73–205 were read.
   For `n=2m+1`, the carrier is all matchings of the labelled cycle. With at
   least three monomers, take the least monomer `a` and its next clockwise
   monomer `b` and flip the whole alternating `a`–`b` arc. With one monomer,
   flip the next two edges. The original gives exact deficiency clock
   `m-|M|`, the maximum-matching rotor, and prefix-interval predecessors.
   This is an existing rejected numbered manuscript, not a new acceptance.
   Its rank-gain/interval-surgery engine is not fresh coupled transport here.

2. **MRT, ordered involution transport.** The entire
   `docs/papers204_208_sequence/scouting/finite_systems_thirtieth/PROOF_PACKAGE.md`
   was read. Its literal `(a,b) -> (bab,aba)` becomes
   `(a,r) -> (a r^2,r^-3)` for `r=ab`. Its full ordered iterate, clock and
   period are reduced to the prior sandwich rule plus a commuting swap.
   The original explicitly preserves the orientation correction, rather
   than treating the product factor alone as the entire dynamics. This
   forbids recycling labelled edge transport implemented by these exact
   conjugations; it does not forbid all matching rewiring.

3. **OMD and HUR.** In
   `docs/papers162_166_sequence/scouting/replacement_matchings_incidence/SCOUT.md`,
   lines 17–45 and 82–89 were read. OMD is `M -> M F M` for fixed matching
   involution `F`, and the old identity is `F T^t(M)=(F M)^(2^t)`.
   HUR is `(A,B) -> (B,BAB)`, the old Hurwitz-action entrance. The old
   recorded experiments are neither reproduced nor independently endorsed
   by the present documentary check.

4. **UUC.** Both `transport_lane/INTAKE.md` and
   `transport_lane/PROOF_PACKAGE.md` under the current batch were read in
   full. On cyclic nonnegative mass compositions, the literal currents are
   `g_i=1_{0<x_i<=x_(i+1)}`, with output `x_i-g_i+g_(i-1)`.
   The original proof provides increasing quadratic energy and the generic
   binary-current reconstruction `x_i=y_i+b_i-b_(i-1)`. Neither a new sharp
   resource clock nor an evaluated residual inverse extremum is present.
   This exact comparison-current variant is not nominated again.

5. **Old planar desk.** The full current-batch
   `planar_matching_lane/HANDOFF.md` and `PROOF_PACKAGE.md` were read. The
   handoff identifies previously excluded component sections, Dyck
   reassociation, summit erosion, regular-star folds and geometric
   relabelling. Its full regular-star argument gives `(x x*)^2=x x*` under
   explicitly stated identities, and its finite-bijection fact has singleton
   fibres. The other named originals in that handoff were not reread here;
   those names are retrieval exclusions, not independent theorem premises.
   We do not extend the fold statement to arbitrary diagram powers or
   multiplication. This new desk does not reopen that old planar desk.

The earlier `fresh_geometry_automata/SCOUT_AND_KILL_LEDGER.md` was also read
as a discovery guide. It contributes no positive or negative theorem premise
to this handoff and is not a pinned dependency. Mutable central indexes were
used for orientation only, not copied as a proof of current milestone.

## 2. Primary source map and bounded reading

### S1 — periodic box-ball transport

Jun Mada, Makoto Idzumi and Tetsuji Tokihiro, *On the initial value problem of
a periodic box-ball system*, [arXiv:nlin/0608037v1](https://arxiv.org/html/nlin/0608037),
16 August 2006. This is identified here as the directly read author preprint;
no journal metadata is inferred.

Actual browser body lines 18–143 were read, covering the complete literal,
the elimination/reinsertion coordinates, Theorem 1, Proposition 1 and
Theorem 2. The finite carrier has `N` labelled cyclic sites, binary entries
and exactly `M < N/2` occupied sites. Repeatedly pair each currently adjacent
unpaired `10`, ignoring earlier pairs, until all ones are paired; exchange
the two entries at every resulting arc. The article's coordinate construction
uses conserved elimination levels, zero-soliton insertion positions and a
reference shift. Proposition 1 contains explicit recursive floor formulas
for the time-dependent coordinates, and Theorem 2 states the initial-value
solution. This source directly blocks presenting that literal or those
coordinates as this desk's new theorem.

Limits: the earlier reference supporting Proposition 1 was not opened and
its full proof is not independently checked here. The later numerical example,
all period-distribution results and higher-capacity variants are not imported.
The OUP finite-carrier source appeared in search but was not relied upon as
a proved periodic-carrier theorem. No complete finite box was executed.

### S2 — published noncrossing-partition toggles

David Einstein, Miriam Farber, Emily Gunawan, Michael Joseph, Matthew
Macauley, James Propp and Simon Rubinstein-Salzedo, *Noncrossing Partitions,
Toggles, and Homomesies*, Electronic Journal of Combinatorics 23(3) (2016),
P3.52, [DOI 10.37236/5648](https://doi.org/10.37236/5648),
[publisher PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i3p52/pdf/).

The publisher metadata and PDF-extracted body through Definition 2.1 and the
following involution statement were read, including the distinct arc and
block representations (PDF pages 1–5). The map on `NC(n)` removes a selected
arc if present; otherwise it adds that arc only when the result still belongs
to `NC(n)`. This is not silently converted into a fixed-cardinality perfect
matching carrier. Any fixed word of these already-defined involutions has
the reverse word as inverse; that observation alone is not a new inverse
mechanism. We do not assert that all toggle words are conjugate to rotation
or that the source classifies all their periods or all independent orbit
statistics. Later displayed text was not used for such claims.

The arXiv HTML route returned 404 before the publisher PDF succeeded. No
local PDF or PDF structural-preflight claim is made: this was the browser's
PDF text, without a visual page review.

### S3/S4 — fixed-cut interval translations and rational reduction

Hideyuki Suzuki, Shunji Ito and Kazuyuki Aihara, *Double rotations*,
[institutional technical report METR 2003-13](https://www.keisu.t.u-tokyo.ac.jp/data/2003/METR03-13.pdf).
H. Bruin and G. Clack, *Inducing and unique ergodicity of double rotations*,
[author institutional manuscript](https://www.mat.univie.ac.at/~bruin/papers/DoubleRotations.pdf),
version dated 20 October 2011 in the read file.

The Suzuki–Ito–Aihara introduction gives
`f(x)={x+alpha}` on `[0,c)` and `f(x)={x+beta}` on `[c,1)`.
The same precise half-open definition is independently displayed by
Bruin–Clack, Section 2. For integers `0<=A,B,C<q`, the grid embedding
`i -> i/q` takes the finite restriction to
`i -> i+A (mod q)` for `i<C`, and `i -> i+B (mod q)` otherwise.
This is a direct specialization of the existing definition, **not a new
literal nomination**. The cut/translation parameters are fixed; there is
no state-dependent motion of a pair of interval boundaries in this carrier.

Suzuki–Ito–Aihara Proposition 6.3 and its proof were read in the browser
PDF text at lines 1855–1868, followed by the complete Theorem 6.1 statement
and proof at 1870–1882. The rational case is reduced by strictly decreasing
positive integer denominators in their induction. Their continuum
finite-type conclusion is not conflated with an exact sharp all-grid
transient clock or all-target discrete inverse extremum. The preceding
rank-two proof and all technical induction dependencies were not fully
reaudited. Bruin–Clack's first two PDF pages were read for definition and
scope only; the later almost-everywhere/fractal/ergodicity proofs were not.
Search-engine apparent recency is not used as publication dating.

### S5 — recent rational Catalan pointer, not an imported proof

Keiichi Shigechi, *Promotion and rowmotion in rational Catalan combinatorics*,
[arXiv:2603.17402v1](https://arxiv.org/html/2603.17402v1), version identifier
dated 18 March 2026. The rendered body also displays 24 August 2026; that
display is not treated as a new version or publication date.

The abstract, rational-Dyck carrier, promotion/toggle discussion and Theorem
7.12 statement were read. The paper explicitly treats the four actions as
bijections and states a matching-map intertwining relation between rowmotion
and inverse promotion. This is only a recent adjacent-source warning:
neither its full proof, every matching-map definition, nor an all-parameter
period classification was audited here. Some browser locations landed in
unrendered diagram code; those passages are not claimed as visually read.
No conclusion of this desk depends on treating this preprint's theorem as
proved. It is not a basis for asserting every rational-Catalan action is a
simple rotation.

Striker–Williams appeared in primary abstract/publisher search results and
the author's website. The attempted full-body routes failed; its detailed
equivariant theorem is not imported as an independently read proof here.

## 3. Source-verification scope

All claimed literal definitions above are grounded in direct primary bodies.
The double-rotation definition was checked in two independent author sources;
the toggle item's title/authors/year were checked in publisher metadata and
its primary body. No secondary index or search non-hit establishes novelty.
For these theoretical sources the relevant evidence is the exact definition
and deductive statement, not an empirical-study pyramid level; the latter is
not applicable. S1/S3/S4/S5 are treated as author/institutional preprints or
technical reports here; only S2's publisher record establishes its journal
publication status in this desk.

Fitness for the limited definition/ownership observation is direct-primary;
fitness for uninspected stronger proofs is **not established**. No complete
Scopus/WoS/DOAJ/Cabell's check, retraction search, ORCID/affiliation audit or
financial/personal conflict-of-interest assessment was performed. Those
fields are unassessed, not clean. No arbitrary A-grade or novelty certificate
is minted from successful browsing. Optional ARS bibliographic API clients
and all external-model uploads remained off under the batch contract.
