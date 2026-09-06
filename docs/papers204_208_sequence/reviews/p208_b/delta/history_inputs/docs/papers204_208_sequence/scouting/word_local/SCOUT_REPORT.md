# Word/local intake — first bounded pass

2026-09-05 UTC. Author scouting, **zero admitted papers**. The project
research skill supplies the early-kill/collision gate; proof-writer supplies
the separate proof package for the GM follow-up. No external review API or
private manuscript upload was used.

## Eight literal pilots

`pilot.py` and its actual `PILOT_CANONICAL.jsonl` contain complete functional
graphs, not sampled trajectories, in the stated boxes. The first five maps
act on inversion-sequence carrier $x_0=0$, $0\le x_i\le i$. ZA acts on
$x_0=0$, $0\le x_i\le n-i$ for $i>0$. MO and MC use cyclic ternary words.
Each box has $1\le n\le8$; the maximum factorial box is 40,320 states.

| Handle | Literal update | Last-box signal | Current decision |
|---|---|---|---|
| PD | Previous equal-letter distance, or zero when the letter has not appeared | Height 23; periods 4,6,8,12,16 | KILL: no uniform recurrence spine; static equality encoding alone is insufficient |
| DS | Length of longest pairwise-distinct suffix ending at each position, minus one | Height 23; periods 1,2,3,4,6,8,16 | KILL: no temporal atlas despite a small image |
| PS | Longest palindromic suffix length at each position, minus one | Height 14; periods 2,4,8 | KILL: no all-parameter theorem; palindrome terminology is not separation from P138 |
| BC | Number of positive proper borders of each prefix | Height 11; seven two-cycles; largest fibre 5040 | KILL: signal too close to P134 whole-border recomputation; a different statistic is not a proved different mechanism |
| ER | Current equal-letter suffix run length, minus one | Height 13; one two-cycle; largest fibre 5040 | KILL: elementary run/equality propagation and factorial source choices, below independent-mechanism threshold |
| ZA | Recompute the entire ordinary Z/prefix-match table, with first entry zero | Height 3; 64 two-cycles, apparently one recurrent state per noninitial zero mask | PROOF_PENDING, not a reserve or paper; separate author proof attempt in `ZA_PROOF_WORK/` |
| MO | $x_i\mapsto\operatorname{mex}\{x_{i-1},x_{i+1}\}$ | Height 2; only fixed points and two-cycles | Cycle specialization receives no separate seat; expanded deductively to GM below |
| MC | $x_i\mapsto\operatorname{mex}\{x_i,x_{i+1}\}$ | Height 2; periods divide $2n$ | KILL: NOR-factor/shifting-language residual not established beyond the occupied local-map surface |

The denominator is eight literal local/word maps, not eight independent
proof classes. GM is the general-undirected-graph expansion of MO, not a
ninth unrelated local rule. No sharp clock or complete recurrence conclusion
is inferred for a killed map solely from these finite data.

## Direct pre-pilot collision kills

The ordinary KMP border-array recomputation is exactly P134, not a fresh
candidate. Its actual `main.tex` proves the $n-1$ canonical two-cycles,
mismatch amplifier, linear clock, and factorial inverse extremum.
Repeated inventory had already been killed in
`docs/papers187_191_sequence/scouting/root_coordinator/KILL_LEDGER.md`.
Truncated positive cyclic differences are the primewise literal dynamics of
P187 cyclic divisor quotient, not a new word mechanism. Bulgarian solitaire,
Ducci and cyclic descent indicators likewise have explicit earlier owner or
kill records. These pre-pilot duplicate probes are not added to the eight.

## ZA targeted follow-up, still unproved

`z_spike.py` checks every binary source through length 14, then 2,000 seeded
source/mask pairs at each of lengths 16,32,64,128,256. Binary source heights
reach four; the tested larger arbitrary-colour sources reach five. Each
tested arbitrary source has the same even-phase recurrent endpoint as its
binary zero-mask representative. These are finite observations, not a
logarithmic bound, universal endpoint theorem or source census.

The identity $Z(x)_i>0\iff x_i=0$ for $i>0$ proves that noninitial zero
masks alternate, but does not prove uniqueness of a recurrent representative.
The six-letter trajectory `010110 -> 002001 -> 010210 -> 001001 <-> 010310`
already refutes the tempting claim that the first Z-image of any binary
word is recurrent. A separate proof attempt owns only `ZA_PROOF_WORK/`.

## GM follow-up and its unresolved value boundary

Update: the independent [GM candidate gate](GM_GATE/CANDIDATE_GATE.md) has
now returned **MATH_VALID / KILL_VALUE_FOR_THIS_BATCH**. Root inspected its
actual proof/source comparison. The degree deadline and sharp witnesses are
preserved as correct candidate mathematics, but the inverse extremum is a
generic incidence-mex statement transferring the P118 forbidden-palette
skeleton. It does not supply the required second residual axis. GM is not
promoted. The paragraphs below retain the author-intake provenance.

