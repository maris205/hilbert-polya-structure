# Paper 33 — Stage 2.5 Phase A/B Working Integrity Audit

Audit date: **2026-09-02 UTC**  
Mode: **Stage 2.5 / Mode 1 pre-review, read-only working audit**  
Paper: **P33 — `33-bolza-control-matched-census`**

## Scope and byte locks

This sidecar verifies the frozen bibliography and a deterministic sample of
citation contexts. It does not edit the manuscript, bibliography, release PDF,
pipeline state, roadmap state, or canonical results; it does not run a census,
validator, scientific computation, Route-A evaluation, or Route-B layer.

| Frozen input | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `b407441c07091ad38fb7e918721d31d2c4e3d897db9a705d92d9ff1f231f96d3` |
| `paper/references.bib` | `12143967175abb0d325e16d156b1bc227e51f886009e7acd64691e84b92cb5e0` |
| `paper/paper.pdf` | `487a8838d9d422e00dcf3e896c9231b96c58fedfc2cdeb2265045f8d11d70031` |
| Stage-1 source-verification report | `f09ed5ff5562f956d8d807c6e23015c52de9bbfcdf8eff313e4bccf1570cc79e` |
| Stage-1 source-verification TSV | `ac794ff7ca903eaab6ea95218252a79c62f139a6ad7601d51b8b35de2bd2c45b` |

The last two hashes were recomputed directly from the current Stage-1 sidecars
when this working artifact was finalized.

## Phase A — 100% reference existence and metadata replay

### Method

Every one of the 20 registered bibliography records received an explicit
title/DOI/stable-ID browser query. The selected URL is the highest-authority
stable landing page available from the query and the frozen source ledger:
publisher/journal/proceedings first, then official archive or author preprint.
For the three known correction/page bindings, the relevant journal page or
Crossref DOI record was also replayed directly. Search results are time-sensitive;
the queries and selected canonical URLs below are therefore part of the audit
trail.

### Per-reference audit trail

