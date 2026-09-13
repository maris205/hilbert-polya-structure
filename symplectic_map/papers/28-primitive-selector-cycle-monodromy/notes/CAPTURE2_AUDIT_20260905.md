# Paper28 capture2 independent archive audit

Date: 2026-09-05.

Decision: CAPTURE2_RECORDING_INTEGRITY_PASS

Runtime/build decision: NOT_YET_ESTABLISHED. This is permission to use the identified, audited capture as input to the successor build-profile design/review, not a compiler-start authorization or a hermetic-runtime/PDF/publication PASS.

## Scope and evidence

This independent audit began evidence reads only after the main controller reported actual capture completion with exit 0. It read the exact new evidence directory, its bound administrative code/plan/review/history, and the unchanged source trio. It performed no archive extraction, host dependency content reads or probes, compilation, PDF-tool invocation, network access, source edit, old-root replay, or modification of captured evidence. Its sole persistent write is this note.

The audit checked all 12 preceding output identities declared by `outcome.json`, including all eight census files. Directory membership is exactly those 12 files plus `outcome.json`, with no failure file or extra output. The output root is mode 0700; all 13 regular output files are mode 0600 with one link. The outcome itself is separately bound below; it does not circularly hash itself.

| Artifact in `dependency-capture2-20260905` | Bytes | SHA256 |
| --- | ---: | --- |
| `outcome.json` | 2148 | `8a081a5f7a66fbcdd4d47899c4af1581ac9fba65c25d002609c118fc634b69f2` |
| `intent.json` | 7096 | `7bdf678098597259751c2789a5b2bbac3d23072b847ed3f14711508f9a8b0081` |
| `capsule.tar` | 320194560 | `c1b7f241f2ef7d49de26868b5a23642eb0ddd1271896a72faeea4da97ccc457a` |
| `manifest.json` | 3963641 | `6107892d5f9750e91ae48292a68117d490876b8a3164758dfdc3442e04eebb8d` |
| `events.jsonl` | 5602303 | `6fdb1bc75fa722eae5241c08bca8ef5d5cdd71dde4e26bd598fceb82e475a2da` |

The eight census identities and lengths are transitively bound by the above outcome; each was independently rehashed, not merely accepted from that outcome.

| Administrative binding | Verified SHA256 |
| --- | --- |
| `CAPTURE2_PLAN_20260905.md` | `ae3db611c0caf8be7883800588c72930f93415caa3f6eaa67a19c24174b7292d` |
| `CAPTURE2_20260905.py` | `495672257827582950d10179a746d7c961d1f0c44b6e7cdda1bff7bcc98bec90` |
| `CAPTURE2_REVIEW_20260905.md` | `0e9f1cd8d4c92d71166d327b95239df497dfec0d7b24c0515c860d704555bc58` |
| `DEPENDENCY_CAPTURE_20260905.py` | `7b6731cb725a63beefea1ff3f46588be919e9858183f529dcec61bf66610393f` |
| `CAPTURE_ELF_20260905.py` | `3e68a46b6821e500b2e95358f43c2de8803dd9f7f27669dce49406ecc95a9fa6` |
| `DEPENDENCY_CAPTURE_RESULT_20260905.md` | `8028fcb97e130cd162393388e48bb82ae437e7484505f2ff88cd3e6abeee2e5c` |

Source bindings agree between intent, manifest and actual unchanged source bytes:

| Source | Bytes / LF | SHA256 |
| --- | ---: | --- |
| `main.tex` | 73733 / 1605 | `bdc7a1edc06b3f8cfc75c6b47a8c24180883d24eef878c70d857588d19f1762e` |
| `math_commands.tex` | 444 / 14 | `16b1e55f52f21b63811a0d34eb64eba955533334f8e5f58005841d6da0a85ce5` |
| `references.bib` | 6104 / 204 | `e6a6bdb24a7db3a75b481c8363aa7733cb3dd4c1e8a121d9d9526eb83228882e` |

## Complete archive and receipt checks

All 6838 logical tar members correspond one-to-one with the manifest: 6050 regular files, 646 directories and 142 symbolic links. Every regular member's entire bytes, size, SHA256, LF count and mode match its row. Every directory/link member has the correct type and mode; every raw link target matches. No duplicate, absolute or parent-traversal member name is present. All archive uid/gid/mtime fields are zero and owner names empty, as declared by the controller.

The archive uses the reviewed PAX format. Its 199 PAX `path` extensions exactly reproduce their corresponding logical member paths; no other PAX field is present. An initial diagnostic assertion disallowing all PAX headers was too strict for this already-declared format and was corrected to this exact-path check; neither the capture nor its acceptance requirements were modified.

All 6836 recorded aliases were independently resolved using only manifest link bytes and path operations and agree with their recorded targets. Every captured directory member is represented by a manifest row, recorded alias or explicit omission. Host device/inode/nlink/size/time identities and directory memberships are consistently recorded in the census/metadata evidence; tar does not itself encode original inode/link-count or directory physical-size identities. No claim that it does is made.

The full 27918-line event journal was replayed as data: 8759 census requests, 6838 metadata rows, 213 omissions, eight capacity passes, 6050 read intents and 6050 read completions. Each regular file has exactly one intent and completion, no overlapping/incomplete read, and a matching archive member. Every intent's expected size, prior cumulative read amount and remaining budget agree; every completion's bytes/hash/LF and cumulative amount agree with the manifest and full archive bytes.

