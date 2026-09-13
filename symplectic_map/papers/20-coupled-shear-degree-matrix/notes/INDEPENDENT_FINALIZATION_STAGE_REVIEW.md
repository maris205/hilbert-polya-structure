# Independent Paper 20 Finalization-Stage Review

Date: 2026-08-22 UTC  
Project: `papers/20-coupled-shear-degree-matrix`  
Role: fresh independent finalization-stage reviewer  
Disposition on any blocker: write nothing

## 1. Review boundary and role independence

I authored none of the 63 files in the locked predecessor universe `G63`.
I read the live project without following symlinks, independently enumerated
and rehashed it, decoded the finalization lock with duplicate-key rejection,
and independently inspected every bound live `/tmp` residue object by literal
path and `lstat` before writing this review.

No source, bibliography, PDF, earlier receipt, earlier lock, earlier review,
or temporary-residue byte was modified. I did not compile LaTeX, run BibTeX,
perform CAS, numerical, experimental, or other scientific execution, create a
candidate or release object, access the network, clean any path, or cause
submission, upload, public hosting, repository push, external messaging, or
identity disclosure. This file is my sole project write.

## 2. Exact `G63` project universe and frozen bindings

No-follow enumeration returned exactly 63 regular files and the four
project-internal directories `experiments`, `notes`, `paper`, and
`refine-logs`. It returned zero symlinks and zero other entry types. The
future paths `paper/main_release_candidate.pdf`,
`paper/FINAL_RELEASE_MANIFEST.json`,
`paper/TERMINAL_REBUILD_RECEIPT.json`, and `paper/reviews` were absent.

The lock's `F61` contains exactly 61 unique, safe project-relative paths in
lexicographic byte order. Its path set equals the live `G63` path set after
excluding only `notes/FINALIZATION_STAGE_SCOPE.md` and
`experiments/finalization_lock.json`. I reread every one of the 61 files and
recomputed its SHA-256, byte count, and LF-byte count. All 61 tuples match the
lock and the 61-row inventory in the scope without exception.

For a compact independently reproducible audit checksum, I encoded each
binding as UTF-8
`path<TAB>sha256<TAB>bytes<TAB>lf<LF>` in lexicographic byte-path order.
The resulting `F61` ledger has 6,686 bytes, total bound content of 2,023,509
bytes and 16,233 LF bytes, and SHA-256
`2cd43b18b31bd3d13a0d91d29c73ca449361af305eb9ec54d90c49b620661cff`.

The two added `G63` identities are:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `notes/FINALIZATION_STAGE_SCOPE.md` | `52ea249aed4ae377cc8be5ebf6e056ae2d9bc3d3b16abe1e56e374412be3d151` | 19,288 | 290 |
| `experiments/finalization_lock.json` | `3b1098c48b6d1b2a4a0f8cf0319aefb8fe6cf1ab4db16baf7fdd9bd345eae842` | 34,833 | 1 |

The scope's last nonempty line is exactly
`FINALIZATION GOVERNANCE SCOPE AUTHOR STOP`, and its identity equals the
lock's `scope_binding`. Repeating the same ledger construction across all 63
live files gives 6,903 ledger bytes, 2,077,630 content bytes, 16,524 LF bytes,
and SHA-256
`de2731527f429da18244dc5b0dac0cb56b819630cede9649caf6ca83876c6ae0`.

## 3. Strict-canonical lock and self-exclusion

The finalization lock decodes as UTF-8 JSON with duplicate-key rejection and
nonfinite-number rejection. Its raw byte stream contains no BOM, carriage
return, or NUL. Recursive Unicode-code-point key sorting with compact `,:`
separators and no ASCII escaping change reproduces the raw bytes exactly,
followed by exactly one terminal LF; the entire file contains one LF byte.

The live object has schema `PAPER20_FINALIZATION_LOCK_V1` and state
`FINALIZATION_STAGE_LOCKED_PENDING_INDEPENDENT_FINALIZATION_REVIEW`. Its own
identity is correctly self-excluded as path
`experiments/finalization_lock.json`, `self_excluded: true`, null SHA-256,
null byte count, and terminal-LF count one. It does not make a false
self-referential digest claim. Its scope binding, `F61` bindings, source
bindings, cleanup snapshot, stage universes, permissions, and effect ceiling
all decode consistently with the bound bytes and scope.

