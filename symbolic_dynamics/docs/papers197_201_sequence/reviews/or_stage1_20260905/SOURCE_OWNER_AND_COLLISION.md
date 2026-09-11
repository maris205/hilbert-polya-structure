# OR: independent source-owner and mechanism subtraction

2026-09-05 UTC. Read scope below is the reviewer's own scope, not inherited
from the author. This bounded audit supports SELECT_INTERNAL_AMBER, not
priority, publication novelty, completeness, or freedom to operate.

## Primary material actually inspected

1. Michael Damron, Janko Gravner, Matthew Junge, Hanbaek Lyu and David
   Sivakoff, *Parking on transitive unimodular graphs*, Annals of Applied
   Probability 29(4), 2089--2113 (2019), DOI 10.1214/18-AAP1443.
   Read the author-hosted [primary PDF](https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2019.pdf),
   introduction and Section 2, PDF pages 1--8. This directly owns the
   parking mechanism: synchronous cars stop at available unit spots and
   pass occupied spots; the introduction includes deterministic unit-speed
   paths, and the transition-kernel setup allows deterministic trajectories.
   Its principal theorems concern infinite-graph random initialization and
   visitation/parking phase transitions. The finite OR clearance lemma is
   an elementary specialization of owned parking, not a new particle model.
   The inspected source does not supply the literal OR rule and target
   decoder; identifying them with an owned object would require an actual
   transfer, not inference from the word "parking".

