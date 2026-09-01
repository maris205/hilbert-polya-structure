# P33 Devil's Advocate Report — Checkpoint 1

Date: **2026-09-01 UTC**  
Workflow: **ARS Deep Research / FULL / Phase 1 only**  
Reviewed inputs:

- `stage1_phase1_rq_brief.md`, SHA-256
  `6f56c66f1ab3f258e75c1bb019a7c9b99e938649ac8bb4053acaa8e3048d8c25`;
- `stage1_phase1_methodology_blueprint.md`, SHA-256
  `e2bbd26b673f0ba8d31a5c826c3331018b1cd82e43d68bbc73ebff1087a362f9`.

Reviewer independence: the Devil's Advocate did not draft either reviewed P33
file. This review used only repository-local material and no network access.

## Checkpoint 1 verdict: **REVISE**

No Critical issue was identified. Three Major issues require Phase-1 revision
before the scholar is asked to confirm progression to Phase 2. The exact-source
firewalls, full-conjugacy standard, negative-result retention, and A2/Route-B
closures are strong; the problem is the interpretation and prespecification of
the matched comparison, not its insistence on exact computation.

## Read-only upstream fact check used by this review

The blueprint binds P28 artifacts whose already-certified implications are
material to scoping:

- the Bolza certificate records
  `sys(Bolza)=2*acosh(1+sqrt(2))`, approximately `3.05714`, hence strictly
  above `21/10`;
- the control certificate records
  `sys(control)=2*acosh(1/(2*exp(-1/5)-1))`, approximately `2.04303`, hence
  strictly below `21/10`, with a primitive equality witness `g0*g3`;
- the control finite-ball certificate already proves that every class with
  length at most `21/10` has a conjugate in the frozen component.

These are not new P33 results. They are consequences of the exact upstream
locks that P33 explicitly requires. Therefore, if replay succeeds, the cutoff
already straddles the two systoles: the Bolza candidate universe is empty and
the control universe is nonempty before any new quotient census is performed.

## Critical issues

No Critical issues identified.

## Numbered issues

### P33-DA-1 — The proposed A0 comparison is systole-confounded

- **Severity:** Major
- **Type:** Scope / comparative validity / framing bias
- **Location:** RQ brief, `Topic area`, Sub-question 3, and `Scope object`;
  methodology blueprint, `Matched readout`, `A0 adversarial and
  proves-too-much checks`, and `Comparative validity`.
- **Problem:** The documents describe the two surfaces as geometrically
  matched on topology, curvature, area, clock, subtype, and cutoff, but the
  cutoff is below the known Bolza systole and above the known control systole.
  Any empty-versus-nonempty contrast is therefore fully explained by this
  local geometric scale difference. Arithmetic versus nonarithmetic status is
  not the only changed variable and is not isolated by this design.
- **Impact:** A closed exact census can be valuable A1 bookkeeping, but its
  owner counts cannot support arithmetic specificity or an A0 discrimination
  claim. Calling the result an A0 adversarial comparison without a
  systole-confounding disposition invites a false causal/arithmetic reading.
- **Recommendation:** Before Phase 2, freeze one of two honest paths:
  (a) retain the current two-surface census but classify every between-surface
  count contrast as `A0_INCONCLUSIVE_SYSTOLE_CONFOUNDED`, using it only for A1
  completeness/method validation; or (b) propose a separately authorized
  systole-normalized or length-density-matched control design. Path (b) changes
  the current immutable cutoff/scope and cannot be inserted silently.

### P33-DA-2 — The declared outcome space contradicts the frozen upstream locks

- **Severity:** Major
- **Type:** Internal consistency / outcome prespecification
- **Location:** Methodology blueprint, `Method`: “No success direction is
  predeclared; zero owners on either surface is a valid closed outcome.”
