# Validation Report

## Deployment authority and sequence

Independent pre-run review Round 3 ended with `DEPLOYMENT_PASS`; the reviewed
`CODE_REVIEW.md` SHA-256 was
`629ed6bfe06f73ad387712c53f28aa73ee6c466098dd22ef502fd34f2d32ba58`.
That authority covered only the source-locked static audit.  Candidate orbit
or action computation remained forbidden.

The official sequence was:

1. verify source-lock v3 and the final independent deployment verdict;
2. confirm from the executable source that R010--R019 controls precede every
   Hénon static identity;
3. run the official safe suite and write `results/pytest.xml`;
4. run `code/scripts/run_static_audit.py --project-root .`;
5. write the human-readable result and validation reports and freeze the
   experiment tracker;
6. invoke the strict semantic manifest builder as the final mechanical step.

Official commands:

```bash
PYTHONDONTWRITEBYTECODE=1 pytest -q --junitxml=results/pytest.xml
PYTHONDONTWRITEBYTECODE=1 python code/scripts/run_static_audit.py --project-root .
python code/scripts/build_result_manifest.py --project-root .
```

## Required validation checks

- Source lock: version 3, status
  `SOURCE_LOCKED_NO_CANDIDATE_EXECUTION`, exact SHA-256
  `d15f5084900aa043e80ada46d3ce22772cd10bbdb348d4fcb000aa9fa2ca49d7`.
- Pre-lock candidate exact/numerical runs, periodic points, and actions:
  zero/false.
- Proof package SHA-256:
  `c579e2da093a8ab588a5818bab0df59a47804792fcdfa338777f48e1bd1a1214`.
- R002: exact nine-record JSON contract; unique contract IDs; five unique
  tagged equations; exact normalized equation content; no forbidden control
  character; every dependency check PASS.
- R001: all eleven executable Python files scanned, including
  `action_audit/protocol.py` and both script wrappers; zero findings.
- Controls-first: the registry order is R000, R001, R002, R010--R019, then
  R020--R023; all registered stages PASS.
- Gauge/normalization controls: matching endpoint, algebraic mismatch,
  uniform algebraic constant, symbolic telescope, transcendental injection,
  pole, multivalued gauge, and logarithm edge cases all give their frozen
  categorical outcomes.
- Hénon identities: inverse compositions, determinant one, one-form
  residuals, type-1 residuals, and graph sign residual are exact zeros.
- Low-period recurrence: equal cyclic neighbor slots are counted twice at
  periods one and two.
- Projective ledger: each audited leading homogeneous system forces every
  projective coordinate to zero at infinity; this is a proof-implementation
  audit, not orbit enumeration.
- Denominator ledger: `3*A_G` is S-integral; the exact `-1/3` control prevents
  an unjustified stronger statement.
- Environment: exact SymPy 1.14.0 categorical arithmetic, no GPU used as
  evidence, no network, no external target data, and no floating-point
  equality evidence.
- Runtime UTC is generated from the container clock; the source-lock and plan
  dates remain frozen research-document metadata.

## Official result and leakage audit

The official run status is
`PASS_STATIC_CERTIFICATE_NO_CANDIDATE_EXECUTION`.

| Field | Recorded value |
|---|---|
| Candidate parameter substituted | false |
| Candidate periodic points computed | false |
| Candidate actions computed | false |
| External prime tables accessed | false |
| Riemann-zero data accessed | false |
| Network access by executable | false |
| Floating point used as evidence | false |

The environment recorded a process high-water mark of 1,161,552 KiB.  This
exceeds the plan's informal estimate of less than 1 GiB, but it is not a
claim or pass/fail metric and does not affect the exact outputs; it is retained
transparently as an operational observation.

## Official test result

```text
82 passed in 1.01s
```

`results/pytest.xml` contains 82 tests, zero failures, and zero errors.  Its
SHA-256 before final manifest construction is
`c29e6bc5f805f32d9a9620dfad42bfe9474973f430c857531970e0f28782fa62`.

## Core result hashes before final manifest

| Artifact | SHA-256 |
|---|---|
| `source_lock_validation.json` | `c0584102565382a2a7d6222051c9e4a00ea8ebee61beabcdbc1d26d8f884af1c` |
| `target_isolation_audit.json` | `90d7613e67cf1cd607d94d4442a12aa8307e588c7ac124e6e0e2218764ae48a0` |
| `proof_audit.json` | `0126098f7bd6020aa32abe1744eb355016959b78f1e46776f58c3812a865970e` |
| `control_audit.json` | `7992e1d314da30455386bab43f19dcfb2ee6a1ffb379135468cf98c134e62efc` |
| `henon_static_audit.json` | `dc8545468f10427be411aa10e3557c18a8a64b00d0c61cc5b761b5833d392b77` |
| `command_environment_manifest.json` | `d244807ce060646c2ae69177cc5ca9f8ebec6d64c1dd9218feadded41ac646e1` |
| `run_summary.json` | `62c19ce399fde3af2c966247d6e621a6327728592b88077945388fd0bd1399eb` |

## Classification and scope decision

The validated label is
`ALGEBRAIC_NORMALIZED_ACTION_CLOCK_REJECTED_BY_ALL_PERIOD_THEOREM`.
The plan disposition is `GO_AS_NARROW_DESIGN_CERTIFICATE`, with
`MERGE_IF_STANDALONE_DEPTH_IS_REQUIRED` as the novelty-aware publication
boundary.  Only the normalized algebraic action-as-exact-prime-logarithm
route is closed.  The validation must not be generalized to all symplectic,
arithmetic, multiplier, return-time, multivalued, nonalgebraic, infinite-place,
or approximate clocks.
