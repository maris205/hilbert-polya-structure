# Exact P208 canonical-operand correction — revision 01

Preparation only: this revised checker has not been executed. The original
checker/launcher preparations and actual failed `p208_p209_reuse_01/` remain
unchanged. Root owns the next actual execution and acceptance decision.

## Actual failure and precise correction

Root's actual first launch returned native exit 1. The checker stopped at
`p208_a`, after 79,727 predicates and 11,844 observed current paths, on
`Archived exact raw comparator`. The parent recorded settled process-group
absence and unchanged known/scoped/configuration/runtime keys. Its 20-payload
failed package is sealed by
`88d504f5a04a74c0e03f313946180899ba3259f4d9d554e8fa59068bee0314a3`.
This does not establish any of the later, unvisited checker gates.

The original P208 commands are exactly:

```text
cmp producer/CANONICAL.json run1.stdout
cmp producer/CANONICAL.json run2.stdout
cmp run1.stdout run2.stdout
```

The first adapter expected the canonical operands in reverse order. Original
`replay_p208_strict.py` lines 241–242 and `replay_p208_b_strict.py` lines
263–264, plus all six original canonical command JSON records, establish the
canonical-first order. The revision transcribes that exact order. It does not
accept arbitrary ordering, remove an argument check, alter raw comparisons,
or modify an original command, canonical output, scientific input or alias.

`SOURCE_DELTA.diff` is the complete three-hunk change: revision preparation
path, the single canonical-target ordering expression, and this preparation's
seven-payload membership count. The original pair-comparison order is unchanged.
`INPUT_PINS.json` and all six `ALIASES.json` declarations are byte-identical to
the originals; there is no new scientific/runtime/documentary fallback.

## Bounded native-argument inspection

The preparation's direct read-only schema diagnostic checked all 52 explicit
native argv expectations in the adapter against original sealed raw records,
and all 52 embedded/native or outer/pre-spawn bindings. It pinned 85 original
record/manifest/source-snapshot files and reread those records at completion.

| Expected argv category | Exact matches after correction |
| --- | ---: |
| P208 wrapper children | 6 |
| P208 canonical comparisons | 6 |
| P208 pair comparisons | 3 |
| P209 producer children | 6 |
| P209 canonical/pair comparisons | 9 |
| P209 outer pairs | 3 |
| Terminal TeX passes | 12 |
| Terminal PDF comparators | 6 |
| P209 outer build | 1 |

P209 canonical comparisons remain stdout-first and include `--`; neither
their order nor the terminal PDF order changed. The independent argv desk
found the same six original adapter mismatches and no additional mismatch.
This is bounded archived argv-schema inspection, not execution of either
checker/launcher, a full current runtime check, mathematics or a build.

`STATIC_CHECK.json` preserves the exact diagnostic command and complete native
output, the static source/AST comparison and its native result, and the
expected exit-1 unified diff generation. `FAILURE_PINS.json` pins all 34
physical files of the original two preparations, failed output package and
root launch/completion records. Those files were checked unchanged during
preparation; this metadata does not add a new runtime audit layer.

## Future execution

The companion `qa/p208_p209_reuse_launcher_revision_01/` launches this source
directly into the new fixed `qa/p208_p209_reuse_02/`, with distinct absent
parent and child caches, exact ENV4 and system Python `-I -S -B`. Root must
read both complete revised sources and deltas and verify their final seals
before running either. The old `reuse_01` must not be reused or overwritten.

All original checker scope and limitations remain as in the preserved
`qa/p208_p209_reuse_preparation/README.md`: six original strict pairs, two
terminal build pairs, unchanged actual prior all-page views, exact current
known keys and six documentary aliases. Success still means only
`PASS_CURRENT_KEYS_REUSED_NOT_NEW_EXECUTIONS_OR_BATCH_ACCEPTANCE`.
No new science, build, view, review, Git operation or central edit occurred.
`HOLD_EXTERNAL` remains in force.
