# Independent Pre-Execution Code Review — Round 1

Review date: 2026-08-14 UTC.

Verdict: **DEPLOYMENT FAIL**.

This review is bound to:

- candidate: `cat_prime_shell_multiplicity_obstruction_v1`;
- source-lock SHA-256:
  `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49`;
- reviewed code/design-tree SHA-256:
  `ff360e9c42d304fbac36fafcc7a977758b3c6fa0e011aadd2522f8185ae86bbe`;
- frozen pre-execution JUnit SHA-256:
  `7b0581287e4525639602c23c95fda7fc97208353ee994b93a6a0120377e4bc92`.

The reviewer was independent of implementation authoring.  No registered
command, candidate entry point, result-manifest command, network operation,
external prime table, generated prime array, Riemann-zero source, numerical
value of `s` or `log(p)`, composite-shell enumeration, or centralizer
calculation was invoked.  No live claim, result, or terminal artifact was
created.  The live registered exact-audit count remains zero.

## Checks that passed

- The live source lock, independent source review, all six local design
  bindings, and all six Paper-8 upstream bindings reproduce their frozen
  hashes.  Safe preflight collected read-only reports `pass: true`, remains
  `READY_FOR_INDEPENDENT_DEPLOYMENT_REVIEW`, records zero registered audits,
  and does not import `prime_shell.candidate`.
- The exact closed inventory reproduces the reviewed tree digest.  It has no
  symlink, hardlink, bytecode, cache directory, missing source, extra source,
  or nested unsupported entry.  An isolated symlink replacement is rejected
  with `CODE_FILES_MISSING` and `CODE_SYMLINKS_FORBIDDEN`; restoring the exact
  file restores a clean scan.
- Sixteen candidate-free tests were freshly run with bytecode and pytest
  cache generation disabled and all passed.  The frozen author-side JUnit
  reports 17 tests, zero failures/errors/skips, and the eight required test
  names; its candidate-contract test was deliberately not rerun in this
  independent review.
- A separate exact integer enumeration reproduced the five frozen rows:
  `p=2:{3:3}` with one length-3 cycle;
  `p=3:{4:8}` with two length-4 cycles;
  `p=5:{2:4,10:20}` with two cycles at each length;
  `p=7:{8:48}` with six length-8 cycles; and
  `p=11:{5:120}` with 24 length-5 cycles, four on eigenlines and twenty off
  eigenlines.  The analytic split/inert/Jordan certificates and the direct
  permutation engine agree with the frozen ledger on every projected field.
- The raw-return factors preserve primitive lengths, including the mixed
  modulo-five factor, while the orbit-label factors have degree `m_p` and
  repeat coefficient `m_p/r`.  Independently recomputed label coefficients
  for repeats 1--3 are respectively
  `(1,1/2,1/3)`, `(2,1,2/3)`, `(4,2,4/3)`, `(6,3,2)`, and
  `(24,12,8)` across the five shells.
- Exact equal-weight power sums are `m_p^(1-r)`; they repair only the first
  repeat when `m_p>1`.  The fractional outer exponents sum exactly to one in
  every shell, retain the `GLOBAL_NORMALIZED_COUNTING` label, and the symbolic
  composite control never chooses or enumerates a value of `q`.  The global
  convergence statements remain proof-only and preserve the declared gap
  for `2 < Re(s) <= 3`.
- Strict JSON rejects duplicate keys, nonfinite constants, and floats.
  Deployment-authority parsing requires one column-one prefix, exact keys,
  canonical JSON, exact Python types, and exact source/tree/test hashes.  The
  fixed CLI exposes no scientific parameter and derives the project root from
  its own file rather than the caller's working directory.
- The lifecycle's ordinary concurrency guard is directionally correct:
  the pre-run result inventory is exact, the claim uses `O_EXCL`, a second
  claim is rejected, candidate import occurs only after a validated review
  and claim, and the reviewed tree is rehashed after execution.  The result
  and final-manifest inventories also reject missing, extra, link, and unsafe
  entries.  The durability defect below nevertheless prevents authorizing
  the lifecycle as advertised.

## Reproducible deployment blockers

### B1 — aliases, capability storage, and dynamic imports bypass the executable-isolation gate

`executable_isolation_scan` checks only an import's root and the final
syntactic name at each `Call`.  It performs no provenance propagation through
import aliases, assignments, containers, subscripts, `getattr`,
`sys.modules`, or `__import__`.  Its network/data-loader counters are literal
zeros rather than quantities derived from findings.

In an isolated complete copy containing the exact expected code inventory,
replacing only the temporary `prime_shell/candidate.py` with this inert body
produces `pass: true`, `errors: []`, a passing candidate-file record,
`network_modules_imported: 0`, and `external_data_loaders: 0`:

