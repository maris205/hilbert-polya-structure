# HCS-C29 Phase-2 source verification

Verification date: **2026-08-11 (UTC)**  
Phase: **2 -- Investigation / source verification only**  
Sources reviewed: **18**  
Existence verified: **18**  
Rejected as fabricated: **0**

Full texts acquired locally: **0**  
Sources verified against original full text: **0/18**

This report grades citation fitness and verifies source existence.  It does not
perform Phase-3 synthesis, write a paper, or validate the repository's exact
matrix calculations.

## 1. Verification protocol

For every included source, the following checks were applied:

1. resolve the DOI at `https://doi.org/<doi>`;
2. match title, authors, year, venue and pages against an official publisher or
   discipline-archive page;
3. compare preprint and journal metadata where both were visible;
4. check the official page for an indicated correction or retraction;
5. grade fitness for the precise C29 claim, not for mathematics in general;
6. record currency, apparent conflict and venue-integrity status.

Semantic Scholar batch verification was attempted for all 18 DOI identifiers
and returned HTTP 429.  The audit therefore records
`[S2-API-UNAVAILABLE: rate limited]` and falls back to DOI plus official
publisher/archive metadata.  This degradation is not recorded as a failed
existence check.

The word **VERIFIED** below means bibliographic existence and metadata match,
not theorem-level verification against a locally acquired original.  For every
entry in this report, `source_acquired = false` and
`source_verified_against_original_full_text = false`.  Exact theorem wording,
hypotheses and locators must be checked from the original before quotation or
paper-stage use.

### Mathematical evidence scale

| Code | Meaning | Overall use grade |
|---|---|---|
| M1-direct | Original peer-reviewed proof/construction directly fits the cited claim | A |
| M1-framework | Original peer-reviewed foundational theorem; C29 must separately establish its hypotheses | A for framework, B for unproved C29 application |
| M2-integrity | Official correction/version-control record | A for integrity control |
| M2-adjacent | Primary theorem is rigorous but the object or hypotheses only partially overlap C29 | B |

The study-design Levels I--VII are not used as an ordinal ranking here: all
included items are theoretical mathematical sources, for which the relevant
gold standard is an original proof under explicit hypotheses.

## 2. Existence and quality matrix

`DOI 200` means the automated resolver reached a page successfully.  `DOI 403`
means the DOI resolved but the destination blocked automated access; in every
such case, an official or authoritative metadata page independently matched the
record.

