# Bounded owner and collision search — stochastic/nonlinear replacement lane

**Date:** 2026-09-03 UTC  
**Systems covered:** `W01`--`W05`, `U01`--`U05`, `A01`--`A05`,
`G01`--`G05`, `F01`--`F04`  
**External state:** `HOLD_EXTERNAL`

## Search protocol

The search was run before ranking and was deliberately bounded.  Exact-map
queries were combined with mechanism queries because an exact string miss is
weak evidence.  Search results were opened or checked against author/arXiv,
journal, DOI, or institutional primary records; snippets and secondary pages
were used only to locate those records.  A miss below means only that this
bounded pass found no literal owner.  It does **not** mean novelty, priority,
ownership, or publication clearance.

Representative query families were:

```text
"equal endpoints" interval flip binary word Markov
random interval rotation word endpoint colours Markov chain
run parity local update cyclic binary word
state dependent rotation word multiplicity random walk cyclic
nonlinear urn state dependent drawing rule pair reaction
square feedback urn finite population absorption
random iteration polynomial maps finite fields functional graph
random polynomial shear finite affine plane
random Frobenius maps truncated polynomial ring
random matrix polynomial A plus or minus A squared finite field
graph bootstrap percolation add missing edge triangle
random graph transformation common neighbors edge toggle
random poset comparison transitive closure Markov chain
random midpoint triangle finite field
random walks finite affine geometry reflection triangle
```

## Primary records and exact subtraction

