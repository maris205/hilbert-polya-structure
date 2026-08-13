# Independent pre-run code review — Paper 4 algebraic action clocks

Review date: Thursday, 2026-08-13 (UTC)

Verdict: DEPLOYMENT_FAIL

This review stayed within the requested guardrails:

- did not access prime tables, zero data, candidate periodic-point solving, candidate action computation, or the formal project CLI;
- used only static reads, safe syntax compilation, safe unit tests, and isolated temporary negative controls;
- did not modify code or notes; this file is the only artifact written.

## Executive summary

The mathematical/source-lock core is mostly implemented as intended:

- source-lock v3 hash and zero-execution counters pass;
- gauge endpoint bookkeeping, pole stops, multivalued-gauge stops, HL beta=0 / beta=1 handling, and `log|A|` nonclaim are present;
- Hénon one-form / type-1 / inverse / Jacobian / multiplicity / projective-infinity / orbit-field / `3A`-only denominator ledger are implemented consistently;
- the current executable surface shows no hidden candidate periodic-orbit solver, no candidate parameter substitution, and no target-data loading.

However, deployment should not proceed yet because four operational defects remain:

1. the proof-text dependency gate `R002` is currently broken and already fails the safe unit suite;
2. the executable-isolation scanner is not fail-closed because it skips `protocol.py`;
3. the result manifest is not closed over Markdown review artifacts such as `results/CODE_REVIEW.md`;
4. the runtime environment manifest is hardcoded to the future date `2026-08-14`, while today is Thursday, 2026-08-13.

## Commands executed

All commands were run from `/root/autodl-tmp/symplectic_map`.

1. Static inventory / source reads:

   - `rg --files ...`
   - `sed -n ...`
   - `rg -n ...`

2. Safe syntax compilation with temp pycache:

   - `PYTHONPYCACHEPREFIX=$(mktemp -d) python -m compileall -q papers/5-algebraic-action-clocks/code/action_audit papers/5-algebraic-action-clocks/code/tests papers/5-algebraic-action-clocks/code/scripts`
   - Result: PASS

3. Safe unit suite:

   - `PYTHONPYCACHEPREFIX=$(mktemp -d) PYTHONDONTWRITEBYTECODE=1 pytest -q papers/5-algebraic-action-clocks/code/tests`
   - Result: FAIL, `1 failed, 61 passed`
   - Failing test: `test_proof_dependency_audit_passes_repaired_proof`

4. Safe suite with only the known failing proof-text gate deselected:

   - `PYTHONPYCACHEPREFIX=$(mktemp -d) PYTHONDONTWRITEBYTECODE=1 pytest -q papers/5-algebraic-action-clocks/code/tests -k 'not test_proof_dependency_audit_passes_repaired_proof'`
   - Result: PASS, `61 passed, 1 deselected`

5. Isolated temporary negative controls (no project CLI):

   - direct import of `validate_source_lock(...)`: PASS
   - direct import of `proof_dependency_audit(...)`: FAIL only on `general_endpoint_mismatch`
   - isolated temp `protocol.py` containing `import requests`: scanner incorrectly returned PASS
   - isolated manifest-selection fixture containing `results/CODE_REVIEW.md`: file was omitted from manifest input
   - direct import of `action_audit.cli._environment(...)`: returned `execution_date_utc = 2026-08-14`

## Required-check matrix