```python
import os as allowed_os

def latent_capabilities():
    imported_alias = allowed_os.system
    capability_box = {"run": imported_alias}
    capability_alias = capability_box["run"]
    capability_alias("true")
    dynamic_alias = getattr(allowed_os, "system")
    dynamic_alias("true")
    dynamic_module = __import__("socket")
    dynamic_module.socket()
```

Nothing in this reproduction is executed; the production scanner is called
only on the temporary AST.  The bypass is still decisive because the P2 gate
claims to rule out network modules, external loaders, and forbidden OS
capabilities.  The current scanner can certify all three while reporting
fabricated zero counters.  Exact tree hashing makes later edits stale, but it
does not make a false scanner result true and cannot substitute for the
source-locked mechanical isolation gate.

Minimum repair: use conservative value/provenance flow for import aliases,
assignment chains, literal containers/subscripts, dynamic attribute access,
module tables, and dynamic imports; reject unresolved dynamic callable
invocation on capability-bearing objects; cover path read/load APIs as well
as network/process APIs; and compute every reported counter from actual
findings.  Add mandatory regressions for direct, assigned, container-laundered,
`getattr`, `sys.modules`, and `__import__` variants plus legal controls.

### B2 — the registered-result semantic validator accepts a structurally false result

`validate_registered_result` checks only the top-level key set.  Inside the
audit it applies `len(...)` to an untyped `rows` value, compares counters with
`0` without excluding booleans, never requires an exact audit key set or the
control/classification fields, and accepts an empty pre-execution gate mapping
because `all([])` is true.

The following isolated reproduction uses a full exact project copy and a
temporary claim only; it does not touch the live lifecycle.  Supplying an
in-memory payload with the correct top-level scalar bindings but with:

```python
pre_execution_gates = {}
independent_review_gate = {"pass": True}
audit = {
    "pass": True,
    "locked_primes": [2, 3, 5, 7, 11],
    "rows": "abcde",
    "terminal_labels": list(TERMINAL_LABELS),
    "numeric_s_or_log_evaluations": False,
    "centralizer_computations_run": False,
    "composite_shells_enumerated": False,
    "proof_only_contract": proof_only_contract(),
}
```

returns exactly
`{"stage":"R090_REGISTERED_RESULT_SEMANTICS","errors":[],"pass":true}`
up to ordinary pretty-print spacing.  Here a five-character string impersonates
five scientific rows, `False` impersonates integer zero, every B1--B4 control
and the classification are absent, and no named P0--P3 gate exists.

Minimum repair: validate exact schemas recursively.  Require `rows` to be a
five-element list in frozen prime order; validate every row, both engine
projections, frozen-ledger match, raw/label/repeat/mechanism record, proof-only
boundary, counter type, control key/value, classification, and terminal label.
Require the exact named pre-execution gates and the exact deployment-review
authority record rather than arbitrary dictionaries containing `pass: true`.
Use `type(value) is int` before integer comparison so booleans cannot pass.
Add negative tests for wrong containers, empty gate maps, bool-as-zero,
missing/extra nested keys, reordered/duplicated rows, and omitted controls.

### B3 — the supposedly durable one-shot claim is not directory-durable

The exclusive writer calls `fsync` on the newly created file and returns
without syncing its parent directory.  The replace path likewise syncs the
temporary file but not the directory after `os.replace`.  File-content
durability does not guarantee persistence of a newly created or renamed
directory entry across a crash.  A crash at that boundary can therefore lose
the `STARTED` claim that is supposed to make the official audit one-shot.

Minimum repair: open the already validated parent directory and `fsync` it
after every exclusive creation and atomic rename, preserving `O_EXCL`,
`O_NOFOLLOW`, single-link checks, and cleanup behavior.  Add a storage-order
regression or a mock-based call-order test.  This repair should accompany the
existing exact inventory and concurrency tests, which otherwise behave
fail-closed under ordinary competing processes.

## Decision

No deployment authority is issued.  Registered execution must remain locked
until B1--B3 are repaired, the safe suite plus the new adversarial regressions
pass, and a fresh independent reviewer binds the new source/tree/JUnit hashes.
The repairs do not require changing the frozen matrix, primes, repeats,
expected ledger, theorem scope, product definitions, analytic nonclaims, or
Paper-10 centralizer reservation.

