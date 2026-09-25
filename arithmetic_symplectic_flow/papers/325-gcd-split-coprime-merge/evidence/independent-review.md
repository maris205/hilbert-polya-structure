# Independent internal review — 325

Candidate: `ANG-20260920-GSM01`.
Status: `OWNED REWRITE CLOCK; REPEATED PRIME-2 PACKETS — STOP / FORK`.
Final finding: no manuscript correction required; the fixed-packet multiplicity gate fails.
Calibration: `NOT_CALIBRATED`. This is inherited-model/shared-context internal review,
not external peer review, cross-model verification or independent-error evidence.

## 1. Input locks, actual access and version influence

| Input | Personally accessed scope | SHA-256 |
| --- | --- | --- |
| [Original card](../candidate-card.md) | Entire original 149-line prefix through its original EOF, before mathematical raw submission | `3874276bd629060b23bec238a267848936a521a056bb4bf4c5ce489b6c864435` |
| Author's first draft | 317 lines, author-reported lock only; **not personally read** | `2a6a9b45d80461a8c1366bf416a4fb7bd1fbfa95d10f55ff6bf902986950ebb0` |
| [Released manuscript](../paper.md) | Measured 331 lines and read completely through EOF after explicit unlock | `b2175e4a7260d8d7479697218ca2835358552d27b02460b7e1b4c800f86aa56b` |

Actual sequence was original-card read and independent main/control derivation;
metadata-only ALL raw ready; author first-draft-lock notice and explicit raw release;
five mathematical raw messages ending ALL RAW FINAL; separate paper unlock;
full manuscript comparison; final adverse checkpoint and this report.
No mathematical finding was sent before the first-draft-lock notice.
This records notification and access order, not inferred private cross-agent proof times.

The author reports that its first draft already contained the full fixed loci,
valuation-gcd basin classification, control basins and phases before receiving raw.
I did not read that version and do not independently attest its contents or write time.
The released version expressly adopts my raw simplifications of the inverse densities
and proof that every main step has κ>0; those were not first-draft theorems according
to the author. The final manuscript is therefore raw-influenced, not a blind draft.
Agreement of inherited same-model contexts is not an independent-error guarantee.

Only the original card and unlocked manuscript were read as research inputs.
No appendix/outcome, scout, ledger, peer answer or historical proof was read.
No auxiliary was delegated; all main and control raw mathematics was my own.
No external lookup, numerical experiment, scientific script or higher-period census occurred.
The only file written is this assigned report.

The current [ARS router](/root/autodl-tmp/.codex/plugins/cache/ars-codex/ars-codex/3.22.0/skills/academic-research-suite/SKILL.md)
was personally reread in full through EOF. Retained workflow/DA/runtime/fallacy
guidance supplied the three checkpoints and scope discipline, not a mathematical theorem.
No venue calibration or manufactured issue quota was applied.

## 2. Checkpoint 1 — independent original-card conclusions

### Full word source, actual inverse and probability

The carrier is the entire discrete-alphabet product X=N_{≥1}^{N0}, not a finite-word
completion or a selected recurrent subset. It is zero-dimensional Polish and nowhere
locally compact: every cylinder leaves a later coordinate free in an infinite discrete
alphabet, whereas a compact set has finite image under each coordinate projection.
Each [a,b] is mapped homeomorphically onto its stated output cylinder, so the main
map is a total local homeomorphism. Units use the same rule; there are no terminals.

For target (c,d,e,η), all merge predecessors are

    (a,b,d,e,η),       ab=c, gcd(a,b)=1.

There is one additional split predecessor (cd,ce,η) exactly when c≥2 and
gcd(d,e)=1. These exhaust the equations and satisfy both inverse identities.
The ordered merge count is 2^{ω(c)}, including one when c=1.
Different pairs give different predecessors; the split predecessor has first-pair
gcd c>1, so cannot duplicate a merge predecessor. Every target has a unit-factor
merge predecessor. Main is onto and finite-to-one, with all overlaps retained.

The weights ρ(n)=1/[n(n+1)] sum to one by telescoping and satisfy ρ(n)≤1/2.
The prescribed product measure exists. A self-contained construction recursively
partitions (0,1] into the specified lengths at every finite prefix; its successive
labels have cylinder mass W(u)=∏ρ(u_i). This is a probability construction,
not a restriction or replacement of X by interval-coded points.
Every nonempty cylinder has positive mass, so support is full.
Every infinite word has mass at most 2^{-r} for every prefix length r and hence zero.
The countable coordinate partitions also exclude non-point atoms.

For every Borel tail section F, μ(uF)=W(u)μ(F). Thus an actual inverse-prefix
replacement vF→uF satisfies the integral IMAGE law for every Borel subset of [v],
with J=W(u)/W(v), not merely for the whole cylinder.
Refinement by a common tail prefix α cancels the factor W(α).
The frozen cylinder-constant version is finite, positive and continuous on its branch,
including every null fixed word. The a.e. law alone does not specify null values.
Neither whole-map measure preservation nor a canonical measure is inferred.

