# P215 Review B initial DATA receiver root correction

2026-09-11 UTC. `POST-CAPTURE CORRECTION / NO PRECOMMIT CREDIT`.

The separately prepared source02 receiver was executed once under its recorded
grant and failed before scientific reconstruction because it required every
runtime manifest path to be a non-symlink under `lstat`. The preserved failure
is `p215_b_data_receiver_source02/run01`; the first rejected runtime member was
the normal versioned library link `/usr/lib/x86_64-linux-gnu/libstdc++.so.6`.

This source03 file is an exact copy of source02 except for its own output root,
root correction-grant identity, and runtime-row file-type check. Runtime rows
now use `stat`, require the resolved target to be a file, read through the
manifest path, and compare those actual bytes with the already captured hash.
All capture membership, pre/post logs, package pins, scientific input pins,
wire parsing, independent transition reconstruction, indegree layering,
height dynamic programming and recurrence checks are unchanged.

The capture already exists, so source03 claims no precommit credit. It is a
transparent post-capture checker correction and may establish initial DATA
only. It cannot establish canonical adoption, strict replay, delta, final B,
build, Round2, paper completion, batch completion, Git sync or external action.
`HOLD_EXTERNAL`.
