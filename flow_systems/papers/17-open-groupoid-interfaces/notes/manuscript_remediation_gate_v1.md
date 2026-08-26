# Paper 17 Freeze-1 manuscript remediation gate v1

Gate date: **2026-08-17 (Asia/Shanghai)**  
Gate role: independent exact-byte authorization for one bounded Freeze-2
technical repair and two later append-only re-reviews  
Gate verdict: **PASS_TO_ONE_BOUNDED_FREEZE2_REPAIR**  
Candidate status: **HOLD; the citation and peer findings remain open**

~~~text
TARGET_ABSENT_BEFORE_WRITE=true
GATE_INTERNAL_FINDINGS=C0/M0/m0
INHERITED_CITATION_FINDINGS=C0/M3/m0:OPEN
INHERITED_PEER_FINDINGS=C0/M0/m1:OPEN
GATE_VERDICT=PASS_TO_ONE_BOUNDED_FREEZE2_REPAIR
THIS_GATE_CLOSES_ANY_FINDING=false
FREEZE2_REPAIR_LANES_AUTHORIZED=1
REFERENCES_BIB_WRITE_AUTHORIZED=false
AUTHOR_CONFIRMATION_COMPLETE=false
CANDIDATE_FREEZE_ELIGIBLE=false
RELEASE_AUTHORIZED=false
STANDALONE_PASS=false
~~~

This is an authorization gate, not a repaired candidate, a citation closure,
a peer-review closure, or a release decision. The three citation Major
findings and the peer Minor finding remain historically and effectively open
until the separately authorized append-only re-reviews inspect stable Freeze-2
bytes. The overlap between citation M-02 and peer W1 does not erase either
reviewer's finding.

## 1. Fresh ARS rule receipt

Before deciding this gate, the reviewer freshly read the ARS-Codex
academic-research-suite root instructions and the complete directly applicable
academic-pipeline, academic-paper, and academic-paper-reviewer workflows. The
reviewer also read in full the methodology-reviewer, peer-reviewer,
citation-compliance, integrity-verification, claim/reference-alignment, and
academic-paper-formatter instructions, together with the six-key artifact-trace,
VLM figure-verification, LaTeX/template, reproducibility, and PDF visual-QA
rules.

The controlling rules applied here are:

1. an authorization to repair does not close a finding;
2. claim text is the primary artifact-trace value, while a claim ID is only an
   additional join key;
3. every active claim-to-artifact association must pass both forward and
   reverse coverage;
4. exact source existence, metadata, locator support, local ownership, direct
   Paper-17 derivation, and diagnostic evidence remain separate;
5. a formatter or build lane may not widen content, hide a limitation, or
   silently correct source ownership;
6. a changed TeX source requires a fresh clean build and complete PDF visual
   inspection; and
7. any input drift, out-of-scope write, stale locator, or broadened source role
   fails closed.

No reviewer instruction is used to infer author identity, affiliation,
funding, competing interests, ethics/consent facts, contributor roles,
repository/archive identifiers, licenses, or release status.

## 2. Exact-byte authority and Freeze-1 receipt

Every textual authority in this section was read from first line to last and
freshly hashed. The Freeze-1 PDF was read page by page and independently
checked as a 12-page A4 document.

### 2.1 Final pre-manuscript authority

| Authority | SHA-256 | Lines | Bytes | Result |
|---|---|---:|---:|---|
| notes/pre_manuscript_exact_byte_gate.md | 157eae8af4efc7916652738d63afe6996e61628b7110620e4cdecacb0bc18633 | 500 | 29,628 | full-read; exact |

That gate passed at C0/M0/m0 only for creation of the first bounded candidate.
It did not pre-approve the resulting candidate, its citation review, its peer
review, or any release.

### 2.2 Freeze-1 candidate tuple

| Frozen candidate path | SHA-256 | Lines/pages | Bytes | Current role |
|---|---|---:|---:|---|
| paper/manuscript.tex | 66e6434bf3b2bfaaac2b5abc2ff04c3cb49bf42a5d230c31e4354a91a8d65f2d | 351 lines | 37,145 | repairable only under Sections 5--7 |
| paper/references.bib | d589a945639dd83fe0c24d643fa1900b0da89171a72163e915fdecb6f456ed67 | 42 lines | 1,712 | exact read-only build input |
| paper/README.md | 460817961461d977ac9ccdc2af1ba08b2245ec440cb146bf9dbbaaa6e95667fc | 112 lines | repairable only under Sections 5 and 8 |
| paper/paper.pdf | bc8cd24b354c618213b70c34385960e4411fea84e689daed75ce03951d3d77cd | 12 pages; raw LF count 678 | 123,895 | rebuild-and-overwrite output only |