PRIME_SHELL_CODE_REVIEW_V1 {"candidate_id":"cat_prime_shell_multiplicity_obstruction_v1","reviewed_code_sha256":"ff360e9c42d304fbac36fafcc7a977758b3c6fa0e011aadd2522f8185ae86bbe","reviewer_independent":true,"source_lock_sha256":"662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49","test_evidence_sha256":"7b0581287e4525639602c23c95fda7fc97208353ee994b93a6a0120377e4bc92","verdict":"FAIL"}

# Independent Pre-Execution Code Review — Round 2

Review date: 2026-08-14 UTC.

Verdict: **DEPLOYMENT FAIL**.

This fresh review is bound to:

- candidate: `cat_prime_shell_multiplicity_obstruction_v1`;
- source-lock SHA-256:
  `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49`;
- reviewed code/design-tree SHA-256:
  `60f53f04c9ab4c0ee036ceba59b3ee678016902ff40b538e9922719a939bc228`;
- frozen pre-execution JUnit SHA-256:
  `dd654b54cc68403234686292aa51dcbd063e025badc893f373222997c74da515`;
- byte-exact Round-1 history size and SHA-256:
  `10004` bytes and
  `77b9cc4b892e0395006d1e058ea065db8b5eae8c829be361ee013b8f469201c0`.

The reviewer was independent of the repair implementation.  No live
registered command, result-manifest command, network operation, external
prime table, generated prime array, Riemann-zero source, numerical value of
`s` or `log(p)`, composite-shell enumeration, or centralizer calculation was
invoked.  All executable attacks and fresh tests described below ran only in
isolated complete copies.  No live claim, result, or terminal artifact was
created; the live registered exact-audit count remains zero.

## Frozen bindings and checks that passed

- The source lock, independent source review, six local design files, and six
  Paper-8 upstream files reproduce their frozen hashes.  The exact inventory
  has no missing or extra source, link, bytecode, cache, or unsupported entry,
  and the framed tree hash reproduces the value above.  The first 10004 bytes
  of this review file remain byte-for-byte the Round-1 failure history.
- The supplied JUnit is well formed and records 20 tests with zero failures,
  errors, or skips.  A fresh isolated invocation with bytecode and pytest
  cache generation disabled independently passed all 20 tests.  The live safe
  preflight remains candidate-free, reports `pass: true`, is
  `READY_FOR_INDEPENDENT_DEPLOYMENT_REVIEW`, and records zero registered runs.
- The repaired scanner rejects the stated ordinary direct, import-alias,
  assignment, literal-container/subscript, `getattr`, `sys.modules`,
  `__import__`, unresolved-call, builtin-`open`, and `Path.read_text` attacks.
  Its network, process, dynamic, and data-loader counters are nonzero for the
  corresponding isolated findings, and the unmodified legal tree passes.
  The stronger bypasses below nevertheless show that provenance isolation is
  not closed.
- The audit-payload validator rejects a string or empty row container,
  boolean-as-zero counters, missing and extra audit/row/direct/analytic keys,
  reordered and duplicated rows, a false cycle action or partition, changed
  product and mechanism records, empty or extra controls, changed
  classification, changed proof or proof-validation records, a selected
  composite `q`, and duplicated terminal labels.  The exact generated audit
  produces no semantic error.  The separate official-gate defect below is the
  remaining Round-1 B2 blocker.
- A separate integer implementation, not importing the candidate package,
  reproduced exactly: `p=2:{3:3}` and one length-3 cycle;
  `p=3:{4:8}` and two length-4 cycles; `p=5:{2:4,10:20}` and two cycles of
  each length; `p=7:{8:48}` and six length-8 cycles; and `p=11:{5:120}` and
  24 length-5 cycles, split into four eigenline and twenty off-eigenline
  cycles.  Matrix orders are respectively 3, 4, 10, 8, and 5.
- The independent formal ledger gives orbit-label coefficients
  `(1,1/2,1/3)`, `(2,1,2/3)`, `(4,2,4/3)`, `(6,3,2)`, and `(24,12,8)` at
  repeats 1--3.  Equal-weight power sums are `m_p^(1-r)`; fractional orbit
  masses sum exactly to one; and retaining a single factor needs respectively
  0, 1, 3, 5, and 23 zero weights.  Raw-return lengths remain distinct from
  orbit labels, especially at the mixed modulo-five row.
- The code remains restricted to `p=(2,3,5,7,11)` and formal repeats
  `(1,2,3)`.  The global convergence statements are schema-bound proof-only
  claims, the gap `2 < Re(s) <= 3` is unclaimed, symbolic `q` has no selected
  value, and centralizer, transfer, quantum, numerical-`s`/`log`, zero-data,
  network, and search work remain outside execution.
