# Final QA report — P152–P156

**Audit date:** 2026-09-02 UTC.  **Scope:** final Round-2 files only, with
Round-0 and Round-1 artifacts checked for preservation.  **Decision:**
`PASS_INTERNAL / HOLD_EXTERNAL`.

## Exact cold replay

Each verifier was executed from the final workspace without runtime network
access.  Fresh stdout was compared byte for byte with every retained canonical
transcript.

| paper | verifier | assertions | transcript SHA-256 | result |
|---:|---|---:|---|---|
| P152 | `verify_p152.py` | 199,581 | `da908cb14d7825573b0c43870c96155c55b1b40d4d394eef3f1e972071fa1083` | exact match / PASS |
| P153 | `verify.py` | 18,942,551 | `fd900d9d0c1233a265834ce7efc25c43e2c9360a5cb3bbb5eaef4d125f67d6f9` | `CANONICAL.txt` and `verification_output.txt` exact match |
| P154 | `verify.py` | 29,590 | `25ab2e157715ddce077402e8f9383a7d52c261401d6579035eb43e8e945e9219` | `CANONICAL.txt` and `verification_output.txt` exact match |
| P155 | `verify_p155.py` | 16,473,121 | `b398a0cade8b64cdab92ee6c638e7607f3310cf9e304a52e8df07ca7d57e410c` | exact match / PASS |
| P156 | `verify_p156.py` | 3,689,489 | `5c78864527c5781da43f79f8b2b667f9d915fd13fadaea09abe6a7c49f76f53e` | exact match / PASS |

Total: **39,334,332 exact assertions**, five of five final transcript gates
passed.

## Deterministic source-only build

For each manuscript, two new directories were populated with only
`main.tex` and `references.bib`.  P152, P153, P155, and P156 used the declared
four-command LaTeX/BibTeX sequence; P154 used its declared five-command
sequence.  Both independent outputs matched one another and the canonical
`main.pdf` byte for byte.

| paper | pages | bytes | PDF SHA-256 | font rows | isolated builds |
|---:|---:|---:|---|---:|---|
| P152 | 5 | 338,933 | `6671feaadf044abe0e4597a0c81064d9e1bc7590e3891e2acbbd6bf94daec8f6` | 25 | 2/2 exact |
| P153 | 5 | 392,821 | `ef8c82be2935ed23c406a7c688138400d9c76924d11f9d5c089893e8747049a5` | 30 | 2/2 exact |
| P154 | 5 | 373,090 | `72b99fe5f4813434cccb3aef9f8a023d0e7ca471029ce9831b4228dfe8db90cd` | 26 | 2/2 exact |
| P155 | 4 | 345,390 | `54fb1fb0a2519950d3b5725ea5e02c09eb89de13048bf7a97c62d41a9f99ebd1` | 28 | 2/2 exact |
| P156 | 4 | 336,311 | `7e222ce483cc755d4bb732f14ecf94d92ea13c505eba91212150308bebcc7979` | 27 | 2/2 exact |

Total: **10/10 source-only builds**, **23 pages**, **1,786,545 bytes**, and
**136/136 font rows** embedded, subsetted, and Unicode mapped.

The final logs were scanned for `pdfTeX warning`, LaTeX/package warnings,
overfull/underfull boxes, undefined references, and rerun requests: zero
matches.  PDF structural checks pass.  All pages report A4 dimensions
`595.276 x 841.89 pt`; author/subject/keyword metadata contains no identifying
value; each source declares exactly one anonymous author.  Every final page
was rasterized and visually inspected.  P154 was rerendered and reinspected
after the final build-only microtype repair.

## Preserved PDF rounds

| paper | Round 0 SHA-256 | Round 1 SHA-256 | Round 2/current SHA-256 |
|---:|---|---|---|
| P152 | `f2c2476df00d223fdacaf8fb28954d5f620b10611087c3ff35b16ea158f17e57` | `2ac0da7bc87f8ce1fcc8d730eb95a9dd0c79c7bc870f5f7e40a30593bc2f59d9` | `6671feaadf044abe0e4597a0c81064d9e1bc7590e3891e2acbbd6bf94daec8f6` |
| P153 | `8940cc2979406cd788e9a1c2ed23cb76422c50ff92fe99723608d0cfcb8dfd77` | `81e56c67a1029add2bc93aaf67add40cbc68016a82e8eb2a1b7025cad2d3bb7a` | `ef8c82be2935ed23c406a7c688138400d9c76924d11f9d5c089893e8747049a5` |
| P154 | `45901bc68e404cd387c48c848b87ce98d24ead5d60c9ec52b7d584fcb34e60f3` | `aafab23ed519a68e3d03df44999aa8dc525db0f3e2a860abb67825e556fd839b` | `72b99fe5f4813434cccb3aef9f8a023d0e7ca471029ce9831b4228dfe8db90cd` |
| P155 | `f1025e7a19e40eed7dc2608bdebad47ebed998345bc58d94aec6b27025c6b3c8` | `54fb1fb0a2519950d3b5725ea5e02c09eb89de13048bf7a97c62d41a9f99ebd1` | `54fb1fb0a2519950d3b5725ea5e02c09eb89de13048bf7a97c62d41a9f99ebd1` |
| P156 | `ee5cedd089d9d837839f9fc715aae9530e19fc4f414dfcbef77ad0adfafa256c` | `7e222ce483cc755d4bb732f14ecf94d92ea13c505eba91212150308bebcc7979` | `7e222ce483cc755d4bb732f14ecf94d92ea13c505eba91212150308bebcc7979` |

For every paper, `main.pdf` and `main_round2.pdf` are byte-identical.  P154's
Round-2 difference is only `microtype` expansion being disabled to remove a
latent pdfTeX warning; protrusion remains enabled and the mathematical text is
unchanged.

## Review and manifest closure

Hostile Review A closed at `0 Critical / 0 Major / 11 Minor`; hostile Review B
closed at `0 Critical / 0 Major / 4 Minor`.  Every listed item has a concrete
repair and no unresolved severity remains.  The five final paper-local
`SHA256SUMS` files cover, respectively, 29, 25, 25, 30, and 30 non-self files:
**139/139** checks pass.  `CANONICAL_PDF_MANIFEST.sha256` covers all five
current PDFs and passes 5/5.

## Release boundary

Final QA establishes internal artifact integrity only.  It does not establish
novelty, priority, ownership completeness, or external readiness.  No upload,
posting, circulation, author contact, specialist contact, or submission is
authorized.  External state remains `HOLD_EXTERNAL`.