`GM_PROOF_PACKAGE.md` gives deductive proofs for arbitrary finite simple
undirected graphs: two-step coordinatewise colour descent, a strict-drop
chain yielding local deadline $\max\{1,\deg(v)\}$, sharp global maximum
degree time at every degree, and the unique largest one-step fibre for
$q\ge\max\{3,\Delta+1\}$. These are author claims pending independent
candidate verification and value/source subtraction, not accepted papers.

`verify_gm.py` is self-contained and imports no earlier research code.
Its actual `GM_CANONICAL.json` records 876,693 assertions across all 76
labelled graphs of order zero through four with two palettes per graph
(34,867 graph/palette/source cases), all target fibre extrema in those
boxes, and complete explicit sharp-witness trajectories for degrees 2–24.
`graph_mex_spike.py` separately checked all graphs through five vertices
and bounded random larger graphs, but that scouting run is not the
standalone theorem verifier and is not an all-size proof.

P118 owns the same local rule on complete multipartite graphs. Its quotient
and full labelled basin/fibre results are not re-claimed here. The general
GM temporal proof does not use that quotient, but a different carrier alone
does not clear the collision gate. An independent candidate check owns
`GM_GATE/`, including the possibility that the new conjunction is too thin.

## Primary-source boundary actually inspected

Hedetniemi, Jacobs and Srimani, *Linear time self-stabilizing colorings*
(2003), [publisher record](https://www.sciencedirect.com/science/article/pii/S0020019003002990)
and [complete author-hosted paper](https://www.cs.clemson.edu/stabiliz/Papers/coloring-ipl-2003.pdf),
were opened. The paper explicitly assumes serial moves on printed page 252;
Algorithm 2.1 on page 253 is the same minimum-absent-neighbour-colour
correction in positive colours. Its Lemmas 4–6 and Theorem 1 establish
proper-colour persistence, a per-vertex move bound, and a total move bound.
The rule, static Grundy colouring, and that serial argument receive zero
credit. Jacobi GM also admits an alternating-part interpretation on the
bipartite double cover; the independent gate must determine whether this
adapter and the existing argument already consume the claimed clock.
No priority or global novelty is asserted.

For ZA, exact phrase searches for iterated Z arrays/prefix tables found
static validation and reconstruction, including Clément–Crochemore–Rindone,
[*Reverse Engineering Prefix Tables*](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2009.1825).
Only the bibliographic record has been retrieved at this point; no body-level
subtraction or absence-of-owner conclusion is claimed for that source.

Queries also covered `synchronous Grundy`, `mex operator` graph iteration,
`minimum excluded` synchronous coloring, and the 2003 exact title.
Search non-hits carry no novelty credit. External circulation remains held.

## Second small intake: four order/stack statistics

`order_distance_pilot.py` and `ORDER_DISTANCE_CANONICAL.jsonl` contain four
further literal maps on $E_n$, fully enumerated through $n=8$.
This brings the root lane to twelve literal pilots, not twelve independent
classes. The new maps are previous-smaller distance (NS), previous-greater
distance (NG), decreasing-stack depth after popping values at most the
current value (VD), and longest alternating subsequence ending at each
position minus one (AE). The last three are not advanced: NG/VD show the
same elementary left-to-right zero propagation silhouette, while AE has a
two-step prefix-shape collapse without an independent inverse theorem.
No exact conjugacy of NG and VD is inferred from identical histograms.

NS has a complete author [proof package](NS_PROOF_PACKAGE.md): two-step
entrance into a blockwise complement core, exact Fibonacci recurrence/fixed
counts, and all target fibres at every time at least two via the original
ascent masks and flagged decreasing-segment counts. Its self-contained
`verify_ns.py` passed 485,578 checks; actual stdout is `NS_CANONICAL.json`.
First-image census, one-step fibres and a global fibre extremum are not
claimed. The independent source/value gate in `NS_GATE/` is pending.
Standard previous-smaller indexing, word counting, and inclusion--exclusion
are not claimed as inventions. No paper ID had been allocated at that intake.

## Later lifecycle and third intake

NS subsequently passed its candidate gate and was numbered P204, then
actual manuscript Review A found the exact binomial-scale/MacMahon adapter
and rejected its two-axis admission. The original proof stays valid;
the numbered draft and adverse evidence are preserved in the batch.
This supersedes the historical pending status above without rewriting
that earlier candidate gate.

Three radius probes and six circular statistics are now recorded in
[the circular intake report](CIRCULAR_SCOUT_REPORT.md), bringing this lane
to 21 literal pilots. CRC3 has a complete two-axis author theorem and
actual standalone 655,256-check canonical; independent source/value gate
pending. General CRC and ternary CRC3 remain one rule family. No additional
paper is admitted by this scout report.
