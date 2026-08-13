# Independent pre-deployment code review

Date: 2026-08-13

Scope reviewed:

- `experiments/source_lock.json`
- `experiments/EXPERIMENT_PLAN.md`
- `notes/PROOF_PACKAGE.md`
- all files under `code/henon_audit/`
- all files under `code/tests/`
- `code/scripts/build_result_manifest.py`

Review mode:

- No formal candidate run was executed.
- `results/target_isolation_audit.json` was not present in the tree at review time, so I reviewed the code path that generates it (`code/henon_audit/cli.py` + `code/henon_audit/protocol.py`) instead of a committed artifact.
- I did one narrow non-candidate symbolic reproducer on the planted-control trace `T=5/2` to confirm the generic hyperbolic modulus-classification path.

Bottom line:

- Low-period recurrence, monodromy order, and trace/resultant wiring look internally consistent.
- The code is not deployment-ready yet because the exact rational-modulus gate is incomplete for hyperbolic cycles, the integral negative control does not actually gate that path, and the new final manifest script is guaranteed to fail on the current repository state.

What looks sound

- `code/henon_audit/dynamics.py:30-36` implements the monodromy in the documented order `A(x[n-1])...A(x[0])`.
- `code/henon_audit/periods.py` uses explicit lower-period branch removal for `n=2,3`, checks determinant-one before interpretation, and includes independent resultant/remainder checks against the hard-coded trace formulas.
- Controls are ordered before candidate execution in `code/henon_audit/cli.py:73-141`, so the candidate gate ordering itself is correct.

## CRITICAL

### 1. The generic hyperbolic exact-rational-modulus classifier never performs the required square test, so `R031-R033-modulus` can miss a non-unit rational modulus

Files:

- `code/henon_audit/modulus.py:137-177`
- `code/henon_audit/modulus.py:208-297`
- `code/henon_audit/cli.py:184-186`

Problem:

- `_exact_hyperbolic_record()` detects only whether `mu=|lambda|^2` has a degree-1 minimal polynomial (`exact_rational_mu`), but it never performs the next required step from the source lock: decide whether the positive square root of that rational `mu` is itself rational.
- It also returns `rational_modulus_values: []` unconditionally.
- `candidate_modulus_audit()` builds `exact_rational_modulus_set` only by unioning those `rational_modulus_values`, so every hyperbolic cycle is effectively invisible to the exact-rational-modulus gate unless some other branch hard-codes a value.
- `cli.run()` then treats `modulus["exact_rational_modulus_set"] == ["1"]` as the candidate gate. Because the hyperbolic path never emits rational `q`, this gate can false-pass.

Concrete reproducer:

- For the planted fixed-point control trace `T=5/2`, the exact relation gives `mu` roots `1/4` and `4`, hence exact rational moduli `1/2` and `2`.
- The current generic path returns two degree-1 `mu` factors (`M-1/4`, `M-4`) but still returns `rational_modulus_values = []`.
- This is a direct violation of `source_lock.json`’s `rational_modulus_rule` and B3 step 8 in `EXPERIMENT_PLAN.md`.

Why this matters:

- This is not just a reporting nicety. It means the finite exact audit can fail to detect exactly the kind of rational modulus it claims to certify.

Precise fix:

1. In `_exact_hyperbolic_record()`, when `factor.degree() == 1`, extract the exact rational `mu`.
2. Require `mu > 0`.
3. Reduce `mu = a/b` with coprime positive integers and test whether both `a` and `b` are perfect squares.
4. If yes, emit:
   - `exact_rational_mu: True`
   - `exact_positive_rational_modulus: "<q>"`
   - `rational_modulus_classification: "RATIONAL_MODULUS_UNIT"` or `"RATIONAL_MODULUS_S_UNIT"` as appropriate for the caller
   - append `q` to `rational_modulus_values`
5. If `mu` is rational but not a rational square, emit an explicit classification like `RATIONAL_MU_BUT_IRRATIONAL_MODULUS`.
6. In `candidate_modulus_audit()`, compute `raw_rational_prime_modulus_count` from the emitted exact rational moduli rather than hard-coding `0`.
7. In `cli.run()`, fail not only on the final set mismatch, but also if any hyperbolic record remains in an unresolved `REQUIRES_SQUARE_TEST` state.

### 2. The integral negative control does not actually test the modulus-classification pipeline it is supposed to gate

Files:

- `code/henon_audit/controls.py:79-122`

Problem:

- `integral_negative_control()` constructs `modulus_records`, but `pass` ignores them completely.
- `exact_rational_modulus_values` is hard-coded to `["1"]` instead of being derived from `trace_zero`, `trace_four`, `trace_fourteen`, and the period-3 complex-trace record.
- As written, the control passes if and only if the rational-multiplier check finds no `±1` roots in the period records. A broken modulus classifier still passes.

Why this matters:

- B2b in the plan says the integral negative control must run the same exact-modulus pipeline and require every exact rational modulus to be `1`.
- Right now, B2b is not a real gate on that logic, so the candidate can proceed with a broken rational-modulus classifier.

Precise fix:

1. Derive `exact_rational_modulus_values` from `modulus_records` rather than hard-coding it.
2. Make `pass` require:
   - the derived modulus set equals `["1"]`
   - no record is left in an unresolved classification state
   - the period-3 complex trace is explicitly classified as irrational-modulus / outside-support
3. Add one planted hyperbolic control through the generic modulus path, not the direct fixed-point shortcut, so the square-test logic is exercised before candidate execution.

### 3. `build_result_manifest.py` is a deployment blocker in the current tree because it requires artifacts that are not produced anywhere

Files:

- `code/scripts/build_result_manifest.py:20-49`

