# Independent Result-Integrity Audit

Audit date: 2026-08-14 UTC  
Verdict: `PASS`  
Scope: Paper 7 official result closure only; this is not a manuscript review.

## Access and execution boundary

This audit was performed independently from the author-side result analysis. It
did not invoke the registered candidate runner, create another lifecycle claim,
extend the registered cutoff, or edit code, result artifacts, or manuscript
files. Exact algebraic checks were performed in memory from the frozen
parameter and the coefficients already serialized in the official JSON. No
network resource, external prime table, Riemann-zero data, floating orbit
match, or approximate comparison was used. This note is the audit's only
write.

## Frozen bindings

All hashes below were recomputed from the current regular, nonsymlink files.

| Object | Independently observed SHA-256 | Result |
|---|---|---|
| `experiments/source_lock.json` | `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1` | MATCH |
| `experiments/EXPERIMENT_PLAN.md` | `b3ed3a90416295f0b64c89dce9fcf3f6d794245c318793f2679f3557a5b4579c` | MATCH |
| `notes/PROOF_PACKAGE.md` | `9c4cff04ac7434822c5e0d091509947da554ac612a6f7b4332c5675fc6a355c9` | MATCH |
| `notes/SOURCE_LOCK_AUDIT.md` | `aaf6854f40036cd272495ad221d5fbf62d08e3185f4cb6efd9f80e211e1c3f2e` | MATCH |
| reviewed 29-file source/code tree | `7a5ea42ea52d35bf4d6608b1175a43ab81ceaa9ed8fbfd0e35e183920dbdd27a` | MATCH V4 |
| `results/CODE_REVIEW.md` | `ac8bc40bc863613260486106ef7d46ea0370bea326019de1b3b1a83d488c6109` | MATCH |
| `results/PRE_EXECUTION_AUDIT.json` | `2d8580805f57168a7cfcc3eeb8ae4a7f4c036d5222bea8a2d7f7a71b6152c948` | MATCH |
| `results/registered_run.claim.json` | `b118f2ae60e3317a45d026ac004997e6629bef35ae5c133f441a2af6a1202ed0` | MATCH |
| `results/EXPERIMENT_RESULTS.json` | `847564ffb9e69aee2018dfa179490fafa81b733ad58231dab9202b82623f3ce6` | MATCH |
| `results/registered_run.json` | `06215794b323552bc953c3ea8935d76c15b205bc7df13c170e448c0562b0b7b9` | MATCH |
| `results/pytest.xml` | `4e38e3197ec588edceac43c8292630a61f018f4f03f36bb3c8606723bbd0f237` | MATCH |
| `results/result_manifest.json` | `6d9407408437954f52b4a1cb7f0caa50ca00bd22be9cf9a348a1bbb60c9a87e8` | MATCH |

The reviewed-tree digest was recomputed independently with the frozen framed
path/content construction over the five explicit scientific inputs and the
24-file closed-world code inventory. The inventory had no missing or extra
source file. `CODE_REVIEW.md` contains exactly one column-one authority line
for each of V1--V4. V1 is `FAIL`, V2 and V3 are `DEPLOYMENT_FAIL`, and the
sole V4 line is the canonical independent `DEPLOYMENT_PASS`, bound to the
source-lock and reviewed-tree hashes above.

The four source-locked upstream bindings also match their live regular files:

| Upstream binding | Observed SHA-256 |
|---|---|
| Paper-2 source lock | `aab59e6d97e919bd9f11f74cf45d8163fc320560dfa74bee85401bd184d37842` |
| Paper-2 proof package | `6d01f26b5832bd88923d4f4ba0bb5ed7010a571f17f46a0e75b6247499034e17` |
| Paper-2 final PDF | `160e9c6fa12c35f500fbae39d9316fc55e8c9b4f1b044ef3deda6037e0b5b1c3` |
| Paper-5 capacity final PDF | `9c3b395a9d4ec704fb54951bd69d5d0fd6d9db7bb6c857f8fb45ee6e5b69c0f8` |

The proof package is therefore byte-for-byte the package audited by the
pre-execution proof contract. This result audit verifies that binding and the
reported proof/evidence boundary; it does not substitute for a mathematical
review of the proofs.

## One-shot lifecycle closure

The result directory contains one claim, one terminal ledger, and one official
candidate-result JSON. There is no `TARGET_HIT_HALT.json` or alternative
claim/result/terminal artifact. All lifecycle links agree exactly:

- run id `REGISTERED_RUN_0001`, registered-run count `1`, and target set
  `["1","-1"]`;
- frozen, started, completed, and result period lists all equal
  `[2,3,4,5,6,7]`;
- immutable claim state `STARTED` and terminal state `COMPLETED_NO_HIT`;
- terminal `failure_code=null`, `stopped_period=null`, and all six periods
  completed;
- claim hash, result hash, pre-execution hash, review-file hash, source-lock
  hash, and reviewed-tree hash all match the actual files and one another;
- `candidate_numerical_runs=0` throughout. The registered work is exact
  symbolic arithmetic, not a numerical or approximate run.

The pre-execution object has all five required P0--P2 gates passing, the exact
V4 independent-review gate passing, status
`AUTHORIZED_FOR_REGISTERED_EXECUTION`, zero prior registered runs, and no
registered candidate period recorded before the claim. The result embeds
byte-for-byte equivalent gate and independent-review objects.

## Exact registered-data audit

