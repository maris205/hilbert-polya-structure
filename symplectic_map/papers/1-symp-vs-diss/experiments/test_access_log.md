# Split access log

## Development

- Full frozen-v2 run: completed before the confirmatory manifest.
- Purpose: implementation debugging and design refinement.
- Result artifact: `results/transport/transport_dev_frozen_v2.json`.
- This split was inspected before source-lock v2 and cannot support confirmatory
  language.

## Validation

- Protocol event: before the primary agent asked agents to postpone validation, an
  implementation agent ran one small smoke test with (N=512), (T=512), and
  escape bound (10^6). The artifact was written only under `/tmp`; it is a
  protocol deviation and is not used for inference.
- Full frozen-v2 run: completed once after code/source-lock alignment, with no
  deviations. Result artifact:
  `results/transport/transport_validation_frozen_v2.json`.
- Four clean neighbor-(a) validation controls were then run under the same
  trajectory protocol. Their deliberate (a)-changes are controls, not candidate
  refits.

## Test

- Status at manifest freeze (`2026-08-12T15:41:40Z`): **UNTOUCHED**.
- The test generator is locked in code unless both `--split test` and
  `--unlock-confirmatory-test` are supplied.
- Source lock, code, thresholds, nonconfirmatory outcomes, and figure layouts were
  frozen before access in `confirmatory_manifest.json`.
- A single exact invocation is authorized by that manifest. Its timestamp, output
  hash, and gate decision must be appended here immediately after completion.

Before test access, at `2026-08-12T15:57:39Z`, the manifest was amended to freeze
the paired cluster-bootstrap/Holm implementation and the four already-preregistered
neighbor-control invocations. This amendment occurred after validation analysis and
before any test artifact existed. All five transport commands are to be launched as
one batch; no result may be used to decide whether another control is run.

### Single-use access record

- Batch opened: `2026-08-12T15:58Z`; analysis completed:
  `2026-08-12T15:59:16Z`.
- All five preregistered transport arms were launched together. No arm was selected
  or omitted after viewing another arm.
- Candidate endpoint: exposure `0.0117239952`, survival `0`, 9,988 gaps,
  (P=-0.70664798), cluster-bootstrap 95% CI
  `[-0.71625339, -0.69678543]`.
- Availability, polarity, and neighbor-specificity gates all failed; all four
  endpoint Holm-adjusted directional diagnostics equaled `1.0`.
- Formal decision: `A0_SHADOW_FAIL_CARRIER_UNAVAILABLE`.
- Test access is now closed. Re-running or changing the seed/thresholds would be a
  new post-confirmatory experiment and cannot alter this decision.

SHA-256:

```text
f30b2dbddbd5e60780aa98362422d3af2dfa0ef02dfe80130774c50bb5b47d4c  results/transport/transport_test_frozen_v2.json
3bf949bbba03d4f655f196ff1992a170a973e13333f3452ca5e9da91dd0bed4a  results/transport/transport_test_neighbor_a150_v2.json
181ff96598d5d4d3b37d1b8dd3fdaeada65994215ed494c94496e01db2cd93bb  results/transport/transport_test_neighbor_a152_v2.json
7d02d45c1fe849fe9290e5ed6816ace876cc396e497e55338dbef756341cb269  results/transport/transport_test_neighbor_a156_v2.json
3e931abf4654af735c074fb960e54fbcec2d0f0882e12196a5753d343812126a  results/transport/transport_test_neighbor_a158_v2.json
a8c272161bd38e37e140c0ad72511461e4fb837edf2bf7880ba21014b89705c5  results/analysis/transport_test_analysis_v1.json
b8186fcd6e323d2e6d2e7e5c05f5f18b98cdf92475675bce25d74e0d158e3cf8  experiments/confirmatory_manifest.json
```
