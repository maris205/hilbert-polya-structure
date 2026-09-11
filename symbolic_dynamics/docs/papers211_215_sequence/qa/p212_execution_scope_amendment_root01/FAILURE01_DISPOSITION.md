# Root documentary receiver pathname correction

The first actual independent-audit receiver failed (11654a, exit1) while
reading an archived successful source command. That command's operand was
`qa/p212_dependency_source_root01/RECEPTION.md`, with the explicitly recorded
cwd `docs/papers211_215_sequence`. Root's first receiver wrongly treated every
operand as workspace-root-relative. No submitted source, audit or input failed.

The failed complete native and source remain unchanged. The new-only
receive_audit02.js resolves each archived sed/cmp operand under its exact
recorded workspace cwd (or actual default workspace cwd when omitted),
checks that resolution remains strictly within the workspace, and still
compares the full raw source range or both operands. It additionally keys
the old failed source, new source and failure original. No source or history
is rewritten, no field/content comparison removed, and no operation granted.
