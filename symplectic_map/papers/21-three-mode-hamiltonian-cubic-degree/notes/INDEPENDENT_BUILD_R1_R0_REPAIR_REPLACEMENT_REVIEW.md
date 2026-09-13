# Independent Replacement Build R1 Review — Paper 21 R0 Receipt Repair

Verdict: PASS.

## Independence and scope

I acted as a fresh replacement build reviewer, distinct from the blocked-build reviewer and build author. I read the repaired receipt, canonical-repair ledger, metadata, authorization, locks, repair-source reviews, historical blocker, persisted outputs, and both recorded roots. The earlier `90d4c0ac...` BLOCK review was historical evidence only. I did not rebuild, invoke BibTeX, edit source/build/dashboard artifacts, use CAS/numerical code or the network, or create any external effect. This note is my sole project write.

## Repaired receipt and canonical JSON

| Artifact | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/BUILD_RECEIPT_R0.json` | 7,339 | 1 | `3899ee597562861623bd161a00063fc683f5f998499c677fd7e85e842f1a6e96` |
| `notes/BUILD_RECEIPT_R0_CANONICAL_REPAIR.md` | 2,168 | 60 | `fefe63317ca10890ba6763bc1fc0dcd3a8c92497caed3ebc454d2704f841e510` |
| `paper/BUILD_METADATA_R0.json` | 2,378 | 1 | `69c67c1485ec95465e522a0d92fea8dcc8ce4d91ed406c39bf57d19563df5e2c` |

I strictly parsed and canonical-round-tripped the receipt, build metadata, source lock, and publication lock. Each is UTF-8, BOM/CR/NUL-free, LF-terminated, recursively Unicode-code-point sorted, and reproduced byte for byte using compact `,`/`:` separators and one terminal LF. Duplicate-key, `NaN`, `Infinity`, and `-Infinity` probes were rejected. The required null self-identity fields remain null.

I independently reconstructed the previous noncanonical receipt by changing only the stated four `checks` key positions. It is 7,339 bytes and hashes to `48e61f31636c3e70f26da61b74fa9655c22a3ac954b9ae56b877cdebedcd5537`; its decoded JSON value equals the repaired receipt. Therefore the repair changed only serialization order, not a measured value, source, output, root, command, page fact, permission, or status.

## Bindings and deterministic outputs

- Every receipt authorization, historical-blocker, source, metadata, and review binding rehashes with its recorded byte count, LF count, and SHA-256. Both repair-source reviews have their required terminal PASS tokens.
- The source trio is unchanged: `main.tex` is `34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2` (84,917 B/1,990 LF), `math_commands.tex` is `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a`, and `references.bib` is `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8`.
- Each of the seven persisted output records matches its byte count, LF count, SHA-256, mode, and regular-file status.
- Both declared temporary roots remain readable. All ten declared snapshot entries in each root match exactly, and every corresponding A/B output and command-log hash agrees.
- `main.pdf`, `main_round0.pdf`, and both root PDFs are byte-identical: 465,922 bytes, SHA-256 `b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3`.

## Build, PDF, and public-scope audit

- The command logs show the authorized four-command pdflatex/BibTeX/pdflatex/pdflatex sequence. First/third-pass reference and citation diagnostics are transitional; the final log has zero fatal errors, undefined citations/references, changed-label warnings, package/LaTeX warnings, hyperref warnings, and overfull boxes. Seven underfull boxes are recorded and explicitly nonfatal.
- Read-only PDF inspection confirms PDF-1.5, letter size, 27 pages, zero rotation, no encryption, and successful Ghostscript nullpage rendering. Metadata title and author are exactly locked, with the fixed 2026-08-22 timestamp.
- All 25 font rows are embedded, subsetted, and Unicode mapped. There are no embedded files, raster images, forms, JavaScript, launch actions, rich media, or XFA. The only URL annotations are the two authorized arXiv URLs.
- Section 8 begins on page 26; the conclusion ends on page 27, where References begins with exactly two entries. The substantive body therefore ends on page 27, within the locked 24–29 page band, and no blank page appears.
- Decoded text preserves the fixed characteristic-zero `g >= 8` theorem, two shears, `C_g=B_gA_g`, phase-aware selector gaps, cone/carry proof, q3 degree row, Perron bound, characteristic polynomial, mod-5 classes 2/3/4, and g=7 boundary. The anti-claims remain bounded.
- The PDF text and metadata preserve anonymity and contain no identity, affiliation, email, ORCID, acknowledgment, funding, local path, digest, reviewer/model/lock/workflow provenance, or unresolved marker. Blanc--van Santen and Shao--Sun are the two citations and remain contextual only.

The prior sole blocker was the receipt's noncanonical key ordering. That defect is repaired; all receipt, source, determinism, log, PDF, page, font, security, anonymity, citation, theorem, and permission checks pass. This PASS does not authorize a new source edit, build, release, transport, upload, or submission without separately granted authority.

BUILD_R1_R0_REPAIR_REPLACEMENT_PASS

