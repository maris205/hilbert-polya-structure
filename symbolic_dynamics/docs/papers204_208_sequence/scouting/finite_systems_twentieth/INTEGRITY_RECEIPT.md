# Actual archival-check receipt

Date: 2026-09-06 UTC. Scope: **checksum integrity only**, not scientific
execution, proof review or admission.

[ARCHIVAL_VALIDATION.json](ARCHIVAL_VALIDATION.json) preserves the actual
four command invocations, UTC start/end returned by the clock, exit codes
and full combined terminal output. All four commands exited zero:

| Check | Base directory | Actual passing lines |
|---|---|---:|
| Historical originals before | workspace root | 18 |
| Nine pre-validation payloads before | this lane | 9 |
| Same payloads after | this lane | 9 |
| Same historical originals after | workspace root | 18 |

The terminal interface returns combined output, so this archival receipt
does **not** claim separate stdout/stderr capture. The report's “as returned”
output wording refers to this exact limitation. No scientific run is being
reused on the strength of these checks. No scientific interpreter, imported
module, mathematical runtime or source-state enumeration was invoked or
certified. Accordingly no scientific runtime capsule, producer-pair raw
comparison or canonical bytes exist; those roles are NOT_APPLICABLE.

VALIDATION_INPUTS.sha256 has nine directory-relative entries and excludes
itself and later receipts. It is an **inner input list**, not the outer
complete manifest. HISTORICAL_SHA256SUMS has eighteen workspace-root-relative
entries and is not interpreted relative to this lane.

The final SHA256SUMS is generated after this receipt and includes every
owned payload, including both pin lists and ARCHIVAL_VALIDATION.json, while
excluding only itself. Its terminal nonself hash/coverage check happens
after seal construction; that outer tool output is not inserted into its
own payload set. Root can independently repeat the following read-only
checks from this lane:

```sh
sha256sum -c SHA256SUMS
sha256sum -c VALIDATION_INPUTS.sha256
cmp <(rg --files -g '!SHA256SUMS' | LC_ALL=C sort) <(sed 's/^[0-9a-f]\{64\}  //' SHA256SUMS | LC_ALL=C sort)
```

And from `/root/autodl-tmp/symbolic_dynamics`:

```sh
sha256sum -c docs/papers204_208_sequence/scouting/finite_systems_twentieth/HISTORICAL_SHA256SUMS
```

The two `cmp` inputs in the coverage command are exact newline-delimited
path lists, not normalized mathematical producer output. There are no
scientific executions, independently accepted findings, paper assignments,
central edits, Git synchronization or external release certified here.
The preserved negative theorem/value/source boundaries remain in force.
