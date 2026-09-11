# Fourth root intake — six component/rank word probes

2026-09-05 UTC. Root author. Full carrier [n]^n, labels 1,...,n,
rooted cyclic positions, synchronous old-state update; n=1,...,6 in the
actual 36-box pilot. The complete stdout is COMPONENT_CANONICAL.jsonl.
component_pilot.py reuses only this root lane's generic pilot.py profiler;
this is not an independent checker. These add six literal rules (root total
27), not six independent mechanisms. There is no numbered admission.

| Rule | Literal statistic at i | n=6 image / H / strict cycles / max fibre | Disposition |
|---|---|---|---|
| SLC | Number of components of {j:x_j>=x_i}, with full cycle count one | 155 / 3 / 39 fixed / 11514 | KILL_CURRENT_NO_RIGID_CONTRACT; explicit periods 2,3,4,6 below defeat extrapolation |
| ECS | Size of the cyclic equal-letter run containing i | 55 / 3 / 28 fixed / 15630 | KILL_OLD_ADJACENT_RUN_MERGER; cyclic cut convention is not a new engine |
| WIR | Length of the longest weakly increasing cyclic scan from i, capped at n | 63 / 1 / 1 fixed+31 two-cycles / 2703 | KILL_MASK_COMPLEMENT_AND_STATIC_CYCLIC_DESCENTS |
| BEG | Maximum distinct-letter count over cyclic prefixes ending just before a return to x_i, full turn allowed | 6 / 2 / 1 fixed / 23400 | KILL_CONSTANT_SUPPORT_CARDINALITY; maximum includes the full turn |
| LUB | Size of the superlevel component containing i, stopping at strictly smaller values | 1683 / 3 / 1 fixed+553 two-cycles / 225 | BOUNDED_PROOF_SCOUT in LUB_PROOF_WORK, not a reserve |
| SPR | One plus the number of strictly smaller earlier letters | 720 / 5 / 132 fixed / 462 | KILL_DIRECT_OWNER; exact shifted Theta on the whole carrier |

## SLC — finite fixed-only guess actually fails

The first n<=6 boxes have only fixed points, but the explicit length-eight
word 12121313 maps to 14141212 and then 12121414, which alternate. The
standalone slc_spike.py records that exact timeline. Its independent
implementation counts superlevel starts by x_j>=a>x_(j-1), with full-cycle
correction one; it imports no pilot function.

An actual deterministic seeded counterexample search (seed 204206) then
used 1,500 words for each n=8,12,20,40, letters 1,...,min(n,8), with a
5,000-orbit-state safety cap. All 6,000 orbits closed before the cap.
At n=20 actual strict three-cycles occur; at n=40 periods 1,2,3,4,6 occur.
SLC_SPIKE_CANONICAL.json preserves full first long-cycle witnesses, source
words, observed heights and every period histogram. No general two-cycle
theorem follows from the smaller boxes, and no all-n inverse/clock contract
was obtained. This closes this signal without a larger rescue cutoff.

The statistic is the classical zero-dimensional superlevel component count;
ordinary component/Betti-curve methods receive no credit. Broad primary
queries on iterated Betti curves/superlevel feedback found neighbouring
topological/morphological work, not a directly inspected owner of this
literal rule. No claim of global novelty or impossibility is inferred.

## ECS — exact mass-merger encoding

Compress a nonconstant word into its cyclic maximal constant runs with
lengths a_1,...,a_k, retaining their labelled boundary anchor. After one
update, every old run has the value a_j. Adjacent old runs with equal
length now coalesce; a maximal sequence s repeated r times becomes one
new run of length rs. This is exactly the cyclic version of adjacent-run
consolidation. A uniform word maps to n^n and stays there. Root read
P147 main.tex's literal map, doubling-ancestry proof and divisor-path
inverse, as well as the earlier C05_RLF kill in the P187–P191 lane.
The linear/cyclic boundary distinction is acknowledged, not called an
exact literal equality to P147's linear carrier; the whole mass-merger
mechanism transfers with the closing adjacency added. No new temporal
engine is demonstrated.

For a nonconstant target, each constant target run of length L and value
s must split into L/s source runs of length s, requiring s|L. Their
colours form a proper colouring of the resulting source-block cycle.
A constant target has a separately anchored cyclic equal-length tiling.
These are static cut/colour counts, not a second nontransferred mechanism.
No sharp cyclic clock or fibre extremum is promoted here.

## WIR — complete elementary temporal and inverse adapter

Let D(x)={i:x_i>x_(i+1)}. It is never the full cycle. If D is empty,
x is constant and WIR(x)=n^n, a fixed state. Otherwise write r_D(i)
for one plus the forward distance from i to D. Then WIR(x)=r_D.
Directly, D(r_D)=D-complement: every non-D position drops by one in
the distance profile, while a D position has value one and cannot drop.
Thus the nonconstant image is precisely {r_D: empty!=D!=[n]}, on which
WIR interchanges D and its complement. Conversely r_(D-complement)
is an explicit source of r_D. Image=core has 2^n-1 states, and the map
has height one for n>=2. This is a distance encoding of mask complement,
not an independently new dynamical primitive.

The inverse of r_D consists exactly of words with cyclic strict descent
set D. For B nonempty, cut the labelled cycle at each edge in B and let
ell_1,...,ell_k be the resulting path lengths. Words whose descents are
contained in B are counted by

    G(B)=product_j binom(n+ell_j-1, ell_j).

For B empty put G(empty)=n, because a weakly increasing full cycle must
be constant. Ordinary inclusion–exclusion gives the exact fibre

    sum_(B subset D) (-1)^(|D|-|B|) G(B).

Necessity/sufficiency here are the defining cyclic descent constraints;
G is independent weakly increasing word counting. This is a complete
static chain/IE adapter, including the empty-cut correction. No novel
cyclic-descent-counting result is claimed. P204's accepted adverse
MacMahon adapter reinforces why a rewritten old static formula is not a
new inverse axis. Root does not claim its linear flagged formula is
literally this cyclic one.

## BEG and SPR — immediate closures

BEG permits d=n among its return lengths. Every shorter prefix's distinct
set is contained in the full word's set, so its maximum is exactly the
global number of distinct letters. The output is a constant word, then
1^n. Its fibre is only the classical occupancy/Stirling count. This
degenerate literal rule is preserved, not silently replaced by the intended
first-return statistic after looking at the output.

For SPR write z=x-1. Its output minus one is
Theta(z)_i=#{j<i:z_j<z_i}, so translation is an exact conjugacy on
{0,...,n-1}^n. Root read the current primary
[Allagan–Gao–Testart preprint](https://arxiv.org/html/2608.24476v1),
Section 1 and Definition 2.3/Proposition 2.5 with its proof: it defines
Theta on arbitrary finite sequences, proves image containment in inversion
sequences and its permutation bijection, and states the fixed/stabilization
programme. The [arXiv record](https://arxiv.org/abs/2608.24476) confirms
25 August 2026. This is a direct full-map owner, not merely a related
Catalan census. Earlier local L01 rejection is consistent with that actual
primary definition. No new paper is justified by shifting all labels.

## Remaining LUB obligation and limits

LUB's local superlevel AREA differs from SLC's global component COUNT.
The graph scout now owns a bounded proof/source/adapter attempt, with
Cartesian span, max-tree area and nearest-smaller primitives explicitly
deducted. The six initial boxes and apparent period-two behavior are not
an all-n theorem. No LUB paper number, candidate PASS or reserve is declared.
All failed data and prior accepted/rejected manuscripts remain unchanged.
External release/contact remains HOLD_EXTERNAL.
