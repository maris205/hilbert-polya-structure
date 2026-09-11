# Fourth-lane execution and provenance

2026-09-05 UTC. Working directory:
 /root/autodl-tmp/symbolic_dynamics

All executions were local CPU Python with -B. No external review process
was invoked. This is author pilot evidence, not independent verification.

## Input versions and exploration

Initial pilot.py SHA256:
5b9f0e3730880761f518577586a69efeb3790869563a2e8776a982e00c638f8b.

The initial complete literal-map run exited zero (process 30960, terminal
chunk 4606e2): six maps, 49 boxes, 130,454 states, 266,310 assertions. Its
scientific enumeration digest was already
64a9a096c6e27ad61d9228feb8f41f5cce9cbf845f393a6fc9c385927156b4c4.
No failed scientific assertion occurred.

Before the canonical replay pair, assertions were added for the DPF
coordinate contraction/full target-fibre formula/fixed census, CRS
disjointness/strict size decrease/unique cycle, UEX's k=2 degree identity,
SEN complement invariance and IDR's extinction bound. The literal maps,
carriers and cutoffs did not change. Final pilot.py SHA256:
358debd2057cf4113bc638094f1d4fb364f95184fc0e2db1c1cfe535d4344c32.

Final assertions per child: 446,531. The scientific enumeration digest
remained unchanged. The initial raw stdout was diagnostic tool output,
not archived as a second canonical file; the complete final canonical is
the package's retained execution record.

## Actual separate replay pair

The executed wrapper is reproduced here as Python code; it was passed
through python -B -c from the stated working directory:

    import subprocess, hashlib, json, sys
    p = "docs/papers204_208_sequence/scouting/graph_geometry_fourth/pilot.py"
    a = subprocess.run([sys.executable, "-B", p], capture_output=True)
    b = subprocess.run([sys.executable, "-B", p], capture_output=True)
    assert a.returncode == b.returncode == 0, (a.returncode,b.returncode,a.stderr,b.stderr)
    assert a.stderr == b.stderr == b""
    assert a.stdout == b.stdout
    sys.stdout.buffer.write(a.stdout)
    sys.stdout.flush()
    print(json.dumps({
        "runs": 2,
        "returncodes": [a.returncode,b.returncode],
        "empty_stderr": True,
        "raw_stdout_equal": True,
        "raw_stdout_bytes": len(a.stdout),
        "raw_stdout_sha256": hashlib.sha256(a.stdout).hexdigest()
    }, sort_keys=True))

Launched as process 58747, initial tool chunk 89d31c. Both children exited
zero and the wrapper completed successfully. Actual terminal receipt:

    {"empty_stderr": true, "raw_stdout_bytes": 19187, "raw_stdout_equal": true,
     "raw_stdout_sha256": "aacb884c6df033bc7245ac2859737a0037b3a57bf31e686cddfd15e35e6defd2",
     "returncodes": [0, 0], "runs": 2}

This is a raw bytes comparison, not normalized JSON equality.

The tool display combining web results and the pair's complete stdout
was truncated near the beginning of that stdout. Therefore a third,
unchanged archival command was actually executed:

    python -B docs/papers204_208_sequence/scouting/graph_geometry_fourth/pilot.py

Process 12998 exited zero. Its complete stdout was captured, parsed as
JSON and saved verbatim with apply_patch as CANONICAL.json. The archival
file's SHA256 and byte length are the same as the original pair's raw
receipt, namely 19,187 bytes and
aacb884c6df033bc7245ac2859737a0037b3a57bf31e686cddfd15e35e6defd2.
The third execution is disclosed rather than represented as an original
pair member. A later hash inspection reconfirmed both file pins.

Complete canonical headline:

    status: PILOT_COMPLETE_NOT_THEOREM
    literal_rules: 6
    boxes: 49
    states_across_boxes: 130454
    assertions: 446531
    enumeration_sha256: 64a9a096c6e27ad61d9228feb8f41f5cce9cbf845f393a6fc9c385927156b4c4

The 49 full profile objects, including cycle counts, image sizes,
heights, deepest and maximum-fibre witnesses, are retained in the complete
CANONICAL.json; this headline is not substituted for full output.

## Same-box diagnostic checks

A separate -B diagnostic loaded pilot.py with runpy (without main)
and inspected existing boxes. Actual output, chunk b5fa7e, exit zero:

    SEN_dimension4_cycle [27, 7104, 39, 10176]
    CRS_prime11_orbit [15, 672, 9, 128, 0, 2047] repeat 0
    CCS_prime3_zero_fibre 58

Another n=5,k=2 diagnostic, chunk 7cd00b, exit zero, exhibited UEX's
star swap: edges {01,02,03} map to {14,24,34} and back. It checks the
listed small witness, not an all-n theorem by enumeration. Neither
diagnostic expanded the six maps' parameter bounds.

## Artifact editing and failure disclosure

Only this directory was edited. One report-writing orchestration call
failed JavaScript parsing before apply_patch ran, due to unescaped
Markdown backticks inside a template literal. It wrote no report or
scientific file and executed no checker. The subsequent report patch
uses safe strings. This is an editing failure, not a failed mathematical
test. No failed scientific output, historical source or old review was
overwritten.

SHA256SUMS lists every nonself file in this directory and is checked
directory-relatively. Integrity closure does not promote any candidate.
