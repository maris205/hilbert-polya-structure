# Independent Paper 27 revised-build review (R1)

## Disposition

Authorization: `B07-E0147-P27-BUILD-REVISION-REVIEW-AUTHORIZATION-R1`.

Disposition: **FAIL / HOLD (no release authority)**.  The two fresh roots are
technically reproducible and mutually identical after the permitted root-name
normalization, but the locked PAPER_PLAN target is 24--28 proof-content pages
and both observed PDFs have only 17 total pages.  The target is not waived or
padded.  A second, independent action-history finding is recorded below.

This artifact is the only write made for this review.  No source, build root,
cache, ledger, release copy, cleanup, upload, or external effect was made.

## Scope and firewall

I read only the paths named by the authorization: `BATCH_07_STATUS.md`; the
three anonymous source files under `paper/`; the two named revision-profile
notes; the preserved failed-root `main.bbl` and `main.log`; the nine named
files in each of `build/r0-rev1-20260830` and `build/r1-rev1-20260830`; and the
four named cache directories in each fresh root.  Checks were direct metadata,
byte, text, manifest, PDF, and normalization checks.  `pdfinfo`, `pdffonts`,
`pdftotext`, and `strings` were used only with PDF output directed to stdout
or `/dev/null`; no compiler or bibliography command was run.

One prohibited probe occurred accidentally in the first metadata loop.  The
loop used the misspelled, absent path
`/root/autodl-tmp/symple_map/papers/27-positive-newton-translation-reciprocity/build/r0-rev1-20260830/main.fls`
(the workspace component should have been `symplectic_map`) and attempted
`stat`, `wc`, `sha256sum`, and `tail` on it.  Each operation returned ENOENT;
no file was opened or changed, and the correctly spelled authorized path was
then checked directly.  This was nevertheless an absent-path/out-of-whitelist
probe prohibited by the review firewall and is counted as a Blocker.

## Finding census

| Class | Findings | Basis |
|---|---:|---|
| Blocker | 1 | accidental absent/out-of-whitelist typo probe described above |
| Major | 1 | both PDFs are 17 pages, below the locked 24--28 proof-content target |
| Minor | 1 | each final log has 5 overfull and 7 underfull box warnings (12 total) |
| Ambiguity | 0 | no unresolved evidence ambiguity after the direct checks |
| **Total** | **3** | |

## Direct metadata and byte census

All listed text and generated files below are regular, mode `0644`, link count
one.  Every text file passed UTF-8 decoding, had zero CR, NUL, or BOM bytes,
and ended in exactly one LF.  The PDF LF counts are reported only as raw-byte
counts and are not interpreted as line endings.

| Path (relative to project) | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `BATCH_07_STATUS.md` | 464378 | 8387 | `44c15f00bbdc58bf4be7aca3568c96bdec3aedeb8f1757aa17d48b7ac8f73f7c` |
| `paper/main.tex` | 33811 | 829 | `ba9879a7084821b18c3e76166706d90d99bc4cb8e0bb1cb09d04a23f3a007f18` |
| `paper/math_commands.tex` | 601 | 17 | `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` |
| `paper/references.bib` | 6610 | 217 | `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5` |
| `notes/BUILD_PROFILE_REVISION.md` | 5238 | 109 | `1c01ec583391c3f60996018debd85f860c4b9709f3913da49c7e6c686e032f63` |
| `notes/INDEPENDENT_BUILD_PROFILE_REVISION_REVIEW.md` | 9161 | 69 | `815f4940302b832f5315c4f2695bcacd21f8bba0ec22d274a78f1573b2f8254c` |
| `build/r0-20260829/main.bbl` (preserved) | 3939 | 118 | `23ad34a5605226dbea73edda95769b4768c2d2c6e834737f3ebe19d502f41df8` |
| `build/r0-20260829/main.log` (preserved) | 16625 | 532 | `94419a503d6f35405ca5d45544f40db6dd6f6fa4a617a34c1b98036a153b1b51` |

Fresh-root file identities were:

| File | r0 bytes/LF/SHA-256 | r1 bytes/LF/SHA-256 |
|---|---|---|
| `main.tex` | 33811 / 829 / `ba9879a7084821b18c3e76166706d90d99bc4cb8e0bb1cb09d04a23f3a007f18` | 33811 / 829 / `ba9879a7084821b18c3e76166706d90d99bc4cb8e0bb1cb09d04a23f3a007f18` |
| `math_commands.tex` | 601 / 17 / `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` | 601 / 17 / `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` |
| `references.bib` | 6610 / 217 / `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5` | 6610 / 217 / `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5` |
| `main.aux` | 3393 / 79 / `fa39835627f5ac0ba1e3f7c4c873844209ebbbeb4ae27435fe43da2427112e52` | 3393 / 79 / `fa39835627f5ac0ba1e3f7c4c873844209ebbbeb4ae27435fe43da2427112e52` |
| `main.bbl` | 3942 / 118 / `3a64583e5ee52f80c00b10235f003bd803bde3520e3fadefd99801a153beedb7` | 3942 / 118 / `3a64583e5ee52f80c00b10235f003bd803bde3520e3fadefd99801a153beedb7` |
| `main.blg` | 906 / 46 / `76792d7f67dc314358a53f43894e619c7da0a51af611ecb3e7ba161b38ee2f92` | 906 / 46 / `76792d7f67dc314358a53f43894e619c7da0a51af611ecb3e7ba161b38ee2f92` |
| `main.fls` | 23262 / 355 / `573ac913b7ffaadb0fb58d02dff8832664c82b54f45f996606c6136c1dfc20cd` | 23262 / 355 / `46ede3c9acb4d81854a9c85734ac31d9d77bc7d9aeacdd546ec266633cc62353` |
| `main.log` | 14809 / 396 / `8c1b9e6e92651c4a00ac67da9dae1f7188921a6820a471b607a75f2b1dc32458` | 14809 / 396 / `8c1b9e6e92651c4a00ac67da9dae1f7188921a6820a471b607a75f2b1dc32458` |
| `main.pdf` | 308570 / raw LF 1838 / `9d2f443090ea85102e14d973cadaef81532f0b2a3ccde6041bc4ed742787753e` | 308570 / raw LF 1838 / `9d2f443090ea85102e14d973cadaef81532f0b2a3ccde6041bc4ed742787753e` |

The fresh root directories are mode `0700` (link count six).  Each named
`texmf-var`, `texmf-config`, `texmf-home`, and `xdg-cache` directory is mode
`0755`, link count two, and has zero direct entries in both roots.  No cache
bytes were found.

## Source copies, manifests, and root-name normalization

`cmp` returned zero for every source-to-r0, source-to-r1, and r0-to-r1
comparison for all three source files.  Reconstructed canonical manifests,
with rows sorted as `main.aux`, `main.bbl`, `main.blg`, `main.fls`, `main.log`,
`main.pdf`, `main.tex`, `math_commands.tex`, `references.bib` and framed as
`path<TAB>bytes<TAB>LF<TAB>644<TAB>1<TAB>sha256<LF>`, each have 9 rows, 817
framing bytes, and 9 LF:

* r0 manifest SHA-256: `11817214698bb1b12ab09fee9b1e19934d84337a235fb29d1147783aac02fe1c`.
* r1 manifest SHA-256: `293709291e59defbc767d2f11cefb44fd0f3f2ac8cb5f05dd8b3c1099f1ddf29`.

The only raw root-manifest difference is the recorder-file hash.  Replacing
`r0-rev1-20260830` and `r1-rev1-20260830` by the common token `ROOT` gave
`cmp=0` for `main.fls` and `main.log`; the raw logs also compare equal, while
the raw `.fls` files differ only in their one `PWD` root-name token.  Each
`.fls` has exactly three outputs (`main.log`, `main.aux`, `main.pdf`) and no
project-absolute output path.  The `.aux`, `.bbl`, and `.blg` files compare
byte-for-byte equal across roots.

## Profile, tool/package, source, and environment bindings

The revised profile records the exact source trio hashes shown above, 15
64-hex digest tokens, the fixed invocation targets (`pdflatex` resolving to
`pdftex`, `bibtex` resolving to `bibtex.original`), eight named TeX packages,
the one-shot sequence (one pdfLaTeX, BibTeX, then two pdfLaTeX passes),
`-no-shell-escape`, and root-local cache variables.  The independent profile
review is bound by SHA-256
`815f4940302b832f5315c4f2695bcacd21f8bba0ec22d274a78f1573b2f8254c` and its
all-zero profile census is the prior consumed control record.  Under this
review whitelist I did not open the external `/usr/bin` or TeX package files;
the fresh logs corroborate the bound versions and package paths (pdfTeX
3.1415926-2.6-1.40.22, TeX Live 2022/dev/Debian; amsmath, amssymb, amsthm,
mathtools, booktabs, array, longtable, and enumitem), and the profile's
record-level hashes remain internally consistent with every fresh artifact.

