# HCS-C33 Phase-2 search strategy

**Audit date:** 2026-08-12 UTC
**Stage:** Phase 2, investigation only
**Candidate:** `HCS-C33_HENON_ACTION_COLLISION_KUMMER`

## 1. Review question

For the area-preserving Hénon family

\[
H_A(q,p)=(1-Aq^2-p,q)
\]

and its exact period-five cyclic action, has prior work already constructed
the following coupled object?

\[
\boxed{
\text{degree-nine equal-action parameter divisor}
+\text{two distinct nonparabolic exact-period-five points}
+\text{whose action-image branches form a transverse ordinary node}
+\text{Hill-determinant Kummer square class}.}
\]

The direct-collision criterion is deliberately conjunctive.  A source is not
a direct duplicate merely because it contains one of:

- a Hénon periodic-orbit polynomial;
- a discrete generating action;
- two critical points with the same critical value;
- Hill's determinant identity;
- a quadratic Kummer cover;
- a Lyashko--Looijenga or braid-monodromy construction.

Those mechanisms are classical.  A direct duplicate must identify the same
period-five Hénon action-image singularity, or an equivalent construction,
and couple its two branches to the intrinsic chronological Hill determinant.

## 2. Phase firewall

This directory contains only the search protocol, the source corpus, and the
source/novelty verification report.  It contains no Phase-3 producer,
independent checker, computed certificate, manuscript, formal Route-A
evaluation, or Route-B invocation.

## 3. Search services and source policy

The audit used:

- Crossref Works API for DOI, author, venue, and publication metadata;
- OpenAlex works-by-DOI for independent metadata, retraction flags, and
  citation-context checks;
- arXiv for exact-title and recent-preprint searches;
- official publisher pages, journal pages, author-hosted PDFs, and the Kyoto
  University repository for primary full text;
- a ranked web-search interface for cross-domain collision searches;
- the complete local `henon_dynamics` corpus via `rg` for repository
  nonduplication.

Only primary papers, primary proceedings chapters, or foundational
monographs support technical statements.  Search snippets and secondary
indexes were used only to discover or disambiguate primary sources.

No foundational date cutoff was imposed.  The recent-search horizon covered
works visible through 2026-08-12, with an explicit 2024--2026 pass.

## 4. Search lanes

### Lane H: exact Hénon orbit algebra

Targets:

- period-five and low-period marker polynomials;
- orbital sums, reversibility classes, discriminants, and Galois groups;
- parameter-dependent stability polynomials;
- exact equivalences between orbital equations.

### Lane A: Hénon and symplectic action geometry

Targets:

- discrete Lagrangian/generating-function formulations;
- periodic action values and action differences;
- equal-action Hénon saddles or trajectories;
- quantum-Hénon Stokes geometry and virtual turning points.

### Lane M: Maxwell and critical-value monodromy

Targets:

- Maxwell strata versus caustics;
- Lyashko--Looijenga critical-value maps;
- generic nodes formed by distinct Morse critical points with equal value;
- Galois and braid monodromy of critical-value covers.

### Lane K: Hill and Kummer decoration

Targets:

- discrete Hill formula and action Hessians;
- stability determinants on equal-critical-value branches;
- quadratic/Kummer covers attached to Hessian or monodromy square classes;
- Kummer covers combined with braid monodromy.

### Lane R: recent horizon

Targets:

- Hénon arithmetic dynamics from 2024--2026;
- recent critical-point/embedded monodromy;
- recent plane-curve/Kummer/braid surveys;
- any new work naming Hénon action collisions or Maxwell divisors.

## 5. Exact query ledger

The following exact strings were run.  Dynamic hit totals were not treated
as stable data; the named-work corpus below is the auditable unit.

### Hénon orbit algebra and action

