# Paper 17 manuscript peer review — Round 1 (Freeze 1)

Review date: **2026-08-17 (Asia/Shanghai)**  
Reviewer role: independent manuscript peer reviewer, method/domain/devil's-
advocate synthesis  
Candidate ceiling: **nonstandalone Technical Note**  
Technical recommendation: **MINOR REVISION**  
Effective technical findings: **`C0/M0/m1`**

```text
PEER_REVIEW_ROUND=1
PEER_REVIEW_FREEZE=1
REVIEW_INDEPENDENT_OF_CONCURRENT_CITATION_REVIEW=true
CONCURRENT_CITATION_REVIEW_RESULT_READ_OR_USED=false
FROZEN_INPUT_HASH_DRIFT=0
CORE_MATHEMATICAL_VALIDITY=PASS
TN_RECORDS_PRESENT=15_OF_15
TN_SCOPE_STATUS=14_PASS_1_REVISE
OWNER_FIREWALL_ROWS=7
ROUTE_DISPOSITION=4_EXPLORATORY_3_REJECTED
A2_A3_A4_STATUS=ALL_FAIL
ROUTE_B_FOR_THE_SEVEN_OWNERS=false
INLINE_TABLES=T1,T2,T3,T4
FIGURE_BRANCH=BOTH_OMITTED
TECHNICAL_PEER_VERDICT=MINOR_REVISION
EFFECTIVE_FINDINGS=C0/M0/m1
AUTHOR_CONFIRMATION_STOP=REQUIRED_SEPARATE_FROM_TECHNICAL_VERDICT
CANDIDATE_FREEZE_ELIGIBLE=false
FINAL_OR_RELEASE_ELIGIBILITY=false
GIT_OR_PUBLIC_SYNC_AUTHORIZED=false
```

The one finding is a bounded prior-work/owner-scope drift in TN-11. It does
not undermine the four direct mathematical results, but the current bytes do
not pass the frozen exact-source ceiling and therefore cannot receive a peer
PASS. The author/declaration placeholders are a separate administrative stop;
they do not inflate the technical finding count.

## 1. Independence, method, and rule receipt

Before reading the candidate, the reviewer freshly read the ARS-Codex
`academic-research-suite` root instructions and the directly applicable
academic-paper-reviewer, methodology-reviewer, domain-reviewer,
devil's-advocate, formatter, citation-compliance, integrity-verification,
claim-reference-alignment, bilingual-abstract, visualization, PDF-visual, and
figure/table-trace instructions in full. The reviewer also read the peer-review
report template in full.

The review then proceeded from the frozen candidate bytes, not from any
concurrent citation review. The concurrent citation reviewer was neither
queried nor used. The reviewer:

1. read `manuscript.tex`, `references.bib`, `paper/README.md`, and the final
   exact-byte gate from first byte to EOF;
2. independently re-derived the generic topos, quantale, localic-gate,
   actual/standard-owner, and dilation arguments;
3. inspected the exact P9, P10, and P11 local-owner passages used by the
   manuscript;
4. freshly hashed and inspected all seven Stage-17 Route records and the
   control manifest fields needed by Tables 3 and 4;
5. rebuilt the manuscript in a fresh isolated temporary directory with the
   recorded XeLaTeX/BibTeX sequence;
6. compared the rebuilt and frozen PDFs by extracted text, metadata, page
   geometry, fonts, and renderability; and
7. rendered and visually inspected all 12 frozen PDF pages, with additional
   table checks on pages 4, 6, 8, and 10.

This is a theoretical-paper review. There are no inferential statistics,
effect sizes, confidence intervals, or model fits to recompute. The finite
counts are deterministic receipts; the reviewer independently checked
`3436 - 84 = 3352` and `48 + 42 = 90` without treating either equality as
theorem evidence.

## 2. Frozen exact-byte passport

| Frozen input | SHA-256 | Lines | Bytes | Result |
|---|---|---:|---:|---|
| `notes/pre_manuscript_exact_byte_gate.md` | `157eae8af4efc7916652738d63afe6996e61628b7110620e4cdecacb0bc18633` | 500 | 29,628 | full-read; match |
| `paper/manuscript.tex` | `66e6434bf3b2bfaaac2b5abc2ff04c3cb49bf42a5d230c31e4354a91a8d65f2d` | 351 | 37,145 | full-read; match |
| `paper/references.bib` | `d589a945639dd83fe0c24d643fa1900b0da89171a72163e915fdecb6f456ed67` | 42 | 1,712 | full-read; match |
| `paper/README.md` | `460817961461d977ac9ccdc2af1ba08b2245ec440cb146bf9dbbaaa6e95667fc` | 112 | 8,911 | full-read; match |
| `paper/paper.pdf` | `bc8cd24b354c618213b70c34385960e4411fea84e689daed75ce03951d3d77cd` | 12 pages; 678 raw LF-count lines | 123,895 | all pages read; match |

The review target `notes/peer_review_round1.md` was absent before this report
was created. No candidate, bibliography, README, PDF, control, Route, source,
or pipeline file was modified.

The seven Stage-17 YAML hashes also remain exact:

```text
GEN-INDISC-R-ACTION-TOPOS-QF-CONTROL       77db1521f1d7cdc9e030e1c26148472e4fe4a772bc4a7c90c27dcabc26822672
GEN-INDISC-Z-ACTION-TOPOS-CONTROL          47c04d015036dcefc95f315bd862996cd3653885b09584d27ee7e07c1492848e
DEN-EF-ORBIT-ACTION-GRPD                    6ea677a679197d053520de03bade7fb3fcba89c6b10aa9eb8a97955883f7ae9d
DEN-EF-PACKET-ACTION-GRPD-P                 d3469e7cf52ed9e84ed3a5f79fcf5ca593a6e60e7bdab8a43b47398c24c5cb91
DEN-EF-ORBIT-STD-CIRCLE-PROXY               163dc6153aafc66bb3209ea51cf8199c32d997e921bcac6707f328aacb4de673
DEN-EF-ORBIT-STD-CIRCLE-COMPARISON-P        b191133dfb4a892b78800dac2b435c0ec58e80cc1ced745cdea08112d7bca727
UNMARKED-PERIOD-SCALING-CONTROL             d1de29ee6708c7846b6f03198fbd9335edfd3c6683928201772513681de58e14
```

## 3. Overall assessment

The Technical Note's mathematical center is sound and appropriately narrow.
For a nonempty globally indiscrete right `H`-space, the manuscript gives a
valid direct description of equivariant étale spaces, computes the bare
arrow-open quantale, keeps the localic comparison hypotheses separate, and
uses an explicit unequal-period dilation to prove only unmarked scale
nonrecovery. The disconnected `Z` control prevents the connected-`R`
specialization from becoming an assertion for arbitrary `H`. The actual and
standard-circle owners are not used interchangeably in any proof or table.

