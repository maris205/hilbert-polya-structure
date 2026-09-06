# Actual two-process replay receipts

Date: 2026-09-05 UTC. Working directory:
`/root/autodl-tmp/symbolic_dynamics`. Interpreter:
`/root/miniconda3/bin/python`, Python 3.12.3. Both scripts use the standard
library only. Neither imports the other, historical or other authors' code,
data files or canonical output. Scientific scripts are pinned in SHA256SUMS.

## Seven-probe pilot

One exploratory run first completed with exit zero. Then the following
command launched two new interpreter processes. The JSON envelope transported
the common raw stdout without normalization, and is not the child stdout.

```sh
python -B -c 'import hashlib,json,subprocess,sys; cmd=[sys.executable,"-B","docs/papers204_208_sequence/scouting/graph_relation_second/pilot.py"]; a=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE); b=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE); assert a.returncode==b.returncode==0; assert a.stderr==b.stderr==b""; assert a.stdout==b.stdout; print(json.dumps({"receipt":{"byte_comparison":"PASS","command":cmd,"exit_codes":[a.returncode,b.returncode],"python":sys.version.split()[0],"raw_stdout_bytes":len(a.stdout),"raw_stdout_sha256":hashlib.sha256(a.stdout).hexdigest()},"canonical":a.stdout.decode("ascii")}))'
```

Wrapper exit 0; both child exits 0; both child stderr streams empty. Actual
receipt (fields retained exactly, whitespace of this receipt display is not
itself called canonical):

```json
{
  "byte_comparison": "PASS",
  "command": [
    "/root/miniconda3/bin/python",
    "-B",
    "docs/papers204_208_sequence/scouting/graph_relation_second/pilot.py"
  ],
  "exit_codes": [
    0,
    0
  ],
  "python": "3.12.3",
  "raw_stdout_bytes": 21489,
  "raw_stdout_sha256": "4da83d5e1054549734a0daf53a232c8730c46c10956ad262e225325fad65678e"
}
```

Full common child stdout: [CANONICAL.json](CANONICAL.json), 21,489 bytes,
including final newline. The saved file's actual digest matches the receipt.
Each execution made 243,120 assertions over 140,982 complete states in 2,906
parameter components. Its internal enumeration digest is
`9c6df6d11f0c4e0b470d809eff6b90fd85fc4a7e75c214d6abc3921802d5738f`.

## CCI proof-pressure checker

A separate exploratory execution first passed. The exact same wrapper
command above was then executed with its script path changed to
`docs/papers204_208_sequence/scouting/graph_relation_second/verify_cci.py`.
It launched two new processes, not a comparison of archived receipts.
Wrapper exit 0; both child exits 0; both stderr streams empty. Actual receipt:

```json
{
  "byte_comparison": "PASS",
  "command": [
    "/root/miniconda3/bin/python",
    "-B",
    "docs/papers204_208_sequence/scouting/graph_relation_second/verify_cci.py"
  ],
  "exit_codes": [
    0,
    0
  ],
  "python": "3.12.3",
  "raw_stdout_bytes": 4433,
  "raw_stdout_sha256": "41ca0312bd5115fc0343310ebfbd493c44ee927d267de7ca438328af92bae2f7"
}
```

Full common child stdout: [CCI_CANONICAL.json](CCI_CANONICAL.json), 4,433
bytes including final newline. The saved file's actual digest matches the
receipt. Each child made 1,029,769 assertions: 63,411 full dynamical sources
and their exact target source sets for all graphs through four vertices and
palettes 3,4,5; 33,868 full graph instances through six vertices for the
static cover extremum; and 133 explicit sharp path families.
The internal enumeration digest is
`002a4104d381bd2791d22c12f7f33d4c0cec87e479a384ad8535ac1d13c24310`.

This is an independent implementation by the CCI proof author, not an
independent review process. Its printed status says so. All-parameter claims
are supported by the separate deductive package, not by finite enumeration.

## Integrity and scope

The nonself manifest covers every file in this directory except itself.
The original scientific scripts did not change between their paired runs
and manifest closure. Canonical hashes verify the saved full stdout; they do
not replace the actual pair commands above. No PDF build, page view,
manuscript review or paper admission is claimed for this scouting package.
