# Citation and novelty verification: period-three residues for an exceptional Hénon family

**Literature freeze:** 2026-08-16 UTC  
**Scope of this ledger:** bibliographic identity, publication status, claim-safe citation roles, and a bounded novelty search for
\[
f_{m,a}(x,y)=\bigl(y+(x^m-a)^2,x\bigr),\qquad m\ge 2,
\]
with special attention to the normalized quartic slice
\[
f_L(x,y)=\bigl(y+(x^2-L)^2,x\bigr).
\]

This is a source-control document, not a proof. Algebraic identities below are the author-proof-package claims whose literature collision was tested. Their theorem-level correctness is carried only by the bound proof and its fresh independent source review; any later computation is an implementation audit and cannot prove the all-\(m\) statements.

## 1. Citation-lock verdict

**Direct precedent exists for the family and for periods-one-and-two blindness.** Cantat–Dujardin exhibit
\[
(x,y)\longmapsto \bigl(y+(x^2-\lambda^2)^2,x\bigr)
\]
as a nontrivial Jacobian \(-1\) family having constant periodic data in periods 1 and 2. Thus the quartic curve itself, its reparametrization \(L=\lambda^2\), and the assertion that periods 1 and 2 fail to separate it are **not new**.

**No direct collision was located for the proposed period-three contribution.** Within the search coverage stated in §§7–8, no indexed paper or primary-source record was found that states any of the following:

1. the exact pointwise period-three second-trace sum
   \[
   S^{(3)}_2(L)=-1296000-1572864L^3
   =-384(3375+4096L^3);
   \]
2. the corresponding cyclewise sum
   \[
   -432000-524288L^3;
   \]
3. that this moment is an exact/minimal period-three separator on the **entire normalized quartic fiber whose formal fixed-point trace multiset is \(0^4\)**;
4. the all-\(m\) weighted-residue shape
   \[
   S_m(a,\epsilon)=C_m\epsilon^{3m}+D_ma^{2m-1}\epsilon^{2m},
   \qquad
   S_m(a)=C_m+D_ma^{2m-1},
   \]
   together with the bound proof-package candidate's exact finite coefficient
   certificate for \(D_m\).

This is a **bounded absence inference**, not proof that no earlier source exists. The defensible novelty claim is therefore narrow: an explicit Hénon-specific period-three trace-residue law and, in degree four, a full-fiber separation result. It is not the discovery of the family, the discovery of low-period blindness, the invention of global residues, or a general multiplier-rigidity theorem.

## 2. Evidence classes used below

| Class | Meaning | Consequence for the manuscript |
|---|---|---|
| **D — direct collision/precedent** | Same family or substantially the same claimed phenomenon. | State priority explicitly; do not claim novelty for the overlapped part. |
| **M — method prior art** | Supplies the algebraic/residue/sum-rule mechanism but not the proposed Hénon theorem. | Cite where the method is introduced; novelty must lie in the specialization, computation, or theorem. |
| **A — adjacent result** | Nearby moduli, multiplier, fixed-point, or low-period result in a different setting. | Use for context and boundaries; do not imply it proves the present claim. |
| **B — broad background** | General structural or dynamical setting. | Optional unless the associated fact is invoked. |

## 3. Verified source records and claim-safe roles

### 3.1 Cantat–Dujardin (2026) — **D: direct precedent**

