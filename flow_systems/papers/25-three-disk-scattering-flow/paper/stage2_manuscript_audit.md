# Paper 25 — ARS Stage 2 manuscript audit

Date: **2026-08-28**

Status: **ARS Stage 2 draft complete; Stage 2.5 awaiting user confirmation.**
This report does not claim Stage 2.5 approval, peer-review acceptance, a
physical determinant, or any Route-A promotion.

## Deliverables and integrity

| File | SHA-256 |
|---|---|
| manuscript.tex | 283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb |
| references.bib | acec840393408f146f5e6eed9723cd4e12275108a6059fe0fdb0c2bc508e7248 |
| paper.pdf | 608b669835f55c02bf5e43c570878728865e8659a58dbd23dae02dbf16dd101f |

- PDF: **12 pages**, 303,170 bytes, PDF 1.5.
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
| English body word count | **4,055** by tools/round9_manuscript_audit.py |
| English abstract | **209 visible words** by `detex`; within 150–300 |
| Traditional-Chinese abstract | **351 Han characters** excluding heading/keywords; within 300–500 |
| Keywords | **7 English; 7 Traditional Chinese** |
| Bibliography | **8 entries; 8 cited; 0 missing; 0 orphaned** |
| Citation calls | **10**, each with a natbib optional locator |
| Source comments | **10** adjacent SOURCE comments |
| Structure | Introduction; related work/background and object typing; main theorems and complete proofs; computational/certificate method; adversarial/Route-A interpretation; limitations; conclusion |
| Declarations | Funding; Conflict of Interest; CRediT-style contributions; Data and Code Availability; Ethics Statement; AI-Assisted Research Disclosure |

The root structural audit recognizes every required manuscript surface. Author,
affiliation, postal address, email, no-funding statement, and no-conflict
statement match the frozen metadata.

## Claim-boundary audit

- Exact physical witnesses are unchanged:
  \(T_2/2=d-2a\), \(T_3/3=d-\sqrt3a\), and the positive mean gap is
  \((2-\sqrt3)a\).
- The unequal periodic means prove only the necessary noncohomology result and
  the impossibility of an owner- and repetition-preserving scalar substitution
  \(z=e^{-cs}\). The minimax mean-roof error is bounded below by half the gap.
- The locked replay is reported as **2,241 rows**: 747 owners at each of
  \(d/a=29/5,6,31/5\); per geometry, 3 period-two matches and 744
  disagreements.
- The unit-roof \(q\)-symbol determinant theorem and the universal
  two-dimensional half-density theorem remain assigned only to their typed
  symbolic/stability objects.
- The symbolic tuple remains
  \((A0_{\rm fail},A1_{\rm pass\ analytic},A2_{\rm analytic\ determinant},
  A3_{\rm fail},A4_{\rm fail})\), overall Route-A rejected.
- The physical three-disk flow remains unassigned. No nonconstant-roof
  physical determinant, exact quantum determinant equality, arithmetic source,
  resonance fit, prime/zero target, Route-B operator, or spectral realization
  is claimed.

## Citation existence and support audit

All sources were checked on 2026-08-28 using original-paper, publisher,
society, journal archive, or DOI metadata. Every in-text citation includes a
locator and adjacent source comment.

| Key | Existence check | Manuscript locator and supported use |
|---|---|---|
| GaspardRice1989Semiclassical | JCP, DOI [10.1063/1.456018](https://doi.org/10.1063/1.456018) | Sections II–IV: semiclassical periodic-orbit construction for the chaotic repellor |
| GaspardRice1989Exact | JCP, DOI [10.1063/1.456019](https://doi.org/10.1063/1.456019) | Abstract and Sections II–III: exact three-hard-disk multiple-scattering matrix/determinant |
| Wirzba1999 | Physics Reports, DOI [10.1016/S0370-1573(98)00036-2](https://doi.org/10.1016/S0370-1573(98)00036-2) | Sections 2–6: symbolic/classical/semiclassical/exact distinctions and multiscattering determinant |
| Ikawa1988 | Numdam/Annales de l'Institut Fourier, DOI [10.5802/aif.1137](https://doi.org/10.5802/aif.1137) | Introduction and theorem statements: periodic rays and Poincaré maps in exterior convex-body scattering |
| BowenLanford1970 | AMS PSPM, DOI [10.1090/pspum/014/9985](https://doi.org/10.1090/pspum/014/9985) | Pages 43–49: finite-type shift zeta and adjacency-determinant framework |
| Ruelle1976 | Inventiones, DOI [10.1007/BF01403069](https://doi.org/10.1007/BF01403069) | Sections 1–3: zeta functions for expanding maps and flows; timing/weight context |
| CvitanovicEckhardt1989 | Physical Review Letters, DOI [10.1103/PhysRevLett.63.823](https://doi.org/10.1103/PhysRevLett.63.823) | Pages 823–826: periodic-orbit quantization and cycle-expansion context |
| Livsic1972 | Math. USSR-Izvestiya, DOI [10.1070/IM1972v006n06ABEH001919](https://doi.org/10.1070/IM1972v006n06ABEH001919) | Main cohomology criteria: periodic-orbit obstruction context; manuscript uses only the elementary necessary direction |

Claim-support result: **PASS**. Citation existence result: **PASS**. Missing-key
check: **PASS**. Orphan-entry check: **PASS**. Locator/comment coverage:
**10/10 PASS**.

## Reproduction and tests

Executed from papers/25-three-disk-scattering-flow with
PYTHONDONTWRITEBYTECODE=1:

    python3 -m unittest discover -s code -p 'test_*.py' -v
    Ran 65 tests in 10.370s — OK

    bash experiments/reproduce_round8.sh verify
    Round-8 tests: 12/12 — OK
    Existing artifacts VERIFIED
    core_sha256 =
    9a29d8894b1ac81f9588fe221375bddc671898b9b08b409b0fa5a1d5a42a9014
    physical_replay_rows = 2241

The reproducer generated two isolated temporary builds, compared them
byte-for-byte, and verified committed evidence without refreshing it. No
__pycache__ directory or .pyc file remains.

## Explicit limitations

The nontransfer theorem excludes only a constant scalar roof, not a genuine
nonconstant-roof transfer operator. The physical ledger is finite through
symbolic length 12; general solved orbits are high-precision numerical
certificates rather than interval proofs; the half-density theorem is local;
and the exact quantum multiple-scattering determinant is not identified with
the symbolic determinant. No arithmetic source is assigned by construction.

## Independent review and patch disposition

An independent read-only reviewer found no Blocker or Major issue and two
Minor wording/scope issues. The abstract now reports 2,241 rows across the
three geometries (747 per geometry), and all full-shift physical-roof claims
now state the no-eclipse hypothesis `d>4a/sqrt(3)`. The Traditional-Chinese
abstract carries the same scope. The post-patch four-pass build and structural
audit are clean; theorem values, frozen ledgers, and Route-A verdicts are
unchanged.

**Audit conclusion:** Stage 2 draft deliverables are complete and internally
reproducible. **Stage 2.5 remains awaiting user confirmation.**
