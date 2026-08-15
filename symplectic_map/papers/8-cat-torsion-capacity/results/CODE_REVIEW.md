# Independent Pre-Execution Code Review — Round 1

Review date: 2026-08-14 UTC.

Verdict: **DEPLOYMENT FAIL**.

This review is bound to:

- candidate: `cat_torsion_primitive_divisor_capacity_v1`;
- source lock SHA-256:
  `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce`;
- reviewed code-tree SHA-256:
  `3706691aa78e02001d95e7f76954feef897f4c988b3866b134896ccb90af976a`.

The reviewer was independent of implementation authoring.  No registered
command or candidate entry point was invoked.  No claim, result, terminal, or
manifest artifact was created.  No network, external prime table, generated
prime target array, zero data, floating matching, or period above twelve was
accessed.  The registered exact-audit count remains zero.

## Checks that passed

- The source-lock file reproduces the bound hash, parses under the strict
  exact-JSON loader, and all six local plus seven upstream bindings reproduce.
- The exact reviewed inventory reproduces the bound tree digest.  It contains
  no symlink, hardlink, extra source, bytecode, or cache artifact under
  `code/`.
- A fresh isolated run of all 21 tests passed with bytecode and pytest cache
  generation disabled.  The frozen JUnit evidence also reports 21 tests,
  zero failures/errors/skips, and all mandatory security test names.
- The safe preflight was called read-only in a fresh interpreter.  All six
  safe gates passed, `cat_torsion.candidate` was absent from `sys.modules`
  both before and after collection, and the report retained zero registered
  periods and zero registered audits.
- An independent exact engine reproduced all twelve determinant values and
  every finite-field period profile:
  `p=2:{3:3}`, `p=3:{4:8}`, `p=5:{2:4,10:20}`,
  `p=7:{8:48}`, `p=11:{5:120}`, `p=19:{9:360}`,
  `p=29:{7:840}`, and `p=199:{11:39600}`.  Independently, the modulo-five
  nilpotent has square zero, four nonzero kernel vectors, twenty period-ten
  vectors, and two period-ten cycles.
- The determinant recurrence/direct engines, locked factorization scope,
  first-appearance semantics, primitive-kernel exact-period bridge, exception
  set `{1,6,12}`, and nonprimitive period-ten repair agree with the frozen
  proof package.
- The positive/negative-trace theorem contract preserves all three parity
  branches.  In particular, `n = 2 (mod 4)` uses index `n/2`, with indices
  `7,9,11` assigned to the separately cited small-index theorem; the code
  performs no matrix/orbit tail calculation.
- The torsion/order, coprime perturbation, point-sum, repeat, and native
  monodromy records preserve the proved separation between a global order
  label and a period-only derivative multiplier.
- Strict JSON rejects duplicate keys, nonfinite constants, and finite floats;
  the command parser exposes no matrix, trace, prime, cutoff, factor, or
  period override; the review authority parser is canonical and stale-closed;
  and the claim/result lifecycle is one-shot and fail-closed on its tested
  paths.
- The existing regressions correctly reject direct/imported aliases, literal
  named containers holding forbidden callables, path-capability laundering,
  symlinks, hardlinks, and extra code files, while accepting the legal
  expression `type(value) is float`.

## Reproducible deployment blocker

### B1 — module-table laundering bypasses the closed-world scanner

The AST value-flow scanner does not track a module recovered through
`sys.modules`.  Consequently both of the following replacement bodies for
`code/cat_torsion/candidate.py` receive `pass: true` and an empty findings
list in an otherwise exact closed-world temporary copy of the reviewed tree:

```python
import sys
mod = sys.modules["os"]
run = mod.system
run("true")
```

```python
import sys
sys.modules["os"].system("true")
```

Reproduction procedure:

1. Copy exactly every path in `EXPECTED_CODE_FILES` and the bound
   `pyproject.toml` into an isolated temporary project.
2. Replace only the temporary `candidate.py` with either body above.
3. Call `executable_isolation_scan(temp_project / "code")`.
4. Observe `pass == True`, `forbidden_access_count == 0`, and
   `findings == []` for both variants.

This is a direct forbidden OS-capability bypass, not a speculative sandbox
extension.  The scanner allows `sys`, does not classify the `modules`
attribute as dynamic, and loses provenance at the subscript before the
`.system` attribute or its alias is called.  It therefore contradicts the
closed-world executable-isolation gate's intended fail-closed semantics.

Minimum repair direction: reject access to `sys.modules` (including aliased
and subscripted forms), or propagate module provenance through module-table
lookups and then apply the existing forbidden-OS capability rules.  Add both
direct and assigned-alias variants as mandatory regressions, while retaining
all current container/path/link and legal-float controls.  Any repair changes
the reviewed tree digest and requires a new independent review round.

## Decision

No deployment authority is issued in this round.  Registered execution must
remain locked until B1 is repaired, the full safe suite and attack regressions
pass on the new tree, and a new independent review binds that exact tree.

# Independent Pre-Execution Code Review — Round 2