Each capacity pass has a complete metadata census of all then-known entries before any read in that wave. Its pending list is exactly the then-unread regular files, not a selected subset. All earlier captured content fields agree with final rows; uncopied files have no prematurely claimed content hash. Pending totals, entry totals, omissions and budget arithmetic agree across the census and event ordering.

| Wave | Pending files | Pending regular bytes | Bytes read before wave | Known entries |
| --- | ---: | ---: | ---: | ---: |
| 000 | 5974 | 245981687 | 0 | 6709 |
| 001 | 46 | 59255672 | 245981687 | 6786 |
| 002 | 14 | 6140688 | 305237359 | 6810 |
| 003 | 11 | 3226024 | 311378047 | 6828 |
| 004 | 3 | 183080 | 314604071 | 6834 |
| 005 | 1 | 89096 | 314787151 | 6836 |
| 006 | 1 | 47472 | 314876247 | 6838 |
| 007 | 0 | 0 | 314923719 | 6838 |

The final accounted resource reads equal archived regular bytes: 314923719, below 2147483648 by 1832559929 bytes. The largest regular file is 35024728 bytes, below the 268435456 per-file cap. Counts remain below 50000 entries and 64 waves. These are verified receipt/controller and archive-consistency statements, not an independent syscall trace or atomic snapshot attestation.

## Required resources and native edges

All 19 required class/package/bibliography-style entries are present as captured regular targets, as are the precompiled format and PDF font map, and all nine requested tool aliases. Tool and resource targets are content-bound by the full manifest. In particular:

- `pdflatex.fmt`: 1503567 bytes, SHA256 `5e3d04e4b504653152b7fbbe415f78de3d353795a3c3d9ceb68e39bb3c0cf8f0`.
- `pdftex.map` resolves to `pdftex_dl14.map`: 4123914 bytes, SHA256 `f2ef4883e12f9f53a33778e8f99cc2006e1434898cbcf493784e3c46f9ed9b18`.
- `pdflatex` resolves to captured `/usr/bin/pdftex`; `bibtex` to captured `/usr/bin/bibtex.original`; configured Python aliases resolve to captured `/root/miniconda3/bin/python3.12`.
- The captured Latin Modern tree contains 92 Type1 files and 596 TFM files. The absent optional `/usr/share/fonts/type1/lmodern` alias tree is therefore not evidence that the declared Latin Modern font family is missing.

An independent in-memory ELF header/dynamic-table decoder, applied to all 165 ELF members during the full archive read, reproduced exactly all 381 recorded dependency edges: nine interpreter edges and 372 DT_NEEDED edges. Every edge has at least one candidate and every recorded candidate is a captured ELF file. There are zero unresolved recorded edges. However, 52 edges have multiple candidates: this is a candidate superset, not a frozen loader winner or proof of ABI/dlopen/import/search closure.

## Explicit omissions and successor-profile constraints

The 213 omissions have exact journal/manifest agreement: 198 missing metadata candidates, eight declared exclusions, five outside-envelope link targets and two excluded search directories. No omission in the 21 required resources or nine requested tool targets prevented capture.

1. Of the missing paths, 195 are individual native-library search candidates; each associated declared native edge has another captured candidate. The other three are optional `/usr/share/fonts/type1/lmodern`, `/usr/share/fonts/truetype/liberation2` and `/var/lib/texmf/web2c/texmf.cnf`. The next profile must explicitly choose its captured TeX configuration and font search roots; it may not silently resolve these through the live host. Captured alternatives include Latin Modern, DejaVu and URW Base35, but that does not authorize a manuscript font substitution.
2. The five unrecorded link targets are `/var/lib/texmf/tex/generic/config/language.dat`, `language.dat.lua`, `language.def`, `/var/lib/texmf/fmtutil.cnf-TEXLIVEDIST` and `/var/lib/texmf/updmap.cfg-TEXLIVEDIST`. Their links are recorded, their targets are not. A candidate profile based on the existing captured `pdflatex.fmt` and map must forbid initex, format/map regeneration and dependence on these missing language/configuration targets. It must not present their presence in a captured lookup database as captured file content or follow their links out to the host.
3. Declared exclusions cover `tex4ht` and the seven listed Python top-level exclusions. The separately admitted `pymupdf` and `fitz` trees were captured despite the general `site-packages` exclusion. The future parser invocation/import closure must be explicitly restricted; this audit did not import those packages or validate their execution.
4. Two Tcl/Tk libraries record a build-time RPATH into `/home/conda/feedstock_root/build_artifacts/tk_1769459871528/_build_env/lib`; this path was excluded, not read. The next profile must not rely on it or claim support for Tk/GUI execution. Candidate-native-edge coverage is not proof that an arbitrary process chooses the intended library.
5. Safe materialization and namespace policy remain necessary. Raw absolute links, fontconfig/kpathsea databases and recorded search configuration can refer beyond the captured subset. A profile must freeze allowed symlink handling, captured-only file/loader/search behavior, environment, writable roots and commands before execution. Generic tar extraction into the host or broad live-host fallback is not endorsed.

No concrete captured-byte, receipt, census or required-baseline-resource integrity discrepancy remains. No recapture is requested by this audit. The next necessary work is the bounded executable successor profile with Paper28-specific validators and explicit disposition of the above limitations. No build, page-count, citation-resolution, anonymous-PDF or final scientific/publication acceptance is inferred here. The first capture failure and all earlier locked history remain failures/preserved records.
