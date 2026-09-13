# Paper 13 Independent Draft-Integrity Review

**Candidate:** `henon_primitive_cycle_cover_v1`  
**Date:** 2026-08-16 UTC  
**Reviewed manifest:** `paper/DRAFT_ARTIFACT_MANIFEST.json`  
**Manifest SHA-256:** `a4ff87715f0849c039764be2bf5bce4880d2214551d02cc455c003edc860665e`  
**Manifest bytes:** 15,322

## 1. Independence, authority, and zero-expansion method

I did not author the draft artifact manifest, the bounded Round-1 revision,
the revised manuscript sources, either build receipt, or either preserved PDF
snapshot.  I performed this review only after the exact Round-2 review at
SHA-256
`10e7e5ef1ca92a348c70495bb9c631e02af055c27c017d219e46736d35a028fd`
ended with its required manuscript-review verdict.

I read exactly the 31 pre-existing paths in the final publication lock's
`integrity_roles.allowlist`.  The manifest contains 30 artifact entries and is
the thirty-first allowed path.  I did not read any unlisted project content,
reviewer-only governance input, code, preexecution or runtime path, external
source, or other paper.  I used no network access.  I did not compile LaTeX or
BibTeX, invoke R100 or a scientific engine, recompute mathematics, edit the
manuscript, or modify a build output.  Before this file was created, its path
was absent.  This review file is the sole write performed by this role.

## 2. Manifest and canonical-JSON audit

The manifest has schema `P13_DRAFT_ARTIFACT_MANIFEST_V1`, is exactly one
newline-terminated JSON line, and is strict UTF-8.  A duplicate-key-detecting
parse found zero duplicate keys and zero nonfinite values.  Recursive key
sorting followed by compact JSON serialization reproduced its exact 15,322
bytes, including the single final newline.

The same strict parse and exact canonical-byte regeneration passed for all
five pre-existing canonical JSON objects declared by the manifest:

| Path | Canonical result |
|---|---|
| `experiments/manuscript_lock.json` | exact sorted compact JSON; one final newline |
| `experiments/publication_lock.json` | exact sorted compact JSON; one final newline |
| `paper/BUILD_RECEIPT_R0.json` | exact sorted compact JSON; one final newline |
| `paper/BUILD_RECEIPT_R1.json` | exact sorted compact JSON; one final newline |
| `results/INDEPENDENT_RESULT_REVIEW.json` | exact sorted compact JSON; one final newline |

The manifest's 30 artifact paths are unique and lexicographically ordered.
Together with the manifest path, their set equals the 31-entry integrity
allowlist exactly.  Every path is relative, normalized, nonescaping, and has
no empty, `.`, or `..` component.  The manifest is excluded from its own
artifact entries and excludes its own byte count and SHA-256; it appears only
as the inventory path.  Its exact bytes do not contain its external SHA-256.

## 3. Independent 30-artifact receipt

I recomputed the byte count and SHA-256 of every artifact immediately before
writing this review.  All 30 bindings matched:

| Path | SHA-256 | Bytes |
|---|---|---:|
| `experiments/manuscript_lock.json` | `488c257f377de1cbc94855041c3e7930cbab3fdf1d390a310684a8fc9b0344cd` | 9,154 |
| `experiments/publication_lock.json` | `5fd33a907d4b324c6b56fdb3b70af1315475f44f077d27ba84a17653514a69cb` | 22,380 |
| `notes/CITATION_VERIFICATION.md` | `08d310cb4c5b8e14810bf06e79e988ecf28b9ef2825868b7f7edfeccdce0e71b` | 27,784 |
| `notes/CLAIMS_EVIDENCE_MATRIX.md` | `21537ed1ed04abf7e3e1dc7d089a105fc36eb5815d164e1cae840f8c56464890` | 13,041 |
| `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R1.md` | `aaa77a37a8d8a8fccedd18073f346312b1ea0245447bbf1b0f5c60095809848c` | 22,525 |
| `notes/INDEPENDENT_MANUSCRIPT_REVIEW_R2.md` | `10e7e5ef1ca92a348c70495bb9c631e02af055c27c017d219e46736d35a028fd` | 17,090 |
| `notes/INDEPENDENT_PUBLICATION_STAGE_REVIEW.md` | `a1213f19a6da5531f411e3a7c63ef0f746a6577f021dd360cfc874463b8dec1c` | 19,231 |
| `notes/INDEPENDENT_RESULT_AWARE_HANDOFF_REVIEW.md` | `3df02be2a4a629d9eeab89b9fe3cd30dc47892729603205d308ab6b9f5320e98` | 15,574 |
| `notes/INDEPENDENT_SOURCE_LOCK_REVIEW_R2.md` | `83b380d5fa1d5e2161281052ea69b447f6c26831f0cf0d818eced8affecd6c8e` | 15,344 |
| `notes/MANUSCRIPT_REVISION_R1.md` | `44f081e3f9497c460ed3101dee5b7ba007bfe6022ded1abe8e0391202b8e2725` | 6,120 |
| `notes/NOVELTY_ASSESSMENT.md` | `bde37eb93989989d2c55c81b13c6919a9ba367c6f2d7ca2320335fd0df155c6a` | 20,383 |
| `notes/PROOF_PACKAGE.md` | `9b1fd6a4e262d7b4dc0df4456e58b1af3b78be63a58014860679d992f71dd6d9` | 25,766 |
| `notes/PUBLICATION_STAGE_SCOPE.md` | `17f56f7f12333803bc8b27a22e27bc33535dbf777483d8da22f34dee17b04e72` | 25,352 |
| `notes/RESEARCH_QUESTION.md` | `18ccf35df9b0f3b73636044c9400f3d79e8f213af365fb33504fa3524f6fd287` | 12,301 |
| `notes/RESULT_AWARE_MANUSCRIPT_SCOPE.md` | `265fd1539d4957a78422c641c9508a432d769389fe7f78fb3cc5fdbf7c8b0307` | 16,992 |
| `paper/BUILD_RECEIPT_R0.json` | `1e05beda50a07fc120c40d4568aa54f9bf51b4c212682b3248a30efb78c38548` | 4,942 |
| `paper/BUILD_RECEIPT_R1.json` | `5480ab22ebc7c9676395f9309baae15aa406f73f0cfa3e4901f288fb3e94ca51` | 5,445 |
| `paper/PAPER_PLAN.md` | `3dd625590a16e0fe64f475e5913a3d5f1b9eac9b2883e136f389c049ae5d0911` | 39,066 |
| `paper/figures/architecture.tex` | `eabb9c99296c39a3744a57aaa7484522d20175e42dc7577a6e658dc732fed9b9` | 3,185 |
| `paper/main.aux` | `dcd56fb868640a1207f8f7c2c9d9b9b3d9de460078b89098e0d934c28ddb7592` | 16,780 |
| `paper/main.bbl` | `1664a96990b3415b471194395b4d4e0d37ccb318013f50bf0e41cd0cd4dd1c9d` | 8,037 |
| `paper/main.blg` | `401ed26512f413fbdbfab267da368164e702c87c2a425eb8afc92f08a2d2a61c` | 918 |
| `paper/main.log` | `998ff0432beb546b56300d41a6a7b5295265de217127c0232a2b1b88b50e9c7b` | 38,628 |
| `paper/main.out` | `838757a680eeb5ef6b3115a65e94801212acb9659c8ae2465e3184db40920af0` | 12,541 |
| `paper/main.pdf` | `4f69c395ffc06c3d3282c09127a520385ff741428cea7083cb1a7618e347df09` | 519,969 |
| `paper/main.tex` | `f62f72ad129bc371d0e76d1daf48b0a2df82cf60d0d1e750d6c0f049047539ce` | 80,689 |
| `paper/main_round0.pdf` | `f9bb3e4c08215e91d0baf3e278ee1802b88a1d77c8e08515b61b51fb5850118d` | 517,616 |
| `paper/main_round1.pdf` | `4f69c395ffc06c3d3282c09127a520385ff741428cea7083cb1a7618e347df09` | 519,969 |
| `paper/references.bib` | `005edd30410ffd8b9b9851e9008636aed9bcddba3195af550bd6daed0529a19b` | 8,175 |
| `results/INDEPENDENT_RESULT_REVIEW.json` | `a5d1d3df1ed5e6e34d16aa50b86f5028c4ea86a655492794f0c58d8febcae23a` | 4,462 |

## 4. Inventory, symlink, and path-closure audit

The top-level `paper/` inventory has exactly the 15 declared entries.  Its
tree has exactly 15 regular files: the 14 declared top-level files plus the
single `paper/figures/architecture.tex` file.  The figures directory has
exactly that one entry.  There is no unlisted build output, extra figure,
temporary file, cache, standalone visual, or unexpected directory entry.

No artifact path, path ancestor, `paper/` tree entry, or figures entry is a
symlink.  The project root resolves physically to itself.  The mistakenly
broader workspace-root path `/root/autodl-tmp/symplectic_map/paper` is absent.
The independent review path was absent before this write.  The manifest's
inventory counts, zero-symlink count, and empty unexpected-entry lists all
match these independent checks.

## 5. Review, revision, and build DAG

The review/revision DAG is closed and contains exactly one revision cycle:

1. The Round-1 review at SHA-256
   `aaa77a37a8d8a8fccedd18073f346312b1ea0245447bbf1b0f5c60095809848c`
   required one bounded revision.
2. The revision receipt at SHA-256
   `44f081e3f9497c460ed3101dee5b7ba007bfe6022ded1abe8e0391202b8e2725`
   records `R1_BOUNDED_REVISION_COMPLETE`, exactly one revision round, the
   revised source bindings, and no compilation or scientific execution by
   the revision role.
3. The canonical Round-1 build receipt at SHA-256
   `5480ab22ebc7c9676395f9309baae15aa406f73f0cfa3e4901f288fb3e94ca51`
   binds every current revised source and every current generated output.
4. The exact Round-2 review named above terminates with the required review
   verdict and states that no required change remains.  No post-Round-2
   revision is authorized or present.

The Round-0 receipt remains canonical at SHA-256
`1e05beda50a07fc120c40d4568aa54f9bf51b4c212682b3248a30efb78c38548`,
and its preserved snapshot remains
`f9bb3e4c08215e91d0baf3e278ee1802b88a1d77c8e08515b61b51fb5850118d`.
The Round-1 receipt binds both preserved Round-0 objects exactly.  Both build
receipts record two byte-identical clean builds, the locked command sequence
and environment, and no Biber, `latexmk`, shell escape, or networked tooling.

Every current Round-1 source and output hash matches the Round-1 receipt.
`paper/main.pdf` and `paper/main_round1.pdf` are byte-identical, each with
SHA-256
`4f69c395ffc06c3d3282c09127a520385ff741428cea7083cb1a7618e347df09`
and size 519,969 bytes.  The terminal current PDF is therefore the reviewed
Round-1 snapshot, not the historical Round-0 PDF.

## 6. Sealed PDF, source, and build-quality checks

Read-only inspection of the sealed current PDF and its exact Round-1 logs
agrees with the receipt and Round-2 review:

- The PDF is A4, unencrypted, and has 27 nonempty pages.  The References
  heading begins on page 26, giving 25 mathematical-content pages and two
  reference pages.
- The public title is exactly *Normalized Primitive-Cycle Covers in a
  Degenerating Hénon Family*.  The byline is `Anonymous Authors` exactly
  once.
- PDF Author, Subject, and Keywords are empty.  CreationDate and ModDate are
  absent.  Creator and Producer are only `pdfLaTeX` and `pdfTeX`.  There is
  no custom metadata stream, JavaScript, form, encryption, or embedded file.
- All 30 fonts are embedded, subset, and Unicode-mapped.  The PDF contains no
  raster image; the architecture figure is vector TikZ content.
- The final LaTeX log has zero TeX errors, undefined references, undefined
  citations, multiply-defined labels, overfull boxes, underfull boxes, or
  missing glyphs.  It contains exactly the eight preserved, nonblocking
  hyperref PDF-string token warnings.  The BibTeX log has zero warnings and
  records 26 entries.
- Extracted public text has one anonymous byline and one bounded
  `RESULT_PASS` occurrence.  It has no email, ORCID, acknowledgment, funding
  text, local path, 64-hex hash, R100 identifier, internal workflow token,
  drafting marker, replacement character, or null byte.
- The source has eight numbered main sections followed by Appendices A--C.
  It contains exactly one figure environment, one architecture input, and
  one exact locked non-evidence caption; it has zero table or tabular
  environments and zero `includegraphics` use.  The diagram source has no
  raster or external-asset reference.

These are artifact and reproducibility checks only.  No PDF, receipt, log,
manifest, or machine result is treated as mathematical evidence.

## 7. R100 firewall and terminal authority

The final publication lock keeps the registered count at one, rerun false,
and invocation unauthorized.  The sole allowed result-review JSON has exact
verdict scope `BOUNDED_IMPLEMENTATION_CONSISTENCY_ONLY`, records zero reviewer
registered-entry invocations and zero scientific recomputations, and denies
machine-proof, theorem-validation, and scientific-truth authority.  The
article's sole public result reference is confined to the required Section 8
same-family paragraph and expressly has no proof role.  No runtime content or
scientific engine was accessed in this review.

All integrity checks above are exact and no drift, missing artifact, extra
artifact, malformed JSON, duplicate key, nonfinite value, path escape,
symlink, inventory expansion, review-DAG break, build-DAG break, PDF mismatch,
metadata leak, identity clue, visual expansion, warning regression, R100
promotion, finalization authority, or submission authority was found.

**Verdict effect:** `ANONYMOUS_REVIEWED_DRAFT_INTEGRITY_ONLY_NOT_FINALIZATION_OR_SUBMISSION`

**Final canonical verdict:** `DRAFT_INTEGRITY_PASS`
