# Citation, claim, and provenance audit

## Scope

This audit applies to the conference-oriented Phase-I methodology paper and its
source-bound research record in the paper's LaTeX package. It checks whether the
external references are used for the bounded background claims they support,
whether the local Phase-I claims are explicitly tied to the repository record,
and whether the research-governance framework, roadmap, and prime-symbolic
lineage have a stated provenance. It does **not** independently prove any local
mathematical result, establish a Route-A/Route-B pass, validate an AI system's
capability beyond the cited setting, or supply peer review.

## Citation register

| Key in `references.bib` | What it supports in the paper | Scope limit |
| --- | --- | --- |
| `CMI2026` | RH is listed as unsolved, and Navier--Stokes as active, by the Clay Mathematics Institute on the stated access date. | An official status page; it does not independently adjudicate a claimed solution or provide evidence for any candidate. |
| `OpenAI2026NavierStokes` | A current company announcement reporting an analytical proof, Lean formalization, and a coordinated-agent workflow for an explicit Navier--Stokes formulation. | An announcement by the reporting organization, not independent peer review, CMI adjudication, or evidence about RH. |
| `Thom2026NonSofic` | A Tao-hosted guest post describing a reported non-sofic-groups result and locating it in prior human work. | A guest post, not an independent proof audit, general capability evaluation, or a basis for reproducing its attribution critiques as verified fact. |
| `Tao2026Misalignment` | A Tao-hosted declaration initially signed by 25 Fields Medallists, used for its stated governance concern about benchmark success, human understanding, and human agency. | A position statement, not an empirical study or evidence that the mathematical community has reached a universal consensus. |
| `Davies2021` | AI can assist human mathematical conjecturing and investigation in selected settings. | Does not show autonomous proof of RH. |
| `RomeraParedes2024` | Evaluator-coupled program search can generate constructions in constrained settings. | Does not validate a dynamical candidate without its own mathematical evaluator. |
| `Trinh2024` | The bounded IMO-AG-30 geometry result cited in the introduction. | Geometry benchmark only; not a general mathematical-reasoning claim. |
| `Hubert2026` | Reinforcement-learning search for Lean-verified proofs in a specialized olympiad-level setting. | Formal verification and target domain remain bounded. |
| `AlpogeFurman2026` | A 2026 zeta-zero preprint, its stated critical-line proportion result, Lean 4 verification, and its limited use as the P6 arithmetic-side benchmark. | A preprint, not a proof of RH or an independently re-reviewed result in this paper. |
| `BerryKeating1999` | Hilbert--Pólya / spectral-asymptotic motivation. | Motivation, not a candidate-specific theorem. |
| `Connes1999` | Trace-formula and arithmetic context. | Context, not an endorsement of the present construction. |
| `Ruelle1976` | Standard dynamical-zeta context for expanding maps and Anosov flows. | Does not supply the required arithmetic source or quantum lift. |
| `Sandve2013` | The narrow reproducibility guidance concerning the relation among inputs, versions, procedures, and outputs. | Does not certify this repository, its mathematics, or every included record as reproducible. |
| `Wilkinson2016` | The FAIR-inspired aspiration toward findability and reusability of research material. | Does not establish that the P1 Wiki satisfies FAIR or functions as an archive. |
| `PhaseIRepository` | The six-line record, local claims, stated gaps, provenance, and repository address. | A source-bound internal research record, not independent external verification. |

The bibliography includes the DOI or official page for every external source.  The GitHub record is cited in the paper and is printed as `https://github.com/maris205/hilbert-polya-structure`.

## Internal provenance register

