# Results

The evidence payload is deterministic and covers six exact scenarios:

| quantity | count |
|---|---:|
| raw labels | 20 |
| canonical particles / premerge cells | 18 |
| event times | 7 |
| simultaneous event groups | 8 |
| projection cells | 75 |
| conservation cells | 6 |
| weak-balance cells | 8 |

All event rows agree with a producer-independent reconstruction based on
exhaustive contiguous weighted-isotonic partitions and block-line crossing
times.  Every arbitrary-multiplicity loss equals the nonnegative pairwise
variance formula.  The no-collision, initial-coincidence, cascade,
simultaneous triple, and disjoint simultaneous faces are all present.

Evidence SHA-256: `dace90669ac08c25b18427dee176b0f09b6754d0fc9d597b8986575363f84809`.
Payload SHA-256: `021e77bca19b76d3cbb09cd53e7215741cb897795e00925fcaa199e227e0b4ec`.
Evaluation semantic SHA-256:
`54650acae7553edea8e073f2c0406aaa418659a4f5442898e515d4d29c8f3130`.

The independent checker passes 1,538 assertions; the hostile suite rejects
all 66 mutations (45 evidence JSON and 21 evaluation YAML).