| ID | Short source | DOI/metadata verification | Claim fitness | Currency | COI check | Venue/predatory check | Verdict |
|---:|---|---|---|---|---|---|---|
| 1 | Dougall--Sharp (2021) | DOI 200; Springer title/authors/volume/pages match | M1-direct for group-extension coding | Current enough; see 2024 correction | No commercial COI apparent; author intellectual stake only | *Inventiones* / Springer; no predatory signal | VERIFIED A, correction-linked |
| 2 | Dougall--Sharp correction (2024) | DOI 200; Springer correction page matches | M2-integrity | Current | Same authors; no commercial COI apparent | *Inventiones* / Springer; no predatory signal | VERIFIED A |
| 3 | Daon (2013) | DOI 200; AIMS title/volume/pages match | M1-direct under Walters/transitivity hypotheses | Foundational, not stale | No commercial COI apparent | DCDS/AIMS; no predatory signal | VERIFIED A |
| 4 | Hashimoto (1989) | DOI 200; ScienceDirect chapter metadata match | M1-framework | Seminal exemption | No commercial COI apparent; historical disclosure norms limited | Advanced Studies in Pure Mathematics/Academic Press; no predatory signal | VERIFIED A |
| 5 | Bass (1992) | DOI 403 after resolution; journal/DOI metadata match | M1-framework | Seminal exemption | No commercial COI apparent; historical disclosure norms limited | *International Journal of Mathematics*/World Scientific; no predatory signal | VERIFIED A |
| 6 | Stark--Terras (1996) | DOI 200; ScienceDirect metadata match | M1-direct for finite graph determinants | Seminal exemption | NSF/MSRI support stated; no commercial COI apparent | *Advances in Mathematics*/Elsevier; no predatory signal | VERIFIED A |
| 7 | Stark--Terras II (2000) | DOI 200; ScienceDirect metadata match | M1-direct for Artin twists | Foundational exemption | Research support disclosed; no commercial COI apparent | *Advances in Mathematics*/Elsevier; no predatory signal | VERIFIED A |
| 8 | Sato--Mitsuhashi--Morita (2014) | DOI 403 after resolution; Taylor & Francis metadata match | M1-direct for matrix weights | Foundational, still controlling claim | No commercial COI apparent | *Linear and Multilinear Algebra*/Taylor & Francis; no predatory signal | VERIFIED A |
| 9 | Fuglede--Kadison (1952) | DOI 403 after resolution; Annals/JSTOR metadata match | M1-framework for finite-factor determinant | Seminal exemption | No commercial COI information expected for period | *Annals of Mathematics*; no predatory signal | VERIFIED A |
| 10 | de la Harpe--Skandalis (1984) | DOI 200; Numdam metadata and full archive record match | M1-framework for trace determinant terminology | Seminal exemption | No commercial COI apparent; historical disclosure norms limited | *Annales de l'Institut Fourier*/Numdam; no predatory signal | VERIFIED A |
| 11 | Clair--Mokhtari-Sharghi (2001) | DOI 200; ScienceDirect metadata match | M1-framework; M2-adjacent to countable AGY | Foundational exemption | No commercial COI apparent | *Journal of Algebra*/Elsevier; no predatory signal | VERIFIED A/B |
| 12 | Lenz--Pogorzelski--Schmidt (2019) | DOI 403 after resolution; AMS-linked and arXiv metadata match | M1-framework; M2-adjacent to matrix-twisted AGY | Current enough | No commercial COI apparent | *Transactions AMS*; no predatory signal | VERIFIED A/B |
| 13 | Gérardin (1977) | DOI 200; ScienceDirect metadata match | M1-framework for finite Weil theory | Seminal exemption | NSF support stated; no commercial COI apparent | *Journal of Algebra*/Elsevier; no predatory signal | VERIFIED A |
| 14 | Thomas (2008) | DOI 403 after resolution; Oxford Academic metadata match | M1-direct for Weil characters | Foundational exemption | No commercial COI apparent | *Journal of the London Mathematical Society*/OUP; no predatory signal | VERIFIED A |
| 15 | Rauzy (1979) | DOI 200; official IMPAN metadata match | M1-framework | Seminal exemption | No commercial COI apparent; historical disclosure norms limited | *Acta Arithmetica*/IMPAN; no predatory signal | VERIFIED A |
| 16 | Veech (1982) | DOI 403 after resolution; official Annals metadata match | M1-framework | Seminal exemption | No commercial COI apparent; historical disclosure norms limited | *Annals of Mathematics*; no predatory signal | VERIFIED A |
| 17 | Zorich (1996) | DOI 200; Numdam metadata and archive record match | M1-framework | Seminal exemption | No commercial COI apparent | *Annales de l'Institut Fourier*/Numdam; no predatory signal | VERIFIED A |
| 18 | Avila--Gouëzel--Yoccoz (2006) | DOI 200; Numdam/publisher metadata match | M1-direct for AGY; M2-adjacent to symmetric C29 object | Foundational exemption | No commercial COI apparent; grant support is not a conflict | *Publications Mathématiques de l'IHÉS*; no predatory signal | VERIFIED A/B |

## 3. Claim-to-source verification matrix

| C29-facing claim | Best source support | Verdict | Required wording boundary |
|---|---|---|---|
| A group extension uses a forward cocycle, and a periodic point in the extension requires identity cocycle product | Dougall--Sharp (2021), checked with its 2024 correction | SUPPORTED | State the hypotheses and convention; do not attribute C25 freeness to this paper. |
| Passing to a genuine two-sided symbolic coding does not insert formal inverse letters into the forward cocycle | Dougall--Sharp convention plus Daon (2013); C29 semantic inference | SUPPORTED AS INFERENCE | Label it as an inference/definition check, not a named theorem in either paper. |
| Suitable two-sided countable-Markov potentials can be cohomologized to one-sided potentials with periodic sums preserved | Daon (2013) | SUPPORTED UNDER HYPOTHESES | Retain Walters/finite-variation and transitivity qualifications. |
| Finite non-backtracking/Hashimoto determinant identities are prior art | Hashimoto (1989), Bass (1992), Stark--Terras (1996) | SUPPORTED | No C29 novelty claim for the general determinant identity. |
| Representation and matrix/unitary twists of finite graph zeta are prior art | Bass (1992), Stark--Terras II (2000), Sato et al. (2014) | SUPPORTED | C29 novelty, if any, must be in the frozen relations and limit, not twisting itself. |
| Trace and von Neumann determinant machinery is prior art | Fuglede--Kadison (1952), de la Harpe--Skandalis (1984), Clair--Mokhtari-Sharghi (2001), Lenz et al. (2019) | SUPPORTED | Distinguish finite factors, Banach trace determinants, bounded-degree tree actions and measure graphs. |
| Lenz et al. directly prove the finite-Weil block-twisted C29 formula | Lenz et al. (2019) | NOT SUPPORTED DIRECTLY | Use Lenz for scalar measure-graph/groupoid context only; prove the finite block twist separately. |
| A countable weighted AGY inverse-branch determinant follows from infinite-graph Ihara theory | Clair--Mokhtari-Sharghi (2001); Lenz et al. (2019) | NOT SUPPORTED | Bounded-degree/action/measure and analytic summability hypotheses are different. |
| Finite-field symplectic Weil representations and character formulas are established | Gérardin (1977), Thomas (2008) | SUPPORTED | The exact (p^{-2}\Theta_p(g)) limit for frozen integral (g) is still a C27/C28 specialization. |
| Rauzy induction, finite-measure Zorich acceleration and the AGY roofed symbolic model are established | Rauzy (1979), Veech (1982), Zorich (1996), Avila--Gouëzel--Yoccoz (2006) | SUPPORTED | These sources do not turn formal inverse branch matrices into genuine positive-time AGY branches. |
| The declared symmetric C26 inverse-arrow graph is the AGY natural extension | No included primary source | UNSUPPORTED / MUST NOT CLAIM | Continue to call it a newly declared symmetric return-matrix groupoid. |
| The inverse-arrow system has an intrinsic positive AGY roof | No included primary source | UNVERIFIED | A geometric derivation is a future stop/go gate. |
| The C25 length-six and C26 length-24 identity relations are established in prior literature | No included source; repository exact certificates only | REPO-SPECIFIC | Cite exact code/certificates, chronology and hashes; do not present a bounded search as global novelty proof. |

