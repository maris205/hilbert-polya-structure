# Paper plan

## Title and one-sentence contribution

**Arithmetic Prefixes and Cycle-Matroid Dependence in a Multiplicative
Plaquette Shift**

For the finite-field constraint
`x_n-x_{an}-x_{bn}+x_{abn}=0`, the paper gives global free coordinates and an
exact formula for every finite projection: the coordinate-dependence matroid
is a direct sum of graphic matroids of root-wise bipartite incidence graphs.

## Claims--evidence spine

| Claim | Evidence | Section |
|---|---|---|
| the full constraint space is explicitly parameterized by the coordinates not divisible by `ab` | multiplicative root decomposition and mixed-difference integration | Section 2 |
| every finite projection has an exact graph-rank count | vertex-potential map, kernel count, and spanning-forest reconstruction | Section 3 |
| cycle relations are the complete finite obstruction | oriented incidence matrix and fundamental cycles | Section 3 |
| deleting or adding one coordinate obeys the exact rank/nullity dichotomy | graphic-matroid bridge/cycle law | Section 5 |
| Haar dependence is exactly cycle rank | uniform pushforward of Haar measure and finite-field entropy | Section 3 |
| prefixes have exponent `N-floor(N/(ab))` | free-axis count and triangular pivot cross-check | Section 4 |
| exponent rectangles have boundary-order complexity | complete-bipartite incidence graph | Section 5 |
| the paper does not conflate three geometries or claim priority | explicit comparison and scope ledger | Section 6 |

## Section structure

1. **Introduction.** State the all-finite-shape theorem first, preview the
   prefix and rectangle corollaries, and subtract the closest literature
   owners without a priority claim.
2. **Multiplicative components and global coordinates.** Prove unique root
   decomposition, solve the plaquette equation on `N_0^2`, and establish the
   restriction homeomorphism onto the free set `B`.
3. **Finite projections and graphic matroids.** Attach a bipartite graph to
   an arbitrary finite set, prove the exact rank and cycle-equation theorem,
   and derive Haar entropy, forest independence, and cycle total correlation.
4. **Arithmetic prefixes.** Prove the exact prefix pattern count, give the
   independent triangular-pivot reading, and define arithmetic-prefix
   complexity without calling it topological entropy.
5. **Exponent rectangles and boundary laws.** Specialize to complete
   bipartite graphs, calculate pattern counts and Haar dependence, and record
   products over distinct roots.
6. **Comparison, scope, and further shapes.** Separate owned frameworks,
   proved statements, and excluded entropy/priority claims; identify the
   finite-shape theorem as the residual internal contribution.
7. **Conclusion.** Summarize how arithmetic and exponent geometries are
   unified by the graph rank while retaining different normalizations.

## Figure and table plan

No graphical figure is needed.  The proof is carried by an explicit incidence
graph construction and exact equations.  Two information-bearing tables are
used:

1. a geometry table comparing arbitrary finite sets, arithmetic prefixes,
   and exponent rectangles;
2. a claim-boundary table separating proved counts from uncomputed dynamical
   entropies and prohibited priority claims.

## Citation plan

- Introduction and Section 6: Kenyon--Peres--Solomyak for the foundational
  multiplicative-integer symbolic setting, and
  Peres--Schmeling--Seuret--Solomyak (2014) for direct two-generator dimension
  context.
- Introduction and Section 6: Ban--Hu--Lin (2019) for multiplicative pattern
  generation and spatial entropy, Ban--Hu--Lai (2021) for multidimensional
  multiplicative-subshift entropy, and Ban--Hu--Lai--Liao (2025) for axial
  products and surface entropy.
- Introduction and Section 6: Mora Cuellar--Rojas Aravena--Yavicoli (2026)
  for prime-valuation coordinates, densities, correlations, and symbolic
  realizations.
- Introduction, Section 3, and Section 6: Whitney (1935) and Watanabe (1960)
  for standard matroid and total-correlation terminology.

## Review state

Two earlier independent cross-agent review rounds and two subsequent official
`gpt-5.4 xhigh` rounds are complete and recorded in `reviews/`.  The official
Round-2 proof audit returned mathematics **PASS**; its single release-package
integrity issue was resolved by synchronizing the canonical PDF, QA receipts,
state, and hashes.  No numerical reviewer score is claimed.  Stage 2.5 and
specialist exact-neighbor review have not passed and remain release gates.
External-release status remains `HOLD`.
