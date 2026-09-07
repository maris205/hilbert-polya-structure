# Actual independent mathematical and documentary execution

Final accepted gate pair: [pair03/RESULT.json](evidence/pair03/RESULT.json).
Both child executions ran the SAME standalone `verify.py` on all positive
compositions with N=1…12: 4,095 states, 115,680 named checks each. The full
1,562,038-byte stdout is [CANONICAL.json](CANONICAL.json), SHA256
`233944c44f8b72ce17495c0f16665dcaac77974c60251275403b98118f68a731`.
Both stdout streams, both empty stderr streams, every command/exit and all
three actual `/usr/bin/cmp` comparisons are retained under `evidence/pair03/`.

The real successful outer command was:

```text
python3 -I -S -B docs/papers204_208_sequence/scouting/MNA_GATE/record_outer_v3.py pair_v3
```

That records the entire native stdout/stderr and exit of `run_pair_v3.py`.
The mathematical children use `/root/miniconda3/bin/python3.12 -I -S -B`
and an explicit, nonexistent `-X pycache_prefix=.../cache_must_remain_absent`
through `run_observed.py`. The environment is exactly PATH=/usr/bin:/bin,
LANG=C.UTF-8, LC_ALL=C.UTF-8, TZ=UTC. Optimization is zero, site loading is
disabled, bytecode writes are disabled, and the alternate cache path remains
absent. The instrumentation compiles the current verifier source and adds
only runtime observation; it imports no author/pilot/old scientific code.

Before and after pins cover 997 known inputs: the exact reviewed physical
copies, current verifier/instrumentation/recorders/canonical, the interpreter,
stdlib source/extension superset, resolved ldd objects and locale/loader
resources. Every before/after pair matches. Each runtime records 55 observed
file keys, of which one is the changing `/proc/<pid>/maps` observation itself.
All 54 reusable ordinary-file keys per run are in the before capsule with
matching sizes/hashes. Raw process maps and exact interpreter flags, modules,
open-event paths and sanitized environment are preserved.

This is not an OS syscall trace: `strace` is unavailable. It is a documented
known-input capsule with Python-open/module/mapped-object observations. Do
not promote it to exhaustive kernel-level file-read monitoring or a terminal
manuscript reuse certificate. The volatile proc maps key is explicitly not
reused as an immutable input.

## Preserved actual failures and chronology

1. `run_pair.py` produced pair01, two successful mathematical runs and three
   successful raw comparisons, then FAILED its final provenance check on
   missing `/usr/lib/locale/C.utf8/LC_CTYPE`. Complete child streams survive.
   Its outer traceback survives as the labelled actual tool-return
   transcription, not a newly claimed native outer capture.
2. Distinct `run_pair_v2.py` produced pair02 with locale pins, again two
   successful mathematical runs and three comparisons, then FAILED on
   missing `/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache`. Its actual
   complete outer stdout/stderr and exit 1 are in `evidence/outer_pair_v2/`.
3. Distinct `run_pair_v3.py` fixes that exact dependency and produces the
   successful pair03. Mathematical source and canonical remain unchanged.
   No old failed source, input inventory or receipt was repaired in place.

Thus there were SIX actual mathematical executions in this independent gate,
all at the SAME assigned cutoff. Only the final pair has accepted provenance
closure. None is a second author scouting pilot, a new literal or a larger
experiment. The canonical was first emitted during pair01 and preserved;
the final accepted pair compares actual raw bytes against it, not its hash
alone. No finite execution proves the all-size statements.

## Full author-output comparison

[author_comparison/RESULT.json](evidence/author_comparison/RESULT.json) records
40,969 checks over all 4,095 frozen original pilot state rows, all twelve
complete summaries, and the original event census. Every scientific field
matches the independent reconstruction. The two 647,902-byte complete
scientific projections were actually compared with `/usr/bin/cmp`, exit 0.
Only the ordering of maximum-fibre target lists is normalized (the author
orders by cut mask, the independent checker lexicographically). No original
full stdout raw-identity claim is made between different implementations.

The original author's 712,674-byte output, exact six declared inputs,
pre-pilot source, contract, proof and actual original execution receipt are
preserved under `inputs/author_lane40/`. The post-pilot bijection addendum is
labelled post-pilot and is first independently pressure-tested here. This
gate does not invent an earlier bijection execution or retrospectively supply
an OS capsule for the old author pilot.

## Non-numerical evidence boundaries

The one-shot freeze validated the assigned 155-payload author seal, copied
all payloads and compared exact bytes; INPUT_ROLES contains the complete
program result. Its terminal display was truncated, so that display is not
called a complete stdout capture. The actual stored result and copies are
the evidence. Web request/result objects are browser return serializations,
not native downloads. Candidate stage requires no manuscript build or page
view; none was performed.
