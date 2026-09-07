# Post-seal wrong-cwd verification failure — actual tool transcription

The initial192-payload `SHA256SUMS` was successfully created, with SHA-256
`74004ca903c61efce6313781549b30c269c43794ce3d550a9f090c342d373d53`.
The immediately following verification used this actual shell command:

```sh
python3 -I -B docs/papers204_208_sequence/scouting/finite_systems_thirty_third/record.py seal && sha256sum -c docs/papers204_208_sequence/scouting/finite_systems_thirty_third/SHA256SUMS
```

Actual cwd was `/root/autodl-tmp/symbolic_dynamics`, while manifest entries
are relative to the scout directory. The seal step succeeded. The check
returned exit1 and reported all192 entries as missing/open failures; its
tool display was explicitly truncated. This is a real verification-path
failure, not a failed mathematical pilot or evidence that sealed bytes
changed. No original complete stdout file existed for that tool invocation,
so this document is honestly a tool transcription, not a native receipt.

The initial handoff and seal are preserved unchanged. `postcheck.py` runs
the same incorrect-cwd checksum command once more, now capturing complete
native stdout/stderr/pins as a NEW reproduction, and then runs the manifest
check from the correct manifest directory. The reproduced failure is not
misrepresented as the original invocation. The successful corrected check
does not erase either failure.

The final closure supplement and new outer `FINAL_SHA256SUMS` explicitly
include these additional artifacts. The older192-payload seal remains a
valid complete manifest of its initial checkpoint, not of later additions.
