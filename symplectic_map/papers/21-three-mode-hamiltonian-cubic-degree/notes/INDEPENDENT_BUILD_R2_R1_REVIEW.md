# Independent Build R2 Review — Paper 21 Deterministic R1

Verdict: PASS.

## Scope and independence

I acted as a fresh build R2 reviewer, distinct from the build author, the
blocked build-R1 reviewer, and the replacement build-R1 reviewer.  I read the
frozen source and build authorities, the historical blocked-R0 record, the R0
repair build and receipt, the blocking receipt review, the receipt-only
canonical repair, the replacement R1 review, the no-change revision ledger and
receipt, the R1 build authorization, the R1 metadata and receipt, the persisted
outputs, and all four named R0/R1 roots.  The earlier reviews were lineage
evidence only; I independently repeated the byte, JSON, root, log, PDF,
pagination, visual, anonymity, citation, theorem, and scope checks.

I did not rebuild, invoke BibTeX or LaTeX, edit source/build/dashboard files,
use a network, or run CAS, numerical, dataset, or scientific work.  The
paper-compile checklist was used only as a read-only validation framework.
This review note is my sole project write.

## Frozen identities and complete lineage

The unchanged source trio is:

| Artifact | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 84,917 | 1,990 | `34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2` |
| `paper/math_commands.tex` | 981 | 33 | `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a` |
| `paper/references.bib` | 675 | 19 | `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8` |

The build and lineage anchors rehash as follows:

| Artifact | Bytes | LF | SHA-256 / terminal or status |
|---|---:|---:|---|
| `paper/BUILD_METADATA_R0.json` | 2,378 | 1 | `69c67c1485ec95465e522a0d92fea8dcc8ce4d91ed406c39bf57d19563df5e2c` |
| canonical `paper/BUILD_RECEIPT_R0.json` | 7,339 | 1 | `3899ee597562861623bd161a00063fc683f5f998499c677fd7e85e842f1a6e96`; `BUILD_R0_REPAIR_PASS` |
| blocked build review | 7,319 | 148 | `90d4c0ac6aa682dbd1ca0df5d1a3d75c42ba56d2a4df341643db888bf753be1c`; `BUILD_R1_R0_REPAIR_BLOCK` |
| `notes/BUILD_RECEIPT_R0_CANONICAL_REPAIR.md` | 2,168 | 60 | `fefe63317ca10890ba6763bc1fc0dcd3a8c92497caed3ebc454d2704f841e510`; `BUILD_RECEIPT_R0_CANONICAL_REPAIR` |
| replacement build-R1 review | 5,005 | 41 | `62511dd572fa14bdea670df85eb6a48fc54e081a916af5935fdca8f870531bdd`; `BUILD_R1_R0_REPAIR_REPLACEMENT_PASS` |
| `paper/SOURCE_REVISION_RECEIPT_R1.json` | 2,126 | 1 | `441c1cc5e7b3372bbe1d7f05e34ac19461f109bcb0de1e9f7cd4e23db6ba8d42`; `R1_NO_OP_REVISION_PASS` |
| `notes/R1_REVISION_WINDOW_NO_CHANGE.md` | 1,571 | 35 | `0d8e1eed4feb45bd20f90907eb1bddaae42ea7fedd9e34869f24395b20aeaf5f`; `R1_REVISION_WINDOW_NO_CHANGE` |
| `paper/BUILD_METADATA_R1.json` | 1,782 | 1 | `8653c6d500998b9f915958eaa78d818feeb9e93d581c37f9fce86e49aa97b2ab` |
| `paper/BUILD_RECEIPT_R1.json` | 5,380 | 1 | `fa0a511a3391135db75b6eaef03e83fa90930219ddacb8aeaf4713d2aff0bada`; `BUILD_R1_NO_OP_PASS` |

The historical `BUILD_R0_BLOCKER.md` remains
`6b97f1203541b254cd1b0a60c7ed29978e2a500286c0ba1b72dad0712276fada`
and records the distinct 21-page pre-repair source attempt only.  The repaired
R0 authorization and the R1 authorization rehash to `9425a795...` and
`3c295e8c...` and have their required terminal tokens.  Every path/byte/LF/hash
binding reachable from the build metadata and receipts was rechecked against
the live artifact; sixty binding occurrences over twenty-six project paths
produced no mismatch.