2. M. Cabezas, L. T. Rolla and V. Sidoravicius, *Non-equilibrium Phase
   Transitions: Activated Random Walks at Criticality*, Journal of Statistical
   Physics 155, 1112--1125 (2014). The browser repeatedly timed out. A fresh
   successful streaming `curl | pdftotext` read of the
   [author-hosted primary PDF](https://www.ime.usp.br/~leorolla/papers/arwcritical.pdf)
   supplied title/metadata and Sections 1--2 through Lemmas 1--3. Particles
   filling holes permanently, excess particles passing settled ones,
   two-type annihilation, and Abelian stabilization are direct precedents.
   The paper distinguishes continuous-time ARW and particle-hole trajectories
   despite stabilization equivalence. We likewise do not infer exact OR
   synchronous times from an Abelian stabilization theorem. No local PDF
   archive, whole-paper read, or theorem in later sections is claimed here.

3. Hanbaek Lyu, *Synchronization of finite-state pulse-coupled oscillators*,
   arXiv:1407.1103v3 (2015). Read the [primary HTML](https://arxiv.org/html/1407.1103)
   introduction, Definition 1 and Section 2 through Definition 2.3 and the
   width-lemma discussion. The FCA holds a post-blinking site when it sees
   a blinking neighbor; OR instead skips an additional phase at source `10`.
   The broader pulse-coupled-oscillator setup and relative frame `X_t-t`
   are already owned. OR is plainly within that broad modeling vocabulary;
   its name is not a new-class claim. Lyu's local-monotonicity premise
   includes synchronization of two coupled sites; OR's persistent `01/10`
   two-cycle prevents a direct application of that synchronizing theorem.
   A failed request for an invented v5 URL was replaced by the actual
   v3 HTML record; no v5 source is cited.

4. Hanbaek Lyu and David Sivakoff, *Persistence of sums of correlated
   increments and clustering in cellular automata*,
   [primary arXiv PDF 1706.08117](https://arxiv.org/pdf/1706.08117).
   Read equation (9), Section 4.1 CCA, Section 4.2 GHM and Section 4.3 FCA
   through the particle descriptions/propositions. These explicitly connect
   three-colour media to annihilating edge particles. In FCA, first-step
   flips and subsequent speed-one-third particles are owned, so delayed
   particle motion cannot be offered as an OR innovation. The CCA copies a
   successor colour, GHM excites a resting zero, and FCA inhibits `2` near
   `1`; these are not OR's extra advance at `10`. The fetched PDF labels
   arXiv v2 but has an internal April 28, 2022 date; this audit cites the
   arXiv identifier and inspected equations, not an inferred publication
   year or unsupported journal metadata.

5. Amitava Banerjee and Muktish Acharyya, *Cellular Automata Model of
   Synchronization in Coupled Oscillators*, arXiv:1601.06980v4 (2017).
   Read the [primary HTML](https://arxiv.org/html/1601.06980) introduction and
   Section II equations (1)--(2). The update uses a floor of a symmetric
   sum of absolute phase differences, with periodic phase reduction and
   an explicitly rotating frame. This is finite nonlinear oscillator
   background, not OR's local two-input table. No theorem from its later
   simulation analysis is used to prove or certify OR.

6. Benjamin Hellouin de Menibus and Mathieu Sablik, *Self-organisation in
   cellular automata with coalescent particles: qualitative and quantitative
   approaches*, [primary arXiv record 1602.06093](https://arxiv.org/abs/1602.06093).
   Read abstract and bibliographic record only. It owns broad particle
   self-organization methods and includes cyclic and one-sided captive
   automata among applications. Its full proofs were not audited here;
   absence of an OR owner cannot be inferred from this abstract-level read.

## Exact transformation tests, with their limits

The OR table is `(111;022;000)` with the first row indexed by current zero.
With local index `3a+b`, the ternary code is 661 (reverse digit display
`000220111`). Code numbers depend on convention and a matching integer in
an unrelated search result proves nothing.

Writing `C` for global +1, `F=C G`, where `G` changes `1` to `2` only before
`0`. In the frame `z_t=x_t-t`,

```text
z_(t+1),i = z_t,i + 1[(z_t,i,z_t,i+1)=(1-t,-t)] mod3.
```

The trigger rotates with `t mod3`. This is a periodic rule family, not an
autonomous CCA conjugacy. Standard moving-frame methodology is zero credit.

The independent verifier tests all six global colour permutations, with
and without exchanged input roles, against the directed specializations
of CCA, GHM and FCA. All 36 identities fail. More strongly, a same-length
full-carrier conjugacy for every n cannot identify OR with CCA or GHM,
since those have fixed states already at n=1 while OR has a three-cycle.
At n=2, FCA has no two-cycle while OR has `01 <-> 10`. These obstructions
exclude that precise family of proposed identifications, not all block
encodings, restrictions, powers, or auxiliary phase lifts.

## Internal exact/proof-owner subtraction

The recovery indexes, central anchor and historical caveats were read.
Retrieval searched available manuscripts and scouting/kill records for
literal reset/increment inequalities, firefly/CCA/GHM, surplus/retention,
capacity-one parking, and particle-hole queues. The nearest actual texts
were opened as follows; their exact hashes are pinned.

### P90: traffic temporal method is occupied

`papers/90-rule184-particle-periodic-zeta/main.tex`: the binary update is
`x_i x_(i+1) + x_(i-1)(1-x_i)`. It has no-11/no-00 recurrent branches with
opposite spatial rotations, sharp layer time `(min(m,n-m)-1)_+`, and a
min-plus car-position solution. Read these proofs and the periodic census.
The two-phase strategy, car/hole extremality and trace census are wholly
background. OR's run factor instead parks one particle and moves all
surplus through two intervening transit bins. We do not infer a new
mechanism from that delay. What did not transfer from P90 is the original
ternary word identification and its every-target local source-set atlas.

### P169: both queue engines and its inverse were inspected

`papers/169-successor-transfer-set-partitions/main.tex`: the literal rule
simultaneously moves each nonsingleton block maximum to its successor block.
Its excess-load factor is
`z_i'=z_i-1[z_i>0]+1[z_(i-1)>0]`, a unit-service queue. Its sparse
labelled-window phase also contains the capacity-one particle/hole rule
`q_i'=q_i-1[q_i=2]+1[q_(i-1)=2]` on `q_i in {0,1,2}`. Thus the parked
particle/hole argument is occupied even within internal history.

The complete inverse proof reconstructs block sets by selecting outgoing
maxima, removing incoming ones, testing nonempty remainders and preserving
minimum-label order; its five-state matrices retain actual label thresholds.
OR's source alternatives are the four/three/two local edge classes, with
one independent binary ambiguity at each `01` target edge. No substitution
of a block load or relabelled outgoing maximum converts that old full
inverse to OR's atlas. A shared generic transfer-matrix representation is
not credited to either candidate as a new mechanism.

### P164 and P196: adjacent-word inverse owners

`papers/164-cyclic-equality-feedback/main.tex`: literal equality recording
collapses to binary affine Rule 102, with a weighted change-mask code
enumerator and one recurrent point at the dyadic lengths under study.
Read the main theorem and interface proof. OR does not factor through that
printed equality mask: the triggering edge `10` is orientation- and
colour-specific. Its inverse is not the q-colouring multiplicity of a
change mask. Merely having a nonlinear first step followed by an owned
factor is generic and gets no credit.

`papers/196-cyclic-godel-implication/main.tex`: read the literal implication,
one-step rotation core and entire gap-product inverse proof. Its update
is `a=>b=top` for `a<=b`, otherwise `b`. All tails are at most one and
all recurrent periods divide n. Its independent gap factors count weak
chains with a final strict endpoint. OR's table is not implication; its
full source sets are independent local binary alternatives, not those
monotone-chain classes. The common inequalities/forbidden-language/trace
architecture is expressly background, not a distinction credited as new.

### CPD/CSPD and the danger of parking wrapper rescue

`reviews/cpd_cspd_owner_gate_20260905/OWNER_TRANSFER_GATE.md` proves an
exact set-level transfer of every circular site-displacement fibre to an
already studied parking site-normalization class. That kills the inverse
axis despite coherent feedback dynamics. OR is not a parking-statistic
writeback or a site-normalization wrapper: it has the literal local table
on the full word carrier. Its two-step run factor is parking, but the
previous normalization-class bijection does not reconstruct its source
words. No equally complete joint transfer was found here. If one is found,
the same kill criterion applies; stronger clocks would not protect OR.

P198 constrained erasure and P201's exact old OCL conjugacy remain killed.
This review does not revive them or edit their accepted historical record.

## Search record and bounded final judgment

Fresh primary-oriented queries included:

```text
"cellular automaton" "one-sided" "reset" three state
"cellular automata" "111022000"
"cellular automata" "000220111"
"cellular automaton" "661" ternary
"cyclic cellular automata" "skip" "three"
"firefly" "advance" "three-state" automaton
particle hole model directed deterministic synchronous parking
site:ime.usp.br/~leorolla/papers/arwcritical.pdf "particle-hole"
```

Queries yielding irrelevant code-number, hobby-simulator, secondary
encyclopedia, or ResearchGate hits supplied no authority. A failed browser
read was not represented as a successful read; the Rolla paper was later
read via a successful independent stream. No-hit searches supply zero
evidence for novelty.

After fully deducting the parking temporal mechanism, the residual passes
the current internal threshold only as a narrow joint theorem for the
specified OR map: exact original-word recurrent exhaustion/action and
sharp prehistory, separated from local source reconstruction/maximality.
This is not a renamed parking algorithm presented as new, nor a claim that
a sign change in an oscillator equation alone creates a new research class.
The proof axes are deductively closed and no full existing owner transfer
was established in the inspected surface. That bounded finding supports
SELECT_INTERNAL_AMBER with an explicit external hold.

The P51--P56 manuscript gap is retained. A local search across available
P1--P196 files does not amount to a re-review of 196 manuscripts or a
complete classification under conjugacy. Further owner work is necessary
before any external circulation.
