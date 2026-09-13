# Independent Paper28 prospective capture review

Date: 2026-09-05
Reviewer: independent bounded agent `/root/p28_capture_review`
Decision: CAPTURE_PLAN_CODE_PASS

Plan SHA256: b7ce665e8487cb6ff1ca0bde8726e838f2d08f4dd108f0b461af0f895fd51f80
Scanner SHA256: 7b6731cb725a63beefea1ff3f46588be919e9858183f529dcec61bf66610393f
ELF helper SHA256: 3e68a46b6821e500b2e95358f43c2de8803dd9f7f27669dce49406ecc95a9fa6
Intake SHA256: 82a7d955d8777309bd4d210647fe6006ff6c5e5290dbc8719a1d14a9127a5166

## Scope of decision

I read the named plan, scanner, byte-only ELF helper and recovery intake, checked the corrected code, and rebound these exact final identities. E0230 authority and the accepted Paper27 prerequisite are taken from the hash-bound intake; this review does not independently reopen the historical ledger, source review or old failure budget. The decision permits the planned already-authorized one-time resource capture under its existing scope. It is not a dependency-capsule acceptance, successor-build-profile PASS, compiler authorization or Paper28 publication/delivery acceptance.

No capture or system-resource census was performed by this reviewer. No compiler, PDF utility, loader, version command, network client or old/new build namespace was invoked or inspected. The sole reviewer write is this new note. Configured interpreter, standard-library startup and administrative read tools remain the explicitly stated control-plane assumptions.

## Checks and pre-execution corrections

- The resource trees, exclusions, exact aliases, runtime data and candidate-library directories are explicit. Ordinary library directories are never census roots. Out-of-envelope links are recorded without target traversal, and unsupported or missing inputs are disclosed rather than silently added to scope.
- Canonical parent traversal uses descriptor-relative `O_NOFOLLOW` operations for regular reads, directory census, metadata and readlink. Regular bytes are bounded, hashed and archived from the same observation, with descriptor/path identity checks. Evidence creation is exclusive, and evidence hashing is bounded descriptor-relative streaming. These checks do not purport to be an atomic filesystem snapshot or protection against an adversarial kernel/mount administrator.
- Review feedback closed the `/lib64` to `/usr/lib64` alias-envelope gap. Non-leading parent components in raw link targets are now recorded without traversal, preventing incorrect lexical collapse across an unvisited symlink. Raw link targets remain present in the evidence.
- `-I -S -B` is required. In capture mode the helper's bytes are checked against this review before helper execution. The ELF parser is byte-only, rejects unsupported machine/header/string-table forms, and checks x86-64 explicitly. Unknown search tokens, including `$ORIGIN_SUFFIX`, are not silently treated as `$ORIGIN`.
- ELF processing records all admitted candidate matches and unresolved edges; it neither executes a loader nor claims to reproduce arbitrary host search precedence. A malformed or unsupported ELF is disclosed as such.
- The freshness test is one exclusive output-directory creation, not a prior census or reusable-root test. Intent precedes resource capture; the journal, tar and manifest precede the outcome. The outcome seals four prior artifacts, not itself or future records. Failures preserve partial evidence and do not launch an automatic retry.
- Archive member names are canonical root-relative resource identities. Literal symlink records may still contain absolute or escaping targets. This archive is evidence, not a safe-to-blindly-extract installation bundle.

Both permitted final self-tests completed with exit code 0:

1. `/root/miniconda3/bin/python3.12 -I -S -B notes/DEPENDENCY_CAPTURE_20260905.py --self-test` reported `SELF_TEST_PASS`.
2. `/root/miniconda3/bin/python3.12 -I -S -B notes/CAPTURE_ELF_20260905.py --self-test` passed its synthetic in-memory valid/malformed fixtures, including wrong-machine rejection.

These are code/synthetic checks, not an executed resource-capture test or an empirical proof of installed dependency completeness.

## Mandatory subsequent review

After the single capture, independently verify outcome hashes, manifest/journal/archive correspondence, literal links, actual tool/resource coverage, and every relevant omission or unresolved edge before using the bytes. An unused standard-library extension may introduce an irrelevant native edge; its presence is not automatically a build blocker, but actual relevance must be decided against the frozen successor profile. Conversely, a recorded candidate superset is not proof of `dlopen`, font/configuration lookup, Python import or loader closure.

The later profile must pin materialization and namespace/search behavior, runtime/environment/tool/source identities, commands, validators and stage order, and prevent undeclared first reads. Paper28's own page, reference, metadata, annotation/bookmark, warning and visual-output requirements remain unchanged. No capture outcome alone grants compilation or converts an old failure into PASS. There is no additional user-confirmation gate introduced by this review.
