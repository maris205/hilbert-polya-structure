# C161 test report

The producer, independent checker, SymPy path, replay, and hostile mutation
suite pass.  The full independent checker records 483,310 assertions while
recomputing 261,630 amplitude-formula cases and 164,284 prime zero-level cases.
The independent SymPy path records 15,834 exact checks.  The mutation-fast path
retains schema, theorem, sentinel, scope, operator, antiunitary, and Route-A
closure while avoiding repeated full sweeps; it rejects 29 repaired-hash
mutations and one stale-hash mutation.  PDF determinism, font embedding,
warning scans, and manifest closure are recorded in `paper/COMPILE_REPORT.md`.
