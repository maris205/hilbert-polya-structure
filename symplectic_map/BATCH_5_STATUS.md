# Five-Paper Autonomous Batch

## Material Passport

- Batch start: 2026-08-13
- Scope authority: the user's standing instruction to complete five consecutive
  papers under the current Session's existing research, validation, directory,
  roadmap, GitHub-sync, and stopping rules
- Checkpoint policy: non-blocking stage confirmations are pre-authorized by the
  standing instruction; pause only for an unresolved integrity failure, a hard
  external blocker, or a major breakthrough
- Cross-model upload: disabled; independent reviews use local Codex subagents
- External prime/zero data: forbidden until a candidate passes its frozen A0/A1
  gates
- Batch status: `COMPLETE_SYNCED`

## Paper Queue

| Batch paper | Project directory | Current stage | Status | Route outcome |
|---:|---|---|---|---|
| 1 | `papers/2-branch-baker` | final PDF, two revision rounds, independent review, final integrity | COMPLETE_LOCAL | `ROUTE_A_REJECTED`; structural finite-clock no-go |
| 2 | `papers/3-prime-multiplier-obstruction` | final 11-page PDF, exact package, two independent review rounds, final integrity | COMPLETE_LOCAL | all-period raw rational-prime multiplier obstruction; exponent-prime base-2 boundary open |
| 3 | `papers/4-integral-henon-multipliers` | final 11-page PDF, two independent manuscript reviews, final integrity | COMPLETE_LOCAL | all-period algebraic-unit / finite-bad-prime obstruction; `A0_FAIL` for exact rational-prime multiplier modulus |
| 4 | `papers/5-algebraic-action-clocks` | final 13-page PDF, two independent manuscript reviews, final integrity | COMPLETE_LOCAL | all-period obstruction for algebraically normalized periodic actions as exact prime-log clocks |
| 5 | `papers/6-arithmetic-clock-escape-trichotomy` | final 12-page PDF, two independent manuscript reviews, final integrity | COMPLETE_LOCAL | `CAPACITY_BOUND_CERTIFIED` for additive finite-rank, fixed-support, algebraic-action readouts |

## Per-Paper Completion Definition

A paper counts as complete only when all applicable items pass:

1. novelty and prior-art boundary recorded;
2. candidate/source lock and forbidden-data policy recorded;
3. implementation and exact/numerical controls verified;
4. validation and sealed test executed only after their gates unlock;
5. result and Route-A decision recorded with explicit stopping rules;
6. LaTeX source, reproducible vector figures, verified bibliography, and PDF
   produced;
7. pre-review integrity, independent full review, revision, re-review, and
   final integrity complete;
8. artifact hashes and reproducibility instructions complete;
9. project synchronized to the configured GitHub repository using the existing
   nested-repository exclusion rules.

## Standing Scientific Rules

- Arithmetic relevance is an entry gate, not a conclusion inferred from chaos,
  GUE-like plots, orbit counts, or generic zeta functions.
- Parameters, clocks, signs, normalizations, cutoffs, and splits are frozen
  before validation.
- Prime/zero tables are not used for candidate selection or tuning.
- Signed or complex cancellations are never replaced by absolute values after
  inspection.
- A failed A0 stops A2--A4 and Route B for that candidate.
- Known constructions are controls or reproduction baselines, not novelty
  claims.
- Null and obstruction results are publishable only with precise scope and
  independent verification.

## Batch Log

- 2026-08-13: batch opened.  `pcf_markov_baker_v1` research package already
  verified; manuscript production begins as batch Paper 1.
- 2026-08-13: Paper 1 round-2 repair supplied the missing generating-partition
  proof using nested cylinders, negative Schwarzian dynamics, the
  no-wandering-interval theorem, and the homterval lemma; 89 tests and a clean
  17-page build pass.  Final independent review remains open.
- 2026-08-13: Paper 2 exact controls and the frozen periods 1--4 audit passed.
  The all-period raw-prime theorem is proved; the only explicitly retained
  exponent-prime boundary is base 2 at periods at least two.
- 2026-08-13: Paper 3 selected the global area-preserving polynomial Hénon
  lift.  During source-lock audit, algebraic-unit monodromy strengthened the
  intended rational-eigenvalue obstruction to an exact rational-modulus
  obstruction; the strengthened claim is being independently checked before
  execution.
- 2026-08-13: Paper 1 closed locally.  Final independent review returned
  `PASS_WITH_MINORS` (7.5/10); both suggested exposition pinpoints were
  applied, the 17-page final PDF rebuilt cleanly, 89 tests passed, and all 25
  frozen research checksums remained valid.  GitHub synchronization is batched
  to the five-paper close so the nested-repository exclusion is applied once.