| Material | Local source / identifier | Permitted use in this paper |
| --- | --- | --- |
| Historical Phase-I evidence corpus | Commit `419ee36c1e310469209f7b83c096ec8aea448386`, 2026-09-13 UTC | Bounded summaries in the evidence landscape and Appendix A; not a new proof audit. |
| P1 Wiki conversion inventory | Commit `afe747a194b92b9804bd69e2f57696884e47d53b`; `p1_wiki/meta/conversion-manifest.md` | Counts, derived-reading status, and conversion limits; not a statement of mathematical strength, publication status, or Route progress. |
| Six-direction navigation and claim boundaries | [`p1_wiki/`](../../README.md) and the parent [internal paper package](../README.md) | Direct the reader to controlling source records and preserve non-transfer boundaries. |
| Prime-symbolic research genealogy | [`flow_systems/docs/prior_work/README.md`](../../../flow_systems/docs/prior_work/README.md) | Constrains candidate admission; it is not proof that the displayed lineage arrows are established mathematical implications. |
| Layer-1 P1--P6 ledger | [Prior Work Guide](../../../flow_systems/docs/prior_work/README.md), plus `AlpogeFurman2026` for P6 | P1--P5 are project source records; P6 is an external preprint benchmark. Their placement in the lineage figure does not independently verify P1--P5 claims or transfer P6 evidence to a descendant. |
| Case-study synthesis protocol | Section 3.3.1 and the direction source map below | Defines the six-direction unit of analysis, separate evidence snapshots, and non-compensatory A0+A1+A2 coding rule; it does not convert the case study into a systematic review or controlled strategy comparison. |
| Human-governed, AI-executed framework | Figure 1, the paper-configuration record, and [`assets/research_framework.png`](assets/research_framework.png), a byte-identical mirror of the author-supplied [P1 Wiki source image](../../research_framework.png), SHA-256 `da9e89f253991fb02db9ae11c2b13a512a4a404f720bf9abe03ff3853887f4a8` | Author-proposed prospective three-layer governance framework: the mathematician owns research origin and scientific authority; a jointly drafted, human-approved `AGENTS.md` constrains bounded AI execution and requires a handoff and review. It does not show that historical Phase-I materials used one uniform agent protocol, nor that a workflow document is mathematical evidence. |
| Updated roadmap | [`assets/rh_roadmap.png`](assets/rh_roadmap.png), SHA-256 `f5e70c5120474702e4f0715bce90c7a88fd5936164594e8b37a2ee0993549d1d` | Author-proposed evidence-obligation / search map; not a progress dashboard or mathematical result. |
| Layer-1, portfolio, and candidate-engineering figures | [`assets/layer1.png`](assets/layer1.png), [`assets/layer3.png`](assets/layer3.png), and [`assets/coo.png`](assets/coo.png), byte-identical to the author-supplied P1 Wiki images `layer1.png`, `layer3.png`, and `coo.png`; SHA-256 `2077a8307c1ed45acfdaba1c34b14bf5e64c81e456d295cf1bfe09e154687578`, `f5c7cffadf14f3e4038888ef7e7ea7913cb448a2dd9ceff44870d743a6a4bdb4`, and `9ffbd569db5163e1e943e29ba09b91eb0029adc0a08e4f8e9f44635e9b10a842`, respectively | Author-proposed visual summaries of the constrained lineage, Phase-I portfolio, and prospective human--AI candidate-engineering protocol. They are presentation/navigation assets, not theorem evidence; labels, arrows, and visual prominence do not confer mathematical validity or transferable Route credit. |

## Session-level source map

The generic PhaseIRepository bibliography key is a navigation citation, not a
replacement for the source records controlling individual summaries. The
following static map identifies the P1 Wiki entrypoint for every row in the
evidence landscape and Appendix A.

| Paper section / landscape row | Source-bound P1 entrypoint | Permitted summary use |
| --- | --- | --- |
| Early free exploration: zeta_mvp0 | [zeta_mvp0 conclusions](../../directions/zeta_mvp0/conclusions.md) | Local operator / relative-trace structures and the still-open endogenous prime-time bridge. |
| Logistic Dynamics | [Logistic conclusions](../../directions/logistic_dynamics/conclusions.md) | Same-object return--roof--transfer--Fredholm chain and its stated stopping boundary. |
| Hénon Dynamics | [Hénon conclusions](../../directions/henon_dynamics/conclusions.md) | Restricted periodic/geometric results and object-specific Route-A limits; not inherited credit. |
| Symplectic Map | [Symplectic conclusions](../../directions/symplectic_map/conclusions.md) | Scoped interfaces/diagnostics and NOT_APPLICABLE; neither a pass nor a failure. |
| Symbolic Dynamics | [Symbolic conclusions](../../directions/symbolic_dynamics/conclusions.md) | Exact finite-system work, process labels, and the missing geometric/analytic/operator bridge. |
| Flow Systems / P24--P28 | [Flow conclusions](../../directions/flow_systems/conclusions.md) | The P24--P28-bounded positive arithmetic A2 = 0/5, Route-B invocation = 0/5, and same-object ownership boundary. |

