# P215 Review B initial DATA root reception

2026-09-11 UTC. Root accepts the single previously captured initial B run as
initial DATA only. The actual child identity is recorded in
`p215_b_initial_binding01/ACTUAL_NATIVE.json`: session `27490`, initial chunk
`298a1f`, continuation chunk `283a1d`, exit zero and no retry. The capture has
exactly 27 files; child and controller exits are zero, all captured stderr is
empty, and all five classes of before/after pin logs are raw-identical.

The clean precommitted source02 receiver was sealed, but its one authorized
execution failed before scientific reconstruction because it rejected the
normal symlink `/usr/lib/x86_64-linux-gnu/libstdc++.so.6`. That failure remains
at `p215_b_data_receiver_source02/run01` and is not PASS evidence. Source03 is
a disclosed post-capture correction: only its output/grant identity and the
runtime check changed from `lstat` non-symlink rejection to `stat` resolved-file
validation followed by hashing the bytes read through the manifest path. It
claims no precommit credit.

The source03 run exited zero with empty stderr. Its independent indegree-layer
and height-DP receiver passed 51,999 checks, reconstructed all 5,704 states and
5,704 predecessors, performed 11,408 literal transition checks, and matched
all 30 carrier rows and closed forms. The verifier's emitted 68,196 assertion
count is retained only as an observed wire field. Actual stdout is exactly
1,739 bytes / 34 lines, SHA-256
`8c20881098141820fbc67fcce89879a634ea590501ed1909986228d7d69970a8`;
stderr is empty.

This establishes initial B DATA only. It is not canonical adoption, strict
replay, final Review B, build, Round2, paper completion or external release.
`HOLD_EXTERNAL`.
