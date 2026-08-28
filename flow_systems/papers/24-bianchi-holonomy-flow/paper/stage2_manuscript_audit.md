# Paper 24 — ARS Stage 2 manuscript audit

Date: **2026-08-28**

Status: **ARS Stage 2 draft complete; Stage 2.5 awaiting user confirmation.**
This report does not claim Stage 2.5 approval, peer-review acceptance, or any
Route-A promotion.

## Deliverables and integrity

| File | SHA-256 |
|---|---|
| manuscript.tex | e43ba0f77332b79df4d84346dcb6e3041c20f4bdded5a91f42caac348ea9fd11 |
| references.bib | 11e7dd42f07ecf22744f5d9c829d13a22212e0d43cb2591c0e9dfd66bde86d87 |
| paper.pdf | e8dcfa74b967054a956521daa138a4cb397292c13674c19e1c03e218438759f1 |

- PDF: **12 pages**, 305,232 bytes, PDF 1.5.
- The generated, Git-ignored `paper.log` was checked after the final build.
- Engine chain: LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX.
- Bibliography mode: natbib with plainnat, numeric citations.
- Final log scan: no undefined citations, undefined references, missing
  characters, overfull boxes, underfull boxes, or LaTeX warnings.
- Visual inspection: title/author block, English abstract, independent
  Traditional-Chinese abstract, equations, typography, and page breaks were
  inspected from rendered PDF pages.

## Length and required surfaces

| Check | Result |
|---|---|
| English body word count | **4,029** by tools/round9_manuscript_audit.py |
| English abstract | **210 words** by token audit; within 150–300 |
| Traditional-Chinese abstract | **317 Han characters** excluding heading/keywords; within 300–500 |
| Keywords | **7 English; 7 Traditional Chinese** |
| Bibliography | **7 entries; 7 cited; 0 missing; 0 orphaned** |
| Citation calls | **9**, each with a natbib optional locator |
| Source comments | **9** adjacent SOURCE comments |
| Structure | Introduction; setting; related work; theorems and complete proofs; exact certificate; adversarial/Route-A interpretation; limitations; conclusion |
| Declarations | Funding; Conflict of Interest; CRediT-style contributions; Data and Code Availability; Ethics Statement; AI-Assisted Research Disclosure |

The root structural audit recognizes every required manuscript surface. Author,
affiliation, postal address, email, no-funding statement, and no-conflict
statement match the frozen metadata.

## Claim-boundary audit

- The central theorem is stated and proved exactly for a commutative ring
  \(R\), a non-zero-divisor \(m\), and \(\gamma=I+mA\in\mathrm{SL}_2(R)\):
  \((\operatorname{tr}(\gamma)^2-4)/m^2
  =m^2\det(A)^2-4\det(A)\).
- The first jet is proved invariant under level-subgroup conjugacy, negated by
  inversion, and multiplied by the repetition number under powers.
- The finite panel is reported as **11,481 exact matrices**, not a complete
  Bianchi conjugacy or primitive-orbit census.
- Frozen collision counts are unchanged: 145 to 517 descriptors,
  372 of 11,336 scalar-collision rows separated, 10,964 remaining,
  maximum bucket 505 to 84, and zero singleton joint buckets.
- The control ledger reports 6,396 witnesses and 6,392 principal-congruence
  rows, while retaining the **2-of-3 canonical control-type gate** as
  incomplete.
- The manuscript stops \(D_9\) as a Gaussian-specific owner mechanism, retains
  the universal theorem and first-jet refinement, and leaves the full flow
  unassigned.
- No prime table, zeta-zero table, resonance target, target-derived statistic,
  orbit-to-prime-ideal map, metric prefix, Route-B operator, or spectral
  realization is claimed.

## Citation existence and support audit

All sources were checked on 2026-08-28 using publisher, society, official
documentation, or DOI metadata. Every in-text citation includes a locator and
an adjacent source comment. Technical claims rely on original papers,
authoritative monographs, or official documentation.

| Key | Existence check | Manuscript locator and supported use |
|---|---|---|
| MaclachlanReid2003 | Springer book, DOI [10.1007/978-1-4757-6720-9](https://doi.org/10.1007/978-1-4757-6720-9) | Chapters 10–11: arithmetic Kleinian and Bianchi setting |
| PfaffRaimbault2020 | AMS, DOI [10.1090/tran/7875](https://doi.org/10.1090/tran/7875) | Introduction and Section 2: Bianchi congruence subgroups/towers and torsion context |
| Pfaff2015 | De Gruyter, DOI [10.1515/crelle-2013-0047](https://doi.org/10.1515/crelle-2013-0047) | Abstract and Sections 3–5: finite-volume Selberg-zeta analytic apparatus |
| LinLipnowski2022 | AMS, DOI [10.1090/jams/982](https://doi.org/10.1090/jams/982) | Introduction and Section 2: complex length and holonomy-trace context |
| HIKMOT2016 | Taylor & Francis, DOI [10.1080/10586458.2015.1029599](https://doi.org/10.1080/10586458.2015.1029599) | Theorem 5.1 and Sections 3–5: interval verification of cusped hyperbolic structures |
| SnapPyDocs2026 | [Official SnapPy 3.3.2 documentation](https://snappy.computop.org/) | Verified-computation and verify_hyperbolicity semantics |
| Reid1991 | JLMS, DOI [10.1112/jlms/s2-43.1.171](https://doi.org/10.1112/jlms/s2-43.1.171) | Main theorem: arithmeticity classification used for the contextual knot-complement control |

Claim-support result: **PASS**. Citation existence result: **PASS**. Missing-key
check: **PASS**. Orphan-entry check: **PASS**. Locator/comment coverage:
**9/9 PASS**.

## Reproduction and tests

Executed from papers/24-bianchi-holonomy-flow with
PYTHONDONTWRITEBYTECODE=1:

    python3 -m unittest discover -s code -p 'test_*.py' -v
    Ran 71 tests in 73.909s — OK

    bash experiments/reproduce_round8.sh
    Round-8 tests: 14/14 — OK
    Existing artifacts VERIFIED
    primary_sha256 =
    cacf5b84d9faecdca1cdfc5e0082cbf21cf491fbfe75835d41919d4c9c5f54f3

The reproducer's two REFRESHED messages refer only to isolated temporary output
roots used for deterministic comparison; the final repository action was
verify-only and committed evidence was not refreshed. No __pycache__ directory
or .pyc file remains.

## Explicit limitations

The elementary word ball is not full-group or conjugacy complete; word length
is not geometric length; the signed first jet is not invariant under all
ambient conjugations; the mandatory control-type gate is incomplete; and no
ideal-valued owner map or dynamical determinant has been built. These are
manuscript-level limitations, not deferred footnotes.

## Independent review and patch disposition

An independent read-only reviewer found no Blocker or Major issue and one
Minor scope omission: the first-jet definition did not repeat the
non-zero-divisor hypothesis needed to make `A=(gamma-I)/m` unique. The
definition and first-jet theorem now state that hypothesis explicitly. The
post-patch four-pass build is clean, the structural audit passes with no
warning, and the frozen research artifacts and Route-A `2/3` control gate are
unchanged.

**Audit conclusion:** Stage 2 draft deliverables are complete and internally
reproducible. **Stage 2.5 remains awaiting user confirmation.**
