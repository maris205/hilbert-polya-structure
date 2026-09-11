# One-use P214 terminal02 grant

2026-09-11 UTC. After terminal01's actual operation returns, freshly recheck
the same source/evidence/runtime pins and terminal02 path absence, then execute
exactly once `BUILD_REQUEST.sh --execute-under-separate-root-grant terminal02`
under the same clean environment. Preserve failure without cleanup or retry.