The contribution is nonredundant at the Technical-Note scale: T1 is the
owner/domain firewall, T2 separates theorem premises and evidence roles, T3
records the finite diagnostic receipt, and T4 records the Stage-17 Route
disposition. F1 and F2 would duplicate those mappings and are correctly
omitted. The paper does not manufacture analytic, determinant, spectral, or
publication credit from the negative Route result.

One sentence nonetheless widens the exact P10 prior-work record from the
authorized P10-1--P10-4 scope to P10's separately excluded copied-component
branch. Because owner discipline is a stated contribution of the note, the
phrase must be corrected before the candidate can pass peer review. The defect
is localized and leaves the core proofs intact, so the per-finding impact is
Minor rather than Major.

## 4. Independent mathematical and TN audit

| TN | Independent check and manuscript anchor | Result |
|---|---|---|
| TN-00 | Title/abstract/Introduction/Declarations identify a Technical Note, deny standalone/full-paper promotion, and preserve `STANDALONE_PASS=false` in the candidate receipt. | PASS |
| TN-01 | Lines 97--105 use the range-first operations `r(x,h)=x`, `s(x,h)=x·h`, `(x,h)(x·h,k)=(x,hk)`, and the matching inverse. Direct action-law substitution verifies source/range and multiplication. | PASS |
| TN-02 | Lines 140--147 correctly show both range and source are open: every nonempty arrow open is `X x U`, and each structure-map image is all of `X`. For usual `R`, every arrow neighborhood contains multiple time values, so range is not locally injective. | PASS |
| TN-03 | Lines 149--162 correctly decompose any étale space over nonempty indiscrete `X` into disjoint global sheets. Intersecting global sheets either gives the empty set or, by openness and the only nonempty base open, forces equality. Groupoid actions on those sheets are exactly continuous discrete left `H`-actions. | PASS |
| TN-04 | Lines 162--166 correctly use connectedness of usual `R` to make every orbit map into a discrete set constant, while discrete `Z` admits all set actions and the regular nontrivial action. | PASS |
| TN-05 | Lines 168--180 correctly identify arrow opens with `O(H)`, transport product and involution, compute the right-sided elements as `empty` and `H`, and exclude an open unit for usual `R`. | PASS |
| TN-06 | Lines 199--205 do not collapse bare `O(H)`, the product-frame comparison `q_H`, and local compactness. The reconstruction claim is explicitly conjunctive and localic. | PASS |
| TN-07 | Lines 207--209 correctly locate indistinguishable-point loss before localic reconstruction, at the `Top -> Loc` passage; no source theorem is credited with reconstructing discarded topological points. | PASS |
| TN-08 | Lines 211--229 keep the actual triple `Set/O(R)/2` separate from the imposed standard-circle triple `BZ/O(S_L x R)/O(S_L)`. No comparison map, topology transport, or union owner is inferred. | PASS |
| TN-09 | Lines 231--248 give a valid groupoid isomorphism under simultaneous dilation of unit and time. The strict-time-identity alternative is explicitly additional structure, so the conclusion is only numerical nonrecovery by the unmarked interface. | PASS |
| TN-10 | Lines 240--242 import only actual indiscreteness and the literal fixed-prime stabilizer input, then apply the generic theorem; they do not infer `p` or numerical `log p` from the output. | PASS |
| TN-11 | Line 244 uses the correct prior-subtraction mode and cites P10 only here, but the phrase “copied-component collapses” exceeds the frozen P10-1--P10-4 locator and its copied-owner exclusion. | **REVISE — W1** |
| TN-12 | Lines 250--278 and Table 3 keep the failed historical tuple separate from the no-retry replacement tuple, reproduce the exact finite counts, and repeatedly deny theorem credit to the controls. | PASS |
| TN-13 | Lines 280--303 and Table 4 reproduce the seven exact YAML rows: four exploratory, three rejected, every A2--A4 value `FAIL`, and Route B false for all seven. | PASS |
| TN-14 | Lines 305--312 state a scoped absence on the evaluated interfaces, not a universal impossibility theorem for every future enrichment. | PASS |

The most important proof attacks were resolved as follows:

- The étale-space argument is not silently assuming `X` is a singleton. Every
  local trivialization maps onto the sole nonempty open `X`; two such sheets
  that meet have a nonempty open intersection whose image is again `X`, so
  they coincide globally.
- The action on sheets cannot retain an untyped `x`-dependence. Opens in the
  relevant product are saturated in the indiscrete `X` coordinate, and the
  action continuity condition reduces precisely to continuity of the discrete
  `H`-action.
- The bare quantale computation is not being used as an étale shortcut. Its
  product, right-sided base, comparison map, and localic reconstruction gate
  are separately stated.
- The dilation obstruction does not prove that marked or enriched structures
  can never retain a period. It proves only that an isomorphism-invariant of
  the stated unmarked output cannot return unequal original periods.

```text
TN_RECORDS_PRESENT=15_OF_15
TN_INTERNAL_MATHEMATICS_PASS=15_OF_15
TN_OWNER_SOURCE_SCOPE_PASS=14_OF_15
TN_OWNER_SOURCE_SCOPE_REVISE=TN-11
HIDDEN_THEOREM_PROMOTION=NONE
HIDDEN_ANALYTIC_OR_ROUTE_PROMOTION=NONE
```

## 5. Finding ledger

### W1 — TN-11 widens the frozen P10 record to an excluded copied owner

**Problem:** The visible prior-work sentence attributes “copied-component
collapses” to P10 inside Paper 17's TN-11 subtraction. The frozen P10 source
row is limited to the claim ledger at P10 lines 132--135 and P10-1--P10-4 with
scope stops at lines 201--306. It authorizes separated,
continuous-observable, Borel/measurable-map, and positive-finite-measure
collapse only. `composition_blueprint_amendment_v1.md` lines 250--266 and the
final exact-byte gate line 137 explicitly exclude the proxy/copied-component
branch from this Paper-17 source role.

**Evidence Anchor:** `text: manuscript.tex line 244 / PDF page 7 “Paper 10 classified separated, measurable, and copied-component collapses”`

**Why it matters:** The cited copied-component result lives on a separately
declared tagged-coproduct owner outside the frozen P10-1--P10-4 locator. The
current wording therefore expands both the visible source role and the owner
surface of a note whose claimed contribution is exact owner typing. The core
topos, quantale, and dilation proofs do not depend on the phrase.

**Minimum remedy:** Restrict the P10 clause to the four authorized roles, for
example “separated, continuous-observable, measurable, and
positive-finite-measure collapses,” and retain the explicit prior-subtraction
ceiling. Pin the P10 citation to ledger lines 132--135 and P10-1--P10-4/scope
stops at lines 201--306. Then rebuild, freeze a new four-file tuple, and rerun
the claim/owner and PDF checks. Do not import P10's P10-5, proxy,
copied-component, operator, Route, or other excluded fields.

**Severity:** Minor — the current bytes fail the exact owner/source ceiling,
but a limited local revision closes the defect and no core theorem changes.

