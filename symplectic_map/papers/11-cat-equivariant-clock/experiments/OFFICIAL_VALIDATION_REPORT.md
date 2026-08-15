# Official Validation Report

**Candidate:** `cat_equivariant_retention_tradeoff_v1`  
**Validation date:** 2026-08-15 UTC  
**Current authority:** registered execution complete; independent result
integrity review pending at the time of this report.

## Gate ledger

| Gate | Evidence | Outcome |
|---|---|---|
| source package | source lock `331a1f90...aaa87b`; source review R2 `2f75d693...cc622` | PASS |
| upstream Paper 9 and Paper 10 bindings | every source-locked SHA and `COMPLETE_LOCAL_FINAL_REVIEW_PASS` terminal status reproduced | PASS |
| executable isolation | exact closed inventory, framed tree `5ee1918a...a4741eb`, AST allowlist, no float/network/process/dynamic-loader capability | PASS |
| pre-execution tests | 16 tests, zero failures/errors/skips; SHA `4cf187fb...9307ff` | PASS |
| independent deployment review | R1 fail history preserved; R2 `DEPLOYMENT_PASS`; full SHA `3cfe1a34...15110c5` | PASS |
| durable claim | exclusive claim written before candidate/scientific import; SHA `c58c9bc9...82c79f` | PASS |
| registered result semantics | strict schema, exact row order, exact fresh-engine records, exact externality booleans, exact/recomputed K001--K012 | PASS |
| terminal closure | `COMPLETED_CERTIFIED`; all nine moduli started/completed; structural control completed | PASS |
| post-run safe tests | 16 tests, zero failures/errors/skips; SHA `a4bd081c...f0287f` | PASS |

## Lifecycle audit

- `registered_audit_count = 1`;
- `arithmetic_modulus_record_count = 9`;
- `structural_unit_control_count = 1`;
- `structural_control_in_modulus_namespace = false`;
- `candidate_rerun_count = 0` in the registered artifact;
- `candidate_numerical_run_count = 0`;
- claim state is `STARTED`, followed by a single terminal state
  `COMPLETED_CERTIFIED`;
- the terminal binds the claim, result, reviewed code tree, complete ordered
  modulus tuple, and completed structural control; and
- no second registered claim, result, or terminal file exists.

## Definition and arithmetic validation

The result retains separate namespaces for `point_burnside`,
`orbit_burnside`, `g_permutation`, `enhanced`, `orbifold`, and
`action_groupoid`, plus the independently typed `structural_unit_control`.
The two invariant engines have separate scientific construction paths. Their
agreement is checked byte-for-byte after excluding only the engine identifier,
and one-sided mutations of support, inverse sign, exponent, twist, sector, and
period are rejected by the frozen tests.

For every row, the direct matrix/cyclic-locus reconstruction equals the
quadratic-algebra unit/torsor reconstruction. Exact tuples are

`(3,3,1), (8,4,2), (20,10,2), (48,8,6), (100,5,20),`
`(12,3,4), (24,12,2), (72,12,6), (60,30,2)`

in the frozen order. Point support is `r_q`, orbit support is 1, every twisted
iterate has the unique fixer `a_q^(-k)`, only the identity inertia sector is
nonempty, and every quotient-stack period is 1.

## Externality and nonclaim validation

The raw schema states and the validator enforces exact Boolean values:

- `ambient_ring_varies_with_q = true`;
- `intrinsic_prime_selector = false`; and
- `external_modulus_specialization_required = true`.

All counters for network access, external prime data, Riemann-zero data,
numeric `s`, numeric `log(q)`, numeric `q^(-s)`, randomness, new zeta
definitions, cross-`q` coefficient-ring identification, adaptive candidate
search, out-of-scope stack simulation, external data loading, and Route B are
zero. No claim of a new equivariant zeta, universal no-go theorem, intrinsic
Riemann factor, prime/zero dynamics, or all-`q` finite proof is authorized.

## Validation disposition

The registered artifact passes every author-side and deployment-authorized
gate and supports the exact classification

`EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED / A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

This report does not self-issue `RESULT_PASS`. A fresh independent reviewer
must bind the raw result and execution-tree hashes, perform read-only exact
recomputation and schema/provenance checks, and write the sole result-review
authority before the final manifest is created.