1. `"Hénon map" periodic orbit action generating function Maxwell`
2. `"area-preserving Hénon map" action periodic orbit generating function`
3. `Hénon map periodic orbit "action difference" bifurcation`
4. `"Hénon map" "action functional" periodic orbit`
5. `"Hénon map" "classical action" periodic orbits`
6. `"Hénon Hamiltonian repeller" action periodic`
7. `Endler Gallas Hénon period 5 polynomial exact orbits`
8. `"Hénon map" "virtual turning points" action`
9. `"Stokes geometry for the quantum Hénon map" equal action`
10. `"A role of virtual turning points" Hénon action`

### Maxwell and critical-value geometry

11. `periodic orbit action degeneracy Maxwell set symplectic map generating function`
12. `critical values generating family Maxwell set symplectic maps periodic points`
13. `"equal action" periodic orbits symplectic map`
14. `"Maxwell set" periodic orbit action Hamiltonian`
15. `"Maxwell set" "generating family" singularity theory`
16. `"Maxwell strata" generating functions Lagrangian singularities`
17. `Lyashko Looijenga map Maxwell strata critical values monodromy DOI`
18. `discriminant critical values finite map node Kummer cover Hessian determinant`

### Hill and Kummer coupling

19. `"Hessian determinant" "Kummer cover" singularity`
20. `periodic orbit equal action Hessian determinant monodromy`
21. `periodic orbit action collision stability determinant`
22. `"action degeneracy" periodic orbits Hessian`
23. `"Hill determinant" generating function periodic orbit`
24. `"Hill determinant" "equal action" periodic orbit`
25. `"Hénon" "Kummer cover" periodic`
26. `Kummer cover square class discriminant critical values monodromy`

### Exact-coefficient collision probes

27. `"110592A^9" Hénon`
28. `"294912A^8" "Hénon"`
29. `"110592" "294912" Hénon`
30. `"50672A^3" Hénon action`

### Recent 2024--2026 horizon

31. `Hénon map periodic orbits arithmetic algebraic 2024 2025 2026`
32. `Hénon symplectic map generating function action 2024 2025`
33. `Hénon map critical values action Maxwell 2024 2025`
34. `periodic orbit action collision Hessian square class arithmetic dynamics 2024 2025`
35. `site:arxiv.org Hénon periodic orbit action Maxwell set`
36. `site:arxiv.org Hénon map periodic orbit action functional Hill determinant`

## 6. Inclusion and exclusion rules

### Included

A work was retained when it directly established or constrained at least one
of the following:

- exact low-period Hénon orbit algebra;
- the Hénon discrete action or equal-action saddle geometry;
- the Maxwell/caustic distinction or critical-value monodromy;
- the discrete Hill action-Hessian/monodromy identity;
- Kummer covers together with braid or plane-curve monodromy;
- a recent Hénon arithmetic or monodromy result needed to assess currency.

### Excluded from technical support

A work was excluded when it concerned only:

- the Hénon--Heiles flow rather than the Hénon map;
- dissipative Hénon attractor numerics without exact action geometry;
- generic periodic-orbit computation with no action or critical-value map;
- arithmetic Hénon heights or rational points with no generating action;
- equicritical strata recording critical-point multiplicities but not
  equal critical values;
- Kummer surfaces or unrelated uses of the name Kummer;
- Maxwell sets in optimal control without a bridge to the Hénon family.

## 7. Named-work flow

The manually frozen decision ledger contains 26 numbered entries: 25 named
works and one recurring Hénon--Heiles exclusion family.  Supplementary
follow-ups and boundary references cited inside annotations are not counted
as separate ledger decisions.

- 26 numbered entries assessed at full-text or official-metadata level;
- 21 of those retained as core, boundary, or current-context sources;
- 5 of those retained as assessed exclusions/near misses;
- 0 direct duplicates of the coupled C33 object found.

The five assessed exclusions are:

1. Kim--Krieger--Postolache--Szeto, *Hénon maps with many rational periodic
   points* (arXiv:2412.01668): arithmetic periodic points, no action image;
2. Zhang, *Arithmetic properties of families of plane polynomial
   automorphisms* (arXiv:2407.15952): height/periodic-parameter geometry, no
   action-value collision;
3. Huxford--Salter, *Noninjectivity of the monodromy of certain equicritical
   strata* (2025): critical-point multiplicity/embedded monodromy, not the
   equal-critical-value Maxwell locus;
