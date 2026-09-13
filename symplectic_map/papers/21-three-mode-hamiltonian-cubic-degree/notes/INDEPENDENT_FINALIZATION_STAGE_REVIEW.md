# Independent Finalization-Stage Review — Paper 21

Date: 2026-08-22 UTC

Verdict: PASS.

## Independence, read universe, and zero external effect

I acted as the fresh replacement independent finalization reviewer. I am
distinct from the finalization-governance author, authored none of the 51
frozen inputs, and authored neither governance artifact. I read exactly the
recovered `G53` project universe. I did not read or inspect any temporary build
root, because root inspection belongs only to the later sole terminal-integrity
reviewer. I did not compile, invoke LaTeX or BibTeX, copy or transform a PDF,
create a release candidate, manifest, terminal receipt, or review directory,
edit any existing project file, access a network, run CAS/numerical/scientific
work, or cause any external effect. This note is my sole project write.

## Re-enumeration, identities, and strict JSON

Two complete readbacks, separated by the substantive audit, found exactly 53
regular non-symlink files and exactly four directories (`experiments`,
`notes`, `paper`, and `refine-logs`), with zero symlinks and zero other entry
types. All names are unique, safe project-relative POSIX paths in byte order.
The 51 `F51` bindings rehash 51/51 with their declared SHA-256, byte count, and
LF count, and the 51 rows independently parsed from the scope table equal the
lock bindings entry for entry.

The recovered governance pair is exactly:

| Artifact | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `notes/FINALIZATION_STAGE_SCOPE.md` | 16,353 | 243 | `1c2b5e6dfe0a355ad839bf3a3b303c3f0258372f0f1c677b440478899f49d01a` |
| `experiments/finalization_lock.json` | 14,767 | 1 | `f8a71bdcddb77c19618c02b61c2a503d46d6a719de60c9bf467c57af98be17ab` |

As an independent diagnostic, framing all 53 byte-sorted paths as
`uint64_be(name length) || name || uint64_be(content length) || content`
gives 1,762,941 framed bytes and SHA-256
`33d37ac1fe0c8b41f5e5d51e0dfd478d6c3b5fa51a47573074ecfbf0636b29d2`.
The underlying files total 1,760,387 bytes and 13,928 LF bytes. The second
complete readback reproduced these values exactly.

All eight JSON files in `G53` strictly decode and reproduce their bytes under
recursive Unicode key order, compact separators, UTF-8, and exactly one
terminal LF. Each is BOM-, CR-, and NUL-free. A duplicate-key probe and
separate `NaN`, `Infinity`, and `-Infinity` probes were all rejected. The
finalization lock safely records its own path while excluding its own digest
and byte count; its scope binding resolves to the exact scope identity above.

The first future review path, candidate, manifest, terminal receipt, and
`paper/reviews` directory were all absent at both readbacks. Thus the live
universe is exactly `G53`, not an inferred or prematurely advanced stage.

## Governance recovery and authoritative lineage

The recovery record is complete and internally consistent. The superseded
scope was 15,341 bytes/225 LF at
`2372c94ac7d0089eaed47f86fb4f2005b3cf4206f800f5ebe0cf89c41f06815a`;
the superseded lock was 14,169 bytes/1 LF at
`7f5473d849dcf7179432395dd32be257b43942ca0d4aca7661686bf8add8682e`.
The first review attempt records 72 passing checks, found one false lock-only
terminal value, and wrote no project file. The still-absent review path
confirms its zero-write disposition.

The sole recorded semantic correction changes the terminal assigned to
`notes/BUILD_R0_BLOCKER.md` from `BUILD_R0_BLOCKED` to `R0_BLOCKED`. Direct
readback of that bound file gives status `R0_BLOCKED` and, after removing its
outer Markdown code ticks, final nonempty line `R0_BLOCKED`. Every `F51` byte
still matches its frozen binding. The recovery changes no source,
bibliography, PDF, receipt, metadata, review, theorem, stage path, role fence,
cleanup rule, or external-effect rule. The superseded governance pair and the
failed review attempt grant no authority.

The lock's 15-entry authoritative chain agrees with the live artifacts. All
asserted Markdown terminals were normalized and checked, and all asserted JSON
statuses were strictly parsed and checked:

- source-lock and publication-lock reviews end `SOURCE_LOCK_PASS` and
  `PUBLICATION_LOCK_PASS`;
- the current repair-source reviews end
  `PAPER_SOURCE_R1_R0_REPAIR_PASS` and
  `PAPER_SOURCE_R2_R0_REPAIR_PASS`;
- the historical first build is `R0_BLOCKED`, while the proof-first repair
  ledger remains a ledger rather than a build pass;
- the canonical R0 receipt has status `BUILD_R0_REPAIR_PASS`; the first build
  review ends `BUILD_R1_R0_REPAIR_BLOCK`; the repair ledger ends
  `BUILD_RECEIPT_R0_CANONICAL_REPAIR`; and its replacement review ends
  `BUILD_R1_R0_REPAIR_REPLACEMENT_PASS`;
- the no-op revision receipt has status `R1_NO_OP_REVISION_PASS`, the R1 build
  receipt has status `BUILD_R1_NO_OP_PASS`, and the fresh R2 review ends
  `BUILD_R2_R1_PASS`.

The frozen source trio remains `paper/main.tex` at
`34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2`,
`paper/math_commands.tex` at
`05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a`,
and `paper/references.bib` at
`4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8`.
The three persisted PDFs are byte-identical, each 465,922 bytes/2,539 LF at
`b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3`.

