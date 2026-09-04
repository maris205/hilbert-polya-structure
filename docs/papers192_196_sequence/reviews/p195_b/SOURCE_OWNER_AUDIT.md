# P195 Review-B source and owner audit

**Date:** 2026-09-04 UTC  
**Decision:** `OWNER_AMBER / HOLD_EXTERNAL`  
**Novelty claim:** none.

## External boundary

Review B reran bounded queries for odd edge-side marker walks, least-labelled
neighbour dynamics, mutual-minimum forest maps, and rooted-tree parity EGFs.
The returned deterministic-tree-walk literature included Angel and Holroyd's
[*Rotor walks on general trees*](https://arxiv.org/abs/1009.4802), whose state
includes rotors and whose update routes a walker by changing cyclic local
directions.  It is not the fixed-tree, side-parity, least-label map of P195.

The cited Bostan--Jiménez-Pastor article is correctly identified by DOI
[`10.5802/crmath.108`](https://doi.org/10.5802/crmath.108) and is used only for
the classical rooted labelled-tree EGF.  Moon, Bergeron--Labelle--Leroux, and
Flajolet--Sedgewick are likewise background sources for Cayley/species
machinery, not asserted owners of the dynamics.

The bounded search did not identify a literal joint map/theorem package, but a
non-hit proves neither novelty nor priority and cannot clear ownership or
freedom to operate.

## Internal collision boundary

Repository-wide inspection rechecked the named tree systems.  P123 changes
all edges inside selected odd connected components and already owns the broad
parity/fixed-two-cycle/tail/zeta silhouette.  P159 deletes all odd-degree
vertices in parallel and derives a binary-rank inverse.  P114, P120, P144,
and P148 also change the carrier or its structure.  P195 instead leaves one
labelled tree fixed and moves one marker according to oriented edge-side
parity and least labels.

The manuscript now explicitly gives the shared `floor((n-1)/2)` scale,
parity recurrence, labelled EGF/species calculus, zeta conversion, and generic
local-fibre language zero contribution and separation credit.  The retained
residual is narrow and direct ownership remains unresolved.
