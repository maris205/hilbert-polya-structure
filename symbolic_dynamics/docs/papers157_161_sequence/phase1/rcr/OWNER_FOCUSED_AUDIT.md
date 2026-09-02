# RCR focused owner and collision audit

**Audit date:** 2026-09-02  
**Scope:** random anchored-rectangle contraction (`RCR`)  
**Decision:** `OWNER_AMBER / MATHEMATICS SURVIVES / HOLD_EXTERNAL`

This is a bounded primary/authoritative owner search and an internal
P1--P156 collision audit.  It is not a novelty, priority, ownership,
freedom-to-operate, attribution, or release certificate.

## 1. Search protocol

The local `papers/` and `literature/` stores were searched first for
decreasing chains, simplex-efficiency chains, random recursive trees, leader
election, nested rectangles, and absorption kernels.  No local RCR owner
source was present.  Public search then used author/publisher, DOI, arXiv,
and journal records.  No draft claim text or private material was sent to an
external person or model.

Representative focused queries were:

- `uniform decreasing Markov chain transition uniformly 1 to n absorption`
- `p(i,j)=1/(i-1) simplex efficiency Markov chain`
- `randomly choose integer between 1 and current absorption harmonic`
- `random recursive tree depth uniform parent records`
- `decreasing Markov chain absorption renewal lower triangular`
- `leader election Markov chain geometric maxima decreasing`
- `random anchored rectangle contraction uniform lattice cell`
- `nested rectangles random process uniformly chosen point`
- `random subrectangle Markov chain absorption`
- exact-form probes containing `(n-1)!`, `k-z`, and `sum of independent
  geometric`

The citation chain was followed backward from Alsmeyer--Marynych to
Van Cutsem--Ycart, Haas--Miermont, and Ross, and sideways through the strict
descent's random-recursive-tree/record interpretation.  A complete
MathSciNet/Zentralblatt/non-English citation closure and specialist review
were not performed.

## 2. Decisive owner subtraction

### 2.1 Ross owns the strict uniform-descent skeleton

