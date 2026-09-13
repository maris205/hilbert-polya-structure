# Evidence Map and Source-Use Ledger

This table controls the use of project records in [manuscript.md](manuscript.md). The snapshot is commit `419ee36c1e310469209f7b83c096ec8aea448386`. A navigation page may orient the reader, but theorem-level statements remain controlled by the named canonical manuscript, claim ledger, evaluator, or receipt.

## Evidence classes

| Class | Meaning | Cannot be promoted into |
|---|---|---|
| **L** | Local mathematical result with a named object, assumptions, and source | A global Hilbert--Pólya or RH claim |
| **C** | Control, counterexample, negative calibration, or transfer obstruction | A universal impossibility theorem unless the source proves one |
| **P** | Process, provenance, source-lock, build, or receipt record | Mathematical correctness, Route credit, peer review, or publication |
| **U** | Unresolved, `UNASSIGNED`, `NOT_APPLICABLE`, `NOT_TESTABLE`, or external hold | Positive evidence or an implicit failure outside its named scope |

## Core records

| Key | Controlling record | Class | Permitted use in this paper | Explicit non-use |
|---|---|---|---|---|
| `P1-RM` | [rh_roadmap0.png](../rh_roadmap0.png) | P | Figure 1 and the A0--A4/B1--B5 obligation vocabulary | Gate/status dashboard |
| `P1-KB` | [P1 Wiki README](../README.md) | P | Six-line architecture; P24--P28 belong inside Session 5 | Proof authority |
| `P1-CL` | [Status and claim vocabulary](../01-status-and-claim-vocabulary.md) | P / U | Four-layer evidence separation and global nonclaim | Mathematical theorem source |
| `P1-X` | [Cross-stream relationships](../02-cross-stream-relationships.md) | P / U | Concept genealogy is not theorem/credit transfer | A formal dependency graph |
| `P1-META` | [P1 metadata README](../meta/README.md) | P | Derived-corpus provenance and source precedence | Mathematical validation |
| `Z0-R` | [Programme roadmap](../../zeta_mvp0/docs/PROGRAMME_ROADMAP.md) | P / U | Conditional five-stage programme | A statement that later stages ran |
| `Z0-C` | [Global claim ledger](../../zeta_mvp0/docs/GLOBAL_CLAIM_LEDGER.md) | L / U | Q/W/\(S_{\rm op}\), local scope, and \(P_0\)/Z/RH boundaries | An unqualified full trace or zero claim |
| `Z0-A` | [Imported-RH claim boundary](../../zeta_mvp0/rh_import_metadata/PRIME_DYNAMICS_RH_CLAIM_BOUNDARY.md) | P / U | Source-preserving archive status of imported RH material | Native `zeta_mvp0` evidence |
| `S1-C` | [LOG-0001 stable results](../../logistic_dynamics/LOG0001_STABLE_RESULTS.md) | L / U | Same-object analytic determinant chain and its two tuples | Riemann-target success or Route B |
| `S1-R` | [Logistic closeout](../../logistic_dynamics/EXPLORATION_CLOSEOUT.md) | C / U | Parked state and structural reopening discipline | A universal no-go theorem |
| `S2-S` | [C424--C428 evaluation scope](../../henon_dynamics/research_c424_c428/EVALUATION_SCOPE.md) | L / U | Exact object, clock, theorem scope, and target-boundary language for the five Hénon records | A complete target determinant or Route-B entry |
| `S2-E` | [C424--C428 evaluation adjudication](../../henon_dynamics/research_c424_c428/EVALUATION_ADJUDICATION.md) | L / U | Formal Hénon Route-A scope and limitations | Route B or RH credit |
| `S2-HOLD` | [C429--C433 checkpoint](../../henon_dynamics/research_c429_c433/SESSION_CHECKPOINT_2026-09-10.md) | P / U | Five admitted contracts and zero completed papers | Published/complete results |
| `S3-D` | [Batch07 final disposition](../../symplectic_map/docs/research-batch07/BATCH07_FINAL_CROSS_PAPER_DISPOSITION_V1_20260913.md) | L / P | Five local deliveries and pause | External peer review or Route advancement |
| `S3-E` | [Batch07 scientific audit](../../symplectic_map/docs/research-batch07/BATCH07_CROSS_PAPER_SCIENTIFIC_AUDIT_V1_20260913.md) | L / U | Bounded findings and `NOT_APPLICABLE` status | A Route PASS or FAIL |
| `S4-P` | [P211--P215 final QA](../../symbolic_dynamics/docs/papers211_215_sequence/FINAL_QA_REPORT.md) | L / P / U | Exact-five internal completion and narrow finite theorems | A0--A4 advance or external publication |
| `S4-ST` | [Symbolic current state](../../symbolic_dynamics/SYMBOLIC_DYNAMICS_STATE.md) | P / U | `HOLD_EXTERNAL` and paused state | A scientific verdict |
| `S5-R` | [Flow Systems proposal](../../flow_systems/propose-flow-systems.md) | P | Continuous-time design and Route vocabulary | Evidence that a candidate passed it |
| `S5-P` | [P24--P28 Stage-5 completion report](../../flow_systems/BATCH_ROUND9_STAGE5_COMPLETION_REPORT.md) | L / C / P / U | Scoped results; positive arithmetic A2 `0/5`; Route-B invocation `0/5` | A complete Hilbert--Pólya chain |
| `S5-END` | [P24--P28 Stage-6 skip receipt](../../flow_systems/BATCH_ROUND9_STAGE6_SKIP_RECEIPT.json) | P / U | Pipeline closure with scientific and Route status unchanged | Permission for new work or scientific progress |

