# Paper 12 exact experiment package

This is a closed-world, exact-integer CPU package for the single frozen candidate `henon_period3_residue_v1`. Track Q and Track R share only definitions and types-only JSON schemas. Their scientific engines have separate roots, helpers, representations, and formula routes.

Current state is pre-execution only. The registered tuple is exactly `[8,9]`; its scientific evaluators must not be called by development tests. Historical `m=2,...,7` values are disclosed by the frozen source package but are neither stored nor read here. No expected `D8`, `D9`, `E8`, or `E9` value is present.

## Safe pre-execution sequence

Run from this paper directory with bytecode and pytest caches disabled:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B -m pytest -p no:cacheprovider code/tests \
  --junitxml=preexecution/junit.xml
PYTHONDONTWRITEBYTECODE=1 python -B code/scripts/run_safe_preflight.py
PYTHONDONTWRITEBYTECODE=1 python -B code/scripts/freeze_code_manifest.py
```

These commands run quartic `m=2`, schema, security, lifecycle, quarantine, and contract tests only. They do not call either valid registered coefficient evaluator and must leave `registered_audit_count=0`, with no runtime claim/result/terminal.

After the code manifest is created, a fresh reviewer who did not author the candidate code must inspect the complete tree, JUnit, preflight, source bindings, Q/R independence, capability gates, recursive validators, and one-shot lifecycle. The reviewer alone may append `preexecution/INDEPENDENT_DEPLOYMENT_REVIEW.json` in canonical JSON using schema `HENON_PERIOD3_INDEPENDENT_DEPLOYMENT_REVIEW_V1` and verdict `DEPLOYMENT_PASS`, with all ten keys listed in `bootstrap.review.REQUIRED_CHECKS` set to `PASS` and exact hashes of the three reviewed preexecution artifacts.

Do not edit any code, test, JUnit, preflight, manifest, or review after that authority is issued. A change requires a new candidate version and fresh review; it is not a rerun.

## Sole registered transaction

Only after an independent deployment PASS:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B code/scripts/verify_preexecution.py
PYTHONDONTWRITEBYTECODE=1 python -B code/scripts/run_registered_once.py
```

The second command creates the durable `STARTED` claim before any scientific import. Each child process verifies a claim-bound capability containing its frozen runner/engine/definitions hashes. Its audit hook rejects and records reads, writes, imports, process, loader, and network capabilities outside exact allowlists. Q is sealed and rehashed before and after R. The noncomputing adjudicator reads and validates both canonical envelopes before it opens the private quartic/counter ledger. Every post-claim exception is terminalized, and all official writes are exclusive, file-fsynced, and directory-fsynced. There is no authorized second claim, result, terminal, or registered run.

The result is an implementation-agreement certificate under external source-proof authority. It never emits a source-level `PROVED` verdict and does not establish universal nonvanishing, all-`m` period-three separation, or any global quartic classification.

## Append-only result review and closure

After a successful terminal, a fresh result-only reviewer may read the sealed R100 artifacts and append `runtime/candidate_v1/review/INDEPENDENT_RESULT_REVIEW.json`. The reviewer may check hashes, namespaces, P1--P10 witnesses, controls, counters, and scope, but may not select another parameter or perform any scientific computation.

Once that canonical `RESULT_PASS` exists, run the separately hash-bound, science-free analyzer exactly once:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B code/postrun_analyzer/analyze.py
```

It validates path/hash pairs and writes `runtime/candidate_v1/official/result_manifest.json` with exclusive create and durable fsync. A failed validation leaves no manifest; an existing manifest is never overwritten.
