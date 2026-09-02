# Paper 30 — Stage 1 Phase 2 independent source verification

Date: **2026-09-02 UTC**

Seat: **VERIFY-SEAT-C**

Post-patch recheck status: **RESOLVED_POST_VERIFICATION**

Disposition: **PHASE2_SOURCE_BASE_READY_WITH_WARNINGS**

## Verification fence

This is an independent ARS Phase-2 source-verification artifact. It verifies
the existence, core metadata, venue, currency, conflict-of-interest limits,
retraction-check status, and bounded claim fitness of the 26 records supplied
by BIB-SEAT-A. It does **not** perform Phase-3 synthesis or novelty assessment,
construct or evaluate a roof/operator/determinant, run scientific computation,
inspect target results, or assign a Route tuple.

A verified general theorem is not thereby an applicability theorem for the
open three-disk repeller. A verified quantum or semiclassical determinant is
not thereby the typed classical nonconstant-roof transfer determinant frozen
for Paper 30.

No Semantic Scholar query was performed, so no record is labeled
S2_VERIFIED. No API-degradation claim is made. All DOI-bearing records were
checked against Crossref DOI metadata and a DOI-resolved publisher or official
journal record. The one DOI-less record was checked on its first-party arXiv
record.

## Hash-bound inputs

| Input | SHA-256 |
|---|---|
| BATCH_ROUND10_STAGE1_PHASE2_VERIFICATION_CONTRACT.md | 41f3881f0fa428c3ce324a12f12bd514649aff652114cc436d5932fb3cb8b72e |
| stage1_phase1_rq_brief.md | 87bf07d94ba92fc69f7c1f8bd73cdf6d8dcc2f5331d6478b3d11ba6c1aa68cf0 |
| stage1_phase1_methodology_blueprint.md | 167c890be3e7dd771542e4c48d8b15015368ba86f8595b838dd04f7a3b6a953a |
| stage1_phase1_checkpoint.md | adb1d4dab9b270f9a40b4fb7eb0923fc2d6ce1d50de07d2441e12a8e091d0b5e |
| stage1_phase2_annotated_bibliography.md (post-patch) | efa7a8b33fa37995f3345f46b232efd4515033d73e2a03f9e5919f59d2977e31 |
| stage1_phase2_source_inventory.tsv | 72c5383b65a23b32983f124c667bac1efdcbe71695e22d8d3d81fb7d5aa4140f |

The bibliography and inventory remained read-only to VERIFY-SEAT-C during the
post-patch pass.

## Post-patch independent recheck

| Audit binding | SHA-256 / result |
|---|---|
| Correction manifest | `59506776c0c536dbfd5b3ee511dd0ac0a52ae74548d08f3cd0dfb7ec9a8fd49c` |
| Initial verification MD | `6771d4c5e46c1ba45b98793fcd20a168da892f7eedfa2dd8fdf9f7af343d204d` |
| Initial verification TSV | `77aa142e4778eb048e2e4e40353c874a86e161de29ccb64670a18fc5f209e848` |
| Bibliography pre-patch / post-patch | `67fd941099205718e203025e92f78fcb976f58951b24cb4aacf1f48615a9e4c0` / `efa7a8b33fa37995f3345f46b232efd4515033d73e2a03f9e5919f59d2977e31` |
| Inventory pre-patch / post-patch | `72c5383b65a23b32983f124c667bac1efdcbe71695e22d8d3d81fb7d5aa4140f` / `72c5383b65a23b32983f124c667bac1efdcbe71695e22d8d3d81fb7d5aa4140f` |
| `R10PH2-C02` | `RESOLVED_POST_VERIFICATION`: P30-S01 and P30-S02 are explicitly bound to correction companion DOI `10.1063/1.457669`. |
| `R10PH2-C03` | `RESOLVED_POST_VERIFICATION`: P30-S03 is explicitly bound to correction companion DOI `10.1063/1.457670`. |
| Corpus invariant | 26 unique inventory IDs; 26 verification TSV rows; correction companions add no evidence rows. |

