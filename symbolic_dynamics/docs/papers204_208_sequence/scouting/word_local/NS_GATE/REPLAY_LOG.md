# NS independent gate replay receipt

Date: 2026-09-05 UTC. Working directory:
`/root/autodl-tmp/symbolic_dynamics`. Runtime: Python 3.12.3,
`/root/miniconda3/bin/python`. No third-party modules, author code, historical
verifiers, data files, random seeds or generated inputs are dependencies.
The input source is pinned in the directory-relative `SHA256SUMS`.

An exploratory invocation of `python -B
docs/papers204_208_sequence/scouting/word_local/NS_GATE/verify_gate.py`
completed with exit zero. It is not substituted for either member of the
fresh comparison pair below.

## Actual pair command

The following command launched two separate interpreter processes and compared
their raw stdout bytes without normalization. It was launched at 12:06 UTC
and its completion was collected after the process finished; no archived
PASS was merely re-labelled as a new execution.

```sh
python -B -c 'import hashlib,json,subprocess,sys; cmd=[sys.executable,"-B","docs/papers204_208_sequence/scouting/word_local/NS_GATE/verify_gate.py"]; a=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE); b=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE); assert a.returncode==b.returncode==0; assert a.stderr==b.stderr==b""; assert a.stdout==b.stdout; print(json.dumps({"byte_comparison":"PASS","command":cmd,"exit_codes":[a.returncode,b.returncode],"python":sys.version.split()[0],"raw_stdout_bytes":len(a.stdout),"raw_stdout_sha256":hashlib.sha256(a.stdout).hexdigest()},sort_keys=True),flush=True); sys.stdout.buffer.write(a.stdout)'
```

Wrapper exit status: 0. Both child exit codes: 0. Both child stderr values:
empty byte strings. Actual receipt line:

```json
{"byte_comparison": "PASS", "command": ["/root/miniconda3/bin/python", "-B", "docs/papers204_208_sequence/scouting/word_local/NS_GATE/verify_gate.py"], "exit_codes": [0, 0], "python": "3.12.3", "raw_stdout_bytes": 2605, "raw_stdout_sha256": "b1dcfc0f0e1ec4c558df0ac59be28e21bd868fd4b389064f744e20ce74be0ae8"}
```

The full common child stdout, including its final newline, is preserved in
[CANONICAL.json](CANONICAL.json). Its SHA-256 was checked against the actual
receipt value above after saving; this is a raw-output digest, distinct from
the internal enumeration digest
`a6292ec62f0048dde37a1ae3dff667d1b8df1de021c58e665823898c7009020a`.
Each child executed 681,499 assertions. The checker itself prints only
`PASS_BOUNDED_MATH_AND_STATIC_ADAPTER_ONLY`; the deductive and source/value
decision belongs to [CANDIDATE_GATE.md](CANDIDATE_GATE.md), not enumeration.

## Scope and replay ceiling

All factorial carriers $1\le n\le8$ are complete, not sampled. Counts for
times 2 through 5 cover both eventual phases but are finite checks only;
the all-$n$, all-$t\ge2$ extension is deductive. There is no one-step fibre
check or first-image census theorem claim. No increased cutoff was used to
compensate for an unresolved proof or source concern. The directory manifest
is complete and excludes itself; input pins in the gate report are separately
workspace-root-relative and are not parsed as directory-relative package pins.
