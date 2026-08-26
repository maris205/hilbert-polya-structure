# Paper 12 continuous-cohomology source manifest

Manifest date and source cutoff: **2026-08-15**  
Scope: exact primary/authoritative framework and packet-owner sources only  
Audit status tuple: protocol `9213d6e27505c09dbfc24899a15dcca9670e897e754fe40efbc9c1ae7248f434`; candidate `f0878aaf97e44041460b05c59acd5b5a45fd6d1bef2d7042e3ad273de5320d1c`; pipeline `9a3c2dbf85a4f2f9a8ebe82a6b8ad82b79379bb7bd5245bbe03e9a39a2200e05`

## 1. Integrity protocol

Each retained PDF came from a versioned arXiv endpoint or the official
publisher endpoint listed below. Each was checked with the unmodified ARS
`pdf_read_preflight.py` script using `pypdf` in an isolated environment. An
initial dependency-missing run was `UNAVAILABLE` and was not counted as
validation; the retained sidecars are the subsequent successful runs. Every
final sidecar reports schema `pdf_read_preflight/1`, tool
`pdf_read_preflight/1.0.0`, verdict `PASS`, equality of declared, enumerated,
and reader page counts, and an empty warnings list.

The physical page is the one-based PDF page index. “Printed” means the page
number visibly printed in the source; when an arXiv manuscript numbers its
own pages, that author page number is reported instead. SHA-256 is a local
reproducibility locator, not a scholarly identifier.

## 2. Retained manifestation ledger

| ID | Retained PDF | Bytes | SHA-256 | Pages / preflight | Sidecar SHA-256 |
|---|---|---:|---|---|---|
| `COH-DEN-v4` | `coh-deninger-dynamical-arithmetic-schemes-v4.pdf` | 1,144,247 | `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09` | 119 / `119=119=119`, `PASS`, no warnings | `84e43728af040d539a46fbbb95ff8cd34f46c75c0245130ef79c2978ccc3806d` |
| `COH-MACK-1978` | `coh-mackenzie-rigid-topological-groupoids-1978.pdf` | 1,080,192 | `b94ed23e24a13047037dbffc5c84513df1cd8931c4391670e05c1f5904f66f83` | 25 / `25=25=25`, `PASS`, no warnings | `8716b0e77a254642f1aae2a9dd75e84e30722711548abb26fa7335a59a0692c2` |
| `COH-BUW-2023` | `coh-blanco-uribe-waldorf-pontrjagin-gerbes-2023.pdf` | 548,010 | `3d46127491c66f3ec0568fccb8df60b9e4465c4f4719b712fc3e23ca48f9e143` | 52 / `52=52=52`, `PASS`, no warnings | `ae2272eed854f175d2d5bec4c624806c826bf9f364d2f4c27e230ede38ea6e42` |
| `COH-FHKP-2022` | `coh-farsi-huang-kumjian-packer-cocycles-2022.pdf` | 469,714 | `194583c289d3c08463a32221a8e6561292d48d5357021db370237c71de697083` | 32 / `32=32=32`, `PASS`, no warnings | `908dea03b5b4523764249a6749e50ae696c0f342a21fe5522c22c1b962a0cb3b` |
| `COH-FW-v2` | `coh-fuchssteiner-wockel-loop-contractible-arxiv-v2.pdf` | 187,771 | `194483f7c90cb752b95f86b2557572bb8deb135032b749503347d7592d752f42` | 13 / `13=13=13`, `PASS`, no warnings | `20303cd7044682edf01aaad44ba2cfd8f90c8694cc8e4eb61241f1640d625acc` |

The corresponding sidecars use the same basename with
`.preflight.json`. The executable verification ledger is
`coh-sources.sha256`; from this directory run:

```bash
sha256sum -c coh-sources.sha256
```

## 3. Source records and exact locators

### 3.1 `COH-DEN-v4`

Bibliographic manifestation:

- Christopher Deninger, *Dynamical systems for arithmetic schemes*.
- arXiv `1807.06400v4`, version stamp 7 February 2024.
- Official record: <https://arxiv.org/abs/1807.06400v4>
- Exact PDF endpoint: <https://arxiv.org/pdf/1807.06400v4>

Locator map and permitted use:

| Physical / printed page | Exact content used |
|---|---|
| 1 / 1 | embedded identifier `arXiv:1807.06400v4 [math.DS] 7 Feb 2024` |
| 32 / 32, Eqs. (35), (38) | finite-kernel exponent exhaustion and an equivariant **set** bijection |
| 33 / 33, Eq. (39) | equivalent set parametrization using `Q_{>0}/N(x_0)^Z` |
| 38 / 38, Section 6 | suspension, exact right `Q_{>0}` action, packet, right `R_{>0}` action, additive `phi^t([P,u])=[P,u e^t]` normalization, and `Gamma^E_{x_0}=Gamma_{x_0}` when `E_f` is contained in `E` |
| 39 / 39, Theorem 6.1 | every point in the packet has isotropy `N(x_0)^Z`; packet/finite-residue-field correspondence and orbit length `log N(x_0)` |

Permitted credit is packet/action/common stabilizer/clock. Eqs. (38)--(39)
and the p. 38 orbit description are not topology-transport theorems. The
source does not define the Paper-11/Paper-12 groupoid or cohomology.

Licence/release note: arXiv provides the official public manifestation, but
no project redistribution licence is inferred from access alone. The local
PDF remains an internal evidence cache and is excluded from public sync.

### 3.2 `COH-MACK-1978`

Bibliographic manifestation:

- K. A. Mackenzie, *Rigid cohomology of topological groupoids*.
- *Journal of the Australian Mathematical Society* (Series A) **26** (1978),
  277--301.
- DOI: <https://doi.org/10.1017/S1446788700011794>
- Official article record:
  <https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/rigid-cohomology-of-topological-groupoids/E6F26A7B330EB996D3D8AF982BA18DA5>
- Exact official PDF endpoint:
  <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E6F26A7B330EB996D3D8AF982BA18DA5/S1446788700011794a.pdf/div-class-title-rigid-cohomology-of-topological-groupoids-div.pdf>

Locator map and permitted use:

| Physical | Printed | Exact content used |
|---:|---:|---|
| 1 | 277 | abstract/domain: locally trivial, locally compact groupoids with vector-bundle coefficients |
| 3 | 279 | Definitions 1.3--1.4: Hausdorff transitive topological groupoid and local triviality |
| 4 | 280 | base is a paracompact connected `C^0` manifold; Definition 2.1 continuous vector bundle with Hausdorff locally convex fibres |
| 6 | 282 | Definition 3.1 continuous groupoid module |
| 9 | 285 | product bundle `B x R` with the trivial action is a continuous module |
| 14--15 | 290--291 | Definition 5.6 full continuous nonhomogeneous cochains on composable tuples and Eq. (5.7) differential |
| 25 | 301 | normalized cochains explicitly postponed to future work |

Permitted credit is a strict-domain groupoid/module comparator, a trivial
real-bundle example, and a full/unnormalized nonhomogeneous convention.
Mackenzie's Hausdorff/local-trivial/LCS hypotheses fail for the nontrivial
indiscrete Paper-12 owner and arbitrary `T0` coefficient group.

Licence/release note: the publisher record states copyright © Australian
Mathematical Society 1978 and does not display an open reuse licence. Local
retention is for verification only; no redistribution is authorized here.

### 3.3 `COH-BUW-2023`

Bibliographic manifestation:

- Jaider Blanco, Bernardo Uribe, and Konrad Waldorf, *Pontrjagin duality on
  multiplicative gerbes*.
- *Journal of Noncommutative Geometry* **17** (2023), no. 4, 1469--1520.
- DOI: <https://doi.org/10.4171/JNCG/528>
- Official article record: <https://ems.press/journals/jncg/articles/12586094>
- Exact final paginated PDF endpoint:
  <https://ems.press/content/serial-article-files/31062>

Locator map and permitted use:

| Physical | Printed | Exact content used |
|---:|---:|---|
| 1 | 1469 | final journal manifestation, DOI, pagination, and CC BY 4.0 statement |
| 4 | 1472 | `Topab`: compactly generated, locally contractible, Hausdorff topological abelian groups; continuous-map convention |
| 5--6 | 1473--1474 | §2.3 simplicial-paracompact double complex; full `Map(X_*,A)` cohomology of continuous cochains; Lemma 2.3 comparison when `A` is contractible or the simplicial space has the stated homotopy property |
| 6--7 | 1474--1475 | §2.4 one-object group nerve `G_p=G^p`, explicit full inhomogeneous differential, Definition 2.4, and Lemma 2.5 `H^1 ~= Hom_cont(G,A)` |

Permitted credit is the exact one-object `(R,R)` continuous-cochain and
Segal--Mitchison comparator, plus a conditional simplicial-space comparator
after every nerve-level hypothesis is proved. It does not establish a named
all-degree topological-groupoid theory for arbitrary `T0` coefficients.

Licence/release note: the official PDF and publisher record state
**CC BY 4.0**. The project nevertheless keeps this retained source PDF out of
the public supplement under its stricter source-byte policy.

