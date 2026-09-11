# Author package artifact audit

2026-09-06 UTC. Cwd: `/root/autodl-tmp/symbolic_dynamics`.
The package audit is read-only and covers all package files except the
nonself manifest itself, all historical input pins, local Markdown links,
the two archived raw replay pairs, and fresh executions of both scientific
entry points against their complete canonical byte streams.

Command:

```text
python -B docs/papers204_208_sequence/scouting/word_local/HVD_PROOF_WORK/audit_package.py
```

Actual execution: exit 0, with the complete stdout below. Both fresh
subprocesses returned no stderr. After recording this receipt, the
nonself manifest was refreshed and the same audit was executed again;
the final result is identical and verifies the finished receipt itself.

```json
{
  "fresh_live_replays": [
    {
      "bytes": 4099,
      "exit_code": 0,
      "raw_byte_equal_to_canonical_and_replay": true,
      "script": "verify_partial_theorems.py",
      "sha256": "b2e5f2f55c93242ae7a71a94689fdab26f6fb96d2cad532fa3dcf80447de3a00",
      "stderr_bytes": 0
    },
    {
      "bytes": 8572,
      "exit_code": 0,
      "raw_byte_equal_to_canonical_and_replay": true,
      "script": "probe_sentinels.py",
      "sha256": "04456889d237746ef4f1053491e701b0b18c1e1db45f56c17cee8d647894299d",
      "stderr_bytes": 0
    }
  ],
  "input_pins": 7,
  "local_markdown_links": 21,
  "nonself_manifest_entries": 13,
  "scope": "partial propositions; admission remains HOLD_PROOF",
  "status": "PASS_AUTHOR_PACKAGE_AUDIT_ONLY"
}
```

No artifact status supplies a missing all-length proof or independent
manuscript review. HOLD_PROOF / NO_ADMISSION is unchanged.
