# Primary-source and novelty audit

Date: 2026-08-06  
Decision: **the operator mechanism is prior art; C02D remains a scoped
negative/effective-specialization result**

## Primary links

- Baladi--Pujals--Sambarino:
  [IMJ preprint 350](https://www.imj-prg.fr/preprints/350.pdf),
  [arXiv:math/0307045](https://arxiv.org/abs/math/0307045).
- Hubbard--Oberste-Vorth II:
  [arXiv:math/9401224](https://arxiv.org/abs/math/9401224).
- Bandtlow--Jenkinson signed trace:
  [arXiv:0802.1468](https://arxiv.org/abs/0802.1468).
- Ruelle graded determinant:
  [GDZ scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0034/LOG_0020.pdf).
- Fried:
  [Numdam article](https://www.numdam.org/item/ASENS_1986_4_19_4_491_0/).
- Baillif--Baladi:
  [arXiv:math/0211343](https://arxiv.org/abs/math/0211343).
- Bolotin--Treschev:
  [MathNet article](https://www.mathnet.ru/eng/rm9348).
- Bandtlow--Jenkinson explicit estimates:
  [arXiv:0802.1638](https://arxiv.org/abs/0802.1638).
- Bandtlow--Slipantschuk:
  [arXiv:2004.03534](https://arxiv.org/abs/2004.03534).
- Rugh 1992:
  [DOI landing page](https://doi.org/10.1088/0951-7715/5/6/003).
- Rugh 1996:
  [Cambridge PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5CCDE98C3D58F37B45E78AD07B29C339/S0143385700009111a.pdf/div-class-title-generalized-fredholm-determinants-and-selberg-zeta-functions-for-axiom-a-dynamical-systems-div.pdf).
- Liverani:
  [arXiv:math/0505049](https://arxiv.org/abs/math/0505049).

## Source ledger

| Source | Directly checked content | Consequence for this project |
|---|---|---|
| Project Paper 5, `5-An Area-Preserving Henon-Map Model.pdf` | The mother recurrence \(x_{n+1}=1-a x_n^2-x_{n-1}\), area preservation, reversibility, near-critical numerical/GUE motivation, and quartic continuum heuristic | The exact recurrence and conservative map are retained. The near-\(a\approx1.02\) statistical layer and quartic fit are not assumed. This project studies the target-free local hyperbolic control \(a=6\). |
| Baladi--Pujals--Sambarino, IMJ preprint 350 / arXiv:math/0307045 | Def. 2.4 pinning maps; (2.13) mixed Cauchy kernel; Def. 3.5 full graph operator; Remark 3.6 composition warning; Lemmas 3.7--3.8 iterated kernels, nuclearity, and absolute periodic trace | The natural source object is an exact one-step mixed Banach kernel. Qualitative pinning, chronological composition, nuclearity, and the absolute trace are not new. |
| Hubbard--Oberste-Vorth II, arXiv:math/9401224 | Complex Hénon horseshoe/pinning framework | Prevents claiming general holomorphic pinning or symbolic gluing as an \(H_6\)-specific invention. |
| Bandtlow--Jenkinson, arXiv:0802.1468 | Eq. (9), Thm. 4.2, and (10)--(11): nuclear holomorphic map-weight operators with fixed-point traces divided by \(\det(I-T')\) | Signed holomorphic fixed-point denominators already have a general operator theory. The BPS-specific leading-minus calculation is a representation-specific obstruction, not a universal no-go. |
| Ruelle, *Invent. Math.* 34 (1976), 231--242 | Operators on exterior forms and alternating Fredholm determinant products | Graded/superdeterminant repair is classical and cannot be the paper's novelty claim. |
| Fried, *Ann. Sci. ENS* 19 (1986), 491--517 | Exterior-power factorization and holomorphic fixed-point traces | Reinforces the classical graded/Lefschetz boundary. |
| Baillif--Baladi, arXiv:math/0211343 | Ruelle--Lefschetz/sharp determinants, form-valued operators, alternating products | A modern general formulation of signed/graded trace mechanisms. |
| Bolotin--Treschev, *Russian Math. Surveys* 65 (2010) | General Hill identity relating \(\det(P-I)\) to the discrete action Hessian | The C02C matching/Hill identity is an effective specialization, not a general novelty claim. |
| Bandtlow--Jenkinson, arXiv:0802.1638 | Explicit singular/eigenvalue and Fredholm-coefficient estimates for holomorphic transfer operators | Generic explicit finite-rank/spectral convergence claims already face strong prior art. |
| Bandtlow--Slipantschuk, arXiv:2004.03534 | Exponential finite-rank interpolation approximation on ellipse/annulus domains | Reframing \(N\) as analytic projection degree is legitimate but not automatically novel. |
| Rugh, *Nonlinearity* 5 (1992), 1237--1263 | Metadata/abstract and BPS's exact attributions were checked; direct full PDF was blocked by the publisher challenge | The pre-registered direct-full-text gate remains formally unmet. No novelty claim may rely on an assumed gap in this paper. |
| Rugh, *Ergodic Theory Dynam. Systems* 16 (1996), 805--819 | Generalized Fredholm determinants for Axiom-A surface diffeomorphisms | Further raises collision risk for an \(H_6\) Fredholm-determinant specialization. |
| Liverani, arXiv:math/0505049 | Fredholm determinants for Anosov maps | Further general prior art for absolute dynamical determinants. |

## Claim-by-claim boundary

| Proposed claim | Ruling |
|---|---|
| First graph-directed pinning operator for a Hénon map | not supported; BPS/Rugh mechanism directly specializes |
| First signed denominator trace for a holomorphic operator | refuted as novelty by Bandtlow--Jenkinson and Lefschetz theory |
| First graded/superdeterminant sign repair | refuted as novelty by Ruelle/Fried/Baillif--Baladi |
| First action-Hessian/monodromy identity | refuted as general novelty by Hill's formula |
| First quantitative analytic finite-rank transfer approximation | refuted as general novelty by existing approximation theory |
| Explicit \(H_6\) mixed domains with rational margins | retained as an effective specialization |
| C02C window \(\Rightarrow\) same-clock operator approximation | refuted under the frozen BPS-kernel semantics |
| Scalar edge cocycle fixes every BPS raw-kernel orbit weight | exactly refuted orbitwise by repetition; aggregate-only cancellation is not ruled out |

## Unresolved source obligation

The Rugh 1992 publisher PDF could not be read directly in this environment.
The BPS paper reproduces and explicitly attributes the relevant construction,
and other accessible primary sources already subsume the proposed novelty.
Consequently this access gap does not rescue C02D, but a future journal
submission making detailed historical claims should obtain the paper through
a library or the author.

## Final novelty ruling

The strongest honest output is a negative/effective research note:

- a formally certified \(Y\times X\) Hénon pinning-domain lemma;
- a semantic theorem separating exact iterates/recodings from an
  approximation on a fixed one-step operator;
- a representation-specific constant-sign and repetition obstruction;
- a clear boundary showing why classical graded and finite-rank machinery
  does not by itself create a Hilbert--Pólya candidate.

No positive RH, Route-B, or manuscript-level new operator claim is authorized.