- Round-1 B3 is repaired.  Both exclusive creation and atomic replacement
  execute file `fsync` followed by parent-directory `fsync`; static call-site
  inspection confirms that claim, result, and terminal writes all use the
  exclusive path.  The isolated call-order regression observes
  `[file, directory]` for each writer mode, while `O_EXCL`, `O_NOFOLLOW`,
  single-link validation, exact result inventory, and one-shot rejection are
  retained.

## Reproducible deployment blockers

### B1R2 — exact-import dunder access still bypasses executable isolation

The repair detects the particular Round-1 examples syntactically, but it
still performs no conservative value/provenance propagation.  Attribute
names are compared with finite forbidden-name sets, and a later call through
an ordinary name is trusted.  Three isolated complete-tree mutations preserve
the exact expected import signatures and each returns the global scanner
record

```text
pass: true
errors: []
network_modules_imported: 0
external_data_loaders: 0
process_capabilities: 0
dynamic_capabilities: 0
```

The first appends to `prime_shell/protocol.py`, which already has the exact
allowed `import os` signature:

```python
def latent_process_bypass():
    runner = os.__getattribute__("system")
    return runner("true")
```

The second requires no import change and appends to
`prime_shell/candidate.py`:

```python
def latent_network_bypass():
    loader = __builtins__.__getitem__("__import__")
    module = loader("socket")
    constructor = module.__getattribute__("socket")
    return constructor()
```

The third appends to `prime_shell/cli.py`, which already has the exact allowed
`Path` import:

```python
def latent_path_bypass():
    target = Path("outside")
    loader = target.__getattribute__("read_text")
    return loader()
```

Nothing in these reproductions is executed; only the temporary AST is
scanned.  They nevertheless falsify the P2 gate's claimed mechanical
exclusion of process, network, dynamic-import, and external-loader
capabilities.  Exact hashing makes an unreviewed mutation stale, but it does
not make the scanner's `pass: true` statement sound and does not satisfy the
Round-1 requirement for conservative capability provenance.

There is also a directly reproducible counter defect.  Appending the
import-preserving assignment `FLOAT_SENTINEL = 1.25` produces the file error
`FLOAT:FLOAT_LITERAL:<line>` and global `pass: false`, but still reports
`floating_literals: 0`.  The aggregation tests `startswith("FLOAT_LITERAL")`
against records whose actual prefix is `FLOAT:`.  Thus not every published
counter is derived correctly from its findings.

Minimum repair: either implement conservative provenance across attribute
resolution, assignments, containers/subscripts, and later name calls, or
fail closed on dunder attribute/call access and other unresolved capability
production.  In particular, ban or resolve `__getattribute__`,
`__getitem__`-based builtin access, and aliases returned by such calls.
Correct the floating-finding aggregation.  Add separate exact-import
regressions for all three bypasses and a positive-count float regression;
the regression must assert category counters, not merely `pass: false`.

### B2R2 — hollow official gate records still certify a false result

`validate_registered_result` requires the five official gate names and
checks only that each associated object has `pass is True`.  It then compares
the result's embedded gates with that same official mapping.  It neither
validates the five recursive gate schemas nor compares them with fresh
side-effect-free recomputations.

The following was reproduced with the actual functions in an isolated
complete project copy, not by replacing the validator.  First a hash-correct
temporary deployment authority was added, the genuine authorized preflight
was collected, a temporary one-shot claim was created, and the exact legal
candidate audit was constructed.  The legal result returned `errors: []` and
`pass: true`.  Then every official gate record was replaced by

```python
{name: {"pass": True} for name in PREEXECUTION_GATE_KEYS}
```

and those same hollow records were embedded in the result.  The temporary
claim's preflight hash was kept consistent, so `validate_claim` itself still
passed.  The semantically false result again returned exactly

```text
{"stage":"R090_REGISTERED_RESULT_SEMANTICS","errors":[],"pass":true}
```

Every source-binding record, upstream-binding record, executable-isolation
record and derived counter, source proof contract, JUnit totals and required
test names disappeared.  This violates the requested exact recursive
official-gate contract and leaves the registered result unable to establish
which P0--P3 evidence actually passed.

Minimum repair: validate exact recursive schemas for all five official gates
or compare their canonical payloads with fresh side-effect-free calls to
`validate_source_and_design`, `validate_upstream`,
`executable_isolation_scan`, `source_schema_contract`, and `parse_junit`.
Keep the existing exact live deployment-review comparison.  Add negative
tests for pass-only gate objects, missing/extra nested gate keys, mutated
records/counters/test names, and wrong containers, plus a legal full-gate
control.

## Decision

