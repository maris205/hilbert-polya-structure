# Paper 22 Final Integrity Review

Date: 2026-08-24 UTC

Project: `papers/22-hamiltonian-cubic-spectral-collapse`

Public title: **Cubic Spectral Collapse for Endpoint-Spiked Hamiltonian Product Shears: Sharp Selector Thresholds in Arbitrary Mode Number**

## Independent role and disposition

This is the sole fresh terminal-integrity review. The reviewer is distinct
from the finalization-governance author, replacement finalization reviewer,
release-candidate author, terminal-build evidence author, and every earlier
source, proof, build, and review role. The reviewer authored none of `Q51`.
All project, ledger, JSON, temporary-evidence, build-root, source,
bibliography, PDF, visual, security, anonymity, governance, permission, and
external-effect checks passed before cleanup began. Cleanup then passed, the
complete project was rehashed with zero byte drift, and this file was the
sole project file written by this role.

The opening root-ledger fences were exact:

| Ledger | SHA-256 | Bytes | LF | Required live state |
|---|---|---:|---:|---|
| `BATCH_06_STATUS.md` | `d1c9695b93d56ec96c0b649a0e7127a5d5ff8ae0655d68f0d2af986ee33f5d21` | 47,198 | 717 | gate `PAPER22_TERMINAL_INTEGRITY_REVIEW_OPEN`; Paper 22 queue `TERMINAL_REBUILD_PASS_PENDING_INDEPENDENT_ROOT_AUDIT` |
| `BATCH_06_IDEA_REPORT.md` | `debb35ebdce2ea7f41cacf2ae42b10e1da83af6d7faee28135c79d691561cfd0` | 58,498 | 1,118 | append-only through the terminal rebuild receipt PASS addendum |

Both identities remained exact after governed cleanup and immediately before
this review was written.

## Exact project and governance audit

A no-follow traversal found exact `Q51`: 51 regular non-symlink files; the
four directories `experiments`, `notes`, `paper`, and `refine-logs`; zero
symlinks; and zero other entry types. Every path was safe and unique. Every
file was opened no-follow and rehashed for SHA-256, bytes, LF count, inode,
mode, owner, and link count. The independently framed 51-file universe had
SHA-256
`6cd461383ddbd56bb0d4a185bb94f0c465b7313dccf972596109d5b18a6fcc42`,
5,385 bytes, and 51 LF. It was identical before and after cleanup.

The recovered finalization chain was exact:

| Artifact | SHA-256 | Bytes | LF | Required state |
|---|---|---:|---:|---|
| `notes/FINALIZATION_STAGE_SCOPE.md` | `09462316380cf1c958aaf06c6a1d0e3a93ba7fcb8060e177420fafff22de268f` | 27,385 | 447 | `FINALIZATION GOVERNANCE SCOPE AUTHOR STOP` |
| `experiments/finalization_lock.json` | `6df9730752823fce76571ff690aab3c6213038d80ae9ba6e94e4f3c7de3d3e33` | 102,689 | 1 | schema `paper22-finalization-lock-v1`; state/status `FINALIZATION_STAGE_LOCKED_PENDING_INDEPENDENT_FINALIZATION_REVIEW` |
| `notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md` | `51513435a9b518f5463bf3e04beeda65583a7fbc8af02a7cab66231542b4deab` | 13,047 | 249 | `FINALIZATION_STAGE_PASS` |
| `paper/FINAL_RELEASE_MANIFEST.json` | `423750e3484e445c667f8ebb13d6858cef3c5a1f6eeded485e879ea7ba5b2266` | 27,463 | 1 | schema `paper22-final-release-manifest-v1`; local-candidate pending status |
| `paper/TERMINAL_REBUILD_RECEIPT.json` | `e26bed197b414ede96a02810cbb71fc26e60660590f353f09ea0d110c06a9e89` | 37,051 | 1 | schema `paper22-terminal-rebuild-receipt-v1`; status `TERMINAL_REBUILD_PASS_PENDING_INDEPENDENT_ROOT_AUDIT` |

