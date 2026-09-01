# Test report

Run from the package root with bytecode disabled.

```text
$ python3 -B code/c281_ricci_producer.py
{"counts": {"asymptotic_rows": 36, "boundary_rows": 8, "case_rows": 14,
"collapse_rows": 12, "covariance_rows": 14, "flow_rows": 68,
"normalized_rows": 66}, "payload_sha256":
"1de35607f6ca4219ddccc844ea5cfb3534d920ce757ff56bcedf898b56f9a973",
"status": "C281_PRODUCER_PASS"}

$ python3 -B code/c281_ricci_checker.py
C281 independent checker: PASS (2063 assertions; producer-independent geometric reconstruction)

$ python3 -B code/c281_ricci_sympy_crosscheck.py
C281_SYMPY_PASS (20 symbolic identities; independent normalized-time reconstruction)

$ python3 -B code/c281_ricci_replay.py
C281 byte replay: PASS (159616 bytes)

$ python3 -B code/c281_ricci_mutation.py
C281 hostile mutation audit: PASS 52/52 (repaired semantic mutations plus stale-hash control)
```

Boundary assertions explicitly fail if an infinite flat clock is replaced by
a finite one, a tied set loses a minimizer, `D/n` is changed, a full collapse
is mislabeled partial, a normalized volume differs from one, or a survivor's
Euclidean blowup dimension is removed.  Exact case-to-parameter mappings,
top/nested/row key sets, full vector lengths, finite normalized-time tails,
and every family-specific key set reject repaired-hash bypasses.
