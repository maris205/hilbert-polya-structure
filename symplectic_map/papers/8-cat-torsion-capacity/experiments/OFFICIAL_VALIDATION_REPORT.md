# Official Validation Report

Date: 2026-08-14 UTC  
Candidate: `cat_torsion_primitive_divisor_capacity_v1`  
Validation mode: frozen-artifact analysis and read-only closure validation

## Final validation decision

`CERTIFIED_WITH_TRANSPARENT_POSTRUN_PROVENANCE_REPAIRS`

The registered exact audit completed once and its scientific payload passes
the frozen semantic contract.  The immutable execution chain, independent
execution authority, independent post-run analyzer authority, dual-tree
roles, distinct JUnit roles, source/upstream bindings, and final closed-world
manifest all validate.  No candidate rerun, numerical run, period extension,
external table access, or floating comparison was used during this analysis.

## Immutable execution chain

| Artifact or role | SHA-256 / value | Validation |
|---|---|---|
| Source lock | `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce` | exact and live |
| Execution code tree | `b4441fb68ac42ab1649ee62037fb7cdf741aa9c09a0b0d5cffc4003697caa059` | independently authorized |
| Execution review | `0fe0a5ba625cbbb88bd6ed6a8ff61389a916fd300127a244981fa4643ffa25a6` | canonical `DEPLOYMENT_PASS` |
| Pre-execution audit | `850cb7cd8eb3ca63dd4e54757e569a66e01f190db0980c8d9682f4931d711883` | claim-bound, all six gates pass |
| Registered claim | `14b06403bd5a23b533138ccec4962d74910e6e0242abfcf7ac5fe6b3a947a0ee` | unique `STARTED` claim |
| Raw experiment result | `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0` | semantic validation passes |
| Registered terminal | `b3a40e9db554ffdc9fe14b654d84f8e918f26fdb47025eb301337b3ecd5fa192` | `COMPLETED_CERTIFIED` |
| Execution post-run JUnit | `2a0844152eea6d9184d374a6e33c3c4be72fce8deb60296c77650027104348cc` | 21/21 pass |

The terminal links the raw result hash and claim hash, reports one registered
run, one registered exact audit, periods 1 through 12 started and completed,
zero numerical candidate runs, and no failure code.

## Source-lock and tracker handling

The frozen source lock explicitly binds
`experiments/EXPERIMENT_TRACKER.md` at
`b977106d20039a5de31db31969ead23829d4dab058d9c7f4c03b1b96e54748f9`.
It was therefore not edited.  Its TODO labels and zero-run disclosure are the
historical source-lock design state, not a mutable completion dashboard.

No `results/RESULT_ANALYSIS_TRACKER.md` was created because the V2 manifest
requires an exact final `results/` inventory; an added file would correctly
invalidate closure.  The two official P5 human reports live under
`experiments/`, outside the final result inventory and outside the source
lock's fixed local-binding list.

## Pre-execution authority history

The independent code review is intentionally history-preserving:

1. Round 1 issued `DEPLOYMENT FAIL` after reproducing a `sys.modules`
   laundering bypass in the closed-world AST scanner.  No candidate was run.
2. The implementation rejected direct and aliased module-table access and
   added regressions.
3. Round 2 replayed the attacks, observed the full safe suite passing, and
   issued the canonical `DEPLOYMENT_PASS` bound to execution tree
   `b4441fb6...a059` and the frozen source lock.

Only that Round 2 authority unlocked the fixed one-shot audit.  It did not
authorize period overrides, external prime/zero data, floating matching,
Route-A A1--A4, or Route B.

## Registered scientific validation

| Gate | Exact observation | Status |
|---|---|---|
| Determinant engines | direct powers equal recurrence for all twelve periods | pass |
| Factor ledger | all exact factorizations and first-appearance selections match the lock | pass |
| Finite-field profiles | eight support primes, 41,003 nonzero vectors, all counts exact | pass |
| Boundary classifier | no carrier at 1, 6, 12; nonprimitive period-ten carrier present | pass |
| Positive-trace theorem contract | norm/determinant and primitive-kernel hypotheses exact | pass |
| Negative-trace theorem contract | all three parity branches exact; no tail orbit computed | pass |
| Clock range | all positive integer orders, including composites | pass |
| Clock regularity | unbounded and discontinuous in every torsion neighborhood | pass |
| Orbit sum vs average | \(n\log p\) versus \(\log p\) kept distinct | pass |
| Native monodromy | depends on period only, not carrier order | pass |

The small ledger was development-seen literature reproduction, and the
modulo-two/three/five boundary statements were analytically derived before
lock.  The registered computation is therefore a deterministic
proof-falsification and consistency audit, not a blind discovery experiment.

## Theorem/computation firewall

- Exactly periods 1 through 12 were executed.
- `periods_above_twelve_computed=[]` and `tail_periods_computed=[]`.
- The proof-contract sample periods above twelve contain no matrix or orbit
  calculation.
- The all-period tail relies on the imported theorem and a separate parity
  proof, not extrapolation from the ledger.
