# Paper 48 PRE-OUTPUT integration candidate

This sealed candidate implements the preregistered all-radix carry-free
finite controls for SD-C50 while preserving the proof/experiment boundary.
The frozen preauthority input is under `preauthority/`; no authority or Git
tree is read or written by the integration driver.

Run a disposable State-A build with:

```sh
python -I -B code/integration/run_integration.py --root "$PWD" --state A
```

State B additionally requires a nonzero 40-hex commit and remains
publication-shaped but unauthorized. The driver installs only the exact
declared output tree, supports a forced late-failure probe, and returns zero
physical replacements on a byte-and-metadata-identical second run.

Evaluator A and B outputs are finite controls. Only `results/proof_audit.json`
contains infinite theorem certificates. Both strict Route validators retain
`(A0_FAIL,A1_FAIL,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)`,
`ROUTE_A_REJECTED`, and a forbidden Route-B invocation.

Status: `HOLD_FOR_INDEPENDENT_AUDIT`.
