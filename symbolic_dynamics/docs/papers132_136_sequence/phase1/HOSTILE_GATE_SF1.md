# Independent hostile gate: SF1 sunflower-transversal process

**Audit date:** 2026-08-31 UTC  
**Reviewer role:** independent hostile proof, owner, value, and collision gate  
**External status:** `HOLD_EXTERNAL`  
**Verdict:** **`REPAIR`** -- the stated formulas are correct, but the current
owner subtraction omits a direct hypergraph-process owner and understates how
much of the proof engine is ordinary size-biased-order background.  This is
not a fifth-paper quota pass.  It becomes an internal short-note pass only
after the exact repairs in Section 9 are applied and rechecked.

## 1. Audited object and immutable replay

The audited files were

- `replacement_scout/stochastic_round2/SCOUT.md`, SHA-256
  `778f3cb88413053d7fad23a8975a2340423ddfefacc733130e9ea4a4390e16f7`;
- `replacement_scout/stochastic_round2/verify_stochastic_round2.py`, SHA-256
  `65b627b2d00a6c0f7376cd6644b01ad5e5e23beed5d4b952331f310006871e22`;
- `replacement_scout/stochastic_round2/CANONICAL.txt`, SHA-256
  `27a11b16bd57ac6e0d06d612b13c40528eb59a31bf45289f1726cbc79c3f9353`.

A fresh run, with bytecode generation disabled, used

```bash
cmp -s CANONICAL.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 verify_stochastic_round2.py)
```

and returned exit code zero.  This independently re-executed the frozen
ledger of 20 systems, 173,928 parameter-labelled inputs, and 1,722,625 exact
assertions.  The SF1 row itself contains 5,812 inputs and 165,986 assertions.
The replay uses only integers and `fractions.Fraction`; it does not use
floating point or sampling.

The finite control is substantial falsification evidence, but neither its
assertion count nor the byte match is used below as a proof or novelty claim.

## 2. Literal hypotheses that must remain fixed

The formulas pass only for the following literal model.

1. A component has a nonempty core `C`, with integer `c=|C|>=1`, and
   nonempty pairwise-disjoint petals `P_i`, with integer `p_i=|P_i|>=1`.
   Its distinct edges are `E_i=C union P_i`, `1<=i<=m`, with `m>=1`.
2. Every edge has a fixed rate `lambda_i>0`.  Among currently unhit edges,
   edge `i` is selected with probability `lambda_i` divided by the sum of
   active rates.  Rates do not change after other components fire.
3. Conditional on selecting `E_i`, one of its `c+p_i` actual vertices is
   chosen uniformly.  A petal choice deletes only `E_i`; a core choice
   deletes all remaining edges of that component.
4. Every chosen vertex is retained in the recorded endpoint.  In particular,
   petal vertices chosen before a core vertex are **not** removed as redundant.
   The output is a transversal, not necessarily a minimal transversal.
5. Components in a forest have disjoint vertex and edge sets, and the global
   scheduler is rate proportional over all currently active edges.

Allowing a zero petal breaks the vertex-resolved divisions by `p_i`; allowing
a zero rate breaks denominators and removes that edge from the race.  A paper
must state positivity rather than leave it implicit in the verifier ranges.

Write

```text
r_i = p_i/(c+p_i),   q_i = c/(c+p_i),
Lambda(A) = sum_(i in A) lambda_i.
```

Thus `r_i+q_i=1`.

## 3. Independent rederivation of the one-clock coupling

Give edge `i` an independent `Exp(lambda_i)` variable `X_i` and an
independent mark `M_i`, uniform on the actual vertices of `E_i`.  Sort the
edges by increasing `X_i`.  Retain consecutive petal-marked edges until the
first core-marked edge; if no mark is in the core, retain all edges.

For a finite active set, the minimum exponential has index `i` with
probability `lambda_i/Lambda(active)`.  Conditional on the minimum and its
time, the residual clocks are independent exponentials with their original
rates.  Induction therefore gives the same marked history as the discrete
process.  This argument uses fixed rates and one independent mark per edge;
it would not justify a model that resamples rates or attaches history-dependent
marks.

The coupling also identifies the endpoint without ambiguity:

- if a core mark is first, all earlier marks are in distinct petals and the
  terminal mark is an actual core vertex;