Round-1 B3 and most of B1/B2 are materially improved, but B1R2 and B2R2 are
deployment blockers.  No `PRIME_SHELL_CODE_REVIEW_V2` deployment authority is
issued.  Registered execution must remain locked until both repairs are made,
the adversarial suite is expanded and passes, a new framed tree and JUnit are
frozen, and a fresh independent review binds those new hashes while retaining
the byte-exact Round-1 and Round-2 failure history.

PRIME_SHELL_CODE_REVIEW_ROUND2_FAIL {"candidate_id":"cat_prime_shell_multiplicity_obstruction_v1","review_round":2,"reviewed_code_sha256":"60f53f04c9ab4c0ee036ceba59b3ee678016902ff40b538e9922719a939bc228","reviewer_independent":true,"round1_review_sha256":"77b9cc4b892e0395006d1e058ea065db8b5eae8c829be361ee013b8f469201c0","source_lock_sha256":"662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49","test_evidence_sha256":"dd654b54cc68403234686292aa51dcbd063e025badc893f373222997c74da515","verdict":"FAIL"}

# Independent Pre-Execution Code Review — Round 3

Review date: 2026-08-14 UTC.

Verdict: **DEPLOYMENT FAIL**.

This fresh deployment review is bound to:

- candidate: `cat_prime_shell_multiplicity_obstruction_v1`;
- source-lock SHA-256:
  `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49`;
- reviewed code/design-tree SHA-256:
  `b078ade2e2ecb66c99760f6871d73d812eaf796beac86a7319e9ed47b965d358`;
- frozen pre-execution JUnit SHA-256:
  `ee46ad6ca672b8cf30140ea84734935b6eda5c77d89ca0868640d08f10de6a95`;
- byte-exact Round-1 history: first `10004` bytes, SHA-256
  `77b9cc4b892e0395006d1e058ea065db8b5eae8c829be361ee013b8f469201c0`;
- byte-exact Round-1-plus-Round-2 history: first `20427` bytes, SHA-256
  `0647a31103b55d55ce901c150cb9b72230ea35541e04af14e539ce9e2ef92db5`.

The reviewer was independent of implementation and repair authoring.  The
source lock, proof package, experiment plan and tracker, independent source
review, all implementation files, all tests, and both prior failure reports
were read.  No registered command, candidate function, result-manifest
command, network operation, external dataset, numerical value of `s` or
`log(p)`, composite-shell enumeration, or centralizer computation was run.
All adversarial mutations were made only in a temporary complete code-tree
copy and were scanned as inert AST; the appended process and data-loader
functions below were never imported or called.  No live claim, result, or
terminal artifact was created.  The live registered exact-audit count remains
zero.

## Frozen bindings and repaired findings

- The frozen inventory and framed tree digest reproduce exactly.  The code
  tree has no extra or missing source, symlink, hardlink, cache, bytecode, or
  unsupported nested entry.  The supplied JUnit is well formed and records
  22 tests with no failure, error, or skip.  Six candidate-free protocol
  security tests were also rerun independently with bytecode and pytest-cache
  generation disabled; all six passed.
- The Round-1 and Round-2 named alias/container, `getattr`, `sys.modules`,
  `__import__`, `__builtins__`, dunder-resolution, `Path.read_text`, and float
  literal regressions now reject their frozen attacks and publish nonzero
  counters in the implicated categories.  Thus B1R2's exact three bypasses
  and float aggregation defect are repaired as written.  The new bypass
  below shows that the broader process/data isolation claim is still open.
- B2R2's hollow-gate defect is repaired as written.  The official preflight
  payload is compared byte-canonically with a fresh side-effect-free
  `collect_safe_preflight` result.  A read-only live comparison returned
  `official_equals_fresh: true`, `fresh_pass: true`, the exact five gate
  names, and status `READY_FOR_INDEPENDENT_DEPLOYMENT_REVIEW`; consequently a
  pass-only replacement cannot match the official full payload.  Recursive
  registered-result validation also retains exact audit, row, engine,
  control, proof-boundary, counter-type, classification, and terminal-label
  checks.
- Round-1 B3 remains repaired.  The candidate-free storage regression
  observes file `fsync` followed by parent-directory `fsync` for both
  exclusive creation and atomic replacement.  The claim remains exclusive,
  hash-bound, and one-shot, and the candidate import is correctly delayed
  until after preflight, durable claim creation, and immediate claim
  validation.
- Static and test inspection found no drift in the frozen scientific scope:
  the only matrix is `((2,1),(1,1))`, primes are `(2,3,5,7,11)`, repeats are
  `(1,2,3)`, raw-return and orbit-label records remain distinct, the
  fractional identity is exact, composite `q` is symbolic only, global
  convergence remains proof-only, and centralizer/transfer/matrix/numerator
  escapes are not run or closed.

