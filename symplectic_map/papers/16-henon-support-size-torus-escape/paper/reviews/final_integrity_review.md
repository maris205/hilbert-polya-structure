# Paper16 Terminal Final-Integrity Review

Date: 2026-08-17 UTC

Candidate: `henon_support_size_torus_escape_v1`

Anonymous article: *Support Size and Finite-Rank Torus Escape for Generalized Hénon Maps*

## Reviewer independence, activation, and effect fence

I am the fresh terminal-integrity reviewer. I am distinct from the finalization-governance author, the independent finalization-stage reviewer, and the release author, and I authored none of R33. I crossed the terminal temporal fence only after both required handoffs were stable:

- the finalization review was `notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md`, SHA-256 `fe421e3dd771d8dd681dc7935f632852b00eff3425246f1292f7886bef0a68aa`, 21,192 bytes, 356 LF, with final nonempty line `FINALIZATION_STAGE_PASS`;
- the release author then issued an explicit AUTHOR STOP after creating `paper/main.pdf` first and `paper/FINAL_RELEASE_MANIFEST.json` second;
- the copied PDF was SHA-256 `b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f`, 442,639 bytes, 2,452 LF, and was byte-identical to both round PDFs; and
- the final manifest was SHA-256 `4bea0b67fff9c547ddc7f19f9147d8e743deac8a5cbe7a6fdc68c33c370b397b`, 37,020 bytes, one LF.

Before temporary creation, both my primary audit and a separate zero-write cross-check returned `TERMINAL_PRECHECK_PASS`. They independently confirmed exact R33, canonical manifest structure, temporal roles and DAG, the R2 and finalization verdicts, release-effect false, source and proof closure, the persisted PDFs, security and anonymity, and the frozen toolchain. Neither precheck compiled, created a temporary path, or wrote in the project.

This report is the sole regular-file project write by this role. `paper/reviews` was created only as its necessary parent, only after all validation and cleanup had passed. No source, bibliography, governance artifact, prior review, receipt, manifest, or PDF was edited. No network or web access, external message, computer algebra, scientific execution, experiment, data or figure generation, rasterization, screen capture, OCR, submission, upload, public hosting, repository push, or identity action occurred.

## Exact R33 input universe

Immediately before temporary creation, again immediately after explicit cleanup, and immediately before this sole write, R33 was exactly 33 regular non-symlink files in four real directories (`experiments`, `notes`, `paper`, and `refine-logs`), with zero symlinks and zero other entries. The full-byte ledger was:

| Path | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `experiments/EXPERIMENT_PLAN.md` | 5,824 | 129 | `f50a42f9dde61f00801c4696447c6b161a496cdfb7047b468041917225ba65f6` |
| `experiments/EXPERIMENT_TRACKER.md` | 1,971 | 48 | `4578dd2cfbedb25cd2a327ba6d865535bf3d007951f9b749032f9bd6d633b83d` |
| `experiments/finalization_lock.json` | 40,508 | 1 | `5ea0e4fbe7573a06fa5de65abdeea621d8172f9b0b577f28b8818aa6cb629722` |
| `experiments/publication_lock.json` | 55,924 | 1 | `9be9105d43e68ee71c745e9fb8748900bc3605e6918475e393b831f47372449c` |
| `experiments/source_lock.json` | 31,945 | 1 | `86205b1f4dc12ab71302e9b283021c8085afc16f0cf6b479d9a91738c03041fd` |
| `notes/CITATION_VERIFICATION.md` | 10,733 | 205 | `6ec31651060c148d3110856d8709206f60c36ea990b6c433fa9ab0e0944bab24` |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | 7,659 | 59 | `bc5541dcebce9b2cb8cb7e180a91097d55f0d6b0fdc74fb5b4be7f432e462311` |
| `notes/FINALIZATION_STAGE_SCOPE.md` | 30,382 | 392 | `74e215842283b9dca1d0eae22006544273759398fd2129e5629505c4500aac0f` |
| `notes/INDEPENDENT_FINALIZATION_STAGE_REVIEW.md` | 21,192 | 356 | `fe421e3dd771d8dd681dc7935f632852b00eff3425246f1292f7886bef0a68aa` |
| `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md` | 21,165 | 392 | `437e44da869719ef4c74c7de277a162390b6102fc163d96420f7165507ae8f76` |
| `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md` | 23,550 | 492 | `f2ede84a5b19ad275b8b396f4f355c86c6b93a69e515ec29691eb29ac0e0172c` |
| `notes/INDEPENDENT_MANUSCRIPT_SOURCE_REVIEW.md` | 16,365 | 372 | `4cdc119a1590cf9accdbd9f23767a9ca20c287c316ec34cba2ee283e8ea11e0b` |
| `notes/INDEPENDENT_PAPER_PLAN_REVIEW.md` | 9,989 | 211 | `d7493502cf05fb489f5dfe88ce48c6b93c549316bc62f95e617aedb255c399d3` |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | 20,503 | 388 | `e61b2857963ff9a64806bb69f585421b52d1d49537b493dce6d09b24ea3850ea` |
| `notes/INDEPENDENT_SOURCE_DESIGN_REVIEW.md` | 13,903 | 360 | `046e2ec16b46e8de903eac950c1df922725c5b16e359f5ed6c45bd28e737dd61` |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW.md` | 14,929 | 298 | `f1c55a810008ef920cd421c4578a98c1d91f8feb800d478e285d2807602cd72c` |
| `notes/NOVELTY_ASSESSMENT.md` | 7,309 | 117 | `83c9ab497211c7b5cd5d11b7061a292aba4fb258976a01ec8b9216b11226b96b` |
| `notes/PROOF_PACKAGE.md` | 16,808 | 704 | `b44c1f164c97fb5d383cbef941fdef88be4e702066e40efcfb18543be0c4bdf8` |
| `notes/PUBLICATION_STAGE_SCOPE.md` | 44,353 | 997 | `26efa57a0fa024b5272117b1e615da63f631967f9506bbf18df3f3b0bafa30a6` |
| `notes/RESEARCH_QUESTION.md` | 8,319 | 318 | `43b7f965dc04db33c1f00e45880466730d7ee2a25d84f117e91cace71b26a928` |
| `paper/BUILD_RECEIPT_R0.json` | 84,479 | 1 | `6390def39a7dcd1d6eac57a81fcf4e30889b5e358e550d0022679d74ddc1ccb2` |
| `paper/BUILD_RECEIPT_R1.json` | 84,163 | 1 | `7285916176945eaa1ee70224afa3b37ac65c1712ad3feeb0befcb408b36b5e76` |
| `paper/FINAL_RELEASE_MANIFEST.json` | 37,020 | 1 | `4bea0b67fff9c547ddc7f19f9147d8e743deac8a5cbe7a6fdc68c33c370b397b` |
| `paper/PAPER_PLAN.md` | 34,681 | 880 | `875d26506ba552c79fe62fe11ac1a70e73e1a00245e8bb1aacc1b5c58753d336` |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | 9,333 | 1 | `cf389ab3e02733b97c6af868a16253141d74417128ed1e262ddd9aafd94e10cb` |
| `paper/main.pdf` | 442,639 | 2,452 | `b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f` |
| `paper/main.tex` | 80,488 | 1,138 | `2bd2dc0f3ddc2d9e75b48aef06b71bede5ecc5840ab1af7b0363a5c6c3f821d9` |
| `paper/main_round0.pdf` | 442,639 | 2,452 | `b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f` |
| `paper/main_round1.pdf` | 442,639 | 2,452 | `b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f` |
| `paper/references.bib` | 2,019 | 64 | `62e331e87056376d35a2181405cdd90bd1d8a9f5bc82f9334d40b9fbe2505b0f` |
| `refine-logs/FINAL_PROPOSAL.md` | 5,387 | 155 | `220bb54312f80f17b6b99a37afffa902fd04a6b696c0c3e1f60f4ed8d374b540` |
| `refine-logs/INITIAL_PROPOSAL.md` | 4,253 | 98 | `329c7a6687612ff806508640f7add09201ac9ddedd41c10fabd9582a4beab8b2` |
| `refine-logs/REVIEW_SUMMARY.md` | 5,479 | 95 | `20256b3f6915781c07dadb6beec26fa69529c5c7d0660b0171c14d460656c55a` |

The manifest's 32 non-self bindings matched the other 32 rows entry-for-entry, including path, SHA-256, byte count, LF count, regular-file status, and non-symlink status. Its artifact-identity object records its own path, schema, and one-LF property, and excludes exactly its own byte count and SHA-256; the stable AUTHOR STOP and this review bind those excluded values. All paths are safe, unique, sorted, project-relative POSIX paths.

## Canonical manifest, verdict chain, roles, and DAG

The final manifest is strict compact recursively Unicode-key-sorted UTF-8 JSON with exactly one final LF and no CR or BOM. Duplicate-key and nonfinite-number probes are rejected. Strict parse-and-reserialize reproduced all 37,020 bytes and the announced SHA-256 exactly. It records `release_effect=false`, terminal review pending, and submission, upload, public hosting, repository push, external messaging, and identity disclosure all false.

The frozen chain is unchanged:

- `PUBLICATION_STAGE_PASS` at SHA-256 `e61b2857963ff9a64806bb69f585421b52d1d49537b493dce6d09b24ea3850ea`;
- `MANUSCRIPT_SOURCE_PASS` at SHA-256 `4cdc119a1590cf9accdbd9f23767a9ca20c287c316ec34cba2ee283e8ea11e0b`;
- R0 receipt/PDF at `6390def39a7dcd1d6eac57a81fcf4e30889b5e358e550d0022679d74ddc1ccb2` / `b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f`;
- `MANUSCRIPT_R1_PASS` at SHA-256 `437e44da869719ef4c74c7de277a162390b6102fc163d96420f7165507ae8f76`;
- the strict canonical no-op revision receipt at SHA-256 `cf389ab3e02733b97c6af868a16253141d74417128ed1e262ddd9aafd94e10cb`, recording zero changed paths, empty-diff SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, the revision window consumed, and zero remaining;
- R1 receipt/PDF at `7285916176945eaa1ee70224afa3b37ac65c1712ad3feeb0befcb408b36b5e76` / `b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f`;
- `MANUSCRIPT_R2_PASS` at SHA-256 `f2ede84a5b19ad275b8b396f4f355c86c6b93a69e515ec29691eb29ac0e0172c`, with zero blocking, required, cosmetic, and advisory findings; and
- `FINALIZATION_STAGE_PASS` at SHA-256 `fe421e3dd771d8dd681dc7935f632852b00eff3425246f1292f7886bef0a68aa`, also with zero findings.

The expanded universes and set differences are exact: F28 has 28 files; G30 adds only the finalization scope and lock; P31 adds only the finalization review; R33 adds only the raw copied PDF and final manifest; T34 adds only this terminal review and its necessary parent directory. The four read sets equal F28, G30, P31, and R33, respectively. The exclusive write edges are governance pair, finalization review, raw PDF then manifest, and finally this review. Each activation occurred only after the earlier role stopped. No role self-signed or expanded its universe.

## Frozen executable identities

All ten executable records were freshly checked before use and matched the finalization lock and both build receipts, including invoked path, resolved path, byte count, SHA-256, complete version output, and version exit code.

| Role | Invoked path | Resolved path | Bytes | SHA-256 | Frozen version / exit |
|---|---|---|---:|---|---|
| bash | `/bin/bash` | `/usr/bin/bash` | 1,396,520 | `59474588a312b6b6e73e5a42a59bf71e62b55416b6c9d5e4a6e1c630c2a9ecd4` | GNU bash 5.1.16(1), 0 |
| BibTeX | `/usr/bin/bibtex` | `/usr/bin/bibtex.original` | 117,128 | `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` | BibTeX 0.99d / TeX Live 2022-dev, 0 |
| mktemp | `/usr/bin/mktemp` | `/usr/bin/mktemp` | 39,432 | `b239a8e9703853fde69bcf2721c1b474eff8f07c4528ae603e2f0f34d8a063a6` | GNU coreutils 8.32, 0 |
| pdfdetach | `/usr/bin/pdfdetach` | `/usr/bin/pdfdetach` | 23,032 | `e0c04f35fc5b0c4096199ff11d70e49db2b1952b4110f96f5f9ef0a3a4135b2d` | Poppler 22.02.0, 99 |
| pdffonts | `/usr/bin/pdffonts` | `/usr/bin/pdffonts` | 23,064 | `257a74fde0c3c36040504ff9068ee4b896c1cc2f19a9fae5a5b3dda55637ba5e` | Poppler 22.02.0, 0 |
| pdfimages | `/usr/bin/pdfimages` | `/usr/bin/pdfimages` | 39,448 | `cdac55daf2eaacbaf9f80cf8371e935c8686cb4fd7e84c42bba9706c1f10c87d` | Poppler 22.02.0, 0 |
| pdfinfo | `/usr/bin/pdfinfo` | `/usr/bin/pdfinfo` | 59,928 | `8ca6e6d0b2e6b3f135a82feb07b3d5750498eb77e6f66412803f425eb8471a8e` | Poppler 22.02.0, 0 |
| pdfLaTeX | `/usr/bin/pdflatex` | `/usr/bin/pdftex` | 1,802,504 | `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` | pdfTeX 3.141592653-2.6-1.40.22, 0 |
| pdftotext | `/usr/bin/pdftotext` | `/usr/bin/pdftotext` | 43,544 | `7de929ce0686af5dbf76975ad08bbff93526b3d9028035176a4ca89d9d19c27d` | Poppler 22.02.0, 0 |
| Python | `/root/miniconda3/bin/python3` | `/root/miniconda3/bin/python3.12` | 30,626,264 | `9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101` | CPython 3.12.3, PyMuPDF/VersionBind 1.27.2.3, 0 |

## Exactly two clean roots and source-only copies

Exactly two distinct roots were created from the literal template `/tmp/p16-paper16-final-XXXXXXXX`:

- A: `/tmp/p16-paper16-final-A7q6ypgd`;
- B: `/tmp/p16-paper16-final-KeCFk0mR`.

Each realized path matched `^/tmp/p16-paper16-final-[A-Za-z0-9]{8}$`, resolved directly beneath `/tmp`, was a reviewer-owned non-symlink directory with mode `0700`, and was empty before copying. Only `paper/main.tex` and `paper/references.bib` were copied, as `main.tex` and `references.bib`. Each copy was byte-identical to the R33 source: `main.tex` was 80,488 bytes, 1,138 LF, SHA-256 `2bd2dc0f3ddc2d9e75b48aef06b71bede5ecc5840ab1af7b0363a5c6c3f821d9`; `references.bib` was 2,019 bytes, 64 LF, SHA-256 `62e331e87056376d35a2181405cdd90bd1d8a9f5bc82f9334d40b9fbe2505b0f`. Before the first command, each root contained exactly those two regular non-symlink files.

## Exact commands and direct process transcripts

Every one of the eight commands used exactly `TZ=UTC`, `LC_ALL=C`, `LANG=C`, `SOURCE_DATE_EPOCH=1786924800`, and `FORCE_SOURCE_DATE=1`. In each root the exact sequence was:

1. `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex`
2. `bibtex main`
3. `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex`
4. `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape main.tex`

All eight exit codes were zero. Standard output and standard error from each process were redirected directly and byte-for-byte into one distinct, prevalidated, reviewer-owned, non-symlink external regular transcript; there was no outer-output truncation dependency.

| Run/index | Concrete transcript path | Bytes | LF | SHA-256 | Bootstrap events | Exit |
|---|---|---:|---:|---|---:|---:|
| A/1 | `/tmp/p16-paper16-final-A1-transcript-CtxBIpxn` | 16,207 | 540 | `aed46a175a1b0cf5613dbb7f4e86b299bb7742b00c6880ac6cc1ce27f52a2cfd` | 119 | 0 |
| A/2 | `/tmp/p16-paper16-final-A2-transcript-GQIIZHcP` | 155 | 4 | `fd9a13dc2ce58e3d773115b95a63c6bc23e005f41b8676999cb6efad4baa0822` | 0 | 0 |
| A/3 | `/tmp/p16-paper16-final-A3-transcript-rdBhszeq` | 7,307 | 140 | `341273961ab8dde444fdb2e7a1ed447462cd9ba00f49d91a7f08afb131459e4c` | 10 | 0 |
| A/4 | `/tmp/p16-paper16-final-A4-transcript-BNYhPmGC` | 6,516 | 103 | `c0a8571ae457bd0045a64c2b4577f58a9c9003c723321ab823e1e8da78116644` | 0 | 0 |
| B/1 | `/tmp/p16-paper16-final-B1-transcript-wjj09lvy` | 16,207 | 540 | `aed46a175a1b0cf5613dbb7f4e86b299bb7742b00c6880ac6cc1ce27f52a2cfd` | 119 | 0 |
| B/2 | `/tmp/p16-paper16-final-B2-transcript-Th1vyjhP` | 155 | 4 | `fd9a13dc2ce58e3d773115b95a63c6bc23e005f41b8676999cb6efad4baa0822` | 0 | 0 |
| B/3 | `/tmp/p16-paper16-final-B3-transcript-cyiWm5ZG` | 7,307 | 140 | `341273961ab8dde444fdb2e7a1ed447462cd9ba00f49d91a7f08afb131459e4c` | 10 | 0 |
| B/4 | `/tmp/p16-paper16-final-B4-transcript-TfSVp0fs` | 6,516 | 103 | `c0a8571ae457bd0045a64c2b4577f58a9c9003c723321ab823e1e8da78116644` | 0 | 0 |

Corresponding A/B transcript pairs were byte-identical. In each run, separator-free concatenation in command order was exactly 30,185 bytes at SHA-256 `6d4255de4ecd3e667955bd029a974712a66b2242b2fed9ac9f1a3d242fff4dcf`. The bootstrap counts `119, 0, 10, 0` exactly matched both historical receipts. They are the accepted bootstrap-only R1-OBS-001 non-finding; they left no retained warning or error in either final log.

## Exact build artifacts and final logs

Each root ended with exactly the following eight regular non-symlink files and no other entry. Every corresponding A/B pair was byte-identical and every identity matched both frozen receipts.

| Name | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `main.aux` | 15,029 | 163 | `9e864bdc9d2266a69bacca246d37e37ce935523b56503441f02a517ffebb5d34` |
| `main.bbl` | 1,586 | 41 | `ded1b190bcef76e90ee59429b7939f87fa87c229df597d926947b8732a7f368b` |
| `main.blg` | 893 | 46 | `e8645261460eb77d5904f14a1c86bb0b9bac7a0209fca85f5494a01d0d90c662` |
| `main.log` | 25,226 | 645 | `a2fc5a1655350c39f897fefc70cba9225cdcca5765c9587aa484b570653fcb3e` |
| `main.out` | 11,380 | 48 | `0ff7ced14d9cdea1fa77908c1c58a3a098530f88028b3133e15ee4d8ab4da713` |
| `main.pdf` | 442,639 | 2,452 | `b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f` |
| `main.tex` | 80,488 | 1,138 | `2bd2dc0f3ddc2d9e75b48aef06b71bede5ecc5840ab1af7b0363a5c6c3f821d9` |
| `references.bib` | 2,019 | 64 | `62e331e87056376d35a2181405cdd90bd1d8a9f5bc82f9334d40b9fbe2505b0f` |

Both final `main.log` files had zero semantic errors, semantic warnings, undefined references, undefined citations, missing glyphs, hyperref warnings, overfull boxes, and underfull boxes. Both contained the exact output summary `Output written on main.pdf (27 pages, 442639 bytes).` Both BibTeX logs had seven entries and zero warning/error events. Both BBL files contained exactly, in locked order, `amorosoViada2009`, `bellGhioca2024`, `ess2002`, `jiXieZhang2026`, `kimEtAl2025`, `kriegerEtAl2015`, and `melloYasufuku2026`.

## Five-way PDF identity and exact validators

Temporary A, temporary B, `paper/main_round0.pdf`, `paper/main_round1.pdf`, and `paper/main.pdf` were byte-identical. Every member was 442,639 bytes with SHA-256 `b4ffdaf30e2d0684b875863393e6937c26f51ce89c6f47567a24ed9a123e5e4f`. No artifact was selected after comparison.

The following non-raster validator outputs were captured in memory in each temporary root. A and B outputs matched each other and the frozen identities exactly.

| Validator | Bytes | SHA-256 | Exit |
|---|---:|---|---:|
| `pdfdetach -list main.pdf` | 17 | `b598e8defe2b1052cb7712293ce6fd0fb9d5225e770ebbca300edc6cf51970b6` | 0 |
| `pdffonts main.pdf` | 2,444 | `07c3390d85daa8c345ccbb871630b1651dc968bcba965febf83d98b1724ad5c8` | 0 |
| `pdfimages -list main.pdf` | 186 | `0fabc764e123f7f3acd3eaa47311e1c50317f8bbb5b50878e699f21534352e8e` | 0 |
| `pdfinfo main.pdf` | 488 | `6a329e0a6643d3aab4cb03bd721835a452c3640d0e231b47a3f72e63889e6de4` | 0 |
| `pdftotext -layout main.pdf -` | 84,830 | `bcce48bf20dfe0c57d5f2e3af87b0ae0928e759178d25799ff12980e689571a7` | 0 |

Because all five PDFs are identical, the fresh A/B structural and security checks apply identically to all five.

## Document geometry, source, proof, citations, and anti-claims

The document has exactly 27 nonempty pages. Pages 1 through 26 contain the mathematical article including Appendices A, B, and C; References alone occupy page 27. The exact nonwhitespace-character vector is:

`1821, 1868, 2831, 3564, 2964, 2278, 2556, 1262, 2240, 2322, 1123, 1338, 2603, 2363, 2252, 1865, 1086, 1147, 2530, 2547, 2736, 1765, 2166, 1804, 2004, 1721, 1050`.

There are exactly eight numbered main sections and three appendices. The four proof tables render on pages 11, 17, 18, and 18. There are zero figures, zero images, and zero image XObjects. There are exactly 24 font rows, all embedded, subset, and Unicode mapped, and exactly 116 internal named links with zero external or dangerous links.

Fresh source checks found exactly 181 abstract words under the locked math-collapsed convention, eight main sections, three appendices, four table environments, zero figure environments, zero `includegraphics` commands, 75 unique labels, 108 reference commands, and every reference target defined. The title is exact, the source byline is `Anonymous`, the front-matter date is empty, and the deterministic metadata-suppression commands are intact.

The proof and theorem package is exact:

- PC1 states coefficient-uniform two-transition finiteness for collected support `s>=2` with bound `#T2 <= d A(s+2,3r)+M(e)S*`, the algebraic-closure bridge, the rank-3r nondegenerate tuple, rank-2r sparse graphs, the GZ/GU/R0/R1 ledger, endpoint and coefficient-coset handling, vertical constant cancellation, simultaneous labels, torsion fibers, and the defining subset sums;
- PC2 gives the locked rank-one family for every prescribed support and retains the `c=0` and `a=0` boundary examples outside the theorem;
- PC3 gives `#T4 <= 4d A(3,3r)+81d^2`, the A/B/C nine-word table, BA continuation, CB/CBA continuation, and the sharp rank-one CBA chain; and
- the exact constants `A(q,R)=(8q)^(4q^4(q+R+1))`, the sparse budgets, the defining `M(e)`, and both M checksums are unchanged.

