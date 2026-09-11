# P215 Review B independent initial DATA receiver plan

2026-09-11 UTC. `PRECOMMITTED_SOURCE PLAN / NO DATA READ`.

Root should seal a receiver implementation before it reads the future run
tree. The receiver is separate from the B verifier and must not import or call
it. It consumes only the fixed preparation/source pins and the eventual raw
capture after a granted run.

First it must require the output directory and exact capture members, compare
all preparation, runtime, package and 43 scientific input pins against current
regular files, require raw-identical before/after check logs, child exit zero,
controller exit zero and empty stderr, and bind receipt byte counts and hashes
to the raw streams. It must parse stdout as strict ASCII with final LF and the
exact 34-line order in `OUTPUT_CONTRACT.md`; missing, duplicate, reordered or
extra fields and lines fail.

Independently, for every `0<=n<=5`, `0<=q<=4`, enumerate all `(q+1)^n`
states and apply the literal prefix-drawdown map. Build the complete transition
array and predecessor buckets. Compute first-zero depth and recurrence by a
bounded layer/indegree traversal, not Floyd. Reconstruct every fibre from the
target zero-block height constraints using dynamic programming over admissible
nondecreasing heights, not the B verifier's flagged-subset enumeration. Count
the same fibres independently with the manuscript recurrence, compare every
reconstructed predecessor and literal transition, and derive image size,
maximum fibre and unique maximizing target. Check all 30 emitted carrier rows
against these independently derived summaries and the theorem closed forms.

The receiver must separately account for its own checks and state count. The
verifier's emitted assertion count is retained as an exact observed field but
is not treated as proof of hidden checks unless root derives its expected
value from the already accepted source. Any receiver defect is corrected only
in a new preserved version without rerunning or changing the initial capture.

An accepted receiver report is initial DATA only. It is not canonical
adoption, strict replay credit, an accepted delta, final B, build, Round2 or
paper completion. `HOLD_EXTERNAL`.
