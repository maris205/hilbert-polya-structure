# P214 Review B initial receiver failure 01

2026-09-11 UTC. The first root DATA receiver invocation exited nonzero at its
first differing reconstructed state. The B scientific run was not rerun or
modified. The failed receiver source is preserved byte-for-byte as
`RECEIVE_INITIAL.failed01.cjs`, SHA256
`d36454d65d9193ba48842b9074c5ace4052b923e6f2f1135b3c2999a4ea512a3`.

Inspection found that the JavaScript F4 multiplication helper reduced before
the left shift, unlike the verifier's shift-then-reduce field operation. The
receiver is corrected only in that helper and augmented with exact mismatch
diagnostics before a new read-only reception attempt. This failure is not a
PASS and gives no replay credit.
