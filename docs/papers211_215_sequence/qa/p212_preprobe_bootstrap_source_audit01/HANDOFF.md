# Source-audit handoff

The original 425-line observer is REVISION_REQUIRED_SOURCE_ONLY, with one
OPEN finding PSA-F1: fd identity is compared with the resolved key only
after body reading. Required correction is bounded to the expected-key
argument, a pre-read stable comparison, and the caller's expected argument.
This package does not amend or accept the original source.

Start with [REPORT.md](REPORT.md) and [FINDINGS.json](FINDINGS.json).
The input [SOURCE_INPUTS.sha256](SOURCE_INPUTS.sha256) is workspace-root-relative;
the package SHA256SUMS is directory-relative and excludes itself.
[READ_SCOPE.md](READ_SCOPE.md) gives actual complete/partial/pin-only scope.

Prior private-Git observer and P212 amendment authorship is disclosed.
New observer authorship is separate; old self-authored code is not independently
accepted here. Root's ordinary-bootstrap assumption is respected. No new
host reads, observer/probe/driver execution, Python/Node parsing/import,
Git/build or external action occurred. Initial 164/204 remains non-closure.
A root-authored correction, if any, needs a separate frozen delta audit.
