# Replacement stochastic scout, round 2: twenty genuinely random finite systems

**Audit date:** 2026-08-31 UTC  
**Scope:** independent replacement discovery; no paper number and no Git action  
**Literal systems retained in the ledger:** 20  
**Post-repair disposition:** `SF1` is eligible only as an anonymous internal
short probability note under **`HOLD_EXTERNAL`**; nineteen systems remain
permanently killed

This round deliberately excludes deterministic closures, affine/matroid span
processes, exclusion and `k`-mer transport, generic coalescence, ordinary
random walks, sorting/carrying, tree pruning, linear-extension clocks, and
cosmetic scheduler changes.  Every retained row makes a state-dependent random
choice.  The exact program found several correct laws, but only the sunflower
transversal law remains large enough after owner subtraction to merit one more
gate.

No bounded search miss is treated as novelty evidence.  The independent gate
in [`../../phase1/HOSTILE_GATE_SF1.md`](../../phase1/HOSTILE_GATE_SF1.md)
returned `REPAIR`: the formulas survived, while the owner and boundary text
required the patches now incorporated below.  The resulting status is
`POST_REPAIR_INTERNAL_SHORT_NOTE_ONLY/HOLD_EXTERNAL`, not a priority or
publication claim.

## 1. Executable breadth contract

[`verify_stochastic_round2.py`](verify_stochastic_round2.py) uses Python
integers and `fractions.Fraction` only.  It performs no floating-point
calculation, pseudorandom sampling, third-party import, network access, seed,
or timestamp lookup.  Distinct labelled events retain their exact
probabilities even when they lead to the same next state.

The frozen stdout is [`CANONICAL.txt`](CANONICAL.txt).  From this directory,
the byte-replay command is

```bash
cmp -s CANONICAL.txt <(PYTHONDONTWRITEBYTECODE=1 python3 verify_stochastic_round2.py)
```

The run covers **173,928 parameter-labelled inputs** and makes **1,722,625
exact assertions**.  Of these, 1,722,622 belong to individual systems and
three are global system-count, unique-handle, and nonempty-row sentinels.
Finite enumeration is falsification evidence; the formulas below still need
ordinary proofs and owner review.

## 2. Permanent twenty-system ledger

