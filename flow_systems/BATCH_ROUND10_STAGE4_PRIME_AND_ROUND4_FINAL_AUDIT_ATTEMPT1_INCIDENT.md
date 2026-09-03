# Round 10 final-audit attempt-1 incident

Date: **2026-09-04 UTC**

Status: **SUPERSEDED TOOLING FAILURE / NO SCIENTIFIC OR AUTHORITY IMPACT**

The first batch-level final-audit run stopped at **1663/1675** checks. All 885
local Markdown links, 92 frozen paths, terminal bindings, request controls,
paper-level audits, official ARS validators, P33 schema recount, and independent
builds passed. The only 12 failures were the same path-resolution defect repeated
for six authority witnesses in each of the P30 and P31 support bundles.

Those authority paths begin with `../../../` and are defined relative to the
support bundle's containing `notes/` directory. Attempt 1 incorrectly resolved
them from the paper root. No source artifact was missing or modified. The failed
receipt is preserved as
`BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_FINAL_AUDIT_ATTEMPT1_PATH_RESOLUTION_FAILURE.json`
at SHA-256
`bd4204f313c5a4467ad546caa46dcb5ac708c7f69ecceaedd39942b600762d2d`.

The audit tool now selects `notes/` as the resolution root only for paths that
start with `../`; paper-root-relative `notes/...` witnesses retain their original
root. A complete from-scratch replay is required before the final audit can pass.
