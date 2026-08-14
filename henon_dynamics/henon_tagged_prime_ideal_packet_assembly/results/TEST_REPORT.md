# Test Report

Command:

```bash
bash code/run_c50.sh
```

Status: `PASS`.

- unit/adversarial tests: 11/11;
- norm-pushforward rows: 54/54;
- P49 half-norm crosschecks: 30/30;
- exact good-characteristic order atoms: 105/105;
- bad-characteristic atoms kept outside the order theorem: 20/20;
- dependency locks: 4/4;
- signed period-three mutation: rejected;
- prime-only key mutation: rejected;
- all-orbit/analytic/operator promotions: rejected.

The certificate is `results/c50_certificate.json`.  All computations are
exact.  No numerical observation is promoted to a theorem.
