# C424–C428 bounded final-integration review

2026-09-09 UTC. **PASS AFTER ONE CLOSED DOCUMENTATION CORRECTION;
ZERO OPEN MUST-FIX — NOT A RELEASE SEAL.**

This review checks agreement between the completed manuscript/evaluation/
build gates, the current delivery summaries and the two new Hénon
registry sections. One genuine quantifier omission in HEN-O409 was
reported, corrected by the coordinator, and independently read back
below. No manuscript, mathematical program, evaluation or build was
changed by this reviewer. This report is the sole file written for this
assignment; the reviewer stops writing after handing it off.

## 1. Scope, reading and reviewer roles

The batch skill governed a bounded integration check and preservation
of existing evidence. This is not another proof certification, third
manuscript pass, formal evaluation, source search or mathematical run.
The reviewer authored C424, supplied the two nonauthor C427 manuscript
reviews, and previously wrote the bounded citation and evaluation-file
reviews. Those roles remain disclosed: this is not a fresh nonauthor
self-review of C424, blind review, human peer review or a statistically
independent error guarantee.

The following current documents were read completely for this check:

- [Manuscript adjudication](../REVIEW_ADJUDICATION.md), 94 lines;
  [evaluation adjudication](../EVALUATION_ADJUDICATION.md), 86 lines;
  [batch final-build report](../FINAL_BUILD_REPORT.md), 97 lines.
- [Release policy](README.md), 79 lines, and
  [round-six decision](../continuation_round6/ROUND6_DECISION.md),
  72 lines. The latter's actual length, not the assignment's approximate
  preliminary count, is used here.
- The five complete paper-local final-build reports: respectively
  196, 198, 172, 100 and 194 lines, totaling 860 lines.
- The 26-line active evaluation selector and 64-line reference-routing
  record; the actual probe receipt, IH6 author run log, independent IH6
  execution receipt and selected milestone/evidence passages.

Selected current-summary reading covers the new opening section of
[batch README](../README.md), the new opening section of
[CURRENT_RESEARCH_STATE.md](../../CURRENT_RESEARCH_STATE.md),
candidate-registry lines 1–40 and obstruction-registry lines 20–38.
This does not claim a new full read of their thousands of historical
registry lines. All ten manuscript reports and all seven evaluation
records were already read fully in the preceding evaluation-file review;
here their exact identities and current adjudications were rechecked,
not relabelled as ten new reviews. The underlying manuscript sources
were consulted only where needed to resolve the identified quantifier.

The separate [tree preflight](PREFLIGHT_TREE.md) and
[historical navigation](HISTORICAL_NAVIGATION.md) belong to their
assigned reviewer. Their full-tree checks were not duplicated here,
and this report does not independently certify their findings.

## 2. Actual finding and verified closure

**I1 — HEN-O409 omitted the large-orbit hypothesis. CLOSED.**

At first inspection, obstruction-registry line 25 said:
“A finite orbit is contained in the finite periodic-line union”.
That unrestricted statement loses the separate finite core. The actual
C425 revised abstract only places every *large* periodic orbit in that
union; its line-exhaustion lemma requires height M>R, while the main
theorem explicitly retains periodic orbits outside the line set inside
the core box. See
[abstract](../papers/C425_fricke_return/sections/00_abstract.tex),
[main theorem](../papers/C425_fricke_return/sections/01_introduction.tex)
and [line-exhaustion proof](../papers/C425_fricke_return/sections/05_line_exhaustion.tex).

The reviewer reported this as a required registry correction without
editing the original. The coordinator adopted it and changed only the
affected sentence to:

> A finite periodic orbit meeting the complement of the proved core box
> is contained in the finite periodic-line union; it is not itself a
> whole line and may move between lines.

The reviewer then independently reread the actual modified row and its
surrounding new section. The conditional matches the reviewed theorem
and preserves the possible finite-core remainder. I1 is closed, not
omitted from the record or retrospectively described as no finding.
No additional source edit, mathematical execution or PDF build was
required. The obstruction-register SHA256 changed from
`8426ecf62ee5eb30a0262a731cb49e69c01ce82fcc94d6114e8598890f661a1f`
to
`950c26deb76f6e59c4bb09ef878e0f291c781a1d64469e10af8d92b78534810c`.

No other open mathematical, source-scope, evidence-identity or
integration must-fix was found within this bounded assignment.

## 3. Five genuine final artifacts and build accounting

A fresh read-only Node standard-library aggregation independently
checked the literal expected PDF/report digests, each manifest member,
actual byte equality and lengths. It ran pdfinfo/pdffonts on both final
copies, inspected all 20 converged engine/BibTeX logs and counted the
actual pass/completion markers in the ten complete final transcripts.
The successful invocation exited 0 with five PASS rows.