Problem:

- The script hard-requires:
  - `experiments/EXPERIMENT_TRACKER.md`
  - `results/EXPERIMENT_RESULTS.md`
  - `results/VALIDATION_REPORT.md`
- None of these files exist in the reviewed tree, and no code in this paper package generates them.
- As a result, the script is guaranteed to raise `FileNotFoundError` on a normal post-run invocation.

Why this matters:

- This is a direct deployment blocker for the newly added manifest stage.

Precise fix:

Choose one of these, then make the workflow consistent:

1. Add generators/templates for those artifacts and document when they are produced, or
2. Remove them from the required manifest set, or
3. Make them optional with explicit `present: false` manifest entries.

Also recommended:

- include `code/scripts/run_exact_audit.py` and `code/scripts/build_result_manifest.py` themselves in the hashed artifact set, because they are executable provenance inputs.

## MAJOR

### 4. The target-isolation scan is too weak for the frozen forbidden-data contract

Files:

- `code/henon_audit/protocol.py:58-120`

Problem:

- `static_target_isolation_scan()` only checks a short deny-list of import roots and function names.
- It does not inspect:
  - string literals / path literals
  - `open`, `Path.read_text`, `Path.open`, `json.load`, `pickle`, or other file reads
  - `subprocess`, `os.system`, or shell-outs
  - URLs, sockets via alternate libraries, or dynamic imports
  - embedded target arrays / prime labels / zero filenames
  - tolerance-based exactness promotion logic
- This is materially weaker than B0 in the experiment plan, which explicitly asks for forbidden prime/zero paths, target arrays, nearest-prime routines, and near-rational promotion checks.

Why this matters:

- `R001` can return PASS while code still violates the source-locked isolation rules.

Precise fix:

1. Extend the AST pass to flag:
   - filesystem reads
   - subprocess/shell execution
   - dynamic imports
   - suspicious string constants matching `prime`, `riemann`, `zero`, `target`, `nearest`, `tolerance`, `epsilon`
2. Scan `*.py` and executable shell scripts under `code/scripts/`.
3. Add seeded negative tests that create tiny fixture modules with forbidden imports, forbidden file paths, and near-rational promotion code, then assert the scanner reports them.

## MINOR

### 5. The tests miss the regressions that matter most for the new modulus and manifest logic

Files:

- `code/tests/test_modulus.py`
- `code/tests/test_controls.py`
- `code/tests/test_protocol_preflight_scope.py`

Gaps:

- No test exercises the generic hyperbolic path on a case with rational `mu=q^2`, such as trace `5/2`.
- No test verifies that `integral_negative_control()["pass"]` depends on the derived modulus classifications.
- No test covers `build_result_manifest.py` at all.
- No test seeds a deliberately bad file and checks that `static_target_isolation_scan()` catches it.

Precise fix:

- Add a modulus regression test with trace `5/2` expecting exact moduli `["1/2", "2"]`.
- Add a control test that asserts the integral negative control derives its modulus set from `modulus_records`.
- Add a manifest integration test in a temp directory with a minimal successful artifact set.
- Add negative scanner tests with forbidden fixtures.

### 6. `proof_dependency_audit()` is a wording check, not an actual mathematical audit

Files:

- `code/henon_audit/preflight.py:19-52`

Problem:

- The function checks whether certain phrases appear in `PROOF_PACKAGE.md`.
- This is acceptable as a documentation-presence check, but it is not an independent theorem audit and can false-pass if the phrases remain while the proof logic drifts.

Recommendation:

- Rename the output role in logs/docs to something like `proof_text_dependency_check`, or
- clearly document that the mathematical audit is external/manual and this code only verifies that required proof ingredients are present in the frozen write-up.

## Recommendation before deployment

Do not deploy yet.

Minimum unblock sequence:

1. Fix the hyperbolic rational-modulus square-test path.
2. Make the integral negative control actually gate the modulus records.
3. Repair `build_result_manifest.py` so it matches the artifact set the package really produces.
4. Strengthen scanner/tests around forbidden-data isolation.

After those are fixed, rerun a fresh static review and then the controls-only path before any full exact audit.

---

# Round 2 independent static code review

Date: 2026-08-13

Scope reviewed:

- `experiments/source_lock.json`
- `experiments/EXPERIMENT_PLAN.md`
- this Round 1 `results/CODE_REVIEW.md`
- current files under `code/henon_audit/`
- current files under `code/tests/`
- `code/scripts/build_result_manifest.py`
- `code/README.md`
- `experiments/EXPERIMENT_TRACKER.md`
- `results/EXPERIMENT_RESULTS.md`
- `results/VALIDATION_REPORT.md`

Review mode:

- No `candidate` / full candidate execution was run.
- No prime-table, Riemann-zero, or sealed prior-candidate data was accessed.
- I only ran safe non-candidate checks:
  - `PYTHONPATH=code pytest -q code/tests/test_modulus.py -k 'generic_hyperbolic_pipeline_performs_exact_rational_square_test'`
  - `PYTHONPATH=code pytest -q code/tests/test_controls.py code/tests/test_protocol_preflight_scope.py`
  - a temporary-module repro against `static_target_isolation_scan()` using an aliased suspicious path and a hand-written tolerance promotion guard

Bottom line:

- `DEPLOYMENT_FAIL`
- Round 1 blocker (1) is fixed.
- Round 1 blocker (2) is fixed.
- Round 1 blocker (3) is only partially fixed: the files now exist, but the tracker/results/validation loop is still not fail-closed.
- There are also two remaining deployment blockers outside the original three: `R010` currently fails in-tree, and `R001` still false-passes alias/tolerance escapes.

