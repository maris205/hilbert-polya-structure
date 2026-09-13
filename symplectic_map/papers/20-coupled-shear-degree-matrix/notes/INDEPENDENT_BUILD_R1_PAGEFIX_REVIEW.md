# Paper20 — Independent R1 build audit after the page-contract repair

Date: 2026-08-22 UTC  
Review ID: `BUILD_R1_PAGEFIX_AUDITOR_2026_08_22`

This is an independent, read-only audit of the two fresh replacement build
roots authorized by `BUILD_AUTHORIZATION_R1_PAGEFIX_RETRY.md`.  I did not run
LaTeX, BibTeX, CAS, symbolic or numerical code, experiments, network access,
transport, publication, or upload, and I did not edit any author source,
metadata, source receipt, or build receipt.  This reviewer-owned note is
out-of-band and is not part of the locked author-file aggregate.

## Authority and source binding

The live authority chain was read to EOF and independently rehashed:

| object | bytes / LF | SHA-256 |
|---|---:|---|
| `notes/SOURCE_PAGEFIX_AUTHORIZATION_R1.md` | 1,095 / 22 | `2043428f4a18dc1a980d122bb98273fa7d6fd89410f8e7eb68d1eeb5b51d20a8` |
| `notes/BUILD_AUTHORIZATION_R1_PAGEFIX.md` | 2,792 / 54 | `57a784bf9fc48ed1f00b31c979be490935a131836bc7e5092e98a6afd59b2a71` |
| `notes/BUILD_AUTHORIZATION_R1_PAGEFIX_RETRY.md` | 954 / 19 | `6994e72d95239c5110abd5f032712e0ef2f5bfcb5e651ca6267d286e5272fd87` |
| `paper/BUILD_METADATA_R1.json` | 5,549 / 1 | `b891b8bb81d6383fc4b49fb81f41c346ecafbbd9663a25b44e7eb6bb8badf8dd` |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | 6,206 / 1 | `d8600e8d50efcda1b694e332a5b4282beb8b6c9ad9b5f302199f6f1aba728d3a` |

The retry authorization names exactly these fresh roots and requires the
source/page-fix hashes below.  All live source rows and all copies in both
roots match byte-for-byte:

| source | bytes / LF | SHA-256 |
|---|---:|---|
| `paper/main.tex` | 61,835 / 1,619 | `b891987e42396981b3859d2aaeb00b39b8281ccb559ef9d6383200a1e8682b90` |
| `paper/math_commands.tex` | 702 / 20 | `37a0347c8784e75020bee7ec545ad350f5c79509ec71f135db4ce982ebf5d582` |
| `paper/references.bib` | 2,335 / 73 | `529612c446e0a56919efb79dae7f80358f4f3fa1fc3424e6e15f7da2886c5eaf` |
| `paper/PAPER_PLAN.md` | 22,064 / 397 | `4dfcf82f8dae85502fced2f7b1d73d80e35ee242eee609dd74b5f59ca793adf3` |
| `experiments/source_lock.json` | 11,847 / 1 | `57d989c7f0aa3fe2351dc3e5d47b761f8add953c5ff70246febedf9183079581` |

The two fresh source-review bindings required by the authorization are live
and passed: `notes/INDEPENDENT_PAPER_SOURCE_R1_PAGEFIX_REVIEW.md` has SHA
`e83053d521542773696a59478944d8974b46b97b5b854cb7c775cc257cb2ee30`, and
`notes/INDEPENDENT_PAPER_SOURCE_R2_PAGEFIX_REVIEW.md` has SHA
`e81e148cc8e9d4b220a62146a6bebb906df0cdb4fb5e555eca423e8ef2a8eaa5`.

The metadata and source-revision receipt are canonical UTF-8 JSON (one
terminal LF, no BOM/CR/NUL, no duplicate keys, finite numbers, and exact
recursive Unicode-key-sorted round trips); their self-identity fields are
null and excluded as required.  The metadata intentionally still has
`planned_build.status=NOT_RUN`, null artifact/page fields, and
`build_authorized=false`: the explicit page-fix retry authorization is the
separate permission for this consumed build, and this audit does not silently
rewrite the pre-receipt metadata state.  The frozen ten-file author aggregate
also independently recomputes to 45,416 bytes, 873 LF, SHA
`3b27fe493832559e90ac5dcb059628492074574fe9492d12e500f7da107f7e90`.

## Build roots and deterministic identity

The audited roots are:

* `/tmp/p20-paper20-r1-pagefix-retry-A-ev483m`
* `/tmp/p20-paper20-r1-pagefix-retry-B-s4iTTx`

Each contains the three permitted source inputs, the four retained command
logs, and the deterministic generated outputs.  The authorized sequence was
the complete four-command chain

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

