# First-pass documentation synchronization

2026-09-09 UTC. This is a research-checkpoint receipt, not a five-paper
release, mathematical certificate, exact sealed payload or formal evaluation.
Scientific disposition: [FIRST_PASS_DECISION.md](FIRST_PASS_DECISION.md).

## Scope and actual pre-integration state

The authorized stream is `/root/autodl-tmp/hilbert-polya-structure`, not the
shell's initial `henon_zeta` directory. The only staged scope will be this
`research_c429_c433/` directory and `henon_dynamics/CURRENT_RESEARCH_STATE.md`.
No candidate/obstruction registry is altered, because no new paper is admitted
and no formal evaluator result is being registered.

The sixteen first-wave and eight review task invocations have completed.
Eight final reviews were fully read by the coordinator and their hashes
recorded in the decision. Their original author-side “pending review” wording
is a historical snapshot, superseded by the final review/adjudication; it is
not rewritten to falsify the original timing.

An actual `git fetch origin` completed with exit status 0. A subsequent
read-only check found both HEAD and origin/main at
`5d70265ce0e110f7aed441984b37d67ccf60275e`, left/right `0 0`.
The only tracked change before integration is the new current-state heading;
the new batch is untracked. Eight inherited unrelated directories remain
untracked and outside the staged scope.

The initial Markdown target scan found one apparent missing target,
`f(z+u`, at X2's coefficient-extraction formula. The coordinator inspected
the actual line: it is mathematics `$[u^j](f(z+u)-f(z))$`, not a Markdown
file link. No file was missing and no mathematical formula was changed.
The final scoped file/link/index checks and real commit/push result will
be recorded below after they run. No synchronization success is claimed
in advance.

Protected state: C424–C428 sealed subtree and all other historical sources,
evaluators, other streams, configuration, remotes and the eight unrelated
directories remain outside this task's write/stage scope. No mathematical
program, old rerun, build, external model upload or paper publication ran.

## Actual documentation preflight

The first strict combined preflight exited 1 because the receipt's quoted
copy of that same coefficient-extraction formula was again parsed as a link.
The read-only parser was corrected to ignore fenced code, display mathematics,
inline code and inline mathematics. No research text or link was modified.
The corrected preflight actually exited 0 with:

- 42 batch files, all `.md`, all regular single-link files; no symlinks;
- 606,038 bytes before this receipt section was appended;
- 130 local file-link targets outside code/math, all existing;
- all eight final review SHA256 values equal to the literal decision pins;
- an empty Git index and exactly one tracked change,
  `henon_dynamics/CURRENT_RESEARCH_STATE.md`.

A standalone `git diff --check` on that tracked change also exited 0.
These are scoped documentation/integrity checks, not a Markdown conformance
test, validation of remote URLs, or additional mathematical runs. The final
index audit must still check all 42 batch files plus the one state file.

## Actual index audit and first-pass synchronization

The exact scoped `git add` and standalone `git diff --cached --check` both
completed with exit status 0. The subsequent full index audit exited 0:
exactly 43 changed paths, comprising all 42 batch Markdown files and the one
current-state file; every entry stage 0 and mode `100644`; every Git blob
read through `git cat-file --batch`, its native SHA-1 identity checked, and
its contents compared byte-for-byte with the corresponding regular disk file.
No other path was staged. The audited snapshot contained 678,853 blob bytes;
the ordered path/mode/object-id summary SHA256 was
`0159eae229ff0add57bce21c9b4a3917ea7f25d2f8c69625cac81d0cf31422f5`.
Those numbers describe the snapshot before this final receipt append.

Actual commit and push both completed with exit status 0:
`2f7d2ad3f06b40939142498c5da06653c86826ab`
(`Record C429-C433 coordinated first-pass proofs and eight reviews`).
By 12:21:38 UTC the explicit remote `refs/heads/main`, origin/main and HEAD
were all that commit, left/right `0 0`. A standalone `git diff HEAD --quiet`
exited 0. Only the same eight inherited unrelated directories remained
untracked. The old sealed C424–C428 subtree object was unchanged at
`05b88231bffb4381f29ddafb3e85c66101811986`.

This receipt append and the state-file synchronization notice are a separate
documentation follow-up; no reviewed proof or review file is changed by them.
The final notice commit's own identifier is reported in the user handoff,
not recursively embedded in itself. First-pass synchronization does not
complete the five-paper batch: new paper admission remains **0/5**.
