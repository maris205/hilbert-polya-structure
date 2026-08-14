# Test Report

Command:

```bash
bash code/run_c49.sh
```

Result: `PASS`.

- unit tests: 10/10;
- exact primitive rows: 36/36;
- square-theorem rows: 30/30;
- cyclotomic divisor products: 36/36;
- period-three signed mutation: rejected;
- `n=2` overextension: rejected on all three orbits;
- nonreciprocal mutation: rejected by primitive norm 13;
- reducible/minimal-polynomial weakening: rejected;
- false one-scalar power law: rejected on all three orbits;
- scalar/ideal claim promotion: rejected;
- dependency hashes: 8/8.

The final checker line is:

```json
{"candidate_id":"HCS-P49","check":true,"core_sha256":"3bb27b0da0d23743e65629f5293a6e3166a8a2fe09e9822cfced763a496a05e7","ideal_packet_status":"OPEN_EXACT_STRUCTURE","scalar_route_status":"STOP_SCOPED_SQUARE_NORM"}
```

The actual output also includes the complete finite-summary object.  No
floating-point root approximation enters any acceptance condition.
