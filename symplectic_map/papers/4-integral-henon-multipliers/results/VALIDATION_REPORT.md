<!-- HENON_AUDIT_META_V1
{
  "artifact": "validation_report",
  "candidate_audit_sha256": "07323e668ef4da5134fb74328bbb0b278fb2b98f789945725e00f963ddab238d",
  "candidate_id": "integral_area_henon_multiplier_support_v1",
  "official_full_run_status": "PASS",
  "pytest_status": "PASS",
  "pytest_xml_sha256": "465319a8ab389158e0b799d7c49a927fdc92a7828ed384e7efc51080f4724ab9",
  "run_summary_sha256": "4ad647f700080cfc51a61663b2dbef422f9454a7db3ed604a7ec58dea1469348",
  "schema_version": 1
}
HENON_AUDIT_META_V1_END -->

# Validation Report

## Deployment sequence

1. Independent static review ended with `DEPLOYMENT_PASS` after four
   fail-closed review/repair rounds.  The final safe reviewer suite reported
   39 passing tests without candidate execution.
2. The official controls-only command ran first.  R000, R001, R010,
   R011--R013, R020, and R021 all passed, and the candidate remained
   unexecuted.
3. Only after that gate did the official full CPU exact audit run R031--R033
   and R040--R043.  All 15 registry entries passed; no must-run entry failed.
4. The official post-run suite completed with 39 passing tests and wrote the
   linked JUnit XML.

Official commands:

```bash
python code/scripts/run_exact_audit.py --controls-only
python code/scripts/run_exact_audit.py
PYTHONPATH=code pytest -q --junitxml=results/pytest.xml
python code/scripts/build_result_manifest.py
```

## Exact validation checks

- Source lock v2 parsed and matched SHA-256
  `3ae1623304b2cc68403cfc20de545edce7cea6af6e2df9c1cd56d4ae8f38d269`.
- The pre-lock record remained zero for candidate exact/numerical runs,
  periodic points, monodromies, external prime tables, and Riemann-zero data.
- The executable isolation audit found zero forbidden-data or network
  dependencies.
- The proof artifact carried one current schema ID and unique required
  theorem, proof-step, and equation IDs; natural-language hints were advisory.
- The polynomial inverse, Jacobian determinant, and symplectic identity held
  exactly.
- Controls were completed before candidate execution.  The planted control
  recovered `1/2,2`; the integral control derived `{1}`; the nonunit Jacobian
  scope gate refused an undeclared conclusion.
- For periods 1--3, all recurrence remainders, determinant residuals, trace
  resultants, cyclic trace differences, lower-period separation certificates,
  rational-root tests, and unit/norm checks passed exactly.
- The real-embedding modulus engine performed exact irreducible-minimal-
  polynomial and rational-square tests.  No unresolved square-test state and
  no raw rational-prime modulus remained.
- All result JSON files parse successfully.  The official run used SymPy
  1.14.0, no GPU, no network, no external target data, and exact rational /
  polynomial arithmetic.  Recorded peak resident memory was 69.434 MiB;
  registered exact stages totaled 0.783474 seconds.

## Test result

The official suite reported:

```text
39 passed in 1.61s
```

The JUnit artifact is `results/pytest.xml`; its SHA-256 is linked in the sole
machine metadata block above.

## Core artifact hashes before final manifest

| Artifact | SHA-256 |
|---|---|
| `results/run_summary.json` | `4ad647f700080cfc51a61663b2dbef422f9454a7db3ed604a7ec58dea1469348` |
| `results/candidate_multiplier_audit.json` | `07323e668ef4da5134fb74328bbb0b278fb2b98f789945725e00f963ddab238d` |
| `results/control_audit.json` | `1a25fb057b37acee8effa2184af0a5eba154746d15a4e7b71ac1fbbe0f1bea88` |
| `results/exact_period_ledger.json` | `7649def89c4712e0698ab06e6b1bd11329a6f534c4592995175fcc6c955873ea` |
| `results/exact_polynomials.json` | `500c30377b79c53a1a747e721e616e826594c591a585a1d4404a9fb2b97cc1f3` |
| `results/negative_result_ledger.json` | `3886ee0271056e6c9febbe54f4a05a9a675b876f8d296a4de4306a352f14f9c6` |
| `results/scope_audit.json` | `548dd825d5abea5b3f672ea4c0aee8cab5014692e7107bfc177f969cfa7b44e5` |
| `results/command_environment_manifest.json` | `674db83eec3f851a1215dd399153578b8e28a8268acf4195c64ad323e4a00c17` |

## Scientific classification

The validation supports the label
`A0_FAIL_EXACT_RATIONAL_PRIME_MODULUS_ABSENT_BY_THEOREM`, not a numerical
absence claim.  The finite period ledger is implementation evidence only.
The theorem does not constrain irrational or approximate multiplier moduli,
and downstream Route-A stages remain stopped for this candidate.