**Confidence:** 5/5 — direct comparison of the candidate sentence, the exact
P10 source, amendment v1 source row, and final exact-byte gate.

| Severity | Open count |
|---|---:|
| Critical | 0 |
| Major | 0 |
| Minor | 1 |

## 6. Owner, Route, and finite-control audit

All seven T1 owner rows are present, distinct, and internally consistent:

```text
GENERIC_R_ACTUAL
GENERIC_Z_FALSIFIER
ACTUAL_ORBIT_P
ACTUAL_PACKET_P
STANDARD_CIRCLE_PROXY
ACTUAL_STANDARD_COMPARISON
UNMARKED_SCALING_CONTROL
```

No mathematical proof transports standard topology to an actual owner,
actual arithmetic provenance to the proxy, or a strict marker to the unmarked
control. The only source-role drift is W1's P10 historical phrase; it does not
populate T1, T4, or any A-coordinate.

Fresh inspection of the seven YAMLs gives the exact table below.

| Owner class | A0 | A1 | A2 | A3 | A4 | Verdict | Route B |
|---|---|---|---|---|---|---|---|
| generic `R` | FAIL | FAIL | FAIL | FAIL | FAIL | rejected | false |
| generic `Z` | FAIL | FAIL | FAIL | FAIL | FAIL | rejected | false |
| actual orbit | ARITH | FAIL | FAIL | FAIL | FAIL | exploratory | false |
| actual packet | ARITH | FAIL | FAIL | FAIL | FAIL | exploratory | false |
| standard proxy | WEAK | WEAK | FAIL | FAIL | FAIL | exploratory | false |
| actual/standard comparison | WEAK | FAIL | FAIL | FAIL | FAIL | exploratory | false |
| unmarked scaling control | FAIL | WEAK | FAIL | FAIL | FAIL | rejected | false |

The control manifest independently confirms 9 CSVs, 3,436 body rows, 84
explicit negatives, 3,352 nonnegative rows, 48 semantic mutation classes, 42
package mutation classes, and 180 test methods. The manuscript's two-fresh,
three-copy, and zero-residue values match the frozen control review receipt.
None of these values is used to prove connectedness, non-etaleness, a topos
equivalence, local compactness, reconstruction, or scale nonrecovery.

## 7. Citation and bibliography structure

The structural graph contains exactly five cited keys and five bibliography
entries:

```text
forssell2013
protinresende2012
wang2026packets
wang2026reflections
wang2026convolution
```

There is no bibliography or citation orphan. Moerdijk and DOI
`10.1090/S0002-9947-1988-0973173-9` are absent from the visible manuscript and
bibliography. Forssell is used once as framework vocabulary and receives no
credit for the direct Paper-17 theorem. Protin--Resende is used for quantale
and localic framework/domain roles; the `Top -> Loc` loss-location sentence is
explicitly Paper 17's typed inference. P9 is confined to TN-10. P10 is cited
only in TN-11, but W1 identifies the one over-broad object named there. P11 is
used for the range-first convention, the standard owner, and TN-11
subtraction without transferring an actual/standard field.

This peer review does not consume or predict the result of the separate
independent citation audit. Its structural and claim-scope checks were
performed afresh from the candidate and frozen sources.

## 8. Trace, tables, omission branch, and nonredundancy

Mechanical inspection gives:

```text
TABLE_ENVIRONMENTS=4
TABLE_LABELS_TAB_T1_THROUGH_TAB_T4=4
SIX_KEY_TRACE_RECORDS=4
EACH_TRACE_HAS_SIX_NONEMPTY_KEYS=true
ACTIVE_ASSOCIATIONS=12
ASSOCIATION_CARDINALITIES=T1:5,T2:4,T3:1,T4:2
TRACE_MARKERS_TOTAL=11
TRACE_MARKERS_UNIQUE=11
TN14_ACTIVE_JOIN=T1_AND_T4
FIGURE_ENVIRONMENTS=0
F1_TERMINAL_BRANCH=OMITTED_BY_COMPOSITION
F2_TERMINAL_BRANCH=OMITTED_BY_COMPOSITION
F1_THREE_ZERO_COUNTS=0,0,0
F2_THREE_ZERO_COUNTS=0,0,0
```

The four tables have different inferential jobs and do not duplicate one
another. T1/T2 make the abstract owner/premise distinctions inspectable; T3
is the only numeric control receipt; T4 is the only Route disposition table.
No fifth table or figure is needed. The all-and-only-active join is exact, and
the omitted F1/F2 planning associations do not appear as manuscript objects,
mentions, or activated obligations.

## 9. Bilingual abstract audit

The independently worded English and Chinese abstracts preserve the same
eight facts in the same order:

| Order | Fact parity | Result |
|---:|---|---|
| 1 | owner-sensitive nonstandalone Technical Note; two parallel point-free interfaces | PASS |
| 2 | direct generic topos and bare quantale/base computations on the frozen indiscrete domain | PASS |
| 3 | usual connected `R -> Set` versus discrete `Z -> BZ` | PASS |
| 4 | bare `O(H)`, `q_H`, and local compactness separated; loss at `Top -> Loc` | PASS |
| 5 | actual `Set/O(R)/2` versus imposed standard `BZ/O(S_L x R)/O(S_L)`; no transfer | PASS |
| 6 | unmarked scale nonrecovery; strict marking extra; no recovery of numerical `log p` | PASS |
| 7 | controls are diagnostic/serialization receipts only | PASS |
| 8 | four exploratory, three rejected, universal A2--A4 failure, no determinant continuation, Route B closed | PASS |

Numbers, owner distinctions, hedges, and negative ceilings agree. The Chinese
abstract contains 279 Han characters under the frozen counting convention and
is not a sentence-by-sentence copy of the English abstract.

## 10. Independent build and 12-page visual audit

The isolated build used exactly:

```text
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

The build completed without LaTeX/BibTeX errors, unresolved citations,
unresolved references, multiply defined labels, overfull boxes, missing
characters, or a rerun request. Three underfull-box diagnostics occur at
source lines 222--226 and 318--319; inspection of the corresponding PDF text
shows no overlap, clipping, or ambiguity, so they are not findings. The fresh
PDF has 12 A4 pages, is unencrypted and text-extractable, passes Ghostscript
`nullpage`, and embeds/subsets/Unicode-maps all seven fonts. Its extracted
text is byte-identical to extracted text from the frozen PDF. The regenerated
binary has a different creation timestamp, so its binary hash is not used to
replace or validate the frozen PDF hash.

Page-by-page visual results:

| Page(s) | Content checked | Result |
|---|---|---|
| 1--2 | title metadata, English abstract, Chinese abstract and keywords | legible; no clipping or symbol substitution |
| 3 | conventions, equations (1)--(2), localic comparison, section transition | legible; equations and symbols intact |
| 4 | T1 plus openness/topos proofs | all seven rows visible; no overflow; proof text intact |
| 5 | connected/disconnected split, bare quantale, localic-gate opening | legible; formulas and citations intact |
| 6 | T2 plus actual/standard triples | four rows and column boundaries legible; no misleading merge |
| 7 | owner firewall continuation, dilation, fixed-prime and subtraction prose | legible; W1 is semantic, not a rendering defect |
| 8 | controls and T3 | four rows, counts, caption, and limitation legible |
| 9 | control limits and Route section | legible; no empty or clipped region |
| 10 | T4, scoped negative result, conclusion opening | seven rows and all A0--A4 values legible |
| 11 | conclusion and declarations | all declaration stops visible and readable |
| 12 | five-entry references | all entries, local paths, hashes, and DOIs readable |

One below-finding-threshold layout note remains: the deferred T4 float appears
between “the finite controls and” at the bottom of page 9 and “Route files” on
page 10, interrupting one limitations sentence. It does not alter content or
trace fidelity, but placing T4 before that paragraph without the mid-sentence
float interruption would improve final typesetting polish.

## 11. Strengths and adversarial coverage

### Strengths

1. The theorem premises are unusually explicit. The `R/Z` falsifier and T2
   prevent the generic topos statement from collapsing into an unqualified
   connected-time claim.
2. The actual/standard firewall is enforced in formulas, prose, tables,
   limitations, and conclusion rather than only in metadata.
3. The paper makes a useful negative result precise: scale is lost by one
   named unmarked passage, while strict marking is admitted as extra
   structure. This is stronger and safer than a vague impossibility claim.
4. The finite-control and Route ceilings are repeated consistently and do not
   substitute computation for symbolic proof.

### Strongest counter-argument

The strongest challenge is that the indiscrete unit might make the entire
action groupoid invisible, reducing both interfaces to trivial objects and
rendering the owner comparison cosmetic. The manuscript defeats the first
half of that challenge: equivariant sheaves retain exactly continuous
discrete `H`-actions, so usual connected `R` and discrete `Z` have different
classifying topoi; the bare quantale simultaneously retains the full frame
and open-set multiplication of `H`. The standard-circle comparison is also
not presented as an actual-owner theorem. The remaining vulnerability is not
in those proofs but in prose-level owner discipline: W1 imports one excluded
P10 copied-owner label into TN-11. Correcting that phrase restores the same
typing discipline to the prior-work subtraction.

### Coverage receipt

| Dimension examined | Evidence surface | Outcome |
|---|---|---|
| logical validity | Sections 2--5, Propositions 3.1/3.3, Theorem 3.2 | PASS |
| owner/domain validity | T1, Sections 4--5, P9/P10/P11 passages | W1 Minor |
| reconstruction scope | T2, Section 4, localic source domain | PASS |
| controls/reproducibility | Section 6, T3, manifest, isolated build | PASS |
| Route/negative claims | Section 7, T4, seven YAMLs | PASS |
| trace/nonredundancy | README six-key traces, markers, T1--T4, omission receipts | PASS |
| bilingual parity | both abstract blocks | PASS 8/8 |
| PDF/formatting | all 12 pages; T1 p.4, T2 p.6, T3 p.8, T4 p.10 | PASS with one non-finding float note |
| declarations/editorial readiness | title metadata and Declarations | author confirmation required; separate stop |

## 12. Technical verdict versus author-confirmation stop

### Technical peer verdict

```text
TECHNICAL_PEER_VERDICT=MINOR_REVISION
CORE_MATHEMATICAL_VALIDITY=PASS
OPEN_TECHNICAL_FINDINGS=C0/M0/m1
PEER_PASS_ON_CURRENT_BYTES=false
```

W1 must be corrected and the changed candidate must receive a new exact-byte
freeze, clean build, and independent claim/owner check. This review does not
authorize editing any file and does not pre-approve the revised bytes.

### Separate author-confirmation and release stop

`AUTHOR TO CONFIRM` remains visible in the author metadata and the declarations
for authorship, affiliation, correspondence, CRediT roles, funding, competing
interests, acknowledgments, ethics/consent scope, repository/archive IDs,
licenses, and venue-specific AI-use wording. Those facts cannot be inferred
from P9/P10/P11 or supplied by peer review.

```text
AUTHOR_CONFIRMATION_COMPLETE=false
CANDIDATE_FREEZE_ELIGIBLE=false
FINAL_ELIGIBILITY=false
RELEASE_AUTHORIZED=false
ROUTE_OR_CONTROL_MUTATION_AUTHORIZED=false
GIT_MUTATION_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
```

The author stop would remain even if W1 were corrected. Conversely, the
existence of author placeholders does not change W1's Minor severity or the
core mathematical PASS.

```text
THIS_FILE_SHA256=EXTERNAL_BY_CONSTRUCTION
THIS_FILE_LINES=EXTERNAL_BY_CONSTRUCTION
THIS_FILE_BYTES=EXTERNAL_BY_CONSTRUCTION
```

This report's stable SHA-256, line count, and byte count must be computed only
after the final byte is closed and reported externally.

## 13. Freeze 2 append-only independent peer re-review

Re-review date: **2026-08-17 (Asia/Shanghai)**  
Reviewer role: independent manuscript peer re-reviewer, with methodology,
domain, devil's-advocate, trace, formatter, and PDF-visual checks  
Candidate ceiling: **nonstandalone Technical Note**  
Technical recommendation on the Freeze-2 bytes: **MINOR REVISION**  
Effective Freeze-2 technical findings: **`C0/M0/m1`**

```text
PEER_REVIEW_ROUND=1
PEER_REVIEW_FREEZE=2
REVIEW_MODE=FRESH_APPEND_ONLY_RE_REVIEW
FROZEN_INPUT_HASH_DRIFT=0
FREEZE1_W1_STATUS=CLOSED
CITATION_M01_ORIGINAL_DEFECT=CLOSED
CITATION_M02_STATUS=CLOSED
CITATION_M03_STATUS=CLOSED
NEW_FREEZE2_FINDING=W2
CORE_MATHEMATICAL_VALIDITY=PASS
TN_RECORDS_PRESENT=15_OF_15
TN_MATHEMATICS_OWNER_AND_SOURCE_SCOPE=15_OF_15_PASS
TECHNICAL_PEER_VERDICT=MINOR_REVISION
EFFECTIVE_FINDINGS=C0/M0/m1
AUTHOR_CONFIRMATION_STOP=REQUIRED_SEPARATE_FROM_TECHNICAL_VERDICT
CANDIDATE_FREEZE_ELIGIBLE=false
FINAL_OR_RELEASE_ELIGIBILITY=false
STANDALONE_PASS=false
ROUTE_OR_CONTROL_MUTATION_AUTHORIZED=false
GIT_OR_PUBLIC_SYNC_AUTHORIZED=false
```

The prior mathematical and source-scope defect is repaired. The sole new
finding is an exact-locator mismatch in the Freeze-2 README: the T3 artifact
and visual receipt place the table object on PDF page 8, but the frozen PDF
and an independent rebuild place the T3 caption and table on page 9. This is
localized trace-metadata drift. It does not affect the proof, bibliography,
table contents, or rendered legibility, but the current exact bytes cannot
receive a peer PASS while their own trace passport contradicts the PDF.

### 13.1 Fresh rule and independence receipt

Before adjudicating Freeze 2, the reviewer freshly read the ARS-Codex
`academic-research-suite` root instructions and the directly applicable
academic-paper-reviewer workflow, re-review protocol, peer-review template,
methodology reviewer, domain reviewer, devil's-advocate reviewer, formatter,
integrity-verification, claim-reference-alignment, citation-compliance,
bilingual-abstract, visualization, PDF-visual-verification, and
figure/table-trace instructions in full.

The reviewer then reread the remediation gate, the four candidate files, the
full prior peer report prefix, the frozen proof/peer-review authority, the
composition blueprint and both amendments, the owner-specific P9/P10/P11
passages, the controls/manifest receipts, the integrated/Route authority, and
the prior citation findings relevant to M-01--M-03. The dispositions below
were independently recomputed from the Freeze-2 bytes. No concurrent citation
verdict was imported into the peer decision.

This remains a theoretical-paper review. There are no statistical estimates,
effect sizes, intervals, or model fits to recompute. The finite counts are
deterministic diagnostic receipts; `3436 - 84 = 3352` and `48 + 42 = 90` were
rechecked without treating either equality as proof of a topological claim.

### 13.2 Append-only prefix and frozen-input passport

The write-before check established the required immutable prefix:

```text
PREFIX_PATH=papers/17-open-groupoid-interfaces/notes/peer_review_round1.md
PREFIX_BYTES=24453
PREFIX_LINES=456
PREFIX_SHA256=e31fface05a61a811dff52f1eaecead9a8b2405727ac69c758b700e0f223774d
PREFIX_MATCH=true
```

The Freeze-2 tuple and gate matched exactly before this append:

| Frozen input | SHA-256 | Lines/pages | Bytes | Result |
|---|---|---:|---:|---|
| `paper/manuscript.tex` | `dc6471b03dbd4e9017909a67ea121000fa6e11172b887aba3cc5e9391d8c9b54` | 351 lines | 37,611 | full-read; match |
| `paper/references.bib` | `d589a945639dd83fe0c24d643fa1900b0da89171a72163e915fdecb6f456ed67` | 42 lines | 1,712 | full-read; match |
| `paper/README.md` | `b12ec948736fd202578204ad2d8c5ea4f58bf1c11b3743cd49fc135df8de40f6` | 168 lines | 15,395 | full-read; match |
| `paper/paper.pdf` | `0f01b3427cb7c576973e1c451609d132343937b08dc3ae6709d6b385844daf50` | 12 pages | 124,544 | all pages read; match |
| `notes/manuscript_remediation_gate_v1.md` | `66ccb9bdaa7ce12febfacbc1fab1cc742c85e94e9631fdb385e0ee768454a840` | 613 lines | 31,329 | full-read; match |

No manuscript, bibliography, README, PDF, proof, control, Route, source,
pipeline, or Git file was modified by this peer lane.

### 13.3 Disposition of Freeze-1 W1 and citation M-01--M-03

| Prior finding | Independent Freeze-2 evidence | Disposition |
|---|---|---|
| Freeze-1 W1 / TN-11 P10 scope | `manuscript.tex` line 244 now names only separated universal-image, continuous scalar-observable, Borel/measurable-map on the stated target domain, and positive-finite-measure collapses; it gives the claim-ledger lines 132--135 and exact P10-1--P10-4 line ranges 201--306. No copied-component, proxy, completion, or P10-5 role remains. | **CLOSED** |
| citation M-01 / four bare trace arrays | README lines 40--120 now contain four complete claim-text-primary six-key T1--T4 records and all twelve supported-claim associations, with unique current TeX marker/line/table/PDF locators. The original structural absence is repaired. W2 below is a new artifact-page mismatch, not survival of the old bare-array defect. | **CLOSED AS ORIGINALLY FRAMED** |
| citation M-02 / over-broad P10 attribution and missing locator | The same exact line-244 repair confines P10 to its four authorized roles and exact local ranges, with P10 used only in TN-11. | **CLOSED** |
| citation M-03 / P11 credit for the standard triple | `manuscript.tex` line 223 says the standard triple is derived directly in Paper 17, limits P11 to owner/chart, arrow/composable-pair, range-first, and owner-splice records at exact line ranges, and expressly denies P11 topos, quantale, base, localic, comparison-triple, or Paper-17 theorem credit. | **CLOSED** |

These closures are byte-specific. They do not waive the separate independent
citation lane or pre-adjudicate its final verdict.

### 13.4 Independent mathematical, owner, and source-scope re-test

All fifteen TN records pass their mathematical and owner/source ceilings on
the new TeX bytes:

- **TN-00--TN-02:** the note visibly remains a nonstandalone Technical Note;
  the range-first operations are type-correct; range and source are open; and
  usual nondiscrete `R` prevents local injectivity, so the specialization is
  open but non-etale.
- **TN-03--TN-04:** every local-homeomorphism sheet over a nonempty
  indiscrete base extends across the sole nonempty base open. Intersecting
  sheets coincide, so equivariant etale spaces are exactly continuous
  discrete left `H`-sets. Connected usual `R` forces constant orbit maps,
  while discrete `Z` retains the regular nontrivial action, giving the
  required `Set`/`BZ` firewall.
- **TN-05--TN-07:** arrow opens are exactly `X x U`, product and involution
  transport to open-set product and inverse on `O(H)`, the right-sided frame
  is `2`, and usual `R` has no open multiplicative unit. The bare quantale,
  `q_H`, and local compactness remain separate conjunctive premises. Point
  loss is located at `Top -> Loc`, not attributed to failure of localic
  reconstruction.
- **TN-08--TN-11:** actual `Set/O(R)/2` and imposed standard
  `BZ/O(S_L x R)/O(S_L)` remain different typed owners. Simultaneous
  unequal-period dilation proves only unmarked numerical-scale nonrecovery;
  strict time is additional structure. P9 imports only actual
  indiscreteness and the literal `(log p)Z` stabilizer. The repaired P10/P11
  subtraction remains TN-11-only and creates no new theorem credit.
- **TN-12--TN-14:** historical and replacement control tuples remain
  separate and diagnostic only. The seven exact owners remain four
  exploratory and three rejected; all seven A2, A3, and A4 coordinates fail;
  Route B is false. The final negative statement is confined to the evaluated
  plain interfaces and does not become a universal impossibility theorem.

```text
TN_RECORDS_PRESENT=15_OF_15
TN_INTERNAL_MATHEMATICS_PASS=15_OF_15
TN_OWNER_DOMAIN_PASS=15_OF_15
P10_VISIBLE_CITATION_COUNT=1
P10_ROLE=TN-11_ONLY
P11_STANDARD_TRIPLE_CREDIT=false
FORSSELL_DIRECT_THEOREM_CREDIT=false
PROTIN_RESENDE_TOP_TO_LOC_ATTRIBUTION=false
HIDDEN_OWNER_OR_DOMAIN_PROMOTION=NONE
ROUTE_DISPOSITION=4_EXPLORATORY_3_REJECTED
A2_A3_A4_STATUS=ALL_FAIL
ROUTE_B_FOR_THE_SEVEN_OWNERS=false
CONTROL_THEOREM_CREDIT=NONE
```

The citation graph has eight citation commands, five distinct cited keys, and
exactly five bibliography entries: Forssell, Protin--Resende, P9, P10, and
P11. Every bibliography key is used and no sixth key is cited. Moerdijk and
DOI `10.1090/S0002-9947-1988-0973173-9` are absent from visible technical
citations and the bibliography.

### 13.5 Trace, artifact, omission, and bilingual re-test

The active trace graph is otherwise exact:

```text
TABLE_ENVIRONMENTS=4
TABLE_LABELS=T1,T2,T3,T4
SIX_KEY_TRACE_RECORDS_PRESENT=4_OF_4
ACTIVE_ASSOCIATIONS=12
ASSOCIATION_CARDINALITIES=T1:5,T2:4,T3:1,T4:2
SUPPORTED_CLAIM_LOCATORS_CORRECT=12_OF_12
TRACE_MARKERS_TOTAL=11
TRACE_MARKERS_UNIQUE=11
EACH_TRACE_MARKER_OCCURS_ONCE=true
TN14_ACTIVE_JOIN=T1_AND_T4
FIGURE_ENVIRONMENTS=0
F1_TERMINAL_BRANCH=OMITTED_BY_COMPOSITION
F2_TERMINAL_BRANCH=OMITTED_BY_COMPOSITION
F1_ZERO_RECEIPT=0,0,0
F2_ZERO_RECEIPT=0,0,0
ARTIFACT_OBJECT_PAGE_LOCATORS_CORRECT=3_OF_4
```

T1 is the owner/domain firewall, T2 separates theorem premises and evidence,
T3 is the finite-control receipt, and T4 is the Route disposition. Their jobs
remain nonredundant. F1 and F2 would duplicate mappings already visible in
T1--T4; both omission branches have zero figure objects, zero substantive
figure mentions, and zero activated figure obligations.

The English and Chinese abstracts still preserve the same eight facts in the
same order: Technical-Note/nonstandalone scope; generic topos and bare
quantale/base computations; `R -> Set` versus `Z -> BZ`; separation of
`O(H)`, `q_H`, and local compactness with loss at `Top -> Loc`; actual versus
standard triples with no transfer; unmarked scale loss and strict marking;
diagnostic-only controls; and the 4/3 Route disposition with universal
A2--A4 failure and Route B closed. Owner names, numbers, hedges, and negative
ceilings agree.

### 13.6 New Freeze-2 finding ledger

#### W2 — T3 object is on PDF page 9, while two README receipts say page 8

**Problem:** The T3 six-key record's `transformation` field states
`current locator manuscript.tex label tab:t3, PDF page 8`. The visual receipt
also states `T3 on page 8`. In the frozen PDF, page 8 contains prose that
refers forward to Table 3, but no Table-3 caption or table object. Page 9
begins with the Table-3 caption and object. The independent isolated rebuild
resolves `\newlabel{tab:t3}` to page 9. The T3 supported-claim locator at
README line 102, `paper.pdf pages 8--9`, is accurate because the TN-12 claim
begins on page 8 and its table appears on page 9; that does not cure the
artifact-object locator or the visual-receipt assertion.

**Evidence Anchors:**

- `text: paper/README.md line 96 / “current locator ... tab:t3, PDF page 8”`
- `text: paper/README.md line 164 / “T3 on page 8”`
- `visual: paper/paper.pdf page 8 / prose-only Table-3 references; no caption or object`
- `visual: paper/paper.pdf page 9 / “Table 3: Finite-control receipt” and complete object`
- `data: isolated rebuild manuscript.aux / newlabel{tab:t3} has page value 9`

**Why it matters:** The README is the candidate's exact six-key trace and
visual passport. A wrong artifact page defeats deterministic navigation and
creates an internal contradiction with both the PDF and the otherwise correct
claim locator. It does not change a theorem, source attribution, owner row,
table value, or rendered page.

**Minimum remedy:** In the candidate README only, change the T3 table-object
locator in the `transformation` field from PDF page 8 to PDF page 9 and change
the visual receipt from `T3 on page 8` to `T3 on page 9`. Preserve the
TN-12 claim locator as pages 8--9. Then compute a new README digest, freeze the
resulting four-file tuple, and independently recheck the trace passport
against the unchanged PDF. No TeX, Bib, figure, table-content, control, Route,
or source change is required by this finding.

**Severity:** Minor — exact trace fidelity fails, but the defect is confined
to two README page statements and leaves the candidate's mathematics,
citations, owners, build, and PDF content intact.

**Confidence:** 5/5 — independently reproduced by frozen-PDF text extraction,
all-page rendering, and the rebuilt auxiliary label.

| Severity | Open count |
|---|---:|
| Critical | 0 |
| Major | 0 |
| Minor | 1 |

### 13.7 Clean build and twelve-page visual re-test

The reviewer copied the frozen TeX and Bib into a fresh temporary directory
and ran the required sequence:

```text
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

