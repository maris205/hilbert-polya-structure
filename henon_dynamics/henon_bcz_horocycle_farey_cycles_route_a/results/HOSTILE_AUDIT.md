# Hostile-input audit

Actual execution: 50 of 50 attacks rejected, process exit zero for the hostile
test harness. Thirty-six JSON semantic mutations repaired their payload hash:
scope/tuple/epoch/contract drift; omitted layers or cycle points; changed
endpoints; unreduced or Boolean rationals; wrong floor, roof or matrices;
wrong powers; smoothness promotion; omitted fixed layers; finite-cardinality
substitution; nested unknown keys and integer-to-float summary drift.

Two raw JSON attacks test duplicate keys and NaN. Six YAML changes each run
through two actual entrypoints: checker evaluation-only and release --write.
They are an unknown key, false-to-zero, unquoted date, duplicate key, true
target flag and integer-to-float epoch. The release invocation must fail with
the explicit preflight evaluation rejection; a later missing-file error is
not accepted as evidence. The manifest bytes, or its absence before first
release, remain unchanged after every actual-write attack.

Smoke separately executes -O and -OO against all six scripts and checks the
specific optimization-refusal diagnostic before argument processing. Thus
assert-based validation is never silently disabled.

Boundary meaning is not inferred from attacks: the independent proof supplies
the discontinuity and continuous-family results. Mutation coverage is bounded
by this named population and is not exhaustive security certification.
