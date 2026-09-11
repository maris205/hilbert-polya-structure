# P200 Review A fresh replay log

Replay1: a fresh process ran verify_independent.py after the first successful
development run. Complete stdout was captured and saved as CANONICAL.txt.
Replay2: another fresh process ran the same verifier under shell pipefail
and piped stdout to cmp against that canonical. Exit0: byte-identical.
Each contains3823696assertions. Deterministic Python-standard-library code;
no seeds, timings, author imports or cached graph files.

Verifier SHA256 fe67ec5db04107fc4ab70ea269b3f1b4c491cfc75ea07f4cf2eb72c55f79c288.
Canonical SHA256 5e886ccfb9f8ad2a4f643cd8c026628bf7ef01101b366084d12e41c4bfb8f149.
All-size deductive reasoning is separate in PROOF_REDERIVATION.md.