- if no core mark occurs, every edge contributes exactly one actual petal
  vertex.

No counterexample occurs at `m=1`: the two endpoints have masses `q_1` and
`r_1`, respectively, and the stopping time is identically one.

## 4. Hostile derivation of (SF1.1)--(SF1.5)

Fix a proper subset `A` of `[m]`.  For `A` to be precisely the set of petals
chosen before absorption, every `i in A` must have a petal mark and clock
below the terminal core time, while every edge outside `A` must have clock
above that time except the edge supplying the terminal core mark.

Conditioning on terminal time `t` and summing its possible edge labels gives

```text
pi(A)
 = product_(i in A) r_i
   * sum_(j notin A) q_j lambda_j
   * integral_0^infinity
       exp(-Lambda([m]\A)t)
       product_(i in A)(1-exp(-lambda_i t)) dt.          (H4.1)
```

Expanding the finite product yields

```text
I(A) = sum_(B subset A) (-1)^|B|
       / (Lambda([m]\A)+Lambda(B)),                     (SF1.1)

pi(A) = product_(i in A) r_i
        * sum_(j notin A) q_j lambda_j * I(A).          (SF1.2)
```

The complement of a proper `A` is nonempty, so every denominator is strictly
positive.  Alternating signs in (SF1.1) do not threaten positivity because
the sum is the positive integral in (H4.1).

If all marks are petal marks, every edge eventually fires and rates only
change their order.  Therefore

```text
pi([m]) = product_i r_i.                                (SF1.3)
```

Given the aggregate event `A`, the selected mark in each `P_i`, `i in A`, is
uniform and independent, and the terminal core mark is uniform on `C`.  A
mixture over the label of the terminal edge does not change the latter
uniformity.  Hence, for fixed `x_i in P_i` and `y in C`,

```text
Pr({x_i:i in A} union {y})
 = pi(A)/(c product_(i in A) p_i).                      (SF1.4)
```

For an all-petal endpoint, mark independence gives

```text
Pr({x_1,...,x_m})
 = product_i [r_i/p_i]
 = product_i 1/(c+p_i).                                (SF1.5)
```

The formulas determine distinct endpoint cells because petals and core are
pairwise disjoint.  Summing (SF1.4) over its vertex choices recovers (SF1.2),
and summing (SF1.5) recovers (SF1.3).

## 5. Hostile derivation of (SF1.6)--(SF1.8)

For unit rates and `k=|A|<m`,

```text
I(A) = integral_0^infinity e^(-(m-k)t)(1-e^(-t))^k dt
     = Beta(m-k,k+1)
     = 1/[(m-k) binom(m,k)].
```

Substitution in (SF1.2) proves

```text
pi(A) = product_(i in A) r_i / binom(m,k)
        * sum_(j notin A) q_j/(m-k).                    (SF1.6)
```

Let `T` count selected vertices, including a terminal core vertex when one
occurs.  Under unit rates the clock order is a uniform random permutation.
For `0<=t<m`, the event `T>t` is exactly the event that the first `t` edges
have petal marks.  Averaging over their uniformly random `t`-subset gives

```text
s_t = e_t(r_1,...,r_m)/binom(m,t),
Pr(T>t)=s_t.                                             (H5.1)
```

Taking successive tail differences proves (SF1.7).  The upper endpoint needs
care: `T=m` is not the same event as “all marks are petals.”  It is the
disjoint union of

- all `m` petal marks, and
- exactly `m-1` initial petal marks followed by a core mark on the last edge.

Indeed,

```text
Pr(T=m)
 = product_i r_i
   + (1/m) sum_j q_j product_(i != j) r_i
 = (1/m) sum_j (r_j+q_j) product_(i != j) r_i
 = e_(m-1)(r_1,...,r_m)/m
 = s_(m-1).                                             (H5.2)
```

Thus the stated boundary mass is correct and does not omit the final-core
case.

For a positive integer-valued variable bounded by `m`,

```text
T   = sum_(t=0)^(m-1) 1{T>t},
T^2 = sum_(t=0)^(m-1) (2t+1) 1{T>t}.
```

Taking expectations proves both moment identities in (SF1.8), and the PGF
is the direct finite sum of the masses from (SF1.7).  The variance formula is
then definitional.  No independence between the tail indicators is assumed.

