# Preserved resumption archival-check failure

2026-09-07 UTC. `resume_closure.py` is retained unchanged.

The first resumption closure completed all eight original/snapshot input
checks and raw comparisons, found both 166-file science maps and 932-file
runtime maps unchanged against current files, found no change in any of the
3,162 historical search/tool pins, and verified all 1,004 originally sealed
payloads unchanged. It then wrote an expanded manifest and successfully ran
the full checksum command. Its final **path-list ordering** comparison failed
with actual exit one:

```
Traceback (most recent call last):
  File "/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/scouting/FTH_GATE/resume_closure.py", line 108, in <module>
    raise RuntimeError("INCOMPLETE_NONSELF_MANIFEST")
RuntimeError: INCOMPLETE_NONSELF_MANIFEST
```

Cause: the manifest's paths were ordered by `Path` component comparison,
while the coverage check sorted relative-path strings. A root file such as
`resume_closure.py` and the sibling directory `resume_closure/` sort in
different relative orders under those two conventions. This was a checker
representation mismatch, not a missing payload or failed checksum.

The expanded attempted manifest has SHA256
`5f8148dfc52d5fede1929d97fa72b2a14af4cefbbe5dd9d191a67da7be530858`
and is preserved by the final closure before any replacement. The PASS in
`resume_closure/RECEIPT.json` describes the completed input/runtime/history
checks; it is **not** the final closure verdict, since the process failed
after writing it. The original 2026-09-06 1,004-payload seal is also retained.

`finalize_resume.py` normalizes both coverage lists to sorted relative-path
strings, checks the actual file sets/counts and raw-compares those normalized
path lists. It performs archival checks only. No scientific kernel, recorded
run, theorem contract, source body, gate report or canonical output changes.
There remain exactly two scientific replays and no failed mathematical test.