### Own densities, all fixed words and decisive multiplicity

For the coprime merge,

    J_M=(ab+1)/[(a+1)(b+1)]<1.

For a split a=gu,b=gv, g≥2, gcd(u,v)=1,

    J_S=(g+1)(u+1)(v+1)/[g(gu+1)(gv+1)]
        ≤4/[g(g+1)]≤2/3.

The estimate uses (u+1)/(gu+1)≤2/(g+1), and similarly for v.
Hence all main κ=−log J are strictly positive. This is an exact ownership
calculation, not an inserted log-prime roof or a uniform non-Zeno estimate.

Every fixed main word is exactly e_N=(N,1,1,...), N≥1.
In the merge case, ab=a forces b=1 and equality of the remaining coordinates
forces the full tail to be units. A split-fixed word would force a=g and b=1,
contradicting g=gcd(a,1)>1. No other signed or finite-tail case is being substituted
for the actual positive-integer infinite carrier.

At e_N, J=ρ(1)=1/2 and κ=log2. Its entire source isotropy is Z,
time image is (log2)Z, and extension kernel is zero. The least positive time
is log2, not merely a return time. Distinct fixed N never meet under actual
forward iteration and therefore cannot be the same packet under any full-tail arrow.
The fixed family gives countably infinitely many distinct packets at the same
prime-2 primitive; r log2 repeats within one packet do not identify different N.
This decides the target negatively before any T² or higher-period search.

### Complete main fixed basins and phases

A word can reach a fixed e_N only if it is eventually 1: finitely many prefix
rewrites cannot alter an infinite suffix. Conversely, on an eventually-unit word,
the finite product P of all nonunit entries strictly decreases on a split and is
preserved on a merge. Only finitely many splits are possible; after the last one,
merging consumes the finite nonunit prefix and reaches a fixed word.

The exact label is the valuation-gcd invariant

    C(z)=∏_p p^{gcd_i v_p(z_i)}.

All-zero exponent lists have gcd zero. Only finitely many primes occur in this
finite nonunit prefix. A split replaces a pair of exponents (x,y) by
(m,x−m,y−m), m=min(x,y), preserving their gcd together with all remaining
exponents. A coprime merge has at most one positive exponent for each prime
and also preserves this gcd. Consequently

    B_N={z eventually 1 : C(z)=N}

is the complete basin, not just a sufficient subfamily or recursive sample.
The invariant is not the original letters' product, ordinary gcd or lcm;
prime valuations are a proof tool and are not inserted into the source rule.
B_1={e_1}; every B_N for N>1 is countably infinite. Their union is countable
and μ-null, with the frozen full-point clock still retained.

Finite actual histories admit finite-prefix charts. Their inverse IMAGE products
compose and their Borel tail laws persist under chart refinement.
For w→z with T^m z=T^n w, the IMAGE is exp[−S_m(z)+S_n(w)] and
c=S_m(z)−S_n(w). Common legal futures cancel between same-lag presentations;
composition aligns the middle histories. The forward arrow (Tz,−1,z) has c=−κ(z),
not +κ(z). Equal triples remain one arrow; lag is not discarded.

For z∈B_N let d(z) be first hitting depth and S(z)=S_d(z)(z).
All arrows w→z in that basin have lag d(z)−d(w)+k and clock
S(z)−S(w)+k log2, k∈Z. Every ancestor, not only the fixed core, has source
isotropy Z, time group (log2)Z and zero extension kernel.
The complete phase is h−S(z) modulo log2. This is a set-level phase coordinate,
not an ambient embedded-circle/Hausdorff theorem or a μdh-invariance claim.

### Three controls, each with its own complete fixed ledger

**MERGE-ONLY.** Every target first letter c has τ(c) ordered factor-pair
predecessors, without coprimality. The map is onto, and its own branch density is
ρ(a)ρ(b)/ρ(ab). All fixed words are e_N with κ=log2.
Its complete basin is instead the eventually-unit words with ordinary finite product N.
It is singleton for N=1 and countably infinite otherwise; main's valuation-gcd
basin does not transfer. Every basin state has source Z, H=(log2)Z, kernel zero
and phase h−S_M modulo log2. The distinct fixed-derived packets again have
countably infinite total multiplicity at log2.

**REFINE-ONLY.** A target (c,d,e,η) has a predecessor exactly when gcd(d,e)=1;
it is uniquely (cd,ce,η), now allowing c=1. This is a total injection but
not onto. A target outside that image remains a legal source, not a terminal.
The split density applies on its own branches also for g=1, where J=2 and
κ=−log2. Main's positive-clock conclusion therefore does not transfer.
All fixed words reduce to e_1. Its sole predecessor is itself, so its complete
basin is singleton. Source isotropy is Z with c(k)=−k log2, H=(log2)Z and
kernel zero; phase is h modulo log2. Positive least time does not require the
positive-lag clock generator to be positive.

