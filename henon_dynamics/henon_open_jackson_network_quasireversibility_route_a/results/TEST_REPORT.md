# Test report

All commands were run from the package root under ordinary Python with bytecode
disabled.

| lane | final result |
|---|---:|
| canonical producer | PASS, 12 networks / 1,020 balances / 84 visible reverse rows |
| producer-independent checker | PASS, 1,215 assertions / 1,134 ledger rows |
| SymPy cross-check | PASS, 9 symbolic identities |
| isolated byte replay | PASS, 2 directories / 356,885 identical bytes |
| hostile mutation suite | PASS, 80/80 rejected |
| optimized execution | PASS, every script rejects both -O and -OO |

The checker imports no producer code. It solves each rational traffic system by
Cramer's rule while the producer uses Gauss--Jordan elimination. Exact row
ownership includes all nested keys, coordinate sets, row order, section
digests, source tokens, scope flags, and raw/semantic YAML bindings.

The release gate additionally rebuilds each manuscript round twice in fresh
directories, checks byte identity, settled logs, embedded/subset fonts,
extracted text, rasterization, the three revision sentinels, and exact manifest
closure.
