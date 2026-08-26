# Paper 17 independent post-candidate citation and claim-reference audit

Audit date: **2026-08-17 (Asia/Shanghai)**  
Reviewer role: independent exact-byte post-candidate citation,
claim/reference, artifact-trace, build, and PDF-visual reviewer  
Effective verdict: **HOLD — `C0/M3/m0`**  
Candidate ceiling: **nonstandalone Technical Note review candidate only**  
Release status: **not authorized**

```text
POST_CANDIDATE_CITATION_AUDIT_COMPLETED=true
FROZEN_INPUT_HASH_DRIFT=0
BIBLIOGRAPHY_ENTRIES=5
DISTINCT_CITED_KEYS=5
CITATION_ORPHANS=0
BIBLIOGRAPHY_ORPHANS=0
WORK_IDENTITY_METADATA_PASS=5_OF_5
WORK_CLAIM_CEILING_FULL_PASS=3_OF_5
MOERDIJK_VISIBLE_TECHNICAL_CITATION_OR_BIB_ENTRY=false
FORSSELL_VISIBLE_WORK_COUNT=1
TN_CLAIM_OWNER_ROWS_FULL_PASS=13_OF_15
TRACE_RECORDS_WITH_SIX_KEYS_PRESENT=4_OF_4
TRACE_RECORDS_WITH_COMPLIANT_CLAIM_TEXT_PRIMARY_ARRAY=0_OF_4
DISTINCT_TRACE_MARKERS=11
ACTIVE_TABLE_ASSOCIATIONS=12
FIGURE_BRANCH=BOTH_OMITTED
BILINGUAL_FACT_PARITY=8_OF_8
CLEAN_ISOLATED_BUILD=true
PDF_PAGES_VISUALLY_CHECKED=12_OF_12
EFFECTIVE_FINDINGS=C0/M3/m0
AUTHOR_TO_CONFIRM_IS_TECHNICAL_CITATION_FINDING=false
CANDIDATE_FREEZE_ELIGIBLE=false
RELEASE_AUTHORIZED=false
```

The five-work bibliography graph is structurally closed, but structural
closure is not a claim-faithfulness pass. Two local-owner citation contexts
exceed or misdescribe their frozen source ceilings, and all four current
table traces replace the required claim-text-primary arrays with bare TN
identifiers. The candidate therefore does not pass this audit. The unresolved
author/declaration fields are recorded separately in Section 10; they are not
used to inflate or dilute the technical finding count.

## 1. Review method and ARS rule receipt

Before judging the candidate, the reviewer freshly read the ARS-Codex
`academic-research-suite` root instructions and the directly applicable
academic-pipeline, citation-compliance, integrity-verification,
claim/reference-alignment, formatter, literature-corpus source-exclusion,
visualization, PDF/VLM verification, and figure/table-trace instructions in
full.

The review applied these controlling rules:

1. reference existence, correct metadata, locator presence, and faithful
   claim support are separate tests;
2. a source ceiling is negative as well as positive: a correct work cannot be
   cited for an expressly excluded result;
3. a locator that points to text not supporting the adjacent claim is a
   mismatch, not a pass;
4. every claim-bearing table trace requires all six keys, and
   `supported_manuscript_claims` must contain claim text as the primary value
   plus an exact current locator; a bare claim ID may be additional only;
5. forward and reverse artifact linkage are both mandatory;
6. omitted artifacts impose zero manuscript use only when the omission branch
   and its zero counts are exact;
7. formatting, compilation, and visual quality cannot cure a citation or
   claim-alignment defect; and
8. unresolved author identity and declarations are release facts, not
   technical citation findings.

The candidate was kept read-only. The only retained output of this review is
this audit file.

## 2. Exact-byte passport and preflight-chain continuity

### 2.1 Stable review-candidate tuple

| Frozen input | SHA-256 | Lines/pages | Bytes | Result |
|---|---|---:|---:|---|
| `paper/manuscript.tex` | `66e6434bf3b2bfaaac2b5abc2ff04c3cb49bf42a5d230c31e4354a91a8d65f2d` | 351 lines | 37,145 | match; full-read |
| `paper/references.bib` | `d589a945639dd83fe0c24d643fa1900b0da89171a72163e915fdecb6f456ed67` | 42 lines | 1,712 | match; full-read |
| `paper/README.md` | `460817961461d977ac9ccdc2af1ba08b2245ec440cb146bf9dbbaaa6e95667fc` | 112 lines | 8,911 | match; full-read |
| `paper/paper.pdf` | `bc8cd24b354c618213b70c34385960e4411fea84e689daed75ce03951d3d77cd` | 12 pages | 123,895 | match; all pages read and viewed |

### 2.2 Controlling gate and source/citation chain

| Frozen record | SHA-256 | Lines | Bytes | Result |
|---|---|---:|---:|---|
| `notes/pre_manuscript_exact_byte_gate.md` | `157eae8af4efc7916652738d63afe6996e61628b7110620e4cdecacb0bc18633` | 500 | 29,628 | match; full-read |
| `notes/pre_manuscript_source_gate.md` | `1a94c73043e01b7d5861a20357abdb26edf5f7115b47d0552ddab376f197e8f9` | 839 | 42,099 | match |
| `notes/pre_manuscript_citation_audit.md` | `5ffd9617e0b009c6bfac441b8de10adefe0f366ffc73586578a1c97c2d848e88` | 362 | 24,190 | match; full-read |
| `notes/sources/paper17_source_manifest.md` | `d1d13d9d9193512775db9e4e2bd2dd555e8bfaaef8ae9bce2e7a378b00cef6e9` | 163 | 10,010 | match; full-read |
| `notes/sources/paper17_sources.sha256` | `2381d5e5445da18f38caa026d3c2e4dfe6026ef944c21a6e32917ded9d6e699d` | 6 | 673 | six of six entries `OK` |
| `notes/sources/.gitignore` | `7aa3d6fc8be69e3c04723aa32c945aeabfddd262829ea29577a04da12681d5ab` | 2 | 87 | adjacent `*.pdf` exclusion present |

The three retained source PDFs and their three same-stem ARS sidecars match
the checksum ledger. The sidecars remain PASS with page-count triples
`12/12/12`, `14/14/14`, and `49/49/49`, with `warnings=[]`. The exact local
owner bytes also remain unchanged:

```text
P9=24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb
P10=27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315
P11=eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002
```

The source chain is therefore intact. The findings below arise in the new
candidate bytes, not from drift in the preflight corpus.

## 3. Open findings

### M-01 — all four current table traces substitute bare IDs for the mandatory v1 claim-text-primary arrays

Severity: **Major**

README lines 36, 45, 54, and 63 contain:

```text
T1 supported_manuscript_claims=[TN-02,TN-04,TN-08,TN-10,TN-14]
T2 supported_manuscript_claims=[TN-03,TN-05,TN-06,TN-07]
T3 supported_manuscript_claims=[TN-12]
T4 supported_manuscript_claims=[TN-13,TN-14]
```

