# P215 B preparation check note

The first read-only package hashing command named both the real
`RUNTIME_BINARIES.sha256` and a nonexistent singular spelling
`RUNTIME_BINARY.sha256`. `sha256sum` reported that one missing operand and
exited 1 after hashing the real files. No file was created, removed or changed,
and no verifier, canonical or run output was read or executed. The command was
not a package PASS. The corrected strict package check is recorded separately
after `SHA256SUMS` is created.
