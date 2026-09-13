# Paper28 capture failure — preserved, no retry

Date: 2026-09-05
Decision: CAPTURE_FAILED_PRESERVED_NO_RETRY
Current gate: NEW_USER_AUTHORITY_REQUIRED_FOR_ANOTHER_CAPTURE
Paper28 remains incomplete; Paper27 accepted local status is unchanged.

## Executed scope and observed result

The one E0230-authorized scanner-only transaction was executed once after the independent prospective plan/code PASS. Session 68136 terminated with exit 1, `CaptureStop: total byte bound`, during the first resource-tree census. No compiler, BibTeX, PDF utility, loader, version command or network client was invoked. No original source, system resource, old profile or old evidence was modified. New evidence is retained at `notes/dependency-capture-20260905`; never reuse or automatically retry that root.

Frozen pre-execution bindings:

- Plan SHA256: `b7ce665e8487cb6ff1ca0bde8726e838f2d08f4dd108f0b461af0f895fd51f80`.
- Scanner SHA256: `7b6731cb725a63beefea1ff3f46588be919e9858183f529dcec61bf66610393f`.
- ELF helper SHA256: `3e68a46b6821e500b2e95358f43c2de8803dd9f7f27669dce49406ecc95a9fa6`.
- Prospective review SHA256: `aca251a66a46d22efda86008571948d4328c44f1b1c0ce24e3c6fd1e411986f9`.

The code and review remain unchanged historical records; their synthetic/pre-execution PASS is not an executed-capture PASS.

## Retained failure evidence

| Artifact | Observed bytes | SHA256 / scope |
| --- | ---: | --- |
| failure.json | 116 | `8e729eee8c6bbfc2986bc6b9482823cf397e80f922e014c3c98b89576f408c57` |
| intent.json | 2301 | `96163eb92f5c8b26ec510c793bb397562dd15f7c61f529be8aee7d2783943c83` |
| events.jsonl | 39077086 | Only bounded head/tail/metadata inspected after failure; no all-reads completeness claim |
| capsule.tar | 2237605376 | Partial evidence; not fully rehashed/validated or extracted, not accepted for build use |

The last progress event reported 112000 captured entries and 2147201912 admitted regular bytes. The final journal entry is `/usr/share/texlive/texmf-dist/tex/generic/tex4ht/textures.4ht`, 1872 bytes, SHA256 `370108808e5d7a8538e2588ed55967da2e8f56fe1a485723f88aa73f5493306c`. The last progress counter is not a final census. Archive size includes headers/padding and is not equal to regular input-content bytes.

The traversal had not finished the first TeX resource tree. The subsequent named-tool loop, static native-dependency closure, terminal source/resource rebind, manifest and successful outcome stages were not reached. There is no dependency-capsule integrity PASS, executable successor-build-profile PASS, measured Paper28 page count or PDF acceptance.

## Cause and additional limit-check defect

The planned full resource-tree superset was too broad for the agent-selected 2 GiB regular-byte budget. Its failure does not demonstrate a mathematical, source, layout or compiler defect in Paper28.

The independent bounded failure check also confirmed a code defect: `visit()` reads a regular file before `add()` enforces the cumulative budget. The rejecting file was therefore read into memory but was not added to the journal/archive, and the exception did not record its path. The actual guarantee was only that admitted/archived regular bytes stay below the limit. Do not claim all resource input reads were strictly capped at 2 GiB, or that the partial evidence records every actual read. No inference of the unrecorded file's identity is made. This contradicts the plan's stronger total-input bound and must be repaired prospectively, not concealed or retroactively patched.

Main and an independent agent checked the exact failure/intent, last journal entries and named output sizes without rereading system dependencies or extracting the archive. That is a bounded failure diagnosis, not a successful full capsule audit. No further capture, source mutation, cleanup or root reuse occurred after the failure.

## Proposed recovery — not yet authorized or executed

Ask the user once for a fresh capture successor: retain all old code/failure/evidence, use an entirely new output root, narrow TeX/font/runtime capture to the actual locked manuscript/tool requirements, and perform a metadata-only capacity census before content copying. Repair cumulative-budget enforcement before any file bytes are read and record each attempted path so a stop is diagnosable. Freeze and independently review the revised plan/code before a new one-time capture; do not simply raise the bound and replay this script. Continue to forbid discovery compilation, network access, system-input mutation and unreviewed capsule use.

Exact narrowed paths, new code and new root must be specified prospectively after that recovery authority; this record does not create them or assume permission. No new confirmation is needed for Paper27's already consumed directory predicate. The permission gap concerns only an additional Paper28 capture after the authorized one failed.

The paper-compile skill was used for prerequisite and output-check discipline; the project's explicit one-time capture and preserved-failure contract controls this stop instead of the skill's generic retry/cleanup examples. OUTPUT_ACCEPTANCE_SCOPE_20260905.md separately records the Paper28-specific future page/link/metadata checks, not a build authorization.
