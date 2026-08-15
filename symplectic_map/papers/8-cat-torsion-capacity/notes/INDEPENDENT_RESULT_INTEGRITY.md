# Independent Final Result-Integrity Audit

Audit date: 2026-08-14 UTC  
Reviewer role: fresh independent result-integrity reviewer  
Verdict: **PASS — `PAPER8_RESULT_INTEGRITY_PASS`**

## Scope and non-execution statement

This was a read-only audit of the completed Paper 8 result package. I did not
invoke the registered candidate, rerun a test suite, modify code, source-locked
inputs, results, reviews, or the manifest, or access external prime tables,
generated prime targets, Riemann-zero data, or approximate matching data. The
only file created by this review is this report, outside `results/`.

## Frozen provenance

| Role | SHA-256 |
|---|---|
| source lock | `87d80da28cacb349c0e277b8f73812287eeb6f8a2e244945a05f90a2f6269dce` |
| final V2 result manifest | `045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f` |
| immutable execution tree | `b4441fb68ac42ab1649ee62037fb7cdf741aa9c09a0b0d5cffc4003697caa059` |
| execution authority | `0fe0a5ba625cbbb88bd6ed6a8ff61389a916fd300127a244981fa4643ffa25a6` |
| post-run analyzer tree | `1aadef8597a641f2fd4e29ec63202942291a22d2552fa966bdb79d771f860f34` |
| analyzer authority | `42e4e2010be2d5cbb51a2ceb1fd9a1f8048bcec17daa2767c9f38cebaaa6fdcd` |
| pre-execution audit | `850cb7cd8eb3ca63dd4e54757e569a66e01f190db0980c8d9682f4931d711883` |
| registered claim | `14b06403bd5a23b533138ccec4962d74910e6e0242abfcf7ac5fe6b3a947a0ee` |
| raw exact result | `0d8054ad36ad8cdef1496948cf5dd98d6a1a55c186d68124f45a5e6e35bddaa0` |
| registered terminal | `b3a40e9db554ffdc9fe14b654d84f8e918f26fdb47025eb301337b3ecd5fa192` |
| execution-tree post-run JUnit | `2a0844152eea6d9184d374a6e33c3c4be72fce8deb60296c77650027104348cc` |
| analyzer-tree JUnit | `fac25a2d332d68f6a2374b14f57d0f9dcacd5ea27c2c7581766b8c84d00499a0` |

The execution review contains exactly one canonical `DEPLOYMENT_PASS`
authority for the execution tree. The post-run review preserves its V1 FAIL
prefix byte-exactly (first 4,825 bytes SHA-256
`635e7dcd49440a41fd5f966c742b924f38428785ec21f4f7af549bca4f89f71b`)
and contains exactly one canonical Round-2 `POSTRUN_ANALYZER_PASS` authority
for the analyzer tree.

## Final-manifest closure

`validate_existing_post_run_manifest` returned stage
`R100_FINAL_POSTRUN_MANIFEST_CLOSURE`, `pass: true`, and no errors, reproducing
manifest SHA-256
`045f3c3d935cd5670e900a210be9d26a2e272bd715c8e0b997da6510efd7d49f`.

The manifest is canonical exact JSON with schema
`CAT_TORSION_RESULT_MANIFEST_V2_DUAL_TREE`, the exact top-level key set,
`pass: true`, and an empty error list. The observed `results/` inventory is
exactly the declared 11-file final inventory, including
`result_manifest.json`; every entry is a single-link regular file, with no
extra entry or link substitution. All 14 declared non-self paths are unique,
exclude the manifest itself, and independently reproduce their recorded
SHA-256 hashes. The intentional no-self-hash rule and the pre-write/final
inventory roles are recorded exactly.

The claim-bound authorization JUnit hash is
`81ffc571c773cfa9a69f157559fdaa3611f55c748908c20183e4eae3f3420aa1`.
The distinct live execution-tree JUnit parses as 21 tests with zero failures,
errors, or skips; the analyzer JUnit parses as 27 tests with zero failures,
errors, or skips. Their roles are not conflated.