## PASS: 1. Hyperbolic modulus classification now enforces `mu=q^2` with `q in Q_{>0}`

Evidence:

- `code/henon_audit/modulus.py:137-147` adds `exact_positive_rational_square_root()`.
- `code/henon_audit/modulus.py:169-229` now:
  - extracts exact rational `mu` only from degree-1 factors,
  - performs the exact rational-square test,
  - emits `exact_positive_rational_modulus`,
  - classifies `RATIONAL_MU_BUT_IRRATIONAL_MODULUS` when `mu` is rational but not a rational square,
  - populates `rational_modulus_values`.
- `code/henon_audit/modulus.py:317-341` derives `exact_rational_modulus_set`, unresolved square-test states, and raw rational-prime moduli from the emitted exact `q` values.
- `code/henon_audit/cli.py:187-193` now hard-fails if the candidate modulus set is not `["1"]`, if any unresolved square-test state remains, or if any exact raw rational-prime modulus appears.
- `code/tests/test_modulus.py:40-54` adds the exact planted regression at trace `5/2`, expecting exact moduli `["1/2", "2"]`.

Safe test evidence:

- `PYTHONPATH=code pytest -q code/tests/test_modulus.py -k 'generic_hyperbolic_pipeline_performs_exact_rational_square_test'`
- Result: `1 passed, 14 deselected`

Conclusion:

- The Round 1 blocker about classifying only rational `mu` without checking `mu=q^2` is repaired.

## PASS: 2. The `a=0` integral negative control now truly gates the modulus classifier

Evidence:

- `code/henon_audit/controls.py:91-162` now computes `derived_moduli` from `modulus_records` and makes `pass` require:
  - no exact rational multiplier roots in the frozen periods,
  - `derived_moduli == [1]`,
  - no unresolved modulus classifications,
  - the period-3 nonreal control to remain outside the rational-modulus claim.
- `code/henon_audit/controls.py:208-217` threads that `pass` value into the candidate gate.
- `code/tests/test_controls.py:17-23` now asserts the derived exact rational modulus set is `["1"]` and that the control passes only with the modulus records in that state.

Other related controls remain sound:

- `code/henon_audit/controls.py:29-78` and `code/tests/test_controls.py:9-14` validate the planted `a=-15/16` positive control and require the generic modulus pipeline to recover `["1/2", "2"]`.
- `code/henon_audit/controls.py:165-205` and `code/tests/test_controls.py:26-30` reject the `delta=2` scope example unless bad prime `2` is declared before multiplier interpretation.

Conclusion:

- The Round 1 blocker that the integral negative control did not actually gate the modulus-classification path is repaired.

## FAIL: 3. Manifest / tracker / results / validation is not yet a closed fail-closed loop

What is fixed:

- `code/scripts/build_result_manifest.py:21-43` now requires:
  - `experiments/EXPERIMENT_TRACKER.md`
  - `results/EXPERIMENT_RESULTS.md`
  - `results/VALIDATION_REPORT.md`
- So the exact Round 1 failure mode (“guaranteed `FileNotFoundError` because the files do not exist in-tree”) is repaired.

What is still missing:

- `experiments/EXPERIMENT_TRACKER.md:27-28` says it is updated from `run_summary.json` after the official full run, but no code verifies that update occurred.
- `results/EXPERIMENT_RESULTS.md:3-7` is still a pre-created template marked `PENDING_OFFICIAL_FULL_RUN`.
- `results/VALIDATION_REPORT.md:3-7` is still a pre-created template marked `PENDING_OFFICIAL_FULL_RUN`.
- `code/README.md:34-38` documents a manual workflow order, but `build_result_manifest.py:53-73` only hashes/presence-checks the files; it does not reject untouched placeholders or confirm that tracker/results/validation were regenerated from the completed run outputs.

Conclusion:

- The file-presence gap is fixed, but the provenance/reporting loop is not yet fail-closed. This original blocker is only partially repaired.

## CRITICAL: `R010` currently fails in-tree, so the audited runner cannot reach controls-only or candidate gates

Evidence:

- `code/henon_audit/preflight.py:19-58` still performs exact substring checks over the proof text.
- In particular, `code/henon_audit/preflight.py:30` requires the literal substring `"every positive-dimensional projective subvariety"`.
- In `notes/PROOF_PACKAGE.md`, that wording is present across a line break rather than as one flat substring, so the check returns false.
- `code/tests/test_protocol_preflight_scope.py:60-63` expects `proof_dependency_audit(...)[\"pass\"]` to be true.
- Safe test run:
  - `PYTHONPATH=code pytest -q code/tests/test_controls.py code/tests/test_protocol_preflight_scope.py`
  - Result: `9 passed, 1 failed`
  - Failing test: `test_proof_parameter_and_symplectic_preflights_pass`
- Direct non-candidate probe of `proof_dependency_audit()` showed:
  - `positive_dimension_hyperplane_argument: false`
  - all other checks true
- `code/henon_audit/cli.py:87-91` raises `RuntimeError("R010 proof-dependency audit failed")` if this check is false.

Conclusion:

- This is a fresh deployment blocker. Even a controls-only run would currently stop at `R010`.

## CRITICAL: `R001` is improved but still not fail-closed for alias/path and custom tolerance escapes

What is good:

- `code/henon_audit/protocol.py:67-115` adds a much broader deny-list than Round 1.
- `code/tests/test_protocol_preflight_scope.py:24-40` now includes a seeded negative test for inline forbidden imports, target arrays, path literals, and `nsimplify(...)`.

Why it is still not fail-closed:

- `code/henon_audit/protocol.py:120-125` only lifts literal strings from the currently visited call subtree.
- `code/henon_audit/protocol.py:185-197` flags suspicious assignment names only when the assigned value is a list / tuple / set, not when a suspicious filename is first stored in a string variable.
- Therefore an aliased path such as
  `prime_file = "riemann_zeros.csv"; Path(prime_file).read_text()`
  is reviewed as a file-read site with `literal_fragments: []` and produces no finding.
- The scanner also has no generic catch for hand-written tolerance promotion such as
  `abs(value - 2) < 1e-5`
  unless a banned helper like `nsimplify` / `isclose` / `allclose` is used.

Concrete non-candidate repro:

- I created temporary files containing:
  - `prime_file = "riemann_zeros.csv"; Path(prime_file).read_text()`
  - `is_exact = abs(value - 2) < 1e-5`
- `static_target_isolation_scan()` returned:
  - `findings: []`
  - `pass: true`
  - `reviewed_file_read_sites` containing the aliased `read_text` site with empty `literal_fragments`

Conclusion:

- Relative to Round 1, the scanner is much better, but it still false-passes cases that violate the B0 “forbidden paths / near-rational promotion” contract. This remains a deployment blocker under the source lock.

## Other audited items that still look sound

- Low-period recurrence wiring, monodromy order, and resultant-based trace checks remain internally consistent:
  - `code/henon_audit/dynamics.py:30-36`
  - `code/henon_audit/dynamics.py:44-60`
  - `code/henon_audit/periods.py:36-79`
  - `code/henon_audit/periods.py:105-300`
- Candidate gating still runs in the correct order, with controls before candidate periods:
  - `code/henon_audit/cli.py:73-100`
  - `code/henon_audit/cli.py:167-193`
- The theorem/check-role wording issue from Round 1 minor item 6 is partially improved:
  - `code/henon_audit/preflight.py:20-24` now explicitly says this is a text/provenance check rather than an independent mathematical audit.
  - But because the implementation is still exact-substring-based, the gate is currently brittle enough to fail on line wrapping.

## Final decision

- `DEPLOYMENT_FAIL`

Minimum unblock sequence before any deployment or controls-only execution:

1. Repair `proof_dependency_audit()` so `R010` is whitespace/line-wrap robust and the safe test suite passes.
2. Make the tracker/results/validation loop fail-closed, not just presence-closed:
   - reject untouched `PENDING_OFFICIAL_FULL_RUN` placeholders, or
   - generate / rewrite these artifacts from run outputs, or
   - validate explicit content linkage against `run_summary.json`.
3. Strengthen `static_target_isolation_scan()` to catch aliased suspicious file paths and custom tolerance-promotion logic, then add negative tests for both escapes.
4. After those are fixed, rerun a fresh static review and then a controls-only execution before any full exact audit.

---

# Round 2 remediation record (implementation author; pending third-party review)

Date: 2026-08-14

This section records fixes made after the Round 2 `DEPLOYMENT_FAIL`.  It is
not an independent review and does not change the deployment verdict by
itself.  No controls-only command and no formal candidate run was executed
during this remediation.

## R010 proof-text gate repair

- `code/henon_audit/preflight.py` now collapses all whitespace before phrase
  checks, so Markdown line wrapping cannot invalidate a dependency.
- It also extracts and requires structured section identifiers for Theorem A,
  Corollary B, Theorem C, Proof Strategy, Dependency Map, Proof, and Steps
  1--7.  The output continues to identify this as a
  `proof_text_dependency_check`; the independent mathematical audit remains
  the v2 source-lock provenance.

## Official-report linkage made fail-closed

- `code/henon_audit/manifest.py` now parses `run_summary.json` and
  `candidate_multiplier_audit.json`, requires a passed `full_exact_audit`
  with `candidate_executed=true` and zero must-run failures, and checks the
  candidate identifier and candidate audit status.
- It rejects `PENDING_OFFICIAL_FULL_RUN` in the tracker, experiment results,
  or validation report.
- All three narratives must carry exact SHA-256 links to the same run summary
  and candidate audit.  The tracker must contain every run ID from the JSON
  registry with status `PASS`; the experiment report must state candidate
  execution and zero failures; the validation report must state pytest PASS
  and hash the exact JUnit XML.
- `build_result_manifest.py` invokes this validation before emitting the final
  manifest and embeds the linkage certificate.  A temporary-directory test
  exercises both a valid linked report set and rejection of a restored
  placeholder.

## R001 alias and tolerance escape repair

- The AST scanner now propagates simple string and `Path(...)` aliases into
  `open` / `read_*` sites and flags suspicious assigned target paths even
  before the read.
- It now rejects custom positive floating-tolerance promotions of the form
  `abs(expression) < tolerance`, including a tolerance stored in a simple
  numeric alias.
- The exact Round 2 reproducer
  `prime_file='riemann_zeros.csv'; Path(prime_file).read_text()` plus
  `abs(value-2)<1e-5` is now a regression test requiring
  `suspicious_target_path_alias`, `forbidden_target_path_literal`, and
  `tolerance_exactness_promotion` findings.

## Safe non-candidate regression result

The complete non-candidate selection was run after these changes:

```text
PYTHONPATH=code pytest -q \
  code/tests/test_algebra.py \
  code/tests/test_dynamics.py \
  code/tests/test_controls.py \
  code/tests/test_protocol_preflight_scope.py \
  code/tests/test_modulus.py::test_real_hyperbolic_modulus_relation_is_reciprocal \
  code/tests/test_modulus.py::test_nonreal_trace_modulus_polynomial_is_exact \
  code/tests/test_modulus.py::test_generic_hyperbolic_pipeline_performs_exact_rational_square_test
```

Result: `21 passed in 1.03s`.

