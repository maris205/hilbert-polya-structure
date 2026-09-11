# Source-only evidence handoff; still unsealed

The 304-line launcher is unchanged from the source handoff sent before root
review: 16,201 bytes, SHA256
`59db5f6e2dbf3dfc0cc612efea679f608e188d6d575dc3627d8f19ae983b17fc`.
Its unconditional final-builder binding failure remains. No invocation,
including a refusal test, was performed. Both prospective output directories
were physically absent in the actual static check.

The separate 164-line `static_check.py` completed with actual native exit 0
and 546 AST/data checks. `STATIC_CHECK.actual.json` contains every check label,
all explicit before/final file keys, complete actual GNU `diff --minimal`
argv/cwd/native exit/separate streams, and the complete source diff.
`STATIC_NATIVE_RETURN.actual.json` archives the full actual checker tool
return. Its tool transport output is combined; no independent checker stderr
is invented. The internal native diff did capture separate stdout/stderr and
returned expected exit 1 with zero stderr bytes. Its 477-line, 27,772-byte
complete diff was applied in memory to the original, validating every removed
or context line and reconstructing all new source bytes.

The first actual static checker failed because it demanded identical GNU and
Python diff hunk choices. `STATIC_FAILURE_01_NATIVE.actual.json` preserves its
full real traceback/native return; `history/static_check_01.py` preserves the
exact failed checker. The first internal diff streams were not printed before
that assertion and are unavailable, not assumed empty. The later successful
diff is a new run. No launcher source fix or execution was involved.

`ORIGINAL_INPUT_PINS.json` binds the complete actual P209 outer source/README
and immutable original P210 unbound writer schema. `PROVENANCE.json` records
those roles, source/diff keys, actual failure and success boundaries, and the
explicit original defect: no P209 outer new session/group or bounded wait.
It does not invent actual final builder/B/Round2/lifecycle evidence. The
existing README and input contract were left unchanged after their successful
static pinning; this separate addendum avoids silently changing those keys.

Root is reading the complete launcher before any seal. A source-only safety
read is also independently assigned to another infrastructure process; it is
not a manuscript review and does not replace root's mandatory original read.
No preparation seal or accepted runtime claim is supplied in this handoff.
The entire actual native outer launch/completion must still be archived by
root after any later separately authorized bound execution.