The tuple is Freeze 1. The future repair must declare a new exact Freeze-2
tuple; it may not overwrite the historical identities in this gate or in either
review prefix.

### 2.3 Final independent review prefixes

| Review prefix | SHA-256 | Lines | Bytes | Effective open state |
|---|---|---:|---:|---|
| notes/citation_audit.md | 1237ce87b959315f733584de959620e465a55586a9d5a632506225194a07080a | 444 | 22,916 | HOLD C0/M3/m0 |
| notes/peer_review_round1.md | e31fface05a61a811dff52f1eaecead9a8b2405727ac69c758b700e0f223774d | 456 | 24,453 | MINOR REVISION C0/M0/m1 |

The citation report's M-01, M-02, and M-03 remain OPEN. The peer report's W1
remains OPEN. Peer W1 overlaps the copied-component part of citation M-02, but
each report retains its independent ledger and must receive its own fresh
append-only disposition.

### 2.4 Effective blueprint, amendment, and source-gate chain

| Frozen authority | SHA-256 | Lines | Bytes | Effective role |
|---|---|---:|---:|---|
| notes/composition_blueprint.md | eac20a67f3638444add12f90ac5dede4c8b3f4ca1773a8afe5586e18d1bff10d | 554 | 36,343 | immutable base |
| notes/composition_blueprint_amendment_v1.md | cfebb477128a3e1a99cb3f9fbedf3e3fce6709cc92d621f6909663f2fc25bddc | 410 | 23,112 | complete claim-text arrays and P10 ceiling |
| notes/composition_blueprint_amendment_v2.md | b95331e40c7c587568522497a73af09ba0d6d9cf0e9a7dac128c93114c8869b1 | 466 | 20,872 | active-artifact predicate and omission semantics |
| notes/pre_manuscript_source_gate.md | 1a94c73043e01b7d5861a20357abdb26edf5f7115b47d0552ddab376f197e8f9 | 839 | 42,099 | final append-only PASS C0/M0/m0 |
| notes/pre_manuscript_source_remediation_gate.md | cbde68a9d03204ded7b74c7947b67f106eaf092a59568a64b610d34276c38e52 | 208 | 9,004 | historical v1 authorization |
| notes/pre_manuscript_source_remediation_gate_v2.md | 64f33377f45b37943934da7dffbe70f601acf4aac24b1601a5195944aa1422c9 | 141 | 6,003 | historical v2 authorization |
| notes/pre_manuscript_citation_audit.md | 5ffd9617e0b009c6bfac441b8de10adefe0f366ffc73586578a1c97c2d848e88 | 362 | 24,190 | final five-seed/source-ceiling PASS |

The effective planning record is base + amendment v1 + amendment v2 in that
order. V1 supplies the complete claim text and exact P10 source role. V2
supersedes only the unconditional optional-figure obligation language. The
source gate's final Section-12/13 state is PASS C0/M0/m0; its earlier HOLD
prefixes remain historical and may not be rewritten.

### 2.5 Mathematical, owner, control, and Route closure

The following frozen chain also rehashed exactly:

| Authority | SHA-256 | Lines | Bytes |
|---|---|---:|---:|
| notes/proof_audit.md | c6810e95d15e1ccf0f1dd48045b0f890ebd98fe637c20a9a5e153e10fa1c4934 | 310 | 20,874 |
| notes/phase2_integrated_gate.md | 3d1b732bf02a6b2f73b9515a0531fdb77d7960d379c22393079c9e3d200c53c0 | 429 | 24,323 |
| notes/route_audit.md | d70ba9d029ae598863e44dbb049c49607063f682de8f7d8a8e5f2074ae531d15 | 211 | 13,035 |
| notes/phase2_postroute_note_gate.md | 981ce692e1aea1a067f9792a4c10ddaede4e89eeedc64c2c1ea7d6da27ed35d3 | 384 | 20,891 |

The seven Stage-17 records remain byte-exact:

| Owner record | SHA-256 |
|---|---|
| GEN-INDISC-R-ACTION-TOPOS-QF-CONTROL | 77db1521f1d7cdc9e030e1c26148472e4fe4a772bc4a7c90c27dcabc26822672 |
| GEN-INDISC-Z-ACTION-TOPOS-CONTROL | 47c04d015036dcefc95f315bd862996cd3653885b09584d27ee7e07c1492848e |
| DEN-EF-ORBIT-ACTION-GRPD | 6ea677a679197d053520de03bade7fb3fcba89c6b10aa9eb8a97955883f7ae9d |
| DEN-EF-PACKET-ACTION-GRPD-P | d3469e7cf52ed9e84ed3a5f79fcf5ca593a6e60e7bdab8a43b47398c24c5cb91 |
| DEN-EF-ORBIT-STD-CIRCLE-PROXY | 163dc6153aafc66bb3209ea51cf8199c32d997e921bcac6707f328aacb4de673 |
| DEN-EF-ORBIT-STD-CIRCLE-COMPARISON-P | b191133dfb4a892b78800dac2b435c0ec58e80cc1ced745cdea08112d7bca727 |
| UNMARKED-PERIOD-SCALING-CONTROL | d1de29ee6708c7846b6f03198fbd9335edfd3c6683928201772513681de58e14 |

Their disposition is still four exploratory and three rejected. Every owner's
A2, A3, and A4 is FAIL; Route B is false. Publication or review status is not
a Route coordinate, and “exploratory” is not analytic, spectral, determinant,
standalone, or full-paper success. No control or Route rerun is authorized.

## 3. Finding-to-repair map

| Repair contract | Open review finding(s) | Exact bounded defect | Closure authority |
|---|---|---|---|
| M1 | citation M-01 | README T1--T4 use bare IDs instead of complete v1 claim-text-primary records with current locators | citation append-only re-review |
| M2 | citation M-02 and peer W1 | manuscript line 244 widens P10 to copied-component/proxy/completion scope and omits its exact local locator | citation and peer append-only re-reviews independently |
| M3 | citation M-03 | manuscript line 223 grammatically overcredits P11 with the adjacent standard topos/quantale/base triple | citation append-only re-review; peer independently checks no regression |

This gate found no conflict among those contracts. All three defects are
localized to the two authorized text surfaces and the rebuilt PDF. No
bibliography change, new source, new claim, new theorem, new owner, new table,
new figure, new control, or new Route record is needed.

## 4. Sole Freeze-2 repair write set

Exactly one repair lane may write exactly these three retained paths:

~~~text
papers/17-open-groupoid-interfaces/paper/manuscript.tex
papers/17-open-groupoid-interfaces/paper/README.md
papers/17-open-groupoid-interfaces/paper/paper.pdf
~~~

The TeX and README changes must be limited to M1--M3, derivative exact
inventory/status receipts, and locator recomputation strictly required by
those changes. The PDF may only be rebuilt from the authorized TeX and the
exact read-only BibTeX file.

The following file is a mandatory read-only input before, during, and after
the repair:

~~~text
path=papers/17-open-groupoid-interfaces/paper/references.bib
required_sha256=d589a945639dd83fe0c24d643fa1900b0da89171a72163e915fdecb6f456ed67
required_lines=42
required_bytes=1712
write_authorized=false
~~~

It may be copied into an isolated temporary build directory as input, but its
repository bytes must remain exact. No bibliography entry, key, field,
locator, author, title, date, DOI, path, hash, or formatting change is
authorized.

Every other path is closed during the repair, including both review reports,
all notes and sources, the project-root README, figures, table data,
generators, build scripts, persistent auxiliaries, controls, reproduction
surfaces, Route records, pipeline state, release metadata, and Git/public
surfaces.

## 5. M1 exact trace-repair contract

README's four active table traces must replace the four bare
supported_manuscript_claims arrays with the complete amendment-v1 records
below. Each item retains the exact v1 claim_id, claim_text, and planning
locator and adds an exact current locator. A separate list of bare IDs may be
retained only as an additional index; it may not replace, abbreviate, alias,
or serve as the primary supported_manuscript_claims value.

The line and page values below are the exact Freeze-1 baseline. If the
line-preserving option in Section 7 is used and the rebuilt pagination remains
the same, these values remain the Freeze-2 current locators. Otherwise every
one of the twelve current locators must be recomputed before Freeze 2.

### 5.1 T1_OWNER_DOMAIN_INTERFACE_FIREWALL

