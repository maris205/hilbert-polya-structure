# P186 improvement log

## Round 0 → Round 1

Review A changed from subset masks to weighted positive-gap compositions.  It
found two Minor abstract defects: the survival condition for a gap was
grammatically ambiguous, and the unique depth-`n-1` sentence omitted the
`n>=2` boundary.  The abstract now says that `g-t` survives exactly when
`g>t`, otherwise disappearing, and states the extremal qualifier.  The
accepted Review-A control ends with 12,106,438 assertions and zero open
findings.

## Round 1 → Round 2

Review B used weak rank profiles `b_j=a_j-j` and signed
inclusion--exclusion coefficient evaluation, with exhaustive state/target/time
checks through `n=17`, the full displayed `n=18` profile, and symbolic stress
through `n=64`.  Its 16,766,548 assertions found no further issue.  Round 2
is byte-identical to Round 1 with SHA-256
`449ddc9983cec9618e8a7cead63730d3ed29e1dbb5f36a630948eac3618f2b48`.
Two source-only cold builds reproduce those bytes.  External status remains
`OWNER_AMBER / HOLD_EXTERNAL`.
