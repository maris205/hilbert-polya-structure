# P212 terminal02 one-build grant

ISSUED_AND_CONSUMED_ON_SINGLE_SUBMISSION, 2026-09-11 UTC. This grant is independent from
terminal01 and usable only after terminal01 returns and cold_build_2 remains
absent. Authorize exactly one invocation of
`BUILD_REQUEST.sh --execute-under-separate-root-grant terminal02` under the
same fixed 13-variable clean environment. It may exclusively create
qa_final/cold_build_2 and perform the same source-only capture. No retry,
cleanup, science, PDF adoption, Git, or external action.
