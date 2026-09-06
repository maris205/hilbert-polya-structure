# Actual author execution and raw-byte evidence

2026-09-06 UTC. This report distinguishes the six actual scientific
executions from later inspection/comparison. No independent review,
root mathematical replay, manuscript build or enlarged cutoff is claimed.

## The three actual pairs

| Producer and role | Exact carrier / checks per execution | Complete first raw output | Second raw output |
|---|---|---|---|
| `pilot.py`, author six-row census | 30 fixed boxes, 46,766 states, 159,261 assertions | [execution_01/stdout.json](execution_01/stdout.json), 48,882 bytes | [execution_02/stdout.json](execution_02/stdout.json) |
| `ofs_tree_probe.py`, author dictionary/falsification probe, importing frozen pilot | Original $n=3,\ldots,10$; 6,171 graph/tree assertions and 26,932 literal flip assertions | [tree_execution_01/stdout.json](tree_execution_01/stdout.json), 6,689 bytes | [tree_execution_02/stdout.json](tree_execution_02/stdout.json) |
| `verify_ofs.py`, standalone author theorem check, no scientific imports | Same 2,055 states; 62,087 assertions; 2,055 completely decoded predecessors | [ofs_theorem_execution_01/stdout.json](ofs_theorem_execution_01/stdout.json), 13,640 bytes | [ofs_theorem_execution_02/stdout.json](ofs_theorem_execution_02/stdout.json) |

The first pair ran at 08:13:56--08:13:57 UTC; the tree pair at
08:27:09--08:27:22; the theorem pair at 08:48:15 and 08:48:29.
Exact start/end timestamps, actual absolute commands, working directories,
child exits, stdout/stderr sizes and before/after input hashes are in
each directory's `RECORD.json`. Every child actually exited zero, every
stderr is empty, and every declared input remained unchanged.

The complete raw stdout hashes, in table order, are:

```
72d4dfb2a8ee749d926488b40b8453d1887204a7a4241d81e9fd6696d3ee3287
aaa682e979faf23a4c2bda003b6982a636361679f9a93e8cde90fb68c9205264
f6d8142f0a72e7b31267378f24671b4de424d972362ae33d93f7f6b57c6eb53e
```

The last pair's second recorder performs a real `cmp` and retains its
command, exit zero and empty raw stdout/stderr. In addition, the
read-only [audit producer](audit_execution.py) actually rechecked all
six process records, all 32 declared before/after frozen/live input
entries, output sizes/hashes and empty stderr; it ran three further
real byte comparisons at 08:59:01. Complete audit stdout is
[EXECUTION_AUDIT.json](EXECUTION_AUDIT.json), status PASS. That later
audit did not rerun any scientific producer. Its output says so explicitly.

## Reproduction and dependency boundaries

Each recorder creates a previously nonexistent execution directory,
copies its explicit inputs and then invokes its copied producer with
`python -I`. Thus the actual author runs began from the copied source
set, not from an existing imported science package.

- `record_pilot.py SERIAL` copies four inputs and runs the six-row pilot.
- `record_tree_probe.py SERIAL` copies six inputs, including `pilot.py`,
  which the probe imports by explicit path. The interpreter generated
  a `__pycache__/pilot...pyc` in each fresh archive. Those two generated
  files are preserved and covered by the final manifest, but did not
  exist as input when the fresh directories were created. A controlled
  reproduction should use a new serial/fresh directory; running inside
  a used archive is not silently equated with that original source-only
  input state.
- `record_ofs_theorems.py SERIAL` copies six inputs, imports only the
  standard library, and has no generated scientific bytecode cache.
  Its size-increasing identities are restricted to the original maximum
  internal size eight, and its $K$ implementation is same-size.

Use a new serial if explicitly reproducing, because existing directories
are deliberately never overwritten. The mathematical proofs are separate
from finite pressure. The initial probe's two false hypotheses are
reported as counterexamples rather than failed mandatory assertions,
exactly as predeclared. All literal/dictionary assertions did pass.

## Other evidence actually inspected

The desk's full polynomial checker and 23-identity result are a separate
QAS/DTC proof-control package. This author read its proof/report and
checked the complete 40-entry desk manifest; no new execution of that
checker by this author is claimed. The report's JCA final rank-one
static count is a deductive adjugate adapter, not a separately asserted
post-pilot numerical formula check.

Source access failures are preserved in `sources/`; an inaccessible
page is not described as read, and a query connection failure is not
an empty search result. Scientific inputs, all earlier hypotheses,
the negative raw outputs and the two generated caches remain intact.