Those cardinalities are the right association cardinalities, but the values
are the obsolete base-blueprint form. The authoritative v1 replacement at
`composition_blueprint_amendment_v1.md` lines 83--153 makes each item a record
whose primary value is the complete frozen `claim_text`, with `claim_id` only
an additional join key. The final exact-byte gate Section 7 then requires the
current candidate to retain that complete array and replace or augment each
planning locator with an exact current locator. It expressly states that bare-
ID substitution fails the candidate.

The expected current joins and locators are:

| Trace | Claim | Exact current manuscript locator | PDF claim page |
|---|---|---|---:|
| T1 | TN-02 | lines 146--147; `TRACE_CLAIM:TN-02` | 4 |
| T1 | TN-04 | lines 165--166; `TRACE_CLAIM:TN-04` | 5 |
| T1 | TN-08 | lines 224--225; `TRACE_CLAIM:TN-08` | 6 |
| T1 | TN-10 | lines 241--242; `TRACE_CLAIM:TN-10` | 7 |
| T1 | TN-14 | lines 307--308; `TRACE_CLAIM:TN-14` | 10 |
| T2 | TN-03 | lines 159--160; `TRACE_CLAIM:TN-03` | 4 |
| T2 | TN-05 | lines 179--180; `TRACE_CLAIM:TN-05` | 5 |
| T2 | TN-06 | lines 204--205; `TRACE_CLAIM:TN-06` | 6 |
| T2 | TN-07 | lines 208--209; `TRACE_CLAIM:TN-07` | 6 |
| T3 | TN-12 | lines 271--272; `TRACE_CLAIM:TN-12` | 8--9 |
| T4 | TN-13 | lines 302--303; `TRACE_CLAIM:TN-13` | 9 |
| T4 | TN-14 | lines 307--308; `TRACE_CLAIM:TN-14` | 10 |

The other five trace values are present and nonempty, and their source hashes,
table labels, PDF pages, caption claims, and limitations match. That does not
cure the fifth value. Without claim text and exact per-claim locator inside
each trace, an independent forward/reverse audit cannot be replayed from the
trace record itself.

Required repair: replace each bare array with the complete authoritative v1
claim records, retaining the exact claim text and adding the current line,
marker, and PDF locator above. Do not use the TN ID as the primary or sole
value. Re-run both directions of the four table traces. README lines 3, 10,
104, and 108 cannot continue to claim a trace PASS until that repair has been
independently re-audited.

### M-02 — the TN-11 P10 citation imports an expressly excluded copied-component/proxy scope and lacks the frozen local locator

Severity: **Major**

Manuscript line 244 says that Paper 10 classified “separated, measurable, and
copied-component collapses” and, under the same combined P10/P11 citation,
subtracts “proxy maps” and “completion records.” The citation command carries
no line locator.

The authoritative P10 owner row is narrower. Amendment v1 lines 246--266 and
the source manifest bind P10 to TN-11 only, to P10-1 through P10-4 only, and to
these four prior roles: separated universal images, continuous scalar
observables, Borel/measurable maps on the stated target domain, and positive
finite measures. They expressly prohibit importing a P10 proxy or copied-
component field. The exact eligible source blocks are the P10 ledger lines
132--135 and the P10-1--P10-4 theorem/scope-stop blocks at lines 201--226,
228--245, 270--285, and 287--306. P10-7--P10-8 copied-component material is
outside that registry.

This is not cured by the fact that the paragraph is a prior-work subtraction:
the TN-11-only ceiling also limits which P10 prior fields may be named within
TN-11. README line 102 correctly says “P10 supports TN-11 only,” but it omits
the internal P10-1--P10-4/no-copied-component restriction and cannot override
the manuscript sentence.

Required repair: restrict the P10 clause to the four authorized prior roles,
remove copied-component/proxy/completion attribution from P10, and provide the
exact P10 line locator. If a different prior field is genuinely needed, it
requires a new source/claim amendment and independent gate rather than a wider
paraphrase. TN-11 and the P10 work-level ceiling fail on the current bytes.

### M-03 — the TN-08 P11 locator does not support the adjacent standard topos/quantale triple

Severity: **Major**

Manuscript lines 217--222 display the standard-owner triple
`BZ/O(S_L x R)/O(S_L)`. Line 223 immediately says that “The standard-owner
formulas and their nontransfer boundary were already recorded” in P11 lines
313--324 and 337--405.

Those exact P11 bytes contain the standard-circle set-level orbit chart,
ordinary topology, the maps `J` and `J^{-1}`, the actual arrow-space open-set
description, the composable-pair chart, and the range-first topological-
groupoid operations. They contain no classifying-topos calculation and no
open-quantale/base computation. The source manifest and final gate therefore
license P11 here for the standard owner and formula/nontransfer boundary only;
they expressly deny P11 credit for a new Paper-17 topos or quantale result.

Because line 223 follows and grammatically points back to the displayed triple,
the current attribution is broader than its exact locator. This is a source-
claim mismatch even though the path, hash, and line range are correct.

Required repair: state unambiguously that P11 supplies only the standard-circle
owner/chart, range-first arrow/composable-pair formulas, and splice stop, while
the displayed `BZ/O(S_L x R)/O(S_L)` calculation is owned and proved in Paper
17. TN-08 and the P11 work-level ceiling fail on the current bytes.

## 4. Five-work citation graph, metadata, locators, and ceilings

The manuscript contains seven citation commands using five distinct keys. The
Bib file contains the same five keys and no others. Every Bib entry is cited;
every cited key resolves. There is no duplicate Forssell arXiv entry and no
visible Moerdijk Bib entry or technical citation.

| Work/key | Candidate uses | Identity/metadata | Locator and claim-ceiling result |
|---|---|---|---|
| Forssell 2013 / `forssell2013` | line 138; PDF p. 3 | PASS: Henrik Forssell; TAC 28(18), 541--551; 2013; DOI `10.70930/tac/jgiz1j78` | PASS: journal Section 2.1, pp. 542--543; framework vocabulary only; Paper-17 proof credit retained |
| Protin--Resende 2012 / `protinresende2012` | lines 178 and 201; PDF p. 5 | PASS: M. Clarence Protin and Pedro Resende; JNCG 6(2), 199--247; DOI `10.4171/JNCG/90` | PASS: printed 203--205, Theorems 2.41/2.45 at 214--215, and 245--246; bare quantale, `q_H`, and local compactness remain separate; no point-loss credit |
| P9 / `wang2026packets` | line 240; PDF p. 7 | PASS: exact local author/title/date/path/hash | PASS: P9 lines 409--426 support actual packet/orbit indiscreteness and literal stabilizer only; no standard-topology transfer |
| P10 / `wang2026reflections` | line 244; PDF p. 7 | PASS: exact local author/title/date/path/hash | **FAIL (M-02):** citation has no exact line locator and imports copied-component/proxy scope outside P10-1--P10-4 |
| P11 / `wang2026convolution` | lines 97, 223, and 244; PDF pp. 3, 6, and 7 | PASS: exact local author/title/date/path/hash | Mixed; weakest-use **FAIL (M-03)**. Line 97 range-first use passes; line 223 overcredits the cited owner/formula locator with the adjacent topos/quantale triple |

