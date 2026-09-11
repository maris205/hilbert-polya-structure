# P214 physical Round2 accepted

2026-09-11 UTC. ACCEPT_PHYSICAL_ROUND2. After two preserved non-credit
pre-manifest failures, separately granted actual `1c59c5` completed once with
exit zero and no session. It copied and RAW-compared all 30 fixed mappings and
passed the complete pre/post binding plus its new nonself manifest.

Independent reception RAW-compared every source/destination pair, verified
exactly 31 regular files and zero symlinks, and rechecked every manifest row.
The 30 payloads total 10,767,955 bytes. `SHA256SUMS` has SHA256
`6896ec1a448c642015d8b8bee5ef18019bc8bc8d7c779191b0cea64321ddc6d5`.
Relative to accepted Round1, only `FREEZE_SCOPE.md` changes; the other 29
payloads are whole-byte equal. The PDF remains seven pages, 191,549 bytes,
SHA256 `a1f95a79c607436ea062f136be50c208b5505ef79568d2df5e73f4ed83a5eed8`.

Attempt 01's strict-manifest-format failure and attempt 02's complete 30-file
partial tree remain under this receipt and `frozen_round2_failed_attempt02`;
neither is relabelled or reused. Physical Round2 is accepted. Two separately
bound source-only terminal builds, artifact audits, actual all-page views and
root independent reception remain. OWNER_AMBER / HOLD_EXTERNAL.

