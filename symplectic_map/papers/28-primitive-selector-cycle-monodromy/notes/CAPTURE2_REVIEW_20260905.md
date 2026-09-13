# Paper28 capture2 independent prospective review

Date: 2026-09-05
Reviewer: independent subagent `/root/p28_capture2_review`
Decision: CAPTURE2_PLAN_CODE_PASS
Scope: the authorized, narrowed, one-shot resource capture only; not executed-capsule integrity, dependency completeness, build or publication acceptance.

Plan SHA256: ae3db611c0caf8be7883800588c72930f93415caa3f6eaa67a19c24174b7292d
Scanner SHA256: 495672257827582950d10179a746d7c961d1f0c44b6e7cdda1bff7bcc98bec90
Utilities SHA256: 7b6731cb725a63beefea1ff3f46588be919e9858183f529dcec61bf66610393f
ELF helper SHA256: 3e68a46b6821e500b2e95358f43c2de8803dd9f7f27669dce49406ecc95a9fa6
Prior failure result SHA256: 8028fcb97e130cd162393388e48bb82ae437e7484505f2ff88cd3e6abeee2e5c

## Review performed

Read the complete final `CAPTURE2_PLAN_20260905.md` and `CAPTURE2_20260905.py`, the complete reused `DEPENDENCY_CAPTURE_20260905.py`, the complete byte-only `CAPTURE_ELF_20260905.py`, and `DEPENDENCY_CAPTURE_RESULT_20260905.md`. Re-read the final plan/controller after the prospective corrections and independently hashed the exact administrative files above. The latest user confirmation supplies the fresh-capture authority; it is not pending again.

Ran only the permitted synthetic self-test command against the final controller:

`/root/miniconda3/bin/python3.12 -I -S -B notes/CAPTURE2_20260905.py --self-test`

Result: exit 0, `CAPTURE2_SELF_TEST_PASS: pre-read refusal, cumulative/per-file limits, exact-bound reads, scope and memory archive`.

No system-resource census/content probe, capture, compiler/BibTeX/PDF-tool invocation, network operation, build-root access, archive extraction or source edit was performed by this reviewer. The configured Python bootstrap and standard-library imports are the plan's explicit trusted control plane, not a claimed resource-capture trace.

## Technical findings

- The new collector's initial traversal is metadata/readlink/directory-membership only. All named roots, exact inputs and required files are visited before the first resource content-copy wave. Each wave freezes its census and checks the entire pending regular-byte sum before copying. Later ELF-discovered candidates enter another metadata-only wave rather than being read immediately.
- The former read-before-cumulative-limit defect is not on the resource-content execution path. The new collector uses its own `visit`, `add`, `read_one` and `copy_wave`; borrowed `resolve`, `native_closure` and `terminal_rebind` dispatch to the new metadata-only methods. The old `capture`, `Scanner.visit` and `Scanner.add` are never called. The reused `read_regular` is confined to the explicitly trusted, hash-checked manuscript source bindings, not resource capture.
- The imported utility namespace is rebound to the new `TREES`, `LIBDIRS`, `EXACT`, `OUTPUT` and limits. Imported main entry points do not execute. Both code hashes and the caller-supplied independent-review hash are bound before exclusive creation of `notes/dependency-capture2-20260905`; no old-root probe, reuse, deletion or retry path is present.
- Each regular-resource attempt first records and fsyncs its path, expected size, prior actual-byte count and remaining budget. The budget is checked before opening content and again after census-versus-fstat identity verification, before reading. Each `os.read` request is at most the reserved expected bytes remaining; there is no unreserved EOF/growth probe. Returned chunks immediately advance the resource-byte counter, and ordinary read/archive failures retain the active path, byte count and available prefix digest. Final descriptor/path checks reject observed drift. In-flight syscalls, abrupt interruption and atomic filesystem snapshots are expressly not overclaimed.
- The fixed bounds remain 2 GiB actual resource bytes, 256 MiB per regular file, 50000 unique entries and 64 closure waves. The synthetic insufficient-total, cumulative and per-file cases reject without invoking their reader; exact-bound and zero-size cases pass without extra reads.
- The declared fonts are the CM/AMS and Latin Modern metric/Type1/encoding subsets plus explicitly named PDF fallback families, not all installed fonts. The 17 locked packages, `article.cls` and `plainnat.bst` are explicit required paths, as are `pdflatex.fmt`, `pdftex.map` and the configured tools. The two named `ls-R` target additions are exact optional paths, not an enlargement to a distribution/library-root census and not an assertion of current existence.
- Symlink targets are metadata-resolved within the narrowed envelope, ordinary library directories are not broadly listed, and excluded/missing/unsupported cases remain explicit. Raw symlink text is retained in the archive, which must not be blindly extracted. Actual aliases, transitive package/font availability, native candidate usefulness and later search/loader behavior remain for the capsule/profile checks already required by the plan.
- Root/output creation is exclusive, with 0700/0600 requested modes and no input mutation. The completed outcome binds only preceding artifacts, not itself. Success requires no unread regular row or active read and equality of actual resource-read bytes with the recorded regular-byte sum; archive-member and receipt reconciliation must still be checked independently on the actual output.

The prospective review identified one small plan/code discrepancy: the durable read-intent initially omitted the explicitly promised remaining-budget field. The author added that field before the final hashes above; the final re-read and self-test passed. No unresolved blocking prospective defect was found in the reviewed scope.

## Decision boundary

This PASS permits only the already authorized single capture execution under these exact bytes. A successful controller outcome is `CAPTURE2_RECORDED_REVIEW_REQUIRED`, not a capsule-integrity or hermetic-build PASS. Preserve the first failed capture and all frozen source/profile/review records. Review actual archive/manifest/receipts/coverage before use, then freeze and review the separate executable Paper28-specific successor build profile. No compilation, page count, PDF acceptance or Batch07 completion is inferred here.