| Item | Status | Evidence |
|---|---|---|
| (1) v3 hash / gates / zero counters | PASS | `validate_source_lock(...)` returns expected SHA-256 `d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7`, `lock_version = 3`, `lock_status = SOURCE_LOCKED_NO_CANDIDATE_EXECUTION`, and all execution counters clean. |
| (2) Gauge general-endpoint formula; single-valued `Qbar` gauge; closed-nonexact / multivalued / pole stops | PASS (logic), FAIL (proof gate robustness) | `gauge.py`, `scope.py`, and `controls.py` encode the repaired semantics correctly. The formal proof-text check still fails to recognize the endpoint formula even though the proof contains it. |
| (3) HL beta=0/1 and `log|A|` boundary | PASS | `algebraic.py` and `controls.py` implement `ZERO`, `ONE`, nontrivial algebraic target classes, and classify `LOG_ABS_ACTION` as nonclaim without numeric post-processing. |
| (4) Hénon one-form / type-1 / inverse / Jacobian; `n=1,2` multiplicity; projective infinity; orbit field / `S` extension; only `3A` integral | PASS | `henon.py` and `test_henon.py` are consistent; safe suite passes these checks. |
| (5) `LOG_OF_TARGET_TWO` is symbolic only and never loads a target | PASS | `controls.py` uses provenance labels only, with `numeric_logarithm_evaluated = False` and `external_target_table_accessed = False`. |
| (6) Scanner fail-closed | FAIL | `static_executable_isolation_scan(...)` skips `protocol.py`, so a forbidden import placed there is invisible to the scanner. |
| (7) CLI is controls-first and has no hidden candidate compute | PASS (current logic), not deployment-ready | `cli.py` runs controls before Hénon static checks and current code shows no hidden solver/parameter substitution. But an official run would still abort at `R002`, and its environment manifest is future-dated. |
| (8) Report-manifest closure | FAIL | `build_result_manifest.py` includes `results/*.json` only; it omits `results/CODE_REVIEW.md` and any other non-JSON result reports. |

## Detailed findings

### F1. Broken proof-text integrity gate blocks deployment

Severity: high

The full safe test suite fails here:

- `papers/5-algebraic-action-clocks/code/tests/test_algebraic.py`
- failing assertion: `test_proof_dependency_audit_passes_repaired_proof`

Direct inspection of `proof_dependency_audit(...)` shows:

- `general_endpoint_mismatch = false`
- all other dependency checks = `true`

Root cause:

- `papers/5-algebraic-action-clocks/code/action_audit/algebraic.py:123` searches for the exact literal string  
  `"$\\chi_n(P_n)-\\chi_0(P_0)+\\sum_{j=0}^{n-1}C_j$" in flat`
- but the proof contains the repaired formula in display-math layout at:
  - `papers/5-algebraic-action-clocks/notes/PROOF_PACKAGE.md:104-106`
  - `papers/5-algebraic-action-clocks/notes/PROOF_PACKAGE.md:360-364`

So the theorem text is present, but the integrity checker is too brittle and would make the official static audit stop at `R002`.

### F2. Executable-isolation scanner is not fail-closed

Severity: high

`papers/5-algebraic-action-clocks/code/action_audit/protocol.py:116-118` explicitly skips:

- any file under `tests`
- any file named `protocol.py`

This means the scanner never audits its own `protocol.py`, even though that module is imported by the executable path and contains source-lock and scan logic.

Temporary negative control:

- created isolated temp directory with only `protocol.py` containing `import requests`
- `static_executable_isolation_scan(temp_dir)` returned:
  - `pass = true`
  - `findings = []`
  - `scanned_files = []`

That is a real fail-closed gap.

### F3. Result-manifest closure is incomplete

Severity: medium

`papers/5-algebraic-action-clocks/code/scripts/build_result_manifest.py:25-35` selects:

- `results/*.json`
- fixed experiment / note files
- `code/**/*.py`

It does not include:

- `results/CODE_REVIEW.md`
- any other non-JSON result report placed under `results/`

Temporary negative control:

- created isolated fixture root containing `results/run_summary.json` and `results/CODE_REVIEW.md`
- replayed the manifest-selection logic
- result: `includes_code_review_md = false`

So the manifest does not close over the required review artifact.

### F4. Runtime environment manifest is future-dated

Severity: medium

Today in this environment is Thursday, 2026-08-13.

But `papers/5-algebraic-action-clocks/code/action_audit/cli.py:49` hardcodes:

- `execution_date_utc = "2026-08-14"`

Direct safe import of `_environment(...)` returned that future date. If the audit were run today, it would emit a manifest dated tomorrow.

Related metadata also uses `2026-08-14`:

- `papers/5-algebraic-action-clocks/experiments/source_lock.json:4`
- `papers/5-algebraic-action-clocks/experiments/EXPERIMENT_PLAN.md:5`

Those document timestamps may be intentional frozen metadata, but the runtime environment manifest should not be future-dated at execution time.

## Positive confirmations

These parts looked good in the current codebase:

- `validate_source_lock(...)` correctly closes the v3 repair ledger and zero-execution gate.
- `controls.py` keeps `LOG_OF_TARGET_TWO` symbolic and does not evaluate or load targets.
- `gauge.py` retains the full endpoint term and distinguishes endpoint-compatible vs mismatch cases.
- `scope.py` stops on map undefinedness, pole/definedness failures, missing keys, and non-admitted observables.
- `henon.py` matches the intended static Hénon identities and the `3A_G` denominator ledger.
- No candidate orbit search, candidate action computation, inherited-parameter substitution, prime-table read, zero-data access, network call, or approximate log fitting was found in the current executable surface.

## Final deployment decision

DEPLOYMENT_FAIL

Rationale:

1. the official proof gate `R002` is currently broken and fails the safe test suite;
2. the scanner is not fail-closed because `protocol.py` is exempt;
3. the result manifest misses the required Markdown review artifact;
4. the runtime environment stamp is future-dated relative to Thursday, 2026-08-13.

I would re-review after those four issues are fixed, without changing the mathematical source-lock claims unless the proof or executable behavior changes.

## Author repair record after the failed pre-run review

**Repair status:** `READY_FOR_ROUND2_REVIEW`; this is not deployment
authorization, and the formal project CLI remains unexecuted.

The four required repairs were implemented as follows:

1. **R002 proof gate.**  `PROOF_PACKAGE.md` now exposes an auditable proof
   contract, version 3, with stable dependency IDs and tagged equations.
   `proof_dependency_audit` parses that structure and normalizes TeX
   whitespace/layout commands instead of searching for exact prose.  Added
   regressions prove that equivalent equation whitespace passes, while an
   endpoint-sign change or missing dependency ID fails.
2. **Fail-closed scanner.**  `protocol.py` is no longer skipped.  All
   executable Python modules, including the scanner itself, are parsed.
   Static deny-list strings do not self-trigger because findings arise only
   from AST import/call nodes and floating literals.  A temporary file named
   exactly `protocol.py` containing `import requests` now fails its test.
3. **Manifest closure.**  A new semantic manifest gate requires all seven
   JSON audit outputs, `CODE_REVIEW.md`, `VALIDATION_REPORT.md`,
   `EXPERIMENT_RESULTS.md`, and passing `pytest.xml`; it validates the
   zero-candidate counters, v3 lock hash, proof-contract version, final review
   verdict, report markers, and test failure/error counts before hashing.
   Every result file is then included, not only `*.json`.
4. **Runtime UTC provenance.**  The runtime environment record now derives
   its date and timestamp from `datetime.now(timezone.utc)` and explains that
   source-lock/plan dates are frozen document metadata.  The resumed session
   metadata reports `2026-08-14` UTC, while a container `date -u` sample
   during the safe repair tests returned `2026-08-13T16:42:41Z`; no hardcoded
   runtime date remains, so this control-plane/container-clock discrepancy
   cannot create a falsely fixed execution date.

Safe verification performed after the repairs:

- syntax compilation: **PASS**;
- full safe unit suite: **72 passed in 2.65 s**;
- JUnit artifact: `results/pytest.xml`, SHA-256
  `5be8ee8c366c60c39489df89db49f65a8275042834f10628e0949292e63f5f29`;
- repaired proof SHA-256:
  `2148e61c537388e22ea96b1d2b7b13dcc40e669ab303966e62f2c227819a0d91`;
- source-lock v3 remains unchanged at
  `d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7`.

No formal CLI, candidate parameter substitution, periodic-point solve,
candidate action evaluation, prime/zero data access, or network operation
was performed.  Round 2 independent review is still required before any
formal static run.

---

# Independent pre-run code review — Round 2

Review date: Thursday, 2026-08-13 (container UTC; session document date is
2026-08-14 UTC)

Verdict: DEPLOYMENT_FAIL

This was an independent re-review of the repaired code and source-lock v3.
It remained strictly pre-run: I did not invoke the formal project CLI, solve
any candidate periodic equation, evaluate any candidate action, substitute
the inherited parameter, access prime or Riemann-zero data, or make a network
request.  Only static reads, syntax compilation, the safe unit suite, and
isolated temporary negative controls were used.

## Executive decision

Two of the four Round-1 blockers are closed:

- the scanner now includes `action_audit/protocol.py`, and a temporary file
  named exactly `protocol.py` containing `import requests` is rejected;
- runtime date and timestamp provenance now comes from the actual UTC clock,
  with frozen source-document dates explicitly distinguished from runtime
  metadata.

