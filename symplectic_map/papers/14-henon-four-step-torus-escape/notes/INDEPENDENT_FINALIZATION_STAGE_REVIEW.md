# Independent Finalization-Stage Review

Review date: 2026-08-17 UTC

Canonical project root: `/root/autodl-tmp/symplectic_map/papers/14-henon-four-step-torus-escape`

## Independence, scope, and method

I performed this review after the finalization-governance author stopped. I did not author or modify any frozen input, either governance artifact, any build artifact, any prior review, or any future release or terminal artifact. Before reaching a decision I made no project write, created no project or temporary build file, invoked no compiler, accessed no network, performed no rasterization or image conversion, and did not create `paper/main.pdf`, `paper/FINAL_RELEASE_MANIFEST.json`, `paper/reviews`, or `paper/reviews/final_integrity_review.md`. Within the project, I read only the exact G31 allowlist. This file is my sole authorized project write.

The review independently checked the exact inventory and identities, strict JSON canonicalization, the complete provenance DAG, source-revision exhaustion, manuscript and evidence locks, both persisted builds, all later path-set equations and role universes, the release-author contract, the terminal two-build protocol, cleanup, the local-only firewall, and terminal immutability. Two read-only cross-checks separately replayed the canonical/DAG and set/role/terminal portions; I retained sole responsibility for the decision.

## Bound G31 input universe

Immediately before this review was written, the canonical root contained exactly 31 regular files, four directories (`experiments`, `notes`, `paper`, and `refine-logs`), zero symbolic links, and no other filesystem object. All 31 files had distinct device/inode identities and link count one. The five pre-review future paths were absent by `lstat`. Each row below was recomputed from bytes at the canonical path; the rows are path-sorted and collectively equal G31.

