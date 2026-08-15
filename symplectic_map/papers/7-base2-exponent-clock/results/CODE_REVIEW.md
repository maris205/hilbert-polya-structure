BASE2_CLOCK_CODE_REVIEW_V1 {"candidate_id":"pcf_quadratic_exact_2adic_boundary_v1","reviewed_code_sha256":"bb648aa54d98b27df71ab849b7515312003d45898aefe9186f114739c1f3eb07","reviewer_independent":true,"source_lock_sha256":"205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1","verdict":"FAIL"}

# Independent pre-execution review

Verdict: `FAIL`; P4 must remain locked. I did not author the reviewed code,
did not run the registered candidate/P4, and did not access prime or zero
data. The authority above binds the only reviewed tree and source-lock hashes.

Baseline: the live lock, proof and four upstream hashes match; all 26 existing
tests pass; the exact-set radical/proper-divisor construction, formal/scheme
pollution accounting, squarefreeness/divisibility/invariance, Chebyshev
`Psi_2=X^2+X-1`, `B_2=-1`, `Lambda=-4`, the `z^2` positive/negative controls,
the degree-2/3 finite-field obstruction and degree-4 witness, and substantive
Paper-2 n=1--4 invariants were independently reproduced. These passes do not
close the following deployment blockers.

## Blocker 1: scanner and binding/tree symlink bypasses

Each isolated fixture below returned scanner `pass=True` with no finding:

- `import os as x; x.system("true")`
- `from os import system as x; x("true")`
- `getattr(builtins, "__import__")("socket")`
- `Path("prime_" + "table").read_text()`
- `convert=float; convert("0.125")`

Separately, adding `code/alias.py -> good.py` left the reviewed-tree digest
unchanged because `review_gate.py:49` resolves before deduplication; the
scanner also accepted the symlink. A fixture with all four upstream paths as
symlinks was reported `regular_nonsymlink_file=True` and passed because
`protocol.py:178` likewise resolves before checking.

Required fix: reject symlinks/path-component symlinks before resolution, hash
the original closed-world path inventory, track import/assignment aliases and
dynamic callable construction (or use a strict allowlist), inspect `Path`
receivers, and add all fixtures as fail-closed tests.

## Blocker 2: algebraic-field target hits are misclassified

For the noncandidate exact fixture over `QQ<u>`
`exact=(z-1)(z+u), B=z, target=1`, the engine produced gcd degree 1,
SymPy resultant `0`, rational field norm `0`, but `engines_agree=False`.
At `dynatomic.py:171`, SymPy `Zero` is compared to the domain's `ANP` zero and
compares unequal. The miss fixture at target 2 correctly gave gcd degree 0,
resultant `2+u`, norm `22`, and agreement true.

Consequently a real P4 hit would raise at `candidate.py:55` before the hit
branch at line 57, preventing the locked halt/extraction protocol.

Required fix: convert the resultant into its coefficient domain (or use a
representation-independent exact-zero predicate) before comparison, and add
`QQ<u>` hit/miss plus target-halt routing tests.

## Blocker 3: manifest and run lifecycle do not close evidence

A complete temporary package with six records whose `targets=[]`, empty
`pre_execution_gates`, a non-authority review file, JUnit
`failures="99"`, and wrong registry schema/candidate/result path was accepted
by `build_post_run_manifest()` with `pass=True` and no semantic errors.
Empty target and gate collections pass vacuously at `manifest.py:166-168` and
`:190-194`; review/JUnit are only hashed; several registry identity fields
are never checked.

The run is also not claimed atomically: `cli.py:33-59` checks only final files,
runs P4, then writes a constant `registered_run_count=1`. Concurrent entry,
failure before final writes, or rerun after `TARGET_HIT_HALT` can therefore
execute P4 more than once. The lower-level candidate entry rechecks only lock
and review, not the complete P0--P2 bundle.