For theorem hypotheses, exact evaluators, frozen inputs, or canonical
manuscripts, follow the source links within those conclusion pages or the
historical [evidence map](../evidence-map.md). This paper does not turn a
navigation page into a replacement proof source.

## Claim discipline checked

- The abstract, introduction, figure captions, discussion, and end matter state that the paper does not prove RH or a Hilbert--Pólya realization.
- The AI background is intentionally limited to the cited task settings. The paper reports the Navier--Stokes announcement without independently adjudicating it; it does not claim that AI proved RH, that any reported open-problem resolution has passed independent scrutiny, or that AI replaces mathematical validation.
- The construction-and-search interpretation is a methodological inference from source-described workflows and bounded prior work. It does not assert that every mathematical problem is reducible to high-throughput search or blind enumeration.
- The Tao-hosted declaration is used as a governance position, not as an empirical result. Its role is to motivate explicit human authority over problem framing, proof acceptance, attribution, and provenance.
- `NOT_APPLICABLE`, internal process completion, scoped negative controls, and local results are not displayed as transferable Route credit.
- The Flow `positive arithmetic A2 = 0/5` and `Route-B invocation = 0/5` statement is explicitly restricted to P24--P28, rather than all continuous flows.
- The proposal for broader Round-2 search is a methodological recommendation from the record, not a theorem or empirical optimization result.
- The lineage requirement is stated as an admission and preservation ledger: a generic map, flow, trace formula, or operator that receives primes only after construction is an external control, not a main candidate.
- The framework distinguishes three extensions: a documented branch of a fixed
  origin; a separately authorized new basic idea that starts a new Layer-1/2
  record; and source-linked reuse through the Wiki. None silently inherits
  candidate identity, mathematical evidence, or Route credit.
- The six-direction case-study protocol distinguishes the historical
  mathematical snapshot from the later navigation snapshot. A missing
  source-bound integrated A0+A1+A2 chain is a statement about the named record,
  not an impossibility result for a family.
- `GO`/`HOLD`/`FORK`/`END` are explicitly unordered operational workflow dispositions in the proposed framework, not existing Route-A/Route-B verdicts or claims about the wording of every historical/current project protocol. A token/compute/time-budget stop, hard contradiction, or declared route closure records an operational boundary at its stated scope; a budget stop is not a negative mathematical result.

## Build and rendering checks

The release-local build command is:

```bash
cd p1_wiki/phase1_ai_guided_exploration/conference_record_v1/latex
./build.sh
```

Closing checks should include a successful LuaLaTeX/BibTeX build, no undefined citation/reference warnings in `build/manuscript.log`, `pdfinfo manuscript.pdf`, a manual inspection of all rendered pages, and `git diff --check`.  Passing these checks establishes rendering and reference-resolution integrity only; it does not establish mathematical correctness or external scholarly validation.

## Verification record for the two-column v1 baseline

The following closing checks were run on 2026-09-13 UTC.

| Check | Command / method | Result |
| --- | --- | --- |
| Reproducible paper build | <code>cd latex && ./build.sh</code> | PASS: LuaLaTeX/BibTeX build completed; tracked PDF is 8 pages. |
| Citation and cross-reference resolution | Inspect <code>latex/build/manuscript.log</code> for undefined citations/references and fatal errors | PASS: none found. |
| Bibliography processor | Inspect <code>latex/build/manuscript.blg</code> | PASS: no BibTeX warnings or errors. |
| PDF metadata | <code>pdfinfo latex/manuscript.pdf</code> | PASS: title, author Liang Wang, subject, A4 page size, and 8-page count present. |
| Page rendering | Render and inspect pages 1--8 | PASS: roadmap, evidence landscape, protocol, candidate card, appendices, and bibliography are legible; no clipped candidate-card rows remain. |
| Wiki links | <code>python3 p1_wiki/tools/verify_wiki_links.py</code> from repository root | PASS: 19,261 local links in 2,306 Markdown files. |
| Asset identity | SHA-256 comparison against the Round-2 roadmap reference | PASS: both values are <code>f5e70c5120474702e4f0715bce90c7a88fd5936164594e8b37a2ee0993549d1d</code>. |
| Patch hygiene | <code>git diff --check</code> | PASS: no whitespace errors. |