| ID | Path | Bytes | SHA-256 |
|---|---|---:|---|
| G01 | `experiments/EXPERIMENT_PLAN.md` | 5522 | `709b32fa83e7cf1502e57393e4b46daf33c83ccb88832a498e223d084eabbd95` |
| G02 | `experiments/EXPERIMENT_TRACKER.md` | 2139 | `da117759e1e6a95579fcae16f27c3c868bd67b6d0b8b5d98e936b456a9354a97` |
| G03 | `experiments/finalization_lock.json` | 40003 | `c54790607bad9c0ee26d0b701a0a83c565f147623fbac7619d823fa4539e4f3a` |
| G04 | `experiments/publication_lock.json` | 23141 | `b8719f81f32fd33a54d419cf89d7165a871c19e6751e1b5287d613dbf708dc18` |
| G05 | `experiments/source_lock.json` | 10716 | `f2077d20262f6a068da58a2227c405573dd34fa8b844461b3d057da94e9eaa0c` |
| G06 | `notes/CITATION_VERIFICATION.md` | 12919 | `0c9b08f566eedb1e9f344f6fb07dfcf0c87015daa566435d0c989ac722d4e2af` |
| G07 | `notes/CLAIMS_EVIDENCE_MATRIX.md` | 5902 | `d1887968e8626c1a8e30c9cb1675a13277c76662ca0fee8834ea024123650f6e` |
| G08 | `notes/FINALIZATION_STAGE_SCOPE.md` | 24662 | `21b4d8c89715b9024d318eb7b44152b2dfa2df58327f8159fef26cab6e41879c` |
| G09 | `notes/INDEPENDENT_CITATION_PRECISION_AUDIT.md` | 21470 | `7e625c593267545088320459b65e990fdea5e347ed779416a6ce334d5a131f17` |
| G10 | `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md` | 18211 | `f24d481c9ad58d606f1da250198892058c5683245cbef64d221c49541e7e91f5` |
| G11 | `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md` | 24046 | `03499cc92c6a5a6b7010f75ba5fd879082dcd4abb61709722fab081bc709fe1b` |
| G12 | `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | 7992 | `0d1bbb1104e2f709312e1cfe0b3c449eb3bd706654c58f87eaf5b621a3ea5596` |
| G13 | `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | 14371 | `81444cb4d89c4797352b3f4558f4d64dacf4cb733ee6014be5b0e9335243b0d4` |
| G14 | `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 18618 | `e3dc9864c72d150e0f7a69d08aad9f4e24f0dde1c6115fe3d428b129ade4573c` |
| G15 | `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW_R2.md` | 12836 | `8bde838d4bd18426f291eb793f5c822fbd6d70d604fc7097c5761c02bb309ef0` |
| G16 | `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | 12934 | `ea6d13c1ec74bbad0ac8c6cd850d0f0b8c33992d05b5e428308eef3347a18308` |
| G17 | `notes/NOVELTY_ASSESSMENT.md` | 8660 | `2fafbef234a7e7cc8fbe10b25e0b920188b3c35472538fcbaf023da8d357bac1` |
| G18 | `notes/PROOF_PACKAGE.md` | 13728 | `c43d8377707e0ee69aa6447984b77c2b5ef6d1d79bc1d56c6b5ab72ea4c8f5aa` |
| G19 | `notes/PUBLICATION_STAGE_SCOPE.md` | 23830 | `156dff2466f42704fd6f1e65f6374d21a097adb98632d7a5125984caceb9d447` |
| G20 | `notes/RESEARCH_QUESTION.md` | 6371 | `782b48dfec973d877bf87c964a3bdd7227b52a21101b68a9a576929441bedb9c` |
| G21 | `paper/BUILD_RECEIPT_R0.json` | 21053 | `b377031ee9961dd506322d6bd721e0832663b4da44ac56c028bff403b8dbb529` |
| G22 | `paper/BUILD_RECEIPT_R1.json` | 28315 | `37baf7a8e49e4b45c4ba41d19b62c9cfb2656d83a022114f63595b115daaae6e` |
| G23 | `paper/PAPER_PLAN.md` | 30112 | `6a0e16e3688714c43c9e9d87054c501d44989e59a523c6ff084eac4c9db3a88f` |
| G24 | `paper/SOURCE_REVISION_RECEIPT_R1.json` | 11437 | `0f8a9d0e9ca9aa7bb13b63016ab14148fd6a29c2a086d532c539e876abd9de1c` |
| G25 | `paper/main.tex` | 47961 | `415f1395f07153ccb158e69cb70051e95e719802d0a1c3315df88be7ccfab538` |
| G26 | `paper/main_round0.pdf` | 384084 | `4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414` |
| G27 | `paper/main_round1.pdf` | 384084 | `4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414` |
| G28 | `paper/references.bib` | 2666 | `816fd8211b7c5ad91dc227ac71b90444cdf5c3b713b60dd9a70fbdd1a8d419bc` |
| G29 | `refine-logs/FINAL_PROPOSAL.md` | 7814 | `719214a159f1e36676d059c626dcefab7fe11b012e44146243db8aa500eb38a0` |
| G30 | `refine-logs/INITIAL_PROPOSAL.md` | 4045 | `ecb3a5151c75dba6ac4b8415d000f9a9a3c36ff80af5b651b9de7ecbad7a6e22` |
| G31 | `refine-logs/REVIEW_SUMMARY.md` | 6383 | `ac2a75bb0f393de1255958705bbcd2e75fa1e0800805d420f048cb0f72c5d54f` |

The scope artifact also had exactly 502 LF bytes. The governance lock had exactly one LF byte. Its 29 `input_bindings` equal the scope's F01--F29 table and the observed frozen files. Its scope binding equals G08, while its self record correctly omits self bytes and self hash.

## Canonicalization and provenance audit

All six JSON artifacts in G31 are strict UTF-8, compact canonical JSON followed by exactly one LF byte. Fresh strict parsing rejected duplicate object names and the nonfinite tokens `NaN`, `Infinity`, and `-Infinity`; recursive object keys are ordered lexicographically by Unicode code point. Canonical reserialization reproduced every file byte for byte. All self-exclusions and all nested path identities were coherent: 143 nested G31 identity records yielded zero byte/hash mismatch and zero cross-record conflict.