~~~yaml
supported_manuscript_claims:
  - claim_id: TN-02
    claim_text: "For the frozen nonempty globally indiscrete right-`H` owner, `G(X,H)` is an open topological groupoid, and its usual nondiscrete-`R` specialization is non-etale."
    planned_manuscript_locator: "Section 3, Generic joint interface; TRACE_CLAIM:TN-02"
    current_manuscript_locator: "Section 3, Generic joint interface; literal TRACE_CLAIM:TN-02; manuscript.tex lines 146--147; table label tab:t1; paper.pdf page 4"
  - claim_id: TN-04
    claim_text: "For a nonempty globally indiscrete owner, connected usual `R` gives `B(G(X,R)) ~= Set`, whereas discrete `Z` gives the nontrivial falsifier `B(G(X,Z)) ~= BZ`."
    planned_manuscript_locator: "Section 3, Generic joint interface; TRACE_CLAIM:TN-04"
    current_manuscript_locator: "Section 3, Generic joint interface; literal TRACE_CLAIM:TN-04; manuscript.tex lines 165--166; table label tab:t1; paper.pdf page 5"
  - claim_id: TN-08
    claim_text: "The actual inherited owner has `Set/O(R)/2`, whereas the separately imposed standard-circle owner has `BZ/O(S_L x R)/O(S_L)`, with no topology, provenance, or coordinate transfer between them."
    planned_manuscript_locator: "Section 4, Localic gate and actual/standard firewall; TRACE_CLAIM:TN-08"
    current_manuscript_locator: "Section 4, Localic gate and actual/standard firewall; literal TRACE_CLAIM:TN-08; manuscript.tex lines 224--225; table label tab:t1; paper.pdf page 6"
  - claim_id: TN-10
    claim_text: "Fixed-prime application occurs only after the generic theorem and imports from Paper 9 only actual packet/orbit indiscreteness and the literal stabilizer `(log p)Z`, without recovering `p` or numerical `log p` from the plain interface."
    planned_manuscript_locator: "Section 5, Scale obstruction and fixed-prime application; TRACE_CLAIM:TN-10"
    current_manuscript_locator: "Section 5, Scale obstruction and fixed-prime application; literal TRACE_CLAIM:TN-10; manuscript.tex lines 241--242; table label tab:t1; paper.pdf page 7"
  - claim_id: TN-14
    claim_text: "On the evaluated plain owners and interfaces, no `C*`-algebra, Haar system, measure, trace, determinant, completed divisor, Weil compression, natural quantization, or standard-to-actual transfer is constructed."
    planned_manuscript_locator: "Section 7, Route outcome and limitations; TRACE_CLAIM:TN-14"
    current_manuscript_locator: "Section 7, Route outcome and limitations; literal TRACE_CLAIM:TN-14; manuscript.tex lines 307--308; table label tab:t1; paper.pdf page 10"
~~~

### 5.2 T2_THEOREM_PREMISE_EVIDENCE_SEPARATION

~~~yaml
supported_manuscript_claims:
  - claim_id: TN-03
    claim_text: "For every nonempty globally indiscrete right-`H`-set in the frozen domain, `B(G(X,H)) ~= B_cont(H)` by a direct classifying-topos calculation."
    planned_manuscript_locator: "Section 3, Generic joint interface; TRACE_CLAIM:TN-03"
    current_manuscript_locator: "Section 3, Generic joint interface; literal TRACE_CLAIM:TN-03; manuscript.tex lines 159--160; table label tab:t2; paper.pdf page 4"
  - claim_id: TN-05
    claim_text: "For the frozen globally indiscrete owner, the bare arrow-open quantale is `O(H)` with base frame `2`, and for usual nondiscrete `R` it is nonunital."
    planned_manuscript_locator: "Section 3, Generic joint interface; TRACE_CLAIM:TN-05"
    current_manuscript_locator: "Section 3, Generic joint interface; literal TRACE_CLAIM:TN-05; manuscript.tex lines 179--180; table label tab:t2; paper.pdf page 5"
  - claim_id: TN-06
    claim_text: "The bare quantale `O(H)`, the composable-pair comparison `q_H`, and local compactness are distinct premises, and localic reconstruction follows only when the registered conjunction holds."
    planned_manuscript_locator: "Section 4, Localic gate and actual/standard firewall; TRACE_CLAIM:TN-06"
    current_manuscript_locator: "Section 4, Localic gate and actual/standard firewall; literal TRACE_CLAIM:TN-06; manuscript.tex lines 204--205; table label tab:t2; paper.pdf page 6"
  - claim_id: TN-07
    claim_text: "For the nonsober actual owner, point loss occurs in the passage `Top -> Loc` rather than through a failure of the Protin--Resende reconstruction theorem on its localic input."
    planned_manuscript_locator: "Section 4, Localic gate and actual/standard firewall; TRACE_CLAIM:TN-07"
    current_manuscript_locator: "Section 4, Localic gate and actual/standard firewall; literal TRACE_CLAIM:TN-07; manuscript.tex lines 208--209; table label tab:t2; paper.pdf page 6"
