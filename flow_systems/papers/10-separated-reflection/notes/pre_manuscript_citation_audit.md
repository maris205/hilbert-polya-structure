# Paper 10 pre-manuscript citation/source-integrity audit

Frozen: **2026-08-14 (Asia/Shanghai)**  
Scope: bibliography and locator readiness only; no theorem, Route, manuscript,
BibTeX, source-lock, or control artifact was edited.  
Method: ARS citation-compliance and claim--reference-alignment review against
the final Phase-2 source corpus and the final proof/Route locks.

## 1. Exact audited inputs

| Input | SHA-256 |
|---|---|
| `notes/phase2_source_novelty_audit.md` | `8b4a2ff1ed911765faa294c43cfbfb9f4986624e972ee4bcb509b12321e658fa` |
| `notes/sources/scope_source_manifest.md` | `38fd6557eba364eff748b35a62ac28bf768b75a259e1e7631099149f67118140` |
| `notes/sources/scope_sources.sha256` | `222c1a6d9552c82890bcc3846245fb4c636eef981a5937b7355d45f5626497aa` |
| `notes/phase2_domain_source_audit.md` | `8dbc4e6487d342bcf352a4b0161bc1c4f17800d07556a3d11b49ce900b3aa582` |
| `notes/sources/dom-source-manifest.md` | `49e20c34eff26915780f43b5df7d5b6635fa35d6225b63ea476cbeab1c14af21` |
| `notes/sources/dom-sources.sha256` | `34ed23b73f01f5027deaa5084bce250d5f77c1dbcd02c38627c950e5803d13ce` |
| `notes/phase2_precedent_search.md` | `68aef453788251edb0e7aad631ea58ca1794fc23e255d5c96b3d8c39030d5719` |
| `notes/phase2_final_gate.md` | `1421ada08a7192e14e7edf4ab9982523c275063dee0c23c1d2f076ac4bf13ffb` |
| `notes/proof_audit.md` | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` |
| `notes/phase3_peer_review.md` | `cd075d267865812c2368679346a2dfde9a5a976d4306b4dc61664adf5f8a3a7e` |
| `notes/route_audit.md` | `fded0943eb3c628e90b407c14aece688b1a79f8be4510c02e98010592b9ca4ee` |
| `results/separated_reflection_controls_manifest.json` | `edc2461873b237ee5050ab24612ca1065e256d33147ccca66fdcf99159e68215` |

The two checksum ledgers verify the twelve retained Paper-10 PDFs and their
preflight sidecars.  Paper 9's Deninger source remains inherited rather than
copied: PDF `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09`,
preflight `0526c6a84b907d109db4e2932cbb378b60b172dce8981c034d866e398a25a9e4`,
and Paper-9 source manifest
`8dd678dc33fa7396484c8c8d63a91943f6755da24eedefa0471860fa94e42906`.

## 2. Verdict

**PASS TO DRAFTING; BIBLIOGRAPHY FREEZE AND PUBLIC RELEASE ARE CONDITIONAL.**

There is no missing mathematical source that blocks drafting.  The retained
corpus is sufficient and nonredundant once optional notation sources are
omitted.  Four bounded metadata/manifestation gates below are mandatory
before the bibliography and release bytes may be declared final.  They do not
authorize expansion of the Phase-2 source search.

## 3. Bounded bibliography and locator plan

### 3.1 Core, expected citations

| Provisional key | Exact role and locator | Manifestation rule |
|---|---|---|
| `Wang2026Packet` | Paper 9 owns the actual nontrivial indiscreteness theorem imported by Paper 10. Cite at the single import point, not as owner of the separated-reflection results. | Use the exact Paper-9 paper/PDF only provisionally; the final entry requires the stable public identity in M1 below. |
| `Deninger2026` | Rational-Witt object, finite set packet, quotient set, suspension/action and stabilizer: arXiv v4 physical pp. 32--33 and 38--39. | Bibliographic identity may use *Indagationes Mathematicae* 37(1) (2026), 25--136, DOI `10.1016/j.indag.2024.05.007`; the entry/note must say the cited locators are in arXiv `v4`, 2024-02-07. It must not credit Deninger with Paper 10's transported topology or reflection theorem. |
| `CagliariMantovani2003` | `Top_0` reflection and its unique-factorization property: physical pp. 3--4. | Published title, journal 132 (2003), 129--138, DOI `10.1016/S0166-8641(02)00370-X`; note that the inspected manifestation is the author preprint. |
| `HernandezArzusaHernandez2020` | Reflection/epireflection vocabulary and separated reflective subcategories: physical p. 2 and pp. 3--6. | Pin arXiv `1704.01146v2` for locators and reconcile its title with the published DOI record under M2. |
| `Pirttimaki2021` | Topological indistinguishability, Kolmogorov quotient and induced-map context: physical pp. 4--6, 9, and 12--13. | Pin arXiv `1905.01157v2`, updated 2021-12-02. Use as terminology/context; Paper 10 proves its own specialized statements. |
| `Preston2008` | Standard Borel and countably separated definitions: physical pp. 3 and 13. | Pin arXiv `0809.3066v1`, 2008-09-18. |
| `FremlinMeasureCh11Dev` | Sigma-algebra, generated sigma-algebra, positive measure and Dirac mass: physical pp. 4--6. | Identify the exact results-only Chapter 11 PDF, version shown as 2002-09-30; do not silently substitute a printed-volume locator. |
| `FremlinMeasureCh41Dev` | Hausdorff Radon convention and its Hausdorff-dependent consequences: physical p. 5 and pp. 66--67. | Identify the exact development Chapter 41 PDF, version shown as 2006-12-14, with its canonical author URL; apply M3. |
| `Lipsman1972` | Competing positive-Radon convention on a locally compact, possibly non-Hausdorff space: physical p. 10 / printed p. 461. | Publisher scan, *Pacific Journal of Mathematics* 42(2) (1972), 453--467. Do not invent a DOI; apply M4. |
| `HofmannTopologicalGroups` | Quotient topological groups and topological-group separation: physical pp. 5--6 and 10--11. | University-hosted course notes; use neutral manifestation metadata until the cover-year anomaly in M4 is resolved. |
| `HoermannCStar2026` | Norm/SOT/WOT on the common carrier `B(H)`, their Hausdorffness, and order: physical p. 43 / printed p. 39. | Pin *C*-Algebras with Aspects of Quantum Physics*, Winter 2023/24 notes, version 2026-08-06, and canonical university URL. |
| `StacksCoproduct0B1W` | Tagged coproduct carrier and coproduct topology, if the manuscript cites the standard definition. | Prefer stable Stacks Project Tag `0B1W` over the incomplete book-sample metadata; access date must be frozen at final release. |

This is a ceiling, not a target count.  A core entry is retained only if the
final prose contains the stated source-owned claim.  Uncited entries must not
remain in `references.bib`.

### 3.2 Bounded adjacency/novelty citations

If the manuscript includes a related-work or novelty paragraph, it may add
only the Phase-2 nearest neighbours already frozen there: Deninger's 2024
survey, Morishita's arXiv `2508.15971v5`, and Deninger's arXiv
`2508.05329`.  Connes--Consani may be retained only when the standard-circle
comparison is actually discussed.  The permitted wording is:

> No direct precedent for the exact rational-Witt
> separated-reflection/observable/measure package was found in the bounded
> Phase-2 search completed on 2026-08-14.

Do not replace this with “first”, “novel”, “unprecedented”, or an exhaustive
literature claim.  Adjacent works support adjacency facts; they cannot be
cited as evidence that a precedent is absent.

### 3.3 Default omissions

- Omit Amini unless a sentence really needs an external convention for
  `C(X)`, `C_b(X)`, `C_0(X)`, or `C_{00}(X)`; defining the notation directly
  is cleaner and avoids transporting its locally compact Hausdorff domain.
- Omit Fremlin Chapter 34 when Preston alone supports the countably-separated
  definition used in the prose.
- Omit the Andre book sample when Stacks Tag `0B1W` is used.
- Omit the Tao, Encyclopedia of Mathematics, and Chao Li web cross-checks
  when the retained primary/authoritative source already owns the claim.
- Do not cite controls, source manifests, proof audits, or Route audits as
  scholarly evidence.  They belong in reproducibility/data-availability
  statements with immutable repository paths and hashes.

## 4. Claim--citation ownership rules for drafting

1. Paper 9 is the only prior-paper owner of the actual indiscreteness input.
   Cite it where that input is imported.  Deninger's source owns the arithmetic
   carrier/action/stabilizer description, not the indiscreteness proof.
2. P10-1--P10-8 and their universal-property specializations are Paper 10's
   proved results.  Background citations may define standard notions, but
   must not make those claims appear externally sourced.
3. Source-space, proxy-space, and copied/tagged-coproduct statements retain
   separate ownership.  A citation about one does not transfer a theorem to
   another.
4. Every claim imported from a source receives the exact manifestation and
   physical-page locator above.  When printed and physical pagination differ,
   state both.  When journal metadata and arXiv locators differ, state which
   bytes control the locator.
5. Split mixed sentences when one clause is source-owned and the next is
   Paper-10-derived.  Place the citation immediately after the owned clause.
6. Radon statements must name the convention before drawing a conclusion.
   Fremlin and Lipsman deliberately document different domains/conventions;
   neither citation may be presented as a unique universal definition.
7. Operator-topology citations apply only to norm/SOT/WOT on the declared
   common carrier.  They do not license a comparison between different
   carriers.
8. The bounded-search statement records a search result, not a theorem.  Its
   date, scope, and nearest neighbours must remain explicit.

## 5. Mandatory metadata/manifestation gates

These are release-blocking but not draft-blocking.

### M1 — companion Paper-9 identity

`Wang2026Packet` presently has an exact local PDF but no frozen public DOI,
preprint identifier, release tag, or immutable repository commit URL in the
audited source locks.  Drafting may use a clearly provisional key.  Before
BibTeX freeze, either:

- cite a public version with exact title, authors, date/version, and stable
  identifier; or
- use a transparent `@unpublished`/repository entry with an immutable public
  commit or release URL and the exact cited PDF/version.

A mutable branch URL or an invented publication status is not sufficient.

### M2 — Hernández title/version-family reconciliation

The retained arXiv record/manifest says *Epireflections in topological
algebraic structures*, while the PDF title page displays *Reflections in
Topological Algebraic Structures*.  Before BibTeX freeze, verify the DOI
landing metadata for `10.1016/j.topol.2020.107204` and record separately:

- the final published title/journal metadata; and
- the exact arXiv `1704.01146v2` manifestation used for physical-page
  locators.

Do not assemble a hybrid title from different manifestations.

### M3 — Fremlin development manifestations

The inspected Fremlin files are development/results-only chapter PDFs, not
unambiguously the paginated printed volumes.  The bibliography notes must
freeze the exact chapter, version date, canonical URL, and the fact that the
physical-page locators refer to those PDFs.  Printed-volume metadata may be
added for orientation only if it is kept distinct from the inspected bytes.

### M4 — unresolved optional metadata

- The Hofmann PDF cover/year text is inconsistent with the manifest's simple
  “Winter 2005” label.  Verify the exact cover metadata, or cite it neutrally
  as university-hosted course notes without asserting an academic year.
- The official publisher manifestation inspected for Lipsman did not expose a
  DOI.  Run one final publisher/Crossref DOI check at release.  If no DOI is
  found, retain the complete journal/pages/publisher URL and explicitly
  record “no DOI located”; never guess one.

Either source may instead be omitted when the final prose does not need it.

## 6. Public-sync exclusion contract

All third-party full texts are verification copies.  Public synchronization
must exclude, without exception:

```text
papers/10-separated-reflection/notes/sources/*.pdf
```

This covers all seven `scope-*` and five `dom-*` PDFs, including the Fremlin
files.  The Design Science License may permit conditional redistribution of
some Fremlin material, but this audit does not establish that a proposed
repository release satisfies its notices and conditions; exclusion is the
safe default.  A public endpoint alone is not redistribution permission.

If the release/sync root also includes inherited Paper-9 or Paper-8 source
directories, their local third-party PDFs must likewise remain excluded under
their own manifests.  Do not duplicate the inherited Deninger PDF into Paper
10.

Safe-to-sync metadata consists of the source manifests, checksum ledgers,
preflight JSON sidecars, canonical URLs, page locators, hashes, and audit
reports.  Immediately before sync, use an explicit allowlist or a staged-file
audit; do not assume an ignore rule exists.  The release gate is zero matched
`notes/sources/*.pdf` files in the tracked/staged/public payload.  Checksum the
local verification corpus first, then exclude the PDF bytes.

## 7. Exact final citation and release checks

The citation-integrity gate is complete only when all of the following pass
on the final candidate bytes:

1. Freeze and report SHA-256 hashes for `manuscript.tex`, `references.bib`,
   every generated figure/table artifact, and the final PDF.
2. Rebuild from a clean auxiliary state.  Require zero undefined citations,
   zero undefined references, zero duplicate BibTeX keys, and no missing
   bibliography fields reported by the selected style/toolchain.
3. Compare the set of in-text citation keys with the BibTeX keys: zero missing
   keys and zero orphan entries.  Rendered references must be visually
   inspected for truncation, malformed URLs/DOIs, and title loss.
4. Validate every DOI and canonical URL against the cited work.  Normalize DOI
   fields, preserve arXiv version suffixes, do not guess identifiers, and
   close M1--M4.
5. Re-run both source checksum ledgers and verify every cited local locator
   against its `PASS` preflight sidecar, PDF hash, and physical page.  Declare
   any physical/printed pagination split and any journal/arXiv split.
6. Build a claim--citation graph.  Every source-owned factual claim must map to
   one exact reference and locator; every P10 theorem claim must map to its
   internal theorem/proof; every mixed compound claim must be split or
   separately supported.
7. Verify that the manuscript never transfers credit or topology/measure
   conclusions among the source packet, proxy, and copied coproduct, and never
   uses a Radon convention without naming it.
8. If included, preserve the exact bounded-search date/scope wording and cite
   only the frozen nearest neighbours.  Do not make a priority claim.
9. Record the final controls-manifest hash and reproducibility command in the
   data/code availability statement, but do not use controls as a literature
   citation or infer empirical support beyond their declared semantics.
10. Run retraction/correction and final metadata checks for journal sources as
    of the release date.  Report the exact self-citation count; the companion
    Paper-9 citation must be justified by its load-bearing theorem role.
11. Perform a public-sync dry run and require zero third-party PDF/full-text
    bytes in the payload.  Confirm that repository-artifact links use an
    immutable commit or release rather than a mutable branch.
12. Verify final PDF metadata and the required availability, ethics/consent
    (as applicable), contribution, conflicts, funding, and AI-assistance
    disclosures; then perform a representative visual/layout audit and
    re-lock the PDF hash after the last change.

## 8. Decision summary

- Critical source/citation blockers: **0**.
- Draft-blocking findings: **0**.
- Mandatory pre-Bib/pre-release gates: **M1--M4**.
- Authorized source expansion: **none**; only final metadata verification for
  the already frozen works is required.
- Final disposition: **PASS TO DRAFTING / CONDITIONAL RELEASE**.
