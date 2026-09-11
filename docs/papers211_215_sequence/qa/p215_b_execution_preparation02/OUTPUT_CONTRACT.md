# P215 Review B initial wire contract

Status: `SOURCE_ONLY_NOT_EXECUTED`.

The future initial stdout must be ASCII/UTF-8 with LF endings and exactly 34
lines, in this order:

1. `P215_B_FLOYD_FLAGGED_SUBSETS_V1`
2. `PARAM|n=0..5|q=0..4`
3. Thirty `CARRIER` rows in n-outer, q-inner ascending order, each containing
   exactly `n`, `q`, `states`, `height`, `image` and `maxfibre` fields.
4. One `TOTAL` row containing exactly `carriers=30`, `states=5704` and the
   verifier's actual positive integer `assertions` count.
5. `PASS`

The receiver will require each carrier value to equal independently evaluated
closed forms: `states=(q+1)^n`; `height=n` exactly when `n>0` and `q>0`, else
zero; `image=(q+1)^(n-1)` for `n>0`, else one; and
`maxfibre=binom(q+n,n)`. It will independently sum states to 5,704.

The concise wire records summaries, not state samples. DATA acceptance also
requires a zero child exit, empty stderr, raw PRE/POST input equality and an
independent complete reconstruction over all source states and targets as
specified in `DATA_RECEIVER_PLAN.md`. No stdout bytes or digest are known or
claimed before execution, and no canonical is read or created here.
