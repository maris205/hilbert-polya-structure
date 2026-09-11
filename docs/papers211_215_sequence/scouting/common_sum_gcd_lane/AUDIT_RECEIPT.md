# Actual documentation-only audit receipt

From the workspace root the following command was actually executed:

    python -I -B docs/papers211_215_sequence/scouting/common_sum_gcd_lane/evidence.py audit

Actual exit code: **0**. Complete stdout:

```json
{"audit": "ARCHIVED_DOCUMENTATION_ONLY", "historical_raw_pairs": 5, "native_bindings": 3, "native_returncodes": [0, 0, 0], "new_scientific_executions": 0}
```

This checked five current/original raw-byte pairs, three native command
result/stdout/stderr bindings and the two successful primary HTML byte/hash
bindings. It did not implement or evaluate the gcd map. The historical
originals total 72,293 bytes. All three native documentation commands
returned 0; both downloaded bodies contain the expected subject and their
arXiv version headers were subsequently inspected in the derived text.

HTML text extraction was done within the capture producer using Python's
standard-library HTML parser, not by an invented extra native command.
The exact raw HTML bodies and derived text both remain archived. Browser
reading covered the specific definition/algorithm passages identified in
`SOURCE_AND_COLLISION.md`, not every theorem of either source.

The evidence producer has no scientific mode or map implementation.
Scientific executions and pilot states are both zero. This is an author
artifact inspection, not independent review or parent/root acceptance.
The eventual directory-relative `SHA256SUMS` excludes only itself; the
historical-input checksum file is workspace-relative.