Two blockers remain and are independently reproducible:

1. R002 is structured syntactically but is still semantic fail-open.  Merely
   retaining a contract ID or required equation tokens is enough to pass,
   even when the associated contract meaning is deleted, an untracked term
   is added to the gauge equation, or a contract ID is duplicated.
2. The result manifest is inclusive rather than closed.  It hashes arbitrary
   extra and nested result artifacts and nevertheless reports semantic PASS,
   so it does not enforce the required no-extra/no-duplicate result schema.

The safe test suite passing does not override these adversarial failures,
because the deployment gate is specifically required to fail closed against
them.

## Commands and safe evidence

All commands were run from
`/root/autodl-tmp/symplectic_map`.

1. Static inventory and source inspection with `rg`, `sed`, `nl`, `stat`,
   and `sha256sum`: PASS.
2. Safe syntax compilation of `code/action_audit`, `code/tests`, and
   `code/scripts` with an isolated bytecode cache: PASS.
3. Full safe unit suite:

   - result: **72 passed in 2.80 s**;
   - no formal CLI or candidate computation was invoked.

4. Direct source-lock validation:

   - source-lock version: 3;
   - SHA-256:
     `d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7`;
   - status: `SOURCE_LOCKED_NO_CANDIDATE_EXECUTION`;
   - all candidate exact/numerical, periodic-point, action, prime-table, and
     zero-data counters: clean;
   - result: PASS.

5. Isolated proof-contract negative controls, each applied to a temporary
   copy of `PROOF_PACKAGE.md`:

   - replace the entire `AC-HL-v3` table-row meaning with contradictory
     placeholder prose while retaining only the ID: R002 incorrectly PASS;
   - append `+T_{untracked}` to the tagged general gauge-shift equation while
     retaining all expected substrings: R002 incorrectly PASS;
   - insert a second, contradictory `AC-GAUGE-v3` contract row: R002
     incorrectly PASS.

6. Isolated manifest negative controls using the complete passing fixture:

   - add `results/unexpected.json`: validation incorrectly remains PASS and
     the unexpected file is selected for hashing;
   - add `results/duplicate/run_summary.json`: validation incorrectly remains
     PASS and the nested duplicate basename is selected for hashing.

7. Isolated scanner control:

   - a temporary `protocol.py` containing `import requests` is scanned and
     rejected with a `forbidden_import` finding: PASS.

8. Runtime provenance control:

   - Python runtime record:
     `execution_date_utc = 2026-08-13` and a timestamp ending in `Z`;
   - contemporaneous `date -u` sample:
     `2026-08-13T16:48:11Z`;
   - the runtime record explicitly states that source-lock and plan dates are
     frozen document metadata: PASS.

## Round-1 repair matrix

| Round-1 item | Round-2 result | Evidence |
|---|---|---|
| R002 proof dependency contract | **FAIL** | Three isolated semantic mutations described above all return PASS. |
| Scanner includes `protocol.py` | **PASS** | Current scan lists `action_audit/protocol.py`; same-name forbidden-import control fails closed. |
| Manifest closes all required reports and JSON | **FAIL** | Required artifacts are included, but arbitrary extra and nested duplicate artifacts are accepted. |
| Actual runtime UTC provenance | **PASS** | Runtime values match the container UTC clock; document/runtime date policy is explicit. |

## Finding R2-F1 — R002 still accepts semantic regressions

Severity: high; deployment blocker

The repaired checker is more stable against harmless TeX whitespace, but it
does not yet provide the promised semantic contract.

At `code/action_audit/algebraic.py:173-232`:

- contract rows are stored in a dictionary, so a duplicate ID silently
  overwrites the earlier occurrence;
- several checks require only that an ID is present, without checking the
  row's stated mathematical content;
- tagged equations are accepted by substring containment, so extra terms can
  alter the equation while all required tokens remain present.

The negative controls show all three paths return `pass = true`.  This is a
real fail-open: for example,

```text
A'-A=chi_n(P_n)-chi_0(P_0)+sum_j C_j+T_untracked
```

retains the required substrings but is not the frozen general gauge formula.

There is also one current source-integrity symptom at
`notes/PROOF_PACKAGE.md:246`: the first `beta` in the `AC-HL-v3` row begins
with the control character U+0008 rather than a backslash.  The prose and
tagged HL equation elsewhere are mathematically correct, but R002 does not
notice this damaged contract-row statement.

