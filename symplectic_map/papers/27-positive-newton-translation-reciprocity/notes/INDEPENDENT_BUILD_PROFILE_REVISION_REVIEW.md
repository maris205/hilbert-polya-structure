# Paper 27 independent build-profile revision review (R1)

## Review disposition

This is the fresh review authorized by `B07-E0143-P27-BUILD-PROFILE-REVISION-REVIEW-AUTHORIZATION-R1`.  The review was restricted to the explicit whitelist: `BATCH_07_STATUS.md`, `BUILD_PROFILE.md`, `BUILD_PROFILE_REVISION.md`, `SOURCE_LOCK_REVISION.md`, the two prior source/revision review records, the three anonymous source files, the four named `/usr/bin` executable paths, and the eight named TeX package paths.  Every listed path was read directly and checked with `stat`, `sha256sum`, `wc`, `od`, and bounded `diff` comparisons.  No path search, recursive traversal, absent-path test, future-root probe, compiler, BibTeX invocation, cache operation, generated output, source mutation, or external effect was used.  The two revision roots were deliberately not probed.

The finding census is all zero.  In particular, the revised bibliography hash is exactly `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5`, and the resolved BibTeX regular file has the complete 64-character digest `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f`.  All other profile-revision digest tokens are also exactly 64 hexadecimal characters and match their named files.

## Direct metadata census

The following are the direct `stat`/`wc`/`sha256sum` observations.  `type` is the resolved type (`stat -L`); `/usr/bin/pdflatex` and `/usr/bin/bibtex` are invocation symlinks, while their resolved regular files have the recorded mode and link-one identity.  The final column records the `od` two-byte tail check for text records; executable tails are binary and are not interpreted as line endings.

| Path | Type; bytes; LF; mode; links | SHA-256 | `od` tail / result |
|---|---|---|---|
| `BATCH_07_STATUS.md` | regular; 442414; 8118; 0644; 1 | `bfe397f6cee5a94943c4324703437df351a828f303a308c1b173227520be0ea1` | `310a`; OK |
| `notes/BUILD_PROFILE.md` | regular; 6124; 117; 0644; 1 | `8fba2cbb84a02078094fbced92cf2b6286e86b6be4360bdbc0a893bd55b32c6e` | `4e0a`; OK |
| `notes/BUILD_PROFILE_REVISION.md` | regular; 5238; 109; 0644; 1 | `1c01ec583391c3f60996018debd85f860c4b9709f3913da49c7e6c686e032f63` | `4e0a`; OK |
| `notes/SOURCE_LOCK_REVISION.md` | regular; 3387; 68; 0644; 1 | `8afd2516173ab949a65bfab7e232c1040c10b897bcce9681e7418c04d0d93445` | `4e0a`; OK |
| `notes/INDEPENDENT_SOURCE_REVISION_REVIEW.md` | regular; 5858; 112; 0644; 1 | `769c21cf8d6c9b42b044cd3546020ad1ea07b1e9fdcdb1e20bc2215f62f98309` | `530a`; OK |
| `notes/INDEPENDENT_SOURCE_LOCK_REVISION_REVIEW.md` | regular; 5903; 113; 0644; 1 | `c909eaac0776eeebeef03fc2b8deca2f041a6cda3004da2d113470fa056ecfe5` | `530a`; OK |
| `paper/main.tex` | regular; 33811; 829; 0644; 1 | `ba9879a7084821b18c3e76166706d90d99bc4cb8e0bb1cb09d04a23f3a007f18` | `7d0a`; OK |
| `paper/math_commands.tex` | regular; 601; 17; 0644; 1 | `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` | `7d0a`; OK |
| `paper/references.bib` | regular; 6610; 217; 0644; 1 | `a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5` | `7d0a`; OK |
| `/usr/bin/pdflatex` (resolved) | regular; 1802504; 4629; 0755; 1 | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` | ELF; OK |
| `/usr/bin/pdftex` | regular; 1802504; 4629; 0755; 1 | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` | ELF; OK |
| `/usr/bin/bibtex` (resolved) | regular; 117128; 393; 0755; 1 | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` | ELF; OK |
| `/usr/bin/bibtex.original` | regular; 117128; 393; 0755; 1 | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` | ELF; OK |
| `amsmath/amsmath.sty` | regular; 87648; 2942; 0644; 1 | `027b292408d989f370f160c9b5f5b89641f69cd19027b0342beb022dd74d7c83` | `2e0a`; OK |
| `amsfonts/amssymb.sty` | regular; 13829; 269; 0644; 1 | `70838b061b56569dd3ed9f339b1bdd1c78ba185de49f27ceae331c97f48b5986` | `2e0a`; OK |
| `amscls/amsthm.sty` | regular; 12594; 444; 0644; 1 | `8d5e2bdb117297385971927b14fe4804314133dc0027b3171249a08280894626` | `2e0a`; OK |
| `mathtools/mathtools.sty` | regular; 59397; 1839; 0644; 1 | `e6bb70c66ffccc39e0ce8786d3dfca962a473339008a5a51ffae09075b74f5a7` | `2e0a`; OK |
| `booktabs/booktabs.sty` | regular; 6078; 175; 0644; 1 | `3fe694a5406f84847143e56ba1841385364277cfe7694a9f4bc0072ca8656abc` | `2e0a`; OK |
| `tools/array.sty` | regular; 12694; 376; 0644; 1 | `1518422cc09b174c47105e41e3606260714b8f99049e3005a87f3c2ce034d157` | `2e0a`; OK |
| `tools/longtable.sty` | regular; 12892; 474; 0644; 1 | `196f2a7038e1727c4088a015bf11cac88abfedc5b7ee5eca65f44ab91dbac415` | `2e0a`; OK |
| `enumitem/enumitem.sty` | regular; 51697; 1909; 0644; 1 | `a217353d233e54e8c0944d87ea2924ec1f20d849a35b749698df03884856e5e3` | `2e0a`; OK |