All four commands exited 0. The final log has no unresolved citation or
reference, multiply defined label, overfull box, missing character, fatal
error, or rerun request. It contains only two underfull-box notices at source
lines 318--319, with no visible clipping or ambiguity. BibTeX reports zero
warnings. Frozen and rebuilt PDFs both pass Ghostscript `nullpage`, have 12
A4 pages, are unencrypted and text-extractable, and embed/subset/Unicode-map
all seven fonts. Their layout-text extractions have the identical SHA-256
`c44799e45e8657be6cd569a31b2b34781ebcfb5c44dfa20b7eac74538deb3e58`.
The rebuilt binary differs by creation metadata and is not substituted for
the frozen PDF.

Every frozen page was rendered and visually inspected:

| Page(s) | Visual surface | Result |
|---|---|---|
| 1--3 | title metadata, bilingual abstracts/keywords, conventions, equations, Section 3 opening | legible; no clipping or symbol substitution |
| 4 | T1 and direct open/topos proofs | seven rows legible; no overflow |
| 5--6 | quantale/localic transition, T2, actual/standard triples | T2 has four legible rows; formulas and citations intact |
| 7--8 | dilation, repaired P10/P11 subtraction, finite-control prose | legible; no rendering defect |
| 9 | T3, control limits, Route opening | T3 complete and legible; establishes W2's true object page |
| 10 | T4 and scoped limitations | seven rows and A0--A4 values legible |
| 11--12 | conclusion, declaration stops, five references | complete and readable; no empty page |