The scope and lock also retain and explicitly demote two earlier scope/lock
pairs as governance-recovery history. Their recorded identities are not used
as current authority. The current pair above is the only live finalization
authority, and no `F61`, source, theorem, candidate-input, residue, role, or
external-effect fact changed across that disclosed pre-review recovery.

## 4. Metadata correction, title lineage, and PDF roles

The superseding correction note is a regular non-symlink file at
`notes/FINAL_MANUSCRIPT_INTEGRITY_R1_METADATA_CORRECTION.md`, SHA-256
`e6791c117c48785e31eabe58f4349e59b0b8d270e662ab0281760b921e6d3404`,
3,915 bytes and 83 LF, ending exactly
`FINAL_MANUSCRIPT_INTEGRITY_METADATA_CORRECTION_AUTHOR_STOP`. Direct
readback confirms that
`notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` is
`937612e3810c99eda8e9499abaa188b1d5b4d8421c7d8c260188d2d4b1481e02`,
8,742 bytes and 161 LF, with terminal line `PUBLICATION_STAGE_PASS`. Thus the
retained 9,484-byte / 213-LF transcription in
`FINAL_MANUSCRIPT_INTEGRITY_R1.md` is disclosed historical metadata only and
is not promoted by the current scope or lock.

The title lineage is explicit and non-substantive:

- the frozen historical source-lock string is `Coupled Hamiltonian Shear
  Degree Matrices in A^4: An asymmetric g>=5 family`;
- the TeX display is **Coupled Hamiltonian Shear Degree Matrices in
  A^4: An Asymmetric g>=5 Family**, with mathematical typesetting for
  `A^4` and `g>=5`;
- the authoritative governance-safe display string is `Coupled Hamiltonian
  Shear Degree Matrices in A4: An Asymmetric g>=5 Family`;
- the PDF metadata title is the deliberately shorter `Coupled Hamiltonian
  Shear Degree Matrices in A4`, with author `Anonymous Authors`;
- the older batch-discovery working title remains historical upstream
  wording rather than a candidate-byte identity.

The capitalization and working-title differences change neither the theorem
nor any source or PDF byte. The frozen source trio independently rehashes as:

| Path | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| `paper/main.tex` | `b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90` | 61,835 | 1,619 |
| `paper/math_commands.tex` | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` | 702 | 20 |
| `paper/references.bib` | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` | 2,335 | 73 |

Independent hashes, LF counts, byte counts, byte comparisons, and `pdfinfo`
page reads distinguish the PDF roles exactly:

| Artifact | SHA-256 | Bytes | LF | Pages | Role |
|---|---|---:|---:|---:|---|
| `paper/main_round1.pdf` | `07426e1892fbbb85876a6f79401318c16f9d3aee96ae7d6ae2b087a25ca98e40` | 429,723 | 2,338 | 23 | sole candidate input |
| `paper/main.pdf` | `ed58824860f77186210fee298b1631e7877868dc828b4b3a9cd048fcaa1545e9` | 380,574 | 2,049 | 14 | historical R0 only |
| `paper/main_round0.pdf` | `ed58824860f77186210fee298b1631e7877868dc828b4b3a9cd048fcaa1545e9` | 380,574 | 2,049 | 14 | historical R0 only |
| `paper/main_round1_failed_pre_pagefix.pdf` | `e40b4b44a3a8fa7e1102efdbc615476a9fa038cf146777838de6b9e0b5cb24f9` | 424,691 | 2,329 | 22 | failed pre-pagefix history |

`main.pdf` and `main_round0.pdf` are byte-identical to each other.
`main_round1.pdf` is byte-unequal to both the R0 byte and the failed
pre-pagefix byte. The future release candidate is absent, so no stale R0 PDF
has been silently substituted and no release claim yet exists.

## 5. Authoritative evidence chain

Every object below is included in the verified `F61` bindings. Independent
terminal/status readback gives:

| Object | Required live endpoint | Result |
|---|---|---|
| `experiments/source_lock.json` | strict-canonical frozen source lock | present and rehashed |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | `SOURCE_LOCK_PASS` | exact |
| `paper/PAPER_PLAN.md` | proof-first plan | present and rehashed |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | `PAPER_PLAN_PASS` | exact |
| `experiments/publication_lock.json` | strict-canonical publication lock | present and rehashed |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `PUBLICATION_STAGE_PASS` | exact |
| `notes/INDEPENDENT_PAPER_SOURCE_R1_PAGEFIX_REVIEW.md` | `PAPER_SOURCE_R1_PAGEFIX_PASS` | exact |
| `notes/INDEPENDENT_PAPER_SOURCE_R2_PAGEFIX_REVIEW.md` | `PAPER_SOURCE_R2_PAGEFIX_PASS` | exact |
| `paper/BUILD_RECEIPT_R1.json` | status `BUILD_R1_PAGEFIX_PASS` | exact |
| `notes/INDEPENDENT_BUILD_R1_PAGEFIX_REVIEW.md` | `BUILD_R1_PAGEFIX_PASS` | exact |
| `notes/INDEPENDENT_BUILD_R2_PAGEFIX_REVIEW.md` | `BUILD_R2_PAGEFIX_PASS` | exact |
| `notes/FINAL_MANUSCRIPT_INTEGRITY_R1.md` | `FINAL_MANUSCRIPT_INTEGRITY_PASS` | exact, subject to disclosed metadata correction |
| `notes/FINAL_MANUSCRIPT_INTEGRITY_R1_METADATA_CORRECTION.md` | `FINAL_MANUSCRIPT_INTEGRITY_METADATA_CORRECTION_AUTHOR_STOP` | exact |

The terminal-build commands and deterministic environment in the
finalization lock agree with the passing page-fixed R1 receipt: four commands
per root, using `pdflatex`, `bibtex`, and two final `pdflatex` passes under
`SOURCE_DATE_EPOCH=1787356800`, `FORCE_SOURCE_DATE=1`, UTC and C locale. The
earlier chain proves only the frozen source and reviewed 23-page candidate
input. It grants no present compile, cleanup, external release, or transport
effect to this reviewer.

## 6. Independent live `/tmp` residue audit

Literal `/tmp` is a non-symlink real directory. Each of the 13 bound
top-level targets is its literal child, exists with the locked type, owner,
group, mode, link count where applicable, and complete child set. All 77
bound residue leaves are root-owned, non-symlink regular files with link
count one. The seven directories contain exactly 71 direct regular files and
zero symlinks, subdirectories, or other entry types.

For each directory below I independently sorted child names in byte order and
encoded each child as
`name<TAB>mode<TAB>uid<TAB>gid<TAB>nlink<TAB>sha256<TAB>bytes<TAB>lf<LF>`.
Every individual field matches the lock.

| Literal directory | Mode | Leaves | Leaf bytes | Leaf LF | Child-ledger SHA-256 |
|---|---:|---:|---:|---:|---|
| `/tmp/p20-paper20-r1-pagefix-retry-A-ev483m` | 0700 | 13 | 576,770 | 5,856 | `3b5010506b1e00bb934e7ad6a9f056acfcd092fb0062002ab904d19a374901a9` |
| `/tmp/p20-paper20-r1-pagefix-retry-B-s4iTTx` | 0700 | 13 | 576,770 | 5,856 | `3b5010506b1e00bb934e7ad6a9f056acfcd092fb0062002ab904d19a374901a9` |
| `/tmp/p20-paper20-r1-pagefix-A-JBuZF3` | 0700 | 7 | 66,202 | 1,752 | `fe6b748a480302ec90e83b85e497b699189d2270d65c5a88289fd4197cc2ac0c` |
| `/tmp/p20-paper20-r1-pagefix-B-w344h4` | 0700 | 7 | 66,202 | 1,752 | `fe6b748a480302ec90e83b85e497b699189d2270d65c5a88289fd4197cc2ac0c` |
| `/tmp/p20-paper20-r1-A-7GEBaI` | 0700 | 13 | 567,377 | 5,735 | `907c06150dfe0cad8f47cfe8fce2d396e49c3160ff70b42d001843a4b199d2ab` |
| `/tmp/p20-paper20-r1-B-rx5cFc` | 0700 | 13 | 567,377 | 5,735 | `907c06150dfe0cad8f47cfe8fce2d396e49c3160ff70b42d001843a4b199d2ab` |
| `/tmp/p20-failed-r0-20260822` | 0755 | 5 | 44,425 | 995 | `844c3d8278c1fd0fcea2889e8ed4a923a3f4a03be0b8058fa734948d3d5706f4` |