Current author-side state: `AWAITING_INDEPENDENT_ROUND_3_REVIEW`.

---

# Round 3 independent static code review

Date: 2026-08-13

Scope reviewed:

- `experiments/source_lock.json`
- `experiments/EXPERIMENT_PLAN.md`
- `experiments/EXPERIMENT_TRACKER.md`
- current `results/CODE_REVIEW.md`
- current files under `code/henon_audit/`
- current files under `code/tests/`
- `code/scripts/build_result_manifest.py`
- `results/EXPERIMENT_RESULTS.md`
- `results/VALIDATION_REPORT.md`

Review mode:

- No candidate run and no full run were executed.
- No prime-table, Riemann-zero, or sealed prior-candidate data was accessed.
- Safe checks actually run:
  - `PYTHONPATH=code pytest -q`
  - `python -m compileall code`
  - a temporary manifest-linkage repro with contradictory narrative markers
  - a temporary proof-text repro with an equivalent wording change
  - a temporary scanner repro with one bad alias/tolerance file and one benign file

Bottom line:

- `DEPLOYMENT_FAIL`
- Round 1 modulus/controls fixes remain intact.
- The R001 scanner repair now appears substantially real: it catches the exact alias/tolerance escape and does not flag the benign temp file I seeded.
- But two Round 2 blockers are still not fully closed:
  1. `R010` is whitespace-robust, yet still fundamentally phrase-brittle rather than structure-driven.
  2. official-report linkage is presence/hash aware, but not a true semantic parse; contradictory stale text can still pass if the expected `PASS` substrings are also present.

## PASS: Round 1 modulus and control repairs did not regress

Evidence:

- `code/tests/test_modulus.py:40-62` still covers the planted trace `5/2`
  square-test path and the candidate exact rational modulus set `["1"]`.
- `code/tests/test_controls.py:9-34` still requires:
  - planted bad-prime control recovers `["1/2", "2"]`,
  - integral control derives exact rational modulus set `["1"]`,
  - determinant scope control refuses undeclared bad support.
- Safe suite result:
  - `PYTHONPATH=code pytest -q`
  - Result: `27 passed in 1.48s`
- Syntax sanity:
  - `python -m compileall code`
  - Result: completed without error.

Conclusion:

- The Round 1 blockers around hyperbolic square testing and integral-control
  gating remain repaired.

## PASS: R001 scanner repair now catches the exact Round 2 escape and did not false-positive on the benign temp file

Evidence in current code:

- `code/henon_audit/protocol.py:131-150` resolves simple string and
  `Path(...)` aliases.
- `code/henon_audit/protocol.py:187-267` propagates those aliases into read
  sites and flags suspicious assigned target paths.
- `code/henon_audit/protocol.py:288-305` flags
  `abs(expression) < positive_float` tolerance promotions.
- `code/tests/test_protocol_preflight_scope.py:46-61` adds the seeded alias
  and custom-tolerance regression test.

Direct non-candidate repro I ran:

- Bad temp file:
  - `prime_file = 'riemann_zeros.csv'; Path(prime_file).read_text()`
  - `tol = 1e-5; abs(value - 2) < tol`
- Benign temp file:
  - `config_file = 'local_config.json'; Path(config_file).read_text()`
  - `abs(value) < 2`
- Observed result:
  - findings only under `bad.py`
  - kinds:
    - `suspicious_target_path_alias`
    - `forbidden_target_path_literal`
    - `tolerance_exactness_promotion`
  - `good.py` appeared only in `reviewed_file_read_sites`, with no finding

Conclusion:

- Relative to the Round 2 reviewer repro, this blocker is repaired.

## FAIL: R010 is no longer line-wrap brittle, but it is still meaning-preserving-wording brittle

Evidence in current code:

- `code/henon_audit/preflight.py:26-28` correctly normalizes whitespace.
- `code/henon_audit/preflight.py:29-42` adds structured section checks.
- But `code/henon_audit/preflight.py:44-58` still hard-requires a fixed set
  of exact substrings such as:
  - `"every positive-dimensional projective subvariety"`
  - `"The other eigenvalue is $\\lambda^{-1}$"`
  - `"No finite-period computation can extend"`
- `pass` remains `all(structured_sections.values()) and all(checks.values())`
  at `code/henon_audit/preflight.py:78`.

Direct non-candidate repro I ran:

- I copied `notes/PROOF_PACKAGE.md` to a temp file.
- I changed only one semantics-preserving phrase:
  - from `every positive-dimensional projective subvariety`
  - to `any positive-dimensional projective subvariety`
- All headings remained present.
- `proof_dependency_audit()` then returned:
  - `structured_sections_ok: true`
  - `failed_checks: ["positive_dimension_hyperplane_argument"]`
  - `pass: false`

Why this matters:

- The Round 2 blocker was not merely “survive line wraps.”  The request was
  to make R010 structured and robust, not just a brittle wording check.
- The current implementation is better than Round 2, but it still rejects a
  mathematically equivalent rewrite because it keys on exact prose fragments.

Conclusion:

- This blocker is only partially repaired and remains deployment-blocking.

## FAIL: official-report linkage still is not a true semantic parse and can accept contradictory stale text

Evidence in current code:

- `code/henon_audit/manifest.py:54-58` parses the JSON inputs, but reads the
  tracker, experiment results, and validation report as raw text.
- `code/henon_audit/manifest.py:68-93` then validates those narratives mostly
  by substring containment:
  - common `PASS` markers,
  - `**Candidate executed:** \`true\``,
  - `**Must-run failed:** \`0\``,
  - `**Pytest status:** \`PASS\``,
  - matching hashes.
