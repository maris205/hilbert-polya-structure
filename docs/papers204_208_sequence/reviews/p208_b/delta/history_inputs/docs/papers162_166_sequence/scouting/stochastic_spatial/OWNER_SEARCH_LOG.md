# Bounded primary-source owner log — stochastic/spatial scout

**Search date:** 2026-09-02 UTC  
**Batch:** P162–P166 breadth intake  
**External status:** `HOLD_EXTERNAL`

## Scope and asymmetry

The owner screen followed the exact literal update and theorem conjunction,
not just the carrier name.  Public web, DOI/publisher records, arXiv, and the
P1–P161 local corpus were searched.  Only primary research papers are used as
positive owner evidence below.  Search snippets, encyclopedias, lecture notes,
forums, theses, and secondary surveys were not used to establish an owner hit.

This is bounded, not systematic: there was no MathSciNet/Zentralblatt closure,
no complete backward/forward citation traversal, no non-English database
search, and no specialist contact.  The logic is asymmetric:

- a verified direct hit or exact internal reduction can kill;
- a non-hit means only that these queries did not return a direct paper;
- no non-hit establishes novelty, priority, authorship, freedom to operate, or
  permission to release.

## DCI — odd-dihedral common-centralizer descent

Literal query target: iid `g_1,...,g_t` in `D_(2n)`, the nested state
`C(g_1) cap ... cap C(g_t)`, its first arrival at the centre, all target
centralizer fibres, and recovery of odd `n` from the survival tail.

Queries included:

- `dihedral group common centralizer random elements centralizer intersection`
- `intersection of centralizers dihedral group probability`
- `simultaneous commuting probability finite groups tuples`
- `higher commuting probability dihedral finite spectrum`

Decisive primary hit:

- Levit and Shwartz, [*Higher Commutativity in Finite Groups: Exact
  Asymptotics and Finite Spectrum*](https://arxiv.org/abs/2605.02071)
  (2026), studies the probability that an iid finite-group tuple commutes
  pairwise, proves a finite Dirichlet-spectrum expansion and recurrence, and
  gives an inverse finite-spectrum theorem.

Zero-credit structural owner:

- Ashrafi, [*On Finite Groups with a Given Number of
  Centralizers*](https://doi.org/10.1007/s10011-000-0139-5) (2000), studies
  finite groups by their element-centralizer counts.

For odd dihedral groups,

```text
common centralizer is noncentral
iff all sampled elements lie in the rotation subgroup
   or in one fixed reflection centralizer
iff the sampled tuple commutes pairwise.
```

Therefore the proposed survival law and its spectral inverse are a literal
specialization of the 2026 higher-commutativity object.  Splitting the same
count into `G`, rotation, individual-reflection, and centre fibres is correct
but theorem-thin after subtraction.

**Decision:** `KILL_DIRECT_TEMPORAL_OWNER`.

## LSC — uniform lattice-simplex contraction

Literal query target: from `Delta_m^d`, sample a uniform lattice point, keep
only its `ell_1` shell index as the next radius, and derive the absorption PGF,
Green row, and dimension inverse.

Queries included:

- `random point lattice simplex Markov chain contraction`
- `random decreasing Markov chain weighted lower state absorption exact`
- `discrete lower weak record values Markov chain exact distribution`
- `finite support weak record values exact distribution`

No primary record was returned for the *geometric drawing* of a nested lattice
simplex.  This is not a novelty result.  More importantly, a direct proof-
engine owner was returned:

- Stepanov, Balakrishnan, and Hofmann, [*Exact Distribution and Fisher
  Information of Weak Record
  Values*](https://doi.org/10.1016/S0167-7152(03)00132-9) (2003), derives
  exact weak-record-value distributions for lattice and non-lattice parents,
  explicitly including finite-atom support.
- Chandler, [*The Distribution and Frequency of Record
  Values*](https://doi.org/10.1111/j.2517-6161.1952.tb00115.x) (1952), is the
  primary lower-record starting point.
- Alsmeyer and Marynych, [*Renewal Approximation for the Absorption Time of a
  Decreasing Markov Chain*](https://arxiv.org/abs/1509.01704) (2015), is a
  primary broad decreasing-chain neighbour; it is asymptotic and does not by
  itself own the exact simplex formulas.

If the finite parent masses are the simplex shell sizes
`w_k=C(k+d-1,d-1)`, the successive lower weak record values have exactly
`P(m,k)=w_k/sum_(j<=m)w_j`, including equality holds.  Thus the entire radius
chain, not merely an analogy, is the finite-support lower weak-record chain.
The shell identity selects a parent distribution but does not leave a second
paper-sized mechanism after exact record-law subtraction.

**Decision:** `KILL_DIRECT_RECORD_ENGINE`.

## QHI and HCI — finite-field rank transfers

Queries included:

- `rank distribution random matrices finite fields exact`
- `random hyperplane intersection finite vector space distribution`
- `Heisenberg group common centralizers random elements rank`

Primary rank owner:

- Fulman and Goldstein, [*Stein's Method and the Rank Distribution of Random
  Matrices over Finite Fields*](https://arxiv.org/abs/1211.0504) (2012),
  explicitly treats finite-field random-matrix rank distributions and their
  exact point probabilities as the starting law.
- Salmond, Grant, Grivell, and Chan, [*On the Rank of Random Matrices over
  Finite Fields*](https://arxiv.org/abs/1404.3250) (2014), is a second primary
  rank-distribution record.

`QHI` is row-rank with rows conditioned nonzero.  `HCI` is ordinary row-rank
in dimension two after quotienting the Heisenberg centre.  Gaussian-binomial
target fibres are standard subspace Möbius counts.  Internally, P109 already
contains uniform pointed subspace fibres and rank-resolved temporal laws;
P111 and P135 occupy the Heisenberg and centralizer carriers.

**Decisions:** `QHI = KILL_RANK_ENGINE`; `HCI = KILL_EXACT_RANK_TRANSFER`.

## ORW — orthocentric random replacement

Queries/records were checked against the already verified P161 source chain:

- Kocik and Solecki, [*Disentangling a
  Triangle*](https://doi.org/10.4169/193009709X470065) (2009), owns the
  orthocentric-system identity.
- Wildberger, [*Neuberg Cubics over Finite
  Fields*](https://arxiv.org/abs/0806.2495) (2008), supplies the finite-field
  metric setting.

P161 already owns the literal four-window orthocenter recurrence.  Choosing
one of the three replaceable vertices only turns the four windows into the
loopless complete-graph walk.  The two-eigenvalue law is generic and every
target fibre is a walk count.

**Decision:** `KILL_INTERNAL_P161`.

## KMP — random-letter prefix automaton

Query target: first hit of a fixed word under iid letters, full prefix-state
law, border/correlation mean, and inverse autocorrelation data.

Decisive primary hit:

- Guibas and Odlyzko, [*String Overlaps, Pattern Matching, and Nontransitive
  Games*](https://doi.org/10.1016/0097-3165(81)90005-4) (1981), introduces
  string correlation and derives generating functions for words avoiding
  prescribed patterns.

The KMP transition matrix is an implementation of that owned correlation
automaton.  P92 and P134 also occupy recurrence avoidance and recomputed border
arrays internally.

**Decision:** `KILL_DIRECT_PATTERN_OWNER`.

## GSW, TTW, and PTW — binary boundary walks

`GSW` was compared directly with P145.  Klostermeyer,
[*Pushing Vertices and Orienting
Edges*](https://combinatorialpress.com/ars/vol51/) (1999), owns vertex pushes;
Chen, Li, and Lin, [*Random Walks on the Folded
Hypercube*](https://doi.org/10.3966/160792642019102006027) (2019), is the
primary random-walk neighbour used in P145's owner subtraction.  Encoding an
orientation or a graph as edge bits makes `GSW` the same cut-space action.

For `TTW`, the static fact that triangle boundaries generate the cycle space
of `K_n` is already generic.  The nearest primary research returned by the
bounded query was DeMarco, Hamm, and Kahn,
[*On the Triangle Space of a Random Graph*](https://arxiv.org/abs/1207.6717)
(2012), which studies triangle generation of graph cycle spaces; it does not
by itself claim this exact complete-graph walk.  The proposed transition law,
however, is immediate Fourier inversion on the generated binary group, and
P67/P127 occupy the matroid/parity carriers.  A bounded literal-walk non-hit is
not novelty.

For `PTW`, no direct primary paper for this exact discrete-time uniform-face
toggle was returned.  The verifier proves that the `rc` face choices have the
single all-face relation and are exactly conjugate to the parity-set walk
modulo complement.  P67 already occupies plaquette dependence.  Again, the
non-hit is not novelty.

**Decisions:** `GSW = KILL_EXACT_INTERNAL_CONJUGACY`,
`TTW = KILL_GENERIC_GROUP_WALK`, `PTW = KILL_EXACT_GROUP_CONJUGACY`.

## CDP, UDC, and BSR — exact internal transfers

These three were killed by algebra before an external owner search could add
value.

- `CDP`: `I+S^-1=S^-1(I+S)`, so scheduler randomness only chooses a cyclic
  phase.  Nilpotence, image, and fibres are the occupied linear-module engine
  of P63/P86/P98/P115.
- `UDC`: uniform choice of a divisor makes prime exponents independent uniform
  lower coordinates.  This is a product of the earlier RCR uniform-descending
  chain and lies next to P142's divisor-valuation atlas.  Searches for
  `uniform random divisor Markov chain absorption` returned no direct literal
  primary paper; that non-hit is irrelevant and is not novelty because the
  internal transfer is exact.
- `BSR`: iterating `x -> 2x+B` is the finite binary shift register.  Its sharp
  source erasure and target histories are already within P93/P101's random
  register/synchronization firewall.

**Decisions:** three permanent internal kills.

## SBW — fair rational-tree growth

Decisive primary hit:

- Calkin and Wilf, [*Recounting the
  Rationals*](https://doi.org/10.1080/00029890.2000.12005205) (2000), owns the
  two-child rational tree and unique enumeration.

The fair scheduler makes the owned level uniform.  Subtractive inversion and
Fibonacci extremizers do not leave a stochastic residual; P131 independently
occupies Euclidean quotient/decoder dynamics.

**Decision:** `KILL_DIRECT_TREE_OWNER`.

## ECR, PLU, and BGW — classical stochastic laws

Decisive primary sources:

- Ewens, [*The Sampling Theory of Selectively Neutral
  Alleles*](https://doi.org/10.1016/0040-5809(72)90035-4) (1972), owns the
  Ewens sampling formula used by `ECR`.
- Blackwell and MacQueen, [*Ferguson Distributions via Pólya Urn
  Schemes*](https://doi.org/10.1214/aos/1176342372) (1973), is a primary
  Pólya-sequence/urn record.  The two-colour beta-binomial and exchangeability
  used by `PLU` are classical specializations.
- Watson and Galton, [*On the Probability of the Extinction of
  Families*](https://www.jstor.org/stable/2841222) (1875), is the original
  branching-process paper.  `BGW` is the literal 0-or-2 Galton–Watson process;
  iterated offspring PGFs and full-binary-tree total progeny are its standard
  core.

P135/P155 additionally occupy cycle-shape extraction internally.  None of
these three can be repackaged as a new finite dynamic.

**Decisions:** `KILL_DIRECT_EWENS`, `KILL_DIRECT_URN_OWNER`, and
`KILL_DIRECT_BRANCHING_OWNER`.

## Final owner disposition

| class | candidates | count |
|---|---|---:|
| direct external object/theorem owner | `DCI, LSC, QHI, KMP, SBW, ECR, PLU, BGW` | 8 |
| exact internal transfer/conjugacy or generic occupied engine | `HCI, ORW, GSW, TTW, PTW, CDP, UDC, BSR` | 8 |
| paper-sized owner-thin retained | none | 0 |

The lane returns an empty pool.  `HOLD_EXTERNAL` remains in force.  Neither the
verifier nor any bounded non-hit authorizes a novelty statement, public post,
priority claim, attribution claim, or submission.

