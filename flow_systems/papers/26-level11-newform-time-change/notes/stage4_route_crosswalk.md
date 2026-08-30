# Paper 26 Stage 4 Route-A crosswalk

Date: **2026-08-30**

Stage 4 strengthens the manuscript's finite theorem, reproducibility chain,
and diagnostic interpretation without changing the Route-A decision state.

| Route coordinate | Stage-3 state retained | Stage-4 contribution | Why no promotion follows |
|---|---|---|---|
| A0 | `WEAK_ARITHMETIC_RELATION` | The exact cycle-pushforward Hecke relation is typed more clearly, and the target-blind exact controls `y-z` and `y-2z` separate generic finite obstruction from any putative newform-specific residue. | The Hecke relation remains structural rather than discriminative; the both-controls-pass residue is zero, so no newform-specific mechanism is supported. |
| A1 | `WEAK` | The 138 registered instances, 55 source-word/prime groups, and 165 group-law rows now have a reader-facing index crosswalk, exact owner-to-taxonomy chain, and a self-contained bounded primitive-root completeness proof. | The evidence is still only the registered multiset with declared multiplicity. Cross-instance conjugacy canonicalization, deduplication, and a global primitive-owner census were not run. |
| A2 | `FAIL` | A first-use dictionary separates the finite owner family from unbounded formal repetition, and the two-control decomposition sharpens the finite/local negative result. | No function space, transfer operator, trace formula, determinant, convergence or continuation theorem, formal A2 evaluation, or root-counting campaign was constructed. |
| A3 | `FAIL` | Primitive-Euler claims are now consistently restricted to the registered multiset, with branch degree, primitive-root exponent, and repetition kept distinct. | No canonical global primitive product, Euler factorization, functional equation, or multiplicity theorem was established. |
| A4 | `FAIL` | The revised scope map makes the missing target-facing obligations explicit. | No operator, spectral target, or prime/zero dictionary was identified or tested. |

Final retained state:

```text
ROUTE_A_TUPLE=(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
OVERALL=ROUTE_A_EXPLORATORY
EVIDENCE_DOMAIN=REGISTERED_138_INSTANCE_55_GROUP_CORRESPONDENCE_COMPONENT_MULTISET
ROUTE_B_INVOCATION_ALLOWED=false
CANONICAL_RESULTS_REFRESHED=false
```

The marker-stripped Stage-4 preview builds in 15 A4 pages with no undefined
citations, undefined references, missing glyphs, fatal errors, or overfull
boxes. This preview is not a Stage-5 promotion. The preliminary Stage-4 drift
audit is not the mandatory Stage-4.5 E6 integrity invocation.