## Reproducible deployment blocker

### B1R3 — exact-import process and arbitrary-file APIs still bypass P2

The scanner still classifies capabilities by a finite set of final attribute
spellings rather than by the provenance and API family of an allowed module.
In particular, `PROCESS_ATTRIBUTES` contains the spelling `spawn`, but not
Python's actual `os.spawnl` family.  Separately, every `.open` and `.read`
attribute is exempted when it appears in `prime_shell/protocol.py`, although
that file's legitimate low-level reads are meant to be restricted to
hash-bound project evidence.

In a complete isolated copy of the frozen tree, appending only the following
inert definitions to `prime_shell/protocol.py` preserves the exact import
signature (`import os`) and the exact closed file inventory:

```python
def round3_latent_process_bypass() -> int:
    return os.spawnl(os.P_WAIT, "/bin/true", "true")


def round3_latent_external_read_bypass() -> bytes:
    descriptor = os.open("/outside-source-lock", os.O_RDONLY)
    return os.read(descriptor, 1)
```

Neither function was executed.  Calling only the production scanner on that
temporary AST returned exactly:

```json
{"dynamic_capabilities":0,"errors":[],"external_data_loaders":0,"pass":true,"process_capabilities":0,"protocol_record":{"errors":[],"pass":true,"path":"prime_shell/protocol.py"}}
```

This is decisive because P2 claims mechanical exclusion of process
capabilities and external data loaders, not merely exclusion of the few API
spellings seen in earlier tests.  The result simultaneously certifies both
forbidden capabilities and publishes false zero counters.  Hash binding would
make this temporary mutation stale, but it cannot make the scanner's asserted
closed-world isolation true; the same argument was already established in
Rounds 1 and 2 for the narrower bypasses.

Minimum repair: resolve allowed-module aliases to module provenance and use
an exact allowlist of the `os` operations required by the reviewed protocol,
rather than an incomplete forbidden-name set.  In particular, reject every
spawn/process API family not explicitly required.  For file operations,
validate the called helper and path provenance against the frozen project
evidence/output roots; do not grant a whole-file exemption to `protocol.py`.
Add exact-import regressions for at least `os.spawnl` and an arbitrary-path
`os.open`/`os.read` chain, and require the process/data-loader counters to be
positive for the corresponding findings while the legal frozen tree remains
zero.

## Decision

No deployment authority is issued.  Registered execution must remain locked
until B1R3 is repaired, the new adversarial regressions and the complete safe
suite pass, a new tree and JUnit are frozen, and a fresh independent review is
bound to those hashes while retaining all three byte-exact failure histories.
No matrix, prime, repeat, expected ledger, theorem, product, analytic scope,
or Paper-10 boundary needs to change.

PRIME_SHELL_CODE_REVIEW_ROUND3_FAIL {"candidate_id":"cat_prime_shell_multiplicity_obstruction_v1","review_round":3,"reviewed_code_sha256":"b078ade2e2ecb66c99760f6871d73d812eaf796beac86a7319e9ed47b965d358","reviewer_independent":true,"round1_review_sha256":"77b9cc4b892e0395006d1e058ea065db8b5eae8c829be361ee013b8f469201c0","round2_review_sha256":"0647a31103b55d55ce901c150cb9b72230ea35541e04af14e539ce9e2ef92db5","source_lock_sha256":"662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49","test_evidence_sha256":"ee46ad6ca672b8cf30140ea84734935b6eda5c77d89ca0868640d08f10de6a95","verdict":"FAIL"}

# Independent Pre-Execution Code Review — Round 4

Review date: 2026-08-14 UTC.

Verdict: **DEPLOYMENT PASS**.

This fresh review is bound to:

- candidate: `cat_prime_shell_multiplicity_obstruction_v1`;
- source-lock SHA-256:
  `662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49`;
- reviewed code/design-tree SHA-256:
  `466fb64928ad5f8b5b4c2643d8875c98568bbbdaabd4abeb6f24cc7ba13ecddb`;
- frozen pre-execution JUnit SHA-256:
  `096dfff6203d48b22340e8def19bacca27294d383c1807f6856985fe99ff0cd8`;
- frozen safe-preflight SHA-256:
  `10cd0a1660c86f87de6661402a0acb37e3b5fcf9c9ce50ce5a4bfbad60360c4d`;
- byte-exact Round-1 history: first `10004` bytes, SHA-256
  `77b9cc4b892e0395006d1e058ea065db8b5eae8c829be361ee013b8f469201c0`;