The package paths in the table are the exact `/usr/share/texlive/texmf-dist/tex/latex/...` paths named by the authorization.  The `od` head checks showed the expected ELF magic for all four executable files and ordinary text starts for all package/source/control files.  All nine text/control/source files passed strict UTF-8 conversion, had no BOM, CR, or NUL byte, and had exactly one terminal LF (the displayed tail has a non-LF byte followed by `0a`).

## Binding and cross-record checks

- The revised source trio agrees byte-for-byte with both `SOURCE_LOCK_REVISION.md` and each prior revision-review table: `main.tex` `33811/829/ba9879...`, `math_commands.tex` `601/17/34fdee...`, and `references.bib` `6610/217/a77d814...`.  The bibliography contains the single authorized inline-math enclosure in the `shafikov_wolf_2003` title; its exact corrected line occurs once and the old malformed expression occurs zero times.  The citation/reference key sets agree at 20 keys, and the anonymous-source firewall has zero governance/path/hash/provenance tokens.
- `INDEPENDENT_SOURCE_REVISION_REVIEW.md` matches its bound `5858`-byte, `112`-LF digest `769c21cf8d6c9b42b044cd3546020ad1ea07b1e9fdcdb1e20bc2215f62f98309`; `INDEPENDENT_SOURCE_LOCK_REVISION_REVIEW.md` matches `5903` bytes, `113` LF, digest `c909eaac0776eeebeef03fc2b8deca2f041a6cda3004da2d113470fa056ecfe5`.  Their terminal markers are respectively `BATCH07_PAPER27_SOURCE_REVISION_PASS` and `BATCH07_PAPER27_SOURCE_LOCK_REVISION_PASS`.
- The profile-revision digest token census contains exactly 15 long hexadecimal tokens (aggregate, three source/review bindings, two executable bindings, and eight package bindings); every token is length 64.  A per-row `diff` against the resolved executable and package hashes returned status 0.  The executable byte diffs `/usr/bin/pdflatex` versus `/usr/bin/pdftex` and `/usr/bin/bibtex` versus `/usr/bin/bibtex.original` also returned status 0.
- The fixed environment diff is exact: `PATH=/usr/bin:/bin`, `SOURCE_DATE_EPOCH=0`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, `LC_ALL=C`, `LANG=C`, and the four root-local `TEXMF*`/`XDG_CACHE_HOME` placeholders.  The one-shot command-sequence diff is exact, including one `pdflatex`, one `bibtex`, and two final `pdflatex` commands with the recorded flags; no custom harness is introduced.
- The ledger's E0142 author-stop records `post_manifest_sha256: b0054477a2f90f7f10aa02e40fec345ae57feddd3a9b8e1ab197438aa054782e` and `manifest_rows: 41`; E0143 repeats that digest and row count in both pre/post fields.  The profile-revision file's own observed digest is `1c01ec583391c3f60996018debd85f860c4b9709f3913da49c7e6c686e032f63` (5238 bytes, 109 LF, mode 0644, link one), and its final marker is `BATCH07_PAPER27_BUILD_PROFILE_REVISION_FROZEN`.
- The exact newly reserved names are `papers/27-positive-newton-translation-reciprocity/build/r0-rev1-20260830` and `papers/27-positive-newton-translation-reciprocity/build/r1-rev1-20260830`.  The profile and E0142/E0143 records consistently state that neither was created or inspected before a later build authorization.  I performed no stat, existence test, listing, or other probe of either name.  The failed `r0-20260829` root is consistently described by the lock/review/ledger records as preserved, immutable, evidence-only, outside the aggregate, and unavailable for copy, repair, overwrite, or reuse; no failed-root bytes were read under this whitelist.

## Finding census

| Check class | Findings |
|---|---:|
| revised source bytes/metadata and `a77d814...` binding | 0 |
| executable identities and complete `c9ec...ad18f` BibTeX digest | 0 |
| eight package paths, hashes, modes, and link counts | 0 |
| profile-revision digest lengths (all 64 hex) | 0 |
| lock/revision review/source cross-record consistency | 0 |
| environment and one-shot sequence | 0 |
| E0142/E0143 manifest digest and 41-row binding | 0 |
| fresh-root and preserved-failed-root boundary | 0 |
| UTF-8/LF/BOM/CR/NUL and terminal-marker checks | 0 |
| citation closure and anonymous metadata firewall | 0 |
| prohibited action or external-effect evidence | 0 |
| **Total** | **0** |

No discrepancy remains.  The sole permitted output of this all-zero review is
this regular mode-0644, link-one UTF-8/LF artifact; no build authority is
implied by it.

BATCH07_PAPER27_BUILD_PROFILE_REVISION_PASS
