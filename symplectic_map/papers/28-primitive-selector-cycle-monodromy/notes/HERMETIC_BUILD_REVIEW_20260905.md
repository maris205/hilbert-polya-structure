# Paper28 independent prospective executable-profile review

Date: 2026-09-05. Reviewer: `/root/p28_profile_review`.

Decision: `EXECUTABLE_PROFILE_REVIEW_PASS` for the exact four control files and source trio bound in the accompanying JSON. This permits the already authorized one-shot local build to enter its execution gate. It is not a claim that compilation, PDF validation, visual review or local acceptance has happened.

## Bound implementation

| Control | Bytes | SHA256 |
|---|---:|---|
| HERMETIC_BUILD_20260905.py | 36786 | `3081c6c677fac2ac4adca4fe34066289708875e9280bce2a035a517653a1b098` |
| HERMETIC_BUILD_PLAN_20260905.md | 11714 | `dddff3b541e91d8175934e64a551f74d6ad74a55de9232e617e655076e322be8` |
| PDF_ACCEPTANCE_20260905.py | 38573 | `e173a8a54d051f8d296b5d1319a44bdea0f30d3ab0be91cc16747027bf9a126c` |
| LOADER_SELECTION_20260905.json | 259022 | `ecc5e3751def20eac1bb96a2ddb5336925d46cf8fcb80b5ee60f4ab25bed9606` |

The JSON also binds each manuscript member by exact bytes, LF count and SHA256; the accepted capture audit and outcome; and the capture manifest/archive. The controller requires the exact review SHA256 as an execution argument, avoiding a review/controller self-hash cycle. The only execution namespace is the exclusively created `build-capsule-20260905`, never a repaired or reused root.

## Independent checks performed

The final controller's read-only preflight passed independently: all 12 sealed capture outputs, 6,838 archive/manifest members, 6,050 regular files, 199 exact PAX path records and the required 703 physical ancestor directories were verified. There are no captured symlinks used as physical ancestors of stored members. Archive bytes were read only; there was no extraction or materialization.

For every selected native edge, the reviewer independently checked reachable-requester edge coverage, membership of the chosen target in the audited candidate set, target SHA256, captured raw-link resolution and the first existing regular target in the explicit ordered directories. All 113 system edges / 36 closure targets and 199 Python edges / 94 targets passed. This does not independently prove symbol relocation, actual runtime imports or unrecorded dlopen behavior.

The existing administrative process reports uid/gid0 and the needed SETUID, SETGID, SYS_CHROOT and MKNOD capabilities, with CapEff `0xa80425fb` and existing seccomp mode2. This is permission metadata, not a successful syscall probe. The child code explicitly clears/verifies capabilities after identity drop and sets/verifies no-new-privileges. Any actual kernel or permission failure still stops the run.

Both supplied memory-only self-tests passed. Six additional cases exercised the actual final-log function through in-memory I/O substitution: ordinary rerunfilecheck package lines pass, underfull diagnostics remain visible, and five actual undefined/overflow/duplicate/rerun warning cases fail. Seven cases exercised the final actual child-lifecycle function with completely mocked path/I/O/Popen/signals: success, timeout, KeyboardInterrupt, wait failure, spawn failure, cleanup failure and a deferred SIGINT delivered when the constructor signal mask is restored. The expected status, kill/reap and failure predicates passed in all cases. Two additional fully mocked child-setup tests verified that parent-death SIGKILL is installed after UID drop, the expected parent identity is checked before exec, and the original signal mask is restored only on a successful setup. An already-exited parent fails before publication execution. These mocks did not spawn or signal any process, change a kernel signal mask, create directories or write evidence. The final updated controller preflight and self-test passed again at the hashes above.

The frozen source's exact title/Anonymous identity, final Section8 sentence, 8 sections plus 32 subsections, 18 bibliography keys, letter layout, clearpage boundary and normal public bibliography URLs support the validator's prospective predicates. Archive-only inspection of plainnat and natbib supports bare DOI `\Url` formatting and the starred References heading rather than an additional bibliography bookmark. The reviewer did not rerun mathematical review or pretend these structural checks establish the eventual physical page count.

## Findings resolved before execution

1. Terminal, title and rendered-heading comparison now handles only source-word-local discretionary hyphens at physical line/page breaks. Genuine source hyphens and punctuation stay mandatory; document text is not globally dehyphenated.
2. Rendering documentation distinguishes ordinary acceptance findings from fatal parser/runtime exceptions that may prevent later artifacts.
3. The final log gate no longer mistakes the ordinary rerunfilecheck package name for an actual rerun instruction.
4. Catchable interruptions and wait errors enter kill/reap cleanup before status/snapshot writes. Cleanup errors are retained as failures, never described as proof of a quiescent child.
5. Failure records seal prior evidence on a best-effort basis and explicitly record seal errors.
6. Physical ancestors remain traversable readonly; raw symlinks are installed last using no-follow parent descriptors. The PAX directory trailing slash is checked by exact member kind, not broadly normalized away.
7. A parallel prospective review identified the constructor-interrupt ownership window. The final controller defers SIGINT across Popen construction and handle assignment, restores the mask inside the cleanup-protected scope, and gives the child a post-UID-drop parent-death signal plus expected-parent check. This is bounded local process ownership, not a transactional receipt or an exactly-once guarantee after host failure.

No blocking prospective finding remains at the bound hashes. One nonblocking descriptive over-approximation remains: the loader JSON lists `collections` among top-level validator imports although it is indirect in the final validator. The frozen executable source and fixed role paths control actual behavior.

## Limits and handoff

The reviewer did not access or probe any execution root, invoke captured tools or a PDF parser, create chroots/devices, read live host dependency content, change source/capture files, or perform network/publication operations. Only these new review notes were authored. The administrative Python/bootstrap, kernel and filesystem remain trusted assumptions; the profile is not a network namespace or an arbitrary-malicious-code security proof. Uncatchable termination or repeated interruption during cleanup is not claimed recoverable by this controller.

Execution must preserve every failure without retry, source repair, new dependency capture, host fallback or root reuse. An automated two-root pass still requires all-page visual inspection and independent final integrity review before a local deliverable is accepted. Paper27's existing acceptance and the incomplete Batch07 status remain unchanged.

The `paper-compile` skill was read fully and supplied the log/page/font/visual-check discipline. The user's stricter immutable-source, captured-only, fixed-pass and preserved-failure contract overrides generic cleanup, installation and retry advice.
