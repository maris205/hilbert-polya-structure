# Exact execution and artifact report

Author evidence only. Four numerical processes completed successfully:
two for the original three-map slate, and two for a D2LC theorem check on
the same six graph boxes. No failed numerical execution occurred and no
producer was repaired after its recorded executions. Failed web source
accesses remain in `source_access_01.json` through `source_access_07.json`.
These source-access errors are not numerical failures.

## Actual commands and outputs

Both recorder commands were run from `/root/autodl-tmp/symbolic_dynamics`:

```sh
python3 -I -B docs/papers204_208_sequence/scouting/finite_systems_sixteenth/capture_pair.py
python3 -I -B docs/papers204_208_sequence/scouting/finite_systems_sixteenth/d2lc_theorem/capture_pair.py
```

Both recorder commands exited zero. Their stdout summaries were, respectively:

```json
{"assertions": 276701, "complete_boxes": 26, "literal_maps_executed": 3, "role": "AUTHOR_SCOUT_NOT_INDEPENDENT_REVIEW", "state_map_pairs": 46819}
{"assertions": 581373, "complete_boxes": 6, "literal_maps_executed": 1, "role": "AUTHOR_THEOREM_CHECK_NOT_INDEPENDENT_REVIEW", "state_map_pairs": 33867}
```

The recorder launches each numerical process using the actual executable
`/root/miniconda3/bin/python3`, flags `-I -B`, a copied `runtime_wrapper.py`,
a copied standalone `pilot.py`, and that execution's own directory. The exact
argument arrays, working directories, elapsed times, environment, exit codes,
stdout/stderr paths and hashes are preserved in each
`execution_0{1,2}/COMMAND_RECEIPT.json`, and repeated in its `PAIR_RECEIPT.json`.
The wrapper compiles with `optimize=0`; assertions remain enabled. Each
process has a separate source snapshot and historical-input snapshot.

| Scope | Process 1 / 2 seconds | Source + historical inputs per process | Runtime files per process | Assertions per process |
|---|---|---:|---:|---:|
| Original 26 boxes | 5.356832981109619 / 5.502636671066284 | 23 = 12 + 11 | 95 | 276,701 |
| D2LC original-box theorem check | 1.0335299968719482 / 1.0213344097137451 | 20 = 4 + 16 | 95 | 581,373 |

The numerical child environment is exactly `LC_ALL=C`, `TZ=UTC`,
`PATH=/usr/local/bin:/usr/bin:/bin` as supplied by the recorder; the actual
interpreter environment is also saved in runtime records. No GPU, random
sampling, floating-point mathematics or orbit cutoff is used.

## Raw identity, not summary identity

In each scope the recorder actually ran `/usr/bin/cmp` between
`execution_01/stdout.json` and `execution_02/stdout.json`. Both exit codes
are zero; raw `cmp.stdout` and `cmp.stderr` are empty and retained. It then
copied the first raw stdout to `CANONICAL.json` and actually compared that
copy with the source; `CANONICAL_COPY_RECEIPT.json` records exit zero.
All four numerical stderr files are empty.

Canonical whole-stdout SHA-256 values:

- Original: `6adb30c877dd8ab07841e4f66369e85fe160f7843227db6ed8f91b3b7ac94916`.
- D2LC theorem check: `8f001e1264d8be063d49ba9f601ed95bed8e91925cffb8fa9d637b4ea53dfa73`.

The original stdout contains all 26 box censuses, complete depth/period/fibre
histograms (including zero fibres), actual longest-tail and longest-cycle
witnesses, first maximal targets and their whole predecessor lists, and
SHA-256 values of the complete ordered integer-arrow arrays. It does not
print every integer arrow; the immutable producer reconstructs every arrow
over each complete carrier and hashes the exact JSON integer array.

The theorem check uses integer-bitset adjacency, distinct from the original
set-based graph update. Every arrow digest agrees with the original. For
every source it follows the orbit to the first repeat independently of the
claimed bound, compares exact depth and period with D1/D2, and verifies all
changed edges, outside data and the frozen decorated local-machine update.
For every target it compares D3's degree-only inverse with the actual full
predecessor bin, checks distinctness, and tests the three-parent equality
condition. All three-parent target masks are printed. This is author
cross-implementation, not independent review.

## Before/after and current-input audit

`PAIR_INPUTS_BEFORE.json` and `PAIR_INPUTS_AFTER.json` are equal in both
scopes. In every execution, `INPUTS_BEFORE_SHA256SUMS` and
`INPUTS_AFTER_SHA256SUMS` are equal. Consumed history is copied in full,
including the sidecar's proof and the original canonical stdout. The top
historical manifest pins 11 workspace-root-relative historical originals;
the sidecar's root-relative historical manifest pins those 11 plus five
original-scout inputs. Neither manifest is presented as a self-contained
directory-relative artifact seal.

Every runtime record covers the interpreter executable, imported modules'
available source and cached files, and file-backed ELF/shared-library
dependencies present in `/proc/self/maps`; version, flags, import path,
module map, byte order and actual environment are retained. All 95 runtime
file hashes and the complete before/after runtime dictionaries match for
each process. This pins the observed dependency closure, not an assertion
that kernel or external operating-system state was snapshotted.

The additional actual command

```sh
python3 -I -B docs/papers204_208_sequence/scouting/finite_systems_sixteenth/audit_and_seal.py audit
```

exited zero. Its `AUDIT_RECEIPT.json` contains actual second raw `cmp`
commands and results, actual `sha256sum -c` checks for copied and historical
inputs, exact runtime counts, and comparisons of current live inputs and
runtime file hashes against the recorded pins. All checks passed. The
audit additionally compares original and sidecar arrow/depth digests and
asserts the original 26-box census and the sidecar's zero-new-box count.

## Seal contract

After final reports are written, the one-shot `audit_and_seal.py seal`
generates `SHA256SUMS` over every file recursively in this exclusive scout
directory except `SHA256SUMS` itself, rejects symlinks, and actually runs
`/usr/bin/sha256sum -c SHA256SUMS` from this directory. Its successful command
output is the final handoff's validation evidence. No validation-output file
is appended afterward, avoiding an unsealed artifact or a circular digest.
The author cannot overwrite an existing execution, receipt or seal with
these recorders. No central index, old artifact, manuscript or Git path was
edited by this scout.