4. Artal Bartolo, *Topology of complex plane curves: braid monodromy, local
   and global problems* (arXiv:2604.26596): current plane-curve survey, no
   Hénon/Hill specialization;
5. the recurring Hénon--Heiles periodic-orbit literature: a continuous
   Hamiltonian with a similar name, not the Hénon map used here.

This was a targeted novelty audit, not a licensed MathSciNet/zbMATH
systematic review.  Search-engine hit counts are unstable and were therefore
not promoted into a PRISMA claim.

Additional recent-horizon searches screened Shudo--Ikeda's 2016 pruning
theory, Zolkin et al.'s 2025 symplectic-map bifurcation diagrams,
Luo--Zhou's 2025 Hénon-like saddle-point equidistribution, and the 2026
Cantat--Dujardin multiplier-rigidity preprint.  None contains the exact
period-five action critical-value polynomial or a Hill-Kummer decoration.

## 8. Local nonduplication lock

The following repository sources were read and byte-locked:

| Local source | SHA-256 | Boundary |
|---|---|---|
| `phase1_hcs_c33_henon_action_collision_kummer/RESEARCH_QUESTION_BRIEF.md` | `14d1f8b33c4e26a9d0b977f0adb8c3a70e9cac7b6f6c2e7e95d94759e2072a64` | frozen C33 question |
| `phase1_hcs_c33_henon_action_collision_kummer/METHODOLOGY_BLUEPRINT.md` | `7df335e02cb74767f726e676375aca669707f95f88412f7a0232c9e1211a395e` | frozen falsifiers |
| `phase1_hcs_c33_henon_action_collision_kummer/PILOT_LEDGER.md` | `c5c2264b77c1f312e514dc91e6424cc74d8a611dabef81605ccdafca9c2dc9ce` | post-pilot exact identities |
| `phase1_hcs_c33_henon_action_collision_kummer/DEVILS_ADVOCATE_CHECKPOINT1.md` | `7e1e23a9332be5073776e7a2ed0563b602c52487243627e9f062eac311787315` | mandatory claim firewall |
| `henon_frobenius_scheme_obstruction/SOURCE_AUDIT.md` | `f7653c951703d9de13493fa86b438044b17b2befd51b0daa8026265c9bd81b41` | Endler--Gallas period-five collision |
| `phase3_hcs_c32_artin_schreier_quantum_trace/SOURCE_AUDIT.md` | `ca5ff6a5a88d320b4b9f82ca4fd08545f830c709a25c8f9836adb04cde8af199` | Morse-local Hill information loss |
| `docs/candidate_registry.md` | `eaf9770b1f945973bd3854b38baa0e76c436206264faee1097af384fe04bedf4` | repository candidate/obstruction ledger |
| `docs/prior_work/papers/5-An Area-Preserving Henon-Map Model.pdf` | `23dad812162728316f633081e1a1995d4c00614a70d0f5877d425c68d0c726b9` | foundational Hénon family only |

The audit therefore forbids novelty claims for the period-five marker
sextic, its ordinary \(S_6\) Galois group, the existence of a discrete Hénon
action, generic Maxwell nodes, the Hill formula, or generic Kummer/braid
monodromy.

## 9. Tool and search limitations

- No cross-model novelty-review endpoint was exposed in this session.  A
  separate same-family research agent performed an independent literature
  lane; this is not represented as cross-model validation.
- Failure to find a direct duplicate is recorded only as
  `NOT_FOUND_WITHIN_SEARCH_BOUNDS`.
- The exact coefficient searches returned no mathematical match, but search
  indexing can miss formulas inside PDFs.
- Older singularity-theory terminology varies between Maxwell set, Maxwell
  stratum, bifurcation set, conflict set, and equal-critical-value locus.
  All variants above were searched or followed by citation snowballing.
- Some catastrophe-theory sources reserve “Maxwell set” for equal global
  minima.  C33 uses the Lyashko--Looijenga equal-critical-value convention
  and makes no minima claim.