| ID | Literal stochastic update | Complete finite pilot | Exact signal and disposition |
|---|---|---:|---|
| `SF1` | In a disjoint sunflower forest, choose an uncovered edge with probability proportional to its fixed rate, then choose a vertex uniformly from that edge; record the vertex and delete every edge it hits. | Uniform `c=1..3`, `m=1..5`, `p_i=1..4`; weighted aggregate `c<=2`, `m<=3`, `p_i,lambda_i<=3`; unit-rate actual-vertex checks; four two-component forest controls. 5,812 inputs, 165,986 assertions. | Every checked aggregate and resolved endpoint, weighted integral, uniform discrete selection-count law, and forest control agrees. **`POST_REPAIR_INTERNAL_SHORT_NOTE_ONLY/HOLD_EXTERNAL`.** The frozen canonical stdout retains its pre-gate scout label. |
| `MS1` | In a perfect matching on equally many red and blue vertices, choose a red-red edge and a blue-blue edge uniformly and replace them by one of their two bichromatic 2-switches uniformly. | Every perfect matching for `n=1..6`; 11,464 inputs, 171,876 assertions. | With `k` bad pairs the `k! 2^k` bichromatic endpoints are uniform and the clock is `k`.  Correct but one factorisation on the classical switch carrier. **Kill.** |
| `PR1` | Independently colour every element of a current set partition by a fair bit and simultaneously split every block by colour. | Every partition of `[n]`, `n=1..5`; complete kernels for `t=0..5`; 75 inputs, 3,129 assertions. | All 2,604 target cells equal the iid-signature formula.  This is random trie/hash collision in partition notation. **Kill direct.** |
| `PK1` | Choose a remaining 3-edge uniformly, accept it into a packing, and delete every intersecting edge. | Every subhypergraph of three named seven/eight-edge 3-graphs; 512 inputs, 6,277 assertions. | 486 multi-terminal and 63 variable-clock sources, at most seven maximal packings.  Random greedy hypergraph matching/RSA owns the process. **Kill.** |
| `TR1` | Choose a present triangle uniformly and then delete one of its three edges uniformly. | Every graph on four and five labelled vertices; 1,088 inputs, 6,099 assertions. | 659 multi-terminal and 338 variable-clock sources; as many as 207 triangle-free endpoints. **Kill no closed atlas.** |
| `ER1` | Choose a nonsingleton hyperedge uniformly and erase a uniform incident vertex from that edge, merging duplicate edges. | Every family on `[3]` and every at-most-four-edge family on `[4]`; 2,069 inputs, 12,390 assertions. | 2,005 multi-terminal and 1,340 variable-clock sources, at most 12 singleton-support endpoints. **Kill generic fragmentation/merger.** |
| `TM1` | In a complete tripartite graph, choose a current edge uniformly, match its endpoints, and remove them. | Every count state `(a,b,c)` in `{0,...,6}^3`; 343 inputs, 2,382 assertions. | 216 multi-residual-species and 200 variable-size sources.  This is finite multispecies annihilation/RSA. **Kill owner.** |
| `CE1` | In a weighted conflict clique, choose a winner proportional to weight, then choose a different loser uniformly and delete it. | All weights in `{1,2,3}^n` and every nonempty state for `n=2..5`; 8,964 inputs, 61,110 assertions. | Survivor `i` has mass `w_i/sum_j w_j`, with fixed `|S|-1` clock.  A one-line Luce martingale. **Kill theorem-thin.** |
| `CH1` | Choose an induced chordless cycle uniformly, then choose one of its missing chords uniformly and add it. | Every labelled graph on `n=4,5`; 1,088 inputs, 6,988 assertions. | 205 sources have multiple chordal completions and 40 have variable fill clocks; support reaches eight. **Kill minimum-fill heuristic/no closed atlas.** |
| `CT1` | In a circular chord matching, choose a crossing chord pair uniformly and delete one of the two chords uniformly. | Every perfect matching on `2n` cyclic points for `n=1..5`; 1,069 inputs, 11,580 assertions. | 1,005 multi-terminal and 725 variable-clock sources.  The carrier and thinning silhouette collide with P130. **Kill internal/no law.** |
| `DC1` | Process original graph edges in a uniformly random order; independently delete or contract the selected edge with a fair coin. | Every graph on three and four vertices; 72 inputs, 3,386 assertions. | The terminal partition is exactly the component partition of Bernoulli bond percolation and the clock is the edge count. **Kill random-cluster/Tutte direct.** |
| `CN1` | In a disjoint satisfying monotone CNF, choose uniformly among all literals still belonging to unresolved clauses; a true literal resolves its clause, a false literal is discarded. | All ordered one-to-four-clause formulas from seven `(false,true)` types; 2,800 inputs, 360,200 assertions. | Total query time is a convolution of independent negative-hypergeometric first-success laws. **Kill random evaluation direct.** |
| `CR1` | From an unsatisfiable signed CNF, delete a uniformly chosen clause and stop at the first satisfiable subformula. | All 256 formulas on the eight non-tautological two-variable clauses; 1,441 assertions. | All 161 unsatisfiable starts are multi-terminal; 150 have variable clocks and support reaches 88. **Kill no factorisation.** |
| `AP1` | Choose an augmenting path of a matching uniformly and flip along it. | Every matching of `K_(2,3)`, one eight-edge six-vertex graph, and `K_4`; 50 inputs, 337 assertions. | Berge termination and the deficiency clock are exact, but 37 sources reach multiple maximum matchings. **Kill classical randomized matching algorithm.** |
| `DG1` | Choose a directed simple cycle uniformly, then delete a uniform arc on it. | Every digraph on three vertices; every at-most-five-arc digraph and the complete digraph on four vertices; 1,651 inputs, 11,843 assertions. | 1,107 multi-DAG and 266 variable-clock sources, at most 446 endpoints. **Kill feedback-arc heuristic.** |
| `SC1` | Choose a free codimension-one face uniformly and perform the corresponding elementary simplicial collapse. | Every labelled complex on one through four vertices; 193 inputs, 1,290 assertions. | Euler characteristic is pathwise invariant, but 131 sources have multiple cores and 18 have variable clocks. **Kill simple-homotopy owner/no terminal law.** |
| `BF3` | Choose a currently essential variable of a Boolean function uniformly, assign it a fair bit, restrict, and stop when the function is constant. | Every truth table on zero through four variables; 65,814 inputs, 526,492 assertions. | Terminal-one mass is exactly the original truth-table bias; 65,752 functions have variable clocks.  This is the decision-tree restriction martingale. **Kill theorem-thin.** |
| `LM1` | Choose a crossing pair of sets uniformly and delete one member uniformly. | Every family on `[3]` and every at-most-five-set family on `[4]`; 5,072 inputs, 29,636 assertions. | 4,276 multi-laminar and 2,382 variable-clock sources, at most ten endpoints. **Kill arbitrary laminarisation.** |
| `GV1` | Choose an induced `P3` uniformly and delete one of its three vertices uniformly, stopping at a cluster graph. | Every induced state of every five-vertex graph; 32,768 inputs, 172,572 assertions. | 8,732 multi-terminal and 3,617 variable-clock sources, at most 15 endpoints. **Kill cluster-deletion heuristic.** |
| `CF1` | Choose an odd cycle uniformly and delete one of its vertices uniformly, stopping at a bipartite induced graph. | Every induced state of every five-vertex graph; 32,768 inputs, 167,608 assertions. | 3,768 multi-terminal and 860 variable-clock sources, at most 15 endpoints. **Kill odd-cycle-transversal heuristic.** |