The manifest and current post-patch hashes were re-computed locally. The
annotated bibliography contains all three exact correction bindings, while the
inventory remains byte-identical and contains 26 source rows. These repairs
close the omission without changing the typed support boundaries or making the
correction notices independent corpus entries.

## Method and audit coverage

- Inventory cardinality: **26 unique IDs**, P30-S01 through P30-S26.
- DOI-bearing records: **25/26**, all checked through Crossref DOI metadata
  and DOI-resolved publisher or official journal pages.
- DOI-less records: **1/26**, P30-S18, checked on the first-party arXiv record.
- Existence outcomes: **26 VERIFIED**, 0 PLAUSIBLE, 0 UNVERIFIABLE,
  0 FABRICATED, and 0 S2_VERIFIED.
- Core metadata: **26/26 exact after bounded normalization**. Two publication
  chronology differences remain documented below. The three correction
  companion bindings are `RESOLVED_POST_VERIFICATION`; no inventory edit or
  additional source row was required.
- Peer-reviewed journal records: **24/26 = 92.3%**. P30-S10 and P30-S18
  remain conservatively outside the numerator.
- Independent second-source checks: **11/26 = 42.3%**, exceeding the 30%
  contract floor.
- Mathematical and mathematical-physics evidence grading: every source is
  recorded at field-neutral **Level VI**. The separate A–F grade measures
  fitness for the exact bounded claim surface, not study-design rank.
- Venue assessment is bounded to publisher/journal identity, recorded review
  status, and observable red flags. It is not an exhaustive commercial-index,
  editorial-board, COPE, or Cabells audit.
- No structured live retraction-database query was run. Every row is therefore
  explicitly NOT_CHECKED; none is described as retraction-clean.
- Source-level conflict declarations and complete funding statements were not
  audited across the corpus. Every row is therefore UNKNOWN_NOT_AUDITED.

## Outcome summary

| Audit dimension | Result |
|---|---:|
| VERIFIED existence | 26 |
| Exact core metadata after bounded normalization | 26 |
| Correction companion bindings resolved post-verification | 3 |
| Correction companion bindings unresolved | 0 |
| Field-neutral Level VI | 26 |
| Claim-fitness A | 8 |
| Claim-fitness B | 16 |
| Claim-fitness C | 2 |
| DIRECT_PREREQUISITE | 9 |
| ADJACENT_METHOD | 10 |
| BACKGROUND_ONLY | 7 |
| EXCLUDE_FROM_CLAIM_USE | 0 |

The grades and support classes apply only to the stated “can support” surface.
They do not certify Paper 30's physical-roof ledger, comparison map, four-error
contract, determinant implementation, or scientific result.

## Per-source claim fitness and support boundary

