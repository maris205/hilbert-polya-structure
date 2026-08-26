# P22 Stage 4.5 Round 2 route-roadmap crosswalk

Date: **2026-08-25 UTC**  
Scope: **read-only correspondence to the two governing files in `skills/`**

This is not a Route-A or Route-B evaluation and grants no route or gate credit.

## Governing bytes

| Roadmap file | Version | SHA-256 | Byte check |
|---|---|---|---|
| `skills/route-a-evaluator.md` | 0.2.0 | `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c` | MATCH |
| `skills/route-b-evaluator.md` | 0.2.0 | `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595` | MATCH |

## Exact evaluator correspondence

| Evaluator boundary | What its roadmap requires | What P22 supplies | Round 2 status |
|---|---|---|---|
| Route A inputs/A0 entry | A frozen dynamical candidate with phase space, dynamics, arithmetic origin, clock, normalization, determinant convention, cutoff/precision, and data split | A pure-algebra theorem about additive sheaf lifts on two Grothendieck sites; none of the mandatory Route-A object fields is defined | `NOT_TESTABLE`; no A0--A4 tuple |
| Route A accumulation | Route-relevant results may be recorded as a structural prior, obstruction, benchmark, implementation pattern, or round-2 clue, but evaluation credit requires the frozen candidate inputs | The descent obstruction is mathematically reusable context for future work, but this paper does not connect it to a frozen orbit/transfer-operator/determinant candidate | Context only; no advancement and no Gate A credit |
| Route B entry | Normally `ROUTE_A_SUCCESS_ROUTE_B_READY`, then one compatible Hilbert space, operator, domain, boundary conditions, clock, and normalization | No Route-A-ready receipt and no operator-theoretic input tuple | `ROUTE_B_NOT_TESTABLE`; invocation remains disallowed |
| Route B layers | B1 complete operator, B2 self-adjointness, B3 spectral type, B4 exact prime-power trace/Weil compatibility, B5 completed-xi divisor identity | None of these objects or theorems occurs in P22 | no B1--B5 tuple; no Hilbert--Pólya claim |
| Gates A--E | Same-object determinant, unitary/scattering completion, self-adjoint generator/spectral law, arithmetic trace, completed-zeta divisor | P22 proves a different site-theoretic obstruction | all gates `NOT_REACHED` |

The manuscript's word “lift” means a lift of an additive morphism of sheaves;
it is not Route-A A4 natural quantization or Route-B operator liftability. Its
finite-flat “cover” is a site cover, not a phase space, flow, clock, or orbit
ledger.

## Authorized Round 2 corrections

| Correction | Manuscript effect | Route effect |
|---|---|---|
| `IL-MINOR-1`, B0005 | Synchronizes displayed draft date to 25 August 2026 | metadata only; none |
| `IL-MINOR-2`, B0094 | Finalizes an author-owned materials-on-request policy | declaration only; none |

## Carried state

```text
ROUTE_A_EVALUATION=NOT_TESTABLE
A0_A1_A2_A3_A4_TUPLE=NOT_ASSIGNED
ROUTE_A_ADVANCEMENT=NONE

ROUTE_B_INVOCATION_ALLOWED=false
ROUTE_B_ENTRY_AUTHORIZED=false
ROUTE_B_STATUS=ROUTE_B_NOT_TESTABLE
B1_B2_B3_B4_B5_TUPLE=NOT_ASSIGNED
HILBERT_POLYA_CLAIM_ALLOWED=false

GATE_A=NOT_REACHED
GATE_B=NOT_REACHED
GATE_C=NOT_REACHED
GATE_D=NOT_REACHED
GATE_E=NOT_REACHED
```

Any future route assignment requires a separate evaluator run on newly frozen,
route-relevant inputs. Stage 4.5 integrity PASS, manuscript completion, or
publication readiness cannot substitute for that run.
