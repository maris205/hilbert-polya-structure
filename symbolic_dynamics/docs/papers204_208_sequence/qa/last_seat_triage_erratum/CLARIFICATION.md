# Sealed last-seat triage table: documentary clarification

2026-09-07 UTC. This is the requested standalone erratum check; it changes
no byte of the sealed 163-payload triage package and no scientific claim.

Root reported a NED table entry naming `FINAL_SOURCE_BOUNDARY.md` while
command 17 actually reads `SOURCE_SUPPLEMENT.md`. The wrong name occurred
in the **pre-seal draft** and was corrected before the documentary audit
and final seal. The current sealed `TRIAGE_REPORT.md`, line 42, already
names `SOURCE_SUPPLEMENT.md`, matching command 17. It would be inaccurate
to say the sealed bundle still contains that typo or to overwrite it.

The same pre-seal correction also aligned the NCC, CTM and GCF document
names with their actual read receipts. This check compares every explicitly
named basename in all six table rows against the relevant native argv;
generic references to ORR intake/pre-code/source portions are additionally
resolved through commands 14–16. No additional candidate body is read.

The preserved seal hash is
`186a6f0463aec4e02a12e6bccef78f9bb700c0dd569704a2f84c8819fb370231`.
The check pins the report, its seal, table-command receipts, and all six
command-17 receipt/raw/pin artifacts, and checks that the report still
matches its entry in the old seal. `check/` contains actual before/after
pins, command, exit and complete stdout/stderr. These are documentary
checks, not fresh source reading or scientific replay.

Conclusion: **NO_ERRATUM_TO_SEALED_BYTES_NEEDED**. The name correction is
documented here for anyone who read the earlier draft. The sealed triage,
ORR diagnostic and Scout33/34 files remain immutable.