## 4. Correction, retraction and integrity audit

- The 2021 Dougall--Sharp paper has an official 2024 correction.  The
  correction page states that its listed main results remain unchanged.  The
  correction must be carried beside the original in any final bibliography.
- No other included publisher/archive page displayed a correction or
  retraction notice during this bounded check.
- This is not a complete Retraction Watch, MathSciNet or zbMATH audit.  The
  statement above means “none indicated on the verified official pages,” not
  a universal negative.
- No predatory-journal alert was triggered.  All 18 items are hosted by
  established mathematical journals, publishers or official archives.
- No commercial conflict relevant to the mathematical claims was identified.
  Several articles disclose ordinary grant support.  Author investment in
  one's own theorem is recorded as an intellectual interest, not a financial
  conflict.

## 5. Novelty boundary verification

### Established prior art

The external sources verify that the following frameworks predate C29:

- non-backtracking/Ihara/Hashimoto determinant identities;
- Artin, representation and matrix-weighted graph-zeta twists;
- group/von Neumann trace extraction and trace-associated determinants under
  explicit finite-factor, bounded-degree or measure-graph hypotheses;
- finite Weil representations and character formulas;
- Rauzy--Veech/Zorich/AGY symbolic and roofed dynamics;
- forward symbolic group extensions and one-/two-sided potential reductions.

### Search-bounded repository delta

The literature audit found no external source containing the frozen C25/C26
matrices and the exact relations asserted in this repository.  The defensible
repository delta is therefore limited to:

1. the exact two length-six C25 identity-holonomy witnesses;
2. the exact C26 braid relation and expanded primitive length-24 word;
3. the no-go showing that the genuine positive natural extension retains the
   regular-trace collapse, using the repository's positive-monoid result;
4. the locally uniform finite-Weil normalized determinant limit for the newly
   declared finite symmetric path system;
5. the explicit separation between this algebraic system and the unresolved
   geometric roof/two-sided trace theorem.

This is a **search-bounded novelty boundary**, not proof that no equivalent
relation exists anywhere in the literature.

## 6. Blockers and limitations

### Critical blockers

None for proceeding from Phase 2 to a scoped algebraic Phase-3 analysis.

### Noncritical gates that remain

1. **Correction handling:** any detailed reliance on Dougall--Sharp beyond the
   basic group-extension convention must be checked against the 2024
   correction.
2. **Object identity:** no source supports calling the declared symmetric C26
   system the AGY natural extension.
3. **Roof/operator theorem:** no source supplies an intrinsic positive roof or
   a two-sided nuclear/flat-trace theorem for the formal inverse branches.
4. **Novelty completeness:** MathSciNet/zbMATH full-text citation-chain and
   relation-level searches were not available; novelty remains bounded.
5. **Programmatic verification degradation:** Semantic Scholar returned HTTP
   429.  All 18 sources nevertheless passed DOI plus official-metadata checks.

## 7. Phase-boundary handoff

The Phase-2 corpus is sufficient for a later synthesis agent to compare the
finite combinatorial determinant with the genuine AGY object.  This file does
not perform that comparison.  Any Phase-3 work must preserve the claim-source
boundaries above and must not convert absence of a source into an impossibility
theorem.