The seven bibliography keys above are exactly the seven cited source keys, with no wildcard citation and no unused entry. Amoroso--Viada Theorem 6.2 is the sole cited proof input; Evertse--Schlickewei--Schmidt is historical comparison only. The locked bounded roles for Krieger and collaborators, Bell--Ghioca, Ji--Xie--Zhang version 2, Mello--Yasufuku's distinct epsilon regimes, and Kim and collaborators' restricted constructions are all present without promotion to stronger claims.

The rendered limitations contain exactly these 21 items in this order, with the exact TeX list controlling mathematical notation:

1. No positive-characteristic analogue is asserted.
2. The two-transition theorem does not allow `c=0`, `a=0`, or a zero displayed `b_j`.
3. Equal exponents are combined and zero coefficients deleted before support is counted.
4. Support size is not asserted invariant under affine or polynomial conjugacy.
5. None of the displayed constants is asserted optimal.
6. No effective enumeration algorithm for T2 or T4 is provided.
7. No height estimate is obtained.
8. Periodic points, rational periodic points, and integral cycles are not classified.
9. Every coefficient stratum with an infinite shorter window is not classified.
10. No theorem is given for arbitrary rational maps, polynomial automorphisms, Hénon compositions, or normal forms.
11. Finite-rank scope is not enlarged to arbitrary subgroups.
12. Finite rank is not replaced by finite generation.
13. No coefficient is assumed to lie in Gamma.
14. No additive closure of Gamma is assumed.
15. The bounded literature comparison neither establishes precedence nor excludes unpublished work.
16. Bell--Ghioca's finite residual is not treated as finiteness of the whole hitting-time set, and the torus restriction is not declared regular.
17. Ji--Xie--Zhang non-density is not converted into finiteness.
18. The Mello--Yasufuku epsilon regimes are not merged.
19. The restricted constructions of Kim and collaborators are not made universal bounds.
20. No code, computer algebra, computation, scan, experiment, data, or numerical check is theorem evidence.
21. The support-one result receives no separate precedence assertion and is proved internally rather than used as a black box.

