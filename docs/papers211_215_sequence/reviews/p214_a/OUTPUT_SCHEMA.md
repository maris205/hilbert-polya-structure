# P214 A verifier output schema

Deterministic UTF-8 text with LF endings:

1. literal header `P214_A_REVERSE_GAUSSIAN_V1`;
2. literal parameter line `PARAM q=2,3,4 m=2,3,4`;
3. nine lexicographically ordered `CARRIER` lines for `q=2,3,4` then
   `m=2,3,4`, each recording states, height, image size and sorted
   `fibre-size:target-count` pairs;
4. one `TOTAL carriers=9 states=5271 assertions=<integer>` line;
5. literal terminal line `PASS`.

Any assertion failure, traceback, nonzero exit, missing line, extra line or
byte mismatch against an actually adopted canonical is failure. No actual
output or PASS is claimed before a separately granted run.
