# Final QA report — P137–P141

**Checkpoint:** 2026-09-01 UTC.  
**Result:** **5/5 PASS INTERNAL; FINAL FREEZE; EXTERNAL HOLD**.

| paper | pages | bytes | exact control | independent gate | fonts | visual pages |
|---:|---:|---:|---:|---|---:|---:|
| P137 | 5 | 400,794 | 18,504,770 | `GO_INTERNAL` | 33/33 | 5/5 |
| P138 | 3 | 279,050 | 3,870,590 | `GO_INTERNAL` | 21/21 | 3/3 |
| P139 | 4 | 326,430 | 2,654,300 | `GO_INTERNAL AFTER OWNER REPAIR` | 25/25 | 4/4 |
| P140 | 4 | 260,643 | 190,740 | `GO_INTERNAL AFTER SCOPE REPAIR` | 22/22 | 4/4 |
| P141 | 4 | 254,394 | 750,181 | `GO_INTERNAL (OWNER-THIN)` | 20/20 | 4/4 |
| **total** | **20** | **1,521,311** | **25,970,581** | **5/5** | **121/121** | **20/20** |

## Control and build replay

After every theorem or ownership repair, all five paper-local verifiers ran in
fresh Python processes.  Each raw stdout matched its frozen transcript byte
for byte.  The canonical transcript digests are:

| paper | transcript SHA-256 |
|---:|---|
| P137 | `7ae1064fd1a2b585c77702d4af04c5acb5934be90d31c5e4f0da8f2e9a049df6` |
| P138 | `551a61f69ba5bb09355bc99c95401bb89ee58ab5c732b81eaa24c6a016330675` |
| P139 | `801b82a729adff63f35dc92306ad1044444d2cd0fc89b603306064fd7f6ec0fe` |
| P140 | `c23afcaf89ee9bf9ac5c2cd43ee72d6599155b9930215bf0dba0b4c328087ec8` |
| P141 | `bcb2e2f68121a3c13e79e0987fcd1ee5e985b225f4a948357424ed70ee695502` |

Fresh verifier/build/visual workspaces were:

```text
/tmp/137-qa-Lkh8vH
/tmp/138-qa-2eEtBf
/tmp/139-qa-bTa7Xm
/tmp/140-qa-8OP89c
/tmp/141-qa-8oLikb
```

Each isolated build began with only `main.tex` and `references.bib` and used
four stages: `pdflatex -> bibtex -> pdflatex -> pdflatex`.  Every command
exited zero.  Every settled log is warning/error/undefined-reference/
undefined-citation/multiply-defined-label/bad-box/rerun free, and every final
PDF is byte-identical to its canonical `main.pdf`.

## Historical-round integrity

- P137 and P138 required no source repair; all canonical and Round-0/1/2 PDFs
  are byte-identical within each paper.
- P139 preserves byte-identical pre-owner-repair Round-0/1/2 PDFs and a
  distinct repaired `main.pdf == main_round3.pdf`.
- P140 preserves a distinct pre-scope-repair Round-0 PDF and
  `main.pdf == main_round1.pdf == main_round2.pdf`.
- P141 changed only documentary summaries; current and Round-0/1/2 PDFs are
  byte-identical.

Every historical round PDF is mode `0444`.

## Bibliography, PDF, text, and visual gates

The bibliography closures are 5/5, 4/4, 5/5, 2/2, and 4/4: **20/20** entries
are cited and resolved.  P139's repaired Mantaci et al. owner citation appears
correctly in the bibliography and rendered PDF.

All PDFs are A4, rotation zero, version 1.5, unencrypted, form-free,
JavaScript-free, attachment-free, and have empty Title, Author, Subject, and
Keywords metadata fields.  No PDF has a metadata stream.  Every visible
byline is `Anonymous`.

All **121/121** font rows are embedded, subsetted, and Unicode-mapped.  Fresh
layout-preserving text extraction contains **80,711 bytes**, **10,797 words**,
and **1,102 lines**.  All pages have searchable text.  Scans found no
unresolved reference, placeholder, draft marker, local filesystem path, email
address, ORCID, affiliation, correspondence, funding statement, or personal
identity leak.  Each manuscript visibly retains its external-hold boundary.

All **20/20** final pages were rasterized at 144 dpi and inspected one by one.
Titles, anonymous bylines, abstracts, theorem statements, proofs, equations,
tables, owner boundaries, limitations, conclusions, and references are
legible.  No page has clipping, overlap, missing glyphs, malformed display,
truncated reference, unintended blank content, or rotation.

## Integrity gate

Paper-local `SHA256SUMS` manifests pass entry by entry:

| paper | entries | manifest SHA-256 |
|---:|---:|---|
| P137 | 20 | `a2d97577cfea0607e939c0c3847272ca89efbff8bcdc3af9e92136e6e92c344f` |
| P138 | 18 | `df56959c701a939649354b577cd39d6c1f38a8db71802967104c08b9916bd935` |
| P139 | 21 | `a85a4fabd8d98db582fbb31e676773e81005b0cbdb3debe9ca2f909420443e85` |
| P140 | 18 | `c8c2dae58e606b9d184457c46fb1c77d12f9afdc4d49c2377dba21907f6b18d0` |
| P141 | 20 | `bcab71c0cde3cfaeb428f09bbc3b91e1f08a76ce47861e60a9e6bcf5f35d197d` |
| **total** | **97** | **97/97 PASS** |

The five canonical PDF digests are frozen in
`CANONICAL_PDF_MANIFEST.sha256`; it passes 5/5 and has SHA-256
`c4235dba289010c17b29a9c82b01d7f3feae1c673ec768dddbbdb0ab327d8f7c`.

This report certifies internal theorem-package consistency, reproducibility,
ownership framing, and artifact mechanics only.  External release, novelty,
priority, authorship, posting, submission, specialist contact, and every other
external action remain **HOLD**.