- `code/henon_audit/manifest.py:96-108` does regex-row extraction for the
  tracker, but the markdown narratives are not otherwise semantically parsed.
- `code/tests/test_protocol_preflight_scope.py:81-143` tests:
  - a valid linked report set, and
  - placeholder rejection,
  - but not contradictory or stale mixed-status narratives.

Direct non-candidate repro I ran:

- I built a temp report set with valid JSON/hash linkage.
- In the markdown narratives, I intentionally inserted contradictory text:
  - `**Official full-run status:** \`FAIL\`` and also `PASS`
  - `**Candidate executed:** \`false\`` and also `true`
  - `**Must-run failed:** \`7\`` and also `0`
  - `**Pytest status:** \`FAIL\`` and also `PASS`
- `validate_official_report_linkage()` still returned `status: "PASS"`.

Why this matters:

- This is exactly the stale/contradictory-text hole the Round 2 blocker was
  trying to close.
- The current validator proves that the expected success strings and hashes
  appear somewhere; it does not prove that the narratives state one coherent
  result and no conflicting status.

Conclusion:

- The manifest/report-linkage blocker remains open and deployment-blocking.

## Final decision

- `DEPLOYMENT_FAIL`

Minimum unblock sequence before deployment:

1. Replace the remaining exact-phrase proof gate with a genuinely structured
   section-aware check, or explicitly downgrade it to a non-gating
   provenance-presence report instead of `R010` pass/fail.
2. Make `validate_official_report_linkage()` parse the tracker and markdown
   narratives into unique status fields, then reject duplicate/conflicting
   values rather than accepting mere substring presence.
3. Add negative tests for:
   - contradictory `PASS`/`FAIL` and `true`/`false` mixed narratives,
   - equivalent proof wording under unchanged structure.

Only after those are fixed should this package move to another deployment
review.

---

# Round 3 remediation record (implementation author; pending Round 4)

Date: 2026-08-14

This is an author-side remediation log, not an independent verdict.  No
controls-only command and no candidate/full run was executed.

## R010 now blocks only stable structure, never equivalent prose

- `notes/PROOF_PACKAGE.md` now carries one versioned
  `HENON_PROOF_SCHEMA_ID`, exactly one ID for each required theorem/proof
  section, and exactly one ID for each indispensable equation in the proof
  chain.
- `proof_dependency_audit()` blocks only when that exact section/equation ID
  schema is missing, duplicated, or contains an unknown ID.  It explicitly
  records that the mathematical audit authority is the independently reviewed
  v2 source lock validated by R000.
- Former natural-language phrase checks remain diagnostic only under
  `advisory_prose_checks`; `natural_language_checks_are_blocking` is `false`
  and advisory failures cannot change `pass`.
- A regression replaces `every positive-dimensional...` by the semantically
  equivalent `any positive-dimensional...`; the advisory flips to false while
  R010 still passes.  A duplicate stable equation ID remains blocking.

## Reports now use one strict JSON authority rather than substrings

- The only accepted machine status is a single JSON object delimited by
  `HENON_AUDIT_META_V1`; it is parsed with duplicate-key detection.
- Each of tracker, experiment results, and validation report has an exact
  field set.  Missing or unknown keys, duplicate blocks, unknown schema,
  candidate, or status, non-PASS states, invalid hashes, and placeholder text
  all fail closed.
- Legacy Markdown bold status fields are forbidden outside the JSON block, so
  contradictory `FAIL`/`false`/nonzero prose cannot coexist with the machine
  authority.
- Tracker rows are parsed into exactly four cells; each run ID must be unique,
  every status is from the closed enum, the set of IDs must equal the JSON run
  registry exactly, and all must be `PASS`.  The JSON registry itself also
  rejects duplicate IDs, extra keys, unknown/non-PASS states, and an empty
  registry.
- Regression tests cover the Round 3 contradictory-status reproducer,
  duplicate tracker IDs, duplicate JSON keys, two metadata blocks, unknown
  fields/states, placeholders, and exact hash linkage.

## Safe non-candidate regression result

`python -m compileall -q code` completed successfully.  The complete
non-candidate suite (candidate-specific audit tests deliberately omitted) ran
with result:

```text
26 passed in 1.14s
```

Current author-side state: `AWAITING_INDEPENDENT_ROUND_4_REVIEW`.

---

# Round 4 independent static code review

Date: 2026-08-13

Scope reviewed:

- `experiments/source_lock.json`
- `experiments/EXPERIMENT_PLAN.md`
- `experiments/EXPERIMENT_TRACKER.md`
- current `results/CODE_REVIEW.md`
- current files under `code/henon_audit/`
- current files under `code/tests/`
- `code/scripts/build_result_manifest.py`
- `code/README.md`
- `notes/PROOF_PACKAGE.md`
- `results/EXPERIMENT_RESULTS.md`
- `results/VALIDATION_REPORT.md`

Review mode:

- No candidate run, full audit run, or formal `--controls-only` run was executed.
- No prime-table, Riemann-zero, or sealed prior-candidate data was accessed.
- Safe checks actually run:
  - `PYTHONPATH=code pytest -q`
  - `python -m compileall -q code`
  - temporary non-candidate proof-gate repros for equivalent prose and duplicate stable IDs
  - temporary non-candidate report-linkage repros for duplicate blocks/keys, legacy contradictions, unknown fields, hash mismatch, tracker duplicate/set mismatch, and one additional indented-legacy-field escape

Bottom line:

- `DEPLOYMENT_FAIL`
- Round 3 blocker (1) is now genuinely repaired: `R010` blocks on the versioned proof-ID schema, section/step IDs, and equation IDs, while equivalent prose is advisory only.
- Most of Round 3 blocker (2) is also genuinely repaired: duplicate blocks, duplicate JSON keys, unknown fields, hash mismatch, tracker duplicate IDs, and tracker set mismatches are rejected.
- However, the claimed “legacy contradictory machine fields are forbidden outside the JSON authority” rule is still fail-open for indented legacy fields, so the strict `HENON_AUDIT_META_V1` authority requirement is not yet fully enforced.

## PASS: R010 now behaves the way the Round 3 blocker required

Evidence in current code:

- `code/henon_audit/preflight.py:20-27` explicitly states that blocking logic is structural only and prose checks are advisory.
- `code/henon_audit/preflight.py:30-83` requires exactly one current schema ID, an exact required section-ID set, and an exact required equation-ID set, each with uniqueness enforced.
- `code/henon_audit/preflight.py:101-126` makes `pass` depend only on those structural checks.

Independent repros I ran:

- Semantics-preserving prose rewrite:
  - changed `every positive-dimensional projective subvariety`
  - to `any positive-dimensional projective subvariety`
  - observed result: `pass=True`, advisory flag for that phrase became `False`
- Duplicate stable equation ID:
  - appended `<!-- HENON_PROOF_EQUATION_ID: CYCLIC_RECURRENCE -->`
  - observed result: `pass=False`, `each_required_equation_id_unique=False`

Existing regression coverage matches that behavior:

- `code/tests/test_protocol_preflight_scope.py:250-275` checks that equivalent prose is non-blocking while a duplicate stable ID still blocks.

Conclusion:

- The Round 3 `R010` requirement is satisfied as implemented.

## PASS: modulus square-test, controls, and scanner regressions all hold in the current tree

Evidence in current code:

- `code/henon_audit/modulus.py:137-229` now performs the exact rational square-root test and emits rational modulus classifications from exact rational `mu`.
- `code/henon_audit/controls.py:29-78` routes the planted `5/2` trace through that generic path and requires `["1/2", "2"]`.
- `code/henon_audit/controls.py:91-162` derives the integral negative-control modulus set from `modulus_records` and requires it to equal `["1"]`.
- `code/henon_audit/protocol.py:59-334` still catches the aliased target-path and tolerance-promotion scanner regressions from Round 2/3.

Safe regression results I ran:

- `PYTHONPATH=code pytest -q`
  - result: `31 passed in 1.54s`
- `python -m compileall -q code`
  - result: completed without error

Relevant tests currently present:

- `code/tests/test_modulus.py:40-62`
- `code/tests/test_controls.py:9-34`
- `code/tests/test_protocol_preflight_scope.py:26-66`

Conclusion:

- The previously repaired modulus, controls, and scanner paths did not regress.

## FAIL: the “strict JSON authority forbids legacy contradictory machine fields” rule still has a real whitespace escape

What the code claims:

- `code/README.md:41-47` says the three official Markdown artifacts are governed by exactly one `HENON_AUDIT_META_V1` JSON block and that legacy bold machine-status fields in the body are rejected.
- `code/henon_audit/manifest.py:97-103` is the enforcement point for that rule.

The fail-open detail:

- `code/henon_audit/manifest.py:36-40` defines `LEGACY_MACHINE_FIELD_PATTERN` as
  line-start anchored `^\*\*...` with no optional leading whitespace.
- Therefore only a body line that begins immediately with `**Official full-run status:**`, `**Candidate executed:**`, etc. is rejected.
- A human-visible contradictory machine field with leading indentation is not matched.

Direct non-candidate repro I ran:

- I built an otherwise valid temporary linked report set.
- In `EXPERIMENT_RESULTS.md` I appended this body line outside the JSON block:

  `  **Official full-run status:** \`FAIL\``

- `validate_official_report_linkage()` still returned `status: "PASS"`.

Why this is deployment-blocking:

- The Round 3 requirement was not merely “reject one exact unindented string.” It was that legacy contradictory machine fields outside the sole JSON authority be rejected.
- The current implementation still allows a contradictory legacy machine field to coexist with a machine `PASS` block, provided the line is indented.
- That is a genuine fail-open path in the exact area that Round 3 claimed to have closed.

Why the current tests missed it:

- `code/tests/test_protocol_preflight_scope.py:175-188` only seeds the unindented form:
  `**Official full-run status:** \`FAIL\``
- There is no regression for the indented equivalent with one or more leading spaces/tabs.

## Other Round 3 report-linkage checks that I independently re-verified

These all behaved correctly in my temporary repros:

- duplicate metadata block → rejected
- duplicate JSON metadata key → rejected
- unknown metadata field → rejected
- hash mismatch → rejected
- tracker duplicate run ID → rejected
- tracker run-ID set mismatch → rejected

So the remaining problem is narrow but real: the legacy-field prohibition is not yet whitespace-robust.

## Note on the committed report templates

The committed `results/EXPERIMENT_RESULTS.md`, `results/VALIDATION_REPORT.md`,
and `experiments/EXPERIMENT_TRACKER.md` are still pre-run templates / pre-run
tracker text rather than final `HENON_AUDIT_META_V1` artifacts.  I am not
counting that against deployment here because `code/README.md:34-47`
explicitly documents that they are replaced/updated after the official full
run, and the parser now fails closed on placeholders or malformed final
artifacts.  The blocker above is instead about the final-artifact validator
still accepting one class of contradictory legacy machine field.

## Final decision

- `DEPLOYMENT_FAIL`

Minimum unblock before deployment:

1. Make legacy machine-field rejection whitespace-robust, for example by
   treating leading horizontal whitespace before `**...**` as still forbidden.
