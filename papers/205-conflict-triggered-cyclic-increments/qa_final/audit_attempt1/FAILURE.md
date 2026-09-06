# Initial terminal auditor layout failure

2026-09-06 UTC. The original `audit_p205.py` execution exited 1 at its
first A after-pin check. It incorrectly assumed the B filename
`AFTER_INPUT_PINS.sha256` also existed in A. The actual accepted A delta
uses `AFTER_FROZEN_PINS.sha256` and `AFTER_LIVE_PINS.sha256`.

The original failed auditor bytes and empty stdout are preserved here.
The traceback was displayed in the execution record (not separately
captured as original stderr). No scientific producer or build failed;
this was an auditor layout error. The scoped correction explicitly maps
the two actual accepted layouts. No historical/review file was renamed,
no parser was relaxed to ignore missing evidence, and this attempt is
never counted as PASS. A new actual execution is required.