~~~

### 5.3 T3_FINITE_CONTROL_RECEIPT

~~~yaml
supported_manuscript_claims:
  - claim_id: TN-12
    claim_text: "The final finite package comprises nine CSVs, 3,436 rows, 84 explicit negatives, 3,352 nonnegative rows, 48 semantic and 42 package mutation classes, 180 passing replacement-run tests, two fresh generations, three byte-identical copies, and zero frozen residue, all as diagnostic and serialization evidence only."
    planned_manuscript_locator: "Section 6, Finite diagnostic controls; TRACE_CLAIM:TN-12"
    current_manuscript_locator: "Section 6, Finite diagnostic controls; literal TRACE_CLAIM:TN-12; manuscript.tex lines 271--272; table label tab:t3; paper.pdf pages 8--9"
~~~

### 5.4 T4_STAGE17_ROUTE_DISPOSITION

~~~yaml
supported_manuscript_claims:
  - claim_id: TN-13
    claim_text: "The seven Stage-17 owners yield four exploratory and three rejected Route-A dispositions; every owner's A2, A3, and A4 value is `FAIL`, and Route B is false."
    planned_manuscript_locator: "Section 7, Route outcome and limitations; TRACE_CLAIM:TN-13"
    current_manuscript_locator: "Section 7, Route outcome and limitations; literal TRACE_CLAIM:TN-13; manuscript.tex lines 302--303; table label tab:t4; paper.pdf page 9"
  - claim_id: TN-14
    claim_text: "On the evaluated plain owners and interfaces, no `C*`-algebra, Haar system, measure, trace, determinant, completed divisor, Weil compression, natural quantization, or standard-to-actual transfer is constructed."
    planned_manuscript_locator: "Section 7, Route outcome and limitations; TRACE_CLAIM:TN-14"
    current_manuscript_locator: "Section 7, Route outcome and limitations; literal TRACE_CLAIM:TN-14; manuscript.tex lines 307--308; table label tab:t4; paper.pdf page 10"
~~~

For each T1--T4 block, the other five trace values are frozen exactly:
artifact_id, source_data, transformation, caption_claim, and limitations must
remain byte-for-byte the Freeze-1 values currently printed in README. M1
authorizes no change to their source hashes, derivations, table labels, caption
claims, or limitations.

After replacement, the active trace cardinalities must be exactly 5/4/1/2,
for twelve associations across eleven unique manuscript markers. TN-14 remains
the only dual active join and must resolve to T1 plus T4. Each literal marker
must occur exactly once in manuscript source. Every listed claim occurrence
must substantively cite its active table, and every substantive table use must
resolve in reverse to one of these records.

The two F1/F2 omission receipts currently printed in README must remain
byte-for-byte unchanged, including their nonempty rationales and all three
zero counts:

~~~text
artifact_id=F1_OWNER_INTERFACE_FIREWALL
terminal_branch=OMITTED_BY_COMPOSITION
manuscript_figure_or_table_object_count=0
substantive_manuscript_mention_count=0
activated_claim_obligation_count=0

artifact_id=F2_EVIDENCE_TO_ROUTE_CEILING
terminal_branch=OMITTED_BY_COMPOSITION
manuscript_figure_or_table_object_count=0
substantive_manuscript_mention_count=0
activated_claim_obligation_count=0
~~~

Their full rationales remain those in Freeze-1 README lines 74 and 83. No F1
or F2 object, file, environment, caption, label, cross-reference, incidental
pointer, data-bearing mention, inference-bearing mention, or claim obligation
may enter the manuscript or PDF.

## 6. M2 and M3 exact manuscript contracts

### 6.1 M2 — P10 TN-11 prior subtraction only

Freeze-1 manuscript line 244 must be replaced in scope without enlarging the
TN-11 claim. P10 may be described only through the frozen P10-1--P10-4 roles:

1. separated universal-image collapse;
2. continuous scalar-observable collapse;
3. Borel/measurable-map collapse on the stated target domain; and
4. positive-finite-measure collapse.

The visible P10 citation must supply this exact local source binding:

~~~text
path=papers/10-separated-reflection/paper/manuscript.tex
sha256=27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315
claim_ledger_locator=lines 132--135
P10-1_locator=lines 201--226
P10-2_locator=lines 228--245
P10-3_locator=lines 270--285
P10-4_locator=lines 287--306
support_mode=TN-11 builds-on and prior subtraction only
~~~

The repaired sentence must remove every P10 copied-component, proxy, and
completion attribution. P10 also supplies no P10-5, P10-7/P10-8,
measure-selection, owner, fixed-prime, direct Paper-17 theorem,
topos/quantale, localic-reconstruction, novelty, standalone, operator, state,
representation, support, disintegration, trace, determinant, analytic,
spectral, Route, or publication credit.

If P11 remains in the same paragraph, its clause and locator must be
grammatically separate so that no P11 field is read as P10 support and no P10
field is read as P11 support. The repair may subtract prior work; it may not
add a priority claim or broaden TN-11.

### 6.2 M3 — P11 formula/owner ceiling and Paper-17 direct triple

Freeze-1 manuscript line 223 must state unambiguously that P11 supports only
the standard-circle owner/chart, the ordinary arrow-space and composable-pair
charts, the range-first formulas/operations, and the owner-splice stop. Its
exact local binding remains:

~~~text
path=papers/11-indiscrete-convolution/paper/manuscript.tex
sha256=eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002
range_first_locator=lines 255--277
standard_owner_chart_locator=lines 313--324
arrow_composable_pair_formula_locator=lines 337--405
owner_splice_stop_locator=lines 1079--1087
~~~

The adjacent standard triple
BZ / O(S_L x R) / O(S_L)
must be explicitly assigned to Paper 17 as this manuscript's direct
derivation. P11 receives no classifying-topos, open-quantale, base-frame,
localic-reconstruction, comparison-triple, novelty, or Paper-17 theorem
credit. It supplies no actual-owner topology, provenance, coordinate, or
standard-to-actual transfer.

The revised clause must keep the actual
Set / O(R) / 2
and the separately imposed standard
BZ / O(S_L x R) / O(S_L)
owners distinct. It may clarify attribution only; it may not change either
triple, theorem statement, hypothesis, proof, or owner/domain firewall.

## 7. Locator stability and manuscript non-regression

The preferred bounded edit replaces Freeze-1 source lines 223 and 244 in
place, one source line for one source line, preserving the 351-line manuscript
and all eleven TRACE_CLAIM line positions. This preference is not permission
to force a stale page locator.

Two valid paths exist:

1. preserve manuscript line count, marker line positions, table labels, and
   rebuilt claim pagination; then the Section-5 baseline locators remain exact;
2. if any source line, marker position, table label, or PDF claim page changes,
   recompute all twelve README current locators against the final Freeze-2 TeX
   and PDF before hashing the tuple.

Partial recomputation is invalid. Historical line/page locators in the two
review prefixes must not be edited; their future append sections will identify
the Freeze-2 locators independently.

The repair must preserve all of the following:

~~~text
DOCUMENT_TYPE=TECHNICAL_NOTE
STANDALONE_PASS=false
TN_CLAIM_SURFACE=TN-00_THROUGH_TN-14
OWNER_FIREWALL_COUNT=7
INLINE_TABLES=T1,T2,T3,T4
INLINE_TABLE_COUNT=4
FIFTH_TABLE_AUTHORIZED=false
FIGURE_BRANCH=BOTH_OMITTED
FIGURE_FILE_COUNT=0
DISTINCT_TRACE_MARKERS=11
ACTIVE_ASSOCIATIONS=12
TN14_ACTIVE_JOIN=T1+T4
BIBLIOGRAPHY_ENTRIES=5
CITED_KEYS=5
CITATION_ORPHANS=0
BILINGUAL_FACT_ORDER=8
BILINGUAL_SAME_OMISSION=true
ROUTE_DISPOSITION=4_EXPLORATORY_3_REJECTED
A2_A3_A4_STATUS=ALL_FAIL
ROUTE_B=false
CONTROLS_ARE_DIAGNOSTIC_ONLY=true
~~~

No theorem, equation, proof, table row, citation seed, abstract fact, control
count, Stage-17 enum, owner token, source role, declaration fact, or limitation
may otherwise change. The non-finding T4 float note does not authorize
opportunistic layout or prose revision in this bounded lane.

## 8. README status, inventory, and author stops

README may change only to implement the complete M1 arrays, update the
Freeze-2 manuscript/PDF/README inventory and any recomputed locators, and make
the candidate-status receipt truthful for the repaired bytes.