The six direct-file targets independently match:

| Literal file | SHA-256 | Bytes | LF | Mode |
|---|---|---:|---:|---:|
| `/tmp/p20-build-r0-command-1.log` | `8338909c7f6dd779890f5e53b7d24ae54b2818f50b57b949e8142168056d67bd` | 12,943 | 368 | 0644 |
| `/tmp/p20-build-r0-command-2.log` | `7b0a0a8d2f1749b44546479273ee9d474d9656cc2a276630ff83cc8a72044dc9` | 158 | 4 | 0644 |
| `/tmp/p20-build-r0-command-3.log` | `1d53b8542c228250a42dc08502677a5c274a0e4dbae526d80446ebbcd5b8767c` | 8,169 | 186 | 0644 |
| `/tmp/p20-cites.txt` | `cd9474bf43d6567ff170f382db9eedc7a97d37618036c3caf2191ef718056210` | 286 | 9 | 0644 |
| `/tmp/p20-labels.txt` | `2a0192a84106cd17ec30cd8bca2d3285b18fbf7e941b5d94372d39d397917678` | 1,513 | 67 | 0644 |
| `/tmp/p20-main-text.txt` | `a690d5478e1a2da1817db1c11ec10a6fade9bf408993c0cfcc8ef13fd20b5a6e` | 43,383 | 739 | 0644 |

For the full set of 77 leaves, sorting by literal absolute path and encoding
`path<TAB>mode<TAB>uid<TAB>gid<TAB>nlink<TAB>sha256<TAB>bytes<TAB>lf<LF>`
gives 10,043 ledger bytes, 2,531,575 content bytes, 29,054 LF bytes, and
SHA-256
`c62093b3cbbe95a8c1c3739d1e087eb5f0d494c0463fe045304ca80017e214d4`.
The canonical compact JSON encoding of the lock's complete
`cleanup_contract` is 18,575 bytes with SHA-256
`19a45211f786babda540de40b959185645fa74af2a15bc22957a89f455355a63`.

No path was removed or altered. No path matching either future terminal-root
template existed at review time. The 13 historical targets therefore remain
live for the sole terminal-integrity reviewer, which must revalidate them and
the two later terminal roots before any exact no-follow cleanup.

## 7. Monotone universes, closed roles, and effects

The stage arithmetic is internally exact:

- `F61` contains the 61 frozen inputs;
- `G63` adds only the scope and finalization lock;
- this sole passing review creates `P64`;
- `R66` may later add only the raw-copy candidate and strict-canonical
  manifest;
- `Q67` may later add only the strict-canonical terminal receipt;
- `T68` may later add only the sole final-integrity review, with
  `paper/reviews` as the only new project directory.

The governance author, this independent reviewer, the future candidate
author, future terminal-build evidence author, and future sole
terminal-integrity reviewer are distinct closed roles. Their permitted writes
are non-overlapping and their stop conditions are explicit. The candidate
author may only make an exclusive raw byte copy of `main_round1.pdf` and then
write the manifest. The terminal builder must use two fresh mode-0700 roots,
write only the receipt, and leave both roots live. Cleanup remains reserved
for the fresh sole terminal reviewer after every `Q67`, root, diagnostic,
PDF, theorem, citation, anonymity, role, and effect check passes.

All finalization-lock external-effect fields are false: network access,
submission, upload, public hosting, repository push, external messaging, and
identity disclosure. Build, CAS, experiment, scientific execution,
publication-external, release-external, transport, and upload permissions are
false at this review gate. The terminal ceiling is only
`LOCAL_ANONYMOUS_RELEASE_ONLY`; no external release or communication is
authorized by this PASS.

## 8. Verdict

I found no hash, inventory, canonicalization, self-exclusion, metadata,
title-lineage, candidate-role, authority-chain, residue-snapshot,
monotonicity, role-separation, cleanup-safety, or external-effect blocker.
Exact `G63` passes its independent finalization-stage gate. This verdict
authorizes only the next local `P64`-to-`R66` role under the frozen scope; it
does not itself create a candidate, manifest, build, cleanup, release, or
external effect.

FINALIZATION_STAGE_PASS
