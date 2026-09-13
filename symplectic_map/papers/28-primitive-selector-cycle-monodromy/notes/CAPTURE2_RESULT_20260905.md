# Paper28 narrowed capture result

Date: 2026-09-05
Execution: session 66176, exit 0
Controller decision: CAPTURE2_RECORDED_REVIEW_REQUIRED
Independent archive audit: CAPTURE2_RECORDING_INTEGRITY_PASS.
Runtime/build acceptance: NOT_YET_ESTABLISHED; next step is the scoped executable successor profile.
Paper28 is not yet compiled or locally accepted; Batch07 remains 1/5 complete.

## Authority consumed and fixed inputs

The user's latest “确认” approved the fresh narrowed capture after the first capture failed. That authority has now been exercised exactly once in `notes/dependency-capture2-20260905`; do not ask for it again or rerun this successful transaction. The prior capture's failure, partial evidence and code remain unchanged. Paper27's local acceptance prerequisite is unchanged.

The new controller reduces the broad font-distribution sweep to explicit manuscript/runtime resource families, performs metadata-only capacity censuses before copying, checks each file's remaining budget before open and again before the first read, and records path/size/budget plus actual bounded-read receipts. The maximum remains 2 GiB; it was not raised.

Exact executed identities:

| Artifact | SHA256 |
| --- | --- |
| CAPTURE2_PLAN_20260905.md | `ae3db611c0caf8be7883800588c72930f93415caa3f6eaa67a19c24174b7292d` |
| CAPTURE2_20260905.py | `495672257827582950d10179a746d7c961d1f0c44b6e7cdda1bff7bcc98bec90` |
| CAPTURE2_REVIEW_20260905.md | `0e9f1cd8d4c92d71166d327b95239df497dfec0d7b24c0515c860d704555bc58` |
| Frozen reused utilities | `7b6731cb725a63beefea1ff3f46588be919e9858183f529dcec61bf66610393f` |
| Frozen byte-only ELF helper | `3e68a46b6821e500b2e95358f43c2de8803dd9f7f27669dce49406ecc95a9fa6` |

The independent prospective review and synthetic tests applied before execution, including tests that an insufficient cumulative/per-file budget never calls the reader. Only selected safe utilities/metadata methods were reused; the old resource `visit`/`add`/`capture` execution path was not run.

## Actual capture

- 6838 manifest entries: 6050 regular files, 646 directories and 142 symbolic links.
- Exactly 314923719 resource-content bytes read, approximately 300.33 MiB, with equal archived regular-byte sum.
- Seven nonempty copying waves, then one final empty census. Every wave records its complete pending-file capacity before copying.
- Wave 0: 5974 regular files / 245981687 bytes. Later native waves add 46 / 59255672; 14 / 6140688; 11 / 3226024; 3 / 183080; 1 / 89096; 1 / 47472.
- 381 statically parsed native dependency edges; zero unresolved edges within the declared candidate-search model. This is not proof of arbitrary runtime loader/dlopen closure.
- All 19 required class/package/style files, the installed pdflatex format and PDF font map, and named tools passed the required-file metadata census before the first resource byte read.
- Source trio identity passed before and after capture: main `bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e`; macros `16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5`; bibliography `e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e`.

Key evidence under the new output root:

| Artifact | Bytes | SHA256 |
| --- | ---: | --- |
| capsule.tar | 320194560 | `c1b7f241f2ef7d49de26868b5a23642eb0ddd1271896a72faeea4da97ccc457a` |
| manifest.json | 3963641 | `6107892d5f9750e91ae48292a68117d490876b8a3164758dfdc3442e04eebb8d` |
| events.jsonl | 5602303 | `6fdb1bc75fa722eae5241c08bca8ef5d5cdd71dde4e26bd598fceb82e475a2da` |
| outcome.json | 2148 | `8a081a5f7a66fbcdd4d47899c4af1581ac9fba65c25d002609c118fc634b69f2` |

The outcome binds 12 preceding outputs: intent, journal, archive, eight census records and manifest. It does not hash itself. Archive bytes include headers/padding; they are not the resource-read count. The archive is not blindly extractable: literal links and omitted targets must be handled by the later reviewed namespace/materialization rules.

## Disclosed omissions and later-profile obligations

All 213 omissions are retained: 198 missing candidates, eight declared exclusions, five out-of-envelope symlink targets and two excluded search directories. Of the missing candidates, only three are non-library paths: optional `/usr/share/fonts/type1/lmodern`, optional Liberation2 fallback directory and `/var/lib/texmf/web2c/texmf.cnf`. Latin Modern resources are nevertheless captured under the declared texmf font tree; the required map/format files passed.

The five out-of-envelope targets are generated language.dat/language.dat.lua/language.def and distribution fmtutil/updmap configuration targets. The proposed later profile must use the captured precompiled format and existing map and prohibit format/map generation or undeclared language initialization; it must not silently read those targets. Tcl/Tk feedstock build-path RPATHs are excluded and no GUI workflow is intended. These are prospective scope constraints, not empirical confirmation that every later command has already run successfully.

The next step after actual archive verification is the independently reviewed executable build profile: frozen materialization/read namespace, library/search choices, fixed environment/commands, complete validators and Paper28-specific page/log/PDF checks. No system first-read discovery may occur in a formal build. No further dependency capture, source modification or public effect is implied by this result.

## Completed independent recording-integrity audit

CAPTURE2_AUDIT_20260905.md, SHA256 `267648ddcc4292593c1c3d7e159fbcac96b6d3f455f9d6afeaaa5d03a741dc8b`, reports `CAPTURE2_RECORDING_INTEGRITY_PASS` and explicitly `NOT_YET_ESTABLISHED` for runtime/build acceptance. The main agent read the complete report and rebound its exact hash.

The fresh auditor verified every one of the 12 sealed outputs, all 6838 tar members, all 6050 regular byte strings/hashes/LF counts, literal links and 199 exact PAX path extensions; replayed 27918 journal events including every read intent/completion and eight capacity censuses; and resolved all 6836 aliases using captured link data. An independent in-memory decoder reproduced all 381 dependency edges from 165 archived ELF files. No concrete recording-integrity discrepancy remains and no recapture is requested.

The 52 multi-candidate native edges still require fixed actual loader/search choices in the next profile. The missing generated configuration targets, disabled regeneration/GUI workflows, controlled imports and captured-only namespace restrictions above remain applicable. This audit does not authorize generic archive extraction, live-host fallback or compiler startup by itself. Proceed to the already scoped successor-profile work; do not start another capture or reopen the completed capture-review loop.

The final main-agent rebind confirmed the original ledger, Paper27 acceptance, Paper28 source trio, first failure result and first failure.json unchanged. No new user confirmation is pending for this completed capture stage.

## Preservation and skill role

No compiler, BibTeX, PDF tool, version command, loader subprocess or network operation ran during capture. No source/system resource, old root, failed evidence, old review or frozen controller was altered or deleted. The first failure.json remains SHA256 `8e729eee8c6bbfc2986bc6b9482823cf397e80f922e014c3c98b89576f408c57`. The capture's configured administrative bootstrap/kernel assumptions and lack of atomic-snapshot or arbitrary-runtime attestation remain explicit.

The paper-compile skill informed prerequisite/output-check discipline. The user-controlled narrowed-capture and preservation contract governs the execution; no generic cleanup, installation, automatic retry or manuscript compression was performed.
