# P24 Round-2 validation report

## Material Passport

- Origin Skill: experiment-agent
- Origin Mode: run + validate
- Origin Date: 2026-08-27
- Verification Status: VERIFIED
- Version Label: p24_round2_validation_v1

## Reproducibility verdict

- Determinism class: deterministic exact Gaussian-integer enumeration.
- Verdict: `REPRODUCIBLE`.
- Core-output combined SHA-256: `d0a4187d8720263fd07041a1e1e4073c41a218eb6e97d4d66094f3c0e4c49b96`.
- A second in-process generation produced the identical byte stream before any
  artifact was written.

## Exact validation checks

- Enumerated reduced words including identity: 22409.
- Unique exact matrices: 11481.
- All determinants exactly one: `true`.
- All entries exactly congruent to `I mod 3`: `true`.
- All orientation inverses present: `true`.
- Maximum trace reconstruction residual: `1.137e-13`.
- Loxodromic / parabolic / identity rows: 10976 / 504 / 1.
- Primitive-within-word-ball candidates / certified observed repetitions:
  10944 / 32.
- Holonomy-shuffle control rows: 10944.
- Prime or zero tables used: `false`.

## File hashes

- `results/bianchi_complex_length_ledger_round2.csv`: `13b1499795dd0147a1db97ee68aa218bae03225446a089f10cc402937548da7e`
- `results/bianchi_holonomy_shuffle_control_round2.csv`: `d47a321f163fa0a1958eaa080a224567c95a216e5f1bc96d50d6ce5c23397e00`
- `results/round2_metrics.json`: `afae7c84f097b1b2b0122283706635c507df4d657dac1d062c2e16dcbe0783dd`


## Claim boundary

`[NUMERICALLY_CERTIFIED]` applies only to exact matrix arithmetic, the stated
elementary-generator reduced-word ball, deterministic collision counts, and the
reported floating reconstruction tolerance.  The sample is **not** a complete
enumeration of `Gamma((3))`, **not** a complete conjugacy-class or primitive
closed-geodesic ledger, and establishes no orbit-to-prime-ideal map.  Those
claims remain `[OPEN]`.  Cusp/scattering terms are not computed.
