# P214 Review B fresh build binding

2026-09-11 UTC. `BOUND_SOURCE_ONLY / NO_GRANT`.

Root's accepted P214 A build02 runtime content manifest remains an exact
223-row fixed list with SHA256
`35e6d5ac4cb0fb3933dc2d4ceb201d5afbf11315bdbcdcf74308a184c1586530`.
This preparation freshly ran its full strict content check successfully. It is
referenced in place and copied only by a future granted recipe; this is
explicit mechanical dependency reuse, not a newly discovered loader closure.

The nine Round1 source rows pass with manifest SHA256
`d4d1e2677ddb1df521cd8860527797d88caacebb94988a090a0c46fd7e55b090`.
The seven B science/history rows pass with manifest SHA256
`9531a8436025d17ee2fc1fe0d31a586ad4bea7ec353235d5554c28ab643941d5`.
The physical Round1 nonself manifest also passes.

`reviews/p214_b/build01` was absent, including as a dangling link. Available
workspace bytes observed were 12,673,503,232. The exact request uses a clean
environment, deterministic date controls, disabled TeX generators and the
guarded source recipe. No grant or operation follows from this binding.

Ordinary trusted TeX/bootstrap, path traversal, storage and supervisor timing
remain the inherited boundary. The 223 selected resources are content pins,
not complete syscall/loaded-memory attestation. Unknown FLS input or any final
diagnostic blocks acceptance. `OWNER_AMBER / HOLD_EXTERNAL`.
