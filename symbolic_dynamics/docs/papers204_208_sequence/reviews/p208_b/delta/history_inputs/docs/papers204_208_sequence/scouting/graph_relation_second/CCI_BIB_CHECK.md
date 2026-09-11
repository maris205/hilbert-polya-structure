# CCI bibliography and source-locator QA

2026-09-05 UTC. Checker: `/root/batch197_fosp_gate`.
Scope: three primary-source citation records and a short-manuscript risk
check only. **BIBLIOGRAPHY_QA_PASS**, with the publication-page locator
qualification below. This document supplies no new lemma, proof repair or
manuscript text and is not manuscript Review A/B. The checker previously
performed the independent CCI candidate gate; that prior familiarity must
be disclosed if the checker later reviews a manuscript.

The scientific scope is exactly the existing
[candidate gate's narrow contract](CCI_GATE/CANDIDATE_GATE.md), subject to
its [source deductions](CCI_GATE/SOURCE_GATE.md) and
[accepted author response](CCI_GATE/AUTHOR_RESPONSE.md).
This QA neither enlarges that contract nor independently certifies novelty.
Only this file was created; frozen gate evidence and earlier access-failure
records were not overwritten. `OWNER_AMBER / HOLD_EXTERNAL` remains.

## 1. Conflict-detection model: corrected citation

**Arik Motskin, Tim Roughgarden, Primoz Skraba and Leonidas Guibas.**
*Lightweight Coloring and Desynchronization for Networks.*
IEEE INFOCOM 2009, pp. **2383–2391**, **2009**.
DOI: [10.1109/INFCOM.2009.5062165](https://doi.org/10.1109/INFCOM.2009.5062165).

The initial task label “Hosseini 2013 desync” was corrected by root; it is
not this paper's author/year metadata and must not enter the bibliography.
The full names and title are printed on the
[readable nine-page author PDF](https://www.timroughgarden.algorithmsilluminated.org/papers/desync.pdf).
The proceedings year, page range and DOI are separately confirmed by
[Queen Mary's institutional publication record](https://www.seresearch.qmul.ac.uk/cfcs/publications/2009/)
under the exact title. The attempted IEEE landing-page open failed; no
publisher-page reading is claimed. No arXiv identifier was verified.

**Passage locators:** author PDF p. 2, Section II-A and Algorithm 1;
p. 3, Theorem 1. The model admits a current-colour/conflict-bit selection
function, so the information model is prior art. Algorithm 1 instead
resamples uniformly when conflicted, and Theorem 1 concerns that randomized
algorithm's proper-colouring convergence. These inspected passages do not
state the gated CCI deterministic arrival or inverse formulas. Do not cite
the randomized convergence theorem as a theorem about CCI.

## 2. The 2-total vertex-cover object

**Henning Fernau, Fedor V. Fomin, Geevarghese Philip and Saket Saurabh.**
*On the parameterized complexity of vertex cover and edge cover with
connectivity constraints.* Theoretical Computer Science **565**,
pp. **1–15**, **2015**.
DOI: [10.1016/j.tcs.2014.10.035](https://doi.org/10.1016/j.tcs.2014.10.035).

The [readable author-hosted journal PDF](https://fedorvf.github.io/articles/2015/2015f.pdf)
prints the title, all four authors, journal, year, volume and pages on p. 1,
with the DOI in its first-page footer. Its 2014 online-availability date is
not the journal volume's citation year.

**Passage locators:** journal/PDF p. 2, the explicit definition of
`t-Total Vertex Cover`; p. 4, Section 3's problem framing. The selected
vertices cover the edges and induce components of order at least `t`.
At `t = 2` this supplies the no-isolated-selected-vertex class used by the
gate. The empty-set and graph-isolate conventions must still be explicit
in CCI. This source supports deduction of the cover object and its
algorithmic study, not a new CCI claim about arbitrary-graph counting,
target-directed closure or the sharp dynamical fibre.

## 3. Total vertex-cover counting: direct text now checked locally

**Xavier Molinero, Fabián Riquelme and Maria Serna.**
*Satisfaction and Power in Unanimous Majority Influence Decision Models.*
Electronic Notes in Discrete Mathematics **68**, pp. **197–202**, **2018**.
DOI: [10.1016/j.endm.2018.06.034](https://doi.org/10.1016/j.endm.2018.06.034).

The [UPC deposit](https://upcommons.upc.edu/handle/2117/122635) contains an
author's final draft. Its cover sheet supplies the publication metadata;
the following page supplies all three full names. Direct locators are the
[standard download](https://upcommons.upc.edu/bitstreams/331d37a2-b15a-44a0-9de1-85a36f5f6d7b/download)
and the [repository API PDF](https://upcommons.upc.edu/server/api/core/bitstreams/331d37a2-b15a-44a0-9de1-85a36f5f6d7b/content).

**Passage locators:** Section 2, PDF p. 5, the total-cover discussion and
Theorem 2.4; PDF p. 6, its proof-sketch conclusion and **Corollary 2.5**.
The corollary establishes #P-completeness of counting total vertex covers.
The preceding discussion's “open problem” language is resolved by that
corollary and must not be quoted out of sequence. These passages deduct
the counting object and its complexity result; they do not state the
gated CCI colour-closure decoder or star extremum.

PDF p. 6 includes the warehouse cover in its numbering: it is body p. 5
of six. The draft does not print journal pagination. “Journal p. 201” is
an offset inference, **not an independently verified typeset-page locator**;
cite Corollary 2.5 and the whole published range instead.

### Actual access and local provenance

Fresh browser attempts to the UPC API, standard download and handle failed
during this task. Earlier successful reading is not represented as a fresh
browser success. Root subsequently reported a successful standard-download
retrieval, and the checker independently inspected that exact local PDF
using `file`, `pdfinfo`, `sha256sum` and `pdftotext` on PDF pages 1–2 and
5–6. Its page count is seven according to `pdfinfo`; the generic `file`
summary says six and must not determine passage numbering.

- Local read path: `/tmp/cci_total_cover_2018.pdf`.
- Size: `326380` bytes.
- SHA256: `50768214c2cfa283667fff4a04d23f6dfd2c75e7d9fc8772dfe533fbe8be4b93`.
- Checked text: deposit metadata, title/authors, total-cover discussion,
  Theorem 2.4 proof sketch, Corollary 2.5.

The temporary path is session-local evidence, not a promised archival copy.
Repository links plus the digest identify the source; preserving a source
snapshot would be a separate root integration action. No source PDF or
old gate record was created, replaced or rehashed by this QA.

## 4. Four-to-five-page manuscript risk check

This is a layout-risk checklist against the already proved contract, not
a proposed new theorem or ready-to-paste exposition. An indicative **4.5
pages including references** leaves only a small margin. The final compiled
PDF, not this estimate, decides compliance.

| Existing material | Indicative space | Risk to check in the actual draft |
|---|---:|---|
| Model, two-axis contract and source subtraction | 0.75 page | Explicit synchronous old-colour trigger, simple undirected graph and `q ≥ 3`; distinguish the owned conflict-bit model from the selected literal rule. Avoid presenting the static cover class as new. |
| Temporal theorem and existing proof | 1.25 pages | First conflict at time `d` means the first increment occurs in the update from `d` to `d+1`. Keep both inequalities for directed arrival, the no-spontaneous-seed argument, and the entrance-versus-period distinction. |
| Target inverse and existing proof | 0.8 page | Keep all three mask conditions and both directions of the reconstruction. The arc orientation and predecessor-closure convention must agree. A finite mask characterization is not an efficient counting algorithm. |
| Supporting static bound, dynamical maximum and equality cases | 1.1 pages | Compression must not delete the four-vertex cases, disconnected products, isolates, small-order exceptions or transfer from a monochromatic extremizer to the whole graph/target. Static support gets no standalone originality credit. |
| Limits, audit statement and references | 0.6 page | Carry all three verified citations; if other named automata are compared, retain their already checked references too. Finite verification is evidence, not the proof, and internal acceptance is not external novelty certification. |

Across these blocks, the highest-risk omissions are the time-index shift,
orientation of the inverse closure, and completeness of equality cases.
The recurrent description must permit distinct disconnected components to
be proper/fixed or rotating; a statement about a seeded component must not
silently become a statement that every graph component rotates. Empty
graphs, unseeded states and `n ≤ 2` need their original conventions.

No all-time inverse atlas, basin enumeration, efficient general cover
counter, new cover class, independently new static extremal theorem or
unqualified novelty statement should appear. If the full gated proofs do
not fit, shorten framing or remove optional exposition rather than omit a
dependency or use finite checks in place of proof. The compiler and later
independent manuscript review must still verify the completed artifact.

## Disposition

Three citation records and their bounded support are checked. The initial
desynchronization author/year mismatch is resolved. The formerly
inaccessible 2018 passage has now been independently read from root's
matching local download, without erasing historical access failures.
Remaining caveat: no published-page-specific Corollary 2.5 locator is
claimed beyond the author-draft PDF location. This file supplies only
source QA and drafting-risk observations; manuscript authorship and the
later A/B decisions remain separate.
