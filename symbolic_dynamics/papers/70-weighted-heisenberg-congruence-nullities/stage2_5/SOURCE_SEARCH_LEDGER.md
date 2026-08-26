# P70 Stage 2.5 source-search ledger

Audit target: `Weighted Three-Term Shifts on Finite Heisenberg Quotients`  
Search freeze: **2026-08-26 UTC**  
Audited source state: the current `references.bib` and current body sections; neither was edited during this audit.  
Release state: **internal / external release HOLD**.

## Method and status vocabulary

Every entry in `references.bib` was searched separately on the public Web with title-, author-, DOI-, and, where available, arXiv-based queries. DOI landing pages, publisher pages, arXiv records, institutional repositories, and original PDFs were preferred. `VERIFIED` means that all supplied BibTeX fields agree with an authoritative or primary record, allowing capitalization and BibTeX accent normalization. `MISMATCH` means that at least one supplied field disagrees. `NOT_FOUND` would be used only after three materially different queries failed to locate exact evidence. No P70 item reached `MISMATCH` or `NOT_FOUND`.

The search is auditable but not exhaustive: public indexing can miss paywalled, non-English, older, or poorly indexed records, and result ordering can drift after the freeze date.

## A. Item-by-item bibliography verification (5/5)

### A1. `LindSchmidt2015` — **VERIFIED**

- Queries run:
  1. `10.1070/RM2015v070n04ABEH004957 Lind Schmidt Heisenberg survey`
  2. `"A survey of algebraic actions of the discrete Heisenberg group"`
  3. `arXiv 1502.06243 Lind Schmidt`
