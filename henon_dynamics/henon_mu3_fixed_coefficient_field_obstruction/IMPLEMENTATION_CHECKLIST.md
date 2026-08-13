# HCS-C44 implementation checklist

- [x] Producer uses only exact integer and finite-field arithmetic.
- [x] Checker is implementation-independent and type-strict.
- [x] All-prime theorem is distinguished from finite controls.
- [x] Histogram convention and rational normalization are frozen.
- [x] Special prime \(p=7\) is explicit.
- [x] The split-prime clock is \(\log p\); no chronological averaging.
- [x] Mutation tests target individual checker gates.
- [x] Default runner is read-only and manifest refresh is fail-closed.
- [x] Paper source and PDF are synchronized.
- [x] Route-A root and archived YAML are byte-identical.
- [ ] `code_commit` is a real implementation commit before final freeze.
