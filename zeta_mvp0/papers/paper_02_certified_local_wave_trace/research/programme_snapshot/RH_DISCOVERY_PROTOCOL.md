# RH Candidate Discovery Protocol

## Provenance and intended use

This protocol was formalized on 2026-08-05, after substantial exploration of
the current Hénon family.  It is a **prospective protocol for future
candidates**, not a preregistered reconstruction of how the (a=1.02) family
was historically selected.  Historical claims are supported only by the
contemporaneous R000--R107A protocols and archives that actually exist.  R200
is the first current branch designed under the prospective bridge rules below.

## 1. Research posture

This project treats the Hilbert--Pólya problem as an **unknown-structure
search**, not as a nearly completed proof whose remaining task is to add more
local lemmas.  The default loop is therefore breadth first:

\[
 \text{generate structurally different objects}
 \longrightarrow
 \text{screen necessary invariants}
 \longrightarrow
 \text{look for anomalous but reproducible signals}
 \longrightarrow
 \text{promote only the survivors to operator theory}.
\]

High-risk and heuristic ideas are allowed at the generation stage.  They are
not allowed to inherit theorem language.  Most candidates are expected to
die, and an informative death is a successful research outcome.

This is deliberately different from a theorem-engineering programme such as
a conditional route to the twin-prime conjecture.  There the first priority
would be to write an end-to-end implication, identify the few missing bridges,
and close them one at a time.  Here the first uncertainty is the object itself,
so premature bridge closure can lock the search onto the wrong structure.

### AI-laboratory mode selection

The distinction is operational rather than rhetorical:

| Research regime | Default search order | Primary artifact | AI role | Main failure mode |
|---|---|---|---|---|
| RH, where the spectral object is unknown | Breadth first: objects \(\to\) invariants \(\to\) anomalous signals \(\to\) operators | Candidate portfolio plus explicit death log | Structure explorer and search engine | Local optimization around familiar but structurally inadequate models |
| TPC-like theorem engineering, where several proof skeletons already exist | Path first: conditional theorem \(\to\) minimum bridges \(\to\) one bridge at a time | End-to-end implication graph plus a minimal bridge ledger | Systems engineer and theorem-attack group | Accumulating local lemmas without a route from hypotheses to target |

The mode-switch rule is simple.  An RH candidate stays in breadth-first
exploration until it survives cheap death tests and has at least one analytic
carrier.  It is then frozen and transferred to bridge closure.  If Route A
reveals a circular bridge, a hidden insertion of target data, or an
energy-dependent object, the candidate returns to the death log rather than
being rescued by more numerical fitting.

## 2. Two complementary routes

Every active idea receives two independent assessments.

### Route B: structural exploration

Route B asks whether the candidate is worth keeping at all.

1. Generate objects from genuinely different mechanism classes, not cosmetic
   parameter changes.
2. Apply the cheapest fatal tests first.
3. Search for a signal that survives controls, resolution changes, and blind
   reruns.
4. Promote only after the signal has a plausible analytic carrier.

Route B may use heuristic asymptotics, numerical experiments, symbolic
search, or AI-generated constructions.  Every such output remains labelled
as a conjecture, diagnostic, or numerical proposition.

### Route A: bridge closure

Route A begins only after a candidate survives Route B or when an existing
mathematical skeleton is already unusually strong.  It asks for the shortest
conditional chain from the current object to a genuine Hilbert--Pólya
mechanism:

\[
 Q\longrightarrow W\longrightarrow S\longrightarrow P\longrightarrow Z.
\]

For each missing arrow, Route A must state one minimal bridge lemma, its exact
hypotheses, and a falsification test.  Adding unrelated lemmas does not count
as progress.  If a bridge requires inserting primes or zeros by hand, the
arithmetic route dies even if the resulting numerical fit is excellent.

The routes are not competing theories.  Route B discovers and kills; Route A
proves, exposes, and concentrates effort.  A healthy portfolio keeps both
running, but never merges their evidence levels.

## 3. Necessary gates

| Gate | Required question | Minimum promotion evidence | Fatal failure |
|---|---|---|---|
| Q -- quantum object | Is there a fixed linear object on a specified Hilbert space? | Self-adjointness or a precisely defined relative/resonance deformation; domain and spectral type stated. | Eigenvalue-dependent operator, arbitrary logarithm of phases, or complex resonances renamed as a self-adjoint spectrum. |
| W -- Weyl clock | Do both growing Riemann--von Mangoldt terms arise analytically? | A classical phase-volume identity plus a quantum remainder $o(E)$. | The clock is obtained only by fitting zeros, hand-picking block dimensions, or matching only the leading $E\log E$ scale. |
| S -- active structure | Does the proposed dynamics change the operator rather than its notation? | A non-removable geometric identity plus converged classical or spectral diagnostics against integrable and equimeasurable controls. | The deformation is unitarily or canonically inert at the claimed level, or its signal converges to the control. |
| P -- primes | Are prime powers endogenous? | A trace/roof/cocycle/transfer mechanism producing $r\log p$ and von-Mangoldt-type weights without a prime table. | Prime lengths or weights are entered term by term, selected retrospectively, or inferred only from an RMT fit. |
| Z -- zero fluctuations | Can a signed oscillatory spectral object carry the explicit formula? | A trace or spectral-shift distribution with the right time support and a frozen held-out test authorized only after P. | Comparing individual ordinates before P, optimizing on the same zeros used for evaluation, or treating a smooth mean count as a zero prediction. |

