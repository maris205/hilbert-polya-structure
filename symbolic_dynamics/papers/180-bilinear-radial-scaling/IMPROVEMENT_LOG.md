# P180 improvement log

## Round 0 → Round 1

Hostile Review A identified one Major completeness defect: an “every-time”
contract whose fibre theorem began only at `t>=1`.  The theorem now states the
time-zero identity fibre before the positive-time formula.  The author
verifier separately sweeps every time-zero target in every declared box,
raising its exact assertion total from 723,995 to 770,697.

The source now explicitly assumes a prime power `q` and `m>=1`, subtracts
internal systems P102/P103/P125/P171, attributes tails and periods to the two
parts of the scalar order correctly, and clarifies that `(3^t-1)/2` and `2s`
are ordinary integers even in characteristic two.

Round-1 PDF SHA-256:
`d0b08ddc5de6a91a120282d6c31dcc56ca67c1bfdc5202d68b24a22335c80b59`.

## Round 1 → Round 2

Reviewer A accepted the assumption, time-zero, and collision-boundary repairs
after two 243,393-assertion replays.  Reviewer B independently reconstructed
1,143,286 extension-field checks, including characteristic two,
non-symmetric forms, and all targets at times zero through four.  Both report
zero open findings.  Round 2 reproduces the accepted Round-1 PDF; two
source-only cold builds and 3/3 visual pages also pass.  External status
remains `HOLD_EXTERNAL`.