After M1--M3, the structural checks, and the clean build all pass, the README's
technical citation/trace PASS statements and its author-confirmation
sole-underlying-stop language may be restored as an author-side Freeze-2
receipt. They must not claim that either independent report has already closed
its findings. Until the append-only re-reviews act, the README must also make
the pending independent citation and peer re-reviews visible.

The following values are immutable:

~~~text
AUTHOR TO CONFIRM=REQUIRED
AUTHOR_CONFIRMATION_COMPLETE=false
CANDIDATE_FREEZE_ELIGIBLE=false
RELEASE_AUTHORIZED=false
STANDALONE_PASS=false
TECHNICAL_NOTE=true
~~~

No author-supplied placeholder may be replaced by inferred data. In
particular, authorship, affiliation, correspondence, CRediT roles, funding,
competing interests, acknowledgements, ethics/consent, repository/archive
identifiers, licenses, and venue-specific AI-use wording remain AUTHOR TO
CONFIRM. Candidate freeze and release remain false even if every technical
repair and build check passes.

## 9. Clean isolated build and 12-page visual contract

The repair lane must build in a fresh isolated temporary directory. It may
copy only the authorized manuscript source and exact read-only BibTeX input
needed for compilation. The required sequence remains:

~~~text
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex manuscript
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
~~~

No auxiliary, log, bibliography intermediate, temporary source copy, or other
build file may be retained in the repository. Only the resulting paper.pdf may
overwrite the authorized PDF path.

Before Freeze 2, all of these checks must pass on the rebuilt output:

1. paper.pdf is exactly 12 A4 pages, unencrypted, text-extractable on every
   page, and passes a Ghostscript nullpage check;
2. the final log has no error, fatal diagnostic, undefined citation,
   unresolved reference, multiply defined label, missing character, overfull
   object, or rerun request;
3. all fonts needed by the mathematics are embedded/subset and Unicode-mapped,
   with no symbol-altering substitution;
4. exactly four table environments and labels exist; T4 remains before
   Declarations and References; all tables are legible and unclipped;
5. the bibliography remains five entries and five cited keys with zero orphans,
   no Moerdijk technical citation/entry, and no duplicate Forssell
   manifestation;
6. all eleven literal markers occur exactly once and the twelve active
   associations pass both directions;
7. F1 and F2 remain BOTH_OMITTED with no object or manuscript/PDF use;
8. the English and Chinese abstracts retain the same eight facts, order,
   numbers, owners, hedges, and omissions; and
9. every one of the 12 pages is visually inspected, including T1, T2, T3, T4,
   both abstract blocks, equations, declarations, and all five references.

The exact BibTeX hash must be checked both before and after the build. Any
change from d589a945639dd83fe0c24d643fa1900b0da89171a72163e915fdecb6f456ed67
invalidates Freeze 2.

## 10. Freeze-2 receipt and later append-only re-reviews

The repair author must freeze and externally report:

~~~text
FREEZE2_MANUSCRIPT_SHA256=<exact>
FREEZE2_MANUSCRIPT_LINES=<exact>
FREEZE2_MANUSCRIPT_BYTES=<exact>
FREEZE2_REFERENCES_BIB_SHA256=d589a945639dd83fe0c24d643fa1900b0da89171a72163e915fdecb6f456ed67
FREEZE2_REFERENCES_BIB_LINES=42
FREEZE2_REFERENCES_BIB_BYTES=1712
FREEZE2_README_SHA256=<exact>
FREEZE2_README_LINES=<exact>
FREEZE2_README_BYTES=<exact>
FREEZE2_PDF_SHA256=<exact>
FREEZE2_PDF_PAGES=12
FREEZE2_PDF_BYTES=<exact>
M1_AUTHOR_REPAIR_COMPLETE=true
M2_AUTHOR_REPAIR_COMPLETE=true
M3_AUTHOR_REPAIR_COMPLETE=true
INDEPENDENT_FINDING_CLOSURE=false
~~~

Only after a valid Freeze-2 receipt exists are two separate review writes
authorized:

1. notes/citation_audit.md may receive one fresh append-only re-review. It must
   preserve exactly the first 444 lines and 22,916 bytes at SHA-256
   1237ce87b959315f733584de959620e465a55586a9d5a632506225194a07080a,
   rehash the complete Freeze-2 tuple, re-audit M-01--M-03 from scratch, and
   retain each historical finding before declaring any closure.
