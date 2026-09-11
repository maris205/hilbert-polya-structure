# Desk execution surfaces and preserved failures

These are desk reception/source actions, not additional scientific runs.
The `native/*.json` files retain actual tool-return objects, including
combined stdout/stderr, observed native exit status and timing metadata.
They are not a claim of syscall tracing or separate-stream capture.

## Author pin checks

First command: `sha256sum -c SHA256SUMS`, cwd
`/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/scouting/arithmetic_lane`.
Exit 1: all 52 keys failed open because the manifest keys are
workspace-relative. The complete combined output is preserved in
`native/manifest_wrong_base.json`. This was the desk's cwd error, not an
author-input mutation or missing author artifact.

Correction: `sha256sum -c docs/papers211_215_sequence/scouting/arithmetic_lane/SHA256SUMS`,
cwd `/root/autodl-tmp/symbolic_dynamics`. Exit 0, 52 OK, retained in
`native/manifest_correct_base.json`. No manifest/parser/hash was changed.

Historical command: `sha256sum -c docs/papers211_215_sequence/scouting/arithmetic_lane/HISTORICAL_INPUT_PINS.sha256`,
same workspace cwd. Exit 0, ten OK, in `native/historical_pins.json`.

## Source acquisition failures

Attempted command: `curl -L --fail --max-time 45 https://www.irif.fr/~berthe/Articles/VL-Brun-JSC.pdf -o docs/papers211_215_sequence/scouting/spr_gate/sources/VL-Brun-JSC.pdf`,
workspace cwd. The first tool call yielded an ongoing native session;
zero bytes had arrived. The retained subsequent tool results are
`native/curl_middle.json` and `native/curl_final.json`; final exit 28:
`curl: (28) Connection timed out after 45000 milliseconds`.
The initial progress chunk is available only in the live conversation,
not claimed as a complete local raw acquisition log. No downloaded PDF
exists or is claimed in this desk package.

The desk mistakenly invoked `pdftotext -layout docs/papers211_215_sequence/scouting/spr_gate/sources/VL-Brun-JSC.pdf docs/papers211_215_sequence/scouting/spr_gate/sources/VL-Brun-JSC.txt`
before waiting for completion. It exited 1 with an I/O error: the input
file did not exist. No extracted file was created. That exact native
tool result was not locally captured before the subsequent call; this
paragraph records the failure, not a newly fabricated raw receipt.

Browser text open/finding of the Brun author source succeeded and is the
actual source-reading surface. Three requested PDF screenshots (zero-based
pages 3, 4, 5) each returned `Failed to fetch restricted URL`; no image
was inspected. These failed tool returns were not locally copied as raw
objects. The report does not claim PDF visual verification or local PDF
byte provenance. The publisher polynomial body was exposed in search;
direct open failed and some equations are missing from the text renderer.

## Integrity-only archived-data read

Actual command:

    /root/miniconda3/bin/python3.12 -I -S -B docs/papers211_215_sequence/scouting/spr_gate/audit_archive.py

Cwd: `/root/autodl-tmp/symbolic_dynamics`. Exit 0, complete returned stdout
in `native/archive_audit.json`; 173,763 checks, 74 pins, 35 archived boxes
and 34,636 stored records. Code is included and covered by the final
nonself desk manifest. This is one actual artifact-only execution; it
neither runs author code nor calculates SPR mathematics. No independent
verifier/canonical scientific pair exists or is asserted for this killed
candidate gate. The author scientific provenance limits are not repaired.