Required fix: freeze exact nonempty nested result schemas and the exact
`{+1,-1}` target set; revalidate live source/upstream/review gates and parse a
passing JUnit document; validate every registry field; and atomically create
a durable lock/tree-bound `STARTED` ledger before candidate construction with
fail-closed terminal transitions and concurrent/interruption tests.

Any repair changes the tree and requires a new independent review. Until then,
the all-period equality remains `OPEN_FOR_N_GE_4` and this review authorizes no
candidate execution.

## Independent pre-execution review, Round 2

Review date: 2026-08-14 UTC. Verdict: `DEPLOYMENT_FAIL`; P4 remains locked.
I did not author the repaired code, did not execute the registered candidate,
did not evaluate any candidate period, and did not access prime tables,
Riemann-zero data, floating orbit matches, or network data.

### Frozen bindings and baseline

- Source-lock SHA-256:
  `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1`.
- Independently recomputed reviewed-tree SHA-256:
  `8716715b9449e2943bfbe1e0566c61d2271260cada2f23c6aa70c6b44d4e5b37`.
- The historical V1 authority occurs exactly once, remains bound to tree
  `bb648aa54d98b27df71ab849b7515312003d45898aefe9186f114739c1f3eb07`,
  and retains verdict `FAIL` unchanged.
- All 23 Python sources parse. All 34 safe tests pass in 2.03 seconds with
  0 failures, errors, or skips; the checked JUnit document contains all four
  required security-test names and passes the strict parser.
- A P0--P2 wrapper run from `/tmp`, with an empty environment except for the
  interpreter path, no external `PYTHONPATH`, and bytecode disabled, passed
  every safe gate, reported zero registered runs, and created no `pyc` or
  `__pycache__` object. Its expected status before this verdict was
  `READY_FOR_INDEPENDENT_PRE_EXECUTION_REVIEW`.

I read the v2 source lock, research question, novelty and proof packages,
source-lock audit, experiment plan and tracker, paper plan, complete V1 review,
author repair record, and the current implementation, wrappers, and tests.

### Round-1 blocker 1: partial closure, one new hard bypass

The repaired tree now fails closed on the original direct attacks and several
extensions: imported and assignment aliases of `os.system`, literal
tuple/dictionary subscript calls, dynamic `getattr`, direct `open`, direct
`os.execv`, a stored `Path.read_text` bound method, and `map(float, ...)`.
Closed-world inventory also rejects an added file symlink, directory symlink,
broken symlink, extra source, and extra directory. The reviewed hash rejects
the former symlink-deduplication attack. A deterministic parent-directory swap
during a held-descriptor read raised `RuntimeError` when the lexical path was
reopened, so the tested parent-swap TOCTOU attack fails closed.

However, the scanner does not propagate callable provenance through a named
tuple or dictionary followed by a subscript assignment. Each of the following
was installed separately as the exact allowed file `tests/test_algebra.py` in
a temporary copy of the complete reviewed tree. In every case the closed-world
inventory passed, the scan returned zero findings, and the full executable
isolation gate returned `pass=True`:

```python
import os
funcs = (os.system,)
run = funcs[0]
run("true")
```

```python
funcs = {"x": open}
run = funcs["x"]
run("artifact.txt")
```

```python
from pathlib import Path
funcs = (Path("prime_" + "table").read_text,)
reader = funcs[0]
reader()
```

The root cause is that `_IsolationVisitor.provenance()` resolves a subscript
only when its receiver is a literal `Tuple`, `List`, or `Dict`. The fixed-point
assignment pass records scalar aliases, strings, and paths, but not immutable
container contents; therefore `funcs[0]` and `funcs["x"]` lose the forbidden
provenance before the final name call.

This is a deployment blocker because it reopens process execution, direct
file access, and the exact forbidden-resource path that the source lock
requires the scanner to reject. Required repair: either propagate exact
tuple/list/dict provenance through named containers and constant subscripts to
a fixed point, or conservatively reject callable-bearing container aliases and
indirect named calls. The repair tests must exercise these three attacks
through `executable_isolation_scan()` on an otherwise exact closed-world tree,
not only through the visitor in isolation.

