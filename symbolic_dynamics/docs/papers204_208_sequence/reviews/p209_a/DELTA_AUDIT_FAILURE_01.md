# Actual first documentary-audit failure

2026-09-07 UTC. `check_delta.py` actually exited 1; the complete returned
traceback and tool completion are preserved in
`delta_check_01/EXECUTION.actual.json`. Its script and all partial artifacts
remain at their original paths without modification.

The original complete measurements and pinned root receipt inspection had
reached the raw-comparison loop. Six actual comparisons exited zero, with
their pre-spawn attempts and complete empty stdout/stderr preserved. Before
the seventh comparison, the audit asserted that both compared files were
already in the combined input map. Live `ROOT_ADOPTION.md` had passed its
explicit fixed SHA256 check but had not been added to that map: it is not
one of the 1,985 historical author-manifest payloads. The protective
coverage assertion stopped the audit. There is no completed after-input
measurement, RESULT or PASS for attempt 1.

This is an actual reviewer-audit bookkeeping defect, not a manuscript,
proof, canonical or root-adoption byte mismatch. The append-only
`check_delta_02.py` / `delta_check_02/` retry adds the exact root-adoption
pin before both measurements, includes all predecessor evidence as inputs,
and verifies the already-created initial-seal alias instead of overwriting
it. No prior scientific artifact or checker implementation is repaired.
Neither documentary attempt launches mathematics, a build, a renderer or
a page view. Acceptance remains unasserted until the corrected closure
actually completes and the reviewer issues DELTA.md.