- 2026-08-14: Paper 2 reached a clean 11-page pre-review build with complete
  claim, experiment, figure, citation, and forbidden-data traceability; its
  first independent manuscript review is in progress.
- 2026-08-14: Paper 3 deployment remains fail-closed.  A second independent
  code review confirmed the exact-modulus square test and controls but rejected
  execution because the report-manifest closure, proof-text audit, and
  alias/tolerance leakage scanner still required repair.  No candidate run has
  occurred.
- 2026-08-14: Paper 4 source-lock v2 froze the algebraically normalized action
  obstruction and explicit gauge/monodromy/complex-observable/denominator-3
  stops; independent counterexample review continues with zero candidate
  action evaluations.
- 2026-08-14: Paper 5 selected a scoped escape-trichotomy synthesis: finite
  rational rank, finite bad-prime support, and algebraic action each exclude a
  complete exact prime clock, so any future candidate must justify an
  infinite, non-good-reduction, or genuinely logarithmic/transcendental
  mechanism.  This remains a draft pending independent novelty and proof audit.
- 2026-08-14: Paper 2 closed locally after independent Round 2 `PASS`
  (8.8/10).  The revision added the exact PCF critical orbit and explicitly
  separated it from the multiplier proof, restored a 45/45 research-manifest
  hash closure, retained the complex-modulus and base-2 open boundaries, and
  produced a clean 11-page final PDF.  Thirty-seven tests pass.
- 2026-08-14: Paper 3 passed four fail-closed pre-execution code-review
  rounds, then executed the frozen controls before the exact candidate.  All
  15 registered checks and 39 tests passed.  The all-period proof restricts
  exact rational multiplier moduli to one; the period-1--3 ledger (five
  cycles) is an implementation audit only.  Geometry passes, but the proposed
  exact prime-modulus clock is `A0_FAIL`; manuscript production has started.
- 2026-08-14: Paper 4 Round 2 retained the execution lock after finding two
  remaining fail-open paths: the structured proof contract did not yet bind
  equation semantics, and the result manifest accepted extra/nested duplicate
  artifacts.  Both are being repaired; no formal action audit has run.
- 2026-08-14: Paper 5 independent proof/novelty review upgraded the correct
  but weak selector union to an additive theorem.  For certificates
  `log p = v + log q + alpha`, Hermite--Lindemann and outside-prime valuations
  force the selected `v` terms to be rationally independent, yielding the
  quantitative bound `#hits <= dim_Q(V) + #S_Q`.  The source lock is now v2;
  the claim remains a scoped capacity certificate, not a universal no-go.
- 2026-08-14: Paper 3 closed locally after Round 1 `PASS_WITH_MINORS` and
  Round 2 `PASS -- MAY FINALIZE`.  Its 11-page final PDF is byte-identical to
  the reviewed revision; 39 tests, 41 official result artifacts, 23 figure
  package entries, and 12 citations pass final integrity.  Git synchronization
  remains deferred to the five-paper batch close.
- 2026-08-14: Paper 4 closed locally after Round 1 `MINOR_REVISION` and
  Round 2 `PASS`.  The corrected 13-page final PDF has a fully provenance-
  classified 27-cell scope figure; 82 tests, 35 official result hashes, 27
  figure-package hashes, and 13 citations pass final integrity.  The theorem
  closes only algebraically normalized action readouts, with the documented
  `MERGE_IF_STANDALONE_DEPTH_IS_REQUIRED` publication boundary.
- 2026-08-14: Paper 5 passed its final tree-bound deployment review after
  binding the actual terminal packages of Papers 3 and 4.  Its single
  registered static run passed all nine gates and 51 tests, certifying the
  additive rank-plus-support capacity theorem with zero numerical runs,
  target matches, prime tables, prime arrays, numerical logarithms, or zero
  data.  Manuscript production has started under the deliberately scoped
  `CAPACITY_BOUND_CERTIFIED` label.
- 2026-08-14: Paper 5 closed locally after Round 1 `PASS_WITH_MINORS` and
  Round 2 `PASS / MAY FINALIZE`.  Its 12-page final PDF is byte-identical to
  the approved revision; 51 tests, all nine registered gates, nine figure
  outputs, 18 citations, and the upstream terminal bindings pass final
  integrity.  All five batch papers are now locally complete; only the
  batch-level integrity audit and configured GitHub synchronization remain.
- 2026-08-14: Independent batch audit returned `PASS` with zero remaining
  local-completion blocker after reconciling one Paper-1 claim-manifest
  cross-reference.  The five safe suites pass 89, 37, 39, 82, and 51 tests.
  The full batch was synchronized to `main` in commit `41b8701`; no nested
  `.git` directory or gitlink was included.