The earlier below-finding-threshold T4 float note persists: T4 falls between
the end of a limitations clause on page 9 and its continuation on page 10.
The sentence remains unambiguous and the table is intact, so this remains a
typesetting-polish observation rather than a second finding.

### 13.8 Devil's-advocate and zero-weakness coverage receipt

The strongest mathematical attack is that the indiscrete unit could make the
sheet action secretly depend on the unit point, invalidating the claimed
reduction to continuous `H`-sets. It does not: every nonempty open in the
indiscrete coordinate is saturated, global sheets partition the etale space,
and continuity of the sheet-index map removes unit-point dependence while
retaining continuous `H`-dependence. The connected/disconnected falsifier
then shows that the result is not merely a statement that all actions are
trivial.

The strongest owner attack is that the standard-circle triple or the P10
collapse vocabulary could be smuggled into the actual owner. The repaired
lines 223 and 244 now block both transfers with exact positive roles and
explicit negative ceilings. The strongest Route attack is that “exploratory”
could be read as partial determinant credit; T4, limitations, and conclusion
all deny that inference, and every A2--A4 field remains failed.

| Dimension attacked | Outcome |
|---|---|
| direct topos/open/quantale logic | PASS |
| localic hypotheses and loss location | PASS |
| actual/standard and strict/unmarked owner firewalls | PASS |
| P9/P10/P11 scope and nonpromotion | PASS; prior W1/M2/M3 closed |
| seven-owner Route and control ceiling | PASS |
| bibliography and bilingual parity | PASS |
| active associations and unique markers | PASS |
| build and twelve-page visual integrity | PASS |
| exact artifact-object locator passport | **W2 Minor** |
| declarations/editorial readiness | AUTHOR TO CONFIRM; separate stop |

