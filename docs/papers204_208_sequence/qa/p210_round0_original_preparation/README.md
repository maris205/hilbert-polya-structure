# P210 author-original reception preparation

Status: **PREPARED_ONLY / CHECKER_NOT_EXECUTED_BY_PREPARER / ROOT_RECEPTION_PENDING**.

This small read-only inspector was written by `/root/p210_author`, who authored the P210 manuscript and verifier and is ineligible for its independent manuscript A/B reviews. This is preparation for root to read, then actually execute separately. It imports only Python standard-library data/inspection utilities; it does not import, execute or shell out to any author audit, runner, verifier, build helper or external command. Its only output when run is a JSON documentary report on stdout. It writes no files, including on failure, and requires isolated, no-site, no-bytecode Python invocation. Root must capture the real command, full stdout/stderr and native return in a fresh root-owned directory.

## Exact inputs and boundary

The immutable author package is `papers/210-weakly-increasing-run-aggregation/` under the workspace. Its author-handoff `SHA256SUMS` is fixed at `b0c72e401acaf50acb611dc27f2ff1c45e3ad6e1b547218b48d13be8c82a0f6c`, with 489 nonself payloads. [INPUT_PINS.json](INPUT_PINS.json) directly binds that seal, the 19 archival original paths and system Python: 21 inputs. The pinned author seal transitively binds all 489 payloads, including the five complete original package ledgers and every archived native record. No host tree was copied or new broad host inventory generated for this preparation.

The inspector covers:

- Exact handoff membership and every payload byte; all five original producer/pair/build package inventories; full gzip-aware pre/post ledgers, including path spelling, resolved target, symlink, size and hash. The only historical exceptions are the exact five package/original-path/old-hash/snapshot/current-hash roles hardcoded from `HISTORICAL_INPUT_ROLES.actual.json`; there is no fallback for another mismatch.
- Entire recorded native argv, child environment, parent bounded relevant environment, start/end ordering, native status and complete stdout/stderr for all 59 child and seven enclosing parent records. The original author audit's enclosing return is now checked, not skipped. All six original `cmp` pairs are re-compared as full bytes; each of the five archived science outputs is compared with the full canonical bytes. No mathematical computation is rerun.
- Original observed Python imports/read attempts/loaded module paths/maps, isolated interpreter settings, source-only cache absence, conservative known source/runtime/configuration pins and recorded `ldd` resolution. The scope remains bounded post-hook observation plus pins, not OS/startup tracing. Failed cache-read attempts are distinguished from consumed bytecode. The complete original paths are memoized only for hash reuse, then every actually checked current path is reread uncached before the documentary result.
- Both actual author builds: exactly ten initial scientific source files, all four pass source/product ledgers, source invariance and successive product chains, physical saved intermediate logs/recorders/bibliography products, reconstruction of every ordered `.fls` input role including repeats, TeX resource/configuration lookup bindings, all final products, complete final logs/text/font reports and final six-page PDF hashes. Earlier overwritten intermediate PDFs have original hash-and-chain roles, not preserved historical PDF bytes; both final draft PDFs are physical.
- All 19 archival original/copy pairs as raw bytes; the archive script and native receipt bindings; the original documentary author audit's result/source/parent receipt; both six-page original author view receipts and their rendered/PDF bindings; exact selected live PDF equality with draft 02. Checking a view receipt is not a new page view. Source-access failures and the Robbins extracted-table caveat remain in the fully bound originals.

The checker does **not** cover the later root strict-author pair, its 54-payload package or root's new six-page view receipt. Those root-owned additions require root's separate exact-schema checks. It also does not perform mathematical review, science replay, TeX execution, page viewing, root acceptance, physical freezing, manuscript A/B, terminal evidence or batch completion. OWNER_AMBER / HOLD_EXTERNAL remain. The author paper was not modified.

## Root invocation after reading

Run from any working directory, with root recording the full actual streams and return separately:

```text
/usr/bin/python3.10 -I -S -B /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p210_round0_original_preparation/inspect_originals.py
```

The checker deliberately requires the exact original 489-payload author handoff. Run before adding paper-local lifecycle/frozen-round files; later growth needs a separately disclosed exact-role adapter, not a rewrite of this preparation or of the author seal. Its success label is only `PASS_DOCUMENTARY_ORIGINALS_ONLY`, with explicit zero science/build/view/review executions and `root_acceptance: false`. A native failure must be preserved and investigated; this preparation makes no passing-execution claim.

The preparation's own `SHA256SUMS` seals only its nonself files. It is not the paper's author seal or root's future whole-paper manifest. [STATIC_CHECKS.actual.json](STATIC_CHECKS.actual.json) preserves both actual static attempts: the initial overly broad method-name scan exited 1 because it mistook two string `replace` calls for filesystem replacement; the exact string-call-aware scan exited 0. The checker source was not changed to clear that false positive. These syntax/safety inspections parsed the source without importing or executing it and do not constitute a run of the documentary checker.