| Paper | Two actual final directories, relative to its paper | Inputs | Pages / bytes | Font resources per selected PDF |
| --- | --- | ---: | --- | ---: |
| C424 | build/final_frozen_01; build/final_frozen_02 | 29 | 21 / 463423 | 22 |
| C425 | build_final_01; build_final_02 | 13 | 12 / 378223 | 23 |
| C426 | builds/final_01; builds/final_02 | 10 | 10 / 343725 | 20 |
| C427 | builds/final_01; builds/final_02 | 10 | 13 / 346694 | 19 |
| C428 | builds/final_01; builds/final_02 | 15 | 16 / 389314 | 19 |

Totals independently checked: **77 manifest inputs, 72 pages,
1,921,379 selected-PDF bytes, 103 embedded Type 1 font resources**.
Every manifest entry rehashed correctly; no manifest had a repeated
member. These are reproducibility inputs, not 77 TeX files or a complete
release-member ledger. In particular C424 pins source evidence/programs,
C425 includes its build script, and C427 separately records its final
wrapper/archive beyond its ten manuscript inputs.

For every paper, main.pdf, main_round1.pdf, main_round2.pdf and the two
new final PDFs compare byte-identical: 25 actual PDF copies checked,
five distinct manuscript identities. All ten final transcripts contain
three pdfLaTeX and two BibTeX passes and the completed-target message:
30 engine and 20 bibliography passes, not 50 builds or review rounds.
Their reported top-level exit codes are 0. No additional compilation
was run to re-establish these facts.

| Paper | Final PDF SHA256 | Complete final-build report SHA256 |
| --- | --- | --- |
| C424 | `3a1eadac84dd7fe9b730cde464bbc31a80469963aa984ac3a7117936e7bdf98b` | `c6d3912f9d07dc2d1d9adb00cca3fef10b3ff91334a3f3cf8113fdaec315357a` |
| C425 | `e7330f65920c40c566b01ee0d864d9f5a023c70010954e8af633c325f92c1dcb` | `a5c121ae9d4108a9ec7671bcb9d02d38cde0566b2eb370494d4dd15e564cb6bb` |
| C426 | `d0b4e14e8ed42002bf0ad454ee004c817403e9662ae92b25306a94adf4d582db` | `6fee551e5265a4da181689104cd46a3027b9e756bb36f5e51676fd5610149698` |
| C427 | `cae339b829dd8a4ca0c57accc75b3a9a3ced62173f49402e853e6d63c2d91bd1` | `8fd54f3ce12360e15ed4ad92cefbcc98c357f2a0c0d34f27b695351d520694a0` |
| C428 | `cf02bdd886584949847f2583904601bb2734010a5f9d9cafbcbe749ddb0553af` | `b085f757c78d3e6780411de7a284749da6e7bb32150592032c727a647ad3e4ef` |

The independently checked manifest SHA256 values are:

| Paper / manifest | SHA256 |
| --- | --- |
| C424 / INPUT_MANIFEST.sha256 | `ea282bedc12d736c9a0e421e5448744504ef742b593d6ebaf07368b27b090f63` |
| C425 / FINAL_INPUT_MANIFEST.sha256 | `c9e8e11efeca9502f0b610847910736f613aa283f77f3f81a01d05c443b2b878` |
| C426 / FINAL_INPUTS.sha256 | `97451e88c5b07516c7e855a494fe256c648e3787a9ff9c267c6b5e52e310cf74` |
| C427 / INPUT_MANIFEST.sha256 | `c802d78cd7ec2e4d6c3a87a1c243c657e14d7247f78514f08f6075d52627b1f9` |
| C428 / FINAL_INPUTS.sha256 | `afa96126117e48bc266cc82406cdd7a55473d799596e36c9334cabe3157e7e0c` |

The 20 converged logs have no substantive warning/error, unresolved
citation/reference or overfull/underfull diagnostic. Full first-pass
transcripts deliberately retain unconverged warnings. C424's transient
0.57625 pt message and historical initial layout correction, C425's
genuine initial failure, and the other documented revision histories
are not counted as failed final builds or hidden by the summaries.
The coordinator's earlier font-column parser error is explicitly
reported in the batch build receipt; this review used the actual
embedding column and found all final resources embedded.

Every-page final viewing is attributed to the actual builders, whose
full reports were read: C424/C425 to as3h_source_spotcheck,
C426/C428 to lyness_round5, C427 to the coordinator. Their respective
complete final text reads are 1107/614/520/645/788 lines, with
21/12/10/13/16 actual final-page views. This review did not render or
view all 72 pages again, and does not turn byte-identical pairs into
144 image views. Archive-member comparisons are likewise attributed
to the builders' complete receipts, not claimed as new extractions here.

## 4. Ten reviews and exact evaluation routing

