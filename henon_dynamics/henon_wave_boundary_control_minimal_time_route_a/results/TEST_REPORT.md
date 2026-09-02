# Test report

All commands below passed on 2026-09-02 with
`PYTHONDONTWRITEBYTECODE=1`:

```text
python -B code/c287_wave_producer.py
python -B code/c287_wave_checker.py
python -B code/c287_wave_sympy_crosscheck.py
python -B code/c287_wave_replay.py
python -B code/c287_wave_mutation.py
python -B code/c287_release_manifest.py
```

Pass markers: `C287_PRODUCER_PASS`, `C287 independent checker: PASS`,
`C287_SYMPY_PASS`, `C287 byte replay: PASS`, and
`C287 mutation suite: PASS 23/23`.  The checker reports 2,804 assertions and
SymPy reports 86 symbolic checks.  The release manifest reruns all five,
then performs two fresh two-pass LuaLaTeX builds of every retained round.

The repaired-hash suite explicitly covers exact theorem/proof corruption,
critical equality, and parameter/modal/revival/subcritical duplicate/drop
replacement, in addition to the original source, scope, Route-A, boundary,
phase, count, reference, and stale-hash controls.
