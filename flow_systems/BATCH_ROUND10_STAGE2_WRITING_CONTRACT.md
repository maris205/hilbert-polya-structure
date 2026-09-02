# Round 10 Papers 29--33 -- Stage 2 writing contract

Contract date: **2026-09-02 UTC**  
Pipeline position: **Stage 2 WRITE authorized**  
Authorization: `BATCH_ROUND10_STAGE2_AUTHORIZATION_20260902.txt`

## 1. Objective

Convert the five frozen Stage-1 Phase-6 research reports into five independent,
publication-facing theoretical/computational-mathematics manuscripts. Each
package must contain a complete LaTeX source, closed BibTeX bibliography,
compiled PDF, internal review, and deterministic manuscript audit. This stage
writes papers; it does not create new scientific evidence.

## 2. Common paper configuration

| Field | Frozen value |
|---|---|
| Paper type | research-design / certificate-methods mathematics article |
| Discipline | dynamical systems, arithmetic geometry, spectral and computational mathematics |
| Target venue | general field journal; no venue-specific compliance claim |
| Body language | English |
| Abstracts | independent English and Traditional-Chinese abstracts |
| Citation system | `natbib` with `plainnat` numeric output |
| Primary output | `manuscript.tex`, `references.bib`, compiled `paper.pdf` |
| Target body length | 4,000--6,500 English words per paper, excluding references and Chinese abstract |
| Author | Liang Wang |
| Affiliation | School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Luoyu Road 1037, 430070, Hubei, P.R. China |
| Contact | `wangliang.f@gmail.com` |
| Funding | none |
| Competing interests | none |
| Evidence profile | closed corpus; no Stage-2 retrieval |
| Citation policy | all inherited anchors remain `none`; claim-to-passage status remains `INCONCLUSIVE` |
| Retraction policy | not checked in Stage 2; limitation remains visible |

Liang Wang retains responsibility for conceptual direction, author
adjudication, stage approvals, interpretation of the bounded synthesis, and
final accountability. AI assistance is disclosed and is not authorship.

## 3. Pre-prose and generator/evaluator controls

Before the first canonical prose mutation, every paper must have:

1. a Stage-2 ClaimIntent manifest mapped one-to-one to the eight Phase-6
   claims, with `same_or_narrower` strength and all negative constraints;
2. a Paper Configuration Record;
3. an inherited, approved outline and evidence map;
4. an Argument Blueprint;
5. a writer D1--D7 paper-blind precommitment; and
6. an evaluator D1--D5 paper-blind scoring-plan precommitment.

The Stage-1 report structures count as the inherited outlines approved by the
user's explicit Stage-2 confirmation. No unregistered claim may be introduced
merely to make the prose more impressive.

## 4. Mandatory manuscript anatomy

Every paper must contain:

1. accurate bounded title and complete author block;
2. English abstract (150--300 words), independent Traditional-Chinese abstract
   (300--500 Han characters), and 5--7 keywords per language;
3. Introduction with the exact conditional research question and contribution
   boundary;
4. frozen mathematical/dynamical setting and owner convention;
5. related literature using only the frozen source inventory;
6. executed methodology accurately described as closed-corpus synthesis and
   review adjudication;
7. paper-specific certificate/proof-method architecture and evidence-synthesis
   findings;
8. reproducibility and prospective implementation interface;
9. adversarial, proves-too-much, or nontransfer boundary where applicable;
10. Route-A interpretation with A0--A4 kept separate and Route B closed;
11. acknowledged limitations and future work;
12. conclusion;
13. Data and Materials Availability, Ethics, CRediT-style Author
    Contributions, Funding, Competing Interests, and AI-Assisted Research
    Disclosure; and
14. a zero-orphan `plainnat` bibliography.

## 5. Citation and evidence firewall

- The admitted bibliographies are exactly the five frozen source inventories:
  P29 22, P30 26, P31 22, P32 26, and P33 20 sources.
- Stage 2 may transform frozen metadata into BibTeX but may not retrieve,
  replace, add, or silently normalize a scientific claim from outside the
  admitted records.
- Every LaTeX citation must be traceable to its frozen source ID. Source-level
  comments retain `anchor=none` and `claim_to_passage=INCONCLUSIVE`.
- No page, theorem, section, paragraph, or quotation locator may be invented.
- No direct quotation may be introduced.
- P32-S13 stays `PLAUSIBLE` and background-only. P33-S06 stays `PLAUSIBLE`,
  context-only, and page-unpinned.
- A bibliography that compiles is not treated as passage-level verification.
  Stage 2.5 remains the mandatory integrity gate.

## 6. Scientific and route firewall

The frozen dynamical object, clock, owner convention, repetition convention,
normalization, and paper-specific prohibited upgrades in the Stage-1 handoff
remain controlling. Stage 2 must not modify any file under the five papers'
`code/`, `experiments/`, or `results/` directories, nor any `stage1_*` note.

Formal Route-A tuples remain unassigned for all five papers; positive
arithmetic A2 remains 0/5; Route B remains uninvoked. Manuscript completeness,
internal review, a clean PDF build, or a future integrity PASS does not award a
Route result.

## 7. Build and audit requirements

- PDF compilation uses LaTeX, never HTML-to-PDF.
- The reproducible chain is LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX.
- Final logs must contain no undefined citation/reference, missing glyph,
  overfull/underfull box, or LaTeX warning that affects the manuscript.
- The deterministic batch audit must verify structure, word/abstract/keyword
  limits, exact bibliography closure, citation-key closure, required
  declarations, claim/Route forbidden phrases, Stage-1/science-tree hashes,
  and the hashes of all Stage-2 outputs.
- An independent read-only review must check all five final manuscripts after
  the primary audit.

## 8. Stage boundary

Successful completion closes **Stage 2 only**. The state becomes
`AWAITING_STAGE_2_5_CONFIRMATION`; `STAGE2_5_INTEGRITY=false`. A separate
explicit user confirmation is required before any Stage-2.5 integrity work.
