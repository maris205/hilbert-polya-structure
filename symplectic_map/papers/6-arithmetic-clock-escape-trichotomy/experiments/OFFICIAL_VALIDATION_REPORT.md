# Official Registered Audit Validation Report

**Candidate:** `additive_finite_arithmetic_capacity_v2`  
**Validation status:** `PASS`  
**Classification checked:** `CAPACITY_BOUND_CERTIFIED`

## Authorized execution sequence

The final independent review first bound the exact code tree
`10fd57b1...82fb7` and source lock `2d27abce...e3fc` with a unique
`DEPLOYMENT_PASS` authority. The official sequence was then:

```bash
PYTHONPATH=code python code/scripts/run_registered_audit.py
PYTHONPATH=code pytest -q -p no:cacheprovider --junitxml=experiments/official_pytest.xml
PYTHONPATH=code python code/scripts/build_result_manifest.py
```

The registered wrapper ran exactly once. Its exclusive-create guards produced
one `EXPERIMENT_RESULTS.json` and one `registered_run.json`; the registry
records `registered_run_count=1` and `candidate_numerical_runs=0`.

## Official test result

The post-run suite reported:

```text
51 passed in 0.33s
```

The persistent JUnit file is `experiments/official_pytest.xml`, SHA-256
`34915053371701fafd147dd39986b7a5eb157ff09c44f425edfd88f0a8ac17da`.
It is outside `results/` because the reviewed fail-closed result protocol
allows exactly `CODE_REVIEW.md`, `EXPERIMENT_RESULTS.json`, and
`registered_run.json` at manifest-construction time. Placing JUnit or prose in
that directory would correctly invalidate the result-tree gate.

## Strict JSON and cross-artifact closure

The immutable result manifest reports:

- exact result tree: PASS; three allowed files discovered, with no missing,
  unknown, nested, or symbolic-link entries;
- strict result and registry schemas/types: PASS;
- all nine gate records equal fresh canonical recomputation: PASS;
- timestamp, source-lock, reviewed-tree, result digest, counters, and
  classification cross-links: PASS;
- eight required regular in-root artifacts present and hashed: PASS;
- semantic errors: none; missing or unsafe artifacts: none.

Core official hashes are:

| Artifact | SHA-256 |
|---|---|
| `results/EXPERIMENT_RESULTS.json` | `9f9878247dc821d15b503abe5a3df713d5bde0f3c76690493dc1b4a98091ace4` |
| `results/registered_run.json` | `4ebec117a2254dc4502c7afd4094e833bc751b8a7e3bffcc16496dd0fd0ea5e3` |
| `results/result_manifest.json` | `21d6910ec1e8e2995d4141f264dce06902f7d1787dea6f28d82346ebd54e3d79` |
| `results/CODE_REVIEW.md` | `5c3db5e39a09070491ca8c3d1cebcb1aad5ae13d0218f76411abe20e2c25d88b` |
| `experiments/source_lock.json` | `2d27abceb65cd0ad39612b287e27e2bbdb0b097a67e3bff4d4d6e280e6e4e3fc` |
| `experiments/upstream_bindings.json` | `654dcd13336e0dea7d4ae49a165601cae31f83db418316a5c356f1b108c40d2e` |
| `experiments/official_pytest.xml` | `34915053371701fafd147dd39986b7a5eb157ff09c44f425edfd88f0a8ac17da` |

The manifest additionally closes the proof ledger
`c411260d...396c3`, scope ledger `c3eae19c...f15d`, and independent
proof/novelty review `4036f346...63b`.

## Safety and interpretation audit

The official report records false for external prime-table access,
prime-target-array generation, and Riemann-zero access, with zero numerical
runs and zero target matches. The exact controls record no evaluated numerical
logarithm. The output classifier accepts only the scoped capacity certificate
and records no asserted forbidden or unknown claim ID.

Accordingly, `CAPACITY_BOUND_CERTIFIED` is valid only for the locked additive
certificate and its declared L/M/A subclasses. Escape conditions are
necessary failures of this certificate, not mutually exclusive, exhaustive,
or sufficient. Nothing in this run opens Route B, performs a prime/zero
comparison, or proves a universal statement about symplectic maps.

