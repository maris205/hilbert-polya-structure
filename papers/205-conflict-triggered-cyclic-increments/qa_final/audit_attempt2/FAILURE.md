# Second auditor schema failure

2026-09-06 UTC. Actual execution exited 1 at the author's declared count:
the auditor looked for `assertions`/`total_assertions`, while the intact
author canonical names its total `total_checks`. No numerical assertion
failed and no canonical was changed. This directory preserves the failed
auditor and empty stdout; the actual displayed traceback is not claimed
as a separately captured original stderr. The correction uses an explicit
author/A/B key mapping, retaining all equality checks and exact values.