The absorption paragraph occurs exactly once in `paper/main.tex` and exactly once in the rendered paper, in Section 8.3 only:

> An earlier manuscript by the same authors treated only the one-monomial case. The present paper reproduces that theorem and proof in full as part of the support-size phase transition, thereby absorbing the earlier manuscript; the two manuscripts will not be submitted in parallel, and the present paper is the sole intended external version of the overlapping material.

## PDF security and anonymity

All five PDFs are unencrypted. Each has zero AcroForm, embedded file, file attachment, JavaScript, launch action, RichMedia, XFA, and image XObject features. There is no trailer ID. PDF author, subject, keywords, creator, producer, creation date, and modification date are empty. The visible byline is exactly `Anonymous`.

Fresh extracted-text and object checks found no manuscript-author name, affiliation, email address, self-identifying link, acknowledgement, internal project or temporary path, governance verdict or hash, agent or model name, long hexadecimal token, external URI, external file link, repository instruction, or dangerous action. Required neutral bibliographic names, years, and locked version dates were retained and treated as exempt.

## Explicit cleanup and post-cleanup stability

After all evidence was recorded in memory, each of the eight concrete transcript paths in the command table was revalidated as a reviewer-owned regular non-symlink file with its exact locked identity and individually unlinked. No wildcard or glob was used.

