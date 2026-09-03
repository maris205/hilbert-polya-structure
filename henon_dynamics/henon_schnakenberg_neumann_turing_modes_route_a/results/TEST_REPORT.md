# C350 test report

All release lanes pass under ordinary Python and explicitly refuse both
`python -O` and `python -OO`.

- Independent checker: 150 assertions.
- SymPy lane: 14 exact identities.
- Isolated byte replay: 2 independent copies.
- Hostile mutation suite: 60/60 attacks rejected.
- Evidence: 9 case rows, 63 modal rows, and 20 length-wall rows.

The release gate additionally validates strict JSON and YAML parsing, raw and
semantic evaluator locks, the self-excluding evidence payload hash, all 27
manifest payloads, deterministic fresh PDF builds, embedded/subset fonts,
text sentinels, rasterization, and absence of build sidecars.
