# P31 Stage-1 Phase-1 Devil's-Advocate Resolution

Date: **2026-09-01 UTC**  
Scope: **Phase-1 design repair only**  
Status: **AUTHOR RESPONSE COMPLETE — independent Checkpoint-1 replay required**

## Immutable review record

The reviewed Devil's Advocate report remains unchanged at
`notes/stage1_phase1_devils_advocate.md`; its pre-revision SHA-256 is
`6cee89a965e53cd864426d089fa4190d5069faa45dc7dadab35f4ba9593be022`.
The pre-revision RQ-brief and methodology hashes were respectively
`2a34e5b6c25f24e3824d76ddb1990a2d34d224c1be01cfbaf3ecb1af1dc804d1`
and
`eac806ac7054592d1e8c1762e5c7c635582ef4db5dd1cdc9d9eff61499957708`.
This response does not revise the DA verdict or claim a new PASS; only an
independent reviewer may replay Checkpoint 1.

## Disposition summary

| Issue | Severity | Author disposition | Revised location |
|---|---|---|---|
| `P31-DA-1` | Major | **RESOLVED_IN_PHASE1_DESIGN** | RQ Brief, “Frozen operational definitions”; Methodology, registry and P5 |
| `P31-DA-2` | Major | **RESOLVED_IN_PHASE1_DESIGN / FEASIBILITY_REMAINS_PROVISIONAL** | FINER Feasible; Methodology P3–P4, validity, and kill gates |
| `P31-DA-3` | Minor | **RESOLVED_AS_PREEXECUTION_GATE** | Methodology, “Frozen controls” |
| `P31-DA-4` | Minor | **RESOLVED_IN_VERIFICATION_CONTRACT** | Methodology, target-blind plan, controls, and reliability criterion |

## Point-by-point response

### P31-DA-1 — global owner and cell-local incidence were conflated

Accepted. The revision now freezes three separate relations:

1. `G`, one row per global oriented primitive owner across the entire frozen
   population;
2. `I`, all 138 correspondence incidences keyed through owner, source, prime,
   cycle, branch, degree, and instance;
3. `C`, one unit per `(source,prime,degree,owner)` cell.

One owner occurring in several cells remains one global fact in `G` but enters
each distinct Hecke-group equation once through `C`. No pooled “global owner
moment” is created. The exact group estimand is now frozen as

```text
M(h,d) = sum_g 1[m(g,h,d)>0] * (k(g)/k(source_h))^2.
```

Its denominator is `k(source_h)^2` inside the squared ratio, with no count
average. The three law predicates, residuals, global `|G|` denominator,
group denominator 55, inherited instance denominator 138, cross-group rule,
and coordinate-conflict propagation are all explicit. The inherited
`2/2/134` taxonomy is labeled instance-level rather than predicted global
owner counts.

The previously strongest counter-argument is therefore answered by typing the
two scientific endpoints separately: global kernel identity is a property of
`G`; recurrence classification is a property of the frozen cell-incidence
operator applied group by group.

### P31-DA-2 — complete negative conjugacy certification was underspecified

Accepted. Feasible was reduced from `5/5` to **`4/5 — PROVISIONAL`**. The
revision freezes the complete universe of `binom(138,2)=9,453` unordered
pairs, four mutually exclusive pair statuses, their accounting identity, and
zero-unresolved closure rule. Positive, invariant-exclusion, and negative
certificate fields are separately specified.

The negative interface now requires a theorem ID/version and immutable
proof/source locator, input preconditions, the integral solution-lattice
construction, determinant/congruence reduction, centralizer quotient,
reduction domain, termination invariant, exhaustive-cycle payload, and an
independent validator. A height cutoff cannot certify nonconjugacy.

No such theorem/source was fabricated during Phase 1: its binding remains
`UNBOUND`. If the complete interface or any pair certificate is unavailable,
the registered endpoint is `NOT_EVALUABLE_CONJUGACY_INCOMPLETE`; an unresolved
audit may be reported, but no partial owner taxonomy or negative scientific
verdict may be emitted.

### P31-DA-3 — fixtures were not frozen

Accepted. The revision defines matrix height and total ordering, exact counts
and deterministic generation for eight known-conjugate, eight inverse, eight
proper-power, eight finite-quotient subgroup-split, and sixteen independently
bounded exhaustive fixtures. It fixes bounds, explicit conjugators, expected
verdicts, insufficient-population behavior, manifest fields, and the rule that
no fixtures may be added after outcomes.

Because this is Phase 1 and no fixture execution was authorized, the
instantiated 48-record manifest is honestly marked `NOT_PROVIDED`. That state
is now a hard preexecution gate, not discretion to choose fixtures later.

### P31-DA-4 — verifier independence was too weak

Accepted. Byte-identical rebuilds are now labeled determinism evidence only.
The independent verifier must directly check conjugator equations, replay
finite-quotient obstructions, validate negative certificates against the
separate theorem/termination contract, and run sixteen fixtures whose complete
conjugator bounds have independent elementary proofs. Failure of any contract
or exhaustive fixture closes no ledger.

## Closure of the DA “What's missing” list

| Missing item | Design response |
|---:|---|
| 1 | Exact `M(h,d)` formula, normalization denominator, three law predicates, and kernel/group endpoints frozen |
| 2 | `G`/`I`/`C` schemas and the cross-group owner rule frozen |
| 3 | Complete theorem/precondition/termination/negative-certificate interface specified and gated |
| 4 | All 9,453 unordered pairs accounted for by a four-status identity with zero unresolved required |
| 5 | Deterministic 48-fixture specification and immutable preexecution manifest contract frozen |
| 6 | `NOT_EVALUABLE_CONJUGACY_INCOMPLETE` and unresolved-pair audit frozen as the honest fallback |

## Stress-test dispositions after revision

- Duplicating one owner across groups no longer changes global owner count;
  its separate cell incidences follow the explicit group equations.
- Giving one owner multiple degrees in one group yields
  `NOT_EVALUABLE_DEGREE_CONFLICT`, never an analyst-selected degree or false
  law verdict.
- Failure to find a conjugator below a bound remains non-evidence; without a
  complete negative certificate the global endpoint is not evaluable.
- All 138 roots being distinct remains an admissible closed outcome if and
  only if all 9,453 pair rows carry valid terminal certificates.

## Phase boundary

This resolution records design changes only. It performs no source search,
bibliography work, synthesis, scientific computation, result generation,
claim registration, manuscript drafting, Route promotion, or canonical
refresh.
