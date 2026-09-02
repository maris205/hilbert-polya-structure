# P162 improvement log

**Lifecycle:** `HOLD_EXTERNAL`

## Round 0

- Frozen artifact: `main_round0_original.pdf`.
- SHA-256:
  `e496ce1be3084e61616494cab2ca405238adfa575a6484db93029f8dae01de46`.
- Author verifier: 1,712,974 assertions, `PASS`.

## Review A disposition

Review A returned `0 Critical / 0 Major / 1 Minor`.

| Finding | Disposition |
|---|---|
| M1: “worst-source absorption clock” in the abstract fails to explicitly exclude the fixed full source. | Accepted. The abstract now says “worst-non-full-source emptying clock,” matching the quantified theorem. No formula, proof, verifier, or reference changed. |

The post-repair artifact is frozen as `main_round1.pdf`. Review B must begin
from that source and PDF without trusting Review A's derivations.

## Review B disposition

Review B returned `0 Critical / 0 Major / 0 minor` after an independent proof
derivation, 2,275,862-assertion verifier, owner/collision audit, two
source-only cold builds, and all-page PDF inspection.  It requested no source
change.  Consequently `main_round2.pdf` is a byte-identical freeze of Round 1:

```text
730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62
```

The current `main.pdf` is byte-identical to that Round-2 artifact.  Final
status is `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.