## Verification record for the original TikZ framework and single-column revision

The following closing checks were run on 2026-09-14 UTC after the new Figure 1,
the governance-framework prose, and the single-column A4 conversion were
applied.

| Check | Command / method | Result |
| --- | --- | --- |
| Reproducible paper build | <code>cd latex && ./build.sh</code> | PASS: LuaLaTeX/BibTeX build completed; tracked PDF is a 13-page single-column A4 document. |
| Citation and cross-reference resolution | Inspect <code>latex/build/manuscript.log</code> for undefined citations/references and fatal errors after the final pass | PASS: none found. |
| Layout diagnostics | Inspect the final log for <code>Overfull</code>, <code>Float too large</code>, and unprocessed-float warnings | PASS: none found. Two non-fatal underfull line-break diagnostics remain. |
| PDF metadata | <code>pdfinfo latex/manuscript.pdf</code> | PASS: title, author Liang Wang, subject, A4 page size, and 13-page count present. |
| Page rendering | Render and inspect pages 2--9 and the bibliography page | PASS: Figure 1 is the human-governed framework and appears before Figure 2 (the RH roadmap); the evidence landscape, candidate-engineering protocol, role table, candidate card, appendices, and bibliography are legible with no visible clipping. |
| Wiki links | <code>python3 p1_wiki/tools/verify_wiki_links.py</code> from repository root | PASS: 19,261 local links in 2,306 Markdown files. |
| Patch hygiene | <code>git diff --check</code> | PASS: no whitespace errors. |

## Verification record for the supplied three-layer framework replacement

The following checks were run on 2026-09-14 UTC after Figure 1 was replaced
by the author-supplied three-layer framework image and a byte-identical
release-local mirror.  They establish asset identity, rendering, and link
integrity only; they do not turn the framework into mathematical evidence or
validate a Route verdict.

| Check | Command / method | Result |
| --- | --- | --- |
| Asset identity | <code>sha256sum p1_wiki/research_framework.png p1_wiki/phase1_ai_guided_exploration/conference_record_v1/assets/research_framework.png</code> | PASS: source and release-local mirror both equal <code>da9e89f253991fb02db9ae11c2b13a512a4a404f720bf9abe03ff3853887f4a8</code>. |
| Reproducible paper build | <code>cd latex && ./build.sh</code> | PASS: LuaLaTeX/BibTeX build completed; the tracked PDF remains a 13-page single-column A4 document. |
| Citation, reference, and float diagnostics | Inspect <code>latex/build/manuscript.log</code> for fatal errors, undefined citations/references, overfull boxes, oversized floats, and unprocessed floats | PASS: none found. Two non-fatal underfull line-break diagnostics remain in dense tables. |
| PDF metadata | <code>pdfinfo latex/manuscript.pdf</code> | PASS: title, author Liang Wang, subject, A4 page size, and 13-page count present. |
| Figure order and visual rendering | Render and inspect the framework, transition, and roadmap pages | PASS: the supplied Figure 1 is readable before Figure 2; its three layers, four contract cards, evidence-handoff loop, and the surrounding explanatory prose are visible without clipping or overlap. |
| Wiki links | <code>python3 p1_wiki/tools/verify_wiki_links.py</code> from repository root | PASS: 19,266 local links in 2,306 Markdown files. |
| Patch hygiene | <code>git diff --check</code> | PASS: no whitespace errors. |

## Verification record for the expanded methodology, case-study, and knowledge-resource edition

