# P215 physical Round2 accepted

2026-09-11 UTC. `ACCEPT_PHYSICAL_ROUND2`. Root consumed the one-use grant into
an absent destination, copied and whole-byte compared every payload, and
generated the exact nonself manifest. The tree has exactly 38 regular files,
zero symlinks and 37 manifest payloads totaling 3,027,778 bytes. Every manifest
row passes; `SHA256SUMS` has SHA-256
`a0dcd09ad6efd3ce01a364df79113bf2e35a73805066a0583448f47baaf24ebe`.

Relative to accepted physical Round1, exactly 36 payloads are RAW-equal and
only `FREEZE_SCOPE.md` changes. The accepted PDF remains six pages, 200,921
bytes, SHA-256
`ff04cdb46b6072398119a962a9038303d3665222da048c8eb14a103105d55f85`.
No B-build PDF or other generated artifact was substituted into the paper.

Final Review B remains accepted no-change at Critical 0 / Major 0 / Minor 0.
All historical failures remain preserved. Physical Round2 is accepted; two
separately authorized source-only terminal builds, complete artifact checks,
actual all-page root views and individual final QA remain. `OWNER_AMBER /
HOLD_EXTERNAL`.
