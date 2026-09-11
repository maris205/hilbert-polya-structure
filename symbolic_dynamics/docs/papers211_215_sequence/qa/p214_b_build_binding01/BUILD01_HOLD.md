# P214 Review B build01 HOLD

2026-09-11 UTC. The one-use root grant was consumed exactly once at chunk
`0345b1`. The build controller returned exit 1. This tree is permanently
preserved and is not retried, cleaned, resumed or relabelled PASS.

All four TeX/Bib passes, PDF diagnostics and seven page renders completed with
their 15 supervised statuses zero. The failure occurred only at the final
`science.after` content check: after `cd` into the cold source tree, the recipe
invoked a manifest whose seven paths are workspace-relative without returning
to the workspace. `science.after.stderr` contains exactly seven not-found
messages and the strict summary warning. The corresponding pre-build check
from workspace root had passed.

This is a build-recipe cwd defect, not a manuscript, TeX, scientific DATA or
input-content change. A future build02 requires a separately sealed recipe,
fresh path/output binding and new one-use grant. No evidence in build01 may be
used as accepted artifact or page-view credit. HOLD_EXTERNAL.
