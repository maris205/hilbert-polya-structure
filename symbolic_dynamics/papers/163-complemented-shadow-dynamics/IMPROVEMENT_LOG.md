# P163 improvement log

**Lifecycle:** `HOLD_EXTERNAL`

## Round 0

- `main_round0_original.pdf`
- SHA-256:
  `899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf`
- Paper-local verifier: 1,430,898 assertions, `PASS`.

## Review A disposition

Review A returned `0 Critical / 0 Major / 0 Minor`. No source, theorem,
proof, reference, verifier, or presentation change was requested. The
byte-identical post-review artifact is frozen as `main_round1.pdf` so that the
no-change decision is auditable. Review B must perform a fresh falsification
pass rather than inherit this verdict.

## Review B disposition

Review B returned `0 Critical / 0 Major / 0 minor` after an independent
proof reconstruction, 1,041,401 exact assertions, fresh ownership and
P1--P165 collision audits, two byte-identical verifier replays, and two
source-only cold builds.  It found no missing boundary case or executable
repair.

No source, theorem, proof, bibliography, verifier, or presentation change
was made.  The accepted internal artifact is frozen as `main_round2.pdf`;
all of `main.pdf`, `main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf` have SHA-256
`899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf`.
External status remains `HOLD_EXTERNAL`.
