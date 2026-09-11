# Root decision: exact P213 enabled-byte materialization only

2026-09-10 UTC. Root accepts the frozen exact source/request reception
../p213_minimal_observer_enabled_root01/RECEPTION.md, 7,131 bytes,
SHA256 6a5ccbc053bc8bd2134466a0dfbeb44c01a7745e4cdc974e7a3656df36726c85,
and its eight-payload seal
43c9e6401cd9189461df4e081d6d6aff219afb1bab8bd82df82d0b6cbdccf45c.

This decision authorizes only checking the existing batch qa parent directory
as ordinary trusted storage, its filesystem available bytes (minimum 64 MiB),
the exact new enabled01 directory's absence, exclusive nonrecursive creation
of that directory, and exact file materialization by apply_patch:
- enabled01/observe.py from the complete reviewed observe.proposed.py.txt,
  98,365 bytes, 6cdc550357b0b6f8322ecc8e22d2fca9ff1d22ee5d9a46caf0c191fcc81ff25d;
- enabled01/capture.sh from capture.proposed.sh.txt,
  1,949 bytes, da71d93c5fd8c587ecbdeec339e054b6c6c0aa56a5c682b901a1c3c038b8705d.

Here enabled01 means the exact
/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p213_minimal_observer_enabled01
directory. No other source path may be substituted. Existing destination,
any byte mismatch, nonregular/link leaf or insufficient capacity is HOLD:
preserve artifacts and do not overwrite, alter permissions to repair a
mismatch, or choose a new runtime path silently.

Record full byte comparisons, exact file keys and directory inventory.
Ordinary parent/owner/kernel trust is inherited; this does not attest
ancestors, native tools or pre-env bootstrap. Capacity is a point observation,
not a reservation. File creation is a source-artifact operation, not observer
execution. The reviewed capture is not run by this decision.

The proposed probe01 directory and streams are not operands of these
materialization checks. A later distinct one-probe grant must authorize
capture allocation and the exact accepted request. Source and all predecessor
packets remain frozen. No Python parsing/import/compile/test, host/library/
runtime inspection, science/build, retry or external action is authorized.
Only the current five-paper batch continues, then pause. HOLD_EXTERNAL.