## 3. `SF1`: the one surviving theorem contract

### 3.1 Literal process

Let `m,c,p_1,...,p_m` be positive integers.  Let a sunflower have core `C`,
`|C|=c`, and pairwise disjoint petals `P_1,...,P_m`, `|P_i|=p_i`.  Its edges
are

```text
E_i = C union P_i.
```

Give edge `E_i` a fixed positive real rate `lambda_i`.  From the unhit edges,
choose `E_i` with probability `lambda_i` divided by the total active rate,
then choose one vertex uniformly from `E_i` and adjoin it to the output
transversal.  If the chosen vertex lies in `P_i`, only `E_i` disappears.  If
it lies in `C`, every remaining edge of that component disappears.  Different
sunflower components are vertex-disjoint.  The global scheduler uses the same
rate-proportional choice over all currently active edges.  Unit rates give the
uniform-edge rule requested by the scout.

Set

```text
r_i = p_i/(c+p_i),        q_i = c/(c+p_i),
Lambda(A) = sum_(i in A) lambda_i.
```

The endpoint is the full recorded set of selected vertices.  It is not
silently reduced after absorption, and need not be a minimal transversal:
every previously chosen petal vertex remains recorded.  This distinction is
essential for the endpoint law.

### 3.2 Exponential-race representation

Attach to each active edge an independent exponential clock of rate
`lambda_i` and, independently, an edge mark which is a uniform vertex of
`E_i`.  The earliest clock gives exactly the discrete rate-proportional edge
choice.  A petal mark deletes that edge; a core mark kills the component.
Memorylessness gives the next step.  The rates must remain fixed and the
uniform marks must be mutually independent and independent of all clocks;
these hypotheses are essential for this one-clock coupling.  Equivalently,
each edge receives one
clock and one mark at time zero: petal-marked edges firing before the first
core-marked edge are recorded, while all later edges are discarded.

This construction is generic exponential-race background and receives zero
credit.  Its value is that it makes the complete endpoint law elementary.

### 3.3 Weighted aggregate and vertex-resolved endpoint laws

For a proper subset `A proper subset [m]`, let `pi(A)` be the probability that
exactly the petals indexed by `A` fire first with petal marks, followed by a
core mark.  Put

```text
I(A) = sum_(B subset A) (-1)^|B|
       / (Lambda([m] \ A) + Lambda(B)).                    (SF1.1)
```

Then the all-parameter aggregate law is

```text
pi(A) = [product_(i in A) r_i]
        [sum_(j notin A) q_j lambda_j] I(A).              (SF1.2)
```

Indeed, if the terminal core clock rings at time `t`, every `i in A` must
have a petal mark and clock below `t`, while every edge outside `A` except the
terminal edge must have clock above `t`.  Thus

```text
pi(A) = [product_(i in A) r_i]
        [sum_(j notin A) q_j lambda_j]
        integral_0^infinity exp(-Lambda([m]\A)t)
        product_(i in A)(1-exp(-lambda_i t)) dt,
```

and expanding the product proves (SF1.1)--(SF1.2).  The remaining aggregate
endpoint, in which every petal fires and no core is ever selected, has mass

```text
pi(all petals) = product_i r_i.                            (SF1.3)
```

These formulas resolve to actual vertices, not merely petal masks.  Fix
`x_i in P_i` for `i in A` and `y in C`.  The precise terminal transversal
`{x_i : i in A} union {y}` has probability

```text
pi(A) / [c product_(i in A) p_i].                         (SF1.4)
```