The frozen provenance graph has 12 ordered edges, 13 roots, and 16 unique outputs. Every input precedes its consuming edge, every output is new at that edge, and roots plus outputs equal F29 exactly. The historical regular-file prefixes replay as 14, 15, 16, 17, 19, 20, 22, 24, 25, 26, 28, and 29. The source-design, source-lock, paper-plan, publication-stage, anonymous drafting, Round-0 build, Round-1 review, bounded no-op revision, Round-1 build, and Round-2 review read/write sets all match their recorded edges.

The five independent gate reports end in their required positive lines: `SOURCE_LOCK_PASS`, `PAPER_PLAN_PASS`, `PUBLICATION_STAGE_PASS`, `MANUSCRIPT_R1_PASS`, and `MANUSCRIPT_R2_PASS`. The current Round-2 report is exactly 24,046 bytes with SHA-256 `03499cc92c6a5a6b7010f75ba5fd879082dcd4abb61709722fab081bc709fe1b`; it records no blocker and no required repair. The bounded revision receipt records `change_count = 0`, empty changes and mappings, and identical pre-, post-, and current identities for both sources. Its sole 1/1 revision window is consumed and no later source or bibliography revision is authorized.

## Manuscript, evidence, and build findings

The theorem package, plan, manuscript, and two manuscript reviews agree on the exact four-step Henon-map composition and the arithmetic escape result. The cited Evertse--Schlickewei--Schmidt input is confined to the stated lattice/coset fact; the rank-`3r` fixed-coefficient family, the full `A`, `B`, `C`, `BA`, `CB`, and `CBA` case split, the `T4`/`T3` semantics, sharpness discussion, and whole-periodic-orbit corollary remain aligned. Citation locators, theorem labels, limitations, negative/zero-evidence statements, and the claims-evidence matrix are mutually consistent. The paper does not turn bounded checks into empirical or external validation, and it preserves the anonymous-author and exact safe-title constraints.

The Round-0 and Round-1 receipts each bind two isolated clean runs with the exact two source files and four-command sequence. All eight recorded process exits are zero. The fixed environment is `FORCE_SOURCE_DATE=1`, `LANG=C`, `LC_ALL=C`, `SOURCE_DATE_EPOCH=1786838400`, and `TZ=UTC`. The commands use absolute `/usr/bin/pdflatex` and `/usr/bin/bibtex`, include `-no-shell-escape`, and match the locked order. The recorded resolved executables, sizes, SHA-256 identities, and version-stdout identities agree across Round 0, Round 1, and the finalization lock.

Every recorded build transcript, command-result map, artifact map, and BBL identity agrees across all four clean runs. The BBL identity is 1,710 bytes and SHA-256 `2102f0d5077f0946d97a93e09c824ee42725161b1d000c76f9adc53331094f92`. The two persisted PDFs compare byte for byte and share the locked identity of 384,084 bytes and SHA-256 `4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414`.

Read-only stdout inspection of the persisted PDFs found 17 letter-size pages, mathematical content through page 17, references beginning on page 17, exact title/subject/empty-author metadata, no custom metadata stream, no forms, JavaScript, attachments, signatures, images, or external payload, and 21 fonts all embedded, subset, and Unicode mapped. There are no undefined citations or references and no unclassified build warning. The only accepted findings remain the two frozen cosmetic items `P14-R1-COS-001` and `P14-R1-COS-002`.

## Closed later-stage sets and roles

The five regular-file sets are path-sorted, duplicate-free, path-safe, and satisfy these exact equations:

- F29 has 29 files.
- G31 equals F29 plus the two finalization-governance artifacts and has 31 files.
- P32 equals G31 plus this independent review and has 32 files.
- R34 equals P32 plus `paper/main.pdf` and `paper/FINAL_RELEASE_MANIFEST.json` and has 34 files.
- T35 equals R34 plus `paper/reviews/final_integrity_review.md` and has 35 files.