Sheldon M. Ross, [“A Simple Heuristic Approach to Simplex
Efficiency”](https://doi.org/10.1016/0377-2217(82)90177-1), *European Journal
of Operational Research* 9 (1982), 344--346, models a move from the `j`th
ranked extreme point by choosing uniformly among the `j-1` better points.
The publisher abstract explicitly identifies this Markov model and its
large-`N` iteration law.

If self-loops are deleted from the RCR coordinate chain, then from state
`j` its next strict state is uniform on `{1,...,j-1}`.  This is **literally
Ross's transition kernel** after relabelling ranks.  Therefore the embedded
strict descent, its logarithmic-scale iteration count, and any claim based
only on that skeleton receive zero contribution credit.

### 2.2 Durrett makes the mean and visit indicators explicit

Richard Durrett's authoritative public version of
[*Essentials of Stochastic Processes*, Version 3.9](https://sites.math.duke.edu/~rtd/EOSP/eosp.html),
Exercise 1.69 in the [official PDF](https://services.math.duke.edu/~rtd/EOSP/EOSP2021.pdf),
states the same strict kernel, asks for mean
`1+1/2+...+1/(i-1)`, and asks the reader to prove that the level-visit
indicators are independent with conditional visit probability `1/j`.

This directly subtracts the strict-chain harmonic mean and the fact that a
strict descent from above visits level `k` with probability `1/k`.  In RCR,
the transient one-dimensional Green row is then obtained by adjoining the
elementary geometric self-dwell at `k`.  The focused package proves the lazy
chain formulas independently, but it does not count the strict visit
mechanism as residual credit.

### 2.3 Consequence for the RCR independent-geometric law

Durrett's independent strict-level indicators also explain why the lazy RCR
PGF factors.  If a strict level `k<m` is skipped, its dwell contribution is
zero; if it is visited, its positive dwell is geometric with departure
probability `(k-1)/k`.  The mixture PGF is

```text
(1-1/k)+(1/k)[(k-1)z/(k-z)]=(k-1)/(k-z).
```

The starting level contributes `(m-1)z/(m-z)`.  Multiplication recovers
`z(m-1)!/prod_(k=2)^m(k-z)`.  Thus even though this exact lazy transform was
not found printed in the screened records, its proof engine is very close to
an owned strict-chain result.  It remains mathematically useful but is
**owner-thin-to-amber**, not a safe standalone contribution.

## 3. Decreasing-chain citation chain

| source | scope actually owned | RCR relation and subtraction |
|---|---|---|
| Bernard Van Cutsem and Bernard Ycart, [“Renewal-Type Behavior of Absorption Times in Markov Chains”](https://doi.org/10.2307/1427901), *Advances in Applied Probability* 26 (1994), 988--1005 | lower-triangular integer-valued chains; asymptotic moments and CLT via renewal/stochastic comparison | RCR is lower triangular; generic absorption/renewal framework is zero credit; the abstract does not state the RCR finite PGF or rectangle target atlas |
| Bénédicte Haas and Grégory Miermont, [“Self-similar scaling limits of non-increasing Markov chains”](https://doi.org/10.3150/10-BEJ312), *Bernoulli* 17 (2011), 1217--1247 | scaling limits and absorption-time convergence for non-increasing integer chains | owns broad non-increasing-chain asymptotics; RCR claims no scaling limit |
| Gerold Alsmeyer and Alexander Marynych, [“Renewal approximation for the absorption time of a decreasing Markov chain”](https://doi.org/10.1017/jpr.2016.39), *Journal of Applied Probability* 53 (2016), 765--782; [arXiv record](https://arxiv.org/abs/1509.01704) | asymptotic absorption laws for eventually **strictly** decreasing chains under renewal-type hypotheses | the RCR chain itself has self-loops, while its embedded chain is strict; this source owns the broad framework, not the printed finite RCR conjunction |
| Sheldon M. Ross, [1982 paper](https://doi.org/10.1016/0377-2217(82)90177-1) | the exact strict uniform-better-rank transition | direct kernel owner for the embedded RCR coordinate skeleton |

The Alsmeyer--Marynych publisher bibliography itself points to Ross and to
Van Cutsem--Ycart, so the strict-kernel hit is part of the closest paper's
citation chain rather than an unrelated keyword match.

## 4. Record and random-recursive-tree subtraction

The embedded strict transition `j -> Uniform{1,...,j-1}` is also the ancestry
label chain of the newest vertex in a uniform random recursive tree.  Luc
Devroye's [“Applications of the Theory of Records in the Study of Random
Trees”](https://doi.org/10.1007/BF02915448), *Acta Informatica* (1988), is the
record-theory owner cited by later work.  A modern primary account by Colin
Desmarais, [“Depths in random recursive metric
spaces”](https://doi.org/10.1017/jpr.2024.32), *Journal of Applied
Probability* 61 (2024), 1448--1462, explicitly recalls that random-recursive-
tree insertion depth is a sum of independent Bernoulli variables and is the
number of records in a uniform permutation.

Accordingly, any presentation of the strict RCR skeleton as a new record,
ancestor, or recursive-tree chain is prohibited.  The lazy dwell law and the
two-coordinate anchored rectangle are different literal objects, but record
terminology supplies no residual credit.

## 5. Leader-election and geometric-max screen

Rudolf Grübel and Klaas Hagemann,
[*Leader election: A Markov chain approach*](https://arxiv.org/abs/1604.03047),
study binomial-thinning participant chains and durations related to maxima of
geometric samples, using discrete potential theory.  Gerold Alsmeyer,
Zakhar Kabluchko, and Alexander Marynych,
[*Leader election using random walks*](https://arxiv.org/abs/1607.08731),
is another nearby record returned by the citation/keyword screen.

Neither transition is `j -> Uniform{1,...,j}` and neither source inspected
states the RCR rectangle law.  They are therefore **nonowners of the literal
update**, but they subtract any broad claim that geometric maxima, decreasing
participant chains, or potential-theoretic Markov analysis are new ideas.

## 6. Literal rectangle search result

The anchored-rectangle queries returned anchored-rectangle packing,
geometric nested-rectangle problems, spatial range-search material, and
generic random contraction/optimization papers.  No returned primary record
used the literal discrete update

```text
[1,x]x[1,y] -> [1,I]x[1,J] with (I,J) uniform in the current cell set,
```

or printed the conjunction of its exact absorption clock and its
every-target Green atlas.

This is a **bounded literal direct-owner non-hit only**.  It is not evidence
that no such owner exists.

## 7. Residual-credit accounting

| component | owner disposition |
|---|---|
| strict uniform descent | direct Ross/Durrett hit; zero credit |
| strict-level visit probability and independent indicators | explicit Durrett treatment; zero credit |
| random-recursive-tree/record interpretation | Devroye and later RRT literature; zero credit |
| lower-triangular absorption/renewal asymptotics | Van Cutsem--Ycart, Haas--Miermont, Alsmeyer--Marynych; zero credit |
| first-step recurrences and finite resolvents | generic Markov-chain algebra; zero credit |
| independent geometric products and maximum-of-clocks identity | generic probability machinery; zero credit |
| tensor-product transition factorization | generic product-chain fact; zero credit |
| exact lazy-coordinate finite formulas | correct and apparently unprinted in the bounded screen, but mechanically close to owned strict visits; amber |
| literal anchored rectangle plus full 2D clock/every-target potential conjunction | bounded direct-owner non-hit; possible residual, unresolved |

The owner-subtracted case is therefore narrower than the scouting report:
the package is not killed mathematically, but it no longer qualifies as
cleanly `OWNER_THIN`.

## 8. P1--P156 collision matrix

| occupied paper | occupied carrier/update | apparent collision | literal and proof-engine separation | disposition |
|---|---|---|---|---|
| P100, least-valuation digit erasure | deterministic arithmetic map clearing one base-`p` digit contribution | finite absorption, exact clock distribution over starting states | RCR is stochastic, lower-triangular, and spatial; its time law is conditional on a fixed start, not a transient-depth enumerator | no literal collision; generic absorption vocabulary zero credit |
| P101, random cap--floor synchronization | iid cap/floor maps of `[0,1]` until a random composition becomes constant | strongest internal collision: independent-geometric absorption representation, explicit moments, and sharp exponential tail | P101 uses record extrema of iid thresholds and a two-geometric synchronization time; RCR uses state-dependent uniform descent, `m-1` distinct geometric factors, a two-axis maximum, and every-target spatial potentials | no conjugacy found, but geometric-sum/tail engine is occupied and receives zero credit |
| P121, product-plus-one coalescence | uniformly chosen adjacent merger `(x,y)->xy+1`; random terminal statistic coupled to Yule histories | stochastic histories, rational/generating-function analysis | P121 has a fixed merger clock and studies terminal laws, antichain markers, and pole ladders; RCR has a variable absorption clock and monotone rectangle state | no literal or theorem-silhouette collision; generic PGF use zero credit |
| P146, uniform ear deletion | uniformly delete a polygon vertex; fixed deletion clock; triangulation endpoint masses via dual-tree hooks | random nested deletion/contraction language | RCR permits self-loops and multi-level jumps, has no triangulation endpoint or hook history, and studies time/potential rather than endpoint fibres | separated |
| P148, even-level plane-tree contraction | deterministic deletion of odd tree levels; image/inverse enumeration | word `contraction` and nested state shrinkage | different carrier, deterministic simultaneous update, image/inverse theorem, and algebraic-series engine | lexical collision only |
| P151, unequal-spider first passage | simple random walk on a finite spider until an absorbing labelled leaf | exact absorption PGF, moments, marked target, first-passage language | P151 is a reversible nearest-neighbour walk using continuants and centre-excursion renewal; RCR is a monotone partial-order chain using triangular resolvents and tensor products; RCR has no endpoint inverse | no literal collision; generic hitting-time/Bellman algebra zero credit |
| P152, triangular-book triad absorption | random active-triad update, lumped count chain with a complement jump | rational absorption transform, explicit mean, parity mark, exponential certificate | P152's reflected Bellman equation and Chebyshev elimination are absent from RCR; RCR uses uniform lower intervals, independent axes, partial fractions, and all-target Green sums | no literal or dominant-engine collision; generic finite absorption zero credit |

P101 is the closest **internal proof-silhouette** collision.  P151 and P152 are
the closest **presentation** collisions because they already establish the
batch standard for boundary-complete stochastic absorption transforms.
P121 is not an absorption-clock owner and is included because the requested
audit explicitly named it and because it occupies random-history generating
functions.

## 9. Decision and next gate

The exact theorem package survives.  The owner label changes from the
scouting `OWNER_THIN` to:

```text
MATHEMATICS: PROVABLE AS STATED
OWNER:       AMBER
EXTERNAL:    HOLD_EXTERNAL
```

Before any paper number or formal manuscript is assigned, a specialist must
check whether the literal two-dimensional anchored-rectangle clock plus
every-target potential is a substantive residual theorem conjunction rather
than a routine tensor/lazification of Ross--Durrett.  Absence of a literal
title hit is insufficient.  No posting, circulation, author contact,
submission, priority language, or novelty claim is authorized.
