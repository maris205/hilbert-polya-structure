# P212 finite observer: pre-read handle-key delta

Root-authored source-only response, 2026-09-09 UTC. Independent delta review
pending. No observer/source import, Python parse, syntax check, test, host
observation, author probe, Node operation, query or build has occurred here.

The independent source auditor identified a finite ordering defect in the
original 425-line observer: whole_file returned after reading before its caller
compared the resolved-path key with the opened file descriptor's before key.
That prevents a successful mismatched observation but does not reject the
mismatched descriptor before its first content read. This is a source-order
argument, not an observed host race or claim of malicious interference.

This new sibling source changes exactly three source regions:

1. whole_file receives the expected resolved-file native key.
2. It calls the existing stable(expected, before) after the same-fd native key
   and bounded-regular check, but before SHA initialization or any os.read.
3. The only whole_file call passes before['stat']. The old post-return check
   remains, as do same-fd after and size checks and all resolution/closing checks.

The original sealed preparation directory is unchanged. The new source still
uses the original HERE/FRONTIER and the originally specified source/trust
receipt paths; it does not silently move or copy those authority roles.
The original disabled grant stays disabled and pin-null. Any actual observation
requires a separate exact root grant and complete native capture.

The finite stable comparison retains the original exclusion of atime. It does
not promise atomic fields, continuous filesystem identity or full-chain openat
isolation. Membership enumeration remains the explicitly declared bounded
path-based scandir/name-only mechanism with before/after resolution and two-pass
name comparison; it is not newly described as directory-fd-bound enumeration.
The ordinary-trusted observer/bootstrap assumption, 164-target/204-component
initial frontier, unknown dependency gaps, read/output ceilings, native layout,
mask checks, no-child behavior and closure_certified=false remain unchanged.

Root is the author of this minimal source delta, not its independent reviewer.
The same original noncontributor source auditor must receive the exact delta.
Neither source acceptance nor a later exit-0 finite observation opens author
runtime probes or P212 query/build phases without their separate gates.
