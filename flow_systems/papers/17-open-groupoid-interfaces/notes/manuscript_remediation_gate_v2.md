# Paper 17 Freeze-2 to Freeze-3 README trace-remediation gate v2

Gate date: **2026-08-17 (Asia/Shanghai)**  
Gate role: independent exact-byte authorization for one narrow README-only
Freeze-3 repair and two later append-only re-reviews  
Gate verdict: **PASS_TO_ONE_BOUNDED_FREEZE3_README_REPAIR**  
Current candidate state: **HOLD**

```text
TARGET_ABSENT_BEFORE_WRITE=true
GATE_INTERNAL_FINDINGS=C0/M0/m0
INHERITED_CITATION_FINDINGS=C0/M1/m0:OPEN_M04
INHERITED_PEER_FINDINGS=C0/M0/m1:OPEN_W2
DISTINCT_REPAIR_OBJECTS=1
AUTHORIZATION_CONFLICT=false
GATE_VERDICT=PASS_TO_ONE_BOUNDED_FREEZE3_README_REPAIR
THIS_GATE_CLOSES_ANY_FINDING=false
FREEZE3_REPAIR_LANES_AUTHORIZED=1
FREEZE3_REPAIR_WRITE_SET=paper/README.md
TEX_WRITE_AUTHORIZED=false
BIB_WRITE_AUTHORIZED=false
PDF_WRITE_AUTHORIZED=false
BUILD_AUTHORIZED=false
AUTHOR_CONFIRMATION_COMPLETE=false
CANDIDATE_FREEZE_ELIGIBLE=false
RELEASE_AUTHORIZED=false
STANDALONE_PASS=false
```

This gate authorizes a repair; it is not the repair, a review closure, or a
release decision. Citation M-04 and peer W2 remain independently open until
their own fresh append-only re-reviews inspect stable Freeze-3 bytes.

## 1. Fresh rule and authority receipt

Before deciding this gate, the reviewer freshly read the ARS-Codex
academic-research-suite root and the complete directly applicable academic
pipeline, academic-paper-reviewer, peer re-review, integrity-verification,
artifact-trace, visualization, and PDF/VLM verification rules. The reviewer
also reread the full current citation report, peer report, remediation gate
v1, candidate TeX, Bib, and README, and independently inspected the relevant
frozen PDF pages.

The controlling distinctions are exact:

1. a table-object location is not interchangeable with the location of a
   manuscript claim supported by that table;
2. all six trace keys must remain current, and claim text remains primary;
3. a repair authorization does not close a reviewer finding;
4. re-review must preserve the historical report and independently test the
   revised bytes; and
5. any input drift or out-of-scope write fails closed.

## 2. Freeze-2 exact-byte passport

The candidate tuple freshly rehashed as follows:

| Frozen path | SHA-256 | Lines/pages | Bytes | Role in this gate |
|---|---|---:|---:|---|
| `paper/manuscript.tex` | `dc6471b03dbd4e9017909a67ea121000fa6e11172b887aba3cc5e9391d8c9b54` | 351 lines | 37,611 | exact read-only |
| `paper/references.bib` | `d589a945639dd83fe0c24d643fa1900b0da89171a72163e915fdecb6f456ed67` | 42 lines | 1,712 | exact read-only |
| `paper/README.md` | `b12ec948736fd202578204ad2d8c5ea4f58bf1c11b3743cd49fc135df8de40f6` | 168 lines | 15,395 | sole repair surface |
| `paper/paper.pdf` | `0f01b3427cb7c576973e1c451609d132343937b08dc3ae6709d6b385844daf50` | 12 A4 pages | 124,544 | exact read-only |

The current reports and prior authorization also rehashed exactly:

| Authority | SHA-256 | Lines | Bytes | Effective state |
|---|---|---:|---:|---|
| `notes/citation_audit.md` | `6dbeaf377c51b5a4b73678d959e16984d14872f46668d49d826794726ff653b3` | 767 | 38,201 | HOLD `C0/M1/m0`; M-01--M-03 closed, M-04 open |
| `notes/peer_review_round1.md` | `426639bb2b07199942df3424b6e3034acf9f974845081de55466d82f62b440a9` | 808 | 42,377 | MINOR REVISION `C0/M0/m1`; W2 open |
| `notes/manuscript_remediation_gate_v1.md` | `66ccb9bdaa7ce12febfacbc1fab1cc742c85e94e9631fdb385e0ee768454a840` | 613 | 31,329 | historical Freeze-2 authorization |

The citation report's preserved Freeze-1 prefix remains 444 lines and 22,916
bytes at SHA-256
`1237ce87b959315f733584de959620e465a55586a9d5a632506225194a07080a`.
The peer report's preserved Freeze-1 prefix remains 456 lines and 24,453
bytes at SHA-256
`e31fface05a61a811dff52f1eaecead9a8b2405727ac69c758b700e0f223774d`.

## 3. One defect, two independent ledgers

Both final Freeze-2 reviews establish the same exact defect:

- README line 96 locates the T3 table object on PDF page 8;
- README line 164 repeats that T3 is on PDF page 8;
- PDF page 8 contains the TN-12 prose and a forward reference, but no T3
  caption or object;