The lock's `F45` bindings passed 45/45, including its 4,719-byte, 45-LF
framing hash
`7d28756acc975090708d582130fb2f69ca4d07ac8b61e60ed906da67254173dc`.
The manifest bound all 49 completed non-self `R50` files. The receipt bound
all 50 `R50` files, including the manifest, and excluded only its own
self-referential identity. The 23-record authoritative chain passed in its
corrected order: `PAPER_PLAN_PASS` precedes publication scope, and the
historical initial build incident still ends exactly `R0_BLOCKED` and is not
a pass. The recovered scope/lock, superseded identities, failed review's
`WRITE_NOTHING` disposition, temporal ledger fences, stage arithmetic
`F45 -> G47 -> P48 -> R50 -> Q51 -> T52`, and five-role separation were
internally consistent.

All ten project JSON files passed a duplicate-aware Python strict UTF-8
decode and recursive canonical re-encode. A genuinely independent
handwritten Node tokenizer, parser, duplicate detector, Unicode code-point
key sorter, and encoder—without `JSON.parse` or `JSON.stringify`—also
reproduced every file byte for byte. Both implementations enforced one
terminal LF, compact separators, recursive key order, no duplicate keys,
nonfinite numbers, BOM, CR, NUL, whitespace drift, or trailing content. The
Node implementation rejected 10/10 adversarial documents. For the
finalization lock it independently counted 394 object nodes, 3,730 object
members, 70 arrays, 555 array values, and 3,822 scalars. All schemas,
statuses, and null self-hash/byte exclusions passed.

## Source, theorem, and bibliography fidelity

The terminal source remained exactly:

