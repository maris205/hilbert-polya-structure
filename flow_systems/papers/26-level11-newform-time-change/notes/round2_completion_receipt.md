# P26 Round-2 completion receipt

Date: 2026-08-27

## Verification

Canonical command:

```bash
./experiments/reproduce.sh
```

- Unit tests: 7 passed, 0 failed.
- Independent complete runs: 2.
- Recursive result comparison: byte-identical.
- Run 1 tree SHA-256:
  `e635ee051ea25d543eb4f3fd72bce5ae4da95d64ee2ca9f90b2f5f81ba8a2da5`.
- Run 2 tree SHA-256: identical.
- Observed wall time for the canonical invocation: approximately 18.7 s.

## Bound sources

```text
8b61912da8d812cc202ad7a0f3db31222a83d728ad67c6c14084e00c144f5b03  code/round2_experiment.py
88f2ece84a26c05989678650480adc1b32e2b09a612f63ce3d8a9992a6f7856c  code/test_round2_experiment.py
d0ac236173d681ce7e4a462e14fa0780cff5a8cd131329c454e9c9f443cf8061  experiments/reproduce.sh
```

## Generated artifacts

```text
84d4e5d77d6e9110a9ff7a95858a09b2207664a91060071e6b8aa3fff8f7295e  results/newform_timechange_variation_ledger.csv
200350f80b4e679555175ca59be250a17c3eb405f0bbd97457bdb25012e049be  results/simpler_parent_length_control.csv
ce8405c0588ae4959cb1ee0cfefb6dc77586bbe91ada790a231af2a6edb0173d  results/round2_summary.json
6848d1b6f8fc32ae4894bca882a4464793174110924a91d10a614a3c52d3205f  results/artifact_manifest.json
```

Machine-readable execution evidence is in
`experiments/reproducibility_receipt.json`; source/output bindings are in
`results/artifact_manifest.json`.

## Boundary receipt

The completed object is a finite positive-word experiment, not a complete
`Gamma_0(11)` conjugacy-class certificate.  Its formal Route-A tuple is
`UNASSIGNED`; Route B was not run or invoked.  Hecke/Euler evidence is
`HEURISTIC`, testability is `NOT_TESTABLE`, and no prime or zero data were used.
