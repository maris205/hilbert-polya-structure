# Exact control — P127

The paper-local verifier uses integer bit masks and no randomness.  It
exhausts all `2^(n^2)` matrices for `1<=n<=4`, including every codomain point
rather than only observed images.  It made **1,271,047 exact assertions** and
reported `STATUS=PASS`.

Controls include the parity quotient, the independent left-factor form,
second/fourth iterates, exact entrance times and periods, the full
`0/1/(2^(n-1)+1)` fibre law, feasible-margin affine sizes, and all component
counts.  A fresh stdout must byte-match `code/verification_output.txt`.

This bounded computation is falsification evidence and does not prove an
all-`n` theorem or establish novelty.
