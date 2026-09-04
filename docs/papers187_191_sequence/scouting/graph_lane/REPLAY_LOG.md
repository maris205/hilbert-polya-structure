# Deterministic replay log

Canonical environment and command:

```sh
LC_ALL=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
python3 -B docs/papers187_191_sequence/scouting/graph_lane/pilot.py
```

The saved transcript is `canonical_stdout.txt`.  After saving it, two new
Python processes were launched independently and compared byte-for-byte with
`cmp -s` against that transcript.

| Replay | Fresh process | Byte comparison | Canonical SHA-256 |
|---|---|---|---|
| 1 | yes | PASS | `911dac94cff467af3f599e7d022f4c0d2c1b94bbb1d69f06b18c6090593735ae` |
| 2 | yes | PASS | `911dac94cff467af3f599e7d022f4c0d2c1b94bbb1d69f06b18c6090593735ae` |

Both strengthened-pilot processes reported denominator 16, survivors
`G01_TRC,G02_ECSC`,
`exact_assertions=1132976`, `owner_status=OWNER_AMBER`,
`external_status=HOLD_EXTERNAL`, and `status=PASS`.

The replay proves deterministic agreement only for this bounded executable and
environment.  It is not a uniform mathematical proof or an owner clearance.