2. Add negative regressions for at least:
   - one-space-indented legacy contradiction,
   - tab-indented legacy contradiction,
   - the other forbidden legacy field names (`Candidate executed`,
     `Must-run failed`, `Pytest status`, etc.) under the same indentation.

Only after that fix should this package proceed to final deployment.

---

# Round 4 remediation record (implementation author; pending follow-up)

Date: 2026-08-14

This is an author-side narrow remediation, not an independent verdict.  No
controls-only command and no candidate/full run was executed.

## Whitespace and Markdown-prefix escape closed

- `LEGACY_MACHINE_FIELD_PATTERN` now accepts arbitrary leading horizontal
  whitespace before a forbidden legacy machine field.
- It also consumes repeated Markdown blockquote prefixes and list markers
  (`-`, `+`, `*`, or ordered markers), including combinations such as
  `> - **Pytest status:** ...`.  A machine field cannot evade the sole JSON
  authority by being indented, quoted, or made into a list item.
- The match still requires the bold machine field to begin immediately after
  those structural prefixes.  An ordinary prose sentence that merely mentions
  `**Official full-run status:**` later in the line is not treated as a second
  machine declaration.

## Regression coverage

The exact reviewer reproducer with two leading spaces is rejected.  The
parameterized regression additionally covers a tab, blockquote, nested
blockquote/list, unordered list, ordered list, and every remaining legacy
field family.  A normal narrative mention is retained as a negative control.

`python -m compileall -q code` completed successfully.  The expanded complete
non-candidate selection passed:

```text
34 passed in 1.18s
```

Current author-side state: `AWAITING_ROUND_4_FOLLOW_UP_REVIEW`.

---

# Round 4 follow-up

Date: 2026-08-13

Scope reviewed:

- current `results/CODE_REVIEW.md`
- `code/henon_audit/manifest.py`
- `code/tests/test_protocol_preflight_scope.py`
- current snapshots of `code/henon_audit/preflight.py`,
  `code/henon_audit/modulus.py`, `code/henon_audit/controls.py`, and
  `code/henon_audit/protocol.py`

Review mode:

- No formal `--controls-only` run was executed.
- No candidate run, full exact audit, prime-table access, or Riemann-zero data
  access was performed.
- Safe checks actually run:
  - `PYTHONPATH=code pytest -q` → `39 passed in 1.50s`
  - `python -m compileall -q code`
  - independent temporary linked-report repros for:
    - `  **Official full-run status:** FAIL`
    - tab-indented `**Candidate executed:** false`
    - blockquote/list/ordered-list/nested-prefix legacy fields such as
      `> - **Pytest status:** FAIL`
    - an ordinary narrative sentence that merely mentions
      `**Official full-run status:**`

Bottom line:

- `DEPLOYMENT_PASS`
- The narrow Round 4 blocker is fixed: legacy machine fields are now rejected
  even with leading spaces, tabs, blockquote prefixes, list markers, and
  nested quote/list prefixes.
- The negative control still holds: an ordinary narrative mention of
  `**Official full-run status:**` later in the line is allowed.
- I re-read the current snapshots of the previously passing Round 4 areas and
  found no behavioral regression in `R010`, modulus square testing, the
  integral-control gate, or the forbidden-data scanner.

## PASS: legacy machine-field rejection is now whitespace- and prefix-robust

Evidence in current code:

- `code/henon_audit/manifest.py:36-40` now allows optional leading horizontal
  whitespace plus repeated blockquote/list prefixes before checking for the
  forbidden bold machine fields.
- `code/henon_audit/manifest.py:102-104` still fails closed as soon as such a
  legacy field is present outside the sole `HENON_AUDIT_META_V1` JSON block.
- `code/tests/test_protocol_preflight_scope.py:215-239` now carries the
  parameterized legacy-prefix regression coverage plus the ordinary-narrative
  negative control.

Independent repro results:

- `  **Official full-run status:** FAIL` → rejected
- `\t**Candidate executed:** false` → rejected
- `> **Must-run failed:** 7` → rejected
- `- **Run-summary SHA-256:** stale` → rejected
- `1. **Candidate-audit SHA-256:** stale` → rejected
- `>\t- **Pytest status:** FAIL` → rejected
- `+ **Pytest XML SHA-256:** stale` → rejected
- ordinary narrative mention of `**Official full-run status:**` later in the
  sentence → accepted, and `validate_official_report_linkage()` returned
  `status == "PASS"`

Conclusion:

- The exact fail-open path identified in the Round 4 review is closed.

## PASS: previously cleared Round 4 items did not regress in the current tree

Current code still matches the previously accepted behaviors:

- `code/henon_audit/preflight.py:75-105` still makes `R010` structural-only:
  exact schema/section/equation IDs are blocking, while
  `natural_language_checks_are_blocking` remains `False`.
- `code/henon_audit/modulus.py:137-227` still performs the exact rational
  square-root test and emits exact rational modulus classifications; the
  irrational-square case still lands in
  `RATIONAL_MU_BUT_IRRATIONAL_MODULUS`.
- `code/henon_audit/controls.py:29-66` still routes the planted `5/2` control
  through the generic modulus path, and
  `code/henon_audit/controls.py:91-148` still derives the integral negative
  control’s modulus set from `modulus_records`.
- `code/henon_audit/protocol.py:59-334` still contains the aliased forbidden
  path and tolerance-promotion findings that Round 2/3/4 required.

Safe regression results:

- `PYTHONPATH=code pytest -q` passed completely: `39 passed in 1.50s`
- `python -m compileall -q code` completed without error

Conclusion:

- I found no behavioral regression in the areas that had already passed before
  this follow-up.

## Final decision

- `DEPLOYMENT_PASS`