```text
STRUCTURAL_CITATION_GRAPH=PASS_5_KEYS_5_ENTRIES_0_ORPHANS
METADATA_GRAPH=PASS_5_OF_5
CLAIM_CEILING_GRAPH=FAIL_P10_AND_P11
MOERDIJK_METADATA_SENTINEL_VISIBLE_IN_TECHNICAL_GRAPH=false
FORSSELL_MANIFESTATIONS_COLLAPSED_TO_ONE_WORK=true
```

Moerdijk remains a six-work-registry metadata sentinel only. Its name appears
in README audit prose but not in the manuscript or Bib; that receipt-level
mention is not a technical citation and does not reopen the sentinel.

## 5. TN-00--TN-14 claim/owner result

| TN | Current candidate locator | Result |
|---|---|---|
| TN-00 | title/abstract and lines 83--93, 314--320 | pass: Technical-Note/nonstandalone ceiling retained |
| TN-01 | lines 97--105 | pass: P11 range-first locator exact |
| TN-02 | lines 140--147 | pass: direct proof; Forssell vocabulary only |
| TN-03 | lines 149--162 | pass: direct equivalence; no Moerdijk use |
| TN-04 | lines 164--166 | pass: connected `R`/discrete `Z` split retained |
| TN-05 | lines 168--180 | pass: bare quantale/base/nonunitality separated from reconstruction |
| TN-06 | lines 109--114 and 201--205 | pass: bare `O(H)`, `q_H`, and local compactness remain conjunctive and distinct |
| TN-07 | lines 207--209 | pass: `Top -> Loc` loss is Paper-17 inference, not source-theorem credit |
| TN-08 | lines 211--225 | **fail: M-03 P11 claim/locator overcredit** |
| TN-09 | lines 233--238 and 246--248 | pass: unmarked nonrecovery and strict-marker ceiling retained |
| TN-10 | lines 240--242 | pass: P9 facts and Paper-17 application separated |
| TN-11 | line 244 | **fail: M-02 P10 negative-ceiling violation** |
| TN-12 | lines 252--278 | pass: exact finite receipt remains diagnostic only |
| TN-13 | lines 282--303 | pass: 4 exploratory/3 rejected, all A2--A4 fail, Route B false |
| TN-14 | lines 305--320 | pass: scoped nonconstruction, not universal impossibility |

```text
TN_ROWS=15
TN_FULL_PASS=13
TN_FAIL=2
TN_FAIL_IDS=TN-08,TN-11
RETAINED_UNVERIFIABLE_CLAIM_COUNT=0
RETAINED_MISALIGNED_CLAIM_COUNT=2
```

## 6. Markers, active associations, trace payloads, and omitted figures

The manuscript contains the exact eleven distinct active markers, each once:

```text
TN-02@146  TN-03@159  TN-04@165  TN-05@179
TN-06@204  TN-07@208  TN-08@224  TN-10@241
TN-12@271  TN-13@302  TN-14@307
```

There are exactly four table environments and labels. The intended active
association set is numerically exact:

```text
T1=TN-02,TN-04,TN-08,TN-10,TN-14
T2=TN-03,TN-05,TN-06,TN-07
T3=TN-12
T4=TN-13,TN-14
ACTIVE_ASSOCIATIONS=5+4+1+2=12
TN-14_DUAL_JOIN=T1+T4
```

T1, T2, T3, and T4 each visibly carry the six required key names, and every
value except `supported_manuscript_claims` is nonempty and current. Therefore
the correct result is not “six-key trace absent”; it is “six-key names present,
mandatory fifth-value payload noncompliant”:

```text
SIX_KEY_NAMES_PRESENT=4_OF_4
SOURCE_HASHES_CURRENT=4_OF_4
TRANSFORMATION_AND_TABLE_LOCATORS_CURRENT=4_OF_4
CAPTION_CLAIMS_AND_LIMITATIONS_NONEMPTY=4_OF_4
SUPPORTED_CLAIM_TEXT_PRIMARY_ARRAYS_COMPLIANT=0_OF_4
TRACE_GATE=FAIL_M-01
```

The `BOTH_OMITTED` branch itself passes. There is no figure environment,
include, label, cross-reference, file, or substantive F1/F2 manuscript/PDF
mention. The two README omission receipts are audit metadata and preserve all
three zero counts. The four tables are legible on PDF pages 4, 6, 8, and 10;
T4 precedes Declarations and References.

## 7. Bilingual eight-fact parity

The English abstract at manuscript line 69 and the independently composed
Chinese abstract at line 78 preserve the same eight ordered facts:

| Order | Shared fact | Result |
|---:|---|---|
| 1 | owner-sensitive two-interface Technical Note; no standalone/full-paper claim | pass |
| 2 | direct generic topos and bare quantale/base computations on the nonempty globally indiscrete domain | pass |
| 3 | connected usual `R` gives `Set`; discrete `Z` gives `BZ` | pass |
| 4 | bare `O(H)`, `q_H`, and local compactness separated; loss at `Top -> Loc` | pass |
| 5 | actual `Set/O(R)/2` versus separate standard `BZ/O(S_L x R)/O(S_L)` | pass |
| 6 | unmarked scale nonrecovery; strict marking is extra; no recovery of `log p` | pass |
| 7 | controls are diagnostic/serialization receipts only | pass |
| 8 | four exploratory/three rejected; all A2--A4 fail; no determinant continuation; Route B closed at Technical-Note ceiling | pass |

No number, owner, hedge, omission, or Route disposition changes between the
two blocks. This parity pass does not cure M-01--M-03.

## 8. Isolated build, PDF, and visual result

A fresh isolated build used the exact frozen TeX and Bib bytes in the sequence
XeLaTeX, BibTeX, XeLaTeX, XeLaTeX. The final build log has no undefined
citation, unresolved reference, multiply defined label, overfull box, error,
or fatal diagnostic. Three underfull boxes remain; they do not clip content or
change a symbol. The rebuilt PDF is A4 and 12 pages. Its complete layout-text
extraction is byte-identical to the frozen candidate PDF extraction, SHA-256
`12a1037761969e45a313c70b8a56a35e9479b9444d83bf6e4e754700e95d56af`.

The frozen candidate PDF independently passes Ghostscript `nullpage`, has
text on all 12 pages, and uses seven embedded, subset, Unicode-mapped fonts.
All 12 pages were visually inspected at rendered-page resolution. No table
overflow, clipped line, empty page, missing glyph, displaced caption, hidden
reference, or misleading encoding was found. T1--T4 and the reference page
are legible. The build and visual layers pass.

The final PDF still prints `AUTHOR TO CONFIRM` and carries that literal value
in PDF author metadata. This is classified in Section 10, not as a build or
font defect.

## 9. Source-exclusion boundary

The exact source-exclusion state is preserved:

- the three research PDFs remain under `notes/sources/`, outside the four-file
  candidate surface;
- adjacent `.gitignore` excludes `*.pdf` in that source directory;
- the checksum ledger covers exactly the three PDFs and three sidecars and
  does not self-hash the manifest;
- no source PDF, preflight sidecar, manifest, control CSV, Route YAML, or gate
  is presented in the Bib as a literature theorem;
- Moerdijk remains metadata-only and absent from the visible technical graph;
- Forssell TAC/arXiv manifestations remain one work; and
- no Git, public sync, redistribution, or release permission is inferred.

