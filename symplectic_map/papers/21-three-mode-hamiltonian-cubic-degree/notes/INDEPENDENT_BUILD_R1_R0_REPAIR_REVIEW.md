# Independent Build R1 Review — Paper 21 R0 Repair

Verdict: BLOCK.

## Scope, independence, and bound identities

I acted as a fresh build R1 reviewer.  I read the paper plan, source and
publication locks, publication-stage scope, historical R0 blocker,
proof-first source-repair ledger, both fresh repair-source reviews, and the
repair-build authorization.  I audited the persisted build products and both
temporary roots named by the receipt.  I did not rebuild, invoke BibTeX,
change source, build, or dashboard artifacts, or use the network.  This note is
the only persisted project write of this review.

The current identities are:

| Artifact | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 84,917 | 1,990 | `34074c5965086d79145bf2b273398c4c17fdc264b6f5e3555fd1b9a2bd27c7b2` |
| `paper/math_commands.tex` | 981 | 33 | `05c80b105ba2942d66aa6e717bbe15f24511abcdbcc5480daffd899f1622087a` |
| `paper/references.bib` | 675 | 19 | `4f1c68133d959ce3377707775830748f1301d082a70c0787c23ae7da183590b8` |
| repair-source R1 review | 6,040 | 110 | `07114e0da0eb41ed827f86064186639ffed49c2be2db97bf3e016d7390fface0` |
| repair-source R2 review | 10,290 | 299 | `3b606a9481811d795dd7fe5ebb16bf280898f56748e61045f8b802de0b063a3a` |
| `paper/BUILD_METADATA_R0.json` | 2,378 | 1 | `69c67c1485ec95465e522a0d92fea8dcc8ce4d91ed406c39bf57d19563df5e2c` |
| `paper/BUILD_RECEIPT_R0.json` | 7,339 | 1 | `48e61f31636c3e70f26da61b74fa9655c22a3ac954b9ae56b877cdebedcd5537` |
| `paper/main.pdf` | 465,922 | 2,539 | `b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3` |
| `paper/main_round0.pdf` | 465,922 | 2,539 | `b02785a088008c3938652c28857347246dbf15e800d71269be7fdcd987e65fe3` |

The two source-review terminal tokens are respectively
`PAPER_SOURCE_R1_R0_REPAIR_PASS` and
`PAPER_SOURCE_R2_R0_REPAIR_PASS`.  The build authorization has the recorded
identity `9425a795...` and its final Markdown code token is
`BUILD_AUTHORIZATION_R0_REPAIR`.

## Blocking strict-JSON defect

`BUILD_RECEIPT_R0.json` declares that object keys are recursively ordered by
ascending Unicode code point and that its compact canonical representation
uses separators `,` and `:` with exactly one terminal LF.  Independent parsing
rejected duplicate keys and nonfinite numbers and confirmed UTF-8, no BOM, no
CR, no NUL, one physical line, one terminal LF, and null self-identity fields.
Nevertheless, byte-exact canonical round-trip fails.

The sole key-order violation is in `$.checks`.  The persisted order near the
end of that object is:

```text
root_outputs_byte_identical,
underfull_hbox_count,
undefined_citation_count,
undefined_reference_count
```

Ascending Unicode order requires:

```text
root_outputs_byte_identical,
undefined_citation_count,
undefined_reference_count,
underfull_hbox_count
```

The first canonical byte difference is at zero-based byte offset 2,595.  The
receipt's SHA-256 correctly identifies its persisted bytes, but a correct hash
of noncanonical bytes does not satisfy the receipt's own strict canonicalization
contract.  By contrast, `BUILD_METADATA_R0.json`, `source_lock.json`, and
`publication_lock.json` each parse strictly and round-trip byte for byte under
the same compact recursively sorted representation.  Both build JSON files
also have the required null `bytes` and `sha256` self-exclusion fields.

Because strict JSON verification was a conjunctive part of this review, the
noncanonical receipt is a build-gate blocker.

## Binding and deterministic-output checks that pass

Every metadata binding resolves to the current exact bytes: the source trio,
paper plan (`63a7de86...`), source lock (`41f350ca...`), publication lock
(`14966ffc...`), and both repair-source reviews.  Every receipt authorization,
source, metadata, historical-blocker, and generated-output path also has the
recorded byte count, LF count, mode where specified, and SHA-256.

The named roots
`/tmp/paper21-r0-repair-a.rai5wu` and
`/tmp/paper21-r0-repair-b.WlpPpd` both remain present.  In each root the three
source inputs match the frozen source identities.  The listed `main.aux`,
`main.bbl`, `main.blg`, `main.log`, `main.out`, `main.pdf`, and four command
logs all match their receipt snapshots.  Each corresponding listed file is
byte-identical between roots A and B.  The persisted generated outputs match
the root outputs, and `main.pdf`, `main_round0.pdf`, and both root PDFs are
byte-identical.

The four command logs show the authorized sequence.  Expected first-pass
reference warnings and third-pass citation warnings are resolved by the final
pass.  The persisted final log has:

- zero fatal errors;
- zero LaTeX or package warnings;
- zero undefined references or citations;
- zero changed-label or hyperref PDF-string warnings;
- zero overfull boxes; and
- exactly seven underfull boxes, which the authorization makes nonfatal.

The BibTeX log records exactly two used entries and zero warnings.

## PDF, pagination, and public-scope checks that pass

Both persisted PDFs are valid 27-page, PDF-1.5, unencrypted letter-size files,
with zero rotation on every page.  Ghostscript nullpage rendering exits zero.
Metadata is exact:

- title: `Three-Mode Hamiltonian Shears in A6: Exact Degree Growth and Cubic Perron Subfamilies`;
- author: `Anonymous Authors`;
- creation and modification time: `2026-08-22T00:00:00Z`.

There is no affiliation, email, ORCID, acknowledgment, funding identity, or
private workflow provenance in extracted public text or metadata.  The PDF has
no encryption, JavaScript, forms, embedded files, raster images, launch action,
rich media, or XFA content.  All 25 font rows are embedded, subsetted, and
Unicode mapped.  The only external URL annotations are the two authorized
arXiv records.

Pagination is exact.  Section 8 starts on page 26.  Its conclusion continues
to and ends on page 27, where the References heading and exactly two entries
then begin.  Thus the substantive body through the conclusion occupies page
27 and satisfies the locked 24--29 page band; the references are excluded as
required.  No page is blank.

Extracted theorem text preserves the algebraically closed characteristic-zero
field, integer `g >= 8`, fixed two shears, `C_g=B_gA_g`, the corrected two
selector gaps, phase recurrence, exact visible `q_3` degree row, Perron bound,
cubic characteristic polynomial, mod-five classes `2,3,4`, and the `g=7`
strict-cone boundary.  The anti-claims remain bounded.  The two body citations
are Blanc--van Santen and Shao--Sun in contextual roles only, and the two
bibliography entries and two arXiv URLs resolve accordingly.  Searches find no
unresolved `??`, `[?]`, `TODO`, `FIXME`, `VERIFY`, `TBD`, placeholder,
undefined-reference text, or build/reviewer/model/lock provenance marker.
Ordinary prose uses of “verify” are not unresolved markers.

## Required disposition

The PDF and deterministic outputs are otherwise blocker-free, but this review
cannot grant build R1 PASS while the bound receipt contradicts its declared
canonical key-order rule.  A separately authorized correction must serialize
the receipt in true recursive Unicode order, establish its new identity, and
receive fresh review.  This note authorizes neither that correction nor a
rebuild, release, transport, upload, or submission.

BUILD_R1_R0_REPAIR_BLOCK
