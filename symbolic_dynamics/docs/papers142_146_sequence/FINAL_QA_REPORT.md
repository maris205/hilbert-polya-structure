# Final QA report — P142–P146

**Checkpoint:** 2026-09-01 UTC.
**Result:** **5/5 PASS INTERNAL; FINAL FREEZE; EXTERNAL HOLD**.

| paper | pages | bytes | canonical exact control | internal gate | fonts | visual pages |
|---:|---:|---:|---:|---|---:|---:|
| P142 | 5 | 373,966 | 319,074 | `GO_INTERNAL`, cosmetic-lift risk | 28/28 | 5/5 |
| P143 | 4 | 334,898 | 13,503,895 | `GO_INTERNAL / OWNER_THIN` | 25/25 | 4/4 |
| P144 | 6 | 328,424 | 6,005,502 | `GO_INTERNAL / OWNER_THIN` | 22/22 | 6/6 |
| P145 | 5 | 395,143 | 155,901 | `GO_INTERNAL AFTER OWNER REPAIR` | 30/30 | 5/5 |
| P146 | 3 | 345,511 | 9,562 | `GO_INTERNAL / OWNER_THIN` | 26/26 | 3/3 |
| **total** | **23** | **1,777,942** | **19,993,934** | **5/5** | **131/131** | **23/23** |

## Exact replay and isolated compilation

The final cold replay invoked:

1. `verify_p142.py`;
2. `verify_p143.py`;
3. the independent `verify_p143_embeddings.py`;
4. `verify_p144.py`;
5. `verify_p145.py`; and
6. `verify_p146.py`.

Every process exited zero and its raw stdout matched the frozen transcript
byte for byte.  Transcript SHA-256 values are:

| paper/lane | transcript SHA-256 |
|---|---|
| P142 | `038c6655f517df31e0ecfbba257823169619347fd1b3d27354cdd3dc428f7fa1` |
| P143 main | `9643e4a8a069c58cdb1a9772a0ad341b85d844a43597b2c3e65450a4ba46938c` |
| P143 independent | `dabdbd7cb891838ef8049f79460c3e5213137f4ad1d62e7377bf3d61989a47fe` |
| P144 | `c9f7c02c4dcbe598ad4b0b8ed260256bd808987d7369cf8a300ef1f8ca046294` |
| P145 | `89aaeddaa2cfc8c66a1d05681e3ef3115f7b13bca665a894b1a48aa2f5df92d9` |
| P146 | `a4ff48a09eba036b82473f01ee5aece03a9f92fc5188735aeb08c22b83545e48` |

Final source-only build directories were:

```text
/tmp/p142-final-TeEueW
/tmp/p143-final-y8Pu4L
/tmp/p144-final-zDPch5
/tmp/p145-round2-9YbxQk
/tmp/p146-final-7X79f2
```

Every four-stage build exited zero and its PDF is byte-identical to the
corresponding canonical `main.pdf`.  Settled logs have no undefined citation
or reference, multiply defined label, bad box, or rerun request.  P146 retains
one deterministic pdfTeX font-expansion ordering notice; repeated byte-
identical builds and page inspection confirm that it is harmless.

## Historical-round integrity

Every paper preserves `main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf`; all 15 historical PDFs are mode `0444`.

- P142 has three distinct review-stage PDF hashes; current equals Round 2.
- P143's repaired Round 1, accepted Round 2, and current PDF are identical;
  its pre-source-repair Round 0 is distinct.
- P144 preserves a five-page Round 0 and six-page owner-repaired Round 1;
  current equals the final Round 2.
- P145 preserves the four-page pre-owner-hit Round 0, the five-page owner-
  repaired Round 1, and a distinct final Round 2.
- P146 preserves the visibly defective Round 0, repaired Round 1, and final
  Round 2 with the paper-visible fourth owner source.

## Bibliography, PDF, text, and visual gates

Bibliography closure is 3/3, 5/5, 7/7, 6/6, and 4/4: **25/25 entries** are
cited and resolved.  The corrected Katona--Nagy DOI, Pallo/Chapoton locators,
folded-hypercube owners, Björner--Wachs DOI, and Coronado--Pons--Riera analogue
are visible in the appropriate final artifacts.

All five PDFs are A4, rotation zero, version 1.5, unencrypted, form-free,
JavaScript-free, attachment-free, and have blank Title, Author, Subject, and
Keywords metadata fields.  No PDF has a metadata stream.  Every visible
byline is `Anonymous`.

All **131/131 font rows** are embedded, subsetted, and Unicode-mapped.  Fresh
layout-preserving extraction contains **89,961 bytes**, **12,095 words**, and
**1,242 lines**; every page contains searchable text.  Scans find no unresolved
reference, placeholder, local filesystem path, email address, ORCID,
affiliation, correspondence, acknowledgement, funding statement, identity
leak, or draft marker.  Each manuscript visibly retains its external-hold or
equivalent release boundary.

All **23/23 final pages** were rasterized at 144 dpi and inspected.  Titles,
anonymous bylines, abstracts, theorem statements, proofs, equations, tables,
owner boundaries, limitations, conclusions, and references are legible.  No
page has clipping, overlap, missing glyphs, malformed display, truncated
reference, unintended blank content, or rotation.

## Integrity gate

Paper-local `SHA256SUMS` manifests pass entry by entry:

| paper | entries | manifest SHA-256 |
|---:|---:|---|
| P142 | 20 | `da65fcb0b1d062622a6545a286eaae886bbe4a466d9b9171d176cdc986b744a6` |
| P143 | 22 | `f1b96365c82bac6f14a6e295dfafb06978981f8391bbedcb008f4137a6a9db12` |
| P144 | 20 | `f75ae227070c6d6948fdfb0fcbbd7853d3bf7f57708515fe4fc16816246fbcc3` |
| P145 | 20 | `04b560f5e10ad294ad970622b5e52265ec6a4f302b5115ae451937a0b14986c8` |
| P146 | 20 | `df68a8cfccced194915ceaf31495d566eb7eb31226ef519869e9ffbc3a5cb7da` |
| **total** | **102** | **102/102 PASS** |

The five canonical PDF digests are frozen in
`CANONICAL_PDF_MANIFEST.sha256`; it passes 5/5 and has SHA-256
`7549f432ac0b40ee2d09ce37141b969185bda1c2abacd29e95ceff8bdf47fc3d`.

This report certifies internal theorem-package consistency, reproducibility,
ownership framing, and artifact mechanics only.  External release, novelty,
priority, authorship, posting, submission, specialist contact, and every other
external action remain **HOLD**.