### Round-1 blocker 2: closed

The independent `QQ(u)` fixture
`exact=(z-1)(z+u), B=z` now behaves correctly. At target `1`, gcd degree is
one, the coefficient-domain resultant is exactly zero, its rational field norm
is zero, `hit=True`, and both engines agree. At target `2`, gcd degree is zero,
the resultant is nonzero, the field norm is `22`, `hit=False`, and both engines
agree.

A synthetic period certificate containing the exact hit serialized with
`status=PASS` and `hit=True`. Static control-flow inspection confirms that the
candidate loop checks engine status and then extracts hits, so the repaired
zero normalization no longer diverts a genuine hit into the disagreement
exception before the target-halt branch.

### Round-1 blocker 3: closed for the requested attacks

- Six exact-key records with empty target lists are rejected explicitly by
  `TARGETS_NOT_EXACTLY_TWO`; empty pre-execution gates are rejected.
- JUnit reports with nonzero failures, malformed XML, or missing required
  security tests are rejected.
- Duplicate-key JSON, malformed JSON, non-finite constants, and finite floats
  in official exact evidence fail closed.
- Inconsistent `QQ(u)` coefficient/expression serialization and inconsistent
  polynomial variable, leading coefficient, and basis/expression serialization
  are rejected.
- Claim mutations in schema, candidate id, success path, hit path, target set,
  and registered periods are all rejected by specific registry errors.
- A second one-shot claim raises `FileExistsError`. An interrupted claim plus
  immutable failed terminal is not a clean `STARTED` state and cannot be
  reclaimed. Two barrier-synchronized claim attempts produced exactly one
  success and one `FileExistsError`.
- A canonical temporary review text with exactly the historical V1 failure and
  one current independent Round-2 pass marker was accepted; duplicate current
  markers and V1-only text were rejected. The actual marker below is a failure,
  so it intentionally grants no deployment authority.

### Final Round-2 disposition

Tree binding, raw-path inventory, `QQ(u)` target semantics, strict nested
evidence, JUnit parsing, and one-shot lifecycle survive the requested attacks.
The named-container callable laundering above leaves executable isolation
fail-open. Any repair changes the reviewed tree and requires a fresh
independent review. No registered candidate execution is authorized, and the
scientific boundary remains `OPEN_FOR_N_GE_4`.

BASE2_CLOCK_CODE_REVIEW_V2 {"candidate_id":"pcf_quadratic_exact_2adic_boundary_v1","review_round":2,"reviewed_code_sha256":"8716715b9449e2943bfbe1e0566c61d2271260cada2f23c6aa70c6b44d4e5b37","reviewer_independent":true,"source_lock_sha256":"205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1","verdict":"DEPLOYMENT_FAIL"}

## Independent pre-execution review, Round 3

Review date: 2026-08-14 UTC. Verdict: `DEPLOYMENT_FAIL`; P4 remains locked.
I did not author the reviewed code, did not execute the registered candidate,
did not evaluate any candidate period, and did not access prime tables,
Riemann-zero data, floating orbit matches, or network data.

### Frozen bindings and regression baseline

- The source-lock SHA-256 is
  `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1`.
- The independently recomputed reviewed-tree SHA-256 is
  `dd346942647bdd74f2c435d5396a720950d6bed246e88686d15f898e18afe3f4`.
- The historical V1 authority occurs exactly once at column one, retains its
  original tree binding and `FAIL` verdict, and the historical V2 authority
  likewise occurs exactly once with its original tree binding and
  `DEPLOYMENT_FAIL` verdict.
- All 36 safe tests passed in 2.58 seconds with zero failures, errors, or
  skips. The strict JUnit parser independently accepted the 36-test report,
  including all five required security tests.
