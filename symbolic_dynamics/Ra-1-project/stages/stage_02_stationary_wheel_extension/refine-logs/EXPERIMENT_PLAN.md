# Experiment Plan

**Problem**: Determine whether any precisely defined stationary symbolic
recoding of the endogenous wheel-sieve path system can retain its exact
arithmetic clock and support compatible primitive periodic words.

**Method thesis**: Theorem gates should eliminate impossible extensions and
bisimulation quotients before code is written.  A finite audit becomes
informative only after one infinite observational recoding, its decoders, and
its path-lifting semantics have been source-locked.

**Date**: 2026-08-12

## Claim map

| Claim | Minimum convincing evidence | Blocks |
|---|---|---|
| C1: strict extensions cannot create periodic points | Periodic-point projection theorem and empty inverse-limit proof | B0 |
| C2: finite strong-bisimulation quotients cannot create cycles; state-class exact-\(q\) and finite local decoders also obstruct stationarization | Complete scoped proofs with counter-boundaries | B1 |
| C3: a new observational recoding warrants an infinite theorem attempt only if one frozen rule has exact arithmetic/clock decoding and compatible periodic witnesses at every cutoff | Complete source lock, exact \(K=5,6,7\) and \(N\le12\) ledgers, all controls, no decoder/path violations | B2–B6 |

Anti-claim: a graph cycle created by merging incompatible representatives is
not an intrinsic periodic orbit and must not receive A1 credit.

## Research storyline

- B0 and B1 are the principal theorem-screening results.
- B2 is now the blocking task.  It defines the infinite object before any
  finite approximation.
- B3 verifies implementation against the theorem baselines and a positive
  cyclic toy.
- B4 and B5 test one frozen recoding and all controls; they do not search over
  recodings, radii, cutoffs, or seeds.
- B6 applies the mechanical outcome hierarchy.  A finite positive signature
  authorizes only an infinite source-lock theorem attempt.
- Determinant and Riemann-zero comparisons are outside the run plan.  Route B
  stays locked.

## Data and evaluation protocol

- Source data: canonical wheel levels generated from the fixed recursion;
  no prime table is read.
- Main cutoffs: \(K=5,6,7\), all reported.
- Period cutoff: \(N=12\), with every period \(1\le n\le N\) reported.
- Arithmetic: exact integers and symbolic labels; logarithms are display-only.
- Seeds: `20260812`–`20260816` for the full random-control ledger.
- Selection: no best cutoff, seed, observation radius, or rule selection.
- Repetitions: deterministic exact computation; random controls use every
  frozen seed once because the seed ledger, not a sampling mean, is the object.
- External data: none.

## Experiment blocks

### B0 — Strict-extension theorem

- Claim tested: C1.
- Task: prove that periodic points project through a semiconjugate extension
  and that the standard inverse-limit natural extension is empty.
- Metric: all proof obligations discharged.
- Success criterion: no hidden reset or predecessor assumption.
- Failure interpretation: repair the phase-space definition.
- Artifact: `G0_STRICT_EXTENSION_OBSTRUCTION.md`.
- Priority/status: **MUST — complete analytically**.

### B1 — Bisimulation and clock theorem gate

- Claim tested: C2.
- Task: prove finite-DAG quotient acyclicity, the level-injective label lemma,
  and the finite-local-decoder obstruction.
- Metric: theorem statements match assumptions; finite/infinite boundary and
  non-bisimulation escape class stated.
- Success criterion: all three scoped proofs close without empirical input.
- Failure interpretation: weaken the claim before defining an experiment.
- Artifact: `G0B_BISIMULATION_AND_CLOCK_OBSTRUCTIONS.md`.
- Priority/status: **MUST — complete analytically**.

### B2 — Infinite observational-recoding source lock

- Claim supported: prerequisite for C3.
- Task: complete every field in
  `OBSERVATIONAL_RECODING_SOURCE_LOCK.md` for one object.
- Required comparison: explicitly distinguish the proposed category from a
  strict extension and from strong bisimulation.
- Metrics: undefined-field count, canonical rule hash, declared coding
  radius/memory class, decoder totality, cutoff-consistency obligations.
- Success criterion: zero undefined required fields and one checkable infinite
  rule independent of \(K\).
- Failure interpretation: `NOT_TESTABLE`; no implementation run.
- Priority/status: **MUST — current blocker**.

### B3 — Exact implementation regression

- Claim supported: infrastructure for C3.
- Task: implement partition/recoding, SCC, fixed-point, Möbius inversion, and
  path-compatibility checks.
