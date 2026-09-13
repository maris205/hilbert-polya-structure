# Independent build-profile review (R5)

reviewer_role: batch07-fresh-independent-build-profile-reviewer-r5
review_scope: direct reads and metadata only on the exact paths authorized by B07-E0128; no search, recursion, absent-path or future-root probe, compiler, BibTeX execution, cache write, generated output, or external effect

## Profile and source checks

BUILD_PROFILE.md is a regular 0644 file of 6,124 bytes and 117 LF bytes, with SHA-256 `8fba2cbb84a02078094fbced92cf2b6286e86b6be4360bdbc0a893bd55b32c6e`.
Every recorded profile SHA-256 token, including the corrected booktabs token, is exactly 64 hexadecimal characters and matches its resolved file.

| Path | Bytes | LF | Mode | SHA-256 |
|---|---:|---:|---:|---|
| `paper/main.tex` | 33811 | 829 | 0644 | `ba9879a7084821b18c3e76166706d90d99bc4cb8e0bb1cb09d04a23f3a007f18` |
| `paper/math_commands.tex` | 601 | 17 | 0644 | `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` |
| `paper/references.bib` | 6607 | 217 | 0644 | `4ec09da4d7be513d2cf11811515975e1f3c35b53ae9d84cbda6748cb39cbd23b` |

The source binding is intact: `main.tex` inputs `math_commands.tex`, uses exactly the eight profiled packages, and names `references` for the bibliography.  No alternate source, shell escape, or unprofiled input is present in the direct source read.

## Resolved toolchain and packages

| Path | Resolved bytes | Mode | SHA-256 |
|---|---:|---:|---|
| `/usr/bin/pdflatex` (same regular file as `/usr/bin/pdftex`) | 1802504 | 0755 | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |
| `/usr/bin/pdftex` | 1802504 | 0755 | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |
| `/usr/bin/bibtex` (same regular file as `/usr/bin/bibtex.original`) | 117128 | 0755 | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |
| `/usr/bin/bibtex.original` | 117128 | 0755 | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |

The eight exact package paths and profile digests all match: amsmath `027b292408d989f370f160c9b5f5b89641f69cd19027b0342beb022dd74d7c83`, amssymb `70838b061b56569dd3ed9f339b1bdd1c78ba185de49f27ceae331c97f48b5986`, amsthm `8d5e2bdb117297385971927b14fe4804314133dc0027b3171249a08280894626`, mathtools `e6bb70c66ffccc39e0ce8786d3dfca962a473339008a5a51ffae09075b74f5a7`, booktabs `3fe694a5406f84847143e56ba1841385364277cfe7694a9f4bc0072ca8656abc`, array `1518422cc09b174c47105e41e3606260714b8f99049e3005a87f3c2ce034d157`, longtable `196f2a7038e1727c4088a015bf11cac88abfedc5b7ee5eca65f44ab91dbac415`, and enumitem `a217353d233e54e8c0944d87ea2924ec1f20d849a35b749698df03884856e5e3`.

## Manifest and constraint checks

The frozen E0128 status rows report `manifest_rows: 36`, `manifest_framing_bytes: 5150`, and identical pre/post aggregate SHA-256 `96e326326a1789143c9cd8dab0f974b7015f404295ab73a6663599c08b925567`.  The profile-opening 35-row framing digest recorded inside BUILD_PROFILE.md remains historical and distinct from this corrected frozen aggregate.

The fixed environment, root-specific TEXMF/XDG cache locations, exact three-pass command sequence, absolute executable targets, 0700 fresh-root rule, source-copy rule, `-no-shell-escape`, and prohibition on retries, alternate tools, writes outside an authorized root, and generated files outside that root all agree with the profile.  No build, cache, generated output, PDF, release copy, or external effect was performed or observed.

findings: 0

BATCH07_PAPER27_BUILD_PROFILE_PASS