- A live P0--P2 safe-preflight wrapper run from `/tmp`, under an empty
  environment except for the interpreter path and with bytecode disabled,
  passed source lock, upstream bindings, executable isolation, proof contract,
  and controls. It reported zero registered runs, no candidate periods, and no
  prime, zero, or floating/approximate access. No `pyc` or `__pycache__` object
  was created. Before this verdict its expected status was
  `READY_FOR_INDEPENDENT_PRE_EXECUTION_REVIEW`.

### Round-2 named-container blocker: closed for the requested cases

Each of the three exact Round-2 attacks was replayed as the replacement for
the allowed `tests/test_algebra.py` in an otherwise complete 23-file
closed-world tree. Tuple-held `os.system`, dictionary-held `open`, and a
tuple-held `Path.read_text` bound method all preserved exact inventory but
were rejected by the executable scanner with
`forbidden_callable_storage`. List, set, nested-container, and multi-step
alias-chain variants were rejected the same way. A complete-tree positive
fixture using the legitimate predicate `type(value) is float` produced no
finding and passed, so the repair does not confuse a type object used for
exact type comparison with a stored or invoked conversion callable.

### Sole Round-3 blocker: callable capability flow remains incomplete

The repair enumerates direct storage sites and literal containers but does not
conservatively track the same forbidden callable through all Python value
producers. Each source below was separately installed as the exact allowed
`tests/test_algebra.py` in a complete closed-world tree. In every case the
inventory passed, the scanner returned no finding, and the executable
isolation gate returned `pass=True`.

Conditional-expression laundering:

```python
import os
run = os.system if True else len
run("true")
```

Lambda implicit-return laundering:

```python
import os
factory = lambda: os.system
run = factory()
run("true")
```

Function-default capture:

```python
import os

def invoke(run=os.system):
    run("true")

invoke()
```

The root cause is that `dangerous_value_provenance()` does not recurse through
an `IfExp`, a `Lambda` implicit return is not inspected like an explicit
`Return`, and `FunctionDef` defaults are not inspected as callable storage.
The later name calls therefore have no forbidden provenance. These are not
new capabilities: all three recover the same process-execution capability
that the source lock requires executable isolation to reject.

Required repair: define one conservative recursive forbidden-capability value
analysis and apply it uniformly to expression branches, lambda bodies,
function and keyword-only defaults, assignments, returns/yields, container
elements, and call arguments. Add these three sources as fail-closed tests of
`executable_isolation_scan()` on an otherwise exact complete tree, while
retaining the full-tree `type(value) is float` positive control.

### Other requested regressions remain closed

- For `QQ(u)` with `exact=(z-1)(z+u)` and `B=z`, target `1` has gcd degree
  one, coefficient-domain resultant zero of type `ANP`, rational norm zero,
  `hit=True`, and engine agreement. Target `2` has gcd degree zero, nonzero
  resultant, norm `22`, `hit=False`, and agreement. The candidate control flow
  tests certificate status before extracting hits, but an exact hit with these
  agreeing engines has passing status and therefore reaches the hit route.
- Strict evidence checks continued to reject empty/invalid period records,
  nonpassing JUnit, duplicate-key JSON, and inconsistent field-element and
  polynomial serialization. A two-thread claim replay produced exactly one
  success and one `FileExistsError`; an interrupted terminal made the claim
  non-clean, and a retry also raised `FileExistsError`.
- An in-memory canonical current-round pass marker was accepted only alongside
  the exact historical V1 and V2 failures; the live review correctly lacked
  current authority before this disposition.

The single capability-flow blocker above is sufficient to deny deployment.
No registered candidate execution is authorized, and the scientific boundary
remains `OPEN_FOR_N_GE_4`.

BASE2_CLOCK_CODE_REVIEW_V3 {"candidate_id":"pcf_quadratic_exact_2adic_boundary_v1","review_round":3,"reviewed_code_sha256":"dd346942647bdd74f2c435d5396a720950d6bed246e88686d15f898e18afe3f4","reviewer_independent":true,"source_lock_sha256":"205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1","verdict":"DEPLOYMENT_FAIL"}

