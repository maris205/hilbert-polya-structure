# P208 strict root author replay supplement

Actual 2026-09-06 UTC root reproduction, not an independent review and not
a manuscript change. The original author package, 487-input Round0, earlier
root pair and their original limitations are preserved byte-for-byte.

The new [scoped recorder](replay_p208_strict.py) completed two source-only
author executions. Both passed 62,101 assertions on all 2,055 states in the
unchanged n=3..10 boxes; the complete graph/source output matches the
paper canonical and the other run by three actual raw `cmp` commands.
All seven child commands exited zero. See the complete
[receipt](root_replays/p208_author_strict/RECEIPT.json) and
[38-entry nonself seal](root_replays/p208_author_strict/SHA256SUMS).

This pair uses isolated, no-site, bytecode-disabled Python (`-I -S -B`),
optimization zero and a distinct nonexistent bytecode-prefix directory for
each run. Neither prefix was created. Each working directory began and
ended with only the unchanged `verify.py`. The inline wrapper executes the
pinned source bytes with `compile(..., optimize=0)` and preserves the exact
canonical stdout; it records actual consumed module files and process-mapped
files separately. Root wrote/read the full recorder before execution.

Before/after checks passed for 981 scientific/documentary inputs, 918
runtime-inventory files, 112 resolved dynamic-link files and 29 loader or
path-configuration entries (including absent paths). Each run's 43 consumed
module files and 12 mapped files were covered by the before inventory and
rechecked after execution. Site packages are disabled; source bytecode
cannot be silently substituted from an old cache. The ldd script, Bash,
comparator, interpreter, standard-library extensions and their resolved
libraries are included. This is concrete dependency evidence, not an OS or
kernel snapshot or a claim of universal hermeticity.

The 981 inputs comprise 484 author-seal items, 488 Round0 items, eight
historical-origin archive items and this recorder. The seven historical
admission documents are consumed from the earlier validated archive;
their hashes exactly match the original provenance list. They do not
pretend to pin a future mutable central contract or lifecycle index.

Root subsequently independently rechecked the complete 38-entry coverage,
every input/runtime/library/configuration reference, all seven saved command
records and stream hashes, both canonical payload counts and actual consumed
files. Actual closure output is saved in
[the inspection record](P208_STRICT_AUTHOR_INSPECTION.actual.json).
Seal SHA-256: `5629ada257a37afd0fcbdbc562472cfd4fc10075fdc2d4d160b3d6709f1e3704`.

Chronology limitation: the launch tool's displayed response inadvertently
omitted its background-session identifier. Root does not invent a recovered
parent-shell exit status; the actual completed receipt and each of its seven
child exit records were inspected afterward. The full output and failures
array are retained. There were no child or validation failures in this pair.

This supplement repairs the affected replay-reuse provenance only. It does
not accept manuscript A, waive B or terminal builds, or complete the batch.
All external actions remain `HOLD_EXTERNAL`.
