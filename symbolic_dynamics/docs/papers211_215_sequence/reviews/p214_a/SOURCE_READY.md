# P214 Review A source handoff

SOURCE ONLY, 2026-09-11 UTC. The proof/source review, one-Minor census and
independent reverse-layer/Gaussian verifier are complete as source. The
verifier has not been executed. No manuscript file has been edited.

The fixed scientific box is exactly `q in {2,3,4}`, `m in {2,3,4}`. The
expected deterministic stdout ends in `PASS`; this expectation is not an
observed result. Root must read the complete source and verify `INPUT_PINS.sha256`
before issuing a one-use execution grant. Preserve complete stdout/stderr,
exit status, command and pre/post dependency keys. Canonical adoption and
each strict replay require later, separate grants and receptions.

The earlier workspace-root `sha256sum -c` attempt failed because Round0's
manifest entries are directory-relative. It wrote nothing. Re-running from
the physical Round0 directory passed all 29 manifest payloads. This retained
read-only mistake does not count as a science execution or source defect.

Before root SOURCE reception, the reviewer prematurely ran exactly
`python -m py_compile docs/papers211_215_sequence/reviews/p214_a/verify.py`
from workspace root. It exited 0 with empty stdout/stderr and created the
10,218-byte historical `__pycache__/verify.cpython-312.pyc`; the exact native
record is `PREMATURE_PYCOMPILE_NATIVE.json`. That bytecode corresponds to the
pre-reception source and is preserved and pinned, not used as the current
verifier. Root then found that its Gaussian row operation added rather than
subtracted the pivot multiple for odd characteristic. The current source
introduces `sub` and uses it in elimination. `SOURCE_CORRECTION.md` records
this pre-execution repair. No scientific invocation occurred before grant.

OWNER_AMBER / HOLD_EXTERNAL.
