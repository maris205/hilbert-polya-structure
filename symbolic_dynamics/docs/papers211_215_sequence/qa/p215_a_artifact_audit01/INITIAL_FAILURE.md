# P215 A artifact checker initial failure

Actual read-only invocation chunk `f3a185` exited 1 before later checks because
the checker expected 26 stderr files inside the 160-file build tree, while the
tree contains 25. All 25 are empty. Root's broader count includes binding-side
capture roles outside the build tree. The checker was narrowed to state its
actual tree scope; no build artifact, binding evidence or failed invocation was
deleted or rewritten. This was a DATA-checker accounting defect, not a TeX,
manuscript or scientific failure.
