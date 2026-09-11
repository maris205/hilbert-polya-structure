# P214 Review A execution preparation

SOURCE only. `RUN_GUARD.sh` fixes the accepted review verifier hash, checks all
25 workspace-relative source pins before execution, permits only the three
named absent output directories, captures exact raw stdout/stderr and exit,
and checks the four current review keys before/after. It has not been run.

Each invocation requires its own root grant. The initial run may establish a
candidate raw output; canonical adoption follows only after complete DATA
reception. The two strict runs are separate later invocations and must compare
whole raw bytes to the adopted canonical, initial and each other. This guard
does not itself perform those receptions or comparisons.

OWNER_AMBER / HOLD_EXTERNAL.
