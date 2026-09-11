# P211 initial-build infrastructure independent audit

2026-09-08 UTC. Auditor `/root/p211_runtime_independent_audit`.
**HOLD_CURRENT_BINDING — BLD-I1 Major/open.**

One concrete blocker was found in truthful failure-stream finalization.
No additional concrete blocker was identified in the inspected ENV8,
future-cwd configuration, selected dependency or ordered-FLS paths. This
report does not authorize production or claim TeX dependency completeness
from a build that has not happened.

## BLD-I1: unknown pre-return native outcome is treated as settled

In [build_core.py](../p211_build_preparation/build_core.py), lines 211–212
initialize `proc=None` and `settled=True`. `Popen(...)` is assigned at
lines 220–222, so an interruption/exception before that call returns can
leave no returned handle. The catch-all `BaseException` handler at 229–230
changes only the reason/error. Since `proc` remains `None`, the whole
session-settlement block at 231–257 is skipped. The recorder then writes
`streams_settled=True`, hashes available raw streams, and creates a normal
`RECEIPT.json` at 258–272.

An absent returned handle is not evidence that no native writer exists.
For this branch, neither an `UNCLOSED.json` marker nor a missing receipt
remains. Therefore `incomplete_native()`/`seal()` at 276–289, and the inner
and outer corresponding checks, can seal a `FAIL_PRESERVED` artifact whose
writer outcome is unknown. The failure is **not** falsely upgraded to a
successful build; the defect is the unsupported final stream hashes and
immutable failed-artifact/settlement claim.

[STATIC_BRANCH_WITNESS.json](STATIC_BRANCH_WITNESS.json) binds the exact
current source path and mechanically inspected catch/guard structure.
This is a static finding, not a claimed live failure reproduction. The
archived static test checks existing settled records and the presence of
an incomplete-attempt guard; it does not cover this path with a receipt
already written.

Required scoped correction: preserve the original package; in a new version,
conservatively record any uncertain no-handle outcome without final stream
hashes or a completed native receipt, force every enclosing seal to refuse,
and verify that branch with a focused non-scientific regression. Do not
erase or relabel the original finding. A new code-dependent lock and exact
root-reviewed binding are required after the change.

## Other inspected mechanisms

- Exact ENV8 has no HOME; the native command vectors explicitly use that
  environment. Python entry gates bind isolated/no-site/no-bytecode settings.
  The three unset-HOME TeX roots are correctly represented as separate
  future `inner/source_only` ABSENT roles, not diagnostic-cwd absence reused
  as the production key (`build_p211.py:21–98`).
- The code admits nine physical pinned sources into an initially source-only
  directory and defines exactly pdflatex, BibTeX, pdflatex, pdflatex, with
  shell escape disabled. There is no cleanup/fix/install/automatic retry.
  Root still must approve the actual nine-source static graph; I did not
  read TeX bodies or follow their pins.
- The candidate retains 840 spellings / 795 file entries, 33 selected ELF
  inputs, 173 metrics, 115 mapped font/encoding names, AMS class/style and
  optional absent `amsart.cfg`. Query commands, full original resolutions,
  selector records/reasons and the saved closing configuration agree.
  Current five code files equal the candidate and physical executed copies.
- Ordered FLS classification preserves duplicate spellings and distinguishes
  sources, prelocked external inputs, generated-before inputs and inputs
  following same-pass outputs. It explicitly does not equate a pass-end hash
  with read-time bytes. BibTeX has separately stated auxiliary/style/database
  evidence, not an invented FLS trace (`build_p211.py:101–194`).
- Ordinary returned-handle settlement and missing-receipt guards are present.
  Immutable pass copies, warnings, measured pages, embedding checks and
  NOT_VIEWED render records remain distinct from root acceptance. These
  observations do not waive BLD-I1 or constitute a live build/kill test.

## Evidence and scope

[RESULT.json](RESULT.json): **791 integrity/static checks**, **271 complete
read inputs / 1,772,893 bytes**, **32 archived native receipts**, and **10
fresh read-only native commands**. Five actual cmp commands verify current
code against diagnostic05 executed copies; five actual diff commands match
every byte of the saved diagnostic01-to-current native deltas. Separate
raw stdout/stderr and real exits are retained in `native/`.

The discovery05 187-payload and diagnostic_capture05 61-payload manifests
were checked completely. The top seal matches the supplied 891-payload
manifest SHA256
`5fa2620b27e04f0d07f9b72434f801a948e95d7df884d2e46a915c42028bd042`;
this audit verifies **263 selected payloads**, not all 891. The candidate
matches `4c66d15e0720bb064fe890c81d531d2400b99891e7f59e537a42657c685d31e6`.
[READ_INPUTS_BEFORE.json](READ_INPUTS_BEFORE.json) and
[READ_INPUTS_AFTER.json](READ_INPUTS_AFTER.json) are the equal full selected
read inventories. [TOOL_RETURN.actual.json](TOOL_RETURN.actual.json) is the
actual decoded checker-tool return, not fabricated outer raw streams.

No submitted script was executed/imported; no TeX/science/canonical body,
proof or old builder was read; no build, render, live settlement stress test,
Git, external action, original mutation or child delegation occurred. Host
dependency referents were not freshly recaptured. Root separately receives
all originals and the actual science. No unavailable OS tracing or recursive
host coverage is demanded; the finding is inside the recorder's own claimed
bounded settlement contract. The earlier 41-payload runtime audit is unchanged.

The paper-compile and project skills/contracts were read. They influenced
the checks for preserved logs/warnings, measured pages and fonts, while the
explicit read-only task overrode generic compile/cleanup/retry/source-edit
steps. This is infrastructure review, not proof contribution or manuscript
review. Any later revision verdict belongs in a separate immutable package.