- No external prime table, generated target array, Riemann-zero data,
  random search, floating matching, transfer/Fredholm construction, or
  quantization experiment entered the result.

## Post-run provenance repair history

The post-run path records two defects and their repairs without rewriting the
execution evidence.

### Repair 1: distinct JUnit roles and dual code trees

The claim-bound pre-execution JUnit record has SHA-256
`81ffc571c773cfa9a69f157559fdaa3611f55c748908c20183e4eae3f3420aa1`.
After the registered run, the execution-tree JUnit was refreshed and has
SHA-256
`2a0844152eea6d9184d374a6e33c3c4be72fce8deb60296c77650027104348cc`.
An initial manifest builder incorrectly treated that legitimate role change
as stale pre-execution evidence.

The repair validates the stored result gates against the immutable,
claim-bound pre-execution audit, while separately validating the current
post-run JUnit.  It also separates the immutable execution tree from the
non-executing analyzer tree.  No candidate or raw execution artifact was
changed or rerun.

### Repair 2: final post-write closure

Independent post-run analyzer Round 1 issued `POSTRUN_ANALYZER_FAIL` because
the pre-write builder did not provide a strict read-only validator for the
tree after `result_manifest.json` had been added.  The full Round 1 prefix is
pinned at SHA-256
`635e7dcd49440a41fd5f966c742b924f38428785ec21f4f7af549bca4f89f71b`.

The narrow repair introduced separate exact pre-write and final inventories,
where the final inventory is the pre-write inventory plus only
`result_manifest.json`.  It added a strict existing-manifest validator,
one-shot write semantics, immediate post-write closure, and isolated
changed/missing/extra/symlink/duplicate/malformed/type/semantic tamper
regressions.  The manifest records non-self hashes but deliberately omits an
impossible recursive self-hash.

Fresh independent Round 2 then issued `POSTRUN_ANALYZER_PASS`, bound to:

| Role | SHA-256 |
|---|---|
| Analyzer code tree | `1aadef8597a641f2fd4e29ec63202942291a22d2552fa966bdb79d771f860f34` |
| Analyzer JUnit, 27/27 pass | `fac25a2d332d68f6a2374b14f57d0f9dcacd5ea27c2c7581766b8c84d00499a0` |
| Post-run analyzer review | `42e4e2010be2d5cbb51a2ceb1fd9a1f8048bcec17daa2767c9f38cebaaa6fdcd` |

The execution and analyzer tree hashes are intentionally distinct.  The
analyzer tree has validation authority only and cannot authorize a candidate
rerun.

## Final manifest record

| Field | Value |
|---|---|
| Schema | `CAT_TORSION_RESULT_MANIFEST_V2_DUAL_TREE` |
| Manifest SHA-256 | `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f` |
| Recorded non-self files | 14 |
| Exact final `results/` entries | 11, including the manifest |
| Manifest errors | none |
| Manifest `pass` | `true` |
| Post-run audit status | `AUTHORIZED_FOR_POSTRUN_MANIFEST` |
| Candidate rerun performed | `false` |

## Final live read-only closure check

This section is finalized after both P5 reports are present.  The validator
invocation is read-only and does not call the registered candidate or test
suite.

- Closure stage: `R100_FINAL_POSTRUN_MANIFEST_CLOSURE`
- Closure pass: `true`
- Closure errors: none
- Observed manifest SHA-256:
  `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f`
- Observed final result inventory (exactly 11 entries):
  `AUTHOR_POSTRUN_REPAIR_NOT_INDEPENDENT.md`,
  `AUTHOR_POSTRUN_ROUND1_REPAIR_NOT_INDEPENDENT.md`, `CODE_REVIEW.md`,
  `EXPERIMENT_RESULTS.json`, `POSTRUN_ANALYZER_PYTEST.xml`,
  `POSTRUN_ANALYZER_REVIEW.md`, `PRE_EXECUTION_AUDIT.json`, `pytest.xml`,
  `registered_run.claim.json`, `registered_run.json`, and
  `result_manifest.json`.

## Classification and limits

| Field | Certified value |
|---|---|
| Scientific classification | `INTRINSIC_TORSION_CAPACITY_CERTIFIED_A0_FAIL_PROVES_TOO_MUCH` |
| Route A | `A0_FAIL_PROVES_TOO_MUCH_NO_A1_TO_A4` |
| Route B | `NOT_OPENED` |
| General carrier claim | proof-certified for every hyperbolic \(\mathrm{SL}_2(\mathbb Z)\) map and every \(n>12\) |
| Frozen cat claim | prime-order exact-period carrier iff \(n\notin\{1,6,12\}\) |
| Clock conclusion | all-integer capacity, non-specific, nonregular, native-monodromy blind |

This validation does not certify a prime-only clock, prime-orbit bijection,
prime/zero match, transfer determinant, zeta interpretation, quantization
claim, or any Route-A layer beyond the failed A0 gate.  No manuscript was
created or modified during P5 analysis.