- Systems: a hand-checkable finite DAG, its strong-bisimulation quotient, and
  a stationary cyclic toy with known fixed-point counts.
- Metrics: exact partition equality, SCC equality, \(\#\operatorname{Fix}(S^n)\)
  for \(n\le12\), primitive counts, and decoder/path-violation count.
- Success criterion: the DAG quotient remains acyclic and the cyclic toy has
  the preregistered positive ledger.
- Failure interpretation: implementation invalid; stop before wheel runs.
- Outputs: tests and a machine-readable sanity certificate.
- Priority/status: **MUST after B2**.

### B4 — Main finite-cutoff observational recoding

- Claim tested: C3, finite evidence only.
- Systems: the one B2-frozen rule on canonical \(K=5,6,7\) wheel graphs.
- Metrics: target state/edge counts, SCCs, class merges, decoder violations,
  representative-compatibility violations, fixed-point counts for every
  \(n\le12\), primitive counts, decoded clocks, shortest witnesses, and the
  rule hash.
- Success criterion: the identical rule has zero violations and at least one
  compatible nonzero primitive count at every cutoff under the frozen
  consistency convention.
- Failure interpretation: `STOP_SCOPED` for this recoding, not a universal
  symbolic no-go.
- Priority/status: **MUST after B3**.

### B5 — Arithmetic, clock, and generic-cycle controls

- Claim tested: C3 and the anti-claim.
- Systems: clock-erased, fixed-deletion, cyclic-deletion, all five random
  deletion variants, and the B3 toys.
- Metrics: the same ledger as B4 plus exact unit-set recovery and the first
  lost label/decoder condition.  Partition coarsening and cycle counts are
  reported even when zero.
- Interpretation: clock erasure may create additional merges or cycles, but
  its loss of clock credit is recorded separately.  A control cycle alone is
  neither success nor failure; the joint signature decides.
- Success criterion: complete control matrix with no best-variant selection.
- Failure interpretation: incomplete controls make the run `NOT_TESTABLE`.
- Priority/status: **MUST after B4**.

### B6 — Consistency and outcome audit

- Claim tested: C3.
- Task: verify artifacts/hashes, apply the priority-ordered mechanical rule,
  and separate finite observations from infinite conclusions.
- Metrics: missing artifact count, hash mismatch count, rule changes, cutoff
  consistency, and exactly one final outcome.
- Success criterion: `INVALID / NOT_TESTABLE`, `THEOREM_STOP`,
  `STOP_SCOPED`, or `FINITE_ESCALATE` follows mechanically.
- Failure interpretation: retain `NOT_TESTABLE`; do not enlarge a cutoff or
  change a rule.
- Priority/status: **MUST after B5**.

## Milestones and resource estimate

| Milestone | Goal | Blocks | Gate | Estimate | Main risk |
|---|---|---|---|---|---|
| M0 | Close impossible categories | B0–B1 | proofs verified | complete; proof only | overextending finite theorem to infinite graphs |
| M1 | Define one infinite object | B2 | zero undefined fields | theory work; no compute estimate | hiding level/prime table in recoding |
| M2 | Validate exact code | B3 | all sanity tests pass | <10 CPU min | cycle detector or Möbius bug |
| M3 | Run main cutoffs | B4 | unchanged rule hash | expected <1 CPU-hour, <4 GB RAM | state explosion or terminal artifact |
| M4 | Run full controls | B5 | every cutoff/seed present | expected <2 CPU-hours | unmatched controls |
| M5 | Freeze scoped verdict | B6 | one mechanical outcome | <15 CPU min | finite-to-infinite overclaim |

Compute figures are estimates, not measured results.  No GPU, external
dataset, human evaluation, prime table, or zero table is required.

## First three actions

1. `S2-D001`: complete and audit the infinite observational-recoding source
   lock.  This is the immediate next step.
2. `S2-R001`: only after D001 passes, run exact DAG and cyclic-toy regression.
3. `S2-R002`: run the unchanged main recoding at \(K=5\), then extend to
   \(K=6,7\) without editing the rule.

There is no authorized determinant run and no `SD-C07` record.

## Final checklist

- [x] Three dominant claims are stated.
- [x] Strict extension, strong bisimulation, and observational recoding are
  separated.
- [x] Finite and infinite conclusions are separated.
- [x] Metrics, cutoffs, controls, and failure interpretations are specified.
- [x] Route B and cross-family expansion remain locked.
- [ ] One infinite recoding source lock is complete.
- [ ] Implementation exists and sanity tests pass.
- [ ] Main and control ledgers are complete.
- [ ] A mechanical Stage-02 outcome is frozen.
