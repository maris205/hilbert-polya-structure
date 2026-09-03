# Round 10 publication-manifest attempt 2 incident

Date: **2026-09-04 UTC**

Status: **SUPERSEDED BEFORE COPY OR GIT MUTATION**

The second allowlist manifest selected 256 files and correctly excluded caches,
private material, unrelated legacy trees, canonical papers, and science/results.
A read-only comparison then showed that its basename pattern selected the
prefixed patch/draft/report files inside the P29/P32 superseded-layout archives
but omitted non-prefixed build logs, PDFs, and compiler transcripts in those
same evidence directories. No copy, staging, commit, or push had occurred. The
256-file manifest is preserved as
`BATCH_ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_AND_ROUND5_SYNC_MANIFEST_ATTEMPT2_SUPERSEDED.json`
with SHA-256 `fe748016186bb3579282dddf3497a568433e98489c57aa60fe6d1b23e054420c`.
The builder now includes every regular file under those explicitly named
superseded-layout directories; all exclusion and publication-boundary rules are
unchanged.
