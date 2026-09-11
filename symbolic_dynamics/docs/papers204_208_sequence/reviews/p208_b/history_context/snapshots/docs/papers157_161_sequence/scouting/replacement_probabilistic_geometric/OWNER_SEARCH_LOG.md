# Bounded owner and collision audit

**Date:** 2026-09-02 UTC  
**Scope:** replacement probabilistic/geometric breadth lane  
**External state:** `HOLD_EXTERNAL`

Search snippets were used only to locate primary or authoritative records.
Positive hits support kills.  A bounded non-hit is **not** evidence of novelty,
priority, ownership, freedom to operate, or source exhaustion.

## Query families

```text
random contiguous block deletion survivor absorption PGF
triangulation flip increase marked vertex degree fan
Lawson random illegal edge flip Delaunay legalization
domino tiling plaquette flip Markov chain
Wang Swendsen Kotecky Kempe component colouring chain
graph local complementation orbit Bouchet
binary contingency table 2x2 switch Markov basis
random improving graphic matroid basis exchange
Coxeter simple descent random walk reduced expressions type B
Markoff triple Vieta descent tree
Descartes quadruple reflection Apollonian group
free word random adjacent inverse cancellation
monochromatic edge random endpoint recolouring
zero temperature one dimensional Glauber isolated spin
monotone triangle single site heat bath Markov chain
finite path k-medians Lloyd median update basins
```

## Positive owner chain

- `RTF`: the standard proof of flip-graph connectivity already transforms any
  polygon triangulation to a fan by flips that increase the marked vertex's
  degree; see Pilaud's authoritative survey/thesis,
  [*Multitriangulations, pseudotriangulations and some problems of realization
  of polytopes*](https://www.ub.edu/comb/vincentpilaud/documents/reports/theseVincentPilaud.pdf).
  P146 additionally occupies triangulation deletion and tree-hook histories.
- `LDL`: Lawson,
  [*Transforming triangulations*](https://doi.org/10.1016/0012-365X(72)90093-3),
  is the primary flip-based legalization owner.
- `DPF`: Luby--Randall--Sinclair,
  [*Markov Chain Algorithms for Planar Lattice Structures*](https://doi.org/10.1137/S0097539799360355),
  explicitly chooses a `2 x 2` window in a domino tiling and rotates two
  parallel dominoes.
- `KCI`: the WSK chain uses Kempe-component colour swaps; Feghali--Johnson--Paulusma,
  [*Kempe equivalence of colourings of cubic graphs*](https://doi.org/10.1016/j.ejc.2016.06.008),
  states the operation and its Markov-chain role.  At three colours the
  verifier's pair/vertex scheduler has the same one-step probabilities.
- `LCW`: Bouchet,
  [*Transforming trees by successive local complementations*](https://doi.org/10.1002/jgt.3190120210),
  defines exactly the neighbourhood-complement operation and local-equivalence
  classes.  Internally, P117 C01 and P145 make the collision decisive.
- `TSW`: Diaconis--Sturmfels,
  [*Algebraic Algorithms for Sampling from Conditional Distributions*](https://doi.org/10.1214/aos/1030563990),
  owns Markov-basis sampling of fixed sufficient-statistic fibres, including
  contingency tables.  The alternating `2 x 2` move is the standard switch.
- `MBE`: Edmonds,
  [*Matroids and the greedy algorithm*](https://doi.org/10.1007/BF01584082),
  supplies the classical greedy/matroid basis engine.  The repository's
  permanent generic matroid-basis exclusion kills the random scheduler without
  needing a same-scheduler owner.
- `BCD`: Reiner,
  [*The distribution of descents and length in a Coxeter group*](https://doi.org/10.37236/1219),
  owns Coxeter length and simple descents.  Reduced histories are reduced
  decompositions, so the stochastic choice adds no independent axis.
- `VMD`: Aigner's authoritative monograph,
  [*Markov's Theorem and 100 Years of the Uniqueness Conjecture*](https://doi.org/10.1007/978-3-319-00888-2),
  develops the Markoff tree; Vieta involutions are also the explicit dynamics
  in the contemporary Markoff-action literature.
- `ACD`: Graham--Lagarias--Mallows--Wilks--Yan,
  [*Apollonian Circle Packings: Geometry and Group Theory I*](https://arxiv.org/abs/math/0010298),
  defines the integer reflection generators and identifies Descartes
  configurations as Apollonian-group orbits.
- `ZIG`: Glauber,
  [*Time-Dependent Statistics of the Ising Model*](https://doi.org/10.1063/1.1703954),
  is the primary nearest-neighbour spin-dynamics owner.  More decisively, the
  literal isolated-spin cycle update already occurs as `R06` in the P132--P136
  stochastic scout.
- `BKM`: Lloyd,
  [*Least squares quantization in PCM*](https://doi.org/10.1109/TIT.1982.1056489),
  is the primary alternating assignment/update owner; replacing means by
  medians is the standard `k`-medians variant, not a new dynamical programme.

`PBL`, `PCR`, and the exact `MTG` scheduler produced no same-formula/same-kernel
hit in the bounded queries.  This does not rescue them: `PBL` violates the
explicit deletion exclusion; `PCR` has neither a closed all-parameter clock nor
a second axis; and `MTG` reduces to a generic single-site heat bath plus the
classical monotone-triangle/ASM census.  `FCR` is killed internally by the prior
free-reduction pilots (`R05/W01`) and by generic deletion, independently of an
external exact-scheduler hit.

## Final gate

| outcome | count |
|---|---:|
| direct classical system or direct owner programme | 8 |
| exact/internal or permanent-exclusion collision | 5 |
| theorem-thin after bounded non-hit | 3 |
| eligible focused finalists | **0** |

Decision: `EMPTY_POOL / HOLD_EXTERNAL`.  No numbering, manuscript drafting,
Git synchronization, upload, or external release is authorized.

