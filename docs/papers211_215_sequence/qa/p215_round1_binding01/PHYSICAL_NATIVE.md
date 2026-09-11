# P215 Round1 independent physical reception

Read-only command chunk `fe21ad`, exit zero, reopened and RAW-compared all 37
mapped source/destination pairs. It checked exact membership against FILES.tsv:
37 payloads plus SHA256SUMS, 38 files total, four declared child directories,
zero symlinks. The full 37-row nonself manifest passed.

Round0 comparison found exactly five changed destinations:
`CLAIMS_EVIDENCE.md`, `NARRATIVE_REPORT.md`, `README.md`, `main.pdf` and
`FREEZE_SCOPE.md`. The other 32 destinations are complete-byte equal.
Manifest SHA256 is
`4e85ad186fe417191ffc9c86922bdc796b03108614f6b3a7672c666673e93554`.