## 6. Hostile derivation of (SF1.9)

Use disjoint independent clock-and-mark families for the components.  The
endpoint and local step count of component `a` are measurable functions only
of that component's clocks and marks.  They are therefore independent across
components.  Sorting all clocks together produces the global
rate-proportional scheduler; interleaving changes no within-component order.
Discarding later clocks after a component's first core mark also changes no
already determined local endpoint.

Consequently

```text
Law(endpoint forest) = tensor_product_a Law(endpoint H_a),
T_forest = sum_a T_a,
G_forest(z) = product_a G_a(z).                          (SF1.9)
```

This remains true for unequal positive rates.  The claim would fail without
vertex-disjoint components or if a rate/mark in one component depended on
the history of another; those extensions are outside the contract.

## 7. Counterexample search and verifier limitations

The following hostile cases were checked algebraically in addition to the
fresh executable replay:

| case | attempted failure | result |
|---|---|---|
| `m=1` | singular complement or off-by-one clock | no failure; masses `q_1,r_1`, `T=1` |
| `A=empty` | missing first-core event | no failure; (SF1.2) is the competing-risk first-core mass |
| `|A|=m-1` | vanishing beta denominator | no failure; denominator is one at unit rates |
| `T=m` | all-petal event confused with the whole top clock atom | repaired explicitly by identity (H5.2) |
| unequal rates | an outside petal-marked edge with a late clock incorrectly excluded | no failure; only its clock must exceed terminal time, regardless of its mark |
| actual vertices | mixture over terminal edge makes the core mark nonuniform | no failure; every mixture component is uniform on the same core |
| two weighted components | global interleaving creates endpoint dependence | no failure; disjoint restrictions of independent clock families remain independent |

The program's terminal dynamic program is structurally independent of the
closed endpoint formulas, which makes the comparison meaningful.  Two audit
scope facts should nevertheless be stated accurately:

1. actual-vertex resolution is exhaustively tested only for unit edge rates;
   the weighted actual-vertex law is proved by conditional mark independence,
   not separately enumerated;
2. the forest factor is checked on four explicit two-component families, not
   on all forests.

Neither is a proof defect because Sections 4 and 6 give all-parameter
arguments.  A paper must not describe those finite lanes as more exhaustive
than they are.

## 8. Owner and novelty gate as of 2026-08-31

### 8.1 Direct and generic ownership that must receive zero credit

The current scout is incomplete here.