The governance author reads F29 and writes exactly two governance files; this reviewer reads G31 and writes exactly this one file; the release-manifest author reads P32 and writes exactly two release files; the terminal reviewer reads R34 and writes exactly one review file. Each role's read and write universes are disjoint and equal the corresponding set transition. Activation strings are chained to the prior stable author stop. No role may expand its own universe, review its own output, self-sign, inherit an earlier write authority, or bypass the next independent gate.

## Release-author contract

This decision activates only the bounded release-manifest author. That role may not compile. It must copy `paper/main_round1.pdf` byte for byte to `paper/main.pdf`, compare the result against both persisted PDFs, and verify the locked PDF size and SHA-256 without rewriting metadata or content. It must then write exactly one strict canonical `paper/FINAL_RELEASE_MANIFEST.json` after the PDF, binding the sorted P32 set plus `paper/main.pdf`: 33 non-self records. Manifest self bytes and self hash remain excluded; duplicate keys and nonfinite values are forbidden; recursive Unicode-code-point key ordering, compact serialization, and exactly one final LF are required.

The manifest's effect remains false and its state remains `LOCAL_ANONYMOUS_RELEASE_CANDIDATE_PENDING_FINAL_INTEGRITY_REVIEW`. The release-author step cannot submit, upload, communicate with a venue, disclose identity, access a network, push a repository, host publicly, or perform any other external action.

## Terminal-integrity contract

Only after a stable exact R34 stop may a fresh terminal reviewer act. Its sole project write is `paper/reviews/final_integrity_review.md`; creation of `paper/reviews` is authorized only as the parent directory for that file and is not an additional artifact. Before writing, the reviewer must observe exactly 34 regular files and zero symlinks.

The terminal reviewer must create exactly two distinct, initially empty, real nonsymlink roots matching `/tmp/p14-paper14-final-XXXXXXXX`, with eight ASCII-alphanumeric suffix characters; a third root is forbidden. Each root initially receives exact-byte copies only of `paper/main.tex` and `paper/references.bib`. Each build uses the locked five-variable environment and this exact sequence:

1. `/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex`
2. `/usr/bin/bibtex main`
3. `/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex`
4. `/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex`

The only permitted temporary names are `main.aux`, `main.bbl`, `main.blg`, `main.log`, `main.out`, `main.pdf`, `main.tex`, `main.toc`, and `references.bib`. Both source pairs, both BBLs, both new PDFs, both persisted PDFs, and `paper/main.pdf` must satisfy their respective locked byte identities; in particular the five PDFs must be byte-identical. All eight process exits must be zero. PDF inspection is stdout-only and read-only: no screenshot, extraction, conversion, rasterization, image write, package installation, or network access is authorized.

Cleanup must revalidate each resolved root, reject any unlisted entry, follow no symlink, delete only the nine explicitly listed regular files in the locked order, use no wildcard or recursive deletion and no unresolved variable or command-substitution target, remove each empty root by nonrecursive `rmdir`, and confirm both roots absent. On exact success, the terminal review is the sole project write, the postwrite inventory is exactly 35 regular files and zero symlinks, and its last two nonempty lines are `FINAL_INTEGRITY_PASS` and `RELEASE_CONFIRMED`. Any failed gate leaves effect false and forbids both pass lines.

Even terminal success has only the effect `LOCAL_ANONYMOUS_RELEASE_ONLY`. It authorizes no later build, source or bibliography revision, finalization, manifest rewrite, terminal-review rewrite, release expansion, camera-ready change, submission, upload, public release, identity disclosure, or external communication. The project is terminally immutable after that exact local gate.

## Findings and decision

Blocking findings: none.

Required repairs: none.

The observed G31 state satisfies every finalization-review gate. This decision does not itself create a release, produce a release manifest, copy a PDF, compile, submit, upload, disclose identity, or authorize any action outside the next bounded local role.

FINALIZATION_STAGE_PASS