No total score can compensate for a zero at a necessary gate.  In particular,
Q+W is a partial testbed, not evidence for P or Z.

Two side diagnostics are recorded without being promoted to gates:

- **R (random-matrix/symmetry diagnostic):** descriptive finite-window
  spectral statistics and response to controlled symmetry breaking;
- **C (relative-container admissibility):** existence and summability of
  signed relative spectral objects.

R and C may guide search, but neither is evidence that P or Z has passed.

## 4. Cheap-to-expensive promotion ladder

Each candidate is assigned one of five states.

1. **Generated.**  One-page card containing the mathematical object, hoped-for
   mechanism, closest prior work, and a precommitted death condition.
2. **Screened.**  Algebraic consistency, units, properness/confinement,
   symmetry, and leading phase volume have been checked.  No zero data may be
   loaded.
3. **Replicated signal.**  A frozen small pilot survives at least one
   independent implementation, a negative control, and a discretization or
   time-step refinement.
4. **Analytic survivor.**  At least Q or W is proved, and the remaining bridge
   is stated as a theorem-sized problem rather than a slogan.
5. **Paper candidate.**  One dominant theorem-level claim and at most one
   supporting numerical claim form a coherent paper.  All failed variants are
   retained in the death log.

The default compute allocation is funnel-shaped: many candidates receive
minutes, a few receive hours, and only an analytic survivor receives a large
spectral computation.  More compute is not a substitute for crossing a gate.

## 5. Independence and hindsight controls

- Future candidate generation and Q/W screening should be zero-input and,
  when historically possible, prospectively blinded.
- No prime list is used before a structural P mechanism has been written down.
- Historically motivated parameters, such as (a=1.02), are frozen and
  declared as prior choices.  This value comes from an RH-motivated,
  zero-exposed research lineage, so it is not described as statistically
  blinded or as number-theoretically selected by the current theorem.
- Discovery runs and confirmatory runs have separate identifiers and files.
- Every numerical proposition carries solver, mesh/time-step, energy-window,
  seed, and stopping information.
- A failed refinement remains visible.  It may narrow a claim, but it cannot
  be silently replaced by a successful post-hoc window.
- Distributional similarity to GOE/GUE is a symmetry diagnostic, not an
  arithmetic mechanism and not evidence for RH.

## 6. Candidate card and death-log schema

Every new object should be entered with the following fields:

```text
candidate_id:
mechanism_class:
fixed_mathematical_object:
route: A | B | A/B
hoped_for_bridge:
closest_primary_prior:
Q/W/S/R/C/P/Z status:
cheapest_fatal_test:
precommitted_death_condition:
zero_or_prime_data_access: none | justified-after-P
current_state: generated | screened | replicated | analytic | paper | dead
decision_date:
decision_evidence:
reusable_negative_result:
```

A dead candidate is never deleted.  Its obstruction is indexed so that later
AI search does not repeatedly rediscover the same failure in renamed form.

## 7. Retrospective Paper 7 scope classification

The Hénon-warped exponential magnetic Schrödinger family is retrospectively
classified as a **paper candidate** for a deliberately partial claim.  This
classification organizes current evidence; it is not a claim that the full
promotion ladder was preregistered before the family was explored.

- Q: proved;
- W: proved through both growing terms for fixed Hénon iterate and fixed
  magnetic field;
- S: supported by frozen, independently replicated classical diagnostics;
- R: finite-window adjacent-ratio and magnetic-response diagnostics;
- C: relative spectral objects are admissible at the individual-summability
  level, with no cancellation or arithmetic implication;
- P: open;
- Z: not tested and not authorized before P.

Paper 7 therefore reports a clock-preserving quantum-chaos testbed.  It does
not close the Hilbert--Pólya programme.  The next paper-level promotion should
come either from an endogenous prime-power trace bridge or from a genuinely
new Route B object that passes more gates, not from a better fit to a finite
list of zeros.

## 8. Search cadence after Paper 7

Maintain three parallel queues:

1. **Broad queue:** several mechanism classes at the Generated/Screened states
   (spectral shift, arithmetic roof, finite-field/adelic coupling, quantum
   graph, growing-shell warp, and new AI-generated objects).
2. **Proof queue:** at most two Route A bridges at a time, currently the
   spectral-shift trace-class problem and an endogenous prime-power carrier.
3. **Replication queue:** at most one expensive numerical candidate at a time,
   with a frozen protocol and an independent checker.

This separation protects the programme from both failure modes: wandering
indefinitely among attractive candidates, and proving hundreds of local facts
about an object that never had a plausible path to arithmetic fluctuations.