The following closing checks were run on 2026-09-14 UTC after the framework was
expanded to distinguish (i) traceable within-origin dynamical expansion,
(ii) a mathematician-authorized new-origin restart, and (iii) cumulative
evidence reuse through the P1 Wiki. They establish build, rendering,
reference-resolution, and local-navigation integrity only. They do not certify
the mathematical source records, make the Wiki an archive, or establish
external submission readiness.

| Check | Command / method | Result |
| --- | --- | --- |
| Reproducible paper build | <code>cd latex && ./build.sh</code> | PASS: LuaLaTeX/BibTeX build completed; the tracked PDF is a 19-page single-column A4 document. |
| Citation, reference, and float diagnostics | Inspect <code>latex/build/manuscript.log</code> for fatal errors, undefined citations/references, overfull boxes, oversized floats, and unprocessed floats | PASS: none found. Eleven non-fatal underfull line-break diagnostics remain in dense tables/figure text; no overfull boxes were reported. |
| Bibliography processor | Inspect <code>latex/build/manuscript.blg</code> | PASS: reports <code>warning$ -- 0</code>; no BibTeX errors. |
| PDF metadata and identity | <code>pdfinfo latex/manuscript.pdf</code>; <code>sha256sum latex/manuscript.pdf</code> | PASS: title and author Liang Wang present; A4, 19 pages, unencrypted; SHA-256 <code>e6057f2e94978e91a3eba9596ed7e9a15437848947392524ac431152a40ea29a</code>. The PDF is not tagged. |
| Visual rendering | Render and inspect the title/abstract page, evidence-synthesis and portfolio pages, candidate-engineering/discussion pages, research-materials/appendix pages, and bibliography | PASS: no visible clipping, overlap, broken figure/table ordering, or reference truncation. Figure 4 follows its Section 3.3.4 introduction; the three extensibility modes and reuse hierarchy are legible. |
| P1 Wiki corpus integrity | <code>python3 p1_wiki/tools/build_paper_corpus.py --check</code> from repository root | PASS: 1,126 logical records. This is a manifest/local-source check, not mathematical verification. |
| P1 Wiki local-link integrity | <code>python3 p1_wiki/tools/verify_wiki_links.py</code> from repository root | PASS: 19,266 local links in 2,306 Markdown files. It does not verify external URLs or heading anchors. |
| Patch hygiene | <code>git diff --check</code> | PASS: no whitespace errors. |

## Verification record for the current AI-mathematics motivation revision

The following checks were run on 2026-09-14 UTC after the Introduction was
reframed around a bounded construction-and-candidate-search interpretation and
three current public sources were added. They establish source recording,
reference resolution, local navigation, and rendering only. They do not
independently validate the reported Navier--Stokes or non-sofic-groups results,
or convert a governance declaration into mathematical evidence.

| Check | Command / method | Result |
| --- | --- | --- |
| Source and claim-boundary review | Check the official OpenAI report and the two Tao-hosted pages against the citations and this audit. | PASS: all three are recorded as public reports or a position statement, with explicit non-adjudication limits. |
| Reproducible paper build | <code>cd latex && ./build.sh</code> | PASS: LuaLaTeX/BibTeX build completed; the tracked PDF is a 20-page single-column A4 document. |
| Citation, reference, and float diagnostics | Inspect the final <code>latex/build/manuscript.log</code> for fatal errors, undefined citations/references, overfull boxes, oversized floats, and unprocessed floats. | PASS: none found. Eleven non-fatal underfull line-break diagnostics remain in dense pre-existing tables/figure text. |
| Bibliography processor | Inspect <code>latex/build/manuscript.blg</code>. | PASS: 15 entries used; <code>warning$ -- 0</code>. |
| PDF metadata and identity | <code>pdfinfo latex/manuscript.pdf</code>; <code>sha256sum latex/manuscript.pdf</code>. | PASS: title and author Liang Wang present; A4, 20 pages, unencrypted; SHA-256 <code>63054feec634bdaa5686adcfee0e3ffe4ba08549bbeeb4bb4ef497d7516265ed</code>. |
| Targeted visual rendering | Render and inspect the new Introduction page and both bibliography pages. | PASS: the revised motivation, caveats, numerical citations, and long web-source entries are readable; no visible clipping or overlap. |
| P1 Wiki corpus integrity | <code>python3 p1_wiki/tools/build_paper_corpus.py --check</code> from repository root. | PASS: 1,126 logical records. This is a manifest/local-source check, not mathematical verification. |
| P1 Wiki local-link integrity | <code>python3 p1_wiki/tools/verify_wiki_links.py</code> from repository root. | PASS: 19,267 local links in 2,306 Markdown files. It does not verify external URLs or heading anchors. |
| Patch hygiene | <code>git diff --check</code> | PASS: no whitespace errors. |