The no-op receipt has an empty `changed_paths` array, zero required findings,
zero cosmetic findings, identical `source_before` and `source_after` arrays,
and a one-window ledger with one consumed and zero remaining.  The R1 metadata
binds that exact receipt and the canonical repaired R0 receipt.  Thus the
lineage contains no unrecorded source revision between R0 and R1.

## Strict JSON and the repaired R0 receipt

I strictly parsed all seven project JSON files:

- `experiments/source_lock.json`;
- `experiments/publication_lock.json`;
- `paper/BUILD_METADATA_R0.json`;
- `paper/BUILD_RECEIPT_R0.json`;
- `paper/SOURCE_REVISION_RECEIPT_R1.json`;
- `paper/BUILD_METADATA_R1.json`; and
- `paper/BUILD_RECEIPT_R1.json`.

Each is valid UTF-8, BOM-free, CR-free, NUL-free, one physical line with one
terminal LF, and recursively ordered by ascending Unicode code point.  Compact
serialization with `,` and `:` separators and the declared Unicode handling
reproduces every file byte for byte.  Duplicate-key, `NaN`, `Infinity`, and
`-Infinity` probes are rejected.  All required self-identity byte/hash fields
are null.

I also reconstructed the historical noncanonical R0 receipt entirely in
memory by moving only `underfull_hbox_count` ahead of the two `undefined_*`
keys.  The reconstructed bytes are 7,339 bytes with SHA-256
`48e61f31636c3e70f26da61b74fa9655c22a3ac954b9ae56b877cdebedcd5537`,
and their decoded JSON value is exactly equal to the current receipt.  The first
serialized difference is the recorded zero-based offset 2,595.  Therefore the
canonical repair changed key order only: it did not change a source, root,
output, command, measurement, permission, page fact, or PASS status.

## R1 roots, stable outputs, and R0/R1 equality

The R1 roots named by the receipt are:

- `/tmp/paper21-r1-a.cMLvZF`;
- `/tmp/paper21-r1-b.2D6a87`.

Each root exists and contains exactly thirteen regular mode-0644 files: the
three frozen source inputs, six stable outputs, and four command logs.  There
is no extra entry, directory, or symlink.  Every source file in both roots has
the frozen source identity above.  The corresponding R1 A/B files are
byte-identical, and they also agree byte for byte with both repaired-R0 roots
`/tmp/paper21-r0-repair-a.rai5wu` and
`/tmp/paper21-r0-repair-b.WlpPpd`.

The stable output identities, common to R0, R1, the roots, and the persisted
paper artifacts, are:

| Output | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `main.aux` | 12,760 | 113 | `f203a377a6752a16ae22b61dd9c241a638081da2b7d54141ac62a2ab785d18c6` |
| `main.bbl` | 731 | 20 | `1be6c9b14cae6da54ed8ab04d9739d0bb02ccc363f52ac6ad69b2c2dcf19a1de` |
| `main.blg` | 885 | 46 | `4ef0e5c28c45d31e9cd0f4459679b0a06bfaa2555498a2f87c6b6e68f588d804` |
| `main.log` | 29,049 | 740 | `ac51e35e84d6cb610ccdb79c57cf79a64da91019656c61167fa65fd1e9e33233` |
| `main.out` | 4,090 | 16 | `25820119b32d0994e23555952047c4fe7ddce7a140420b21a1817b9e9141208c` |
| `main.pdf` | 465,922 | 2,539 | `b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3` |

The four command-log identities are likewise common to both R1 roots and both
R0 roots: `18966cdb...`, `7b0a0a8d...`, `fefcab54...`, and `30225d34...` in
the authorized pdflatex/BibTeX/pdflatex/pdflatex order.  The persisted
`main_round0.pdf`, `main_round1.pdf`, and `main.pdf`, together with all four
root PDFs, are all byte-identical at the displayed PDF identity.  The R1
receipt's assertions `root_outputs_byte_identical` and
`r0_r1_all_generated_outputs_byte_identical` are therefore independently
confirmed rather than inferred from the receipt.