No additional weakness was found after the adversarial pass. W2 is the only
effective Freeze-2 peer finding.

### 13.9 Effective technical verdict and separate author stop

```text
TECHNICAL_PEER_VERDICT=MINOR_REVISION
CORE_MATHEMATICAL_VALIDITY=PASS
PRIOR_FINDINGS_RETESTED=FREEZE1_W1,CITATION_M01,CITATION_M02,CITATION_M03
PRIOR_FINDINGS_CLOSED=4_OF_4
OPEN_FREEZE2_TECHNICAL_FINDINGS=C0/M0/m1
OPEN_FINDING=W2_T3_PDF_OBJECT_PAGE_LOCATOR
PEER_PASS_ON_CURRENT_BYTES=false
```

`AUTHOR TO CONFIRM` remains visible in author metadata and declarations for
authorship, affiliation, correspondence, CRediT roles, funding, competing
interests, acknowledgments, ethics/consent scope, repository/archive
identifiers, licenses, and venue-specific AI-use wording. Those facts are
outside peer authority. They are not counted as W2 and would remain a
candidate/release stop even after W2 is repaired.

```text
AUTHOR_CONFIRMATION_COMPLETE=false
CANDIDATE_FREEZE_ELIGIBLE=false
FINAL_ELIGIBILITY=false
RELEASE_AUTHORIZED=false
STANDALONE_PASS=false
ROUTE_OR_CONTROL_MUTATION_AUTHORIZED=false
GIT_MUTATION_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
```

This append authorizes no candidate edit, source acquisition, control or
Route execution, build publication, release, Git mutation, or public sync.
The report's final full-file SHA-256, line count, and byte count must be
computed externally after the last byte closes. The immutable 24,453-byte
prefix receipt must be rechecked at that same boundary.

## 14. Freeze 3 final append-only peer closure

Closure date: **2026-08-17 (Asia/Shanghai)**  
Review mode: fresh exact-byte re-review of peer W2, with independent testing
of the same underlying locator condition called citation M-04  
Technical peer verdict on Freeze 3: **PASS**  
Effective peer findings: **`C0/M0/m0`**

```text
PEER_REVIEW_FREEZE=3
REVIEW_MODE=FRESH_APPEND_ONLY_CLOSURE
FREEZE2_PREFIX_PRESERVED=true
FREEZE1_NESTED_PREFIX_PRESERVED=true
W2_VERDICT=FULLY_ADDRESSED
W2_STATUS=CLOSED
CITATION_M04_UNDERLYING_CONDITION_INDEPENDENTLY_RETESTED=PASS
CITATION_LANE_VERDICT_USED_AS_PEER_EVIDENCE=false
NEW_OR_REGRESSION_FINDINGS=NONE
TECHNICAL_PEER_VERDICT=PASS
EFFECTIVE_FINDINGS=C0/M0/m0
PEER_PASS_ON_CURRENT_BYTES=true
AUTHOR_CONFIRMATION_STOP=REQUIRED_SEPARATE_FROM_TECHNICAL_VERDICT
CANDIDATE_FREEZE_ELIGIBLE=false
FINAL_OR_RELEASE_ELIGIBILITY=false
STANDALONE_PASS=false
```

### 14.1 Fresh rule, yardstick, and prefix receipt

The reviewer freshly reread the ARS-Codex academic-research-suite root, the
academic-paper-reviewer workflow and re-review protocol, the integrity
verification artifact-trace rules, the claim-reference-alignment rules, and
the figure/table-trace example. The controlling yardstick was kept unchanged:
the W2 text and evidence anchors in the immutable Freeze-2 peer prefix, plus
the exact Freeze-3 remediation contract. The later citation-lane outcome was
not used as evidence for the peer verdict.

Before this append, both required historical prefixes matched:

```text
FREEZE2_PEER_PREFIX_BYTES=42377
FREEZE2_PEER_PREFIX_LINES=808
FREEZE2_PEER_PREFIX_SHA256=426639bb2b07199942df3424b6e3034acf9f974845081de55466d82f62b440a9
FREEZE2_PEER_PREFIX_MATCH=true
FREEZE1_NESTED_PREFIX_BYTES=24453
FREEZE1_NESTED_PREFIX_LINES=456
FREEZE1_NESTED_PREFIX_SHA256=e31fface05a61a811dff52f1eaecead9a8b2405727ac69c758b700e0f223774d
FREEZE1_NESTED_PREFIX_MATCH=true
```

The exact Freeze-3 passport was:

| Input | SHA-256 | Lines/pages | Bytes | Result |
|---|---|---:|---:|---|
| `paper/manuscript.tex` | `dc6471b03dbd4e9017909a67ea121000fa6e11172b887aba3cc5e9391d8c9b54` | 351 lines | 37,611 | unchanged read-only identity |
| `paper/references.bib` | `d589a945639dd83fe0c24d643fa1900b0da89171a72163e915fdecb6f456ed67` | 42 lines | 1,712 | unchanged read-only identity |
| `paper/README.md` | `161a7f523c2daf32c6f015c27054e1a1a36192fcf2581158dea1cb5828436ca1` | 168 lines | 15,395 | full-read Freeze-3 repair surface |
| `paper/paper.pdf` | `0f01b3427cb7c576973e1c451609d132343937b08dc3ae6709d6b385844daf50` | 12 A4 pages | 124,544 | unchanged read-only identity; targeted page check |
| `notes/manuscript_remediation_gate_v2.md` | `fccdc745ca1c8e6a59d3768054222923f3fc9626459f2805ff0636dc73168f41` | 311 lines | 12,331 | full-read; match |