Every precise all-petal transversal `{x_1,...,x_m}` has probability

```text
product_i 1/(c+p_i).                                      (SF1.5)
```

Equation (SF1.4) follows because, conditional on an aggregate marked history,
the core vertex is uniform in `C` and each selected petal vertex is uniform in
its own `P_i`.  The verifier separately enumerates these actual marks for
`c<=2`, `m<=3`, `p_i<=3`; it does not infer the resolved law merely by summing
the mask process.

### 3.4 Uniform scheduler: complete discrete selection-count law and PGF

For unit rates and `|A|=k`, the beta integral in (SF1.1) is

```text
I(A) = 1 / [(m-k) binom(m,k)].
```

Consequently

```text
pi(A) = [product_(i in A) r_i] / binom(m,k)
        * [sum_(j notin A) q_j]/(m-k).                    (SF1.6)
```

Let `T` be the number of selected vertices before the component absorbs and
write `e_t` for the elementary symmetric polynomial.  Define

```text
s_t = e_t(r_1,...,r_m)/binom(m,t),       s_0=1.
```

The event `T>t` says that the first `t` distinct edges in a uniform random
edge order all carry petal marks, so

```text
Pr(T>t) = s_t,                     0<=t<m,
Pr(T=t) = s_(t-1)-s_t,             1<=t<m,
Pr(T=m) = s_(m-1).                                      (SF1.7)
```

The top atom contains two disjoint mechanisms and must not be identified with
either one alone:

```text
Pr(T=m) = product_i r_i
          + (1/m) sum_j q_j product_(i != j) r_i
        = e_(m-1)(r_1,...,r_m)/m.
```

The first term is the all-petal endpoint; the sum is the event that the first
`m-1` choices are petals and the last choice is a core vertex.

Hence

```text
G(z) = sum_(t=1)^(m-1) (s_(t-1)-s_t) z^t + s_(m-1) z^m,
E[T] = sum_(t=0)^(m-1) s_t,
E[T^2] = sum_(t=0)^(m-1) (2t+1)s_t,
Var(T) = E[T^2]-E[T]^2.                                 (SF1.8)
```

The heterogeneous petal sizes matter: replacing all `r_i` by their mean loses
the target-resolved law and generally changes every symmetric polynomial of
degree at least two.

### 3.5 Forest factorisation

For disjoint sunflower components `H_1,...,H_d`, use independent clocks and
marks on their disjoint edge sets.  Each projected marked history is therefore
independent of all other components.  Sorting all component clock rings gives
the global rate-proportional scheduler, while deleting the unused clocks of a
component after its first core mark changes no projected history.  It follows
that

```text
Law(endpoint forest) = tensor_product_a Law(endpoint H_a),
T_forest = sum_a T_a,
G_forest(z) = product_a G_a(z).                           (SF1.9)
```

Independence and dissociation of restrictions of an exponential/size-biased
order to disjoint item sets are generic owned facts and receive zero credit.
The displayed consequence identifies the fully marked, stopped endpoint and
clock for this particular carrier; it is not a claim that forest independence
is a new general principle.  This is a coupling proof, not an inference from
the dynamic program.  The program independently re-enumerates three unit-rate
two-component forests and one unequal-rate forest, comparing every joint
endpoint mass and the complete discrete choice-count convolution.

### 3.6 Post-repair proof plan for the internal note

1. Establish the one-clock/one-mark exponential representation and identify
   terminal transversals exactly.
2. Condition on the terminal core time and integrate to obtain
   (SF1.1)--(SF1.3).
3. Resolve the independent uniform vertex marks to prove
   (SF1.4)--(SF1.5).
4. In the unit-rate case, evaluate the beta integral and derive the
   elementary-symmetric tail, mass, PGF, and moments.
5. Couple disjoint components by independent clock families to prove the
   tensor-product endpoint law and discrete selection-count convolution; the
   elapsed completion time is instead the maximum of component stopping times.

No step should be sold as a new exponential-race, beta-integral, or symmetric-
polynomial method.  The claim is only the complete exact atlas for this
literal weighted sunflower process.

## 4. Fresh owner gate and exact zero-credit contract

### 4.1 Directly owned background

