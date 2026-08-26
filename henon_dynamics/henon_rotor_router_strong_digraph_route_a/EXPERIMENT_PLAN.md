# Experiment plan

## Claim-driven validation

1. **Complete simple-graph census.** Enumerate every labeled simple loopless directed graph on \(n=2,3,4\) vertices and retain exactly the strongly connected graphs.
2. **Exact invariants.** For each retained graph, compute every \(t_v\) as an exact row-Laplacian cofactor, then compute \(M,L\), the total unicycle-state count, and Eulerian status.
3. **State-level dynamics.** Materialize every rotor configuration, detect unicycles directly, apply the advance-then-move rule, decompose the recurrent permutation into cycles, and check common length, orbit count, vertex visits, and every distinguished-arc traversal count.
4. **Cyclic-order controls.** Audit every cyclic order for \(n\le3\); audit every cyclic order for the first 128 strong \(n=4\) graphs and one canonical order for all remaining \(n=4\) graphs.
5. **Multigraph/loop controls.** Add four explicit strongly connected directed multigraph sentinels, including a one-vertex loop system, parallel arcs, loops, non-Eulerian imbalance, and an Eulerian double-edge graph; audit every cyclic order.
6. **Independent and symbolic checks.** Use a checker with a Leibniz determinant and independently reconstructed state dynamics; use SymPy for all matrix-tree cofactors and kernel equations and for selected full finite-permutation determinants.
7. **Integrity layer.** Require byte-identical replay, 25 repaired-hash semantic mutation rejections, one stale-hash rejection, three content-distinct PDFs, deterministic final recompilation, embedded fonts, layout checks, and a 27-payload-file manifest.

## Interpretation

The global theorem chain is mathematical: exact common length/count are source-locked to Pham's Theorem 1, and the local-frequency and finite-cycle consequences are derived explicitly. Exhaustive \(n\le4\) enumeration and multigraph sentinels are implementation regressions. They do not restrict the theorem domain and do not authorize any arithmetic interpretation.