## Verification record for the Figure 3--5 supplied-asset replacement

The following checks were run on 2026-09-14 UTC after the inline TikZ
renderings of Figures 3--5 were replaced with the author-supplied Layer-1,
Phase-I portfolio, and candidate-engineering images. They establish asset
identity, rendering, reference resolution, and local-navigation integrity
only. They do not turn the images into theorem evidence, transfer a local A1
label across tracks, or validate a mathematical candidate.

| Check | Command / method | Result |
| --- | --- | --- |
| Asset identity | <code>sha256sum p1_wiki/{layer1,layer3,coo}.png p1_wiki/phase1_ai_guided_exploration/conference_record_v1/assets/{layer1,layer3,coo}.png</code> | PASS: each source/release-local pair is byte-identical: <code>layer1.png</code> = <code>2077a8307c1ed45acfdaba1c34b14bf5e64c81e456d295cf1bfe09e154687578</code>; <code>layer3.png</code> = <code>f5c7cffadf14f3e4038888ef7e7ea7913cb448a2dd9ceff44870d743a6a4bdb4</code>; <code>coo.png</code> = <code>9ffbd569db5163e1e943e29ba09b91eb0029adc0a08e4f8e9f44635e9b10a842</code>. |
| Reproducible paper build | <code>cd latex && ./build.sh</code> | PASS: LuaLaTeX/BibTeX build completed; the tracked PDF is a 21-page single-column A4 document. |
| Citation, reference, and float diagnostics | Inspect the final <code>latex/build/manuscript.log</code> for fatal errors, undefined citations/references, overfull boxes, oversized floats, and unprocessed floats | PASS: none found. Ten non-fatal underfull line-break diagnostics remain in dense table/text blocks. |
| Bibliography processor | Inspect <code>latex/build/manuscript.blg</code> | PASS: reports <code>warning$ -- 0</code>; no BibTeX errors. |
| PDF metadata and identity | <code>pdfinfo latex/manuscript.pdf</code>; <code>sha256sum latex/manuscript.pdf</code> | PASS: title and author Liang Wang present; A4, 21 pages, unencrypted; SHA-256 <code>334b2a63df3856b03ee9c8f2b1dff42a949da110508fe9aad9b6b1ca6f5597a4</code>. |
| Targeted visual rendering | Render and inspect pages 7 and 10--12 | PASS: Figure 3 uses the Layer-1 research framework; Figure 4 uses the portfolio overview after its source-bound introduction; Figure 5 uses the human--AI candidate-engineering protocol. The images, captions, page breaks, and surrounding text are legible with no visible clipping or overlap. |
| P1 Wiki corpus integrity | <code>python3 p1_wiki/tools/build_paper_corpus.py --check</code> from repository root | PASS: 1,126 logical records. This is a manifest/local-source check, not mathematical verification. |
| P1 Wiki local-link integrity | <code>python3 p1_wiki/tools/verify_wiki_links.py</code> from repository root | PASS: 19,276 local links in 2,306 Markdown files. It does not verify external URLs or heading anchors. |
| Patch hygiene | <code>git diff --check</code> | PASS: no whitespace errors. |

## Release note

Before external circulation, repeat this audit on the release commit, freeze the repository with a tag or archival deposit, and replace the provisional funding and competing-interest text with the author's actual declarations.  A double-blind venue also requires a separately anonymized manuscript and repository link strategy.