| ID | Exact query | Authoritative top URL | Existence / metadata / correction verdict and licensed boundary |
|---|---|---|---|
| P33-S01 | `site:arxiv.org/abs/1301.5446 Two-Parametric Hyperbolic Octagons Nazarenko` | [official arXiv record](https://arxiv.org/abs/1301.5446) | `VERIFIED_EXACT`: A. V. Nazarenko, 2013, title and arXiv ID match. The abstract supports the two-parameter compact genus-two octagon construction and generators, not the frozen specialization's arithmeticity, systole, owner census, or certificate closure. |
| P33-S02 | `10.1063/1.1850177 Hyperbolic Octagons Teichmuller Space genus 2` | [EPFL institutional record](https://infoscience.epfl.ch/entities/publication/eb38a039-e625-41a3-a9a6-4fb5a81f7d7d) | `VERIFIED_EXACT`: five authors, 2005, *J. Math. Phys.* 46(3), 033513, DOI match. Licensed only for the peer-reviewed genus-two octagon-family setting. |
| P33-S03 | `10.2969/jmsj/02740600 Takeuchi arithmetic Fuchsian groups correction` | [official J-STAGE record](https://www.jstage.jst.go.jp/article/jmath1948/27/4/27_4_600/_article) | `VERIFIED_EXACT_CORRECTION_BOUND`: Kisao Takeuchi, 1975, 27(4), 600–612, DOI match. J-STAGE explicitly records a 20 October 2006 citation correction and PDF-file correction; it is not a retraction. The manuscript preserves the correction and uses only the criterion-level boundary. |
| P33-S04 | `10.1007/978-3-031-51959-8_16 Lindemann Weierstrass Popescu` | [DOI landing](https://doi.org/10.1007/978-3-031-51959-8_16) | `VERIFIED_YEAR_VARIANT`: Sever Angel Popescu; author preprint 2023, cited book-chapter issue 2024, pp. 349–366. Licensed only as a Lindemann–Weierstrass ingredient, not as a P33 group conclusion. |
| P33-S05 | `10.1016/0167-2789(91)90053-C Periodic Orbits regular hyperbolic octagon` | [DOI landing](https://doi.org/10.1016/0167-2789%2891%2990053-C) | `VERIFIED_EXACT`: Aurich, Bogomolny, and Steiner; 1991; *Physica D* 48(1), 91–101. The abstract supports regular-octagon matrices, a length law, and periodic-orbit enumeration, not a complete P33 owner quotient. |
| P33-S06 | `Felix Jenni 1984 ersten Eigenwert Laplace Operators Commentarii 59 193 203 E-Periodica` | [ETH E-Periodica archival object](https://www.e-periodica.ch/cntmng?pid=com-001%3A1984%3A59%3A%3A16) | `PLAUSIBLE_PRESERVED`: the archive and [EuDML record](https://eudml.org/doc/139972) confirm Felix Jenni, exact title, *Comment. Math. Helv.* 59 (1984), 193–203. E-Periodica exposes archival-object DOI `10.5169/seals-45391`; no publisher article DOI is asserted. Search-visible first-page text (journal p. 193) discusses a shortest closed geodesic on a genus-two surface, but it does not by itself pin the exact Bolza/project theorem or replay inequality. Status remains page-unpinned, context-only, and `PLAUSIBLE`; no upgrade is licensed. |
| P33-S07 | `10.1007/BF01896258 Riemann Surfaces Shortest Geodesic maximal length` | [DOI landing](https://doi.org/10.1007/BF01896258) | `VERIFIED_EXACT`: Paul Schmutz, 1993, *GAFA* 3(6), 564–631. Licensed for broad extremal/systolic context only, not the P33 cutoff replay. |
| P33-S08 | `10.1080/10586458.2015.1073642 Bolza Quaternion Order systoles` | [author preprint](https://arxiv.org/abs/1405.5454) | `VERIFIED_YEAR_VARIANT`: Katz, Katz, Schein, and Vishne; preprint 2014, journal issue 2016, 25(4), 399–415, DOI match. The abstract explicitly supports Bolza arithmetic-Fuchsian and quaternion-order context; it does not supply a P33 owner census. |
| P33-S09 | `10.1016/j.geomphys.2010.06.006 Geodesic Length Spectrum compact Riemann surfaces` | [publisher record](https://www.sciencedirect.com/science/article/pii/S0393044010001233) | `VERIFIED_EXACT`: Grácio and Sousa Ramos, 2010, 60(11), 1643–1655. The abstract supports symbolic/combinatorial genus-two length-spectrum computation, not full conjugacy, roots, inversion, or completeness. |
| P33-S10 | `10.5802/jtnb.683 Computing Fundamental Domains Fuchsian Groups Voight` | [official Numdam record](https://archive.numdam.org/item/JTNB_2009__21_2_467_0/) | `VERIFIED_YEAR_VARIANT`: John Voight; preprint 2008, journal 2009, 21(2), 467–489, DOI match. Supports a Dirichlet-domain/presentation algorithm for suitable cofinite Fuchsian input, not automatic applicability to both P33 inputs. |
| P33-S11 | `10.4230/LIPIcs.SoCG.2023.27 Computing a Dirichlet Domain hyperbolic surface` | [official DROPS record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2023.27) | `VERIFIED_EXACT`: Despré, Kolbe, Parlier, and Teillaud; 2023; article 27:1–27:15; DOI and URN match. The abstract fixes the polygon-with-side-pairings input and explicit Dirichlet-domain output. |
| P33-S12 | `10.1142/S0218196706002986 linearity conjugacy word-hyperbolic groups pages` | [publisher DOI record](https://doi.org/10.1142/S0218196706002986) | `VERIFIED_EXACT_PAGE_BINDING`: Epstein and Holt, 2006, 16(2). Direct Crossref stable-ID replay reports pages **287–305**, agreeing with the current BibTeX and manuscript; stale third-party 287–306 rows are rejected. Supports general linear-time conjugacy decision, not the frozen P33 certificate format. |
| P33-S13 | `10.1070/IM1990v035n01ABEH000693 Lysenok algorithmic properties hyperbolic groups` | [official MathNet record](https://www.mathnet.ru/eng/im1275) | `VERIFIED_EXACT`: I. G. Lysenok, 1990, 35(1), 145–163, DOI match. The official abstract supports root-extraction solvability and related decisions in hyperbolic groups; no P33 implementation or negative-certificate serializer follows. |
| P33-S14 | `10.1007/s00209-021-02808-5 counting prime geodesics Cherubini Wu Zabradi` | [author preprint](https://arxiv.org/abs/1901.03824) | `VERIFIED_YEAR_VARIANT`: Cherubini, Wu, and Zábrádi; preprint 2019, journal issue 2022, *Math. Z.* 300, 881–928. Full text pp. 7–8 defines primitive root-conjugacy classes and maps closed geodesics to them. Licensed for primitive/repetition semantics, not P33 serialization. |
| P33-S15 | `10.1093/imrn/rnad156 reciprocal geodesics Erlandsson Souto` | [Oxford DOI landing](https://doi.org/10.1093/imrn/rnad156) | `VERIFIED_EXACT`: Viveka Erlandsson and Juan Souto, 2024, *IMRN* 2024(13), 10298–10318. Licensed for reciprocal geodesics/classes conjugate to inverses, not the external inverse-pair policy for every P33 owner. |
| P33-S16 | `10.1007/s00220-012-1557-1 correction 10.1007/s00220-018-3094-z Strohmaier Uski` | [base DOI](https://doi.org/10.1007/s00220-012-1557-1) and [correction DOI](https://doi.org/10.1007/s00220-018-3094-z) | `VERIFIED_EXACT_CORRECTION_BOUND`: base work 2013, 317, 827–869; correction 2018, 359, 427. Crossref marks the latter as a correction updating the base DOI. The correction concerns the Section 7.3 / p. 854 example coordinates; the manuscript uses only general rigorous-computation architecture and keeps the correction visible. |
| P33-S17 | `10.1109/TC.2017.2690633 Arb efficient arbitrary precision midpoint radius arithmetic` | [author preprint](https://arxiv.org/abs/1611.02831) | `VERIFIED_EXACT`: Fredrik Johansson, 2017, *IEEE Trans. Computers* 66(8), 1281–1292. Supports midpoint-radius/ball arithmetic and error radii, not group decisions. |
| P33-S18 | `10.1017/S096249291000005X Rump Verification Methods rigorous floating point` | [official Cambridge record](https://www.cambridge.org/core/journals/acta-numerica/article/abs/verification-methods-rigorous-results-using-floatingpoint-arithmetic/770FE58E5293985CCAB770AF09C4F3FF) | `VERIFIED_EXACT`: Siegfried M. Rump, 2010, *Acta Numerica* 19, 287–449, DOI match. Cambridge's extract supports rigorous verification using floating-point computation; it does not decide conjugacy or primitivity. |
| P33-S19 | `10.1080/10586458.2015.1029599 Verified Computations Hyperbolic 3-Manifolds` | [author preprint](https://arxiv.org/abs/1310.3410) | `VERIFIED_YEAR_VARIANT`: Hoffman et al.; preprint 2013, journal issue 2016, 25(1), 66–78, DOI match. Supports separation of approximate hyperbolic candidates from interval/Krawczyk validation and an independently replayable data-file pattern, for 3-manifolds rather than P33 surfaces. |
| P33-S20 | `10.1017/fmp.2017.1 Formal Proof Kepler Conjecture Hales` | [official Cambridge record](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/formal-proof-of-the-kepler-conjecture/78FBD5E1A3D1BCCB8E0D5B0C463C9FBC) | `VERIFIED_EXACT`: Hales et al., 2017, *Forum of Mathematics, Pi* 5, e2, DOI match. Supports a large producer/checker formal-artifact precedent, not a requirement that P33 use one proof assistant or proof that P33 is validated. |

### Phase-A accounting

| Measure | Result |
|---|---:|
| Registered BibTeX records | 20 |
| Records queried and replayed | 20/20 (100%) |
| `VERIFIED_EXACT` or bounded year-variant records | 19 |
| `PLAUSIBLE` retained | 1 (P33-S06) |
| Fabricated / nonexistent records | 0 |
| Citation uses in manuscript | 48 |
| Unique cited keys | 20 |
| Dangling manuscript keys | 0 |
| Uncited bibliography keys | 0 |
| Existing correction bindings replayed | 2 (P33-S03, P33-S16) |
| Existing corrected page binding replayed | 1 (P33-S12, 287–305) |

**Phase-A working disposition:** `PASS_WITH_BOUNDARIES`. No ghost citation,
fabricated record, new metadata defect, or unauthorized bibliography expansion
was found. P33-S06 remains deliberately conservative rather than being promoted
from an archival first-page snippet.

## Phase B — deterministic citation-context sample

### Sampling rule and coverage

The 48 citation uses are ordered by manuscript occurrence. The base sample is
every third use starting at use 1 (uses 1, 4, 7, …, 46; 16 uses). Use 48 is
added to cover the otherwise-unrepresented Reproducibility section. Use 12 is
added as a risk-based top-up for the sole `PLAUSIBLE` source P33-S06.

- sampled uses: **18/48 = 37.5%**;
- unique sources represented: **14/20**;
- citation-bearing major sections represented: **6/6** (Introduction,
  Literature/Theory, Executed Methodology, Method Architecture,
  Evidence-Synthesis Findings, and Reproducibility);
- all sampled manuscript uses retain canonical `anchor=none`; this audit does
  not silently write passage anchors into the manuscript.

`FAITHFUL_BOUNDED` below means the cited source supports the wording at the
stated record/abstract/passage level and the manuscript preserves the stronger
excluded use. It does **not** convert the manuscript's frozen
`claim_to_passage=INCONCLUSIVE` field into a byte-bound passage certificate.

| Use | Manuscript locator | Source / source locator | Context verdict | Exact support boundary |
|---:|---|---|---|---|
| 1 | Introduction, lines 66–69 | P33-S01; official arXiv abstract | `FAITHFUL_BOUNDED` | Supports a compact genus-two octagon family and generators; not the frozen control's arithmeticity, systole, or census. |
| 4 | Introduction, lines 75–78 | P33-S08; arXiv abstract | `FAITHFUL_BOUNDED` | Supports the Bolza arithmetic-Fuchsian group and quaternion order; not a P33 owner ledger. |
| 7 | Literature/Theory, lines 105–111 | P33-S02; EPFL record/DOI metadata | `FAITHFUL_BOUNDED` | Supports a broader peer-reviewed genus-two octagon-family setting. The sentence explicitly rejects specialization-level transfer. |
| 10 | Literature/Theory, lines 121–126 | P33-S05; DOI/DESY abstract | `FAITHFUL_BOUNDED` | Supports regular-octagon periodic-orbit and matrix context; no project-specific quotient or completeness claim. |
| 12 | Literature/Theory, lines 127–133 | P33-S06; E-Periodica p. 193 plus EuDML metadata | `FAITHFUL_CONTEXT_ONLY` | The manuscript says `PLAUSIBLE`, page-unpinned, context-only and explicitly refuses an exact systole theorem/formula. The archive snippet does not license an upgrade. |
| 13 | Literature/Theory, lines 130–133 | P33-S07; DOI title/abstract surface | `FAITHFUL_BOUNDED` | Broad extremal/systolic context only; the manuscript explicitly withholds the project replay inequality. |
| 16 | Literature/Theory, lines 146–152 | P33-S14; arXiv PDF pp. 7–8 | `FAITHFUL_PASSAGE_BOUND` | Definition 2.14 and the following closed-geodesic/root-conjugacy discussion support primitive classes versus powers. External inversion pairing remains a P33 design rule. |
| 19 | Literature/Theory, lines 157–163 | P33-S11; DROPS abstract and PDF p. 1 | `FAITHFUL_PASSAGE_BOUND` | Supports an algorithm from a hyperbolic polygon with side pairings to an explicit Dirichlet domain, with polynomial termination; it does not unify the two P33 input models. |
| 22 | Literature/Theory, lines 178–181 | P33-S16; article abstract, with correction bound | `FAITHFUL_BOUNDED` | Supports a rigorous scheme separating bounded computation, error estimates, and completeness for hyperbolic-surface spectral objects. Corrected example coordinates are not reused. |
| 25 | Literature/Theory, lines 189–195 | P33-S19; arXiv PDF pp. 1–3 | `FAITHFUL_PASSAGE_BOUND` | Supports approximate-candidate then rigorous interval/Krawczyk validation for hyperbolic 3-manifolds. The manuscript preserves the object mismatch and makes no P33 validation claim. |
| 28 | Executed Methodology, lines 212–217 | P33-S16 plus correction DOI | `FAITHFUL_CORRECTION_BINDING` | The sentence reports only that the 2018 correction remains bound to the base work; Crossref confirms the update relation. |
| 31 | Method Architecture, lines 385–390 | P33-S10; Numdam abstract | `FAITHFUL_BOUNDED` | Supports a distinct exact domain/presentation pathway for suitable cofinite Fuchsian groups; no common P33 implementation is inferred. |
| 34 | Method Architecture, lines 391–396 | P33-S13; MathNet abstract | `FAITHFUL_BOUNDED` | Supports root-extraction solvability in hyperbolic groups; no P33 payload, serializer, or applicability proof. |
| 37 | Method Architecture, lines 403–408 | P33-S16; article abstract/full-text architecture | `FAITHFUL_BOUNDED` | Supports rigorous predicate/error/completeness components only; the paragraph says none supplies the missing P33 implementation. |
| 40 | Method Architecture, lines 412–418 | P33-S19; arXiv PDF p. 20 independent-check passage | `FAITHFUL_PASSAGE_BOUND` | Supports a broader producer/replay pattern: emitted data may be checked by an independent rigorous scheme. It does not validate the P33 schema. |
| 43 | Evidence-Synthesis Findings, lines 440–445 | P33-S02; EPFL record/DOI metadata | `FAITHFUL_BOUNDED` | Bounds only the control-family context and explicitly refuses project owner identification. |
| 46 | Evidence-Synthesis Findings, lines 446–455 | P33-S09; publisher abstract | `FAITHFUL_BOUNDED` | Supports genus-two symbolic/candidate-generation context; no source is converted into a full-conjugacy, maximal-root, inverse-pair, or completeness certificate. |
| 48 | Reproducibility, lines 489–495 | P33-S18; Cambridge Extract and author full text | `FAITHFUL_BOUNDED` | Supports disciplined enclosure/verification methods using floating-point arithmetic; the paragraph explicitly says precision cannot prove group-theoretic relations or completeness. |

### Phase-B accounting and findings

| Measure | Result |
|---|---:|
| Sampled citation contexts | 18/48 (37.5%) |
| `FAITHFUL_BOUNDED` / `FAITHFUL_PASSAGE_BOUND` / correction-bound | 18 |
| Contradicted or materially overstated sampled contexts | 0 |
| Canonical passage anchors created | 0 |
| P33-S06 status change | none; `PLAUSIBLE`, page-unpinned, context-only retained |

**Phase-B working disposition:** `PASS_WITH_LOCATOR_WARNING`. The sampled
contexts preserve their source roles and stronger-claim exclusions. Because
the canonical source excerpts and exact anchors were not frozen into the
manuscript, this working check does not erase the manuscript's honest locator
warning or its `claim_to_passage=INCONCLUSIVE` declarations.

## Working conclusion

P33 has no Phase-A ghost reference and no Phase-B sampled citation
misrepresentation. The one conservative record, P33-S06, remains conservative;
the S03/S16 correction bindings and S12 page range survive replay. This sidecar
is suitable as input to the batch integrity compiler, but it is not by itself a
Stage-2.5 completion checkpoint or permission to modify any canonical paper.
