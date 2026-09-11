# One-use root grant: P215 Review B initial run

2026-09-11 UTC. Root accepts runtime preparation02 after full source, seal,
runtime, input-pin, syntax, JSON and exact-membership checks. The controlled
output path was first queried at root chunk `5922f0` and is absent, including
as a symlink.

Root authorizes exactly one submission of the command sealed in
`p215_b_execution_preparation02/REQUEST.initial.proposed.json`, from the
workspace root under its fixed clean environment. Preparation seal SHA256 is
`3c11f5eb22d0fbf2a7511d1a1f9577e51023aff8b8d354137b22256d8e7f5a28`.

The grant is consumed by the immediately following submission. Any failure or
partial tree is preserved without retry/reuse. This grants no DATA acceptance,
canonical adoption, strict replay, build, final B, Round2, terminal, central,
Git or external action.