- byte-exact Round-1-plus-Round-2 history: first `20427` bytes, SHA-256
  `0647a31103b55d55ce901c150cb9b72230ea35541e04af14e539ce9e2ef92db5`;
- byte-exact Round-1-through-Round-3 history: first `27854` bytes,
  SHA-256
  `775d05e002ce4cd1bc343cbca01f2b2db471c239442c9e0752500aafb6c55cff`.

## Reviewer independence and execution boundary

The reviewer authored the Paper-9 source-design package but did not author,
repair, or freeze the Paper-9 implementation, tests, JUnit, or preflight.
The review is therefore independent of code implementation and all four
repair rounds, while not being independent of the mathematical source
design.  That narrower boundary is sufficient for this implementation and
deployment audit and is disclosed rather than described as independent
scientific validation.

No registered command, result-manifest command, network operation, external
dataset, prime or zero table, numerical value of `s` or `log(p)`, composite
shell enumeration, centralizer computation, or scientific parameter search
was invoked.  Scanner attacks were inert source mutations in temporary
directories.  The complete exact unit suite was rerun without bytecode or
pytest-cache generation; these unit calls did not claim the registered
lifecycle or create live results.  The live result directory remained the
three-file pre-run inventory, and the live registered exact-audit count
remained zero throughout review.

## Frozen bindings and fresh evidence

- The source lock, independent source review, all six local design files, and
  all six Paper-8 upstream artifacts reproduce their frozen hashes.  The
  exact code inventory contains no missing or extra file, symlink, hardlink,
  bytecode, cache, unsupported directory, or nested entry.  Independent
  framed hashing before and after tests reproduced the reviewed tree digest.
- The frozen JUnit is well formed and records `23` tests with zero failures,
  errors, or skips and all fourteen required test names.  A fresh complete
  invocation independently passed all 23 tests in `2.15` seconds with
  `PYTHONDONTWRITEBYTECODE=1` and pytest cache disabled.  No cache or bytecode
  remained in the live tree.
- The frozen safe preflight reports `pass: true`, status
  `READY_FOR_INDEPENDENT_DEPLOYMENT_REVIEW`, the exact five gate names, zero
  network/process/dynamic/data-loader/float findings, the current tree and
  JUnit hashes, no deployment authority before this appended decision, and
  `registered_exact_audits: 0`.
- All three prior failure histories and their canonical failure authorities
  remain byte-exact at their frozen prefix boundaries.  Before this decision,
  no Round-4 deployment-authority prefix occurred.

## B1R3 closure: exact executable bodies and capability sites

The Round-4 scanner no longer treats an allowed module or the whole protocol
file as generally safe.  It combines three closed checks:

1. exact import signatures for every executable file;
2. location-free canonical AST-body SHA-256 values for every executable file,
   with the protocol digest excluding only the digest-map assignment needed
   to avoid a fixed point; and
3. exact multisets of reviewed `os`, bare-`os`, and filesystem-touching
   `Path` call sites, including lexical function, canonical target shape, and
   occurrence count.

The legal frozen tree reproduces every body and site signature with all
capability counters zero.  Independent inert mutations then reproduced the
following fail-closed behavior:

- appending `os.spawnl(os.P_WAIT, ...)` plus arbitrary-path
  `os.open`/`os.read` returned `pass: false`, with process count `1`, external
  loader count `2`, and dynamic count `3`; the protocol record named the
  unreviewed `spawnl`, `open`, and `read` sites and the body-digest mismatch;
- appending a wrapper call
  `stable_file_bytes(Path("/outside"))` returned `pass: false` through the
  exact executable-body digest even though it introduced no new direct
  low-level call site;
- rebinding `os` and later invoking an aliased `spawnl` returned
  `pass: false` through the body digest and the unreviewed bare-`os` site;
- an extra nominally approved `os.fsync` call is rejected by the exact site
  multiset, so adding an allowed spelling is not enough to bypass review.

The earlier direct/import-alias, assignment, container/subscript, `getattr`,
`sys.modules`, `__import__`, `__builtins__`, dunder-resolution,
`Path.read_text`, unresolved-call, builtin-`open`, and float-literal attacks
also remain rejected.  Their implicated category counters are derived from
the concrete finding records; the float regression now produces a positive
float count.  Thus Round-1 B1, B1R2, and B1R3 are closed for the reviewed
tree.  This authorization relies on the combined exact tree hash, body
signatures, site signatures, and deployment authority; it does not claim
that a simultaneously rewritten scanner policy and code tree could retain
this authority, because any such edit changes the reviewed tree hash.

## B2 closure: recursive result semantics and fresh gate equality