**GCD-COALESCENCE.** Every target first letter c has countably infinitely many
ordered predecessors (cu,cv,tail), gcd(u,v)=1. The map is onto, with individual
branch density ρ(a)ρ(b)/ρ(c), c=gcd(a,b). Infinite inverse count does not turn
their union into a single injective IMAGE chart or justify a whole-map ratio.
The complete fixed locus is f_ab=(a,b,b,...), a|b.
Its κ is −logρ(b)=log[b(b+1)], source isotropy Z, time group that positive
number times Z, and extension kernel zero. Its complete basin consists of
eventually-b words whose gcd of all letters equals a. Iterated prefix gcds
give both necessity and sufficiency. Every such basin is countably infinite and null;
its phase is h−S_C modulo log[b(b+1)]. Different fixed pairs cannot merge.
For each b there are τ(b) fixed-derived packets at that time; b=1 gives log2,
while b≥2 gives composite-integer primitive times, already log6 at b=2.

These are complete fixed-derived basins and groups, not claims that all other
source isotropy vanishes or that the full higher-period ledger has been classified.

## 3. Checkpoint 2 — complete manuscript comparison

All 331 manuscript lines were read after unlock; the measured hash matches the
released input. No correction is needed to its inverse count, branch identities,
probability, arbitrary-Borel tail law, full-point version or clock sign.
The explicit interval residual map gives the same product law as the raw
recursive interval construction; surjectivity onto all words is correctly unnecessary.

The manuscript's lexicographic (P,ell) proof is valid: for a nonfixed eventually-unit
word, a merge lowers ell by one; a split strictly lowers positive-integer P.
There can be only finitely many strict P drops and only finitely many ell drops
between them. This strengthens the presentation, not the scope, of the raw argument.
The valuation-gcd proof identifies precisely the resulting fixed label and justifies
B_1 being singleton; it does not replace the source by a prime-factor algorithm.

All control domains and images agree with their own raw derivations.
The example (2,2,1,...) has main label 2 but MERGE-ONLY label 4.
The REFINE-ONLY null core has negative signed κ but the stated positive H generator.
GCD-COALESCENCE retains its infinitely many predecessors and the full eventually-
constant basin, not merely its displayed immediate-predecessor examples.
The ancestor-isotropy and phase formulas preserve all branches and all heights.

The manuscript explicitly attributes the raw density simplifications and all-main
positivity addition, while the older first-draft contents remain author-reported here.
Administrative companion contents, links beyond these inputs, and the author's
other source accesses were not independently audited by this reviewer.

## 4. Checkpoint 3 — adverse checks, limits and disposition

- Equal log2 groups do not merge fixed packets: distinct fixed futures can never meet,
  even using arbitrary inverse histories or retained lag. The multiplicity objection
  is intrinsic to the full frozen owner, not a choice of representatives.
- The returning basins are null, but not absent. The all-point branch prescription is
  explicitly frozen and compatible; an a.e. identity alone would not justify silently
  assigning their clock. Deleting these states would change the source and its ledger.
- Nonfixed ancestors retain source isotropy Z once they enter a fixed core. Treating
  them as having trivial isotropy because they are not literally periodic would be wrong;
  both the manuscript and the derived phase formulas avoid that error.
- Positivity of all main κ does not grant a classical suspension, a uniform waiting-time
  bound, prime multiplicity or natural A0. REFINE-ONLY also confirms that signed κ and
  the positive generator of H are different notions.
- The divisor interface is genuine: d|n iff gcd(n,d)=d, and a proper divisor actually
  rewrites to (d,n/d,1,η). But g>1 is a different common-factor condition on general
  pairs, so the paper rightly claims admissibility deformation rather than conjugacy.
- Higher nonfixed returns remain unclassified. The fixed-family counterexample already
  decides the target; additional cycles could not remove those extra fixed packets.
  No universal no-go for arithmetic rewriting or canonical-measure existence is proved.

No blocking or nonblocking manuscript correction is requested, and no issue was
manufactured to meet a quota. Genuine arithmetic feedback, owned nonatomic IMAGE,
and positive fixed-return clocks are retained as positive results. The main target
nevertheless fails at countably infinite prime-2 fixed-packet multiplicity: STOP / FORK.
Same-object ownership remains intact; selecting a single N, changing the probability
or substituting a control would require a new object, not a repair of this result.
Stronger naturalness remains OPEN. T3 is NOT SUPPLIED / NOT PURSUED; classical
A0/A1/A2 are NOT APPLICABLE, formal Route UNASSIGNED and Route B NOT INVOKED.
This report is frozen against the original-card prefix and released manuscript hashes above.