The six candidate records were parsed using their serialized exact
`1,u,u^2` coefficient basis in
`Q(u)=Q[U]/(U^3-2U^2+2U-2)`. Independently, for every `n=2,...,7`, the audit
verified all of the following from the frozen coefficients:

1. the serialized iterate equation is exactly `g^n(z)-z`;
2. its radical, the lower-period overlap, and the monic radical/set-difference
   exact-period component obey the source-locked formula;
3. the formal dynatomic quotient is exact, its recorded radical is correct,
   and in these six candidate records that radical equals the set-theoretic
   exact-period component;
4. the exact-period component is squarefree, its degree is divisible by `n`,
   and all recorded degree, multiplicity, and cycle-count fields are correct;
5. the serialized `B_n` is exactly
   `product_{j=0}^{n-1} g^j(z)` and
   `B_n(g(z))-B_n(z)` is zero modulo the exact-period component;
6. for each target `+1` and `-1`, the serialized gcd is the constant one,
   the independently recomputed target resultant equals the serialized field
   element, and its exact rational field norm equals the recorded nonzero
   integer. Thus all twelve gcd/resultant/norm decisions agree and none is a
   target hit.

The raw comparison table is:

| `n` | exact degree | cycles | `gcd(+1)` | `N(+1)` | `gcd(-1)` | `N(-1)` |
|---:|---:|---:|---:|---|---:|---|
| 2 | 2 | 1 | 0 | `2^2` | 0 | `2^2` |
| 3 | 6 | 2 | 0 | `2^9` | 0 | `2^9` |
| 4 | 12 | 3 | 0 | `2^20` | 0 | `2^24` |
| 5 | 30 | 6 | 0 | `2^50 * 16807` | 0 | `2^60 * 161051` |
| 6 | 54 | 9 | 0 | `2^102 * 117649` | 0 | `2^120 * 387420489` |
| 7 | 126 | 18 | 0 | `2^294` | 0 | `2^266 * 868028736113769706358509` |

The six serialized wall times sum exactly to `23,239,165,865 ns`. Every row
has `status=PASS`, run id `R042` through `R047`, evidentiary role
`DEVELOPMENT_SEEN_REPRODUCTION`, and optional `q=3` diagnostic
`NOT_REQUESTED`.

## Controls, regression, tests, and manifest

The three dynamical controls were independently checked from their serialized
rational polynomials:

- for `z^2` at period two, `B=+1` is detected, `B=-1` is absent, and the
  declared negative target `B=2` is absent;
- for `z^2-2` at period two,
  `Psi_2=z^2+z-1`, `B=-1`, and `Lambda=-4` are detected with the correct
  sign;
- for `z^2-3/4`, the nonempty formal period-two factor is correctly kept
  separate while the set-theoretic exact-period component is empty, preventing
  a false target hit.

The upstream Paper-2 regression files have hashes
`dd5272f51243586523d13ba5e716503c648c46d43a0699153d686ae6fe8f1947`
and `c0edd8b509920890470c9f93f0256b0d2f2dbdd3a4f4da367c5abb128282fdb8`.
Their schemas, period-1--4 keys, formal degrees `2,2,6,12`, conjugacy ledger,
and paired multiplier/resultant invariants agree with the control record.

The JUnit XML is well formed, contains 38 distinct test cases, reports 38
tests with zero failures, errors, and skips, has no failure/error nodes, and
contains all six mandatory security/integrity tests.

The strict manifest has `pass=true`, exactly 12 unique listed hashes, and all
12 recompute correctly. Its recorded pre-manifest result-tree inventory has
exactly the nine authorized evidence files with empty `missing`, `extra`,
`nested`, `symlinks`, and `unsupported` lists. The live result directory now
contains precisely those nine files plus the manifest itself; there is no
unrecorded result artifact. `unsafe=[]` and `semantic_errors=[]`.

## Human-report and inference-boundary audit

`OFFICIAL_EXPERIMENT_RESULTS.md` reproduces every degree, cycle count, gcd
degree, norm factorization, wall time, total wall time, and frozen hash from
the raw JSON. `OFFICIAL_VALIDATION_REPORT.md` reproduces the lifecycle chain,
38-test result, strict-manifest status, twelve exact no-hit certificates, and
proof-versus-finite-evidence decision matrix. `EXPERIMENT_TRACKER.md` records
R042--R047 as development-seen no-hit reproductions and R090 as complete.

All three human documents preserve the correct evidentiary boundary:

- finite classification:
  `BASE2_EQUALITY_ABSENT_N2_TO_N7_DEVELOPMENT_SEEN`;
- new blind periods: none; periods 2--7 were disclosed as seen before lock;
- theorem-backed local valuation:
  `EXACT_2ADIC_VALUATION_ALL_PERIODS_CERTIFIED_BY_PROOF`;
- rational equality excluded by the local obstruction only at periods 2 and
  3, while the all-period question remains
  `BASE2_EQUALITY_ALL_PERIODS_OPEN_N_GE_4`;
- modulus-only and characteristic-exponent equality are not inferred;
- route labels remain exactly
  `ROUTE_A_NOT_ADVANCED / ROUTE_B_NOT_OPENED`.

## Disposition

`PASS`: the frozen source/proof bindings, V4 authority, one-shot lifecycle,
all six exact period records, all twelve target certificates, controls,
upstream regression, 38-test JUnit report, 12-hash manifest, and human reports
form a mutually consistent official result closure.

Exact blockers: none.

No additional candidate period is authorized under this source lock. The
remaining scientific obstacle is proof-level control of `B_C=+/-1` for
`n>=4`; any new computation must be a separately source-locked project.
