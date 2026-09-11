# Actual execution receipt

2026-09-05 UTC; cwd `/root/autodl-tmp/symbolic_dynamics`.
Runtime: Python 3.12.3. Only standard-library modules; no imported old code,
external datasets, seeds, author canonicals or hidden generated inputs.
These are author-side checks, not an independent candidate review.

## Final scientific input and raw output

```text
58461a5749e0d3cfa8094813ef1aec7a39a9ce0fd3e0fa68239d205b8db708b5  pilot.py
f738dbd448f3455f57821a20e65d81e05fcf54403027fef758bb54fe56d46cef  CANONICAL.json
```

The actual fresh two-subprocess wrapper was:

```python
import subprocess, json, hashlib, sys
args = [sys.executable, "-B",
        "docs/papers204_208_sequence/scouting/graph_geometry_third/pilot.py"]
a = subprocess.run(args, capture_output=True)
b = subprocess.run(args, capture_output=True)
assert a.returncode == b.returncode == 0
assert not a.stderr and not b.stderr
assert a.stdout == b.stdout
print(json.dumps({"returncodes": [a.returncode, b.returncode],
                  "stderr_bytes": [len(a.stderr), len(b.stderr)],
                  "raw_equal": a.stdout == b.stdout,
                  "stdout_bytes": len(a.stdout),
                  "sha256": hashlib.sha256(a.stdout).hexdigest(),
                  "raw_stdout": a.stdout.decode()}, sort_keys=True))
```

Observed receipt, wrapper exit zero:

```json
{"raw_equal":true,"returncodes":[0,0],"sha256":"f738dbd448f3455f57821a20e65d81e05fcf54403027fef758bb54fe56d46cef","stderr_bytes":[0,0],"stdout_bytes":26251}
```

The tool wrapper ran as process session 65601. Its actual captured stdout
was parsed after successful completion and installed unchanged as CANONICAL.json
using an allowed patch; a real `sha256sum` then matched the receipt. No stdout
normalization is called byte equality. JSON indentation/trailing newline are
included in the 26,251-byte hash. Complete raw stdout is the canonical file;
it contains 40 box profiles, depth/cycle counts, extrema counts and digests,
and all four proof-directed $C_7$ sentinel traces.

Each final run made 513,700 assertions over 243,356 source states. The
functional-graph enumeration digest is
`da620826744423642448263ad83600561168a75267afa6e21e7bb84928947bfa`.
Both final runs include the $C_7$ sentinels. The underlying full graph boxes
remain $n\le5$, with geometric fields $p=3,7$; sentinels are not an exhaustive
larger-size carrier. Code/canonical integrity checks are separate from the
full mathematical limitations in the report.

## Earlier execution history, not counted as final replay

The first seven-rule exploratory process (session 93466) was manually
interrupted with exit 130 after finding an inefficient extrema-reporting
comprehension: `max(fibres.values())` was recomputed for each candidate target.
It had no successful complete stdout or assertion counterexample. Actual
terminal ending:

```text
  File ".../pilot.py", line 206, in main
    rows.append(analyse(name, p, nxt))
  File ".../pilot.py", line 63, in analyse
    max_fibre_targets=sorted(y for y, count in fibres.items()
  File ".../pilot.py", line 64, in <genexpr>
    if count == max(fibres.values())),
KeyboardInterrupt
```

The maximum was hoisted out of the comprehension; the large complete target
list was then replaced by its exact cardinality, first witness and digest.
This changes output size, not map mathematics. EVEN was added as the replacement
for ODD's immediately rejected live seat, leaving eight total literal maps.
The intermediate session 69127 returned zero with 513,444 checks but produced
an overlarge exploratory stdout; the displayed tool response was truncated.
It is not the final canonical, is not claimed to be a retained raw replay,
and supplies no evidence beyond the later complete final executions.
Session 64252 then returned zero with the compact reporting code and printed
selected summaries. The four proof-directed $C_7$ checks were added next;
the final two runs above supersede both for the scientific input now pinned.

No failed proof or negative mathematical witness was overwritten. No frozen
manuscript or accepted historical package was edited. The earlier performance
interruption is disclosed, not turned into a claimed PASS.