| Source | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/main.tex` | `926c6fd083ee532b6ca5dde1a366e6c2cb93d0bfec855ac38944bcbac7fcc0a1` | 69,241 | 1,921 |
| `paper/math_commands.tex` | `544a046194ef6b0326609b79275f5f04595519354b11a9fb0a91356cacdb612c` | 330 | 11 |
| `paper/references.bib` | `50f8ed9f1f415bc53a32c39a437b35fb1a4cff066efb44e681804e293dd6a53d` | 1,928 | 55 |

Source, extracted PDF text, outlines, and fresh renders retained all 17 locked
theorem features: characteristic zero; `r >= 4`; `g >= 2r+1`; `h=g-1`;
`m=r-2`; the fixed word `F=T` after `S`; `C=BA`; the exact endpoint row
replacements of `M=2 11^T-I`; the sufficient cone and both strict selectors;
the exact phase recurrences; domain-based leading-form survival without
coefficient positivity; strict last-coordinate visibility for `n>=1` with
the tied `n=0` case separate; the exact degree and Perron identities; the
`(r-3)`-dimensional semisimple unit sector and three-dimensional equal-middle
restriction; the displayed `Q_(m,h)` and exact cubic factor; exact algebraic
and geometric unit multiplicity `r-3`; the scalar recurrence and its initial
values; the `g=2r` seed/selected-face boundary; formal `r=3` consistency
only; and four arbitrary nonzero coefficients on the fixed supports.

All six anti-claim fences remained explicit. The cone is sufficient and is
not claimed maximal, necessary, unique, exact, or classificatory. The cubic
is an annihilator and is not uniformly claimed minimal, irreducible, or an
algebraic-degree-three theorem. The boundary is not a global failure or
classification theorem. Formal `r=3` substitution proves no `r=3` theorem.
No arbitrary-Hamiltonian, positive-characteristic, topological, metric,
arithmetic, entropy, or hyperbolicity conclusion is asserted.

The bibliography contained exactly six unique entries. The source retained
exactly four citation commands and the six keys `BlancVanSanten2021`,
`ShaoSun2025`, `Deserti2016`, `DangFavre2021`, `Rangarajan2002`, and
`FujiokaKogawaLiShudo2023`. AUX, BBL, BLG, OUT, source labels/references,
six bibcites/bibitems, and 36 bookmarks closed with no missing citation or
reference. Citations remained contextual and transferred no proof of the new
claims.

## Deterministic terminal-build and PDF audit

Before cleanup, the two terminal roots were exact ordinary root-owned
mode-0700 directories:

- `/tmp/paper22-terminal-A.nFqXVO`
- `/tmp/paper22-terminal-B.Vio934`

Each had exactly 13 ordinary link-count-one files: the source trio, four
command logs, and six outputs. The recorded environment contained exactly
`PATH=/usr/bin:/bin`, `SOURCE_DATE_EPOCH=1787529600`,
`FORCE_SOURCE_DATE=1`, `TZ=UTC`, `LC_ALL=C`, and `LANG=C`. Each root ran
exactly `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` with the locked
arguments and exit vector `0,0,0,0`; there was no retry, fifth pass,
`latexmk`, shell escape, source edit, project overwrite, or network action.
The live `/usr/bin/pdflatex` and `/usr/bin/bibtex` resolved-tool identities
matched the receipt.

All 13 entries agreed byte for byte across terminal A/B and the accepted
R0-repair A/B and R1-no-op A/B comparators. The accepted command-log hashes
were `1775b04c...fc5fe41`, `7b0a0a8d...72044dc9`,
`7418c3d6...44b2f9b7`, and `0de73741...d4c198c6`. The accepted AUX, BBL,
BLG, LOG, OUT, and PDF hashes were respectively `22a3bcd3...e5bcfb2`,
`13faf550...1c28c3aa`, `91128590...ef15f92`,
`3f8a5951...b5924cb0`, `c732b3dd...e172093a`, and
`53168434...9e488a7`. Final command four and `main.log` had zero fatal,
LaTeX/package warning, undefined citation/reference, rerun/changed, and
overfull events, with only the exact three nonblocking underfull boxes at
source line 944 and badness `6316,10000,6316`.

Terminal A, terminal B, current, round-zero, round-one, and release-candidate
PDFs were six-way byte-identical at SHA-256
`5316843486e1cdf68e9193bf6ad5efe3820543135e27ca6ee64d3a9579e488a7`,
471,647 bytes and 2,649 LF. Independent Poppler, Ghostscript, and PyMuPDF
checks found PDF 1.5; 26 unrotated US-Letter pages; all 130 page boxes exact;
26 nonempty text pages; zero out-of-page word boxes; 28 fonts all embedded,
subsetted, and Unicode mapped; zero images, attachments, embedded files,
forms, widgets, signatures, JavaScript, encryption, dangerous actions, or
external file specifications. The only actions were 111 ordinary internal
links, eight ordinary URI actions to six bibliography destinations, and the
ordinary page-one GoTo open action. There were 36 outlines and no appendix.

The visible author was exactly `Anonymous` once. The title metadata matched
the public title. Author, Creator, Producer, Subject, and Keywords were empty;
CreationDate and ModDate were exactly `D:20260824000000Z`. Source, AUX, BBL,
BLG, OUT, final log, extracted text, metadata, outlines, object dictionaries,
and renders contained no unresolved placeholder, private path, governance
token, known digest, agent identity, email, or provenance marker.

## Fresh visual review

The reviewer created only `/tmp/tir22-audit.obbMI1`, an independently named
root-owned mode-0700 scratch whose basename did not begin `paper22`. It
rendered all 26 pages, assembled and inspected seven contact sheets covering
pages 1--4, 5--8, 9--12, 13--16, 17--20, 21--24, and 25--26, and separately
rendered and inspected pages 1, 8, 13, 22, 24, and 26 at higher detail.
Every page was upright, complete, readable, and internally consistent. No
clipping, overlap, blank or duplicated page, missing glyph, malformed
formula/table, broken heading, displaced footline, identity leak, or visual
provenance marker was found. The title/author/abstract, selector cone,
invariance ledger, exact unit multiplicity, boundary and anti-claim wording,
Limitations, Conclusion, and all six references were directly inspected.

The scratch contained exactly 43 regular files and five directories,
10,876,463 regular-file bytes, zero links, and zero special entries. Before
governed evidence cleanup, the reviewer unlinked exactly those 43 scratch
files individually and removed exactly those five scratch directories. The
scratch path was confirmed absent.

Four initial read-only harness expectations were corrected without changing
any artifact or repeating a build: hyperref's UTF-16 octal bookmark encoding
was checked as encoded; PyMuPDF's integer-valued `needs_pass` false state was
handled semantically; its local named-link representation was reconciled
with the underlying ordinary GoTo dictionaries; and known-hash scanning was
expanded from unique R50 values to all governance JSON digests. These were
review-tool assertions only and produced no project or governed-evidence
change.

## Governed evidence cleanup and post-cleanup integrity

Immediately before cleanup, `/tmp` contained exactly the following 12
authorized targets and no other top-level basename beginning `paper22`:

- `/tmp/paper22-prebuild28-manifest.txt`
- `/tmp/paper22-r0-A.PIwA2V`
- `/tmp/paper22-r0-B.xwtGZQ`
- `/tmp/paper22-r0-postbuild37-manifest.txt`
- `/tmp/paper22-r0-repair-A.0zGVu9`
- `/tmp/paper22-r0-repair-B.FwYPpz`
- `/tmp/paper22-r0-repair-validation.Y4OsGc`
- `/tmp/paper22-r1-noop-A.JMXTHF`
- `/tmp/paper22-r1-noop-B.lEctAm`
- `/tmp/paper22-r1-review.Nb23X3`
- `/tmp/paper22-terminal-A.nFqXVO`
- `/tmp/paper22-terminal-B.Vio934`

The legacy lock and terminal receipt matched every literal/relative path,
type, mode, UID/GID, device, inode, link count, stat size, SHA-256, byte
count, and LF count. The complete live inventory was exactly 244 nodes:
227 regular files, 17 directories, 73,298,199 regular-file bytes, zero
symlinks, zero special entries, zero unlisted descendants, and 227 unique
regular-file device/inode pairs with link count one. All 16 must-remain-absent
assertions were absent and were never cleanup targets.

Only after every preceding audit passed, the reviewer exercised the recovered
bounded authority. It opened exact directories no-follow, revalidated exact
entries, unlinked the 227 enumerated regular files individually, and removed
the 17 exact empty directories deepest-first with `rmdir`. It used no
recursive deletion command, `rm -r`, `rm -rf`, glob, wildcard, unresolved
shell variable, command substitution, prefix deletion, symlink traversal,
special-file deletion, or deletion-by-discovery. All 12 targets are now
absent, every one of the 16 absence assertions remains absent, and no
top-level basename beginning `paper22` remains in `/tmp`.

This cleanup intentionally removed only temporary build/review evidence. The
removed paths are not recoverable by ordinary filesystem path after unlink
and `rmdir`; retained project artifacts, manifests, receipts, source, PDFs,
and ledgers preserve their governed identities. Cleanup changed zero project
bytes: the exact Q51 framing hash and both root-ledger identities remained
unchanged afterward.

## Terminal state

Creating `paper/reviews` and this sole review advances the project to exact
`T52`: 52 regular files, five directories, zero symlinks, and zero other
entry types. The local release candidate is confirmed only within the
`LOCAL_ANONYMOUS_RELEASE_ONLY` boundary. Submission, upload, public hosting,
repository push, network transport, external messaging, identity disclosure,
and every other external effect remain false and unauthorized. This review
does not unlock or perform any external release action.

FINAL_INTEGRITY_PASS
RELEASE_CONFIRMED