## Canonical mathematical source pointers

The main manuscript avoids reproducing long proofs. If a reader needs a precise theorem rather than the paper’s bounded synthesis, use the original sources below.

| Stream | Canonical source entrypoints |
|---|---|
| zeta free exploration | [Paper 01 TeX](../../zeta_mvp0/paper_01_clock_preserving_henon/manuscript/main.tex), [Paper 02 TeX](../../zeta_mvp0/paper_02_certified_local_wave_trace/manuscript/paper/main.tex) |
| Logistic | [nuclear Fredholm TeX](../../logistic_dynamics/projects/exact_uc_polar_nuclear_fredholm/paper/main.tex), [growth-order TeX](../../logistic_dynamics/projects/exact_uc_polar_growth_order/paper/main.tex) |
| Hénon | [C424 TeX](../../henon_dynamics/research_c424_c428/papers/C424_integer_valued_quadratic/main.tex), [C428 TeX](../../henon_dynamics/research_c424_c428/papers/C428_integer_period_spectrum/main.tex) |
| Symplectic | [P27 TeX](../../symplectic_map/papers/27-positive-newton-translation-reciprocity/build/final-20260905-r0/main.tex), [P31 TeX](../../symplectic_map/papers/31-qpi-sharp-phase-mixing/paper/v3/main.tex) |
| Symbolic | [P211 TeX](../../symbolic_dynamics/papers/211-kernel-image-projection-feedback/main.tex), [P215 TeX](../../symbolic_dynamics/papers/215-prefix-drawdown-clock/main.tex) |
| Flow | [P24 final TeX](../../flow_systems/papers/24-bianchi-holonomy-flow/stage5_finalization/manuscript.tex), [P25 final TeX](../../flow_systems/papers/25-three-disk-scattering-flow/stage5_finalization/manuscript.tex), [P26 final TeX](../../flow_systems/papers/26-level11-newform-time-change/stage5_finalization/manuscript.tex), [P27 final TeX](../../flow_systems/papers/27-congruence-inverse-limit-no-go/stage5_finalization/manuscript.tex), [P28 final TeX](../../flow_systems/papers/28-bolza-magnetic-flow/stage5_finalization/manuscript.tex) |

For Flow Route-A tuples, use the original evaluator records rather than a README: [P24 proxy](../../flow_systems/evaluations/route_a/P24-BIANCHI-MARKED-WORD-PROXY/2026-08-28-round8.yaml), [P25 calibrator](../../flow_systems/evaluations/route_a/P25-Q-SYMBOL-NO-REPEAT-PHASE-CALIBRATOR/2026-08-28-round8.yaml), [P26](../../flow_systems/evaluations/route_a/P26-LEVEL11-NEWFORM-TIME-CHANGE/2026-08-28-round8.yaml), [P27 residual](../../flow_systems/evaluations/route_a/P27-CONGRUENCE-INVERSE-LIMIT-GEODESIC-FLOW/2026-08-28-round7.yaml), and [P28 proxy](../../flow_systems/evaluations/route_a/BOLZA-MAGNETIC-EVEN-L4-CERTIFIED-OWNER-PROXY/2026-08-28-stage1-round8.yaml).
