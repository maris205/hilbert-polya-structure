# P212 physical Round2 accepted

2026-09-11 UTC. ACCEPT_PHYSICAL_ROUND2. The single granted fixed-copy command
exited 0 without a session. Its native record preserves 27 pre/post input
checks and all 25 payload manifest checks. No retry or cleanup occurred.

Independent physical verification compared all 25 source/destination pairs
as whole bytes, found exact 26-file membership with only the expected
`sections` and `evidence` child directories, no symlinks, and reproduced the
25-entry nonself manifest. Total payload size is 12,863,465 bytes; manifest
SHA-256 is `37af2dd2a762aa234fd44040505c6f5b896742aa477f89cccc92fa49e4892951`.
Relative to Round1, exactly README, CLAIMS_EVIDENCE, NARRATIVE_REPORT and
FREEZE_SCOPE changed; the other 21 roles are raw equal. The unchanged PDF is
six pages, 191507 bytes, SHA-256 `096adcb6...e66997c31`.

This follows separately accepted final A/B and exact lifecycle adoption.
It does not relabel A/B builds as terminal, rerun science, or edit a frozen
file. Two new source-only terminal builds, complete artifact comparison and
actual all-page views remain. OWNER_AMBER / HOLD_EXTERNAL.
