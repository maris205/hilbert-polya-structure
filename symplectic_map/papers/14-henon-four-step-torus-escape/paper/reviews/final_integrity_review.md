# Paper 14 Terminal Final-Integrity Review

Date: 2026-08-17 UTC

Candidate: `henon_four_step_torus_escape_v1`

Scope: terminal review of the stable local anonymous release-candidate author stop under `experiments/finalization_lock.json` and `paper/FINAL_RELEASE_MANIFEST.json`. I am fresh and independent of every author, builder, and reviewer named by the lock. I did not author or alter any of the 34 reviewed inputs.

## Verdict basis

All terminal gates passed. Before this report was created, the canonical project root contained exactly the locked R34 set: 34 regular files, the four directories `experiments`, `notes`, `paper`, and `refine-logs`, zero symlinks, zero other filesystem entry types, and no `paper/reviews` path. All 33 manifest input bindings matched their declared byte counts and SHA-256 identities. The manifest itself matched the stable author stop at 32293 bytes and SHA-256 `e832be91a990d1d1caf7e2b4aba40fa8d9a1196524c815e03b30309df6226e68`.

The immediate prewrite R34 identity ledger SHA-256 was `b7ce3823f60ecee26969ef0816746eca24e8d161b69286bc75686e878d821bfd`. This ledger encodes, in locked R34 path order, each path, byte count, SHA-256 identity, and LF count. It matched the author-stop bindings and contained no hard-link substitution; the three persistent PDF paths had distinct inodes.

Strict UTF-8 parsing and canonical byte round-trips passed for all seven R34 JSON artifacts: the source, publication, and finalization locks; the R0 and R1 build receipts; the R1 source-revision receipt; and the final release manifest. Each used recursively lexicographic object-key order, no insignificant whitespace, and exactly one terminal LF. Synthetic duplicate-key and `NaN`, `Infinity`, and `-Infinity` probes were each rejected.

The manifest's 12-edge frozen source-to-R2 DAG prefix was byte-for-byte structurally equal to the finalization lock. The complete DAG had 16 edges, 34 covered nodes, 13 roots, 21 outputs, and no cycle. The theorem lock, source identities, receipt chain, review verdict chain, and finalization gate were unchanged. The bounded source revision had change count zero, its sole revision window was consumed, and no additional revision window was authorized.

The terminal reviewer role and build contract in the manifest were structurally identical to those in the finalization lock. The terminal reviewer was the sole next role and this report was the sole project-file write authorized to it. At author stop, `release_effect` was false. Submission, upload, repository push, public hosting, venue communication, camera-ready change, network transfer, and identity disclosure remained forbidden.

## Locked toolchain and clean builds

The toolchain identities and version outputs matched the lock:

- `/usr/bin/pdflatex` resolved to `/usr/bin/pdftex`, 1802504 executable bytes, SHA-256 `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9`.
- `/usr/bin/bibtex` resolved to `/usr/bin/bibtex.original`, 117128 executable bytes, SHA-256 `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f`.

Exactly two distinct, initially empty, real non-symlink roots were created: `/tmp/p14-paper14-final-A7c9K2mQ` and `/tmp/p14-paper14-final-R4t8V6xZ`. Each initially received only byte-exact copies of `paper/main.tex` and `paper/references.bib`. Every command used `FORCE_SOURCE_DATE=1`, `LANG=C`, `LC_ALL=C`, `SOURCE_DATE_EPOCH=1786838400`, and `TZ=UTC`, and the exact locked sequence `pdflatex -> bibtex -> pdflatex -> pdflatex` with the locked absolute executable paths and arguments. All eight build process exit codes were zero.

The two final temporary inventories were identical and contained exactly eight regular files. `main.toc` was absent in both builds. Every present allowed file was byte-for-byte identical across A and B and matched every R0/R1 receipt build:

| File | Bytes | LF count | SHA-256 |
|---|---:|---:|---|
| `main.aux` | 9036 | 117 | `bbeaac7b60ba30549663c0e8f8826791a8e4e687489aa66046d2e0eeee212f31` |
| `main.bbl` | 1710 | 49 | `2102f0d5077f0946d97a93e09c824ee42725161b1d000c76f9adc53331094f92` |
| `main.blg` | 893 | 46 | `d7a9a65efe15b8bd2d3cdf0357ee228d10fcf02e47dd1ee17a06212222bd3e26` |
| `main.log` | 25556 | 652 | `81b1d76a8cecf652e80a89ffe5bdca88d65da1ddf0d5f6e239ac8f0b4ef0deba` |
| `main.out` | 5256 | 23 | `9022eb613584537c76a78f0731bd7cd0c69e614184df323db12ee72a24a8be7a` |
| `main.pdf` | 384084 | 2017 | `4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414` |
| `main.tex` | 47961 | 1270 | `415f1395f07153ccb158e69cb70051e95e719802d0a1c3315df88be7ccfab538` |
| `references.bib` | 2666 | 79 | `816fd8211b7c5ad91dc227ac71b90444cdf5c3b713b60dd9a70fbdd1a8d419bc` |

The A PDF, B PDF, `paper/main.pdf`, `paper/main_round1.pdf`, and `paper/main_round0.pdf` were five-way byte-identical: 384084 bytes, SHA-256 `4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414`.

## PDF, bibliography, log, and anonymity gates

Read-only stdout inspection of both build PDFs established 17 physical pages, mathematical content through the mixed content/reference boundary on page 17, and the `References` heading beginning on page 17. `pdftotext` produced 39500 bytes with SHA-256 `33258515a0d6f41326c2e6ac7033542d0390c1f8ebbad6fb4c346b28eaba48cd`; all 17 pages were nonempty and no unresolved marker was present.

Each PDF contained exactly 21 fonts; all 21 were embedded, subsetted, and Unicode-mapped. The exact metadata title was `Four-Step Escape from Finite-Rank Tori for Monomial Henon Maps`, the subject was `Arithmetic dynamics`, and the PDF author field was empty. The sole visible author line was `Anonymous`. Creator and producer metadata matched the receipts. There were zero image objects, embedded files, signatures, JavaScript payloads, forms, custom metadata, or metadata streams.

The source citations, AUX citations, bibliography entries, and BBL items were the same eight locked keys. The BBL identity was 1710 bytes and SHA-256 `2102f0d5077f0946d97a93e09c824ee42725161b1d000c76f9adc53331094f92`. Final logs contained zero undefined citations or references, zero BibTeX warnings or errors, zero LaTeX errors, zero missing characters or fonts, and zero overfull boxes. Per build, the only diagnostics were the receipt-classified three hyperref PDF-string warnings and one underfull hbox, covered by accepted cosmetic findings `P14-R1-COS-001` and `P14-R1-COS-002`; the unclassified warning count was zero.

No rasterization, screenshot, image conversion or extraction, network access, package installation, submission, upload, or external communication occurred.

## Cleanup and terminal scope

Immediately before cleanup, each root was revalidated as the exact permitted real directory and every entry as a listed regular file. In the locked explicit order, every present file was individually unlinked; the absent `main.toc` was explicitly rechecked; each empty root was then removed by nonrecursive `rmdir`. No wildcard or recursive deletion was used. Both full temporary paths were subsequently verified absent.

This report is the sole R34-to-T35 project-file addition and `paper/reviews` is its necessary parent. The pass effect is strictly `LOCAL_ANONYMOUS_RELEASE_ONLY`. It is not a public release, submission, upload, identity disclosure, camera-ready authorization, or permission for any later source, manifest, build, or review write.

FINAL_INTEGRITY_PASS
RELEASE_CONFIRMED