This workspace is not itself a Git worktree, so tracked/untracked state cannot
be asserted from Git metadata here. That does not authorize publication; it
keeps the existing Git/public stop in force.

## 10. `AUTHOR TO CONFIRM`: separate nontechnical candidate/release hold

The manuscript contains ten literal `AUTHOR TO CONFIRM` occurrences, and the
PDF repeats the placeholder on the title page and in author metadata. They
cover four fact classes:

| Class | Unresolved author-supplied facts | Effect |
|---|---|---|
| identity/contact | author list, affiliation, correspondence address, author identifier | candidate/release hold |
| availability/licensing | repository URLs, released revision, archive identifiers, redistribution status, materials and code licenses | candidate/release hold; no public-availability inference |
| declarations | ethics/consent scope confirmation, competing interests, funding/grant or confirmed no-funding statement | candidate/release hold |
| responsibility/credit | CRediT roles, acknowledgments, contributor/permission facts, submitting-author verification, venue-specific AI wording | candidate/release hold |

These facts cannot be supplied from P9/P10/P11 ownership or from an automated
receipt. They remain unresolved until the actual author confirms them. They
are not a citation-source defect and are excluded from `C0/M3/m0`; nevertheless
they independently prevent candidate freeze and every release action even
after the three technical Major findings are repaired.

README line 112 calls author confirmation the “sole reason” for candidate-
freeze ineligibility and says the citation and trace checks pass. That statement
is no longer accurate for this exact tuple because M-01--M-03 are independent
additional holds. This receipt drift is derivative of the three findings and
is not counted as a fourth finding.

## 11. Finding ledger, verdict, and next exact-byte gate

| Severity | Open count | Findings |
|---|---:|---|
| Critical | 0 | none |
| Major | 3 | M-01 trace arrays; M-02 P10 ceiling/locator; M-03 P11 claim/locator alignment |
| Minor | 0 | none |

```text
FINAL_EFFECTIVE_VERDICT=HOLD
FINAL_EFFECTIVE_FINDINGS=C0/M3/m0
STRUCTURAL_BIB_GRAPH_PASS=true
SEMANTIC_CITATION_CEILING_PASS=false
TABLE_TRACE_HARD_GATE_PASS=false
BUILD_AND_PDF_VISUAL_PASS=true
AUTHOR_CONFIRMATION_HOLD=true
REVIEW_CANDIDATE_HOLD=true
RELEASE_HOLD=true
RELEASE_GIT_PUBLIC_SYNC=false
```

This audit does not authorize edits to the frozen candidate, manuscript
acceptance, release, Git mutation, archive deposit, or public synchronization.
The next eligible action is a separately authorized minimal correction of the
four-file candidate tuple that:

1. restores all four complete v1 claim-text-primary trace arrays with exact
   current locators;
2. narrows P10 to the exact P10-1--P10-4 TN-11 subtraction role and supplies
   its locator;
3. narrows the P11 sentence to owner/chart/range-first formula support and
   assigns the standard topos/quantale triple to Paper 17;
4. updates the README PASS/hold receipts honestly;
5. incorporates actual author-confirmed identity and declaration facts rather
   than inferred values; and
6. rebuilds and freezes a new TeX/Bib/README/PDF hash tuple.

Only a fresh independent exact-byte citation/claim-reference review of that
new tuple may close these findings or recommend the next peer/release gate.
This file's SHA-256, line count, and byte count are external by construction
and must be reported only after its final byte is closed.

## 12. Freeze-2 append-only independent closure review

Re-review date: **2026-08-17 (Asia/Shanghai)**  
Re-review role: fresh exact-byte citation, claim/reference, six-key trace,
source-boundary, build, and PDF-visual reviewer  
Freeze-2 effective verdict: **HOLD — `C0/M1/m0`**  
Historical disposition: **Freeze-1 M-01--M-03 are closed on Freeze-2 bytes;
new Freeze-2 M-04 is open**

```text
FREEZE2_CITATION_REREVIEW_COMPLETED=true
AUDIT_PREFIX_PRESERVED=true
AUDIT_PREFIX_SHA256=1237ce87b959315f733584de959620e465a55586a9d5a632506225194a07080a
AUDIT_PREFIX_LINES=444
AUDIT_PREFIX_BYTES=22916
FROZEN_INPUT_HASH_DRIFT=0
FREEZE1_M01_CLOSED_ON_FREEZE2=true
FREEZE1_M02_CLOSED_ON_FREEZE2=true
FREEZE1_M03_CLOSED_ON_FREEZE2=true
NEW_FREEZE2_M04_OPEN=true
BIBLIOGRAPHY_ENTRIES=5
DISTINCT_CITED_KEYS=5
CITATION_ORPHANS=0
BIBLIOGRAPHY_ORPHANS=0
WORK_IDENTITY_METADATA_PASS=5_OF_5
WORK_CLAIM_CEILING_PASS=5_OF_5
TN_CLAIM_OWNER_ROWS_FULL_PASS=15_OF_15
TRACE_RECORDS_WITH_SIX_KEYS_PRESENT=4_OF_4
TRACE_RECORDS_WITH_CANONICAL_CLAIM_TEXT_PRIMARY_ARRAYS=4_OF_4
TRACE_RECORDS_WITH_ALL_CURRENT_PAYLOADS=3_OF_4
DISTINCT_TRACE_MARKERS=11
ACTIVE_TABLE_ASSOCIATIONS=12
FIGURE_BRANCH=BOTH_OMITTED
BILINGUAL_FACT_PARITY=8_OF_8
CLEAN_ISOLATED_BUILD=true
PDF_PAGES_VISUALLY_CHECKED=12_OF_12
RETAINED_UNVERIFIABLE_TECHNICAL_CLAIMS=0
RETAINED_MISALIGNED_TECHNICAL_CLAIMS=0
EFFECTIVE_FINDINGS=C0/M1/m0
AUTHOR_TO_CONFIRM_IS_TECHNICAL_CITATION_FINDING=false
AUTHOR_CONFIRMATION_COMPLETE=false
CANDIDATE_FREEZE_ELIGIBLE=false
RELEASE_AUTHORIZED=false
STANDALONE_PASS=false
```

This append preserves the first audit as the correct finding record for the
Freeze-1 tuple. It does not erase or rewrite M-01--M-03. The three bounded
repairs succeed on Freeze-2, but a fresh visual-to-trace comparison exposes a
different stale current-table locator. Consequently the Freeze-2 candidate
does not pass this re-review.

### 12.1 Fresh ARS and exact-byte authority receipt

Before evaluating Freeze-2, the reviewer freshly read the ARS-Codex
academic-research-suite root, academic-pipeline workflow, citation-compliance,
integrity-verification, claim/reference-alignment, formatter,
source-exclusion, visualization, VLM/PDF verification, and six-key
figure/table-trace instructions in full. The effective Paper-17 authority was
then read in its frozen order: base blueprint, amendment v1, amendment v2,
source gate and citation preflight, final exact-byte gate, the complete
Freeze-1 audit prefix, and the Freeze-1 remediation gate. The exact P9, P10,
and P11 owner passages and the cited Forssell and Protin--Resende PDF pages
were reopened from matching local bytes.

The append authorization matched exactly:

| Authority | SHA-256 | Lines | Bytes | Result |
|---|---|---:|---:|---|
| `notes/manuscript_remediation_gate_v1.md` | `66ccb9bdaa7ce12febfacbc1fab1cc742c85e94e9631fdb385e0ee768454a840` | 613 | 31,329 | full-read; exact |
| pre-append `notes/citation_audit.md` prefix | `1237ce87b959315f733584de959620e465a55586a9d5a632506225194a07080a` | 444 | 22,916 | exact; preserved |

The stable Freeze-2 tuple also matched before every substantive check:

| Frozen candidate path | SHA-256 | Lines/pages | Bytes | Result |
|---|---|---:|---:|---|
| `paper/manuscript.tex` | `dc6471b03dbd4e9017909a67ea121000fa6e11172b887aba3cc5e9391d8c9b54` | 351 lines | 37,611 | exact; full-read |
| `paper/references.bib` | `d589a945639dd83fe0c24d643fa1900b0da89171a72163e915fdecb6f456ed67` | 42 lines | 1,712 | exact; full-read |
| `paper/README.md` | `b12ec948736fd202578204ad2d8c5ea4f58bf1c11b3743cd49fc135df8de40f6` | 168 lines | 15,395 | exact; full-read |
| `paper/paper.pdf` | `0f01b3427cb7c576973e1c451609d132343937b08dc3ae6709d6b385844daf50` | 12 pages | 124,544 | exact; all pages read and viewed |

No candidate, bibliography, source, figure, table, build, control, Route,
README, Git, release, or public byte was changed by this review.

### 12.2 Freeze-1 M-01 closure: canonical claim-text-primary arrays restored

README contains four parseable YAML records, and each has exactly the six
required top-level keys. A mechanical item-by-item comparison with remediation
gate Sections 5.1--5.4 gives exact equality for every `claim_id`, complete
`claim_text`, `planned_manuscript_locator`, and
`current_manuscript_locator`:

```text
T1=5_OF_5_EXACT
T2=4_OF_4_EXACT
T3=1_OF_1_EXACT
T4=2_OF_2_EXACT
CANONICAL_ARRAYS=4_OF_4
ACTIVE_ASSOCIATIONS=12
DISTINCT_MARKERS=11
TN14_DUAL_JOIN=T1+T4
```

All eleven literal markers occur exactly once at manuscript lines 146, 159,
165, 179, 204, 208, 224, 241, 271, 302, and 307. Their substantive forward
uses resolve to T1/T2/T3/T4 in the frozen `5/4/1/2` pattern. The reverse scan
found no unregistered substantive table-supported claim. The introductory or
display-description pointers at lines 116, 276, and 282 state table role or
layout; the surrounding prose carries the reasoning independently and does
not ask the table to establish an additional technical proposition. They are
therefore structural rather than hidden active associations under the ARS
exemption.

The TN-12 claim locator correctly spans PDF pages 8--9: the prose claim begins
on page 8 and the table object is on page 9. That fact does not cure the
separate stale T3 `transformation` locator recorded as M-04 below.

**Freeze-1 M-01 disposition on Freeze-2: CLOSED.**

### 12.3 Freeze-1 M-02 closure: P10 is TN-11/P10-1--P10-4 only

Manuscript line 244 now gives one grammatically separate P10 clause with the
exact local binding:

```text
owner_sha256=27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315
claim_ledger=lines 132--135
P10-1=lines 201--226
P10-2=lines 228--245
P10-3=lines 270--285
P10-4=lines 287--306
support_mode=TN-11 builds-on/prior-subtraction only
```

Those exact source bytes support separated universal images, continuous
scalar observables, Borel/measurable maps on the stated target domain, and
positive finite measures. The repaired sentence attributes no copied
component, proxy, completion, P10-5, operator, support, measure selection,
trace, determinant, Route, owner, fixed-prime, direct Paper-17 theorem,
novelty, or standalone result to P10. The adjacent P11 clause is separate and
has its own locator.

**Freeze-1 M-02 disposition on Freeze-2: CLOSED.**

### 12.4 Freeze-1 M-03 closure: P11 formula/owner ceiling is explicit

Manuscript line 223 now states first that the displayed standard
`BZ/O(S_L x R)/O(S_L)` triple is derived directly in Paper 17. It then limits
P11 to its standard-circle owner/chart, ordinary arrow-space and
composable-pair charts, range-first formulas/operations, and owner-splice
stop, with exact P11 locators `255--277`, `313--324`, `337--405`, and
`1079--1087`. The sentence expressly denies P11 classifying-topos,
open-quantale, base-frame, localic-reconstruction, comparison-triple, and
Paper-17 theorem credit.

The actual `Set/O(R)/2` and separately imposed standard
`BZ/O(S_L x R)/O(S_L)` owners remain distinct at lines 211--225. No topology,
provenance, coordinate, or standard-to-actual transfer appears.

**Freeze-1 M-03 disposition on Freeze-2: CLOSED.**

### 12.5 New Freeze-2 M-04: T3 current table-page locator and visual receipt are stale

Severity: **Major**

README line 96, inside the mandatory T3 six-key trace, says:

```text
current locator manuscript.tex label tab:t3, PDF page 8
```

README line 164 independently says that T3 is on page 8. Both statements are
false for the exact frozen PDF. Complete page rendering places the Table 3
caption and object at the top of PDF page 9. Fresh text extraction finds no
`Finite-control receipt` caption on page 8 and finds it on page 9. A clean
build from the exact TeX/Bib bytes independently emits:

```text
\newlabel{tab:t3}{{3}{9}{Finite-control receipt ...}{table.3}{}}
```

T1, T2, and T4 correctly resolve to pages 4, 6, and 10. README line 102's
TN-12 claim locator, `paper.pdf pages 8--9`, is also correct because it spans
the prose claim and the floated table. The defect is specifically the stale
current artifact locator in T3's `transformation` value and the matching
false visual receipt.

This is not cosmetic pagination prose. The exact-byte gate requires every
active table's current six-key trace to bind the actual inline artifact and
treats a stale trace as a hard failure. One of four trace records therefore
has all six key names and a canonical claim array but not all-current payload
values. The false visual receipt also prevents the README from serving as an
exact replay record for the frozen PDF.

Required repair: under a new, separately authorized exact-byte lane, change
the T3 table-object/current transformation locator and the visual receipt from
PDF page 8 to PDF page 9; recheck all four table pages and every current
locator against the resulting exact README bytes. Do not change the already
correct TN-12 `pages 8--9` claim locator merely to make all page values equal.
This audit does not authorize that repair.

### 12.6 Five-work graph, claim ceilings, and TN matrix

The manuscript has eight citation commands using five distinct keys; the Bib
has the same five entries and no others. There are no citation or bibliography
orphans, no Moerdijk technical citation or Bib entry, and exactly one Forssell
work/entry.

| Work | Exact Freeze-2 result |
|---|---|
| Forssell 2013 | PASS: official TAC Section 2.1, journal pp. 542--543; framework vocabulary only; Paper-17 proof ownership retained |
| Protin--Resende 2012 | PASS: printed pp. 203--205, Theorems 2.41/2.45 at 214--215, and 245--246; bare `O(H)`, `q_H`, and local compactness remain distinct; no point-loss attribution |
| P9 | PASS: exact hash and lines 409--426; actual indiscreteness/literal stabilizer only |
| P10 | PASS after M-02 repair: exact hash and P10-1--P10-4 locator; TN-11 subtraction only |
| P11 | PASS after M-03 repair: exact hash and four locator ranges; formula/owner support only |

