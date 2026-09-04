# P195 Review-A source and owner-collision audit

**Audit date:** 2026-09-04 UTC  
**Decision:** `PASS`; historical internal source-boundary revision installed
and accepted; no external literal-map owner established.  
**Gate:** `OWNER_AMBER / HOLD_EXTERNAL`.

## Bibliography verification

| Record | Checked metadata | Result |
|---|---|---|
| Moon, *Counting Labelled Trees* | Canadian Mathematical Monographs 1, Canadian Mathematical Congress, 1970 | PASS |
| Bergeron--Labelle--Leroux, *Combinatorial Species and Tree-Like Structures* | Cambridge University Press, standard 1998 citation, DOI [10.1017/CBO9781107325913](https://doi.org/10.1017/CBO9781107325913) | PASS |
| Bostan--Jiménez-Pastor, *On the exponential generating function of labelled trees* | *Comptes Rendus Mathématique* 358(9--10), 1005--1009 (2020), DOI [10.5802/crmath.108](https://doi.org/10.5802/crmath.108) | PASS |
| Flajolet--Sedgewick, *Analytic Combinatorics* | Cambridge University Press, print year 2009, DOI [10.1017/CBO9780511801655](https://doi.org/10.1017/CBO9780511801655) | PASS |

These sources correctly support Cayley/Prüfer and labelled-species
background.  None is used as evidence that the P195 map is new.

## External owner pressure

Queries combined exact and translated variants of `least-labelled neighbour
odd side tree walk`, `tree edge odd component deterministic dynamics`,
`mutual least neighbours forest map`, and `labelled tree odd branches
recurrent EGF`.  Results covered deterministic rotor walks, parity/odd-degree
trees, and rooted-tree EGF background.  No result in this bounded query stated
the literal fixed-tree root update together with P195's parity classification,
integrated least-label EGF, and local inverse atlas.

That non-hit does **not** establish novelty, priority, completeness,
independence from an unqueried conjugate, or freedom to operate.  The gate
remains `OWNER_AMBER / HOLD_EXTERNAL`.

## Internal P1--P191 subtraction

The live definitions and sequence collision inventories were checked.  P114
deletes leaves from rooted forests; P120 mirrors odd-order fringes of plane
trees; P144 reassociates Dyck factors; P148 deletes even-level vertices; none
is P195's fixed-carrier marker walk.

Two additional close surfaces were missing from Round 0:

- **P123 odd-component complementation** already has parity-triggered
  fixed/two-cycle recurrence, sharp `floor((n-1)/2)` tail, labelled generating
  functions, and zeta.  Its literal update complements every odd connected
  graph component and its clock is a split-tree depth; P195 instead preserves
  a tree and moves one root marker along odd cut sides.
- **P159 parallel odd-vertex pruning** deletes all current odd-degree vertices
  from a labelled graph and builds a rank-transfer atlas.  P195 deletes
  nothing and uses the least label only after edge-side eligibility.

The shared parity, tail scale, fixed/two-cycle vocabulary, EGF/species algebra,
zeta conversion, and generic fibre bookkeeping must be declared zero-credit.
This was finding P195-A1; the repaired manuscript and source ledger now make
the subtraction explicit.  It was a source firewall omission, not a
demonstrated mathematical collision.

P195's retained internal residual is limited to the literal odd-side
least-neighbour marker update, its edge-orientation/off-path clock proofs, the
integrated mutual-edge count, and the incident-edge inverse test.

P195-A1 and the dual-status finding P195-A2 are closed.  Open source/status
findings: `0`.  The gate remains `OWNER_AMBER / HOLD_EXTERNAL`.