- **Problem:** If the required replay passes, zero Bolza owners below the
  cutoff and at least one primitive control owner are already forced by the
  two systole theorems. A zero-owner control manifest cannot be a valid closed
  outcome; it would contradict the locked primitive equality witness. If the
  source replay fails, the design requires a stop rather than a closed zero.
  Likewise, the P33 run is target-blind with respect to prime/zero data, but it
  is not blind to these already-known geometric outcomes.
- **Impact:** The current wording creates an impossible success state and
  inaccurately presents the new census as direction-free. That weakens the
  integrity of later preregistration and makes an upstream contradiction look
  like an admissible result.
- **Recommendation:** Replace the symmetric zero-outcome language with replay
  invariants: `Bolza candidates=0` and `control primitive owners>=1` whenever
  all upstream locks pass. Any violation is `UPSTREAM_REPLAY_CONTRADICTION`
  and stops closure. Describe `Lambda=21/10` as an **inherited historically
  target-blind cutoff whose coarse support outcome is now known**.

### P33-DA-3 — The A0 control panel is not mapped to the Route-A mandatory-control gate

- **Severity:** Major
- **Type:** Missing design element / Route-scope ambiguity
- **Location:** RQ brief, Sub-question 3; methodology blueprint, `A0
  adversarial and proves-too-much checks` and `Route boundary`.
- **Problem:** The nonarithmetic surface is one genuine matched control and the
  marked-word proxy is a simpler-parent diagnostic. The “data-firewall
  control” checks forbidden-input absence but is not one of Route A's
  comparative arithmetic controls. The documents neither identify three
  qualifying controls nor state that the formal A0 control gate remains
  incomplete.
- **Impact:** A later report could wrongly treat one surface and one proxy as
  closure of A0's mandatory-control requirement. The full tuple is currently
  unassigned, but the permitted A0 vocabulary is not frozen tightly enough to
  prevent promotion by implication.
- **Recommendation:** Add an explicit control-accounting table in the Phase-1
  design. Unless a third qualifying control is separately authorized, freeze
  `A0_CONTROL_PANEL_INCOMPLETE`, prohibit a formal A0 verdict, and limit P33 to
  one adversarial observation plus A1 census evidence.

### P33-DA-4 — Certification failure and scientific census status are conflated

- **Severity:** Minor
- **Type:** Method / result taxonomy
- **Location:** Methodology blueprint, `Outcome states` and `Phase-2
  dependency`.
- **Problem:** `CERTIFICATION_OBSTRUCTION` and
  `SHARPLY_BOUNDED_INCOMPLETE_CENSUS` are workflow/evidence states, whereas a
  closed owner census is a scientific result. The same single outcome field
  risks making lack of a complete conjugacy method look like a mathematical
  no-go for owners.
- **Recommendation:** Freeze separate fields such as
  `execution_status`, `census_completeness`, `scientific_result`, and
  `route_interpretation`. An unavailable solver yields `NOT_EVALUABLE`, not a
  negative owner theorem.

### P33-DA-5 — `CLOSED_MATCHED_CENSUS` is semantically ambiguous

- **Severity:** Minor
- **Type:** Reporting clarity
- **Location:** Methodology blueprint, `Outcome states`.
- **Problem:** “Matched census” can be read as matched counts, although the
  intended meaning appears to be that both censuses used a matched contract
  and both closed.
- **Recommendation:** Rename it `BOTH_CENSUSES_CLOSED_UNDER_COMMON_CONTRACT`
  and report the two counts separately.

## Strongest counter-argument

> The project is framed as an arithmetic-versus-nonarithmetic matched census,
> but its frozen upstream theorems already place `21/10` below the Bolza
> systole and above the control systole. Thus the coarse contrast is known in
> advance and has a complete geometric explanation. The remaining work is a
> control-side conjugacy quotient and multiplicity census; however exact, it
> cannot isolate arithmetic specificity and should not be marketed as closing
> A0.

The best defense is that P33 still closes a real A1 ownership/completeness gap
under one exact contract. That defense succeeds only if the A0 language is
narrowed and the known systole asymmetry is made an explicit confound rather
than treated as the comparison's finding.

