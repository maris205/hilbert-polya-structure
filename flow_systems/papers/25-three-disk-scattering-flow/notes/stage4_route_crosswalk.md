# Paper 25 Stage 4 Route-A crosswalk

Date: **2026-08-30**

Stage 4 improves object typing, positioning, and reproducibility without
changing either Route-A decision state.

| Evaluated object | Retained state | Stage-4 contribution | Why no promotion follows |
|---|---|---|---|
| Unit-roof symbolic calibrator | `(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)`; `ROUTE_A_REJECTED` | The consolidated four-object map makes its exact finite-type determinant and clock explicit. | A0 fails by construction, and this artificial clock cannot transfer credit to the physical flow. |
| Physical three-disk flow | `UNASSIGNED` | The exact two-witness noncohomology obstruction and the validation-only role of the 2,241-row replay are stated more sharply. | No physical determinant, arithmetic Euler product, target correspondence, or spectral operator is constructed. |

Final retained state:

```text
SYMBOLIC_ROUTE_A_TUPLE=(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)
SYMBOLIC_OVERALL=ROUTE_A_REJECTED
PHYSICAL_FLOW_ROUTE_A_TUPLE=UNASSIGNED
ROUTE_B_INVOCATION_ALLOWED=false
CANONICAL_RESULTS_REFRESHED=false
```

The marker-stripped Stage-4 preview builds in 13 A4 pages with no undefined
citations, undefined references, missing glyphs, fatal errors, or overfull
boxes. This preview is not a Stage-5 promotion.
