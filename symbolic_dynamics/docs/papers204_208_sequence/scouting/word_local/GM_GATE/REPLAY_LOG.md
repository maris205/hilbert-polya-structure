# Independent GM gate raw-byte receipt

Date: 2026-09-05 UTC. Working directory:
`/root/autodl-tmp/symbolic_dynamics`.

The first exploratory execution of verify_gate.py returned zero. Two further
fresh subprocesses were then actually executed and compared in memory as raw
bytes. Both return codes were zero, both stderr byte strings were empty, and
the stdout byte strings were equal without normalization.

Actual receipt:

```json
{"byte_comparison":"PASS","command":["/root/miniconda3/bin/python","-B","docs/papers204_208_sequence/scouting/word_local/GM_GATE/verify_gate.py"],"exit_codes":[0,0],"python":"3.12.3","raw_stdout_bytes":2799,"raw_stdout_sha256":"37ad2ae57e682f81b21ff7af1562af6bfed4e64601fa34c1eb9ee5dc3b747d4e"}
```

Each run made 3,804,852 assertions. Repeating the test does not increase the
number of distinct tested systems. The literal transcript was saved as
CANONICAL.json and its actual filesystem bytes were checked against this
receipt after saving. Input and output hashes appear in SHA256SUMS.

To reproduce one execution from the workspace root:

```sh
python -B docs/papers204_208_sequence/scouting/word_local/GM_GATE/verify_gate.py
```

For a full comparison, run the command twice with separate subprocesses,
capture stdout and stderr as bytes, verify both return codes, compare the
stdout byte strings, then compare them to CANONICAL.json opened in binary
mode. No author verifier is imported or executed by this independent check.
This is candidate evidence, not a manuscript review or owner clearance.