TN-00--TN-14 were then re-read from the complete manuscript rather than only
rechecking the former failures. All fifteen remain within their frozen
technical owner, hypothesis, source, diagnostic, and Route ceilings. In
particular, TN-08 and TN-11 now pass; TN-03 remains a direct Paper-17 proof
without Moerdijk; TN-07 keeps point loss at `Top -> Loc`; TN-12 remains
diagnostic only; and TN-13/TN-14 retain four exploratory/three rejected, all
A2--A4 `FAIL`, Route B false, and the scoped nonconstruction ceiling.

```text
STRUCTURAL_CITATION_GRAPH=PASS_5_KEYS_5_ENTRIES_0_ORPHANS
METADATA_GRAPH=PASS_5_OF_5
CLAIM_CEILING_GRAPH=PASS_5_OF_5
TN_MATRIX=PASS_15_OF_15
RETAINED_UNVERIFIABLE_TECHNICAL_CLAIMS=0
RETAINED_MISALIGNED_TECHNICAL_CLAIMS=0
```

M-04 is a current artifact-trace/receipt defect, not an unsupported literature
claim, so it does not reduce the 15/15 TN or 5/5 work-ceiling results.

### 12.7 Omitted figures, bilingual parity, build, PDF, and source boundary

F1 and F2 retain the exact nonempty `OMITTED_BY_COMPOSITION` rationales and
all three zero counts. There is no manuscript figure environment,
`includegraphics`, F1/F2 label, object, caption, cross-reference, or
substantive use. Under `BOTH_OMITTED`, the active set is exactly T1--T4.

The English and independently composed Chinese abstracts retain the same
eight facts in the frozen order, including the same connected-`R`/discrete-`Z`
contrast, premise separation, actual/standard owner split, unmarked/strict
boundary, diagnostic ceiling, 4/3 Route result, all-fail coordinates, Route-B
stop, and Technical-Note hedge. No owner, number, omission, or strength drift
was found.

A fresh isolated build copied only the exact TeX and read-only Bib bytes and
ran XeLaTeX, BibTeX, XeLaTeX, XeLaTeX. It produced 12 unencrypted A4 pages.
The final log has no error, fatal diagnostic, undefined citation/reference,
multiply defined label, missing character, overfull box, or rerun request.
Two underfull boxes at source lines 318--319 are nonclipping layout warnings.
The rebuilt layout-text extraction is byte-identical to the frozen PDF
extraction, both SHA-256
`c44799e45e8657be6cd569a31b2b34781ebcfb5c44dfa20b7eac74538deb3e58`.
The rebuilt binary PDF hash differs because the engine emits build metadata;
no content or layout-text difference was found.

The frozen PDF passes Ghostscript `nullpage`, has nonempty extractable text on
all 12 pages, and uses seven embedded, subset, Unicode-mapped fonts. Every
page was rendered and inspected. Both abstracts, equations, four tables,
declarations, and all five references are legible; no clipping, empty page,
missing glyph, table overflow, or misleading visual encoding was found. The
actual table pages are T1=4, T2=6, T3=9, T4=10. Thus the rendering itself
passes; M-04 is the trace/receipt mismatch discovered by that visual check.

The local source ledger again returns six of six `OK`. The three PDF
sidecars remain PASS at `12/12/12`, `14/14/14`, and `49/49/49`, each with
`warnings=[]`; adjacent `.gitignore` still excludes `*.pdf`. The ledger covers
exactly the three PDFs and three sidecars and does not self-hash the manifest.
Moerdijk remains a metadata-only sentinel; Forssell's two manifestations are
one work; and no source PDF, sidecar, control, Route record, or manifest is
presented as a literature theorem. No Git/public/release permission is
inferred.

### 12.8 Separate `AUTHOR TO CONFIRM` stop and final Freeze-2 verdict

The manuscript still has ten literal `AUTHOR TO CONFIRM` occurrences covering
identity/contact, repository/archive/license, ethics/consent confirmation,
competing interests, funding, CRediT/acknowledgments, and venue-specific AI
wording. Those author-supplied facts remain unresolved. They are not a
technical citation finding and are excluded from `C0/M1/m0`, but they
independently prevent candidate freeze and release.

| Finding | Freeze-2 status |
|---|---|
| historical M-01: bare trace arrays | CLOSED on Freeze-2 |
| historical M-02: P10 ceiling/locator | CLOSED on Freeze-2 |
| historical M-03: P11 attribution | CLOSED on Freeze-2 |
| new M-04: T3 stale PDF page in six-key trace and visual receipt | **OPEN Major** |

```text
FINAL_EFFECTIVE_VERDICT=HOLD
FINAL_EFFECTIVE_FINDINGS=C0/M1/m0
FREEZE1_M1_M2_M3_CLOSED=true
FREEZE2_NEW_M4_OPEN=true
STRUCTURAL_BIB_GRAPH_PASS=true
SEMANTIC_CITATION_CEILING_PASS=true
TABLE_TRACE_HARD_GATE_PASS=false
BUILD_AND_PDF_VISUAL_PASS=true
AUTHOR_CONFIRMATION_HOLD=true
CANDIDATE_FREEZE_ELIGIBLE=false
RELEASE_AUTHORIZED=false
STANDALONE_PASS=false
RELEASE_GIT_PUBLIC_SYNC=false
```

The smallest eligible next action is a separately authorized exact-byte
README-only trace-receipt correction that preserves the current TeX, Bib, and
PDF bytes, fixes the two false T3 page-8 statements without changing the
correct TN-12 pages-8--9 locator, freezes a new four-file tuple, and receives
a fresh independent append-only citation/trace review. This audit merely
recommends that gate; it authorizes no candidate edit, manuscript acceptance,
peer closure, release, Git mutation, archive deposit, or public sync.

The stable SHA-256, line count, and byte count of the complete appended audit
must be computed externally after the final byte is closed. The preserved
prefix identity remains the exact 444-line, 22,916-byte SHA-256 receipt stated
above.

## 13. Freeze-3 append-only final citation and trace closure

Re-review date: **2026-08-17 (Asia/Shanghai)**  
Re-review role: independent exact-byte citation, claim/reference, source-boundary,
and six-key artifact-trace closure reviewer  
Freeze-3 technical citation verdict: **PASS — `C0/M0/m0`**  
Candidate/release state: **HOLD — author confirmation remains required**