Each of the ten actual manuscript reports rehashed to the value in
[REVIEW_ADJUDICATION.md](../REVIEW_ADJUDICATION.md). Their actual
round-1/round-2 line counts are:
C424 230/173, C425 230/203, C426 175/80, C427 292/204,
C428 145/124. Assignment, author/reviewer separation and adjudicated
changes agree with the paper-local final reports. In particular the
C428 second pass's six affected-page views are not misreported as
another all-sixteen-page review; the separate final builder viewed all
sixteen. Honest no-change round-2 aliases are distinguished from the
two real final builds of every paper.

A separate read-only restricted parser accepted the JSON-scalar,
two-space-indented YAML subset used by these files, checked duplicate
keys and compared all five grade leaves, tuple arrays, version fields,
selector links and candidate-registry tuples. It exited 0. This is a
structural consistency check, not a new grade decision or general YAML
parser claim. The five active and two superseded evaluation digests
remain the exact objects accepted by the preceding evaluation review.

| Candidate / active date suffix | A0 | A1 | A2 / A3 / A4 |
| --- | --- | --- | --- |
| C424 / 2026-09-09-corrected.yaml | WEAK_ARITHMETIC_RELATION | WEAK | FAIL / FAIL / FAIL |
| C425 / 2026-09-09-corrected.yaml | WEAK_ARITHMETIC_RELATION | WEAK | FAIL / FAIL / FAIL |
| C426 / 2026-09-09.yaml | WEAK_ARITHMETIC_RELATION | FAIL | FAIL / FAIL / FAIL |
| C427 / 2026-09-09.yaml | WEAK_ARITHMETIC_RELATION | WEAK | FAIL / FAIL / FAIL |
| C428 / 2026-09-09.yaml | WEAK_ARITHMETIC_RELATION | WEAK | FAIL / FAIL / FAIL |

All five full overall labels are ROUTE_A_EXPLORATORY. All 45 A2
metrics are NOT_TESTABLE, all five mandatory arithmetic control gates
remain INCOMPLETE, all 45 scope flags and five Route-B permission flags
are false. These assertions were checked directly in the active files,
not inferred from the prose table. The selector's historical pending
review wording is expressly superseded by the later adjudication and
does not create a new open review gate.

The actual unchanged evaluator v0.2.0 rehashes to
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
The active C424/C425 corrections and preserved initial files remain
distinct; C425's changed A1 completeness prose is not falsely described
as unchanged metric-map bytes. No A2 measurement or grade was changed.

## 5. Contract ownership and registry boundaries

After I1, both new registry sections and the current delivery summaries
preserve the following distinctions:

- C424 covers quadratic Int(Z), not all Q[t]. Rational normalization
  does not force original rational coordinates to be integral. C412's
  imported theorem/method and the 147-parameter exact residual
  dependency remain explicit; aggregate counts across maps are not a
  point count for one map.
- C425 retains all ordered forcing, the ordinary fixed-word clock,
  whole-line plus finite-core exhaustion, and exact pointwise period
  procedures. The 27-line/54-return bounds are not an attained
  universal period spectrum or an executed all-parameter census.
- C426 retains every number field and all two-dimensional affine
  coordinates, including wild centres and the ideal-square obstruction
  after local existence. Prime ideals are genuine source arithmetic,
  not rational-prime primitive owners. Its scoped static-observable
  A1_FAIL does not say the Hénon map has no periodic points.
- C427 retains the complete all-dimensional/all-forcing semilinear
  atlas, nonzero-block rigidity, mixed-zero channels and level-independent
  finite remainder. The n=3 C421 import, the distinct fixed-level height
  theorem and the absence of a practical complexity claim remain visible.
  A period bound alone is not the new classification theorem.
- C428 retains the all-degree integral-coefficient family-union spectra,
  both Jacobian signs, all-diameter reduction, exact certificates and
  realizations. It does not claim per-polynomial coexistence, an arbitrary
  integer-valued extension or a rational quadratic result. C417's
  positive-sign list/method are deducted; the typeset map-interface fix
  does not imply the frozen mathematical programs were wrong.

These are exactly five admitted contracts, not five renamings of one
result or a sixth paper assembled from auxiliaries. WM6 and the
PC424-L descent theorem remain complete auxiliary results; the original
periodic-data-to-algebraic-transfer bridge and the wild tower remain
unclosed. A0 source evidence, ordinary cycle products and geometric
structure are not target Euler factors, root numbers, automorphy,
target zero matching or a Hilbert–Pólya realization. A4_FAIL records
no submitted candidate-specific lift, not universal impossibility.

The accepted citation-review hash and its 28-entry total match the
adjudication. DOI-display omissions with versioned URLs, the five
internal-reference alerts, unperformed compliance checks and unavailable
structural-PDF sidecars remain limitations. No citation retrieval or
comprehensive new citation/compliance audit was performed here.

## 6. Mathematical-run accounting and release boundary