- PDF page 9 contains `Table 3: Finite-control receipt` and the complete T3
  object; and
- README line 102 correctly locates the supported TN-12 claim across PDF
  pages 8--9, because its prose begins on page 8 and its table appears on
  page 9.

Citation M-04 classifies the hard trace failure as Major; peer W2 classifies
the same localized defect as Minor. That severity-label difference is not an
authorization conflict. Both reports keep the Freeze-2 candidate from PASS,
identify the same two false page statements, prescribe the same README-only
repair, and prohibit changing the correct TN-12 pages-8--9 claim locator.

## 4. Sole Freeze-3 repair contract

Exactly one repair lane may write exactly one retained path:

```text
papers/17-open-groupoid-interfaces/paper/README.md
```

Its write-before precondition is the exact Freeze-2 README identity:

```text
SHA256=b12ec948736fd202578204ad2d8c5ea4f58bf1c11b3743cd49fc135df8de40f6
LINES=168
BYTES=15395
```

The lane must make exactly these two single-character substitutions and no
other change.

### R1 — T3 transformation/object locator

Replace the unique line-96 substring:

```text
current locator manuscript.tex label tab:t3, PDF page 8
```

with:

```text
current locator manuscript.tex label tab:t3, PDF page 9
```

### R2 — visual receipt

Replace the unique line-164 substring:

```text
T3 on page 8
```

with:

```text
T3 on page 9
```

README line 102 must remain byte-for-byte:

```text
    current_manuscript_locator: "Section 6, Finite diagnostic controls; literal TRACE_CLAIM:TN-12; manuscript.tex lines 271--272; table label tab:t3; paper.pdf pages 8--9"
```

All claim IDs, complete claim texts, planned locators, current claim locators,
association cardinalities, marker positions, source hashes, transformation
provenance, caption claims, limitations, and both F1/F2 omission receipts must
otherwise remain byte-for-byte unchanged. No status, declaration, inventory,
prose, punctuation, whitespace, or line-ending change is authorized.

Applying only R1 and R2 deterministically yields:

```text
FREEZE3_README_SHA256=161a7f523c2daf32c6f015c27054e1a1a36192fcf2581158dea1cb5828436ca1
FREEZE3_README_LINES=168
FREEZE3_README_BYTES=15395
```

Any other README identity is outside this gate.

## 5. Exact read-only set and no-build rule

The following three candidate files must remain byte-for-byte exact before,
during, and after R1--R2:

```text
paper/manuscript.tex  dc6471b03dbd4e9017909a67ea121000fa6e11172b887aba3cc5e9391d8c9b54  351 lines  37611 bytes
paper/references.bib d589a945639dd83fe0c24d643fa1900b0da89171a72163e915fdecb6f456ed67   42 lines   1712 bytes
paper/paper.pdf      0f01b3427cb7c576973e1c451609d132343937b08dc3ae6709d6b385844daf50   12 pages 124544 bytes
```

No XeLaTeX, BibTeX, PDF regeneration, isolated build, control execution, or
Route execution is needed or authorized. The unchanged PDF is the object to
which the corrected README must point; overwriting it, even with a visually
equivalent rebuild, invalidates Freeze 3.

Every path other than `paper/README.md` is closed during the repair, including
TeX, Bib, PDF, figures, notes, reports, sources, controls, Route records,
pipeline state, project-root README, release metadata, Git, and public-sync
surfaces.

## 6. Freeze-3 receipt and trace non-regression

After R1--R2, the exact four-file Freeze-3 tuple must be:

```text
FREEZE3_MANUSCRIPT_SHA256=dc6471b03dbd4e9017909a67ea121000fa6e11172b887aba3cc5e9391d8c9b54
FREEZE3_MANUSCRIPT_LINES=351
FREEZE3_MANUSCRIPT_BYTES=37611
FREEZE3_REFERENCES_BIB_SHA256=d589a945639dd83fe0c24d643fa1900b0da89171a72163e915fdecb6f456ed67
FREEZE3_REFERENCES_BIB_LINES=42
FREEZE3_REFERENCES_BIB_BYTES=1712
FREEZE3_README_SHA256=161a7f523c2daf32c6f015c27054e1a1a36192fcf2581158dea1cb5828436ca1
FREEZE3_README_LINES=168
FREEZE3_README_BYTES=15395
FREEZE3_PDF_SHA256=0f01b3427cb7c576973e1c451609d132343937b08dc3ae6709d6b385844daf50
FREEZE3_PDF_PAGES=12
FREEZE3_PDF_BYTES=124544
R1_AUTHOR_REPAIR_COMPLETE=true
R2_AUTHOR_REPAIR_COMPLETE=true
INDEPENDENT_FINDING_CLOSURE=false
```

The repair lane must verify the four object pages as T1=4, T2=6, T3=9, and
T4=10. It must also verify that all four six-key records, twelve active
associations in the `5/4/1/2` pattern, eleven unique literal markers, the
TN-14 T1+T4 dual join, and the two zero-use omission receipts remain exact.
The mathematics, five-work citation graph, owner/source ceilings, bilingual
eight-fact parity, 4-exploratory/3-rejected Route disposition, universal
A2--A4 failure, Route-B false value, diagnostic-only control ceiling, and
nonstandalone Technical-Note ceiling must not change.