1. **The literal hypergraph covering process has a direct general owner.**
   Reuven Bar-Yehuda, “One for the Price of Two: A Unified Approach for
   Approximating Covering Problems,” *Algorithmica* 27 (2000), 131--144,
   [DOI 10.1007/s004530010009](https://doi.org/10.1007/s004530010009),
   Section 5.1 and Theorem 6, writes the Pitt algorithm for hypergraph vertex
   cover: select an edge `e`, select a random `x in e` with prescribed
   normalized reciprocal-weight probability, remove `x`, and add it to the
   cover.  In the unweighted case the selected vertex is uniform in the
   hyperedge.  The theorem explicitly treats HVC.  Choosing the edge by a
   fixed rate-proportional scheduler is a particular randomized edge-selection
   policy, not a new covering algorithm.  This is closer than the scout's
   present Pitt graph citation and must be named as the direct process owner.
2. Pitt's 1985 Yale report owns the graph ancestor.  Gupta, Ligett,
   McSherry, Roth, and Talwar's primary paper
   [*Differentially Private Combinatorial
   Optimization*](https://drops.dagstuhl.de/storage/16dagstuhl-seminar-proceedings/dsp-vol09511/DagSemProc.09511.6/DagSemProc.09511.6.pdf)
   explicitly describes the uniform-uncovered-edge/random-endpoint rule and
   attributes it to Pitt.  It is useful corroboration, but Bar-Yehuda is the
   required hypergraph citation.
3. The rate-proportional order is ordinary size-biased sampling without
   replacement / Plackett--Luce order.  Plackett's primary model is
   [“The Analysis of Permutations,” DOI
   10.2307/2346567](https://doi.org/10.2307/2346567).  Alexander Gnedin's
   [*Infinite Size-Biased Orders*, arXiv:2309.15799](https://arxiv.org/abs/2309.15799),
   now published as [DOI
   10.1007/s11083-026-09743-2](https://doi.org/10.1007/s11083-026-09743-2),
   starts from arbitrary positive-rate independent exponentials, records the
   finite chain probabilities, and states dissociation of restrictions to
   disjoint item sets.  Therefore the exponential race, memorylessness,
   size-biased ordering, and disjoint-order independence in Sections 3 and 6
   are generic owned machinery.
4. Erdős--Rado own the sunflower/Delta-system carrier, and the general
   transversal literature owns the hitting-set framing and approximation
   questions.  The paper claims no new sunflower extremal theorem or
   approximation ratio.
5. Beta integration, inclusion--exclusion, elementary symmetric polynomials,
   tail-sum moments, and multiplication of PGFs for independent sums are
   standard tools.  Merely assembling them cannot be advertised as new
   method.

### 8.2 Bounded direct-package non-hit

Separate searches through arXiv and publisher/DOI records used multiple
formulations of each of the following:

- sunflower/Delta-system + random transversal/hitting set + random edge and
  random vertex;
- Pitt/random-uncovered-edge/random-endpoint + star or hypergraph;
- size-biased/Plackett--Luce/exponential order + Bernoulli marks + first core
  or first success;
- weighted sunflower + endpoint distribution/inclusion--exclusion/PGF;
- disjoint sunflower forest + terminal law/tensor product.

The closest primary sources found were the general HVC process of
Bar-Yehuda, Plackett--Luce/size-biased-order sources, LP-rounding/repair
algorithms for general hitting set, random-greedy matching/independent-set
processes, and sunflower extremal papers.  No source located in this bounded
audit prints the conjunction

```text
fixed edge rates on one heterogeneous sunflower
 + exact selected-petal subset integral
 + actual-vertex endpoint refinement
 + unit-rate complete stopping PGF and two moments
 + disjoint-component endpoint tensor product.
```

This is a **bounded non-hit**, not evidence of priority or a novelty
certificate.  Any later direct package owner overrides this gate.

### 8.3 Residual value after honest subtraction

| claim | owner status | residual value |
|---|---|---|
| random edge / random vertex hypergraph cover | directly owned by Bar-Yehuda/Pitt | zero |
| sunflower carrier and transversal validity | classical | zero |
| exponential race and size-biased order | directly generic | zero |
| forest independence at the order level | generic dissociation | zero |
| weighted selected-petal endpoint integral | bounded non-hit | medium, but elementary |
| actual-vertex endpoint refinement | follows conditionally from uniform marks | low alone; useful as part of atlas |
| heterogeneous unit-rate stopping PGF and moments | bounded non-hit | medium-low, exact all-parameter corollary |
| complete conjunction for a sunflower forest | bounded non-hit | the only defensible short-note residual |

The residual is coherent but narrow.  Its value lies in a complete exact
atlas for a sharply specified special carrier, not in a new process or a new
probability method.  It is adequate only for an anonymous internal short
note under `HOLD_EXTERNAL`.

## 8.4 P1--P131 and current-batch collision firewall

A literal repository scan outside SF1 found no earlier use of a sunflower or
Delta-system process and no earlier “choose an unhit hyperedge, then a
uniform vertex” update.  The closest occupied systems are still distinct:

| occupied item | why it is not SF1 | zero-credit warning |
|---|---|---|
| P114 | deterministic parallel rooted-forest leaf peeling | forest vocabulary and deletion clocks are not new |
| P121 | random adjacent `xy+1` block coalescence | generic random absorption/PGF rhetoric is occupied |
| P129 | a pile moves one step rootward and coalesces on contact | exponential-clock coupling and stopping-time language are occupied/generic |
| P130 | deterministic chord retraction with target-wise fibre products | “product law” alone cannot distinguish a paper |
| killed current stochastic lanes | matching/RSA, switching, percolation, and random evaluation | no theorem may be imported from a killed scheduler variant |

SF1 has a different carrier, update, endpoint object, and proof observable, so
there is no literal P1--P131 collision.  Conversely, that absence does not
restore credit removed by the external HVC and size-biased-order owners.

## 9. Exact repair contract

The verdict changes from `REPAIR` to an internal `PASS` only after every item
below is visible in the candidate report and manuscript.

### Mandatory textual patch A -- hypotheses and endpoint meaning

Add in the first formal definition, not only in code ranges:

```text
m,c,p_1,...,p_m are positive integers and lambda_1,...,lambda_m are
positive real numbers.  Components are vertex-disjoint.  The endpoint is
the full recorded set of selected vertices and is not reduced to a minimal
transversal.
```

State that fixed rates and independent uniform marks are essential for the
one-clock coupling.

### Mandatory textual patch B -- the top clock atom

Immediately after (SF1.7), insert the displayed identity

```text
Pr(T=m)
 = product_i r_i + (1/m) sum_j q_j product_(i != j) r_i
 = e_(m-1)(r_1,...,r_m)/m.
```

Say explicitly that `T=m` contains both a final core choice and the
all-petal endpoint.  Do not identify these events.

### Mandatory owner patch C -- direct HVC owner

Add Bar-Yehuda 2000, DOI `10.1007/s004530010009`, Section 5.1/Theorem 6,
to the owner table.  The exact required subtraction is:

```text
Bar-Yehuda directly owns the general hypergraph Pitt process of selecting
an unhit edge, randomly selecting a vertex in it, adding the vertex to the
cover, and deleting hit edges; in the unweighted case the vertex is uniform.
The SF1 contribution does not include the covering algorithm, its validity,
or any approximation guarantee.
```

Calling this merely “general greedy framing” is insufficient.

### Mandatory owner patch D -- size-biased-order boundary

Cite Plackett 1975 and Gnedin arXiv:2309.15799 / DOI
`10.1007/s11083-026-09743-2`.  Give zero credit to

```text
rate-proportional sampling without replacement, independent exponential
representation, finite ranking probabilities, memorylessness, and
independence/dissociation of restrictions to disjoint components.
```

The forest theorem may claim the fully marked stopped endpoint consequence,
but not independence as a new general principle.

### Mandatory positioning patch E -- residual-only title and abstract

The title/abstract/contribution list must center the complete exact law for a
heterogeneous sunflower forest.  They must not claim a new randomized
transversal algorithm, a new exponential-race method, or a general theory of
random greedy hitting sets.  A safe one-sentence residual is:

```text
For the owned random-edge/random-vertex covering process restricted to
vertex-disjoint heterogeneous sunflowers with fixed edge rates, we derive
the complete recorded-transversal law and, at unit rates, the complete
stopping PGF and first two moments.
```

### Mandatory evidence patch F -- audit-scope honesty

State that weighted aggregate endpoints are exhaustively checked over the
frozen range, actual-vertex endpoints are separately checked at unit rates,
and forest factorisation is checked on four two-component controls.  Do not
say that weighted vertex-resolved endpoints or arbitrary forests were
exhaustively enumerated.

### Optional but useful verifier strengthening

Extend `sunflower_resolved_successors` to accept fixed rates and compare the
weighted actual-vertex law on a small all-parameter lane.  This is not needed
for mathematical correctness, but if done it changes canonical stdout,
assertion totals, hashes, and every downstream seal and therefore requires a
fresh freeze.

## 10. Acceptance test and terminal decision

The mathematical contract passes: no counterexample was found, all nine
displayed formulas were independently derived, and the fresh exact replay is
byte-identical.  The current ownership contract fails because it omits the
direct HVC owner and does not yet explicitly subtract the modern
size-biased-order/dissociation source.

Therefore:

```text
CURRENT_VERDICT=REPAIR
PROOF_STATUS=PASS
FRESH_BYTE_REPLAY=PASS
DIRECT_PROCESS_OWNER_STATUS=FAIL_UNTIL_BAR_YEHUDA_ADDED
SIZE_BIASED_ENGINE_STATUS=FAIL_UNTIL_PLACKETT_GNEDIN_SUBTRACTED
INTERNAL_COLLISION_STATUS=PASS_WITH_ZERO_CREDIT_BOUNDARY
POST_REPAIR_ELIGIBILITY=INTERNAL_SHORT_NOTE_ONLY
EXTERNAL_STATUS=HOLD_EXTERNAL
```

Applying Sections 9A--9F without enlarging the claims is a mechanical repair;
after an independent text recheck it is sufficient for `PASS`.  Failure to
make any one of owner patches C--E is a `KILL`, because the remaining paper
would present an owned general process or generic proof engine as its advance.
