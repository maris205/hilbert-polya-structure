# P207 B — actual independent executions

2026-09-06 UTC. Five actual B mathematical processes completed: one
initial run and two fresh pairs. This log records executions, not a
promise to run them. Every producer, raw comparison and pin comparison
exited zero. No B mathematical or recorder attempt failed; none was
overwritten. The optional `jq` inspection utility was unavailable and
the JSON was inspected with Python instead; that was not a producer run.

## Exact invocation and isolation

The following recorder commands were actually run from
`/root/autodl-tmp/symbolic_dynamics`:

```text
python3 -I -B docs/papers204_208_sequence/reviews/p207_b/record_review.py initial_01 --initialize --runs 1
python3 -I -B docs/papers204_208_sequence/reviews/p207_b/record_review.py pair_01 --runs 2
python3 -I -B docs/papers204_208_sequence/reviews/p207_b/record_review.py pair_02 --runs 2
```

The initial completed before the two fresh pairs began. The two pair
recorders ran in distinct directories concurrently; within each pair
the two mathematical children ran sequentially, each in a new source-only
subdirectory. The recorder refuses existing attempt directories and
opens raw streams exclusively. It never passes the canonical or
author/reviewer data to the mathematical child.

Each child command is the following exact pattern, with the actual
absolute path in its receipt:

```text
/root/miniconda3/bin/python3.12 -I -B /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p207_b/executions/ATTEMPT/runN_source/verify.py
```

Its cwd is that same `runN_source` directory, containing only its
byte-checked standalone source at launch. The main B `verify.py`
imports only stdlib modules and does not read files, import author/A/
gate code, run another program, or load any canonical lookup table.
The recorder and the artifact auditor do read comparison data; they
are separate programs with separate roles.

The interpreter is Python 3.12.3 (Anaconda build, GCC 11.2.0), binary
SHA-256
`9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101`.
An actual same-flag probe in every attempt asserts and records
optimize=0, debug=true, isolated=1, dont_write_bytecode=1.
`-I` ignores Python environment import/optimization overrides and
excludes the script cwd/user site from module search. The producer
uses sorted/deterministically ordered output, not an asserted fixed
PYTHONHASHSEED under isolated mode. No random source or float arithmetic
is used; determinant interpolation uses exact rational numbers.

## Exact runtime inputs and output

Each attempt pins all 106 Round1 physical inputs and the 144 context
inputs (134 final-A physical files and ten other immutable files), plus
the B checker, recorder and their two manifest files. That is 254
initial pins. Each pair additionally pins the already-existing B
canonical, making 255. The recorder hashes them before and after and
runs an actual raw `cmp` on those pin lists. The initial canonical is
created exclusively from the successful initial stdout, after the
math producer exits; its creation is not a preexisting math input.

All five mathematical streams contain 2,158,999 successful assertions
and identical complete 1,558,382-byte JSON. Their common SHA-256 is

`b7206f01180dcbe5eca24dbaec67cc96ae5dc80f86004455d382e7723c786fda`.

| Actual process | Start–end UTC | Producer exit | Raw canonical cmp exit |
|---|---|---:|---:|
| initial_01/run1 | 08:20:52.423246–08:21:26.082668 | 0 | 0 |
| pair_01/run1 | 08:22:10.545881–08:22:44.162306 | 0 | 0 |
| pair_01/run2 | 08:22:44.181182–08:23:18.104117 | 0 | 0 |
| pair_02/run1 | 08:22:11.751352–08:22:45.473370 | 0 | 0 |
| pair_02/run2 | 08:22:45.490692–08:23:19.210412 | 0 | 0 |

Both pairwise raw comparisons exited zero. All three live-canonical
comparisons and all three before/after-input comparisons also exited
zero. The initial receipt contains five actual commands; each pair
receipt contains eight, for 21 recorded commands total. There are
13 actual `cmp` calls: five producer/canonical, two pairwise, three
live canonical and three before/after pins. All command stderr streams
are physically present and empty, including all five producer streams.

Complete receipts and directory-relative nonself manifests:

- [initial receipt](executions/initial_01/RECEIPT.json) and
  [manifest](executions/initial_01/MANIFEST.sha256).
- [first fresh pair receipt](executions/pair_01/RECEIPT.json) and
  [manifest](executions/pair_01/MANIFEST.sha256).
- [second fresh pair receipt](executions/pair_02/RECEIPT.json) and
  [manifest](executions/pair_02/MANIFEST.sha256).

Each directory retains every full `.stdout`/`.stderr`, copied source,
canonical snapshot and before/after input list. `CANONICAL.json` is
the complete output, not a count-only summary or truncated transcript.
The 20,115 changed sign classes include every actual chosen witness.

## Results within the original complete cyclic bounds

These are finite-box results, not the proof of the all-n statements.
Full source sets, equality lists and height distributions are checked
and their hashes/values appear in the canonical.

| n | States/targets each | Image | Core | Observed H(n) | Max fibre | Maximizers |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 13 | 13 | 1 | 3 | 7 |
| 4 | 81 | 33 | 11 | 5 | 7 | 2 |
| 5 | 243 | 86 | 21 | 5 | 7 | 10 |
| 6 | 729 | 212 | 63 | 5 | 18 | 2 |
| 7 | 2,187 | 526 | 85 | 5 | 18 | 14 |
| 8 | 6,561 | 1,309 | 155 | 5 | 47 | 2 |
| 9 | 19,683 | 3,247 | 373 | 5 | 47 | 18 |
| 10 | 59,049 | 8,025 | 613 | 6 | 123 | 2 |

Total complete cyclic sources and targets each: 88,560. The other
bounds are exactly those in `intake/REVIEW_SCOPE.md`; the 36-state
determinant is fully determined by z=0,...,36, not a new cycle-size
experiment. Formal traces are through 60 and seed-only witnesses
through n=64. No larger full-box cutoff was introduced.

## Separate artifact audit, not mathematical replay

The following additional command actually exited zero:

```text
python3 -I -B docs/papers204_208_sequence/reviews/p207_b/audit_artifacts.py
```

It reads prior and current canonical/receipt bytes, without importing
or executing any mathematical checker. It passed 12,845 checks over
501 actually consumed immutable objects and writes
[ARTIFACT_AUDIT.json](ARTIFACT_AUDIT.json), SHA-256
`fceef2dd896087d563fed7a043a096138e1380e814ee3232b4ba110abedba6d6`.
Its actual console output and command are preserved in
`AUDIT_EXECUTION.json`. It verifies original author/A/root evidence,
all stored local witnesses, shared summaries and the five actual B
receipts. This audit and prior root reproductions are not added to
the five B run count. The prior author/A runtime limitations are not
retroactively changed by B's isolated execution.

## Gate boundary

Successful replay does not close LNR-S1, establish originality, create
an accepted delta or authorize public release. The initial report
recommends exact no-change continuation with zero current P207 findings;
root response, B exact-delta acceptance, root reproduction, Round2
and terminal gates remain separate.