The actual historical receipts support four round-six mathematical
executions: one bounded affine probe, two IH6 author commands and one
independent IH6 reconstruction. Adding the earlier three gives seven
for the batch. The probe's 26,460 seed scan is not the semilinear atlas
and is not used to extrapolate its proof. The IH6 author's D<=10 run
has 71,068 restrictions; its needed D<=9 prefix and the independent
reconstruction have 35,778. The 9,020 generic graphs, 512 exceptional
graphs, eleven witnesses and seven controls belong to the stated
independent receipt, not an invented author output identity.

No math program, finite-core renderer, old certificate, GPU job or
target panel was executed in this integration review. Hashing, parsing,
pdfinfo/pdffonts and reading existing logs are read-only document checks.
Some initial path lookups used an incorrect relative/name assumption;
they returned missing-path diagnostics, were corrected by file discovery,
and changed no file or evidence. They are not mathematical/build failures.

The release policy correctly reuses unchanged legacy-format code and
its expressly historical 21+21-test receipt, rather than claiming a new
suite execution. The actual source/test hashes independently rechecked
here are respectively
`529ad136f29879c5bb659171127b45e7edb8e5b3c05044b4e43e035114cd444f`
and
`2c5dc213ba100b724b707ac34c0d364be5330710f3b5b0d7995ef06d61668434`.
Neither source was executed or edited during this review. Legacy schema
identity is distinct from the explicit new payload root.

At this check, root PAYLOAD_LEDGER.json and MANIFEST.sha256 were absent.
No current exact seal, independent post-seal membership result, commit
or push is certified here. The current-state fetch statement is the
coordinator's recorded observation, not a new Git check by this reviewer.
The policy still requires writer quiescence, outside candidate/approval
receipts, a literal external pin, actual inventory/check/seal/verify and
independent membership verification. Historical trees, ignored outputs
and failures must not be silently removed. After sealing, new receipts
belong outside the exact payload. No all-platform, concurrency-security
or mathematical-authenticity guarantee is inferred from checksums.

The positive integration disposition permits the coordinator to proceed
to those separate actual release operations. It does not preclaim them,
authorize another stream, C429, Route B, force push or external manuscript
submission. Stop at the C428 five-paper checkpoint.

## 7. Checked control-document identities

These are review-time identities, not future live trust pins. The
package's eventual approved ledger must separately pin its exact
membership; later authorized package-external state updates are not
claimed to preserve the earlier current-state hash.

| Document | SHA256 |
| --- | --- |
| REVIEW_ADJUDICATION.md | `3411681c4efb21c1d72a1f26f76b47dd97ff1798a036e91402d793275dd9df05` |
| EVALUATION_ADJUDICATION.md | `38903b42303ca9b4af83fe4e264a8c9cbc50193c010723685cbd3b8ac77d572f` |
| FINAL_BUILD_REPORT.md | `62a50a9cfe31473958d2874109caf8a7321eb6f9e29dec083803c6784f70ebdd` |
| release/README.md | `f94d5db06709261f9a05a79c6f61ff465ba7d2b303e08cbbd9996fb078b646d5` |
| continuation_round6/ROUND6_DECISION.md | `04ba718e64c5fb0b02b4b12899ab822b08d7ba4eecd612cfe86974447657b8a8` |
| README.md | `3515a443dde50ef4a862414a4ace37069fe904f036e3abfa2268c9b18b854b12` |
| CITATION_REVIEW.md | `3a5099702673399324cd187b708f0a3c6e508edff85c55f9d9381c6a2e2f2121` |
| REVIEW_EVALUATION.md | `34d2d2f7c34f82ffa02fab89f62bb68dea900914222f7350db34e3d581feb8ac` |
| EVALUATION_SCOPE.md | `4ed6b70d93fd54e8a308323195f6f29bac341637c9dff3f5befe1313c41d6549` |
| EVALUATION_REFERENCE_ROUTING.md | `80a0139166cbe68cf385c48f65bc77499d741ab07e9554448ade1f68eac32b3e` |
| evaluations/README.md | `c97c79fa4acb61fc08f274ddaeeeacd79548d9a9b92de04f2fc1a39398bcd969` |
| ../CURRENT_RESEARCH_STATE.md, checked opening | `e2af21f270f200bb3e5af05213bf4fa08e419d2ba7b359748531664b281e1101` |
| ../docs/candidate_registry.md, checked new section | `9b65c79f420c40b7f955bc7bfdd53d3413080f7d8988523caf22147d13e11097` |
| ../docs/obstruction_registry.md, I1 corrected | `950c26deb76f6e59c4bb09ef878e0f291c781a1d64469e10af8d92b78534810c` |

Disposition: **one reported required correction, independently closed;
zero open required corrections; bounded integration PASS; reviewer
STOP-WRITE.** The external coordinator retains release and Git authority.