```text
FREEZE3_CITATION_CLOSURE_COMPLETED=true
FREEZE2_AUDIT_PREFIX_PRESERVED=true
FREEZE2_AUDIT_PREFIX_SHA256=6dbeaf377c51b5a4b73678d959e16984d14872f46668d49d826794726ff653b3
FREEZE2_AUDIT_PREFIX_LINES=767
FREEZE2_AUDIT_PREFIX_BYTES=38201
HISTORICAL_FREEZE1_PREFIX_PRESERVED=true
HISTORICAL_FREEZE1_PREFIX_SHA256=1237ce87b959315f733584de959620e465a55586a9d5a632506225194a07080a
HISTORICAL_FREEZE1_PREFIX_LINES=444
HISTORICAL_FREEZE1_PREFIX_BYTES=22916
FROZEN_INPUT_HASH_DRIFT=0
FREEZE1_M01_CLOSED_NO_REGRESSION=true
FREEZE1_M02_CLOSED_NO_REGRESSION=true
FREEZE1_M03_CLOSED_NO_REGRESSION=true
FREEZE2_M04_CLOSED_ON_FREEZE3=true
BIBLIOGRAPHY_ENTRIES=5
DISTINCT_CITED_KEYS=5
CITATION_ORPHANS=0
BIBLIOGRAPHY_ORPHANS=0
WORK_IDENTITY_METADATA_PASS=5_OF_5
WORK_CLAIM_CEILING_PASS=5_OF_5
TN_CLAIM_OWNER_ROWS_FULL_PASS=15_OF_15
TRACE_RECORDS_WITH_SIX_KEYS_PRESENT=4_OF_4
TRACE_RECORDS_WITH_CANONICAL_CLAIM_TEXT_PRIMARY_ARRAYS=4_OF_4
TRACE_RECORDS_WITH_ALL_CURRENT_PAYLOADS=4_OF_4
DISTINCT_TRACE_MARKERS=11
ACTIVE_TABLE_ASSOCIATIONS=12
FIGURE_BRANCH=BOTH_OMITTED
BILINGUAL_FACT_PARITY=8_OF_8
RETAINED_UNVERIFIABLE_TECHNICAL_CLAIMS=0
RETAINED_MISALIGNED_TECHNICAL_CLAIMS=0
TECHNICAL_CITATION_FINDINGS=C0/M0/m0
AUTHOR_TO_CONFIRM_IS_TECHNICAL_CITATION_FINDING=false
AUTHOR_CONFIRMATION_COMPLETE=false
CANDIDATE_FREEZE_ELIGIBLE=false
RELEASE_AUTHORIZED=false
STANDALONE_PASS=false
```

This section preserves Sections 1--12 as the correct historical records for
their exact tuples. It closes only citation M-04 on the exact Freeze-3 bytes
below. It does not rewrite the original M-01--M-03 findings, erase the Freeze-2
M-04 finding, adjudicate the independent peer ledger, or authorize a candidate
freeze or release.

### 13.1 Fresh ARS and exact-byte authority receipt

Before evaluating Freeze 3, the reviewer freshly read the ARS-Codex
academic-research-suite root and complete directly applicable academic-pipeline,
citation-compliance, integrity-verification, claim/reference-alignment,
formatter, source-exclusion, visualization, VLM/PDF, and six-key
figure/table-trace instructions. The complete Freeze-3 remediation gate, the
full 767-line current audit prefix, the new README, the unchanged TeX and Bib,
the exact P9/P10/P11 owner passages, and the relevant local Forssell and
Protin--Resende source pages were then read from matching bytes.

The append authorization and both required prefix receipts matched exactly:

| Authority | SHA-256 | Lines | Bytes | Result |
|---|---|---:|---:|---|
| `notes/manuscript_remediation_gate_v2.md` | `fccdc745ca1c8e6a59d3768054222923f3fc9626459f2805ff0636dc73168f41` | 311 | 12,331 | full-read; exact |
| pre-append `notes/citation_audit.md` | `6dbeaf377c51b5a4b73678d959e16984d14872f46668d49d826794726ff653b3` | 767 | 38,201 | exact; preserved |
| historical Freeze-1 audit prefix | `1237ce87b959315f733584de959620e465a55586a9d5a632506225194a07080a` | 444 | 22,916 | exact; preserved within the larger prefix |

The four-file Freeze-3 tuple also matched before the substantive checks:

| Frozen candidate path | SHA-256 | Lines/pages | Bytes | Result |
|---|---|---:|---:|---|
| `paper/manuscript.tex` | `dc6471b03dbd4e9017909a67ea121000fa6e11172b887aba3cc5e9391d8c9b54` | 351 lines | 37,611 | exact; read-only |
| `paper/references.bib` | `d589a945639dd83fe0c24d643fa1900b0da89171a72163e915fdecb6f456ed67` | 42 lines | 1,712 | exact; read-only |
| `paper/README.md` | `161a7f523c2daf32c6f015c27054e1a1a36192fcf2581158dea1cb5828436ca1` | 168 lines | 15,395 | exact Freeze-3 repair |
| `paper/paper.pdf` | `0f01b3427cb7c576973e1c451609d132343937b08dc3ae6709d6b385844daf50` | 12 pages | 124,544 | exact; read-only |

No build or PDF regeneration was authorized or performed. No candidate,
bibliography, source, control, Route, peer-report, pipeline, Git, release, or
public byte was changed by this review.

### 13.2 M-04 closure: T3 artifact and TN-12 claim locators are now distinct and correct

README line 96 now states:

```text
current locator manuscript.tex label tab:t3, PDF page 9
```

README line 164 independently records `T3 on page 9`. README line 102 remains
byte-for-byte the required TN-12 claim locator ending in `paper.pdf pages
8--9`. These values correctly distinguish the location of the floated table
object from the span of the supported prose claim.

The exact frozen PDF was inspected without rebuilding it. Page 8 contains the
Section 6 prose and the sentence beginning `Table 3 gives the final finite
receipt`, but no Table 3 caption or object. Page 9 begins with `Table 3:
Finite-control receipt` and contains the complete object. The four table-object
pages and their claim-page joins are now:

| Trace | Exact object page | Exact supported-claim PDF locator(s) | Result |
|---|---:|---|---|
| T1 | 4 | TN-02 p. 4; TN-04 p. 5; TN-08 p. 6; TN-10 p. 7; TN-14 p. 10 | current |
| T2 | 6 | TN-03 p. 4; TN-05 p. 5; TN-06 p. 6; TN-07 p. 6 | current |
| T3 | 9 | TN-12 pp. 8--9 | current after R1/R2 |
| T4 | 10 | TN-13 p. 9; TN-14 p. 10 | current |

Thus neither the old page-8 object claim nor its duplicate visual receipt
survives, while the correct pages-8--9 claim locator was not flattened or
altered. **Freeze-2 M-04 is CLOSED on the exact Freeze-3 tuple.**

### 13.3 Six-key trace and M-01 non-regression

README still contains four independently parseable YAML trace records. Each
has exactly the required six keys: `artifact_id`, `source_data`,
`transformation`, `caption_claim`, `supported_manuscript_claims`, and
`limitations`. Mechanical item-by-item comparison against the canonical v1
arrays gives:

```text
T1_CANONICAL_CLAIMS=5_OF_5
T2_CANONICAL_CLAIMS=4_OF_4
T3_CANONICAL_CLAIMS=1_OF_1
T4_CANONICAL_CLAIMS=2_OF_2
CANONICAL_CLAIM_TEXT_PRIMARY_ARRAYS=4_OF_4
ALL_CURRENT_SIX_KEY_PAYLOADS=4_OF_4
ACTIVE_ASSOCIATIONS=12
DISTINCT_CLAIM_IDS=11
TN14_DUAL_JOIN=T1+T4
```