## One-shot execution and forbidden-access audit

The pre-execution record has zero registered audits and no executed periods.
The immutable claim, result, terminal, and manifest consistently record one
and only one registered exact audit, `REGISTERED_RUN_0001`, over periods
1 through 12. The terminal is `COMPLETED_CERTIFIED`, binds the exact raw-result
hash, and has no failure code. The manifest records
`candidate_rerun_performed: false`.

Across the source lock, preflight, claim, result, terminal, and final manifest,
the following remain exact: zero candidate numerical runs, zero generated
prime-target arrays, no external prime-table access, no Riemann-zero-data
access, and no floating or approximate matching. The source lock additionally
records zero target matches and zero parameter or matrix searches.

## Independent mathematical recomputation

An independent standard-library integer engine, without importing Paper 8
candidate code, reproduced

`det(A^n-I) = [-1,-5,-16,-45,-121,-320,-841,-2205,-5776,-15125,-39601,-103680]`

for `n=1,...,12`, together with every locked factorization and the selected
first-appearance primes

`[none,5,2,3,11,none,29,7,19,none,199,none]`.

Independent enumeration of every nonzero vector reproduced the exact
finite-field period profiles:

- `p=2:{3:3}`, `p=3:{4:8}`, `p=5:{2:4,10:20}`;
- `p=7:{8:48}`, `p=11:{5:120}`, `p=19:{9:360}`;
- `p=29:{7:840}`, `p=199:{11:39600}`.

Modulo five, `N=A+I` satisfies `N^2=0`; its nonzero kernel has four period-2
points, the complement has twenty period-10 points, and hence two period-10
cycles. The exact carrier exception set is therefore recorded as `{1,6,12}`.

The general-theorem tail remains proof-only:
`periods_above_twelve_computed=[]`, `tail_periods_computed=[]`, and every
negative-trace sample says `matrix_or_orbit_computation_performed: false`.
The three theorem-contract components pass without converting imported
primitive-divisor evidence into a computed tail.

The clock record consistently states all-integer prime-and-composite range,
unboundedness and discontinuity in every torsion neighborhood, and native
monodromy blindness to torsion order. Its exact witnesses, coprime-order
growth, `A^10` matrix, characteristic coefficients, `10*log(5)` orbit sum,
and repeated `r*10*log(5)` sum independently check. The terminal and result
agree on
`INTRINSIC_TORSION_CAPACITY_CERTIFIED_A0_FAIL_PROVES_TOO_MUCH`, with Route A
`A0_FAIL_PROVES_TOO_MUCH_NO_A1_TO_A4` and Route B `NOT_OPENED`.

## Human-report audit and non-blocking stale-status warning

The source-lock review, execution code review, both explicitly non-independent
author repair records, and the V1/V2 post-run analyzer review are hash-bound by
the final manifest and agree with the execution history. The author repair
records grant themselves no independent authority.

Two later writing-stage materials are outside the final result manifest:
`PAPER_PLAN.md` (SHA-256
`702d46ab1cf82cba01e2bfe0e4add87b0321f940712b3a439b2f42b369d34726`)
and `notes/CITATION_VERIFICATION.md` (SHA-256
`a1aecd7cd98b882ade733e3de7ddbe5a3dcf7c2eaf09e2411da81183b94ea328`).
Their scientific scope and nonclaims agree with the certified result, but
both still describe the manifest as pending and the post-run review as V1
FAIL. This is stale writing-stage status text, not a defect in the frozen
result package. It must be updated and re-bound before either document is
used as final manuscript authority. At audit time there was no manuscript
draft or manuscript peer-review report; `paper/` contained only
`references.bib`.

## Decision

The completed result package is exact, one-shot, source-bound, mathematically
reproducible, and finally closed. No result-integrity blocker remains. This
PASS authorizes use of the frozen exact result under its declared scope; it
does not authorize period extension, prime/zero fitting, Route-A A1--A4,
Route B, transfer/Fredholm, quantization, or priority claims.