**Verified record.** Serge Cantat and Romain Dujardin, “Multiplier rigidity for complex Hénon maps,” arXiv:2603.09445, version 1 submitted 10 March 2026, classifications math.DS and math.CV. Persistent arXiv DOI: [10.48550/arXiv.2603.09445](https://doi.org/10.48550/arXiv.2603.09445). Primary records: [arXiv abstract](https://arxiv.org/abs/2603.09445) and [arXiv HTML](https://arxiv.org/html/2603.09445v1).

**Status at the cutoff.** Preprint. The arXiv record contained no journal reference or publisher DOI at the freeze date. Cite it as an arXiv preprint, not as a published journal article. The source file displays a later internal manuscript date; that does not replace the arXiv version-history date.

**Claim-safe role.** This is the closest and mandatory citation. It establishes finite multiplier rigidity for complex Hénon maps, explains normalized generalized-Hénon forms and their residual root-of-unity ambiguity, and gives the exact quartic family above as a period-1/2 obstruction. Its Example 4.3 computes, for a Jacobian \(-1\) generalized Hénon map, fixed-point trace \(p'(x_0)\) and period-two trace \(p'(x_0)p'(y_0)+2\); taking \(p_\lambda=(x-\lambda)^2(x+\lambda)^2\) makes both spectra constant.

**What it directly takes off the novelty table.** The quartic family, its periods-1-and-2 blindness, and the observation that degree four is the first possible degree for this obstruction.

**What must not be attributed to it.** It does not state the explicit period-three moment above, a period-three separator for the whole quartic fiber whose formal fixed-point trace multiset is \(0^4\), the all-\(m\) two-term residue law, an explicit value \(P(4)=3\), or universal nonvanishing of \(D_m\). Its general Noetherian argument yields existence of a finite period bound, not the present scoped degree-four bound.

### 3.2 Friedland–Milnor (1989) — **B/M: structural normal form and conjugacy**

**Verified record.** Shmuel Friedland and John Milnor, “Dynamical properties of plane polynomial automorphisms,” *Ergodic Theory and Dynamical Systems* **9**(1) (March 1989), 67–99. DOI: [10.1017/S014338570000482X](https://doi.org/10.1017/S014338570000482X). Primary [Cambridge journal record](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/dynamical-properties-of-plane-polynomial-automorphisms/43661938D1C6688699C178D0B47B97C0).

**Status.** Peer-reviewed journal article.

**Claim-safe role.** Cite for the structural classification and normal forms of polynomial automorphisms of the plane, including generalized Hénon maps and the conjugacy framework underlying normalized polynomial parameters. Cantat–Dujardin also invoke Friedland–Milnor for the special low-degree fixed-trace determination in degrees 2 and 3.

**Boundary.** The proposed equivalence \(f_{m,a}\sim f_{m,b}\iff a^{2m-1}=b^{2m-1}\) should be presented as an explicit specialization proved in the manuscript, with Friedland–Milnor cited for the ambient normal-form/conjugacy theory. Do not attribute the period-three residue formula, the quartic fiber theorem, or a degree-four period bound to this paper.

### 3.3 Cattani–Dickenstein–Sturmfels (1996) — **M: global-residue method prior art**

**Verified record.** Eduardo Cattani, Alicia Dickenstein, and Bernd Sturmfels, “Computing Multidimensional Residues,” in *Algorithms in Algebraic Geometry and Applications*, ed. L. González-Vega and T. Recio, Progress in Mathematics **143**, Birkhäuser, Basel, 1996, 135–164. DOI: [10.1007/978-3-0348-9104-2_8](https://doi.org/10.1007/978-3-0348-9104-2_8). Preprint: arXiv:alg-geom/9404011, submitted 27 April 1994 ([arXiv record](https://arxiv.org/abs/alg-geom/9404011)). The [Springer volume record](https://link.springer.com/book/10.1007/978-3-0348-9104-2) confirms the chapter title and pages.

**Status.** Published book chapter; cite the 1996 chapter, optionally appending the arXiv identifier for access and priority.

**Claim-safe role.** Mandatory if the proof uses a global residue, a quotient-algebra trace, a weighted deformation, or extraction of a top normal-form coefficient. The paper explicitly develops multidimensional/global residues as rational functions of coefficients and trace formulas over zero-dimensional complete intersections.

**Boundary.** The multidimensional residue machinery and trace-to-coefficient mechanism are not new. The proposed contribution can only be the Hénon-specific setup, exact reduction, coefficient evaluation, and resulting separation statement. This source does not contain the present family or its period-three formula.

### 3.4 Cvitanović–Hansen–Rolf–Vattay (1998) — **M/A: exact Hénon periodic-orbit sum rules**

**Verified record.** Predrag Cvitanović, Kim Hansen, Juri Rolf, and Gábor Vattay, “Beyond the periodic orbit theory,” *Nonlinearity* **11**(5) (1998), 1209–1232. DOI: [10.1088/0951-7715/11/5/003](https://doi.org/10.1088/0951-7715/11/5/003). Preprint: arXiv:chao-dyn/9712002, submitted 2 December 1997 ([arXiv record](https://arxiv.org/abs/chao-dyn/9712002)); an [author-hosted article PDF](https://cns.gatech.edu/~predrag/papers/contourNonl.pdf) is also available.

**Status.** Peer-reviewed journal article.

**Claim-safe role.** Cite when positioning exact periodic-orbit identities and sum rules for area-preserving Hénon dynamics. This paper is important evidence that exact Hénon orbit sums and Fredholm/analyticity-based relations are established prior art.

**Boundary.** Its orbit sums use stability denominators/Fredholm-determinant structures and are not the proposed finite algebraic second power sum of traces on the exceptional quartic fiber. It does not classify that fiber or give the claimed \(L^3\)-affine period-three separator. Do not call “exact Hénon sum rules” new without this qualification.

### 3.5 Dullin–Meiss (2000) — **A: generalized-Hénon low-period background**

**Verified record.** Holger R. Dullin and James D. Meiss, “Generalized Hénon maps: the cubic diffeomorphisms of the plane,” *Physica D: Nonlinear Phenomena* **143**(1–4) (1 September 2000), 262–289. DOI: [10.1016/S0167-2789(00)00105-6](https://doi.org/10.1016/S0167-2789(00)00105-6). Primary [Elsevier record](https://www.sciencedirect.com/science/article/pii/S0167278900001056).

**Status.** Peer-reviewed journal article.

**Claim-safe role.** Background for low-period orbit and bifurcation analysis in area-preserving generalized Hénon maps, especially cubic maps and normal forms.

**Boundary.** It is not a source for the quartic exceptional family, a global-residue trace formula, or a full-fiber period-three separation theorem.

### 3.6 Huguin (2024) — **A: one-dimensional small-cycle multiplier moduli**

**Verified record.** Valentin Huguin, “Moduli spaces of polynomial maps and multipliers at small cycles,” arXiv:2412.19335, version 1 submitted 26 December 2024, 63 pages, classifications math.DS and math.AG. Persistent arXiv DOI: [10.48550/arXiv.2412.19335](https://doi.org/10.48550/arXiv.2412.19335). Primary records: [arXiv abstract](https://arxiv.org/abs/2412.19335) and [author publication page](https://www.vhuguin.com/).

**Status at the cutoff.** Preprint. No journal reference or publisher DOI was located on the arXiv or author record by 2026-08-16. Use the arXiv identifier; do not invent a journal venue. The current manuscript PDF is available from the author as [MPolyMult.pdf](https://vhuguin.com/publications/MPolyMult.pdf).

**Claim-safe role.** Cite for the result that, for one-variable degree-\(d\) polynomial maps modulo affine conjugacy, the period-1-and-2 multiplier morphism is finite and birational onto its image, and for its discussion of small-cycle isospectral phenomena (including quartic one-variable polynomial pairs in its appendix).

**Boundary.** This is a result for one-dimensional polynomial moduli, not for Jacobian \(-1\) polynomial automorphisms of \(\mathbb C^2\). It cannot support a claim that periods 1 and 2 determine the present Hénon family; Cantat–Dujardin give precisely the contrary exceptional family. It contains neither the proposed period-three moment nor the quartic Hénon fiber classification.

### 3.7 Hutz (2010) — **A: formal-period/dynatomic-cycle background**

**Verified record.** Benjamin Hutz, “Dynatomic cycles for morphisms of projective varieties,” *New York Journal of Mathematics* **16** (2010), 125–159. Primary [journal article PDF](https://nyjm.albany.edu/j/2010/16-8p.pdf). Preprint: arXiv:0801.3643 ([arXiv record](https://arxiv.org/abs/0801.3643)).

**Status.** Peer-reviewed journal article. No DOI was found in the journal or arXiv metadata; cite the stable journal URL and arXiv identifier rather than supplying a guessed DOI.

**Claim-safe role.** Cite if the manuscript discusses formal periodic points, exact versus formal period, dynatomic multiplicities, or effectivity/degree of dynatomic cycles for morphisms of projective varieties.

**Boundary.** It is not a Hénon multiplier-spectrum or residue-separation result. Also do not confuse arXiv:0801.3643 with Hutz's separate good-reduction paper arXiv:0801.3645.

### 3.8 Hutz (2020) — **A: higher-dimensional projective multiplier invariants**

**Verified record.** Benjamin Hutz, “Multipliers and invariants of endomorphisms of projective space in dimension greater than 1,” *Journal de Théorie des Nombres de Bordeaux* **32**(2) (2020), 439–469. DOI: [10.5802/jtnb.1129](https://doi.org/10.5802/jtnb.1129). Preprint: arXiv:1908.03184. Primary [Centre Mersenne record](https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.1129/).

**Status.** Peer-reviewed journal article.

**Claim-safe role.** Background for conjugacy invariants built from multiplier matrices of periodic points on moduli of projective endomorphisms and for the existence of isospectral families in higher-dimensional projective dynamics.

**Boundary.** Polynomial Hénon automorphisms compactify birationally and have indeterminacy; they are not regular endomorphisms of projective space. This paper therefore supplies analogy and terminology, not the present trace formulas or a theorem directly applicable to the family.

### 3.9 Guillot–Ramírez (2019) — **M/A: fixed-point multiplier relations**

**Verified record.** Adolfo Guillot and Valente Ramírez, “On the Multipliers at Fixed Points of Quadratic Self-Maps of the Projective Plane with an Invariant Line,” *Computational Methods and Function Theory* **19**(4) (2019), 687–716. DOI: [10.1007/s40315-019-00293-w](https://doi.org/10.1007/s40315-019-00293-w). Preprint: arXiv:1902.04433, originally posted under the broader title “On the multipliers at fixed points of self-maps of the projective plane” ([arXiv record](https://arxiv.org/abs/1902.04433)); the publication is also listed on [Ramírez's author record](https://valentermz.github.io/cv/).

**Status.** Peer-reviewed journal article. Use the published title in the bibliography; the arXiv title differs.

**Claim-safe role.** Cite for algebraic relations among fixed-point multipliers obtained from index/Lefschetz-type formulas and for generic reconstruction phenomena for quadratic self-maps of \(\mathbb P^2\) preserving a line.

**Boundary.** It treats projective-plane self-maps with an invariant line, not polynomial Hénon automorphisms or their period-three fiber. It does not imply the proposed formulas.

### 3.10 Ueda (2004) — **B/A: fixed points of polynomial automorphisms**

**Verified record.** Tetsuo Ueda, “Fixed points of polynomial automorphisms of \(\mathbb C^n\),” in *Complex Analysis in Several Variables—Memorial Conference of Kiyoshi Oka's Centennial Birthday*, Advanced Studies in Pure Mathematics **42**, Mathematical Society of Japan, Tokyo, 2004, 319–324. DOI: [10.2969/aspm/04210319](https://doi.org/10.2969/aspm/04210319); the DOI resolves to the [Project Euclid record](https://projecteuclid.org/euclid.aspm/1546542864).

**Status.** Published conference-volume chapter.

**Claim-safe role.** Background for fixed-point questions and index identities for polynomial automorphisms of affine complex space.

**Boundary.** This exact title must not be conflated with Ueda's other work on fixed-point formulas for projective maps. It is not a source for a period-three trace moment, multiplier-moduli separation, or the claimed all-\(m\) residue law.

### 3.11 Bianchi–He (2026) — **B: current frontier, optional**

**Verified record.** Fabrizio Bianchi and Yan Mary He, “A thermodynamic path metric for complex Hénon maps,” arXiv:2606.29363, version 1 submitted 28 June 2026, classifications math.DS and math.CV. Persistent arXiv DOI: [10.48550/arXiv.2606.29363](https://doi.org/10.48550/arXiv.2606.29363). Primary [arXiv record](https://arxiv.org/abs/2606.29363).

**Status at the cutoff.** Preprint; no journal reference or publisher DOI was present on the arXiv record.

**Claim-safe role.** Optional current-context citation for thermodynamic/covariance geometry on hyperbolic components of complex Hénon maps and its use of unstable derivative cocycles and Cantat–Dujardin-type rigidity.

**Boundary.** Its unstable-multiplier thermodynamic metric is not a finite algebraic trace-power sum over all formal period-three points. It is not a direct collision and is unnecessary in a minimal algebraic proof bibliography.

## 4. Direct-collision map

| Proposed manuscript component | Closest located source | Collision assessment | Safe positioning |
|---|---|---|---|
| The curve \(p_L(x)=(x^2-L)^2\) | Cantat–Dujardin, with \(L=\lambda^2\) | **Direct; already present** | “Following the exceptional family exhibited by Cantat–Dujardin…” |
| Fixed trace multiset \(0^4\) and period-two trace multiset \(2^{12}\) | Cantat–Dujardin Example 4.3 | **Direct; already present in substance** | Re-derive for self-containment, but credit the example and do not label it new. |
| Full normalized quartic fiber with formal fixed-point trace multiset \(0^4\) is \(p_L=(x^2-L)^2\) | No direct statement located | **No direct collision located; likely elementary refinement** | State as a proposition proved by coefficient comparison; avoid overselling. |
| Exact period-three moment \(-1296000-1572864L^3\) | None located | **No direct collision located** | Present as the principal explicit computation, subject to independent verification. |
| Period three is the exact minimal separator on that full fiber | Cantat–Dujardin gives only failure through period 2 and general finite determination | **No direct collision located for the upper bound/minimality pair** | Claim only for this normalized fiber, combining known lower bound with the proved period-three upper bound. |
| All-\(m\) two-term weighted law and coefficient certificate | Cattani–Dickenstein–Sturmfels supplies method only | **No direct collision located; method is prior art** | Call the family-specific weighted computation new, not the residue formalism. |
| \(f_{m,a}\sim f_{m,b}\iff a^{2m-1}=b^{2m-1}\) | Friedland–Milnor/Cantat–Dujardin normal-form framework | **Likely specialization, not broad novelty** | Prove explicitly and cite structural normal forms; use as setup rather than headline novelty. |

## 5. Method and background boundaries

The literature supports the following disciplined division of labor:

- **Normal form and conjugacy:** Friedland–Milnor, sharpened in the modern rigidity setting by Cantat–Dujardin.
- **Existing direct obstruction:** Cantat–Dujardin's quartic family and constant period-1/2 data.
- **Global residue and quotient trace:** Cattani–Dickenstein–Sturmfels.
- **Exact Hénon orbit sum rules:** Cvitanović–Hansen–Rolf–Vattay.
- **Generalized-Hénon low-period dynamics:** Dullin–Meiss.
- **Small-cycle multiplier maps in one variable:** Huguin.
- **Formal periods and projective multiplier invariants:** Hutz (2010, 2020).
- **Index-derived fixed-point relations in dimension two:** Guillot–Ramírez and, for polynomial automorphisms, Ueda.
- **Current unstable-multiplier/thermodynamic direction:** Bianchi–He.

Accordingly, phrases such as “we introduce a residue formula for periodic points,” “the first exact Hénon sum rule,” or “the first multiplier rigidity result for Hénon maps” are not claim-safe. A defensible sentence is:

> Building on the period-1/2 exceptional quartic family identified by Cantat and Dujardin and on classical global-residue trace methods, we compute a period-three trace-power moment explicitly and prove that it separates the entire normalized quartic fiber whose formal fixed-point trace multiset is \(0^4\).

If the uniform \(m\)-statement is retained, add:

> For the even-degree family \(p_{m,a}(x)=(x^m-a)^2\), weighted homogeneity reduces the analogous period-three moment to two possible parameter monomials and yields an explicit finite coefficient certificate; no universal nonvanishing assertion is made.

## 6. Novelty positioning by claim

| Candidate claim | Novelty confidence after search | Citation/wording requirement |
|---|---:|---|
| Quartic family and period-1/2 blindness | **None** | Attribute directly to Cantat–Dujardin. |
| Classification of the normalized quartic fiber with formal fixed-point trace multiset \(0^4\) | **Moderate** | Prove fully; call it a useful exact fiber description, not a sweeping classification theorem. |
| Exact quartic period-three second trace moment | **Moderate–high, bounded** | Headline explicit result; report normalization and whether points or cycles are counted. |
| Exact/minimal separation at period 3 on that fiber | **Moderate–high, bounded** | Say “on this normalized fiber” every time; the lower bound \(>2\) is known from Cantat–Dujardin. |
| All-\(m\) two-term weighted form and finite coefficient certificate | **Moderate–high, bounded** | Credit global-residue machinery; separate the proved shape/certificate from the unproved nonvanishing conjecture. |
| Parity specialization \(C_m=0\) for odd \(m\) | **Moderate, bounded** | Present as a derived family-specific symmetry/weight consequence, not as a general residue theorem. |
| Universal \(D_m\ne0\), hence period-3 recovery for all \(m\) | **Not established** | Must be labeled conjectural/open or omitted from theorem claims. |
| General finite multiplier rigidity | **None** | Attribute to Cantat–Dujardin. |

“Moderate–high” here means that no direct collision appeared under the documented search, not that priority has been exhaustively certified.

## 7. Search protocol and recorded queries

The search was run in English over arXiv, publisher/DOI pages, author publication pages, and general scholarly web indexing. Exact-title and exact-formula searches were followed by source-page checks. Recent searches were bounded by the literature freeze above.

### 7.1 Direct quartic/fiber searches

- `2024 2025 2026 Hénon "(x^2-lambda^2)^2" "period 3" trace`
- `2024 2025 2026 quartic Hénon Jacobian -1 period three multiplier spectrum`
- `2024 2025 2026 Hénon "periodic data" "period 1 and 2" "period 3"`
- `2024 2025 2026 "Trace_3" Hénon multiplier rigidity`
- `"fixed-trace-zero" quartic Hénon`
- `"quartic" "Hénon" "period-three" multiplier`

**Result.** Cantat–Dujardin was the only direct family hit retained after source inspection. It covers the exact family up to \(L=\lambda^2\) and the period-1/2 obstruction, but not the searched period-three formulas or full-fiber theorem.

### 7.2 Uniform-family and residue searches

- `2024 2025 2026 Hénon "(x^m-a)^2" period three`
- `2024 2025 2026 even degree Hénon "global residue" periodic points trace`
- `2024 2025 2026 "period-three residue" Hénon`
- `2024 2025 2026 Hénon trace power sum multidimensional residue`
- `"Computing Multidimensional Residues" DOI`
- `Hénon global residue periodic orbit sum rule`

**Result.** These searches recovered classical multidimensional-residue machinery and exact Hénon orbit-sum literature, but no paper stating the proposed family-specific two-term law or coefficient certificate.

### 7.3 Exact-coefficient searches

- `"1572864" Hénon period 3`
- `"1296000" "Hénon" trace`
- `"3375+4096" Hénon multiplier`
- `"524288" Hénon period 3`

**Result.** No scholarly direct match was located for any exact coefficient/formula search.

### 7.4 Conjugacy and exponent searches

- `Hénon "a^{2m-1}" conjugacy`
- `Hénon "2m-1" "(x^m-a)^2"`
- `even degree Hénon conjugacy root of unity parameter`
- `"(x^m-a)^2" dynamics`

**Result.** The searches led back to general Hénon normal-form and root-of-unity conjugacy background, not to the explicit proposed equivalence or period-three law.

### 7.5 Recent-frontier searches

- `site:arxiv.org/abs/26 Hénon multiplier spectrum 2026`
- `site:arxiv.org/abs/2607 Hénon multipliers dynamics`
- `site:arxiv.org/abs/2608 Hénon multipliers period`
- `2026 "complex Hénon" multiplier trace spectrum`

**Result.** The relevant 2026 records found were Cantat–Dujardin and Bianchi–He. The former is the direct neighbor; the latter concerns unstable-cocycle thermodynamic geometry and is background only.

### 7.6 Metadata-resolution searches

Exact-title, author-title, DOI, Crossref-style, arXiv, journal, and publisher queries were separately run for Friedland–Milnor; Cattani–Dickenstein–Sturmfels; Cvitanović–Hansen–Rolf–Vattay; Dullin–Meiss; Huguin; both Hutz papers; Guillot–Ramírez; Ueda; Cantat–Dujardin; and Bianchi–He. The identifiers and statuses recorded in §3 are the resolved versions. Two common metadata traps were explicitly rejected:

- the Cattani–Dickenstein–Sturmfels chapter DOI ends in **`_8`**, not `_7`;
- the Dullin–Meiss DOI ends in **`00105-6`**, not `00100-6`.

## 8. Bounded absence statement

As of 2026-08-16 UTC, the searches above did not locate an indexed arXiv paper, primary publisher record, or author-hosted scholarly record giving the bound proof-package candidate's exact period-three quartic moment, the claimed full-fiber period-three separation theorem, or the uniform all-\(m\) two-term coefficient certificate.

This inference is bounded by:

- the databases and web pages reachable and indexed at the freeze date;
- English-language/title/abstract/formula discoverability;
- searches of arXiv and public publisher/author records rather than every thesis, proceedings archive, or print-only source;
- the possibility of unpublished manuscripts, nonindexed notes, differently normalized formulas, or future work.

Therefore the manuscript should say **“we are not aware of a prior explicit formula/result”** or **“no such result was located in our search”**, never **“this has never been done.”** Exact priority should be rechecked immediately before submission.

The local environment did not expose the novelty-check skill's separate cross-model reviewer endpoint. No independent-model verdict is fabricated in this ledger; the conclusion rests on the documented source search and must remain bounded accordingly.

## 9. Mandatory nonclaims

The following statements are outside the verified result or contradicted by direct prior art and must not appear as theorem-level claims:

1. **No universal nonvanishing claim:** do not assert \(D_m\ne0\) for every \(m\ge2\) unless a complete proof is added. At present this is an open conjectural step.
2. **No all-degree period-three recovery claim:** do not infer that period-three data recover \(a^{2m-1}\) for every \(m\).
3. **No family-discovery claim:** the quartic family \(p_L=(x^2-L)^2\) and its period-1/2 blindness are already explicit in Cantat–Dujardin under \(L=\lambda^2\).
4. **No universal quartic-Hénon theorem:** the separation result concerns the normalized Jacobian \(-1\) fiber whose formal fixed-point trace multiset is \(0^4\), not all quartic generalized Hénon maps.
5. **No global \(P(4)=3\) claim:** separation on this fiber does not identify the finite rigidity bound for every degree-four complex Hénon map.
6. **No global low-period-fiber classification:** one explicit full fiber does not classify all positive-dimensional fibers of low-period multiplier maps.
7. **No residue-method novelty claim:** global/multidimensional residue and quotient-trace techniques are classical; cite Cattani–Dickenstein–Sturmfels.
8. **No first-exact-sum-rule claim:** exact periodic-orbit identities for Hénon maps predate this work; cite Cvitanović et al. and distinguish the weight/observable.
9. **No general multiplier-rigidity claim:** finite multiplier rigidity is Cantat–Dujardin's theorem.
10. **No unstable-multiplier or saddle-spectrum claim:** a formal trace sum over all algebraic periodic points is not automatically an unstable-multiplier spectrum, a saddle-only invariant, or a thermodynamic invariant.
11. **No arithmetic consequence without proof:** do not claim height bounds, arithmetic finiteness, or arithmetic rigidity from the period-three formula alone.
12. **No geometric multiplicity shortcut:** if formal periodic schemes are counted, do not silently replace them by distinct exact-period points; invoke an appropriate dynatomic/intersection argument or state the counting convention precisely.

## 10. Precise bibliography recommendations

### Tier 1 — mandatory in the shortest defensible paper

1. **Cantat–Dujardin (2026), arXiv:2603.09445.** Cite in the introduction, immediately at the family definition, and in the discussion of period-1/2 blindness and general finite rigidity.
2. **Friedland–Milnor (1989), DOI 10.1017/S014338570000482X.** Cite for plane-polynomial-automorphism structure, generalized-Hénon normal form, and conjugacy background.
3. **Cattani–Dickenstein–Sturmfels (1996), DOI 10.1007/978-3-0348-9104-2_8.** Cite at the first global-residue/quotient-trace step.
4. **Cvitanović–Hansen–Rolf–Vattay (1998), DOI 10.1088/0951-7715/11/5/003.** Cite in related work to distinguish the new finite algebraic moment from classical Hénon orbit sum rules.
5. **Huguin (2024), arXiv:2412.19335.** Cite where one-dimensional small-cycle multiplier determination is contrasted with the Jacobian \(-1\) Hénon exception.

### Tier 2 — strongly recommended when low-period Hénon context is discussed

6. **Dullin–Meiss (2000), DOI 10.1016/S0167-2789(00)00105-6.** Use for generalized-Hénon low-period and bifurcation context.

### Tier 3 — include only if the corresponding paragraph is retained

7. **Hutz (2010), NYJM 16, 125–159, arXiv:0801.3643.** Include for formal/exact period or dynatomic-cycle language.
8. **Hutz (2020), DOI 10.5802/jtnb.1129.** Include for higher-dimensional projective multiplier invariants and isospectral families.
9. **Guillot–Ramírez (2019), DOI 10.1007/s40315-019-00293-w.** Include for index-derived fixed-point multiplier relations in \(\mathbb P^2\).
10. **Ueda (2004), DOI 10.2969/aspm/04210319.** Include for fixed points/index background specific to polynomial automorphisms of \(\mathbb C^n\).
11. **Bianchi–He (2026), arXiv:2606.29363.** Include only for a final current-frontier paragraph on unstable-cocycle thermodynamic geometry; omit from a minimal algebraic paper.

For sources with both a published version and a preprint, the bibliography should use the published version as the main record and may add the arXiv identifier for access. For Cantat–Dujardin, Huguin, and Bianchi–He, use **preprint/arXiv** status exactly as of the freeze date. Do not assign them journal venues not present in their primary records.

## 11. Submission-time recheck list

- Re-open arXiv:2603.09445, arXiv:2412.19335, and arXiv:2606.29363 for new versions or journal references.
- Repeat the exact coefficient searches and the family search with the manuscript's final notation.
- Search forward citations of Cantat–Dujardin and keyword-search any new version for “period 3,” “quartic,” “residue,” and the exact coefficients.
- Confirm whether the manuscript counts fixed points of \(f^3\), formal period-three points, exact-period-three points, or cycles; retain the factor-of-three distinction in every formula and caption.
- Keep the novelty sentence restricted to the proved quartic fiber theorem and any proved uniform coefficient statement.
