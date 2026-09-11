# P214 Review B build02 fresh binding preparation

2026-09-11 UTC. `BOUND_SOURCE_ONLY / NO_GRANT / NOT_EXECUTED`.

Build01 remains permanently HOLD for its final science-manifest cwd failure;
the exact cause and four-line recipe delta are recorded in
`BUILD01_HOLD_AND_DELTA.md`. No build01 output or page view is reused.

Fresh preparation checks passed all nine Round1 source rows, all seven B
science/history rows, the physical Round1 30-row nonself manifest, and all 223
accepted runtime content rows. Their manifest SHA256 values remain,
respectively,
`d4d1e2677ddb1df521cd8860527797d88caacebb94988a090a0c46fd7e55b090`,
`9531a8436025d17ee2fc1fe0d31a586ad4bea7ec353235d5554c28ab643941d5`,
`0f37b61c4a52ea3289daf4eda2b82fca489b60bf34e0141e3907b074badda3e0`
and
`35e6d5ac4cb0fb3933dc2d4ceb201d5afbf11315bdbcdcf74308a184c1586530`.

`reviews/p214_b/build02` was freshly absent, including as a dangling link;
12,637,069,312 bytes were available. The new recipe is Bash-syntax valid and
144 lines. It changes only the preparation path, output path, and the two
explicit workspace-root science checks described by the exact delta.

Ordinary trusted TeX/bootstrap, path traversal, storage and supervisor timing
remain inherited boundaries. The 223 resources are content pins, not complete
syscall or loaded-memory attestation. Unknown FLS input or any final diagnostic
blocks acceptance. This binding preparation issues no grant and performs no
build. `OWNER_AMBER / HOLD_EXTERNAL`.