## What's missing

1. An explicit “known before P33” ledger for the two systole/cutoff
   implications and the control equality witness.
2. A prespecified confounding disposition for the nonmatched systole scale.
3. A Route-A A0 control-count table distinguishing a genuine comparative
   control from a data firewall and a proxy diagnostic.
4. Separate workflow, completeness, scientific-result, and Route-status
   fields.
5. A frozen interface for the full conjugacy certificate: required witness,
   nonconjugacy certificate, completeness proof, and lawful
   `NOT_EVALUABLE` path. Phase 2 may identify an implementation, but it should
   not redefine these success criteria after seeing the census.
6. A precise significance statement explaining what is learned beyond the
   already-known empty Bolza universe and nonempty control universe.

## Stress-test results

| Stress test | Result | Reason / required disposition |
|---|---|---|
| Remove the strongest upstream systole certificates | **FAIL** | Feasibility and the finite candidate universes lose their proof base. This dependency is acceptable only because it is explicit and hash-bound. |
| Flip the RQ: can both censuses close while the A0 inference remains invalid? | **YES** | Exact A1 closure does not remove the systole confound or supply three A0 controls. |
| Mask the arithmetic/nonarithmetic labels | **FAILS A0 discrimination** | The cutoff-support contrast is still predicted by the two systoles, showing that arithmetic labels are unnecessary to explain it. |
| Move the cutoff below the control systole or above the Bolza systole | **HIGH SENSITIVITY** | The population contrast changes at known geometric thresholds; no robustness claim is licensed. This is a diagnostic only, not permission to change the frozen cutoff. |
| Let one surface close and the other retain one unresolved conjugacy class | **NO MATCHED READOUT** | Report separate bounded manifests; do not compare counts or infer A0. |
| Replace full conjugacy with equal trace/length or a bounded conjugator search | **FAIL** | The blueprint correctly prohibits this; the fail-closed rule must remain. |
| Suppose the full conjugacy method is unavailable | **PARTIAL** | The contract-feasibility RQ receives “not closed,” but no scientific owner/no-go conclusion follows; statuses must be separated. |
| “So what?” — is significance justified as written? | **NO** | It becomes justified only as exact A1 quotient/completeness closure or as a documented certification obstruction, not as arithmetic specificity. |

## Item-by-item disposition recommendations

| Finding | Recommended disposition before Phase 2 | Recheck condition |
|---|---|---|
| P33-DA-1 | `MUST_FIX` | Systole confound is explicit and A0 wording is narrowed, or a newly authorized matched-scale design is supplied. |
| P33-DA-2 | `MUST_FIX` | Impossible zero-control outcome is removed; upstream replay invariants and contradiction stop are frozen. |
| P33-DA-3 | `MUST_FIX` | Qualifying controls are counted against Route A and formal A0 is marked incomplete unless the requirement is actually met. |
| P33-DA-4 | `SHOULD_FIX` | Workflow/evidence status is separated from scientific census result. |
| P33-DA-5 | `SHOULD_FIX` | Closed-both-surfaces status is renamed and counts remain separate. |

## Strengths retained

- The owner unit is full-group conjugacy modulo inversion, not a trace or word
  proxy.
- Primitivity, nonconjugacy, completeness, and sign decisions fail closed.
- Upstream artifacts and resource ceilings are explicitly frozen.
- Prime/zero inputs, post-hoc cutoff changes, magnetic comparison, A2--A4,
  and Route B are excluded.
- A bounded incomplete result is retained rather than hidden.

## Checkpoint routing

**REVISE.** Do not treat Checkpoint 1 as passed. Revise only the Phase-1 RQ and
methodology surfaces under author/orchestrator control, then rerun an
independent Checkpoint-1 review. This report does not authorize Phase 2,
scientific execution, a bibliography, synthesis, drafting, Route evaluation,
or changes to any upstream P28 artifact.