### 3.4 `COH-FHKP-2022`

Bibliographic manifestation:

- Carla Farsi, Leonard Huang, Alex Kumjian, and Judith Packer, *Cocycles on
  groupoids arising from `N^k`-actions*.
- *Ergodic Theory and Dynamical Systems* **42** (2022), no. 11, 3325--3356;
  published online 18 October 2021.
- DOI: <https://doi.org/10.1017/etds.2021.69>
- Official article record:
  <https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/cocycles-on-groupoids-arising-from-mathbb-nk-actions/B70BFA05CEAB5475C63CAA49C539F323>
- Exact official PDF endpoint:
  <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B70BFA05CEAB5475C63CAA49C539F323/S0143385721000699a.pdf/cocycles-on-groupoids-arising-from-dollarmathbb-nkdollar-actions.pdf>

Locator map and permitted use:

| Physical | Printed | Exact content used |
|---:|---:|---|
| 1 | 3325 | final journal manifestation, DOI, pagination, and CC BY statement |
| 12 | 3336 | Definition 3.7: continuous `H`-valued groupoid 1-cocycles, unit-function coboundaries, and first continuous cocycle groupoid cohomology |

Definition 3.7 applies to a topological groupoid and a topological locally
compact abelian `H`, so `H=R` matches Paper 12 in degree one. Its coboundary
sign is `f(r gamma)-f(s gamma)`, opposite to Paper 12's frozen cochain-map
representative, but the two images are the same subgroup after `f |-> -f`.
No all-degree complex, arbitrary-`T0` coefficient theory, marked isotropy
image, or period quotient is imported.

Licence/release note: the official manifestation is **CC BY 4.0** (© the
authors, 2021; Cambridge publication). The retained PDF is still excluded
from the project supplement by policy.

### 3.5 `COH-FW-v2` and published crosswalk

Retained bibliographic manifestation:

- Martin Fuchssteiner and Christoph Wockel, *Topological Group Cohomology
  with Loop Contractible Coefficients*.
- arXiv `1110.2977v2`, version stamp 12 April 2012.
- Official arXiv record: <https://arxiv.org/abs/1110.2977v2>
- Exact PDF endpoint: <https://arxiv.org/pdf/1110.2977v2>

Published-manifestation crosswalk:

- *Topology and its Applications* **159** (2012), 2627--2634.
- DOI: <https://doi.org/10.1016/j.topol.2012.04.006>
- Official publisher record:
  <https://www.sciencedirect.com/science/article/pii/S0166864112001800>
- Author publication record: <https://www.math.uni-hamburg.de/home/wockel/>
- The arXiv API labels v2 “final version,” supplies that journal reference,
  and binds the same DOI. The author page independently lists the same title,
  coauthor, journal, volume, year, and pages and points to the arXiv version.

Locator map and permitted use for the retained v2 bytes:

| Physical / author page | Exact content used |
|---|---|
| 1 / 1 | embedded identifier `arXiv:1110.2977v2 [math.AT] 12 Apr 2012`; title/authors |
| 2--3 / 2--3 | topological group/module domain; full continuous standard complex; Definition I.1 and continuous homogeneous group cochains |
| 7 / 7 | Corollary II.8: continuous-to-locally-continuous cohomology isomorphism for loop-contractible coefficients |
| 8--9 / 8--9 | compactly generated variant and its hypotheses |

The PDF's dynamically rendered title date (17 April 2018) and metadata
creation date do not change the embedded arXiv v2 identifier/version stamp;
the exact retained byte hash above controls this manifestation. The publisher
PDF endpoint returned an access denial during this audit, so no publisher PDF
was retained and no claim of byte identity or published physical-page
crosswalk is made. The arXiv final-version content is used only as a
one-object continuous-group-cochain comparator.

Licence/release note: no open reuse licence is inferred for either the arXiv
or Elsevier manifestation. The retained arXiv PDF is local verification
evidence only.

## 4. Release and citation boundary

The source directory's existing `.gitignore` is:

```gitignore
*.pdf
!*.preflight.json
```

The current filesystem snapshot has no Git metadata, so `git check-ignore`
and an index audit are unavailable here. A later public-sync dry run must
enumerate the staged payload and show that it contains no `notes/sources/*.pdf`.
No retained source PDF is a manuscript attachment or public supplement.

Bibliography and prose citations must use the canonical arXiv, DOI, journal,
publisher, or author endpoints above. Local filenames, hashes, and preflight
sidecars are internal reproducibility data only. The checksum ledger covers
exactly the five retained PDFs and their five sidecars; it does not imply a
licence to redistribute any source.
