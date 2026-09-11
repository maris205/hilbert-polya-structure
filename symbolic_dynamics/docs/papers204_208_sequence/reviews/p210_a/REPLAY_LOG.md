# Review A actual replay evidence

The independent checker is `verify.py`, committed before semantic author code
or canonical reading. Its source hash is
`4d152ceb7eebb8f1b4bf7632ad1a91f8be7e373520682022843fa6e81dd2de9b`;
parameters hash `854c270325ec270875863ed1110106ea397b1587f3da7f67876e4ce1d84e6de0`.
The complete actual stdout canonical is703850 bytes, SHA256
`d96ed0240dec421d78cdbfb013869680c91685c1848ea2ee030a71f86ab7aa74`.
It has133978 checks, all4095 states/edges/targets at N=1..12, full trajectory
events/source sets/suffix first sets,265 image/triangular objects and28 surplus
witnesses. Schema and every table column are declared in the canonical itself.
No canonical field was replaced by a digest-only summary.

## Selected fresh pair

`pair02/` is the selected complete fresh pair after the launcher correction.
Its parent actual command/exit/raw streams are in `execution/pair02/`.
It uses the source-only capsule copied from original A code/parameters/design
and canonical, not author or candidate scientific code. From the workspace root:

```sh
/usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p210_a/absent_record_pair02 docs/papers204_208_sequence/reviews/p210_a/record.py pair02 /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p210_a/absent_driver_pair02 docs/papers204_208_sequence/reviews/p210_a/instrumentation/evidence.py pair --paper docs/papers204_208_sequence/reviews/p210_a --out docs/papers204_208_sequence/reviews/p210_a/pair02
```

Do not rerun that command into its existing output. Each new driver, outer
recorder and scientific invocation must have an explicit new absent cache
path; the new package output must also be absent. The two scientific commands
are completely recorded in `pair02/commands/run_1/ATTEMPT.json` and run_2's
counterpart. Both use `/usr/bin/python3.10 -I -S -B -X pycache_prefix=...`,
the copied runtime probe and copied independent verify.py. The working
directory is `pair02/source`; PARAMETERS.json is read there. `-O` is absent,
site is disabled, and all three driver/scientific cache paths remained absent.

Both native exits are0. Each complete raw stdout is preserved under its
command folder; both have133978 checks. Native `cmp_pair`,
`cmp_1_canonical` and `cmp_2_canonical` all exit0. These are actual raw byte
comparisons, not decoded JSON equality. Both `ldd` commands also exit0.
The complete2631-path INPUTS_BEFORE/AFTER inventories are equal; every
observed import/open/maps file is in that key and no site package or old byte
cache was consumed. Inputs include original/copy code, parameters, canonical,
helper code, interpreter, stdlib, shared libraries, ldd dependencies,
loader/locale/gconv settings and relevant configuration. Exact environment,
sys.flags, xoptions, sys.path, modules, imported files and bounded open/map
observations are in CONTEXT.json and runtime_1/2.json. This is not an OS or
startup syscall trace. `REPLAY_KEYS.json` gives exact file keys and replay
schema; its listed complete inventories, not only the main-script hash,
constitute the runtime reuse key.

## Production, earlier pair and supplemental comparison

`produce01/` is the actual first native0 production; its full stdout was copied
to CANONICAL.json. The first production completed before semantic author
checker reading. `pair01/` also has two complete native0 runs and all three
native0 comparisons. The scientific child artifacts remain unchanged, but
its parent launcher metadata has the historical sanitization failure described
in `SANITIZATION.md`; it is not the selected full-parent acceptance pair.
The first production's parent launch was the actual direct tool invocation,
not a later invented file receipt. No root run is labelled as A evidence.

AFTER commitment, `compare_author.py` reads both complete canonical files and
checks every scientific author field against A's independent graph/data:
edges, full trajectories, every deleted cut/new block and its parent list,
all source sets, all24576 suffix endpoint sets/counts/branches/minima, every
attaining preimage, all triangular decodings, endpoint coefficients,
fixed/depth summaries and28 witness orbits. `execution/compare_author02/`
is the selected fresh native0 whole-data comparison:300628 predicates, full
stdout, unchanged three exact input hashes. The earlier identical comparison
is retained with its parent-metadata caveat. Different canonical schemas are
NOT said to be byte-equal; author assertion-category counts are checked for
internal consistency, not counted as A's scientific checks.

## Root replay interface

Run original `verify.py` twice with the original absolute PARAMETERS.json,
or copy precisely these source inputs into a fresh root-owned capsule. For a
direct call, use the template in REPLAY_KEYS.json with an absent absolute cache
prefix and capture complete stdout. Compare both outputs to the original
CANONICAL.json and each other using native cmp. Check the full relevant
dependency key before/after; do not reuse A's driver receipt as a root run.
This review does not itself perform or declare root acceptance.