## Independent pre-execution review, Round 4

Review date: 2026-08-14 UTC. Verdict: `DEPLOYMENT_PASS` for the frozen
registered protocol. I did not author the repair, did not run the registered
candidate or P4, did not evaluate a candidate period, and did not access prime
tables, Riemann-zero data, floating orbit matches, or network data. This review
was strictly limited to verifying the Round-3 repair and the requested safety
regressions; no new attack surface was introduced.

### Frozen bindings and historical authority

- Source-lock SHA-256:
  `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1`.
- Independently recomputed reviewed-tree SHA-256:
  `7a5ea42ea52d35bf4d6608b1175a43ab81ceaa9ed8fbfd0e35e183920dbdd27a`.
- The V1, V2, and V3 historical authority lines each occur exactly once at
  column one, retain their original tree and source-lock bindings, and retain
  their original failure verdicts. The current parser rejects any mutation of
  those historical bindings and accepted an in-memory canonical Round-4 pass
  marker bound to the current tree.

### Scanner repair verification

Every requested source was installed separately as the exact allowed
`tests/test_algebra.py` in an otherwise complete 23-file closed-world tree.
All dangerous fixtures retained `inventory.pass=True` but were rejected by
executable isolation with `forbidden_callable_storage`:

- the Round-3 `IfExp`, lambda implicit-return, and function-default captures
  of `os.system`;
- the historical named tuple and dictionary attacks, including stored
  `os.system`, `open`, and `Path.read_text`;
- list, set, nested-container, and multi-step alias-chain variants.

The complete-tree positive control containing
`return type(value) is float` retained exact inventory, produced zero
findings, and passed executable isolation. The live reviewed tree also passed
the scanner with zero forbidden-access findings.

### Safe regression results

- All 38 safe tests passed in 2.92 seconds with zero failures, errors, or
  skips. The strict JUnit parser accepted the independent 38-test report and
  found every required security test.
- A safe-preflight wrapper run from `/tmp` under an empty environment except
  for the interpreter path, with bytecode disabled and no external
  `PYTHONPATH`, passed source lock, upstream bindings, executable isolation,
  proof contract, and controls. It created no `pyc` or `__pycache__` object,
  reported zero registered runs and no registered periods, and reported no
  prime, zero, or floating/approximate access.
- In the independent `QQ(u)` fixture
  `exact=(z-1)(z+u), B=z`, target `1` had gcd degree one, coefficient-domain
  `ANP` resultant zero, rational norm zero, `hit=True`, and engine agreement.
  Target `2` had gcd degree zero, nonzero resultant, norm `22`, `hit=False`,
  and agreement. Static control-flow verification confirmed that an agreeing
  exact hit has passing certificate status and reaches the subsequent hit
  route rather than being intercepted as disagreement.
- Manifest and evidence regressions rejected empty/invalid period records,
  nonpassing JUnit, duplicate-key JSON, and inconsistent field-element and
  polynomial serialization. Two simultaneous one-shot claims produced exactly
  one success and one `FileExistsError`; an interrupted terminal made the
  claim non-clean, and a further claim attempt also raised `FileExistsError`.

All requested pre-execution checks pass for the exact frozen bindings below.
This authority permits only the already frozen registered protocol and makes
no claim about its unexecuted scientific outcome.

BASE2_CLOCK_CODE_REVIEW_V4 {"candidate_id":"pcf_quadratic_exact_2adic_boundary_v1","review_round":4,"reviewed_code_sha256":"7a5ea42ea52d35bf4d6608b1175a43ab81ceaa9ed8fbfd0e35e183920dbdd27a","reviewer_independent":true,"source_lock_sha256":"205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1","verdict":"DEPLOYMENT_PASS"}
