# C196 results

## Exact evidence

- Payload SHA-256:
  `6269e5194aa8c5b69bb2d8786efc2ca70935261b10e8e78def7c006ae53e2545`.
- Evidence-file SHA-256:
  `58efbb32c8788e901d6e94e6cff27c0f60026a3dc8a4147b04d7613742b617c5`.
- Evidence bytes: 123,388.
- 18 systems; 126 pencil rows; 417 Hermitian, 417 commutator, and 99
  trace/energy checks.
- Minimum sampled gap: `7.215938966533e-01`.
- Maximum Newton, atlas, and inverse-position residuals:
  `4.440892098501e-15`, `6.408593517931e-15`, and
  `6.217248937901e-15`.
- At `T=256`, maximum positive/negative position errors are
  `3.497743809727e-01` and `2.729106490272e-01`; velocity errors are
  `1.715099803243e-03` and `1.178082193964e-03`.

## Verification

- Independent checker: 2,210 assertions with exact nested schema closure.
- SymPy reconstruction: 1,200 checks.
- Replay: 123,388 exact bytes.
- Mutations: 135 repaired-hash and one stale-hash rejection, including five
  unknown-key schema injections.
- Final PDF: 3 pages, SHA-256
  `efa8b97487763be814a0e3c5b65fe56616a377e3e2aacc7d97e26e611061b008`.

The all-parameter theorem comes from the proof and classical source lock, not
the finite oracle.  Verdict:
`A0_FAIL / A1_FAIL / A2_FAIL / A3_FAIL / A4_NATURAL_QUANTIZATION`, overall
`ROUTE_A_REJECTED`, Route B false.
