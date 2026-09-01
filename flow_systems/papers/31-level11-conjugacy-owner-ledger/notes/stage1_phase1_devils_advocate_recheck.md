# P31 Devil's Advocate Recheck — Checkpoint 1

Date: **2026-09-01 UTC**  
Role: **same independent Devil's Advocate reviewer**  
Boundary: **Phase-1 design recheck only; no external search, Phase-2 work, or scientific computation**

## Input integrity

| Input | SHA-256 |
|---|---|
| `stage1_phase1_devils_advocate.md` | `6cee89a965e53cd864426d089fa4190d5069faa45dc7dadab35f4ba9593be022` |
| revised `stage1_phase1_rq_brief.md` | `b5927371ff7422b084dee6c8644ba14981b88b8f15cab9997f5df254cdd312b1` |
| revised `stage1_phase1_methodology_blueprint.md` | `046e4b826ffd0cfbf2e697d13bbf8d925dc775ef262798af4c4f2ef8e9ca23d2` |
| `stage1_phase1_resolution.md` | `624780725fc006517bfc391c0945e8a2ae67a09c482f6b28d4d1278bc49b204e` |

The initial DA bytes match the hash recorded in the resolution. The resolution
does not overwrite the initial verdict; this file performs the requested replay.

## Final verdict: PASS

All four original findings are adequately resolved at the Phase-1 design
level. The unbound subgroup-conjugacy theorem contract and uninstantiated
fixture manifest remain explicit **preexecution gates**, not evidence that
conjugacy closure has already been achieved. `PASS` therefore approves the
revised scoping contract only; it does not certify a solver, an owner ledger,
or a scientific result.

## Item-by-item recheck

### P31-DA-1 — global owner versus cell-local incidence

- **Original severity:** Major
- **Recheck verdict:** **RESOLVED**
- **Evidence checked:**
  - `G` is now one row per global oriented primitive owner across all 138
    instances; source, prime, branch, cycle, and degree cannot multiply owners.
  - `I` preserves all original correspondence incidences under an explicit
    owner/source/prime/cycle/branch/degree/instance key.
  - `C` deduplicates only within
    `(source_word,prime,hecke_degree,owner_id)` and is never called a global
    owner quotient.
  - Cross-group recurrence is explicit: one owner stays one row in `G` but may
    enter each separate Hecke-group equation once through `C`; no pooled global
    owner moment is defined.
  - The conflict matrix freezes `m(g,h,d)`, `u(g,h,d)`, `D(g,h)`, priority
    statuses, and orthogonal cross-group flags.
  - The estimand is fixed as
    `M(h,d)=sum_g u(g,h,d)*(k(g)/k(source_h))^2`, an unaveraged exact rational
    sum. The three law predicates, degree-conflict propagation, exact residuals,
    and distinct denominators `|G|`, 55, and 138 are separately typed.
- **Stress result:** Duplicating one global owner across two groups leaves `G`
  unchanged and produces only the two prospectively defined group incidences;
  the former strongest counter-argument no longer holds.

### P31-DA-2 — complete negative subgroup-conjugacy certificate

- **Original severity:** Major
- **Recheck verdict:** **RESOLVED BY FAIL-CLOSED CONTRACT**
- **Evidence checked:**
  - Feasibility is reduced to `4/5 — PROVISIONAL`.
  - The complete universe is all `binom(138,2)=9,453` unordered row pairs, with
    exactly four statuses and a zero-unresolved accounting identity.
  - Positive certificates contain a literal subgroup conjugator and exact
    equation checks; invariant exclusions name the invariant and both values.
  - Negative certificates require a bound theorem ID/version/source,
    preconditions, full integral solution lattice, determinant/congruence
    reduction, centralizer quotient, finite reduction domain, termination
    invariant, exhaustive payload, hash, and separate validator verdict.
  - Bounded search failure cannot become negative evidence.
  - The theorem binding remains honestly `UNBOUND`. Until it is supplied,
    `NOT_EVALUABLE_CONJUGACY_INCOMPLETE` forbids a closed partition, global
    taxonomy, or cell-local law verdict.
- **Stress result:** A large failed conjugator search still produces no
  nonconjugacy conclusion; only a contract-valid exhaustive certificate can
  close that pair.

### P31-DA-3 — adversarial fixtures

- **Original severity:** Minor
- **Recheck verdict:** **RESOLVED AS A HARD PREEXECUTION GATE**
- **Evidence checked:** matrix height and ordering, exact fixture counts,
  explicit conjugators, power exponents, subgroup-split moduli and bound,
  insufficient-fixture status, bounded-exhaustive proof fields, manifest
  schema, and no-post-outcome-addition rule are now frozen.
- **Residual status:** the 48-record manifest is correctly `NOT_PROVIDED`; this
  blocks solver execution and is not silently treated as a completed control.

### P31-DA-4 — verifier independence

- **Original severity:** Minor
- **Recheck verdict:** **RESOLVED**
- **Evidence checked:** byte identity is now labeled determinism only. The
  verifier must directly check witness equations, replay finite-quotient
  obstructions, validate negative payloads against a separately stated theorem
  and termination contract, and pass sixteen independently bounded exhaustive
  fixtures.

## Closure of prior missing-content list

| Prior missing item | Recheck status |
|---|---|
| Exact three-law estimands and denominators | Closed through `M(h,d)`, exact law predicates, residuals, and distinct global/group/instance denominators |
| Global-owner/incidence schemas and cross-group rule | Closed through separate `G`, `I`, `C`, and conflict-matrix contracts |
| Complete negative-certificate interface | Closed at design level; theorem binding remains a fail-closed prerequisite |
| All-pairs accounting | Closed at exactly 9,453 pairs and zero unresolved required |
| Frozen fixture manifest rule | Closed at specification level; uninstantiated manifest blocks execution |
| Honest incomplete-ledger fallback | Closed as `NOT_EVALUABLE_CONJUGACY_INCOMPLETE` with no partial taxonomy |

## Remaining prerequisites, not new findings

1. Bind and independently validate the P3 theorem/source/implementation
   contract before any scientific pair classification.
2. Instantiate and hash all 48 fixtures before solver execution.
3. Preserve the exact source-lock and zero-unresolved rules when those gates
   are later attempted.

Failure of any prerequisite changes the later result to `NOT_EVALUABLE`; it
does not reopen researcher discretion or invalidate the present Phase-1
design.

## Checkpoint disposition

**PASS — Checkpoint 1 scoping contract accepted.** Phase 2 may investigate and
verify the still-unbound mathematical sources/contracts under the pipeline's
separate authorization. This recheck authorizes no computation, result,
manuscript drafting, claim registration, Route promotion, or canonical refresh.