Required repair before another review:

- reject non-whitespace control characters in the proof contract;
- require the exact set of contract IDs, exactly once each;
- validate each contract row against explicit machine-readable dependencies,
  not mere ID presence;
- parse each tagged equation into an exact normalized contract, or otherwise
  require equality to its allowed normalized form, so extra terms, changed
  operators, and duplicate tags fail;
- add regressions for the three mutations above.

## Finding R2-F2 — manifest schema is not closed against extras or duplicates

Severity: high; deployment blocker

`code/action_audit/manifest.py:39-51` recursively selects every file below
`results/`, while `validate_required_artifacts` at lines 170-215 checks only
that the required paths are a subset of that selection.  It never requires
the selected result set to equal the declared result schema.

Consequently, both `results/unexpected.json` and
`results/duplicate/run_summary.json` are accepted and hashed while
`validate_required_artifacts(...)["pass"]` remains true.  Hashing an extra
artifact does not make the schema closed: an unintended, stale, ambiguous,
or duplicate result still receives final-manifest authority.

Required repair before another review:

- define the exact allowed `results/` input set as the seven required JSON
  files plus `CODE_REVIEW.md`, `VALIDATION_REPORT.md`,
  `EXPERIMENT_RESULTS.md`, and `pytest.xml`, excluding only the manifest being
  built;
- require equality, not subset inclusion, between discovered and allowed
  result paths;
- reject nested result files/directories and duplicate required basenames;
- add negative regressions for an unexpected JSON file and a nested duplicate
  `run_summary.json`.

## Positive confirmations

- The v3 source-lock hash is unchanged and all pre-execution counters remain
  zero.
- The scanner covers all eleven executable Python files, including
  `protocol.py`, and reports no finding in the current tree.
- The formal CLI order remains source lock, isolation scan, proof gate,
  controls, and only then Hénon static identities.
- The executable surface contains no candidate periodic-orbit solver, no
  inherited-parameter substitution, and no candidate action evaluation.
- `LOG_OF_TARGET_TWO` remains a symbolic provenance label; there is no
  numeric logarithm or external target-table read.
- Runtime UTC is generated dynamically and the document-date discrepancy is
  transparent.
- The Hénon checks remain static identities and categorical proof audits;
  they do not enumerate candidate orbits.

## Final deployment decision

DEPLOYMENT_FAIL

The formal static CLI must remain closed.  Re-review is appropriate after
R002 rejects semantic mutations and the result manifest enforces an exact,
no-extra/no-duplicate schema.  No mathematical source-lock amendment is
required by this review unless repairing the malformed contract-row control
character changes the frozen source document; the underlying theorem claims
were not challenged here.

## Author repair record after Round 2

**Repair status:** `READY_FOR_ROUND3_REVIEW`; this record is not deployment
authorization.  The formal static CLI and all candidate execution remain
closed.

Both Round-2 blockers were repaired without changing source-lock v3:

1. **Unique machine-readable R002 contract.**  The former natural-language
   table was replaced by exactly one delimited JSON contract.  Its parsed
   schema, ordered contract records, IDs, and explicit dependency lists must
   equal the frozen in-code contract exactly.  Duplicate JSON keys, duplicate
   contract IDs, missing or changed dependencies, duplicate equation tags,
   and any tagged equation that differs after layout-only TeX normalization
   now fail.  Equivalent whitespace and `left`/`right`/spacing commands still
   pass.  R002 also scans the entire proof file for non-whitespace Unicode
   control characters.  The U+0008 before `beta` was removed.
2. **Exact manifest result schema.**  The manifest now permits exactly the
   seven required JSON outputs plus `CODE_REVIEW.md`,
   `VALIDATION_REPORT.md`, `EXPERIMENT_RESULTS.md`, and `pytest.xml` as
   inputs.  A regular top-level `final_result_manifest.json` is an optional
   output and is never hashed as its own input.  Validation rejects missing
   or unknown results, nested result paths/directories, repeated basenames,
   symlinks, paths resolving outside the normalized project root, and
   non-regular required inputs.  Required-set equality replaces the former
   subset test.

The exact Round-2 reproductions now behave fail closed:

- delete `beta_zero_has_no_complex_logarithm` from `AC-HL-v3`: R002 FAIL;
- append `+T_{untracked}` to the gauge equation: R002 FAIL;
- replace `AC-OBS-v3` with a second `AC-GAUGE-v3`: R002 FAIL with duplicate-ID
  evidence;
- inject U+0008 anywhere in the proof contract: R002 FAIL with its codepoint
  and offset recorded;
- add `results/unexpected.json`: manifest validation FAIL with an unknown-path
  record;
- add `results/duplicate/run_summary.json`: manifest validation FAIL with
  nested-path and duplicate-basename records;
- replace a result with a symlink or point a result symlink outside the root:
  manifest validation FAIL.

Safe verification after repair:

- syntax compilation: **PASS**;
- full safe suite: **82 passed in 3.17 s**;
- JUnit SHA-256:
  `7a20191906004ba63b617066fde8dc4ccfb3450f4e697b3e4c9dd16213f70f99`;
- repaired proof SHA-256:
  `c579e2da093a8ab588a5818bab0df59a47804792fcdfa338777f48e1bd1a1214`;
- unchanged source-lock-v3 SHA-256:
  `d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7`.

No formal project CLI, candidate parameter substitution, periodic-point
solve, candidate action evaluation, prime/zero data access, or network
operation was performed.  A fresh independent Round-3 pre-run review is
required before deployment.

## Round 3 author self-check

Status: `AUTHOR_SELF_CHECK / NOT INDEPENDENT / NO DEPLOYMENT AUTHORITY`

This check was performed by the Round-2 repair author and therefore cannot
issue an independent `DEPLOYMENT_PASS`.  Its sole purpose was to verify that
the repaired implementation is ready for a separate reviewer.

Scope and outcome:

- R002 baseline structured contract: PASS.
- Replace an `AC-HL-v3` semantic dependency while retaining the surrounding
  prose and ID: correctly FAIL.
- Add an untracked term to the exact gauge equation: correctly FAIL.
- Duplicate `AC-GAUGE-v3`: correctly FAIL with both duplicate-ID and frozen
  contract mismatch evidence.
- Exact result-schema fixtures with an extra file, missing required report,
  stale failed review verdict, nested duplicate, or required-result symlink:
  all correctly FAIL.  The stale-review fixture specifically fails the
  semantic `CODE_REVIEW.md` gate even though its flat path schema is valid.
- Safe syntax compilation: PASS.
- Full safe unit suite: **82 passed in 3.07 s**.

No formal CLI/static candidate run, candidate parameter substitution,
periodic-point solve, candidate action evaluation, target-data read, or
candidate result generation occurred.  Independent Round-3 review remains
mandatory before deployment.

---

# Independent pre-run code review — Round 3

Review date: 2026-08-14 session research date; the isolated runtime check
reported the container UTC clock as 2026-08-13.

Verdict: DEPLOYMENT_PASS

## Independence and scope

This reviewer did not author or repair the Paper-4 implementation and had not
participated in its Round-1 or Round-2 reviews.  The review was deliberately
narrow: it independently re-tested the two remaining Round-2 blockers, then
performed only the requested source-lock, scanner, runtime, and execution-order
regression checks.  No implementation code was changed.

The review remained pre-run.  I did not invoke
`code/scripts/run_static_audit.py`, build a result manifest, substitute the
inherited parameter, solve a candidate periodic equation, evaluate a candidate
action, access prime or Riemann-zero data, or make a network request.  Every
adversarial mutation was made in a system temporary directory and removed
after its check.

## Executive decision

Both Round-2 deployment blockers are closed:

1. R002 now requires one exact parsed JSON contract and one exact normalized
   instance of every tagged equation.  It rejects semantic dependency deletion,
   changed equations, duplicate IDs, duplicate tags, and non-whitespace control
   characters while retaining harmless layout invariance.
2. The manifest layer now enforces a flat exact allowlist, semantic validity of
   every required artifact, regular-file containment, and no duplicates or
   symlinks.  Every requested negative fixture fails and the exact legal
   fixture passes.

No new deployment blocker was found.  `DEPLOYMENT_PASS` authorizes only the
source-locked exact static audit described by the plan.  The candidate
periodic-orbit/action execution gate remains closed.

## Independent R002 reproductions

Baseline `proof_dependency_audit` on the repaired proof returned PASS with
proof-contract version 3, an exact nine-record contract, five uniquely tagged
equations, and no forbidden control character.  SHA-256 of the reviewed proof:

`c579e2da093a8ab588a5818bab0df59a47804792fcdfa338777f48e1bd1a1214`.

Each following result was independently reproduced on a temporary copy of
`notes/PROOF_PACKAGE.md`:

| Mutation/control | Expected | Observed |
|---|---|---|
| Delete `beta_zero_has_no_complex_logarithm` from `AC-HL-v3` | FAIL | FAIL: frozen structured contract mismatch |
| Add `+T_{untracked}` to the tagged gauge equation | FAIL | FAIL: exact normalized equation mismatch |
| Replace `AC-OBS-v3` by a second `AC-GAUGE-v3` | FAIL | FAIL: duplicate ID and frozen contract mismatch |
| Add a second `AC-GAUGE-v3` equation tag | FAIL | FAIL: tag count becomes two |
| Inject U+0008 into the proof contract | FAIL | FAIL: codepoint 8 reported and JSON rejected |
| Change only whitespace and add `left`/`right` layout commands to the gauge equation | PASS | PASS |

The structured JSON object is compared to the complete frozen in-code value,
including record order, kinds, IDs, and dependency lists.  Duplicate JSON keys
are rejected by the parser.  The tagged displays are compared after removing
only whitespace and explicitly enumerated TeX layout commands; an added term or
changed operator cannot survive this normalization.

## Independent manifest reproductions

The legal fixture contained exactly the seven required JSON records plus
`CODE_REVIEW.md`, `VALIDATION_REPORT.md`, `EXPERIMENT_RESULTS.md`, and
`pytest.xml`.  It passed semantic validation, and all eleven declared result
inputs were selected.  A top-level regular
`results/final_result_manifest.json` was also confirmed to be an optional
output that remains excluded from its own input set.

Independent temporary-fixture results:

| Mutation/control | Observed result |
|---|---|
| Add top-level `results/unexpected.json` | FAIL with exact unknown path |
| Add nested `results/nested/unknown.txt` | FAIL as nested and unknown |
| Add `results/duplicate/run_summary.json` | FAIL as nested, unknown, and duplicate basename |
| Replace required `run_summary.json` with an in-root symlink | FAIL as a symlink and invalid semantic input |
| Add a result symlink resolving outside the project root | FAIL as symlink, unknown, and outside-root path |
| Remove `VALIDATION_REPORT.md` | FAIL as missing required artifact |
| Leave the flat schema intact but make the final review verdict `DEPLOYMENT_FAIL` | FAIL at the `CODE_REVIEW.md` semantic gate |
| Exact legal flat schema | PASS |
| Exact legal schema plus optional top-level final manifest | PASS; final manifest excluded from inputs |

Thus an extra, nested, same-basename, symlinked, outside-root, missing,
unknown, or semantically stale result cannot receive manifest authority.

## Safe regression evidence

- Source-lock v3 validation: PASS.
- Source-lock SHA-256:
  `d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7`.
- Pre-lock candidate exact/numerical runs, periodic points, actions, prime
  tables, and zero data: all zero/false.
- Executable-isolation scan: PASS; all eleven executable Python files were
  covered, including `action_audit/protocol.py` and both script wrappers; zero
  findings.
- Syntax compilation: PASS.
- Full safe unit suite: **82 passed in 1.25 s**.
- Isolated Round-3 JUnit SHA-256:
  `938186e4112fe679f3fa4539a6aae1ffb245b0fbff01a9780376c23e6d6903e7`.
- Runtime record: actual UTC date from `datetime.now(timezone.utc)`, timestamp
  ending in `Z`, and frozen document dates explicitly distinguished from
  runtime metadata.
- Static source order: R000 source lock, R001 executable isolation, R002 proof
  contract, R010--R019 controls, then R020--R023 Hénon static identities.
  Controls therefore precede every Hénon check.
- Executable surface: no candidate periodic-orbit solver, inherited-parameter
  substitution, candidate action evaluation, prime/zero reader, network call,
  or approximate logarithmic matcher found.

## Final deployment decision

DEPLOYMENT_PASS

The repaired implementation is ready for its registered source-locked static
audit and subsequent exact-manifest build.  This decision does not authorize a
candidate orbit/action computation and does not change any mathematical claim
or source-lock prediction.
