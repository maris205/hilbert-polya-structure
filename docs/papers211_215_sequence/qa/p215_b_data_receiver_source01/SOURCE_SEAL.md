# P215 Review B initial DATA receiver source seal

2026-09-11 UTC. `SOURCE HOLD / NOT EXECUTED ON SCIENTIFIC DATA`.

The receiver passed syntax checking and the synthetic negative-only self-test.
No P215 B capture member or scientific output was returned or read. The broad
discovery traversal documented in `SOURCE_STAGE_FAILURE01.md` nevertheless
violated the stricter no-query boundary, so this is not an accepted source
seal. The three-entry integrity manifest `SOURCE_INPUTS.sha256` passed strict
verification and has SHA-256
`5adf562f613ef807c943ff9ebd1289f69eaa0f52d7cf735a3831f189d41d46a5`;
it is not an acceptance seal.

The receiver's later exclusive `INITIAL_NATIVE.json` is deliberately outside
this pre-execution source seal. No canonical, strict replay, build, manuscript,
central-index, Git or external action is authorized by this seal.
