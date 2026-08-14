<!-- HENON_AUDIT_META_V1
{
  "artifact": "experiment_tracker",
  "candidate_audit_sha256": "07323e668ef4da5134fb74328bbb0b278fb2b98f789945725e00f963ddab238d",
  "candidate_id": "integral_area_henon_multiplier_support_v1",
  "official_full_run_status": "PASS",
  "run_summary_sha256": "4ad647f700080cfc51a61663b2dbef422f9454a7db3ed604a7ec58dea1469348",
  "schema_version": 1
}
HENON_AUDIT_META_V1_END -->

# Exact Experiment Tracker

The source-locked controls-only deployment completed before the candidate was
opened.  It returned `CONTROLS_PASS_CANDIDATE_NOT_EXECUTED`, with all eight
pre-candidate gates passing.  The subsequent official CPU exact run completed
all 15 registered runs without a failure.

| Run | Purpose | Status | Notes |
|---|---|---|---|
| R000 | Validate immutable source lock | PASS | Lock v2 matched frozen SHA-256; pre-lock candidate count remained zero. |
| R001 | Forbidden-data isolation | PASS | AST/dataflow scan found no target-data or network dependency. |
| R010 | Proof provenance and stable-ID structure | PASS | Versioned theorem, proof-step, and equation IDs were unique; prose hints were nonblocking. |
| R011 | Planted bad-prime control | PASS | Generic exact-modulus path recovered `1/2` and `2` with frozen support `{2}`. |
| R012 | Integral negative control | PASS | Through period 3, the derived exact rational-modulus set was `{1}`. |
| R013 | Nonunit Jacobian scope control | PASS | The `delta=2` reciprocal-unit conclusion was refused without predeclared support `{2}`. |
| R020 | Cubic parameter preflight | PASS | The monic irreducible cubic has one real root in the frozen rational interval. |
| R021 | Polynomial inverse and symplectic identity | PASS | Both inverse compositions, determinant one, and the symplectic matrix identity held exactly. |
| R031 | Candidate exact period 1 | PASS | Two exact fixed points; determinant, trace resultant, multiplier unit, and cyclic checks passed. |
| R032 | Candidate exact period 2 | PASS | The fixed branch was removed exactly; two points forming one cycle passed all checks. |
| R033 | Candidate exact period 3 | PASS | The fixed branch was removed exactly; six points forming two cycles passed all checks. |
| R040 | Irrational-unit scope control | PASS | The cat-map control retained an irrational algebraic-unit spectral radius greater than one. |
| R041 | Floating-parameter rejection | PASS | Approximate `u` was rejected from the exact integrality pipeline. |
| R042 | Modulus reporting guards | PASS | Irrational exact and approximate near-rational moduli remained outside rational support classification. |
| R043 | Bad-set provenance | PASS | Candidate support was empty and planted support `{2}`, both frozen before multiplier access. |

The all-period conclusion is sourced exclusively to the deductive proof in
`notes/PROOF_PACKAGE.md`.  Runs R031--R033 are a finite implementation audit
and do not supply statistical or inductive evidence for the theorem.