Every item retains its full `claim_text`, planning locator, and exact current
line/marker/table/PDF locator; a bare TN ID is never substituted for the claim
text. The eleven literal markers occur exactly once at manuscript lines 146,
159, 165, 179, 204, 208, 224, 241, 271, 302, and 307. Their substantive uses
form the exact T1/T2/T3/T4 `5/4/1/2` association pattern. Reverse scanning found
no hidden substantive table-supported claim. The unmarked mentions at lines
116, 276, and 282 describe registry role, execution-layer display, or table
layout and remain structural; the marked surrounding claims carry the
substantive reasoning. **M-01 remains CLOSED without regression.**

### 13.4 Five-work graph, owner ceilings, and TN matrix

The unchanged manuscript has eight citation commands using five distinct
keys, and the unchanged Bib has exactly those five entries. There are zero
dangling citations and zero orphan references. Moerdijk remains absent from
the manuscript and Bib; the TAC and arXiv manifestations of Forssell remain
one visible work, not duplicate entries.

| Work | Freeze-3 independent result |
|---|---|
| Forssell 2013 | PASS: official TAC Section 2.1, journal pp. 542--543 supports only open-groupoid/equivariant-sheaf framework vocabulary; Paper-17 proof ownership remains explicit |
| Protin--Resende 2012 | PASS: printed pp. 203--205, Theorems 2.41/2.45 at 214--215, and pp. 245--246 support the bounded open-quantale/localic framework; bare `O(H)`, `q_H`, and local compactness remain separate, and point loss is not credited to the source theorem |
| P9 | PASS: exact hash `24dfcc...31bb`, lines 409--426; actual indiscreteness and literal stabilizer only |
| P10 | PASS: exact hash `27bae8...d315`, ledger 132--135 and P10-1--P10-4 ranges; manuscript line 244 remains TN-11 builds-on/prior-subtraction only and imports no copied-component, proxy, completion, P10-5+, operator, support, trace, or determinant scope |
| P11 | PASS: exact hash `eb1aa4...1002`, lines 255--277, 313--324, 337--405, and 1079--1087; owner/chart, arrow/composable-pair, range-first formulas, and splice stop only; Paper 17 retains the displayed triple and theorem credit |

The complete TN-00--TN-14 registry was rechecked against the unchanged source
bytes and manuscript. All fifteen remain within their mathematical owner,
domain, source, diagnostic, Route, and nonstandalone ceilings. In particular,
TN-03 still has no load-bearing Moerdijk use, TN-07 locates possible point loss
at `Top -> Loc`, TN-08 and TN-11 retain the repaired P11/P10 boundaries, TN-12
is diagnostic only, and TN-13/TN-14 retain four exploratory/three rejected,
universal A2--A4 `FAIL`, Route B false, and scoped nonconstruction.

```text
STRUCTURAL_CITATION_GRAPH=PASS_5_KEYS_5_ENTRIES_0_ORPHANS
WORK_METADATA_GRAPH=PASS_5_OF_5
WORK_CLAIM_CEILING_GRAPH=PASS_5_OF_5
TN_MATRIX=PASS_15_OF_15
M01_M02_M03_NO_REGRESSION=true
RETAINED_UNVERIFIABLE_TECHNICAL_CLAIMS=0
RETAINED_MISALIGNED_TECHNICAL_CLAIMS=0
```

### 13.5 Omission, parity, Route, PDF, and source-boundary non-regression

F1 and F2 retain `OMITTED_BY_COMPOSITION`, nonempty rationales, and all six
zero-use counters. The TeX still contains no figure environment or
`includegraphics`, so the active artifact set remains exactly T1--T4.

The English and independently composed Chinese abstracts retain the same eight
facts, owners, numbers, hedges, omissions, `4/3` Route disposition, universal
A2--A4 failure, Route-B stop, and Technical-Note ceiling. The seven table rows
remain four exploratory and three rejected; all A2, A3, and A4 entries remain
`FAIL`, and all Route-B values remain false.

Because TeX, Bib, and PDF are byte-identical to Freeze 2, this closure did not
repeat or replace the already recorded clean build. It performed the required
read-only artifact/claim-locator check on frozen PDF pages 4, 6, 8, 9, and 10.
T1, T2, T3, and T4 are legible on pages 4, 6, 9, and 10 respectively, with no
clipping or table overflow in those inspected pages; page 8 carries the TN-12
prose side of the p. 8--9 join.

The local source checksum ledger again returns six of six `OK`. The three
same-stem ARS PDF sidecars remain PASS at `12/12/12`, `14/14/14`, and
`49/49/49`, each with `warnings=[]`. The adjacent `.gitignore` still excludes
`*.pdf`; the ledger covers exactly the three PDFs and three sidecars and does
not self-hash the manifest. Research PDFs remain local-only and outside the
candidate. No sidecar, manifest, gate, control, Route record, or local PDF is
promoted into the bibliography as a theorem, and no redistribution, Git,
release, or public-sync permission is inferred.

### 13.6 Separate author-confirmation stop and final Freeze-3 citation verdict

The unchanged TeX still contains ten literal `AUTHOR TO CONFIRM` occurrences.
Identity/contact, repository/archive/license, ethics/consent, competing
interests, funding, CRediT/acknowledgments, and venue-specific AI wording remain
author-supplied facts. They are not technical citation findings and are not
included in `C0/M0/m0`, but they independently keep candidate and release
eligibility false. This citation review also does not close or replace the
independent peer-review ledger.

| Citation finding | Freeze-3 status |
|---|---|
| historical M-01: bare trace arrays | CLOSED on Freeze 2; no regression |
| historical M-02: P10 ceiling/locator | CLOSED on Freeze 2; no regression |
| historical M-03: P11 attribution | CLOSED on Freeze 2; no regression |
| Freeze-2 M-04: T3 stale object page and visual receipt | **CLOSED on Freeze 3** |
| new Freeze-3 citation/claim/trace findings | none |

```text
FINAL_FREEZE3_CITATION_VERDICT=PASS
FINAL_FREEZE3_CITATION_FINDINGS=C0/M0/m0
ALL_CITATION_FINDINGS_CLOSED_ON_EXACT_FREEZE3=true
STRUCTURAL_BIB_GRAPH_PASS=true
SEMANTIC_CITATION_CEILING_PASS=true
TABLE_TRACE_HARD_GATE_PASS=true
SOURCE_BOUNDARY_PASS=true
AUTHOR_CONFIRMATION_HOLD=true
PEER_LEDGER_CLOSED_BY_THIS_AUDIT=false
CANDIDATE_FREEZE_ELIGIBLE=false
RELEASE_AUTHORIZED=false
STANDALONE_PASS=false
RELEASE_GIT_PUBLIC_SYNC=false
```

The exact Freeze-3 tuple therefore passes this citation/claim/source/trace
lane, and M-04 requires no further citation repair. This is not a standalone
manuscript pass or a release authorization. Only separately authorized author
confirmation and the remaining independent gates may determine a later
candidate state. The stable SHA-256, line count, and byte count of the complete
appended audit must be computed externally after its final byte is closed.