The fixed profile environment is exactly `PATH=/usr/bin:/bin`,
`SOURCE_DATE_EPOCH=0`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, `LC_ALL=C`, `LANG=C`,
with the four root-local `TEXMF*`/`XDG_CACHE_HOME` directories.  The epoch
timestamps in both logs/PDFs and the root-local `.fls` working directories are
consistent with those bindings.  No shell-escape, network, installation, or
output outside a fresh root is evidenced.

## Preserved failed-root boundary

The preserved `r0-20260829/main.bbl` is 3939 bytes and contains the malformed
line 101 `of {\mathbb c}^n`.  The preserved log records the corresponding
`LaTeX Error: \mathbb allowed only in math mode` at line 515 and the terminal
`Fatal error occurred, no output PDF file produced!` at line 532, with
undefined citation warnings from the pre-BibTeX attempt.  The revised fresh
`main.bbl` instead contains the corrected math enclosure and the fresh logs
have no such error.  Fresh source copies match the revised paper trio and no
fresh `.fls` or manifest names the preserved root, so the failed root remains
evidence-only and was not copied, overwritten, or reused.

## PDF byte, text, font, metadata, and security checks

Both PDFs begin with `%PDF-1.5`, end with `%%EOF`, compare byte-for-byte, and
have SHA-256 `9d2f443090ea85102e14d973cadaef81532f0b2a3ccde6041bc4ed742787753e`.
`pdfinfo` reports for each: Creator `TeX`, Producer `pdfTeX-1.40.22`, PDF
version 1.5, letter pages, no encryption, no JavaScript, no AcroForm, no
tagging, no user properties, and no suspects.  Creation and modification are
raw `D:19700101000000Z` (the local `pdfinfo` rendering is 1 January 1970
CST).  `strings` finds no `/Encrypt`, `/JavaScript`, `/JS`, `/AA`,
`/OpenAction`, `/AcroForm`, `/Metadata`, `/MarkInfo`, `/StructTreeRoot`,
`/UserProperties`, `/Suspects`, `/Title`, `/Author`, `/Subject`, or
`/Keywords` entries.

`pdffonts` lists 23 Type 1 fonts, all embedded, subset, and Unicode-enabled;
the complete command output compares equal between roots.  `pdftotext`
exits zero for each PDF, produces identical 37,587-byte decoded text, and
contains the anonymous author line, the title, `Theorem 3.2`, `Proposition
6.1`, `Lemma 7.1`, `References`, and the cited author/reference text including
Shafikov--Wolf and Bianchi.  A scan of the decoded text finds zero governance,
ledger, path, hash, authorization, or root-name tokens.

## Final-log and bibliography checks

The two final logs are byte-identical.  Each reports `Output written on
main.pdf (17 pages, 308570 bytes)`.  Counts per final log are: LaTeX/package
warnings 0; undefined-reference warnings 0; label-change/rerun warnings 0;
fatal/error lines 0; overfull boxes 5; underfull boxes 7.  The 12 nonfatal
typesetting warnings are disclosed as the Minor finding above, including a
471.85603pt overfull equation at source line 259.  The `.blg` files compare
equal, report BibTeX 0.99d, 20 entries, and `warning$` count 0.

## Locked page target and release decision

`pdfinfo` independently reports exactly 17 pages for both fresh PDFs.  The
decoded page sequence places article content through page 14 and references
on pages 15--17, so proof-content is at most 14 pages (and less if title/
abstract front matter is excluded).  This is strictly below the locked
24--28 proof-content-page target; even the generous 17-page total is seven
pages short of the minimum.  The target is a release criterion and cannot be
waived, padded, or repaired in this review.  Together with the strict
firewall violation recorded above, this requires `FAIL / HOLD`; no source edit,
rebuild, cleanup, or release action is authorized.

BATCH07_PAPER27_BUILD_REVISION_REVIEW_FAIL
