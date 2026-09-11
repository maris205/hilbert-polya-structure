# P208 pre-execution author scope

Frozen before the first new paper-local producer, 2026-09-06 UTC.

Full carriers: every labelled triangulation for n=3,4,5,6,7,8,9,10.
Equivalent trees have m=n-2 internal vertices, N=n-1 leaves.
Formal e is auxiliary and is not counted as a polygon state.
No larger scouting or proof-repair cutoff is authorized by this declaration.

Adapt the original author tuple/geometric code verify_ofs.py. Do not import
it at runtime and do not copy the independent gate verifier. Reuse is author
reuse, not an independent implementation. Preserve the original source in
provenance/. Add complete canonical graph and source-set payloads, explicit
labelled diagonals, assertion-enabled runtime guards and both parity witness
identities. Retain the original auxiliary identity subboxes: G-squared and
frozen-cherry tests m<=6; KG tests m<=7, so constructed trees stay within
the same maximum internal size eight. Complete F and inverse graph checks
still cover every m=1,...,8. No external data, lookup tables or old checker
imports may be needed in an execution directory.

Record three distinct source-only directories: initial full stdout creation
and a subsequent pair against that canonical. Use python -I -B, require
optimize=0, isolated=1 and dont_write_bytecode=1. Capture complete live input
bytes/hashes before and after, interpreter/hash, actual standard-library
module origins/hashes from a same-import runtime probe, ldd output,
environment/settings, command/stdout/stderr/exit for every child and actual
/usr/bin/cmp results for both canonical comparisons and pair equality.
A source-only execution directory starts with only verify.py. Evidence
snapshots are outside those directories. Do not overwrite any existing
run/canonical; every failure is retained in its exclusive directory.

This is author numerical pressure and not the all-parameter proof, external
review, independent manuscript review or terminal root replay.