Review date: 2026-08-14 UTC.

Verdict: **DEPLOYMENT PASS**.

This fresh independent review is bound to:

- candidate: `cat_torsion_primitive_divisor_capacity_v1`;
- source-lock SHA-256:
  `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce`;
- reviewed code-tree SHA-256:
  `b4441fb68ac42ab1649ee62037fb7cdf741aa9c09a0b0d5cffc4003697caa059`.

The complete Round 1 deployment-failure record above was preserved byte for
byte as the prefix of this file; its pre-append SHA-256 was
`30803e5ae1ee4d33c0b3dd0c927fa71ec8d1f88f6d312b14d38ec14cdc4c1b76`.
The Round 2 reviewer was independent of implementation authoring.  No
registered command or candidate entry point was invoked, and the candidate
module was absent from `sys.modules` before and after safe-preflight
collection.  No claim, result, terminal, or post-run manifest was created.
No network, external prime table, generated prime target array, zero data,
floating or approximate matching, or matrix/orbit computation above period
twelve was used.  The registered exact-audit count remains zero.

## Round 1 blocker replay

In a fresh full closed-world temporary copy containing exactly every path in
`EXPECTED_CODE_FILES` and the bound `pyproject.toml`, replacement of only
`candidate.py` by each of the following attack families was rejected:

- `mod = sys.modules["os"]`, followed by an assigned `mod.system` call;
- a direct `sys.modules["os"].system(...)` call;
- `import sys as registry`, followed by `table = registry.modules` and either
  an assigned or direct module-table capability call;
- an additional nested alias chain through `registry2` and `table`.

Every attack produced `pass: false` with
`forbidden_module_table_access: sys.modules`.  The legal control
`type(value) is float` still produced `pass: true` and zero findings, and the
restored temporary tree again passed with zero findings.  This closes Round
1 blocker B1 without weakening the legal-float control.

## Regression and integrity checks

- The source lock reproduced its bound digest under the strict exact-JSON
  loader.  All six local bindings and all seven upstream bindings were live
  and exact.
- The reviewed inventory reproduced the bound tree digest, scanned 23 Python
  files with zero findings, and contained no generated file, symlink,
  hardlink, missing path, extra path, or unsupported entry under `code/`.
- A fresh safe run of all 21 tests passed with bytecode and pytest cache
  generation disabled.  The frozen JUnit evidence independently reports 21
  tests and zero failures, errors, or skips, including all six mandatory
  security regressions.
- Safe-preflight collection passed all six P0--P2 gates and did not import
  `cat_torsion.candidate`.  Before this authority was appended it correctly
  remained `READY_FOR_INDEPENDENT_PRE_EXECUTION_REVIEW`; its counters were
  zero registered audits, no registered periods, and zero candidate numerical
  runs.
- An independent integer engine reproduced the determinant ledger
  `[-1,-5,-16,-45,-121,-320,-841,-2205,-5776,-15125,-39601,-103680]`,
  the locked factorizations, and first-appearance primitive-divisor semantics.
- Independent finite-field enumeration reproduced
  `p=2:{3:3}`, `p=3:{4:8}`, `p=5:{2:4,10:20}`,
  `p=7:{8:48}`, `p=11:{5:120}`, `p=19:{9:360}`,
  `p=29:{7:840}`, and `p=199:{11:39600}`.  The separate modulo-five
  check gave `N^2=0`, four nonzero kernel vectors, twenty period-ten points,
  and two period-ten cycles.
- The proof-only negative-trace parity audit retained the three required
  branches: odd `n` uses `2n`, multiples of four use `n`, and
  `n = 2 (mod 4)` uses `n/2`, with half-indices 7, 9, and 11 assigned to the
  separately cited small-index theorem.  No tail orbit was computed.
- Exact rational clock controls reproduced invariant torsion order, prime and
  composite order witnesses, coprime perturbation growth, point-sum scaling,
  repeat scaling, and point-order blindness of native monodromy.
- Review authority parsing remained canonical and stale-closed.  The fixed
  CLI exposed no scientific override; strict JSON, one-shot claim, terminal
  prefix, nested-manifest, link/path, and result-inventory regressions all
  passed.  The pre-authority result directory contained only the review,
  safe-preflight, and JUnit files, so no registered lifecycle had begun.

## Decision

The repaired tree satisfies the frozen pre-execution contract.  Deployment
authority is issued only for the single source-locked exact audit over periods
1 through 12.  It does not authorize any period extension, external
prime/zero comparison, floating match, transfer/Fredholm or quantization
experiment, Route-A layer A1--A4, or Route B.

CAT_TORSION_CODE_REVIEW_V1 {"candidate_id":"cat_torsion_primitive_divisor_capacity_v1","reviewed_code_sha256":"b4441fb68ac42ab1649ee62037fb7cdf741aa9c09a0b0d5cffc4003697caa059","reviewer_independent":true,"source_lock_sha256":"87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce","verdict":"DEPLOYMENT_PASS"}
