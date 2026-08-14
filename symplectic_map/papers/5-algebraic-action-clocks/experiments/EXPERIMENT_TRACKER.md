# Experiment Tracker

**Candidate:** `algebraic_exact_action_clock_obstruction_v1`  
**Tracker date:** 2026-08-14  
**Stage:** official source-locked static audit complete; final manifest closure authorized  
**Candidate exact/numerical runs:** 0 / 0

## Immutable lock record

- Source lock v2 SHA-256 (historical, before independent review):
  `552ec986fc35d0afb3137050ddf8dfe748647c51b8517293a0e072b9612b1497`
- Source lock v3 SHA-256 (mandatory pre-execution repair):
  `d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7`
- Proof package SHA-256:
  `c579e2da093a8ab588a5818bab0df59a47804792fcdfa338777f48e1bd1a1214`
- Internal counterexample-audit SHA-256:
  `9462f5afa9b070e268e811d164bebd8821f1bde124f6465199bd55e551879ee9`
- JSON validator: Python standard-library `json.tool` because `jq` is not
  installed in the workspace.
- Static symbolic engine: SymPy 1.14.0.

The lock hash is recorded before any candidate periodic point or action is
computed.  Editing `source_lock.json` requires a versioned amendment and a
new hash; it may not be justified by later output.

## Run ledger

| Run | Type | Input scope | Output | Status | Candidate data used |
|---|---|---|---|---|---|
| R000 | Source-lock validation | `source_lock.json` | JSON parse PASS; SHA-256 recorded | PASS | None |
| R001 | Written proof reconstruction | General field evaluation, Hermite--Lindemann implication, gauge ledger | Conditional theorem survives; normalization assumption made explicit | PASS, internal | None |
| R002 | Static symbolic identity audit | Formal variables for $H_a$, $G$, $L_a$, and a length-7 gauge telescope | All five Hénon residuals zero; gauge sum $=7C$ | PASS | None |
| R003 | Adversarial counterexample pass | Frozen assumptions and nine attack families | Broad claim refuted; narrow theorem survives | PASS, same workstream | None |
| R004 | Independent counterexample cross-check | Frozen theorem and attack checklist only | `REPAIR`: core theorem passes; nine mandatory boundary repairs identified | COMPLETE | None |
| R005 | Source-lock v3 repair | R004 only; no candidate output | General endpoint term, logarithm edge cases, orbit field, low-period multiplicity, and fail-closed evaluation gates incorporated | PASS | None |
| R006 | Independent pre-run code review round 1 | Static code, syntax checks, safe tests, isolated negative controls | `DEPLOYMENT_FAIL`: brittle R002, scanner self-skip, incomplete manifest closure, hardcoded runtime date | COMPLETE | None |
| R007 | Author repair and safe regression suite | Review findings only; formal CLI remained closed | Four findings repaired; syntax PASS; 72/72 safe tests PASS | READY FOR ROUND 2 | None |
| R008 | Independent pre-run code review round 2 | Repaired static code plus exact reviewer reproductions | `DEPLOYMENT_FAIL`: R002 semantic fail-open; result manifest accepted extras and nested duplicates | COMPLETE | None |
| R009 | Author fail-closed repair and safe regression suite | R008 findings only; formal CLI remained closed | Unique exact JSON proof contract, exact normalized tagged equations, whole-proof control-character scan, and exact flat result schema implemented; syntax PASS; 82/82 safe tests PASS | READY FOR ROUND 3 | None |
| CR3 | Independent pre-run code review round 3 | Exact R002 and manifest negative controls plus safe regression checks | `DEPLOYMENT_PASS`; authority SHA-256 `629ed6bfe06f73ad387712c53f28aa73ee6c466098dd22ef502fd34f2d32ba58` | PASS | None |
| OTEST | Official unit/JUnit run | Source-locked code and tests | 82 passed; zero failures/errors; JUnit SHA-256 `c29e6bc5f805f32d9a9620dfad42bfe9474973f430c857531970e0f28782fa62` | PASS | None |
| OSTATIC | Official formal static audit | R000, R001, R002, R010--R019, R020--R023 only | Every registered stage PASS; classification `ALGEBRAIC_NORMALIZED_ACTION_CLOCK_REJECTED_BY_ALL_PERIOD_THEOREM` | PASS | None |
| OCLOSE | Strict final manifest closure | Exact flat result allowlist, required source/proof/tracker files, executable Python | Prescribed as the final mechanical step after this tracker freeze; no included input may be edited afterward | AUTHORIZED | None |
| R100+ | Candidate periodic-orbit/action audit | Inherited $a=u$, periods at most 1--3 | Not authorized in this task | NOT RUN | None |

## R002 exact residuals

The static script checked the following polynomial identities without
solving for an orbit:

| Residual | Exact result |
|---|---:|
| $\partial_qG-(2q^2-p)$ | 0 |
| $\partial_pG+q$ | 0 |
| $(\partial_qL_a-p)|_{Q=q^2-a-p}$ | 0 |
| $(-\partial_QL_a-P)|_{P=q}$ | 0 |
| $(L_a+G)|_{Q=q^2-a-p}$ | 0 |
| $\sum_{j=0}^{6}(\chi_{j+1}-\chi_j+C)$ with $\chi_7=\chi_0$ | $7C$ |

This is a sign and implementation check only.  It is not experimental
evidence for the all-period algebraicity or transcendence statements.

## Proof-audit status by claim

| Claim | Status | Remaining gate |
|---|---|---|
| C1 algebraic action | PASS AFTER v3 REPAIR | Stepwise definedness and pole gates explicit. |
| C2 prime-logarithm exclusion | PASS AFTER v3 REPAIR | $\beta=0$ and the $A=0,\beta=1$ exception explicit. |
| S1 gauge formula | PASS AFTER v3 REPAIR | General endpoint mismatch retained. |
| S2 transcendental-constant counterexample | PASS | None beyond independent cross-check. |
| S3 Hénon potential/type-1 sign | PASS | Static residuals recorded. |
| S4 algebraicity of finite Hénon periodic points | PASS, written proof | Independent projective-dimension review. |
| S5 $S$-integrality and denominator 3 | PASS, written proof | Independent valuation review. |
| Novelty/positioning | PASS | Retain 3/10 standalone and no priority claim. |

## Leakage and execution audit

- External prime tables accessed: **no**.
- Riemann-zero data accessed: **no**.
- Candidate periodic points computed: **no**.
- Candidate actions computed: **no**.
- Parameter tuned after action inspection: **no**.
- Transcendental scale or per-step constant fitted: **no**.
- Floating comparison with $\log p$: **no**.

## Current gate

Independent Round 3 authorized the exact static deployment, and the official
suite and formal static CLI both passed.  All seven JSON outputs retain a
closed candidate-execution gate: no inherited parameter, periodic point,
action, prime table, or zero datum was evaluated.  The result label is
`ALGEBRAIC_NORMALIZED_ACTION_CLOCK_REJECTED_BY_ALL_PERIOD_THEOREM`.

The plan decision is `GO_AS_NARROW_DESIGN_CERTIFICATE`; publication should
`MERGE_IF_STANDALONE_DEPTH_IS_REQUIRED` because standalone novelty remains
3/10.  The route decision closes only the frozen normalized algebraic action
as an exact prime-logarithm clock.  It does not close other symplectic or
arithmetic clocks.  After this tracker is frozen, the strict manifest builder
is the sole remaining mechanical action; all hashed inputs then remain
immutable.
