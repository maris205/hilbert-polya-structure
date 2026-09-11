# First evidence capture: preserved infrastructure failure

Actual command:

`python3 -B docs/papers204_208_sequence/scouting/finite_systems_nineteenth/evidence.py capture`

Actual parent exit: 1. Both byte comparators had already completed with
exit 0; their raw stdout/stderr, command receipts, input hashes and runtime
before/after files remain unchanged in this directory.

The subsequent history-file inventory did **not** launch. The recorder
attempted the nonexistent absolute executable `/usr/bin/rg` and raised:

`FileNotFoundError: [Errno 2] No such file or directory: '/usr/bin/rg'`

The existing empty `history_inventory.stdout` and `.stderr` were opened
before the failed process launch; they are not successful search outputs.
No `history_inventory.command.json` exists because the exception occurred
before a child process/exit receipt could be produced. The actual traceback
was returned by the terminal call and is not represented as child stderr.

Repair: resolve `rg` from the invoking environment to its concrete installed
path, pin that path before/after, and capture again in a new
`evidence_capture_02/` directory. The scientific producers, boxes, raw
outputs, proof and comparator claims were not changed or rerun for this
infrastructure failure.