I reconstructed the superseded noncanonical R0 receipt entirely in memory by
moving only `underfull_hbox_count` ahead of the two `undefined_*` keys. The
result is exactly 7,339 bytes at
`48e61f31636c3e70f26da61b74fa9655c22a3ac954b9ae56b877cdebedcd5537`,
and its decoded JSON value equals the current receipt. This independently
confirms a serialization-order-only repair. The no-op receipt has an empty
changed-path list, zero required and cosmetic findings, equal before/after
source arrays, and one consumed revision window with zero remaining.

The five source-review artifacts classified as historical non-authority bind
only the superseded `74434cdc...` or `c3d34411...` source, or the intermediate
`910086eb...` source produced during the failed-independence worker interval.
Their PASS-looking final lines do not override the explicit non-authority
classification. Likewise, the first build R1 review remains an authoritative
incident blocker, not a build pass.

## PDF, source, and public-scope cross-check

Read-only checks of the bound PDF confirm 27 letter-size, unrotated,
unencrypted PDF-1.5 pages; exact title and `Anonymous Authors`; empty subject
and keywords; fixed creation/modification time; 25/25 embedded, subsetted, and
Unicode-mapped fonts; zero raster images, embedded files, forms, or JavaScript;
and successful Ghostscript nullpage rendering. The bound final log has zero
fatal, undefined, warning, and overfull diagnostics and exactly seven
nonblocking underfull hboxes. Page 26 begins Section 8; conclusion prose ends
on page 27 before the References heading and the exactly two bibliography
entries. The body-through-conclusion page is therefore 27, within 24--29.

The live source and decoded PDF preserve the characteristic-zero, integer
`g >= 8` theorem; the displayed `A_g`, `B_g`, and `C_g=B_gA_g`; the two and
only two selector gaps; the phase recurrence; the exact third-coordinate
degree row; the cubic characteristic polynomial; mod-five classes 2, 3, and
4; and the `g=7` strict-cone boundary. The two citation keys and two
bibliography entries are exact and remain context-only. No identity,
affiliation, email, ORCID, acknowledgment, funding, local path, digest,
reviewer/workflow provenance, unresolved marker, priority claim, or forbidden
theorem enlargement was found.

## Stage, role, candidate, build, cleanup, and firewall contracts

The monotone universes are exact and arithmetically consistent:
`F51 -> G53 -> P54 -> R56 -> Q57 -> T58` has respectively
51, 53, 54, 56, 57, and 58 files, with `paper/reviews` as the sole fifth
directory only at `T58`. The five roles are ordinal, distinct, temporally
closed, and each has one declared read universe and write boundary. A later
role cannot start before the predecessor stops and the predecessor universe is
fully re-enumerated and rehashed.

The release candidate contract permits only an exclusive raw byte copy from
`paper/main_round1.pdf` to `paper/main_release_candidate.pdf`, with expected
SHA-256 `b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3`.
Compilation, transformation, metadata rewrite, rendering, signing, and
optimization are all false. The candidate must be created first; only then may
the strict-canonical manifest be written. The manifest must bind every
non-self member of exact `R56`, record the raw-copy dependency DAG, exclude
its own hash and byte count, and leave every external effect false.

The later terminal-build contract names exactly two fresh mode-0700 roots,
copies only the source trio, fixes `SOURCE_DATE_EPOCH=1787356800`,
`FORCE_SOURCE_DATE=1`, `TZ=UTC`, `LC_ALL=C`, `LANG=C`, and
`PATH=/usr/bin:/bin`, and requires the exact four-command
`pdflatex -> bibtex -> pdflatex -> pdflatex` sequence in each root. It requires
eight zero exits, root and command-stream equality, six-way PDF equality, 27
pages, body-through-conclusion page 27, zero fatal/undefined/marker/warning/
overfull diagnostics, seven nonblocking underfull hboxes, 25/25 compliant
fonts, and the pre-review receipt status
`TERMINAL_REBUILD_PASS_PENDING_INDEPENDENT_ROOT_AUDIT`.

The terminal reviewer alone must inspect and clean the six literal historical
roots plus the two then-literal terminal roots. The method is narrowly fenced:
validate the literal real `/tmp` child, ownership, mode, type, inventory, and
absence of symlinks/subdirectories; no-follow unlink each named regular file;
then `rmdir` the empty exact root. Recursive deletion, wildcards, globs,
unresolved variables, and broad targets are forbidden. Cleanup must precede
creation of the sole terminal review file.

All seven external-effect flags remain false: network access, submission,
upload, public hosting, repository push, external messaging, and identity
disclosure. The only eventual terminal effect after the later sole integrity
review is `LOCAL_ANONYMOUS_RELEASE_ONLY`.

## Exact effect of this PASS

This PASS advances only `G53` to `P54` by adding this note. It authorizes only
a fresh release-candidate author who is distinct from both the governance
author and this reviewer to re-enumerate and rehash exact `P54`, create the
exclusive raw candidate copy first, write the strict-canonical final release
manifest second, and stop. It does not authorize this reviewer or the
governance author to perform that work, and it does not directly authorize a
terminal build, root cleanup, terminal review, source edit, release outside
the local anonymous boundary, transport, upload, submission, message, network
access, or identity disclosure. Any mismatch or extra path in `P54` voids the
handoff and requires a blocker rather than continuation.

FINALIZATION_STAGE_PASS
