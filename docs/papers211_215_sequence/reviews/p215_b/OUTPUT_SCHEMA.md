# P215 Review B proposed output schema

Status: `SOURCE_ONLY_NOT_EXECUTED`. A successful future run emits deterministic
ASCII/UTF-8 with LF endings in this exact order:

1. Header `P215_B_FLOYD_FLAGGED_SUBSETS_V1`.
2. Parameter row `PARAM|n=0..5|q=0..4`.
3. Thirty `CARRIER` rows in n-outer, q-inner ascending order. Each records
   `n`, `q`, complete carrier size, observed Floyd height, image size and
   maximum fibre.
4. One `TOTAL` row recording 30 carriers, 5,704 states and the actual complete
   assertion count.
5. Literal final row `PASS`.

For every state the source independently computes the literal transition,
Floyd entry/period/recurrent point, every turn-word iterate through extinction,
and the exact deepest predicate. For every target it retains the complete
literal predecessor bucket in memory and compares it with the complete
flagged-subset reconstruction, every reconstructed transition, the independent
determinant, the displayed recurrence, and the image predicate. Carrier image,
height, maximum fibre and unique maximizer are checked separately. The concise
wire output does not mean sampled internal coverage.

Any exception, nonzero exit, stderr, missing/extra line, wrong total/final row,
or later whole-byte canonical mismatch is failure. The verifier does not read
a canonical or external file. No actual output, assertion count, canonical or
PASS is claimed at SOURCE stage.
