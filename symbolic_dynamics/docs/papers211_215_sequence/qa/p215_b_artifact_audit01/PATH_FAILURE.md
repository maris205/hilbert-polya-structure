# Preserved artifact-manifest path failure

The first read-only attempt to check the 160-row build manifest from the build
root used `../../../../qa/...`, one parent too many, and exited 1 because the
manifest path did not exist there. It changed no artifact and is not PASS
evidence. The corrected `../../../qa/...` invocation passed all 160 rows.

A later combined closing command successfully checked this artifact seal and
checker, then incorrectly looked for the review `FINAL_SHA256SUMS` in this
artifact directory and exited 1. That absent-path lookup also changed nothing;
the final review seal was checked separately from its correct directory.
