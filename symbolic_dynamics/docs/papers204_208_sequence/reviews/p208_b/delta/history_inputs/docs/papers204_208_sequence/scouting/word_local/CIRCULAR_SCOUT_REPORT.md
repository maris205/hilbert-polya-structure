# Third root intake: six circular statistics

2026-09-05 UTC. Author: root. The first pass exhausts [n]^n for n=1,…,6
for each rule, with values 1,…,n, cyclic labelled positions and synchronous
updates. `CIRCULAR_STATS_CANONICAL.jsonl` is the complete 36-line actual
stdout. The scout imports this same lane's `pilot.py` graph profiler;
it is author exploration, not independent theorem verification.

| Rule | Literal coordinate | n=6 exact output | Disposition |
|---|---|---|---|
| CNE | Distance to next equal letter to the right; n if unique | image203; H5; cycles1:1,2:18; max fibre720 | No all-n temporal theorem; no promotion. |
| CNM | Nearest positive circular distance to another equal letter in either direction, n if none | image168; H4; fixed16; max fibre720 | Fixed-only small boxes do not prove convergence; no promotion. |
| CCS | Multiplicity of the letter at the position | image150; H3; fixed82; max fibre1800 | Exact old equal-cardinality merger; kill. |
| CDW | Longest pairwise-distinct window starting at the position, capped at n | image197; H4; periods1,3,4,6,9,12; max fibre720 | No rigid two-axis contract; no promotion. |
| CUW | Length before the first equal adjacent pair encountered going right, capped at n | image58; H6; sole fixed point; max fibre15630 | Exact sliding-AND/equality-mask adapters below; kill. |
| CRC | Strict-record count of the scan starting at the position | image462; H2; cycles1:1,2:70; max fibre371 | Complete ternary theorem below, independent gate pending. |

These bring the root to 21 literal pilots after the preceding 12 word/order
and three radius rules; they are not 21 independent mechanisms. General
CRC and CRC3 are one family, not two seats. Radius OPR/EPR have long or
varied periods already in their original small boxes; CPR has no closed
all-parameter contract. Their full 27-line output stays RADIUS_CANONICAL.jsonl.

## Exact cheap rejections

For CCS, quotient by equality blocks. All old blocks of equal size receive
that same size as new letter and merge. The size multiset therefore evolves
by exactly the permanently occupied equal-cardinality coagulation. The
P187–P191 combinatorial C04_PME kill and P147–P151 root EQC record explicitly
cover this word-map factor. Relabelling does not supply a new engine.

For CUW let E(x) be the equal-adjacent-edge starts. If E is nonempty, the
output at i is one plus forward distance to E. Where i∉E consecutive
output distances differ; where i∈E the output one equals the next output
exactly if i+1∈E. Hence E(CUW(x))=E∩(E−1) for nonempty E. Empty E
instead gives n^n and then 1^n; full E gives 1^n. The nonempty proper
part is literally sliding-AND erosion. The two uniform exceptions do not
create an independent time mechanism.

The target determines E through its one positions, with the empty-mask
constant-n case separated. Contracting equal edges leaves a cycle with k
unequal edges, whose proper-colouring count is exactly
(q−1)^k+(−1)^k(q−1), including the k=1 impossibility and k=0 value q.
Root read the original P162–P166 `cyclic_sliding_and/SCOUT.md` §§1–2 and
`root_cyclic_equality_feedback/SCOUT.md` §§1–2: the former is this exact
AND clock and the latter's equation (5) is precisely this mask weight.
Both axes transfer, rather than merely sharing names or small numbers.

## CRC3 author proof and actual execution

`CRC_TERNARY_PROOF_PACKAGE.md` proves on {1,2,3}^n for every n≥1: exact
first/second images; reflection core and sharp height; exact populations;
source-maximum/run-based one-step decoding; sharp maximum fibre three for
n≤2 and 1+J(n) thereafter; and all equality targets through optimal block
sizes. Integer products and transfer matrices are classical. No maximum
fibre for larger alphabets is asserted.

The new self-contained `verify_crc3.py` imports no pilot, old or reviewer
code. First invocation to `CRC3_CANONICAL.json` and a second physical run
to `/tmp/crc3_author_replay.stdout` both exited zero; actual raw `cmp`
against the saved canonical exited zero. Both contain 655,256 assertions
on all 88,572 ternary states through n=10, including every-target fibres
and equality cases, whole functional graphs, and all exact source sets
through n=7 (3,279 targets). A finite integer-product DP through n=40
pressures the exchange proof. Python 3.12.3, fixed integer arithmetic,
`-B`, no randomness, external data or network. These boxes pressure new
deductions, not substitute for them or rescue an unproved conjecture.

- Canonical and second raw stdout:
  `1b035b1fc2036e2e1b237c3aeaeb5cefa9af3a830f2f76cf0b43cf75ac8fb9be`.
- Verifier: `8665dfa7342247a8dac651476b3c7ab9c134873fbc6e366f7bfae3a61eadc354`.
- Ternary proof: `2a843e89f628197e31c1548597311780bfa0f6fa0d7a32903b86a5940d987634`.

The nonauthor graph agent owns CRC3's independent source/value gate. Full
static adapters must be checked; neither bounded nonhits nor ordinary
integer-break terminology settles admission. The earlier general CRC
proof spike's proposed general-tree inverse is explicitly unverified and
is not the present theorem contract. No formal paper ID is allocated.

NS/P204's adverse manuscript Review A is a live caution: its entire
flagged inverse reduces to a binomial scale times an old exact-descent-set
count. The original candidate acceptance remains archived; the numbered
draft is rejected, not silently changed into a completed one-axis paper.
CRC3 does not escape equivalent scrutiny by having a new run formula.
All material remains OWNER_AMBER / HOLD_EXTERNAL.
