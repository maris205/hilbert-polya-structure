# CRC3 independent gate replay log

2026-09-05 UTC. Working directory:
`/root/autodl-tmp/symbolic_dynamics`.

## Actual executions

An exploratory execution of `python -B .../CRC3_GATE/verify_gate.py`
completed successfully with 721,397 assertions. It had no failed check
and required no mathematical or checker repair.

After that success, the following actual wrapper launched two fresh
subprocesses with the unchanged checker:

```python
import subprocess, hashlib, json, sys
p = "docs/papers204_208_sequence/scouting/word_local/CRC3_GATE/verify_gate.py"
a = subprocess.run([sys.executable, "-B", p], capture_output=True)
b = subprocess.run([sys.executable, "-B", p], capture_output=True)
assert a.returncode == b.returncode == 0
assert a.stderr == b.stderr == b""
assert a.stdout == b.stdout
print(json.dumps({
    "runs": 2,
    "returncodes": [a.returncode, b.returncode],
    "empty_stderr": True,
    "raw_stdout_equal": True,
    "raw_stdout_bytes": len(a.stdout),
    "raw_stdout_sha256": hashlib.sha256(a.stdout).hexdigest()
}, sort_keys=True))
sys.stdout.buffer.write(a.stdout)
sys.stdout.flush()
```

The wrapper exited zero. Both children exited zero; stderr was empty in
both; the full raw stdout byte strings were equal, not merely the parsed
JSON, a summary line, or the scientific digest.

Actual receipt:

```json
{"empty_stderr": true, "raw_stdout_bytes": 3163, "raw_stdout_equal": true, "raw_stdout_sha256": "6ead393b4a0c46d641f0ce7a7d83381ad4e0ae704afca21cb81b11f2e1fe1a01", "returncodes": [0, 0], "runs": 2}
```

The complete emitted JSON is saved verbatim as `CANONICAL.json`. The
receipt appears after the JSON in the wrapper output because the printed
text receipt was buffered while the raw child bytes were written; this
does not affect the direct comparison of the child streams.

## Scope of each run

All labelled ternary words for n=1..10: 88,572 sources; 88,572 full
target-source-set comparisons. Independent full orbit walks are used,
with literal all-earlier-position forward comparisons through n=7.
All compositions of totals 1..14 are independently checked for maximum
product and ALL optimum multisets. Each run executes 721,397 assertions.

Scientific enumeration digest:
`abf6be308260a038858c557cab1ae257e4be1746ba706b0fd99e48cff8d994bb`.

The separate digest records `[word, forward, tail, period, fibre_size]`
for each full-box word. It is not substituted for the raw-stream test.
Finite enumeration does not prove the all-n claims, whose deduction audit
is in `CANDIDATE_GATE.md`.

## Artifact discipline

Only files inside `CRC3_GATE/` were created or edited for this gate.
Author inputs, exploratory failures elsewhere, prior gates, manuscripts,
batch indexes, Git state, and external systems were not modified.
`SHA256SUMS` pins the five content files and was checked against the actual
filesystem after creation. The manifest does not hash itself.