2. notes/peer_review_round1.md may receive one fresh append-only re-review. It
   must preserve exactly the first 456 lines and 24,453 bytes at SHA-256
   e31fface05a61a811dff52f1eaecead9a8b2405727ac69c758b700e0f223774d,
   independently rehash the Freeze-2 tuple, re-audit W1 and all mathematical,
   owner, Route, build, and visual non-regression checks, and retain the
   historical Minor finding before declaring any closure.

The two reviews are independent. Neither reviewer may repair the candidate,
rewrite its own prefix, consume the other review as a substitute for fresh
analysis, or pre-approve a PASS. A new or surviving finding yields HOLD or
REVISE. Even two zero-finding append-only outcomes do not authorize release,
root-README edits, Git mutation, archive deposit, public sync, controls, Route,
or pipeline changes.

## 11. Fail-closed conditions

Freeze 2 is invalid and the later review writes remain unauthorized if any of
the following occurs:

~~~text
ANY_BOUND_INPUT_HASH_DRIFT
ANY_WRITE_OUTSIDE_THE_THREE_PATH_REPAIR_SET
REFERENCES_BIB_HASH_OR_BYTE_DRIFT
INCOMPLETE_OR_BARE_ID_PRIMARY_M1_ARRAY
ANY_OF_TWELVE_CURRENT_LOCATORS_STALE
ANY_OF_OTHER_FIVE_TRACE_KEYS_CHANGED
ANY_OMISSION_RECEIPT_CHANGED_OR_F1_F2_USE_INTRODUCED
P10_SCOPE_BEYOND_P10_1_THROUGH_P10_4_TN11_SUBTRACTION
P10_EXACT_LOCAL_LOCATOR_MISSING
P11_CREDITED_WITH_THE_STANDARD_TOPOS_QUANTALE_BASE_TRIPLE
PAPER17_DIRECT_DERIVATION_CREDIT_MISSING
MANUSCRIPT_LOCATORS_PARTIALLY_RECOMPUTED
TABLE_BIB_MARKER_ASSOCIATION_OR_BILINGUAL_COUNT_DRIFT
ANY_OWNER_DOMAIN_CONTROL_ROUTE_OR_STANDALONE_PROMOTION
BUILD_NOT_CLEAN_OR_NOT_ISOLATED
PDF_NOT_EXACTLY_12_A4_PAGES
INCOMPLETE_12_PAGE_VISUAL_INSPECTION
AUTHOR_PLACEHOLDER_INFERRED_OR_CANDIDATE_RELEASE_FLAG_RAISED
~~~

No control execution and no Route execution is required or authorized by this
repair. No weak Route result may be repackaged as a full paper, and publication
status supplies no missing coordinate.

## 12. Final authorization receipt

~~~text
P17_MANUSCRIPT_REMEDIATION_GATE_V1=PASS_TO_ONE_BOUNDED_FREEZE2_REPAIR
CURRENT_CANDIDATE_STATE=HOLD
CITATION_FINDINGS_REMAIN_OPEN=C0/M3/m0
PEER_FINDINGS_REMAIN_OPEN=C0/M0/m1
SOLE_REPAIR_WRITE_SET=paper/manuscript.tex,paper/README.md,paper/paper.pdf
REFERENCES_BIB=READ_ONLY_EXACT_D589A945
POST_FREEZE2_CITATION_REVIEW=APPEND_ONLY_PRESERVE_PREFIX
POST_FREEZE2_PEER_REVIEW=APPEND_ONLY_PRESERVE_PREFIX
PROJECT_ROOT_README_WRITE_AUTHORIZED=false
NOTES_WRITE_AUTHORIZED_DURING_REPAIR=false
SOURCE_OR_BIBLIOGRAPHY_WRITE_AUTHORIZED=false
FIGURE_OR_TABLE_ARTIFACT_WRITE_AUTHORIZED=false
CONTROL_OR_ROUTE_RERUN_AUTHORIZED=false
PIPELINE_WRITE_AUTHORIZED=false
RELEASE_AUTHORIZED=false
GIT_MUTATION_AUTHORIZED=false
PUBLIC_SYNC_AUTHORIZED=false
CANDIDATE_FREEZE_ELIGIBLE=false
STANDALONE_PASS=false
THIS_FILE_SHA256=EXTERNAL_BY_CONSTRUCTION
THIS_FILE_LINES=EXTERNAL_BY_CONSTRUCTION
THIS_FILE_BYTES=EXTERNAL_BY_CONSTRUCTION
~~~