- Direct records: [Math-Net publication page](https://www.mathnet.ru/eng/rm9658), [publisher-hosted English PDF](https://www.mathnet.ru/links/f94b19d18b946cea26f0dd62e0627860/rm9658_eng.pdf), [arXiv:1502.06243](https://arxiv.org/abs/1502.06243), [DOI](https://doi.org/10.1070/RM2015v070n04ABEH004957).
- Field audit: Douglas Lind and Klaus Schmidt; title; *Russian Mathematical Surveys* 70(4), 657–714 (2015); DOI; and arXiv identifier all agree.

### A2. `GollSchmidtVerbitskiy2014` — **VERIFIED**

- Queries run:
  1. `10.1016/j.indag.2014.04.007 Goll Schmidt Verbitskiy`
  2. `"Algebraic Actions of the Discrete Heisenberg Group: Expansiveness and Homoclinic Points"`
  3. `arXiv 1312.2469`
- Direct records: [Elsevier/ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0019357714000366), [arXiv:1312.2469](https://arxiv.org/abs/1312.2469), [author publication page](https://pub.math.leidenuniv.nl/~verbitskiyea/pages/publications.html), [DOI](https://doi.org/10.1016/j.indag.2014.04.007).
- Field audit: Martin Göll, Klaus Schmidt, Evgeny Verbitskiy; title; *Indagationes Mathematicae* 25(4), 713–744 (2014); DOI; and arXiv identifier all agree.

### A3. `GurevichHadani2010` — **VERIFIED**

- Queries run:
  1. `10.1007/978-0-8176-4831-2_8 Gurevich Hadani canonical quantization`
  2. `"Notes on Canonical Quantization of Symplectic Vector Spaces over Finite Fields"`
  3. `arXiv 0708.0669 Gurevich Hadani`
- Direct records: [DOI/Springer chapter](https://doi.org/10.1007/978-0-8176-4831-2_8), [arXiv:0708.0669](https://arxiv.org/abs/0708.0669), [Hadani publication list](https://web.ma.utexas.edu/users/hadani/publications.htm).
- Field audit: authors, chapter title, *Arithmetic and Geometry Around Quantization*, Progress in Mathematics 279, 233–251, Birkhäuser, 2010, DOI, and arXiv identifier all agree.

### A4. `Zaidenberg2008` — **VERIFIED**

- Queries run:
  1. `math-ph/0606070 Zaidenberg convolution equations lattices`
  2. `"Convolution Equations on Lattices: Periodic Solutions with Values in a Prime Characteristic Field"`
  3. `Geometry and Dynamics of Groups and Spaces 265 721 742 Zaidenberg`
- Direct records: [arXiv:math-ph/0606070](https://arxiv.org/abs/math-ph/0606070), [original MPIM preprint PDF](https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2006/67.pdf), [Springer book record](https://link.springer.com/book/10.1007/978-3-7643-8608-5).
- Field audit: Mikhail Zaidenberg; chapter title; *Geometry and Dynamics of Groups and Spaces*, Progress in Mathematics 265, 721–742, Birkhäuser, 2008; and arXiv identifier all agree. The BibTeX entry contains no chapter DOI, so no DOI claim is being made.

### A5. `FordJha1993` — **VERIFIED**

- Queries run:
  1. `10.1080/10586458.1993.10504271`
  2. `"On Wendt's Determinant and Sophie Germain's Theorem"`
  3. `Ford Jha Wendt determinant Experimental Mathematics 2 113 120`
- Direct records: [Taylor & Francis publisher page](https://www.tandfonline.com/doi/abs/10.1080/10586458.1993.10504271), [EuDML full record](https://eudml.org/doc/233508), [DOI](https://doi.org/10.1080/10586458.1993.10504271).
- Field audit: David Ford and Vijay Jha; title; *Experimental Mathematics* 2(2), 113–120 (1993); and DOI all agree.

### A6. Bibliography summary

| Result | Count | Keys |
|---|---:|---|
| VERIFIED | 5 | all five keys |
| MISMATCH | 0 | none |
| NOT_FOUND | 0 | none |

## B. Ghost and dangling citation audit

Citation-key extraction from all `sections/*.tex` found exactly the same five unique keys as `references.bib`.

- dangling in-text keys absent from the bibliography: **0**;
- bibliography entries never cited in the body: **0**;
- unresolved citation markers or raw placeholder keys: **0**;
- ghost works: **0**.

## C. Citation-context verification (10/10 commands; 100%)

The denominator is the 10 citation commands in the current body. Every context was checked against an abstract or original text, not merely against metadata.

| # | Manuscript locator | Citation(s) and claim in context | Original-content check | Verdict |
|---:|---|---|---|---|
| 1 | `sections/1_introduction.tex:3–7` | Zaidenberg develops positive-characteristic lattice Fourier/torsion-point viewpoint | The [original paper](https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2006/67.pdf) treats convolution on finite-rank lattices/toric grids over positive-characteristic fields and identifies spectral questions with torsion points on algebraic hypersurfaces. | SUPPORTED |
| 2 | `sections/1_introduction.tex:12–16` | unit-coefficient resultant is Wendt’s determinant and relates to Fermat-curve points | The [publisher abstract](https://www.tandfonline.com/doi/abs/10.1080/10586458.1993.10504271) explicitly identifies Wendt’s determinant as the resultant of `X^n-1` and `(-1-X)^n-1` and relates it to points on Fermat curves modulo a prime. | SUPPORTED |
| 3 | `sections/1_introduction.tex:22–24` | Göll–Schmidt–Verbitskiy develop principal Heisenberg expansiveness/homoclinic methods | The [abstract and paper](https://arxiv.org/abs/1312.2469) explicitly cover expansiveness, a nonexpansive homoclinic point, and an equal-entropy symbolic cover for discrete Heisenberg principal actions. | SUPPORTED |
| 4 | `sections/1_introduction.tex:24–27` | Lind–Schmidt treat the exact integer element `1+a+b` as a mixing example | The [original PDF, Example 4.4(a)](https://www.mathnet.ru/links/f94b19d18b946cea26f0dd62e0627860/rm9658_eng.pdf) states: for `f=1+x+y`, the action is mixing. | SUPPORTED |
| 5 | `sections/1_introduction.tex:55–59` | finite Heisenberg Stone–von Neumann description is standard | The [chapter abstract](https://arxiv.org/abs/0708.0669) explicitly proves a stronger finite-field Stone–von Neumann theorem and constructs the canonical Weil representation. | SUPPORTED; P70’s cross-characteristic transfer is proved locally |
| 6 | `sections/3_regular_decomposition.tex:18–22` | Gurevich–Hadani as standard owner/model | Same original-content check as #5. The manuscript does not silently transfer the complex statement; it gives a direct cross-characteristic proof. | SUPPORTED |
| 7 | `sections/4_character_blocks.tex:33–39` | cyclotomic torsion intersection is analogous to Zaidenberg’s abelian lattice Fourier analysis | Zaidenberg’s original text uses positive-characteristic Fourier analysis and torsion points on a torus. P70’s “analogous” wording is accurate and scoped. | SUPPORTED |
| 8 | `sections/4_character_blocks.tex:40–42` | `(1,1,1)` resultant is classical Wendt determinant | Ford–Jha’s defining resultant is exactly the displayed pair after the manuscript’s odd-`ell` unit/sign normalization. | SUPPORTED |
| 9 | `sections/7_scope_declarations.tex:3–7` | principal Heisenberg actions and `1+a+b` precede P70 | [Göll–Schmidt–Verbitskiy](https://arxiv.org/abs/1312.2469) own the principal-action framework; [Lind–Schmidt](https://www.mathnet.ru/eng/rm9658) include the exact element. | SUPPORTED |
| 10 | `sections/7_scope_declarations.tex:6–10` | finite Stone–von Neumann theory is standard; only weighted mod-`p` nullity formula claimed | Gurevich–Hadani support the standard-theory statement. The “only” boundary is a manuscript claim, not a global priority certificate. | SUPPORTED WITH SEARCH BOUNDARY |

Context support rate: **10/10 citation commands (100%)**, exceeding the required 30% sample.

## D. Alternate-term exact-neighbor query ledger

The following searches were run through **2026-08-26**. “No exact collision” means that no public result located by these terms states the same weighted cross-characteristic formula, including both the cyclotomic degree and the `ell(ell-1)` Fermat-locus jump with block corank one. It is not a worldwide novelty finding.

| Core advance | Query (three materially different formulations per advance) | Search result / nearest public neighbor |
|---|---|---|
| Exact fixed-space formula | `"alpha x_g+beta x_{ga}+gamma x_{gb}" Heisenberg finite quotient` | No exact public match located. |
|  | `weighted three-term group shift finite Heisenberg congruence nullity` | No exact formula located. A direct method neighbor is [Deundyak–Leonov (2016)](https://vestnik.kubsu.ru/article/view/686), which solves general convolution equations on finite Heisenberg groups by noncommutative FFT. |
|  | `periodic configurations Heisenberg group finite field convolution kernel dimension` | General finite-Heisenberg convolution and lattice-convolution literature surfaced; no matching symbolic fixed-dimension formula. See [Deundyak–Leonov PDF](https://vestnik.kubsu.ru/article/download/686/1168/694) and [Zaidenberg](https://arxiv.org/abs/math-ph/0606070). |
| Clock–shift determinant / Fermat locus | `"det(alpha I+beta U+gamma V)" Heisenberg` | No exact public match located. |
|  | `clock shift matrix determinant Fermat curve finite field` | Fermat determinantal-representation and generic clock/shift results surfaced, but not the P70 identity in this setting. |
|  | `Weyl pair three term determinant alpha beta gamma` | General Weyl-pair literature surfaced; no exact three-term determinant/source collision located. |
| Corank-one nonlinear jump | `"ell(ell-1)" Heisenberg nullity Fermat` | No exact public match located. |
|  | `singular clock shift block nullity one cyclic recurrence` | No exact public match located. |
|  | `finite Heisenberg regular representation nonlinear block kernel dimension` | Standard representation sources surfaced, especially [Grassberger–Hörmann (2001)](https://dmtcs.episciences.org/284) and [Gurevich–Hadani](https://arxiv.org/abs/0708.0669); neither states the weighted block-kernel formula. |
| Character gcd / torsion term | `cyclotomic gcd character blocks finite Heisenberg shift` | No exact public match located. |
|  | `Wendt determinant periodic points Heisenberg group shift` | [Ford–Jha](https://eudml.org/doc/233508) and Heisenberg-action sources surfaced separately; no combined fixed-space formula. |
|  | `torsion points alpha beta u gamma v finite quotient convolution` | [Zaidenberg](https://arxiv.org/abs/math-ph/0606070) surfaced as the abelian torsion-point owner; no nonlinear Heisenberg jump. |

## E. Nearest neighbors not present in the current bibliography

### E1. Direct finite-Heisenberg convolution neighbor — material omission

V. M. Deundyak and D. A. Leonov, “FFT and Solving of Convolution Equations on Heisenber Group over Prime Galua Field,” *Ecological Bulletin of Research Centers of the Black Sea Economic Cooperation*, no. 2 (2016), 46–53, [publisher record](https://vestnik.kubsu.ru/article/view/686), [original PDF](https://vestnik.kubsu.ru/article/download/686/1168/694).

Original-text inspection, not just metadata, confirms that this paper:

- defines left and right convolution on a finite group;
- lists the `p^2` one-dimensional and `p-1` degree-`p` irreducibles of `H(F_p)`;
- constructs forward/inverse noncommutative Fourier transforms from cyclic FFTs;
- gives an algorithm for solving convolution equations by inverting the representation blocks.

Owner subtraction: Deundyak–Leonov own a direct finite-Heisenberg convolution/Fourier solution framework and essentially the characteristic-zero representation ledger. They do **not** study P70’s cross-characteristic coefficient field `F_p` with quotient order `ell`, singular kernel dimensions, the weighted three-term symbol, the cyclotomic gcd term, the Fermat-locus determinant, or the exact corank-one/full-jump formula. Because the method neighborhood is direct, the source should nevertheless be cited and subtracted explicitly before external release.

### E2. Direct finite-Heisenberg representation neighbor

Johannes Grassberger and Günther Hörmann, “A Note on Representations of the Finite Heisenberg Group and Sums of Greatest Common Divisors,” *Discrete Mathematics & Theoretical Computer Science* 4(2), 91–100 (2001), [publisher](https://dmtcs.episciences.org/284), [DOI](https://doi.org/10.46298/dmtcs.284), [PDF](https://dmtcs.episciences.org/284/pdf).

This source constructs all irreducible representations of finite Heisenberg groups (more generally `H(Z_n)`) and counts their equivalence classes. For prime `n=ell`, its list specializes to the character/nontrivial-central-character strata used by P70. It does not supply the weighted fixed-space formula. Gurevich–Hadani remains a valid standard Stone–von Neumann source, but this earlier, direct finite-group source is a closer owner for the explicit irreducible ledger.

## F. Search-bounded conclusion

All five current bibliography entries and all ten current citation contexts are source-valid. The expanded search nevertheless found a **material related-work omission**: finite-Heisenberg convolution equations were treated directly by Deundyak–Leonov (2016), and the explicit finite-Heisenberg irreducible classification has a direct earlier source in Grassberger–Hörmann (2001). No inspected source states P70’s exact weighted cross-characteristic nullity formula.

The only permissible priority conclusion is:

`BOUNDED_NO_EXACT_WEIGHTED_NULLITY_COLLISION_LOCATED_AS_OF_2026-08-26`

Collision risk is **MEDIUM-HIGH**: the determinant and representation decomposition are elementary once the block model is selected, and a general finite-Heisenberg convolution solver already exists. Hidden, implicit, non-English, or unpublished derivations remain plausible. This ledger is not a worldwide novelty or priority certificate.