| primary record | scope actually supported | subtraction in this lane |
|---|---|---|
| John Rhodes and Anne Schilling, [*Unified theory for finite Markov chains*](https://arxiv.org/abs/1711.10689) (2017) | finite Markov chains presented as random walks on finite semigroups, with semigroup normal forms and stationary laws | Generic finite-semigroup compression is zero credit.  It is fatal to `W04/W05/G03/F03` unless the literal map supplies a separate inverse and recovery axis; none does. |
| Sergei Konyagin, Florian Luca, Bernard Mans, Luke Mathieson, Min Sha, and Igor Shparlinski, [*Functional Graphs of Polynomials over Finite Fields*](https://arxiv.org/abs/1307.2718) (2013) | structural and computational study of finite-field polynomial functional graphs | Small-prime polynomial graph signatures are zero credit for `A01`--`A03`. |
| José Alves Oliveira and Fabio Enrique Brochero Martínez, [*Dynamics of polynomial maps over finite fields*](https://arxiv.org/abs/2201.00954) (2022) | complete functional graphs for broad structured finite-field polynomial maps, including monomial reductions | Scalar power and regular polynomial reductions are zero credit for `A02/A05/F04`. |
| Wade Hindes, [*Dynamical and arithmetic degrees for random iterations of maps on projective space*](https://arxiv.org/abs/1904.04709) (2019) | random iteration of finite families of rational self-maps | Randomizing polynomial generators is not by itself a new theorem axis for `A01`--`A05`. |
| Henrik Renlund, [*Generalized Pólya urns via stochastic approximation*](https://arxiv.org/abs/1002.3716) (2010) | generalized one- and two-draw urns, including two-colour examples | Generic two-draw/replacement-urn framing is zero credit for `U02/U04`. |
| Sophie Laruelle and Gilles Pagès, [*Nonlinear Randomized Urn Models: a Stochastic Approximation Viewpoint*](https://arxiv.org/abs/1311.7367) (2013) | urn drawing rules reinforced by nonlinear functions | State-dependent nonlinear sampling weights are zero credit for `U01/U03/U05`. |
| Thomas Gottfried and Stefan Grosskinsky, [*Asymptotics of generalized Pólya urns with non-linear feedback*](https://arxiv.org/abs/2303.01210) (2023) | broad nonlinear-feedback urn asymptotics | A nonlinear feedback function alone cannot be claimed as the contribution of `U01/U03/U05`. |
| József Balogh, Béla Bollobás, and Robert Morris, [*Graph bootstrap percolation*](https://arxiv.org/abs/1107.1381) (2011) | the `H`-bootstrap rule that adds a missing edge completing a copy of `H` | For `H=K_3`, the active update of `G01` is precisely triangle completion.  Only a new random-history atlas could remain, and exact tests found no compressed statistic for it. |
| James Parkinson, [*Isotropic random walks on affine buildings*](https://arxiv.org/abs/math/0606662) (2006) | harmonic-analysis treatment of random walks in finite/affine geometric settings | Generic harmonic analysis or isotropic geometry-walk language is zero credit for `F02/F03`. |
| Nicolaos E. Manitara, Apostolos I. Rikos, and Christoforos N. Hadjicostis, [*Privacy-Preserving Distributed Average Consensus in Finite Time using Random Gossip*](https://arxiv.org/abs/2111.04642) (2021) | randomly scheduled pairwise averaging/gossip maps and finite-time consensus questions | Randomly scheduled midpoint/averaging language is zero credit for `F01`; in any case its characteristic-three map is just a linear retraction. |

## Literal-query outcome

| systems | bounded exact-query result | decision independent of the miss |
|---|---|---|
| `W01/EEI`, `W02/UIR`, `W03/RPE` | no literal finite-word kernel located | all lack a nontrivial sufficient statistic and reduce to full finite-state DP |
| `W04/PCR`, `W05/MCR` | no literal wording hit; direct cyclic/group-walk and data-dependent-rotation neighbours found | both are killed by action-only structure and current `AQN/HWR/DCR` collision |
| `U01`--`U05` | no exact finite capped rule located; broad nonlinear and two-draw urn owners found | only deterministic population clocks survive; every endpoint axis remains a path recursion |
| `A01/CCM`, `A03/RPS` | no literal coefficient-mutation or paired-shear owner located | histories have no normal form; small-field transition matrices are not theorem evidence |
| `A02/RQS`, `A05/RMP` | broad finite-field polynomial dynamics and random iteration records found, no exact pair hit retained | generic polynomial functional-graph/semigroup ownership is already fatal |
| `A04/RFS` | no exact truncated-ring random family hit | Frobenius makes the maps finite-linear, so it fails the mechanism gate internally |
| `G01/IWC` | direct `K_3` graph-bootstrap owner | direct mechanism owner plus no stochastic history compression |
| `G02/XEC`, `G05/OCN` | no literal rule located; local-complement/pivot neighbourhood appeared for toggle language | `G02` is finite-linear/rank-shadowed; `G05` is an irregular involution walk |
| `G03/IER` | generic conditional relabelling only | current graph-relabel walk collision is decisive |
| `G04/NPC` | generic poset-closure/frontier literature; no literal scheduler hit retained | current `OPG` and the permanent generic-closure exclusion are decisive |
| `F01/RMT`, `F02/AGS`, `F04/DRF` | no literal finite-field triangle rule located | respectively linear projection, affine action, and determinant-power reductions |
| `F03/RSR` | ordinary affine reflection/random-walk neighbourhood | generic group walk with no inverse or recovery axis |

## Internal collision firewall

The P1--P161 directory names, the P152--P161 occupancy and kill ledgers, and
the active P162--P166 scout ledgers were searched before freezing the slate.
The decisive internal comparisons are:

- `W04/W05` are random schedulers over the data-dependent rotation actions
  already isolated in the adaptive-map lane (`AQN`, `HWR`, `DCR`, `EGR`).
- `A04` is a hidden finite-linear family; `A05/F04` reduce to polynomial or
  determinant-power dynamics adjacent to P103 and the permanent generic-power
  exclusion.
- A proposed random `A E_i A` coordinate-sandwich system was removed before
  numbering because `NL18/MSQ` already killed the same rank-one followed by
  scalar-power proof engine.  Thus the frozen `A01` is instead the genuinely
  different cubic coefficient-mutation kernel.
- `G01/G04` are closure schedulers.  `G04` is especially close to the current
  stochastic closure candidate `OPG`; neither random scheduling nor terminal
  DP creates a new axis.
- `G02` changes binary adjacency data through linear incidence operations and
  is too close to the excluded random-rank/span-erosion silhouette even though
  its literal carrier is a graph.
- `G03` is another graph relabelling walk, already occupied by `EGR` at the
  action-only level.
- `F01/F02/F03` collapse respectively to a linear retraction, an affine action,
  and affine reflections.  The geometry/group scout permanently excludes a
  generic group walk presented as new finite geometry.
- No candidate uses random cuts, deletion, pruning, sorting, exclusion flow,
  coalescence, coupon collection, or the RTI translation-intersection update.

## Owner-gate conclusion

```text
DIRECT_OWNER_HITS: G01 mechanism; broad owners for urn/polynomial/action families
LITERAL_MISSES: non-evidence only
SURVIVORS: 0
DECISION: EMPTY_POOL
EXTERNAL_STATE: HOLD_EXTERNAL
```

No novelty claim is made.  The right next action is a new mechanism lane, not
an expanded search around any kernel recorded here.