## Logs and bibliography

The first command has the expected first-pass undefined cross-references and
citations.  BibTeX then uses exactly the two authorized database entries and
reports `warning$ -- 0`.  The third command has the expected transitional two
citations pending one more pass.  The fourth command resolves them.  The final
persisted/root log has:

- zero fatal errors and zero lines beginning with a TeX error marker;
- zero undefined citations and zero undefined references;
- zero LaTeX, package, changed-label, rerun, or PDF-string warnings;
- zero overfull hboxes or vboxes; and
- exactly seven underfull hboxes and zero underfull vboxes.

The seven underfull boxes occur at the recorded table lines, are explicitly
nonfatal under the authorization, and are visually benign.  The final log ends
normally with `Output written on main.pdf (27 pages, 465922 bytes)`.

## PDF structure, security, fonts, and visual audit

Read-only inspection of the byte-identical PDF establishes:

- PDF 1.5, 27 pages, unencrypted, 465,922 bytes;
- every page is 612 by 792 points (US letter) with rotation zero;
- exact title `Three-Mode Hamiltonian Shears in A6: Exact Degree Growth and Cubic Perron Subfamilies`;
- exact author `Anonymous Authors`;
- creation and modification timestamps exactly `2026-08-22T00:00:00Z`;
- 25 font rows, each embedded, subsetted, and Unicode mapped;
- zero raster images, embedded files, forms, JavaScript, launch actions, rich
  media, XFA, or encryption object;
- one benign catalog open action resolving to an internal `GoTo`; and
- exactly two external URI annotations, both on page 27 and exactly the two
  authorized arXiv URLs.

Ghostscript nullpage rendering succeeds.  All 27 pages were raster-inspected,
with additional high-detail inspection of dense ledger and boundary/reference
pages.  No clipping, overlap, malformed rule or table, corrupt or missing
glyph, wrong rotation, blank page, or other visible rendering defect appears.
Every page contains extracted nonspace text.

Section 8 begins on page 26.  Conclusion prose continues onto page 27 and ends
before the `References` heading; exactly two reference entries follow on that
page.  Thus the substantive body from the abstract through the conclusion ends
on page 27 and satisfies the locked 24--29-page band.  References are excluded
as required, and no appendix or figure changes the count.

## Public theorem, citation, anonymity, and scope

The decoded public text preserves the complete locked statement: an
algebraically closed characteristic-zero field, integer `g >= 8`, the fixed
Hamiltonian shears, the displayed A and B matrices and `C_g=B_gA_g`, exactly
the corrected two selector gaps, the phase recurrence, characteristic-zero
coefficient survival, six-coordinate visibility with q3 as the exact degree
row, the Perron-root equality and strict bound, the cubic characteristic
polynomial, mod-five classes 2/3/4, and `g=7` as a strict-cone boundary rather
than a tie.  The conclusion and anti-claims do not enlarge the theorem.

The body has exactly the two authorized contextual citations.  Blanc--van
Santen is used only for the affine-triangular terminology boundary; Shao--Sun
is used only for dimension-four algebraic-degree context.  The text expressly
disclaims theorem transfer from either.  The auxiliary and bibliography files
contain exactly those two citation keys/bibitems, and the PDF contains exactly
their two authorized URLs.

The public title and anonymous author are exact.  Text, metadata, and object
scans disclose no affiliation, institution, email, ORCID, acknowledgment,
funding, real identity, local path, digest, reviewer/model identity, workflow,
lock, dashboard, build-receipt, venue, or submission provenance.  Searches are
clean for unresolved `??`, `[?]`, `TODO`, `FIXME`, `VERIFY`, `TBD`,
`PLACEHOLDER`, and `XXX` markers.

No JSON, lineage, source-binding, root, determinism, log, bibliography, PDF,
page, font, security, rendering, anonymity, citation, theorem, or scope blocker
was found.  This review records the deterministic R1 build result only and does
not itself authorize a source change, rebuild, release, transport, upload, or
submission.

BUILD_R2_R1_PASS