| Source | Existence / metadata | Level / grade | Exact support_class | Can support | Cannot support |
|---|---|---|---|---|---|
| [P30-S01](https://doi.org/10.1063/1.456017) | VERIFIED; exact; correction companion bound; `RESOLVED_POST_VERIFICATION` | VI / A | DIRECT_PREREQUISITE | The classical three-hard-disk repeller, collision coding, physical orbit geometry, and geometrical lengths, when read with DOI 10.1063/1.457669. | Fidelity of any project ledger, a chosen transfer-operator function space, or a certified determinant/error bound. |
| [P30-S02](https://doi.org/10.1063/1.456018) | VERIFIED; exact; correction companion bound; `RESOLVED_POST_VERIFICATION` | VI / B | BACKGROUND_ONLY | The semiclassical three-disk periodic-orbit and Ruelle-zeta construction, when read with DOI 10.1063/1.457669. | Identification of the semiclassical spectral function with the classical physical-roof transfer determinant. |
| [P30-S03](https://doi.org/10.1063/1.456019) | VERIFIED; exact; correction companion bound; `RESOLVED_POST_VERIFICATION` | VI / C | BACKGROUND_ONLY | The exact quantum S-matrix/multiscattering determinant as a typed comparator, when read with DOI 10.1063/1.457670. | Substitution of the quantum determinant for a classical transfer determinant or proof of roof specificity. |
| [P30-S04](https://doi.org/10.1103/PhysRevLett.63.823) | VERIFIED; exact | VI / B | ADJACENT_METHOD | Periodic-orbit/cycle organization in a three-disk chaotic-scattering setting. | Nuclearity, a common coefficient basis, or a four-component numerical error certificate. |
| [P30-S05](https://doi.org/10.1088/0305-4470/24/5/005) | VERIFIED; exact | VI / B | ADJACENT_METHOD | Cycle-expansion organization for classical smooth flows and periodic-orbit weights. | Convergence or coefficient accuracy for Paper 30's uninstantiated roof/operator and cutoffs. |
| [P30-S06](https://doi.org/10.1016/S0370-1573(98)00036-2) | VERIFIED; exact | VI / B | BACKGROUND_ONLY | n-disk symbolic itineraries and the distinction among exact-quantum, semiclassical, and classical periodic-orbit objects. | Transfer of quantum trace-class determinant results to the frozen classical roof operator. |
| [P30-S07](https://doi.org/10.2307/2373793) | VERIFIED; exact | VI / A | DIRECT_PREREQUISITE | The foundational Markov/symbolic coding interface for a hyperbolic flow and a return-time roof. | Identification of the exact three-disk collision section, branch map, or pointwise flight roof. |
| [P30-S08](https://doi.org/10.1007/BF01389848) | VERIFIED; exact | VI / B | BACKGROUND_ONLY | General Axiom-A flow, suspension, periodic-orbit, and thermodynamic-formalism background. | Automatic applicability to a noncompact ambient open billiard or its exact transfer space. |
| [P30-S09](https://doi.org/10.5802/aif.1137) | VERIFIED; exact | VI / A | DIRECT_PREREQUISITE | Rigorous several-strictly-convex-obstacle trajectory geometry and periodic-ray framework. | Paper 30's discretization, coefficient window, determinant definition, or numerical tolerance. |
| [P30-S10](https://doi.org/10.5802/jedp.457) | VERIFIED; exact | VI / B | BACKGROUND_ONLY | A primary bridge among several-convex-body periodic trajectories, zeta functions, and scattering poles. | Peer-reviewed-journal weight, project roof fidelity, or cross-roof nontransfer. |
| [P30-S11](https://doi.org/10.1353/ajm.2001.0029) | VERIFIED; exact | VI / A | DIRECT_PREREQUISITE | The most direct corpus theorem for a Ruelle operator and return-time weights on planar open billiard flows under stated convexity/visibility hypotheses. | Applicability without matching those hypotheses, normalization, coding, roof convention, and function space to Paper 30. |
| [P30-S12](https://doi.org/10.1088/0951-7715/24/4/005) | VERIFIED; exact | VI / B | ADJACENT_METHOD | Conditional spectral estimates for transfer operators of Axiom-A flows with general potentials. | A theorem for every open billiard, or a choice of Paper 30's rank, orbit cutoff, basis, and comparison window. |
| [P30-S13](https://doi.org/10.1007/BF01403069) | VERIFIED; exact | VI / A | DIRECT_PREREQUISITE | The foundational periodic-zeta/transfer relation for expanding maps and Anosov flows. | Physical specificity: the formal identity is available to consistently built control roofs as well. |
| [P30-S14](https://doi.org/10.1007/BF02699133) | VERIFIED; exact | VI / A | DIRECT_PREREQUISITE | Fredholm-type determinant machinery for specified dynamical operators under the paper's contraction/smoothness hypotheses. | Trace-class or nuclear status of an unconstructed Paper 30 operator, or distinction of physical from shuffled/unit roofs. |
| [P30-S15](https://doi.org/10.1007/BF01388795) | VERIFIED; exact | VI / B | ADJACENT_METHOD | Meromorphic continuation of generalized zeta functions in the stated Axiom-A setting. | Pointwise three-disk flight times or a legal finite-rank/orbit coefficient comparison. |
| [P30-S16](https://doi.org/10.1007/BF02099469) | VERIFIED; exact | VI / B | ADJACENT_METHOD | Meromorphic zeta and operator machinery for isolated compact hyperbolic sets of real-analytic flows. | Applicability without proving analytic/model hypotheses or a four-error project interface. |
| [P30-S17](https://doi.org/10.4007/annals.2013.178.2.6) | VERIFIED; exact; correction-bound | VI / B | ADJACENT_METHOD | Meromorphicity of the Ruelle zeta function for the stated smooth Anosov setting; the erratum says this first part is unaffected. | The affected Section-7 maximal-entropy spectral-gap claim unless read with S18; any direct theorem for the three-disk roof ledger. |
| [P30-S18](https://arxiv.org/abs/2203.04917) | VERIFIED; exact first-party erratum | VI / B | DIRECT_PREREQUISITE | The mandatory correction boundary for S17: it fixes the affected spectral-gap argument and states that first-part meromorphicity is unaffected. | Independent peer-reviewed support or physical-roof/determinant specificity. |
| [P30-S19](https://doi.org/10.1007/s00220-007-0355-7) | VERIFIED; exact | VI / B | ADJACENT_METHOD | Explicit a priori transfer-operator eigenvalue bounds on the source's eligible spaces. | A tail bound before Paper 30's operator space, constants, and hypotheses are instantiated. |
| [P30-S20](https://doi.org/10.1016/j.aim.2008.02.005) | VERIFIED; exact | VI / B | ADJACENT_METHOD | Explicit eigenvalue estimates for suitable transfer operators on holomorphic/Bergman spaces. | Proof that the coded three-disk operator acts on the required holomorphic domain or chosen basis. |
| [P30-S21](https://doi.org/10.1007/s00211-019-01031-z) | VERIFIED; exact | VI / B | ADJACENT_METHOD | Spectral-Galerkin error analysis for one-dimensional full-branch uniformly expanding Markov maps. | Automatic transplantation of its basis/rates to an open-billiard flow operator without a derived comparison map. |
| [P30-S22](https://doi.org/10.1090/S0025-5718-09-02280-7) | VERIFIED; exact 2010 issue year; 2009 e-publication noted | VI / B | ADJACENT_METHOD | Numerical evaluation and quadrature-driven approximation error for Fredholm determinants of eligible trace-class integral operators. | Proof that Paper 30's operator is trace class, that orbit and projection coefficients share a map, or that all four project errors are bounded. |
| [P30-S23](https://doi.org/10.1070/IM1972v006n06ABEH001919) | VERIFIED; exact | VI / A | DIRECT_PREREQUISITE | The foundational periodic-data obstruction for cohomological triviality in stated hyperbolic/symbolic settings. | A global positive cohomology conclusion from a finite orbit sample or unverified system hypotheses. |
| [P30-S24](https://doi.org/10.2307/1971334) | VERIFIED; exact | VI / A | DIRECT_PREREQUISITE | Regularity and perturbative foundations for the Livšic cohomology equation in Anosov systems. | Replacing equality of all required periodic sums with shuffled-label similarity or finite numerical agreement. |
| [P30-S25](https://doi.org/10.4007/annals.2011.173.2.11) | VERIFIED; exact | VI / C | BACKGROUND_ONLY | A stronger matrix-cocycle periodic-data/coboundary theorem over hyperbolic systems. | Necessity for the scalar roof comparison, exact three-disk applicability, or any project-specific nontransfer result. |
| [P30-S26](https://doi.org/10.1112/blms.70258) | VERIFIED; exact 2026 issue assignment; 2025 online-first noted | VI / B | BACKGROUND_ONLY | Current abelian Livšic extensions for homologically full transitive Anosov flows under the stated hypotheses. | Direct applicability to the open three-disk repeller or a positive conclusion from Paper 30's finite registered cutoff. |

## Applicability boundary: physical three-disk versus general flow theory

1. **Physical object layer.** S01 is the direct classical three-hard-disk
   source. S02 is semiclassical, S03 exact quantum, and S06 primarily
   quantum/semiclassical. Their shared geometry does not collapse their
   determinant types. S04–S05 support cycle organization, not project-level
   determinant existence or certification.
2. **Open-billiard layer.** S09–S11 are the closest rigorous obstacle/open-
   billiard sources. Even these require an explicit match of dimension,
   obstacle separation/visibility or no-eclipse assumptions, trapped set,
   section, normalization, and operator space.
3. **General hyperbolic-flow layer.** S07–S08 and S12–S17 apply only under
   their own expanding, Axiom-A, Anosov, compact-hyperbolic-set, smoothness,
   analyticity, pinching, or function-space hypotheses. The bibliography does
   not itself prove their transfer to the exact three-disk instance.
4. **Numerical layer.** S19–S22 provide separable spectral-tail, projection,
   and determinant-evaluation methods. None supplies the missing legal map
   among Paper 30's orbit cutoff, finite-rank cutoff, coefficient basis/window,
   and typed roof.
5. **Cohomology layer.** S23–S26 constrain what periodic data can establish.
   A verified differing periodic sum may obstruct equivalence after hypotheses
   are checked; finite agreement cannot prove global equivalence.

## Independent second-source cross-checks

The following 11 key records received a second check independent of the
primary publisher landing-page display.

| Source | Independent authoritative locator | Facts cross-checked |
|---|---|---|
| P30-S01 | [Pierre Gaspard author publication list](https://gaspard.pierre.web.ulb.be/articles.html) | title, authors, year, journal/pages, and the now-bound correction companion |
| P30-S02 | [Pierre Gaspard author publication list](https://gaspard.pierre.web.ulb.be/articles.html) | title, authors, year, journal/pages, and the now-bound correction companion |
| P30-S03 | [ULB-linked OpenAIRE record](https://explore.openaire.eu/search/publication?pid=10.1063%2F1.456019) and [author list](https://gaspard.pierre.web.ulb.be/articles.html) | title, authors, year, venue/pages, DOI, typed exact-quantum scope, and the now-bound correction companion |
| P30-S09 | [Centre Mersenne article record](https://aif.centre-mersenne.org/articles/10.5802/aif.1137/) | title, author, year, volume/issue/pages, DOI, and obstacle scope |
| P30-S11 | [University of Western Australia record](https://research-repository.uwa.edu.au/en/publications/spectrum-of-the-ruelle-operator-and-exponential-decay-of-correlat/) | title, author, year, venue/pages, DOI, peer-review label, and exact open-billiard hypotheses |
| P30-S12 | [University of Western Australia record](https://research-repository.uwa.edu.au/en/publications/spectra-of-ruelle-transfer-operators-for-axiom-a-flows/) and [arXiv:0810.1126](https://arxiv.org/abs/0810.1126) | metadata, DOI, and conditional Axiom-A scope |
| P30-S17 | [first-party Annals record](https://annals.math.princeton.edu/2013/178-2/p06) and [S18 author erratum](https://arxiv.org/abs/2203.04917) | metadata and exact corrected versus unaffected claim boundary |
| P30-S21 | [author-hosted primary manuscript](https://wormell.perso.math.cnrs.fr/preprints/W17S-preprint.pdf) and [arXiv:1705.04431](https://arxiv.org/abs/1705.04431) | author/title and one-dimensional expanding-map method scope |
| P30-S22 | [AMS version-of-record PDF](https://www.ams.org/mcom/2010-79-270/S0025-5718-09-02280-7/S0025-5718-09-02280-7.pdf) | title, author, 2010 volume/issue/pages, 2009 electronic-publication date, DOI, and numerical-only scope |
| P30-S23 | [MathNet first-party journal record](https://www.mathnet.ru/eng/im2373) | title, author/transliteration, year, volume/issue/pages, DOI, and cohomology scope |
| P30-S26 | [Warwick institutional record](https://wrap.warwick.ac.uk/id/eprint/194803/) | title, author, DOI, peer-review status, 2026 volume/issue/article number, and 2025/2026 publication chronology |

## Venue, currency, COI, and retraction findings

1. The 24 peer-reviewed records are attached to established journals and
   recognized scholarly publishers; no observable predatory-venue red flag was
   found. This is a bounded venue assessment, not a fresh audit of all indexes,
   boards, and ethics policies.
2. P30-S10 is an established research-proceedings article but is conservatively
   not counted as peer reviewed. P30-S18 is a first-party arXiv erratum and is
   also not counted as peer reviewed.
3. P30-S18 and P30-S26 fall in the 2021–2026 default currency window. The 24
   older sources are retained only for origin-model, historical, theorem,
   correction, or foundational method claims; that exemption does not support
   a literature-absence or novelty inference.
4. COI status is UNKNOWN_NOT_AUDITED for all 26 sources. Publisher or
   repository affiliation/funding displays were not converted into conflict
   judgments.
5. Retraction status is NOT_CHECKED for all 26 sources because no structured
   live retraction query was completed. The known correction relationships
   below are not retraction-clearance findings.

## Metadata errata and record-display discrepancies

| ID | Record | Finding | Disposition |
|---|---|---|---|
| CORR-P30-01 | P30-S01 | JCP 91(5), 3279 contains a formal correction to equations in the classical paper; DOI 10.1063/1.457669. The patched bibliography explicitly binds it. | `RESOLVED_POST_VERIFICATION`. The binding is exact and mandatory before formula-level use; original metadata and the 26-row inventory remain unchanged. |
| CORR-P30-02 | P30-S02 | The same JCP 91(5), 3279 notice separately corrects equations/text in the semiclassical paper; DOI 10.1063/1.457669. The patched bibliography explicitly binds it. | `RESOLVED_POST_VERIFICATION`. The binding is exact and mandatory before formula-level use; original metadata and the 26-row inventory remain unchanged. |
| CORR-P30-03 | P30-S03 | JCP 91(5), 3280 corrects Eq. 5.4, appendix expressions, and text in the exact-quantum paper; DOI 10.1063/1.457670. The patched bibliography explicitly binds it. | `RESOLVED_POST_VERIFICATION`. The binding is exact and mandatory before formula-level use; original metadata and the 26-row inventory remain unchanged. |
| BIND-P30-01 | P30-S17/S18 | S18 states that the error lies in the Section-7 maximal-entropy spectral-gap part of S17 and that the first meromorphicity part is unaffected. | Existing corpus binding is correct. Any affected spectral-gap use must cite/read both; no unqualified S17-only use. |
| DISP-P30-01 | P30-S22 | AMS assigns volume 79, issue 270, April **2010**, pages 871–915, while recording electronic publication on **2009-09-24**; Crossref may expose the earlier date. | Inventory year 2010 is the correct issue/citation year. This is publication chronology, not an inventory erratum. |
| DISP-P30-02 | P30-S26 | Wiley gives first publication **2025-12-19** and issue online **2026-01-21**; Wiley's citation and Warwick's official record assign **2026**, volume 58(1), e70258. | Inventory year 2026 is the correct issue/citation year. Preserve the online-first date as provenance; no inventory erratum. |

No other title, author, year, venue, DOI, volume, issue, page, or article-number
error was found in this bounded verification pass.

## Paper-level Phase-2 disposition

**PHASE2_SOURCE_BASE_READY_WITH_WARNINGS**

The corpus clears the full-mode source-count and peer-review thresholds; all
26 inventory IDs exist on authoritative records; every ID appears exactly once
in the verification TSV; and the bounded source base is fit to enter a later
Phase-3 evidence-synthesis gate.

The S01–S03 correction omissions are closed as
`RESOLVED_POST_VERIFICATION`; their now-bound companions remain mandatory for
formula-level use. Warnings remain for the mandatory S17/S18 affected-claim
binding, the strict physical-three-disk versus general Axiom-A/open-billiard
applicability boundary, S22's numerical-method-only fitness, unknown
source-level COI, and the absence of a structured live retraction check.

This disposition does not establish pointwise physical roof/coding fidelity,
operator nuclearity, a common finite-rank/orbit comparison map, cross-roof
nontransfer, any determinant value, any scientific result, novelty, or Route
status.
