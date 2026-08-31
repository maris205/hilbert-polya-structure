# Test report

All commands are run from the package root.

```text
python3 -B code/c264_power_map_producer.py
C264_PRODUCER_PASS cases=646 elements=21280 payload=0a8e28cd9a0e37ac65ad802fe107eaf329ab3f604dc8be23184b4d0809e9a662

python3 -B code/c264_power_map_checker.py
C264 independent checker: PASS (202656 assertions; mode=full)

python3 -B code/c264_power_map_sympy_crosscheck.py
C264_SYMPY_PASS (1029 symbolic matrix/rank checks across 220 maps)

python3 -B code/c264_power_map_replay.py
C264 byte replay: PASS

python3 -B code/c264_power_map_mutation.py
C264 repaired-hash mutation gate: PASS 33/33
```

The independent checker imports no producer and directly follows every orbit and every stored iterate. Mutation tests recompute the outer payload hash after corruption, so rejection is semantic rather than a stale-hash shortcut.
