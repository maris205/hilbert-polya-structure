# Actual discovery-scope failure and documentary limitations

This is an adverse record, not a retrospective correction of an original
search. It broadens the initial author-scout-path disclosure with the final
auditor's case-sensitivity finding. Root was told both findings.

## 1. What actually ran

The unchanged `discovery.py` is v1. Its original physical source and helper
are also in `history/discovery_v1_source/`, with a before/copy/after manifest.
Its exclusion regex omitted `order_geometry_tenth` and
`order_geometry_tenth_desk`, and it was case-sensitive. The actual lists
therefore also retained these five uppercase paths:

- `docs/papers204_208_sequence/P208_A_RESPONSE.md`
- `docs/papers204_208_sequence/P208_B_RESPONSE.md`
- `docs/papers204_208_sequence/P208_FINAL_QA.md`
- `docs/papers204_208_sequence/P209_A_RESPONSE.md`
- `docs/papers204_208_sequence/P209_ROOT_ADMISSION.md`

Together with 37 paths under the two author-scout directories, those are
42 known protected paths in **each** of the three original content searches.
The complete lists are in each `discovery/*/scope.json`, and the documentary
audit enumerates the protected subset without reopening those source files.

| Original search | Files actually searched | Full raw hit lines | Hit lines in the 42 known protected paths |
|---|---:|---:|---:|
| `initial` | 6,520 | 1,652 | 10 |
| `matrices` | 6,522 | 4,939 | 74 |
| `exact_cubic` | 6,522 | 40 | 0 |

All three recorded content exits were zero, with empty stderr and equal
before/after pins on their enumerated inputs. Each preserves the filename
scan's argv/cwd/exit/full separate streams, full scope list, content argv,
full separate streams, exit and both pin arrays. The zero protected hits in
`exact_cubic` do not undo its actual input access. Likewise the original
scope note saying “no excluded scientific-body scan” is an inaccurate v1
claim; it is preserved as originally produced and superseded by this record.

The discovered paths include scientific proof and matrix-independent OFS
math-code files. These were scanned by rg; they were not executed. It is
incorrect to describe rg snippets as full-body proof reading, and equally
incorrect to claim clean scientific nonaccess. Direct P208/P209 manuscript
files were not separately opened. Mandatory central contracts included
their theorem summaries. **P208/P209 reviewer eligibility is not established.**

## 2. Correction only for the remaining search

`discovery_v2.py` adds the exact two missing directory exclusions, makes
exclusions case-insensitive and asserts the known author directories absent.
The distinct `corrected_final` search examined 6,456 files and returned
17 raw hit lines, exit zero and empty stderr. Its before/after pins match.
The documentary audit finds zero of the 42 known protected paths in it.

The corrected source, scope, raw streams and pins are separate. No v1 source,
search record or at-time pin was overwritten. This is **not** a retroactive
scope PASS, an independent review or evidence that every scientifically
sensitive path in the repository has been enumerated.

## 3. Other real failures and capture boundaries

The `nearby_originals` snapshot failed on the nonexistent
`scouting/algebra_third/INTAKE.md`, exit one, after copying its first target.
[FAILED_SNAPSHOT_01.md](FAILED_SNAPSHOT_01.md) gives the exact command and
complete actual merged terminal output. Its original API output did not
separate stdout/stderr, and there was no emitted pin manifest. The partial
physical directory is retained. `nearby_originals_v2` is a separate successful
operation on resolved targets, not a fabricated original success.

The primary PDF structural preflight exited zero but its substantive
verdict was **UNAVAILABLE**, `pypdf-not-installed`. That is not a successful
structural/page/visual check; see the original sidecar and captured command.

A late convenience attempt to summarize the documentary audit used `jq`
and actually failed. [FAILED_UTILITY_01.md](FAILED_UTILITY_01.md) transcribes
the exact shell command, cwd and complete actual merged terminal output,
`/bin/bash: line 1: jq: command not found`, exit 127. This is an after-the-fact
record, not an at-launch recorder or separated original streams. The
successful fallback is the distinct fully captured
`commands/documentary_audit_summary/`, which parses the existing JSON with
standard-library Python. Neither operation is science.

Some bootstrap/administrative shell reads, tool-level file displays and
filename-only discovery were not wrapped in `capture.py`. The initial
filename display was bounded by `head`; it is not the corpus-completeness
evidence. The four actual content searches have their own complete durable
records described above. Of the 49 completed wrapper commands examined in
the first documentary audit, 43 have no per-command explicit pin arguments;
their separate pre-read physical manifests or discovery pin arrays are the
relevant evidence where present. Do not claim universal at-launch command-
input capture, universal physical snapshots or hermetic execution.

Only one literal and zero pilots/scientific producer runs occurred. No
scientific assertion total, replay pair, source-owner clearance, independent
acceptance or new seat follows from these documentary checks.
