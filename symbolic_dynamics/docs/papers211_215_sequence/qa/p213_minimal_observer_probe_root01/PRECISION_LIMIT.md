# Preliminary view precision boundary (original view preserved)

INITIAL_RAW_RECEIVE_NATIVE.json contains a complete raw read and exact
thirteen-field external stream keys, but its decoded convenience projection
used ordinary JavaScript JSON.parse. That projection rounds integer values
outside the IEEE-754 safe range, including runtime nanosecond metadata.
Its nested sourceKey metadata numbers MUST NOT be used as exact runtime keys
or compared to full documentary integer keys. The captured stdout.bin bytes
are unchanged, exact and independently hash-pinned; this is a display/parser
precision limitation, not an observer failure or repaired output.

The preliminary status, lengths, flags, bounded counts and SHA256 strings are
not large-integer claims. Exact runtime reception must parse raw integer
lexemes losslessly, preserve scalar types and reject unsupported/duplicate
JSON fields. The separate lossless-data check records such integers without
rounding. It does not run the observer again or rescan runtime targets.
Keep this original view and its limitation; do not overwrite it as PASS.