- Erdős and Rado's original
  [*Intersection Theorems for Systems of Sets*](https://doi.org/10.1112/jlms/s1-35.1.85)
  (1960) owns the sunflower/Delta-system carrier.  The definition, extremal
  motivation, core, and petal geometry receive zero credit.
- Bar-Yehuda's
  [*One for the Price of Two: A Unified Approach for Approximating Covering
  Problems*](https://doi.org/10.1007/s004530010009) (2000), Section 5.1 and
  Theorem 6, directly owns the general hypergraph Pitt process: select an
  unhit edge, randomly select a vertex in it, add that vertex to the cover,
  and delete hit edges; in the unweighted case the vertex is uniform.  The
  `SF1` contribution does not include this covering algorithm, its validity,
  or any approximation guarantee.  Its fixed rate-proportional edge scheduler
  is merely one randomized edge-selection policy.
- Pitt's 1985 Yale technical report, *A Simple Probabilistic Approximation
  Algorithm for Vertex Cover* (TR-404), owns the graph ancestor “choose an
  uncovered edge and a random endpoint.”  Gupta, Ligett, McSherry, Roth, and
  Talwar explicitly reproduce that rule on page 8 of
  [*Differentially Private Combinatorial Optimization*](https://drops.dagstuhl.de/storage/16dagstuhl-seminar-proceedings/dsp-vol09511/DagSemProc.09511.6/DagSemProc.09511.6.pdf).
  Therefore the generic random greedy covering algorithm and its validity as a
  cover receive zero credit.
- Chvátal and McDiarmid's
  [*Small transversals in hypergraphs*](https://doi.org/10.1007/BF01191201)
  and the subsequent transversal literature own greedy hypergraph-cover
  framing and performance-bound questions.  `SF1` claims no approximation
  ratio or new transversal-number bound.
- Plackett's
  [*The Analysis of Permutations*](https://doi.org/10.2307/2346567) (1975)
  owns the finite weighted-ranking model, while Gnedin's
  [*Infinite Size-Biased Orders*](https://arxiv.org/abs/2309.15799), also
  published as [DOI 10.1007/s11083-026-09743-2](https://doi.org/10.1007/s11083-026-09743-2),
  treats positive-rate exponential representations and dissociation of
  restrictions.  Rate-proportional sampling without replacement, independent
  exponential representation, finite ranking probabilities, memorylessness,
  and independence/dissociation on disjoint components all receive zero
  credit.
- Beta integrals, inclusion--exclusion, elementary symmetric polynomials,
  tail-sum moments, and independent-product PGFs are standard probability
  tools and receive zero credit.

For the negative controls, Bal and Bennett's
[*The Matching Process and Independent Process in Random Regular Graphs and
Hypergraphs*](https://doi.org/10.37236/10698) explicitly gives the uniform-edge
random greedy hypergraph matching process, consuming `PK1`; Dyer, Jerrum, and
Müller's [*On the switch Markov chain for perfect
matchings*](https://arxiv.org/abs/1501.07725) confirms the classical perfect-
matching switch carrier surrounding `MS1`.  These sources are not used to
inflate the `SF1` residual.

### 4.2 Bounded non-hit

Fresh searches included the literal conjunctions

```text
"random greedy" sunflower hypergraph transversal random edge vertex
randomized hitting set choose uncovered set random element sunflower
"choose an uncovered edge" "random vertex" hypergraph
sunflower graph Pitt randomized vertex cover stopping time
Delta-system random greedy transversal probability distribution
sunflower hypergraph stochastic transversal edge rates
```

They found Pitt-type vertex-cover rules, greedy transversal bounds, sunflower-
free independent-set processes, generic random greedy matchings, and sunflower
kernelization.  They did **not** locate a primary source printing the literal
sunflower process together with its weighted all-endpoint law, actual-vertex
resolution, full discrete selection-count PGF, and forest tensor product.
This is only a
bounded non-hit as of the audit date.  It is not a novelty certificate, and a
direct owner of this package would kill `SF1` immediately.

### 4.3 Residual contribution allowed to survive

After subtraction, the sole contribution contract is:

```text
heterogeneous sunflower petals + fixed edge rates
    -> complete aggregate endpoint integral
    -> complete actual-vertex terminal-transversal law
    -> unit-rate elementary-symmetric discrete selection-count PGF and moments
    -> independent forest endpoint tensor product and choice-count convolution.
```

The process, the term “sunflower,” random-edge/random-vertex greedy covering,
the size-biased/exponential order, disjoint-order independence, and every
generic probability tool are explicitly zero contribution.  The residual is
appropriate only for an anonymous internal short exact-probability note under
`HOLD_EXTERNAL`.  It is not a broad new theory of hitting sets.  The frozen
finite evidence is scoped narrowly: weighted aggregate endpoints are
exhaustively checked only over the stated frozen range; actual-vertex
endpoints are separately checked at unit rates; forest factorisation is
checked on four two-component controls.  Weighted vertex-resolved endpoints
and arbitrary forests are proved symbolically, not exhaustively enumerated.

## 5. P1--P131 and first-117 firewall

The twenty final handles were compared literally with the occupied P1--P131
maps and all systems in the earlier P132--P136 scout lanes.  Two attractive
draft rows failed this test.  Iid random ambient-hyperplane intersection had a
beautiful Möbius kernel, but the exact literal system already appears as `R7`
in `papers112_116_sequence/scouting/ROOT_SCOUT.md`; it was removed and replaced
by `MS1`.  Uniform permutation cycle-splice deletion was also removed because
it recycled the local cycle surgery of P105 under a random scheduler, the very
cosmetic-scheduler pattern excluded by this round; `CH1` replaces it.  Neither
removed row is counted among the twenty.

| Current systems | Closest internal occupants | Firewall result |
|---|---|---|
| `SF1` | P114 rooted-forest pruning; P121/P129 stochastic coalescence; P130 product fibres | `SF1` adds chosen vertices to a hypergraph transversal, kills a component on a core mark, and otherwise removes one petal edge.  It neither prunes a rooted carrier nor transports/coalesces mass.  Its product is probabilistic independence across disjoint components, not an inverse-fibre product.  **Literal pass; rhetoric from those papers is zero credit.** |
| `MS1`, `AP1`, `CT1` | P130 chord-matching thinning | `MS1` preserves all vertices and matching size under colour-repair switches; `AP1` flips augmenting paths; `CT1` deletes crossing chords and is the actual crowded silhouette.  Only `CT1` is killed internally, while the other two are killed by classical/thin mechanisms. |
| `PR1` | P110 cyclic shift--join partitions; P126 balanced composition refinement | `PR1` is an iid signature-refinement Markov chain, not either literal map, but binary refinement clocks and partition kernels are occupied; the external trie owner completes the kill. |
| `CH1` | P130 uses “chord” only for circle matchings; P114 uses graph deletion | Here a graph gains a diagonal of a uniformly chosen induced cycle until it is chordal, so neither internal update is literal.  The pilot nevertheless has a broad, unstructured completion law and variable clocks; classical chordal-completion/minimum-fill framing gets all algorithmic credit. |
| `PK1`, `TR1`, `ER1`, `TM1`, `DG1`, `SC1`, `LM1`, `GV1`, `CF1` | P114 deletion/peeling and P121/P129 random aggregation warnings | The carriers and witness choices are literal new maps, but their exact pilots yield either generic invariants or large unstructured terminal laws.  None is promoted by changing the carrier name. |
| `DC1` | P114 graph/forest language | The rule is edge exposure with delete/contract coins, not leaf deletion; its terminal law is nevertheless ordinary Bernoulli percolation/random-cluster background. |
| `CN1`, `CR1`, `BF3` | prior Boolean scout controls; no occupied paper map | Literal maps are new to the P1--P131 paper list, but negative-hypergeometric short-circuiting, clause relaxation, and the restriction martingale are textbook owners or theorem-thin. |
| `CE1` | P121/P129 weighted stochastic competition rhetoric | No literal collision, but the normalized-weight martingale proves the entire result in one line. |

The firewall is about the joint carrier and update, not a ban on shared words
such as “absorption,” “fibre,” or “PGF.”  Conversely, changing only the carrier
while retaining an occupied theorem engine earns no slot.

## 6. Final decision

The hostile owner/proof gate found no mathematical counterexample but required
the repairs now present in this document.  `SF1` therefore advances as the
**only** theorem-scale residual from this round, with status
**`POST_REPAIR_INTERNAL_SHORT_NOTE_ONLY/HOLD_EXTERNAL`**.  Any defensible note
must prove (SF1.1)--(SF1.9), keep the actual vertex-resolved endpoint law
central, and state every generic algorithmic/probabilistic ingredient as zero
credit.  It is not cleared for external submission.

`MS1` is the nearest runner-up but is permanently killed: after recognising
the switch carrier, its uniform `k!2^k` endpoint law is just a bijection between
the `k` red pairs and `k` blue pairs plus one orientation bit per pair.  The
other eighteen rows have direct owners, theorem-thin martingales, internal
collisions, or no closed terminal atlas.  No second candidate is promoted.