## 7. Later append-only closure reviews

Only after the exact Freeze-3 receipt in Section 6 exists may the following
two independent review lanes write:

1. `notes/citation_audit.md` may receive one fresh append-only review. It must
   preserve exactly its current 767-line, 38,201-byte prefix at SHA-256
   `6dbeaf377c51b5a4b73678d959e16984d14872f46668d49d826794726ff653b3`,
   independently rehash the Freeze-3 tuple, re-audit M-04, and regression-test
   the closed M-01--M-03 findings, all four six-key traces, twelve
   associations, source ceilings, and PDF object/claim locators.
2. `notes/peer_review_round1.md` may receive one fresh append-only re-review.
   It must preserve exactly its current 808-line, 42,377-byte prefix at
   SHA-256
   `426639bb2b07199942df3424b6e3034acf9f974845081de55466d82f62b440a9`,
   independently rehash the Freeze-3 tuple, re-audit W2, and check that no
   mathematical, owner, source, trace, Route, or scope regression occurred.

Neither review may edit the candidate, consume the other report as a
substitute for fresh analysis, rewrite any historical prefix, or pre-approve
PASS. Each report may close only its own finding on exact Freeze-3 evidence.
A surviving or new finding yields HOLD/REVISE. Even two zero-finding review
outcomes do not authorize candidate freeze, release, or any further write.

## 8. Administrative and publication stops

The following values remain immutable:

```text
AUTHOR TO CONFIRM=REQUIRED
AUTHOR_CONFIRMATION_COMPLETE=false
CANDIDATE_FREEZE_ELIGIBLE=false
FINAL_ELIGIBILITY=false
RELEASE_AUTHORIZED=false
STANDALONE_PASS=false
TECHNICAL_NOTE=true
PROJECT_ROOT_README_WRITE_AUTHORIZED=false
CONTROL_OR_ROUTE_RERUN_AUTHORIZED=false
PIPELINE_WRITE_AUTHORIZED=false
GIT_MUTATION_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
```

No author identity, affiliation, correspondence, contributor role, funding,
competing-interest, acknowledgment, ethics/consent, repository/archive,
license, or venue-specific AI-use fact may be inferred. Publication status is
not a Route coordinate. Neither an exploratory Route disposition nor a weak
coordinate may be repackaged as full-paper, standalone, analytic, spectral,
determinant, or release credit.

## 9. Fail-closed conditions

Freeze 3 and the later review authorization are invalid if any of the
following occurs:

```text
FREEZE2_INPUT_HASH_DRIFT
ANY_REPAIR_WRITE_OUTSIDE_PAPER_README_MD
README_CHANGE_OTHER_THAN_R1_AND_R2
FREEZE3_README_HASH_NOT_161A7F523C2D
TN12_PAGES_8_9_CLAIM_LOCATOR_CHANGED
ANY_CLAIM_TEXT_ID_LOCATOR_OR_ASSOCIATION_CHANGED
ANY_OTHER_TRACE_KEY_OR_OMISSION_RECEIPT_CHANGED
TEX_BIB_OR_PDF_BYTE_DRIFT
ANY_BUILD_OR_PDF_REGENERATION
ANY_OWNER_SOURCE_CONTROL_ROUTE_OR_STANDALONE_PROMOTION
ANY_HISTORICAL_REVIEW_PREFIX_REWRITE
REVIEW_WRITE_BEFORE_STABLE_FREEZE3
AUTHOR_PLACEHOLDER_INFERRED_OR_RELEASE_FLAG_RAISED
```

## 10. Final authorization receipt

```text
P17_MANUSCRIPT_REMEDIATION_GATE_V2=PASS_TO_ONE_BOUNDED_FREEZE3_README_REPAIR
CURRENT_CANDIDATE_STATE=HOLD
CITATION_M04_REMAINS_OPEN=C0/M1/m0
PEER_W2_REMAINS_OPEN=C0/M0/m1
SOLE_REPAIR_WRITE_SET=paper/README.md
FREEZE3_EXPECTED_README_SHA256=161a7f523c2daf32c6f015c27054e1a1a36192fcf2581158dea1cb5828436ca1
TEX_BIB_PDF=READ_ONLY_EXACT
BUILD_AUTHORIZED=false
POST_FREEZE3_CITATION_REVIEW=APPEND_ONLY_PRESERVE_CURRENT_PREFIX
POST_FREEZE3_PEER_REVIEW=APPEND_ONLY_PRESERVE_CURRENT_PREFIX
RELEASE_AUTHORIZED=false
CANDIDATE_FREEZE_ELIGIBLE=false
STANDALONE_PASS=false
THIS_FILE_SHA256=EXTERNAL_BY_CONSTRUCTION
THIS_FILE_LINES=EXTERNAL_BY_CONSTRUCTION
THIS_FILE_BYTES=EXTERNAL_BY_CONSTRUCTION
```
