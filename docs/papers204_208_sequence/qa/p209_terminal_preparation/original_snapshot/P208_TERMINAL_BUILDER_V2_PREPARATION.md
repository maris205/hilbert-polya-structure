# P208 terminal builder revision 2 — prepared, not built

2026-09-06 UTC. The new [379-line revision](run_p208_terminal_builds_v2.py)
has SHA256 `7399c2db47f08001152277cbddff6a544831a424702ec77ee7af510c8a92ad6c`.
Root read its complete implementation and the complete independent
[original-version code audit](P208_TERMINAL_BUILDER_CODE_AUDIT.md).
The audited original and its preparation/audit input bytes remain unchanged.
No accepted author/reviewer recorder is imported or edited.

## Applied audit changes

- TB-1: record early and late actual parent file-backed mappings/modules;
  rehash the early inputs after; include normalized configuration bytes and
  the early actual parent inputs in the exact coverage union. Add the gconv
  tree, including the observed cache, to the before/after inventory.
- TB-2: add the known Poppler data tree. Require the exact eight-key parent
  environment and workspace cwd before any outputs, and record original
  argv, flags, interpreter, cache prefix, environment, PID and sample phase.
  State that child mappings/transient loads/non-fls resource accesses are
  not directly observed. Known potential resources are not called consumed.
- TB-3: use explicit exceptions for optimization/isolation/no-bytecode/
  alternate-cache/argument/environment guards. Internal assertions are used
  only after the unconditional optimization-zero check.
- TB-4: save attempted argv/cwd/settings before spawning, and distinguish
  NOT_STARTED OSError from an interruption with no completed-child result;
  never invent an exit code. Independently collect and promptly save every
  available after-inventory, preserving failed collection/equality phases.

Root additionally linked the required physical Round2 to a future exact
root freeze receipt: 487 payloads, complete manifest hash, accepted current
B seal and delta hashes, and the eleven exact source-only inputs. The
allowlist was checked against the actual main TeX includes and local files:
three top-level inputs and sections 00 through 07. No local figure/style
resource is referenced. Existing complete source reading supports this
specific P208 contract; the builder is not a generic resource discovery tool.
Effective user TeX roots are queried in each cold cwd and must be absent
before and after, rather than treating hard-coded `/root` inventory paths
as the effective HOME-absent search path. Extracted-text markers and final
rerun diagnostics also gate success. Seven rendered files never imply views.

## Actual preparation tests and limits

The [actual preparation receipt](P208_TERMINAL_V2_PRELAUNCH.actual.json)
preserves the full returned combined outputs and exits of:

- an isolated metadata-only helper probe (exit 0), finding 1,788 configuration
  records and 271 Poppler files, exact coverage of both actual locale/gconv
  mappings, all eleven sources present, and no qa_final directory;
- an optimized invocation rejected by the explicit guard (exit 1);
- an otherwise controlled invocation rejected because physical Round2 was
  absent (exit 1), before any output directory;
- a direct qa_final absence check (exit 0).

Both guard refusals were actually observed once before the recorded repeat;
neither was a build attempt. An AST parse also passed. During unexecuted
draft editing a string-substitution splice and provisional source labels
were corrected before the AST check; no broken version was executed or
represented as passing. The exact tests above use the final recorded hash.

The independent auditor reviewed the original implementation, not this new
revision; root's code inspection and metadata/negative tests are not a new
independent acceptance. Child-spawn failure and closure-component failure
branches were inspected, not artificially injected. The finite provenance
scope does not claim continuous child tracing or a hermetic kernel image.

The project research and paper-compile skills caused the gated source-only
pair, preserved diagnostics, font/reference checks and explicit pending
actual views. No cleanup, scientific changes, compilation, package install
or external release occurred. At this receipt there is no accepted B delta
in root's ledger, no physical Round2, no qa_final and no P208 terminal PASS.
HOLD_EXTERNAL remains.