The result validator requires exact top-level, audit, row, direct-engine,
analytic-engine, product, mechanism, control, proof-boundary, counter,
classification, and terminal-label schemas.  It rejects booleans in integer
counter positions, wrong containers, missing or extra nested keys,
reordered or duplicated prime rows, noncanonical or invalid cycles, changed
product/mechanism records, a selected composite `q`, and incomplete controls.

Most importantly, the official preflight is no longer trusted because its
five named records merely contain `pass: true`.  At result validation it is
compared byte-canonically with a fresh side-effect-free
`collect_safe_preflight` recomputation, and the embedded gates and deployment
review must equal those fresh official records.  The legal full-gate fixture
passes; a pass-only hollow map fails with
`OFFICIAL_PREFLIGHT_NOT_LIVE_EXACT_RECOMPUTATION`.  Round-1 B2 and B2R2 are
therefore closed.

## B3 closure: durable one-shot lifecycle

Exclusive claim, result, and terminal creation retain `O_EXCL`, optional
`O_NOFOLLOW`, single-link validation, exact inventories, and immediate claim
revalidation.  Atomic replacement writes a same-directory exclusive
temporary file.  Both creation modes execute file `fsync`, close the file,
and then open and `fsync` the already validated parent directory.  The fresh
storage regression observed `[file, directory]` for both writer modes.
Candidate import remains delayed until after a passing fresh preflight,
hash-bound deployment authority, durable exclusive claim, and immediate
claim validation.  Round-1 B3 remains closed.

## Mathematical and scope/schema audit

- The only matrix is `((2,1),(1,1))`, the only prime tuple is
  `(2,3,5,7,11)`, and formal repeats are exactly `(1,2,3)`.  Unsupported
  moduli fail before enumeration.
- Both exact engines reproduce the frozen point and cycle profiles:
  one length-3 cycle at two; two length-4 cycles at three; two length-2 and
  two length-10 cycles at five; six length-8 cycles at seven; and twenty-four
  length-5 cycles at eleven, split into four eigenline and twenty off-line
  cycles.  Their canonical cycle partitions are disjoint and exhaustive.
- Raw-return factors retain primitive lengths, including the mixed
  modulo-five factor.  Orbit-label denominator degree is `m_p`, its repeat
  coefficient is the exact rational `m_p/r`, equal weights give
  `m_p^(1-r)`, and fractional orbit masses sum exactly to one.  The one-orbit
  record exposes the exact discard count rather than hiding selection.
- Composite `q` remains symbolic, with the Jordan-totient product explicitly
  over prime divisors.  No numerical `q`, `s`, or logarithm is accepted or
  emitted.
- All-prime and analytic statements remain proof-only.  The safe contracts
  are divergence/nonabsolute convergence only for
  `1 < Re(s) <= 2` and absolute convergence for `Re(s) > 3`; the gap
  `2 < Re(s) <= 3` remains unclaimed.  Centralizer, matrix-valued,
  numerator/alternating, transfer/Fredholm, cohomological, enriched-selector,
  zero, quantum, and Route-B paths remain outside execution and outside the
  certified scalar theorem.

## Decision and authority

All Round-1 through Round-3 blockers are closed in the tree bound above, the
complete safe suite passes, and no new deployment blocker was found.  This
Round-4 authority unlocks exactly one source-locked registered audit through
the production fail-closed lifecycle.  It does not authorize changes to the
matrix, prime tuple, repeat tuple, expected ledger, theorem, product
semantics, normalization, analytic scope, external-data policy, centralizer
reservation, or Route-B status.  Any change to the source, reviewed tree,
JUnit, authority line, or preserved failure-history prefixes makes the
authority stale and requires a new independent review.

PRIME_SHELL_CODE_REVIEW_V4 {"candidate_id":"cat_prime_shell_multiplicity_obstruction_v1","review_round":4,"reviewed_code_sha256":"466fb64928ad5f8b5b4c2643d8875c98568bbbdaabd4abeb6f24cc7ba13ecddb","reviewer_independent":true,"round1_review_sha256":"77b9cc4b892e0395006d1e058ea065db8b5eae8c829be361ee013b8f469201c0","round2_review_sha256":"0647a31103b55d55ce901c150cb9b72230ea35541e04af14e539ce9e2ef92db5","round3_review_sha256":"775d05e002ce4cd1bc343cbca01f2b2db471c239442c9e0752500aafb6c55cff","source_lock_sha256":"662809d40f7e409e439983774a36349b90f265616a488061fda3c5b9064c2d49","test_evidence_sha256":"096dfff6203d48b22340e8def19bacca27294d383c1807f6856985fe99ff0cd8","verdict":"DEPLOYMENT_PASS"}
