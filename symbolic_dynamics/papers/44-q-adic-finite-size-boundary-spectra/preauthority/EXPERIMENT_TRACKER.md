# Experiment tracker

This tracker is deliberately outcome-free at package freeze. Filling any
result requires an executed command, sealed outputs, and a new manifest.

The neutral shared raw-input manifest is already frozen at SHA-256
`2421795bb1d341805f185fd9941db6ba31d9c521e0cbe1ff28fb24a0617dba10`.
It contains no expected output and is not an experiment result. Each future
evaluator must independently expand it before sealing its own source.

| Run | Claim/block | Evaluator A | Evaluator B | Mutations | Status | Evidence path |
|---|---|---|---|---|---|---|
| M0 | B5 contract lint | not run | not run | not run | `TODO` | none |
| M1 | C1/B1 exact census | not implemented | not implemented | not run | `TODO` | none |
| M2 | C1/B2 residue/image mechanism | not implemented | not implemented | not run | `TODO` | none |
| M3 | C2/B3 golden separation | not implemented | not implemented | not run | `TODO` | none |
| M4 | C2/B4 and B5 closeout | not implemented | not implemented | not run | `TODO` | none |

## Entry schema for future authorized runs

Each completed row must add:

- UTC start/end time and exact command;
- code commit or immutable source hash;
- environment/toolchain lock;
- input-fixture manifest hash fixed before expected outputs are exposed;
- evaluator-specific output manifest hashes;
- canonical projection comparison;
- mutation-by-mutation outcome;
- success, failure, or inconclusive decision under `EXPERIMENT_PLAN.md`;
- deviations and whether they were outcome dependent.

No `PASS` may be entered merely from the proofs or the witness ledger.