Each of the following files was then revalidated and individually unlinked in this exact name order under A and then under B: `main.aux`, `main.bbl`, `main.blg`, `main.log`, `main.out`, `main.pdf`, `main.tex`, `references.bib`. Thus 16 concrete regular-file paths were individually removed. Each root was verified empty and then removed with `rmdir`. No recursive deletion, broad target, unresolved environment variable, symlink traversal, raster tool, wildcard, or glob was used.

All eight transcripts and both roots were proven absent. A fresh full-byte project scan after cleanup again found exact R33: 33 regular files, four directories, zero symlinks, zero other entries, and 33/33 identities unchanged. At that point both `paper/reviews` and this review path were still absent.

## Findings, T34, local effect, and immutability

There is no inventory, binding, canonicalization, temporal, role, DAG, source, review, revision, toolchain, command, transcript, artifact, log, citation, proof, theorem, document, font, link, security, anonymity, cleanup, effect, or immutability blocker. Blocking, required, cosmetic, and advisory finding counts are all zero.

Creation of the necessary parent `paper/reviews` and this sole regular file yields exact T34: the 33 R33 paths listed above plus `paper/reviews/final_integrity_review.md`, for 34 regular files in exactly five directories (`experiments`, `notes`, `paper`, `paper/reviews`, and `refine-logs`), zero symlinks, and zero other entries. R33 remains byte-for-byte unchanged.

The only effect is `LOCAL_ANONYMOUS_RELEASE_ONLY`. This is not submission, upload, public hosting, repository push, external messaging, camera-ready identity insertion, author disclosure, or authorization for any such action. The complete T34 universe is immutable under this protocol; any later external or identity-bearing action requires wholly separate explicit authorization.

FINAL_INTEGRITY_PASS
RELEASE_CONFIRMED