with `HOME=/root`, `PATH=/usr/bin:/bin`,
`FORCE_SOURCE_DATE=1`, `LANG=C`, `LC_ALL=C`,
`SOURCE_DATE_EPOCH=1787356800`, `TZ=UTC`, and network disabled.  The eight
retained command logs show successful completion and final `Output written`
records; all final source hashes match the frozen inputs, so no source edit
occurred during the build.  Every corresponding file in the two roots is
byte-identical:

| output | bytes | SHA-256 |
|---|---:|---|
| `main.pdf` | 429,723 | `07426e1892fbbb85876a6f79401318c16f9d3aee96ae7d6ae2b087a25ca98e40` |
| `main.aux` | 11,920 | `a96b8a6d534c04f897581590f431164f75f600ee0c85ce062cdc33ad617a8d16` |
| `main.bbl` | 2,282 | `15c4662bc3e3c6b65eef8a8b80d7f8210da9b8b3011a9ba5c5896504adff81f6` |
| `main.blg` | 900 | `3292543c220a005dc56db3fdaf1287cd9f142cc52b2d0db012f4da156ae66e15` |
| `main.log` | 28,899 | `34bf450186dfc29b4355ade433de214f48daf09efb724e0941a32456a6b5771f` |
| `main.out` | 5,653 | `9cfe3093cc76d9ea5da78ad4dc35e3701dcbd91e14031ba6052e937212f12fa2` |

The four command logs are also identical across roots (sizes 14,846, 158,
9,446, and 8,071 bytes, respectively).  Ghostscript's null-page parser
exits successfully.  `pdfinfo` reports a 23-page, unencrypted Letter-size
PDF (version 1.5, no JavaScript); its deterministic creation/modification
time is consistent with the locked epoch.

## Page contract and readback

Page-by-page text extraction places Section 10 on page 20, Section 11 on
page 21, and `12 Conclusion` on page 22.  `References` begins later on that
same page, with the remaining bibliography on page 23.  Thus the
substantive body through the conclusion is exactly 22 pages, satisfying the
locked 22--26 range (planned 24); the total PDF length is 23 pages.  The
references sharing page 22 does not reduce the body count because the contract
is measured through the conclusion.

## Diagnostics, bibliography, labels, and fonts

The final (fourth) LaTeX pass has zero fatal errors, emergency stops,
undefined references, undefined citations, overfull boxes, or draft-marker
hits.  Its nonfatal diagnostics are three underfull boxes (the related-work
table), four hyperref PDF-string token warnings, and one
`Label(s) may have changed` warning.  The first pass has the expected
pre-BibTeX undefined-citation/reference messages, and the third pass retains
the expected citation-resolution messages before the final pass; neither
appears in the final pass.  BibTeX uses `plainnat`, processes seven entries,
and reports zero warnings in `main.blg`.

Independent source/auxiliary checks find 67 unique labels with no duplicates,
64 reference uses over 44 unique targets with no missing targets, and 67
resolved `newlabel` records in `main.aux`.  There are 14 citation uses over
seven unique keys; the seven keys are exactly the seven `\\bibitem` keys in
`main.bbl` and the seven `\\bibcite` keys in `main.aux`, with no missing or
unused key.  Exact scans of the source and extracted PDF find zero `??`,
`[?]`, `TODO`, `TBD`, `VERIFY`, or `FIXME` markers.

`pdffonts` reports 25 font rows; every row has `emb=yes`, `sub=yes`, and
`uni=yes`.  This count is a readback fact (repeated font names can occupy
separate PDF objects), and all rows satisfy the embedding/subsetting checks.

## Historical artifacts explicitly excluded

The earlier expanded pre-page-fix roots
`/tmp/p20-paper20-r1-A-7GEBaI` and `/tmp/p20-paper20-r1-B-rx5cFc`, together
with the persisted `paper/main_round1.pdf`, are the superseded 22-page
artifact (SHA `e40b4b44a3a8fa7e1102efdbc615476a9fa038cf146777838de6b9e0b5cb24f`);
its conclusion is on page 21 and it fails the locked body minimum.  The
consumed wrapper roots `/tmp/p20-paper20-r1-pagefix-A-JBuZF3` and
`/tmp/p20-paper20-r1-pagefix-B-w344h4` contain only failed command logs and no
PDF.  None of these historical or failed artifacts is used as evidence for
the replacement pass.  The two `pagefix-retry` roots above are the only
audited replacement-build evidence.

## Verdict

No source/authorization binding, deterministic identity, PDF integrity,
page-contract, diagnostic, bibliography, cross-reference, font, or provenance
blocker was found.  This is a build-audit pass only: it does not itself create
`BUILD_RECEIPT_R1.json`, persist/replace the PDF, or authorize publication,
transport, upload, experiments, CAS, or further source editing.  Those
downstream actions require the parent-controlled receipt and the independent
R2 build audit.

BUILD_R1_PAGEFIX_PASS
