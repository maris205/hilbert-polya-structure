# P214 Review B initial receiver failure 02

2026-09-11 UTC. After correcting the F4 helper, the second root DATA receiver
invocation verified every state, transition, depth, target, predecessor list,
triangular list and carrier row, then exited nonzero only at its independently
derived aggregate verifier-check count. The B scientific run was not rerun or
modified. This failed receiver source is preserved as
`RECEIVE_INITIAL.failed02.cjs`, SHA256
`9088af0c1cc8d150b0bc1433a43bbcc46dd15d5d5ab545d2c10772584582f9dc`.

The current receiver is augmented to disclose the exact aggregate mismatch
before any arithmetic correction. This failure is not a PASS and gives no
strict or scientific replay credit.
