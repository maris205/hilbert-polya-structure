# Exact controls before P210 admission was indexed

Root physically copied these four current controls before changing any of
them for P210 admission and the a380d247 private-sync receipt. Four native
`cp` operations and four native raw `cmp` operations returned zero with empty
streams. [The complete preservation record](PRESERVATION.actual.json) pins
each original, copy and unchanged post-copy source, plus the actual root
MNA and Git reception prerequisites. The source is
`../preserve_p210_admission_controls.py`.

| Original role | Exact physical copy | SHA-256 |
|---|---|---|
| Workspace recovery index | [SYMBOLIC_DYNAMICS_STATE.md](SYMBOLIC_DYNAMICS_STATE.md) | `7f6506c6c4ce3f0e418e161f2ce508018bc651c07b42e2c738a0b4945fb8d5ec` |
| Batch recovery index | [PIPELINE_STATE.md](PIPELINE_STATE.md) | `fbd241b662b3169847e7ca09407c0037070bf4a32b2fecd93d5a4ecbe245d48a` |
| Theorem contracts | [FINAL_THEOREM_CONTRACTS.md](FINAL_THEOREM_CONTRACTS.md) | `887f52a013a56e6ec638e80514a52cc1be290c1791d34fc345eba00d2aaf46e5` |
| Private-sync receipt | [GIT_SYNC_RECEIPT.md](GIT_SYNC_RECEIPT.md) | `3793a50f6dc74cf5b4d2fc9626e00d5c28e14b739052ba78ecc6fd873377dbdd` |

These are exact historical path/hash-role resolutions for later documentary
checking. Their relative prose links retain their original document origins;
moving a copy here does not rebase old links or redefine scientific inputs.
No theorem, accepted review, old seal or failed record was changed. Current
indexes may advance after this snapshot; an old pending statement remains
true of its historical capture, not a new unresolved manuscript finding.
The six nonself payloads are covered by SHA256SUMS. HOLD_EXTERNAL remains.
