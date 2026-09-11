# Root documentary receiver failure01

Actual native c5feb8 exited1 before any successful result or seal. The original
receiver source cb8690b6…da27067 and complete RECEPTION_NATIVE01_FAILURE.json
remain unchanged. Its broad substring test searched inside a complete read
of the old source02 checker and matched that checker's own truncation-detection
string. This was a receiver expectation error, not truncated P212 source,
a driver run or an operational incident.

New-only receive_source02.js replaces only that substring test with an exact
outer-output header test and additionally includes its own source in the full
input set. Every successful saved source range must still equal the complete
current source range byte for byte, and each required multi-range source must
still reconstruct its entire EOF. No malformed or truncated source is waived.
The original plan's documentary-only authority extends only to this exact
two-line correction. No submitted-source, query, host-body or build permission
is added. Its actual complete diff, next result and native return are recorded
separately; this disposition alone does not assert a successful corrected run.
