# Test report

Date: 2026-08-14

Command:

```bash
bash code/run_c57.sh
```

Outcome:

- primary exact certificate: PASS;
- independent reconstruction: PASS;
- unit tests: 15/15 PASS;
- adversarial mutations: 22/22 rejected;
- dependency locks: 8/8 matched;
- primary core SHA-256:
  `2ccd08d4dd7d9735dc874af1abb04b7a982f21f8767988906df217fa71807526`;
- primary/independent `Delta_5`:
  `139.73257286997208461648902413540656140563617814033`;
- `git diff --check`: PASS;
- bytecode generation disabled in the runner.

The independent implementation does not import the primary module.  It
reconstructs both closing factors, trace resultants, root isolators, the
integer margin and incidence minors.