The citation report independently present at this boundary hashed as
`7cd2b9c358b0e3b88697ef06feb740d7dd5db20a2be35d9bc836503265e5ee32`
(1,015 lines; 50,944 bytes). This was recorded only as an input receipt. Its
PASS assertion did not substitute for the peer lane's W2/M-04 evidence test.

### 14.2 Precommitted closure criterion and exact delta evidence

W2 is fully addressed only if all of the following hold simultaneously:

1. the T3 six-key `transformation` field locates the table object on PDF page
   9, not page 8;
2. the visual receipt says T3 is on page 9, not page 8;
3. the TN-12 supported-claim locator remains `paper.pdf pages 8--9` because
   its prose begins on page 8 and its supporting object is on page 9;
4. PDF page 8 contains no T3 caption/object and PDF page 9 contains the exact
   `Table 3: Finite-control receipt` object; and
5. no candidate byte other than the two authorized single-character README
   substitutions changes.

The Freeze-3 evidence satisfies the criterion exactly:

- README line 96 contains the unique new substring
  `current locator manuscript.tex label tab:t3, PDF page 9`; its page-8 form
  occurs zero times.
- README line 164 contains the unique new substring `T3 on page 9`; its
  page-8 form occurs zero times.
- README line 102 retains exactly the TN-12 locator
  `paper.pdf pages 8--9`.
- Reversing only those two `9` characters to `8` on an in-memory stream
  deterministically reproduces the entire Freeze-2 README identity:
  `b12ec948736fd202578204ad2d8c5ea4f58bf1c11b3743cd49fc135df8de40f6`,
  168 lines and 15,395 bytes. Thus there is no third README change.
- Targeted extraction from the unchanged frozen PDF places the table captions
  at T1=page 4, T2=page 6, T3=page 9, and T4=page 10; page 8 has no table
  caption. The PDF remains 12 A4 pages, unencrypted, and 124,544 bytes.

```text
W2_PHASE2A_VERDICT=FULLY_ADDRESSED
W2_EVIDENCE_ANCHORS=README_LINES_96_102_164;PDF_PAGES_8_9
W2_RESIDUAL_GAP=NONE
W2_MADE_WORSE=false
W2_STATUS=CLOSED
M04_SAME_OBJECT_LOCATOR_CONDITION=SATISFIED
```

The peer lane closes W2 only. The statement about M-04 means that its factual
page-locator condition was independently reproduced and found satisfied; the
citation report remains the owner of M-04's formal citation-lane closure.

### 14.3 Trace and candidate no-regression audit

The full repaired README retains four well-formed six-key records. Mechanical
and semantic inspection gives:

```text
SIX_KEY_TRACE_RECORDS=4_OF_4
EACH_HAS_ARTIFACT_ID_SOURCE_DATA_TRANSFORMATION_CAPTION_CLAIM_SUPPORTED_CLAIMS_LIMITATIONS=true
ACTIVE_ASSOCIATIONS=12
ASSOCIATION_CARDINALITIES=T1:5,T2:4,T3:1,T4:2
SUPPORTED_CLAIM_LOCATORS_CORRECT=12_OF_12
TABLE_OBJECT_PAGE_LOCATORS=T1:4,T2:6,T3:9,T4:10
TRACE_MARKERS_TOTAL=11
TRACE_MARKERS_DISTINCT=11
TN14_ACTIVE_JOIN=T1_AND_T4
TABLE_ENVIRONMENTS=4
FIGURE_ENVIRONMENTS=0
F1_TERMINAL_BRANCH=OMITTED_BY_COMPOSITION
F2_TERMINAL_BRANCH=OMITTED_BY_COMPOSITION
F1_ZERO_RECEIPT=0,0,0
F2_ZERO_RECEIPT=0,0,0
TRACE_VERDICT=PASS
```

The supported claim text remains primary. Forward linkage is complete for all
twelve associations, and reverse inspection exposes no unlisted substantive
table use. Structural references such as introducing a registry or saying a
receipt is displayed do not create an additional data-bearing claim. TN-14
remains the sole active dual join and names both T1 and T4.

Because TeX, Bib, and PDF are byte-identical to the fully reviewed Freeze-2
tuple, the two-character README repair cannot alter any theorem, equation,
citation command, bibliography entry, owner row, control value, Route value,
abstract sentence, declaration, table content, or rendered glyph. Targeted
checks nonetheless reconfirmed four table environments, zero figure
environments, eleven unique literal markers, and five bibliography entries.

Accordingly, the prior non-trace results carry without regression on identical
bytes: all fifteen TN records pass; P10 remains TN-11-only; P11 receives no
standard-triple theorem credit; Forssell receives no direct-theorem credit;
Protin--Resende receives no direct `Top -> Loc` attribution; all seven owners
retain the 4-exploratory/3-rejected disposition; every A2--A4 value remains
failed; Route B remains false; controls remain diagnostic only; the bilingual
eight-fact parity and nonstandalone Technical-Note ceiling remain exact.

No XeLaTeX, BibTeX, PDF regeneration, control execution, or Route execution
was run in this closure lane. The no-build rule was preserved.

### 14.4 Final technical verdict and separate administrative stop

The strongest residual attack was that correcting the T3 object page might
silently shift the TN-12 claim locator from pages 8--9 or alter a neighboring
trace field. Exact reverse-delta reconstruction defeats that attack: only the
two false object-page statements changed, while the claim locator and every
other byte reconstruct the previous README exactly. No new or regression
finding remains.

```text
TECHNICAL_PEER_VERDICT=PASS
CORE_MATHEMATICAL_VALIDITY=PASS
W2_STATUS=CLOSED
OPEN_TECHNICAL_FINDINGS=C0/M0/m0
PEER_PASS_ON_FREEZE3_BYTES=true
```

This technical PASS does not resolve author-controlled facts. `AUTHOR TO
CONFIRM` remains required for authorship, affiliation, correspondence, CRediT
roles, funding, competing interests, acknowledgments, ethics/consent scope,
repository/archive identifiers, licenses, and venue-specific AI-use wording.

```text
AUTHOR_CONFIRMATION_COMPLETE=false
CANDIDATE_FREEZE_ELIGIBLE=false
FINAL_ELIGIBILITY=false
RELEASE_AUTHORIZED=false
STANDALONE_PASS=false
ROUTE_OR_CONTROL_MUTATION_AUTHORIZED=false
GIT_MUTATION_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
```

No candidate, source, control, Route, pipeline, Git, or public-sync write is
authorized by this closure. The report's final SHA-256, line count, and byte
count must be computed externally after this append, together with both
historical prefix receipts.
