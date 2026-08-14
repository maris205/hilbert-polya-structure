# Citation Verification

## Scope and method

This audit covers the seventeen references expected to carry the paper's historical
and prior-art statements.  Metadata was checked on 2026-08-13 against DOI
registration records and, where available, the publisher's article page or an
authoritative repository copy.  Content claims were checked against official
abstracts, publisher PDFs, or author-posted/arXiv manuscripts.  Search-result
snippets were not used as claim evidence.

Status labels mean:

- **M+C verified:** bibliographic metadata and the stated content claim were
  checked from primary or publisher-controlled material.
- **M verified / claim restricted:** metadata is verified, but the full text
  was not independently available; only the narrow claim stated below is safe.
- **M verified / exact formula pending:** the article and its broad relevance
  are verified, but a formula already quoted in the source lock was not
  independently located in accessible full text.  The manuscript must not
  attribute that exact formula to the article without a page/section check.

## Claim-level audit

| Citation key | Status and authoritative record | Safe claim for this paper | Do not claim from this audit |
|---|---|---|---|
| `alseda2025realteapot` | **M verified / exact formula pending.** Cambridge University Press and Crossref: [DOI 10.1017/etds.2025.15](https://doi.org/10.1017/etds.2025.15). ETDS 45(10), 2945--2975; authors and official abstract checked. | The paper studies real zeros of kneading determinants for unimodal/tent maps and explicitly places the reciprocal of a Galois conjugate in the kneading-determinant framework. It is safe to cite as direct modern prior art showing that this kneading-determinant setting is established. | The source lock's more specific statement (K_{\sqrt2}=RLR^\infty) and (D_{\sqrt2}(z)=(1-2z^2)/(1+z)) was not independently found in the accessible abstract/HTML. Treat that exact attribution as **page-level verification pending**, not as established by this audit. |
| `hofbauer1985periodic` | **M+C verified.** Cambridge University Press: [DOI 10.1017/S014338570000287X](https://doi.org/10.1017/S014338570000287X); official 20-page PDF checked, especially Lemmas 1--2 and the zeta discussion. | Markov-diagram closed paths encode periodic points of piecewise monotone interval maps, with finitely many exceptional codings; on a decreasing return branch a period-(n) symbolic object can correspond to period (2n). Finite exceptional periodic codings contribute explicit finite zeta factors. | Do not state that Hofbauer proves this project's particular three-state quotient or its exact single ghost; those are the present worked calculation. |
| `milnor1988iterated` | **M verified / claim corroborated.** Springer DOI record: [DOI 10.1007/BFb0082847](https://doi.org/10.1007/BFb0082847), pp. 465--563. The role of this work was also checked through Rugh--Tan's primary-source account. | Foundational kneading theory for continuous piecewise monotone interval maps and the established connection between kneading data, entropy, and dynamical zeta functions. | Do not assign this paper the project's signed matrix (W), its boundary quotient, or a weighted formalism developed later. |
| `demelo1993one` | **M+C verified.** Springer: [DOI 10.1007/978-3-642-78043-1](https://doi.org/10.1007/978-3-642-78043-1), *One-Dimensional Dynamics*, Ergebnisse series volume 25 (1993). Publisher metadata and the relevant homterval/no-wandering results in the full text were checked. | For smooth interval maps with nonflat critical points, the homterval lemma and no-wandering-interval theorem reduce a nontrivial itinerary fibre to a wandering interval or an attracting periodic basin; the negative-Schwarzian basin theorem forces such a basin to meet a critical point or boundary. These results may be applied after their hypotheses are verified for the frozen quadratic map. | Do not infer the project's exact three-state graph, sole boundary ghost, or zeta correction from the book; those are proved directly here. |
| `rugh2015kneading` | **M+C verified.** EMS Press: [DOI 10.4171/JFG/24](https://doi.org/10.4171/JFG/24); [arXiv:1407.5313](https://arxiv.org/abs/1407.5313). Publisher metadata and full manuscript checked. | Rugh and Tan extend kneading theory to branch weights, define a weighted kneading determinant, prove a zeta identity, and explicitly use point germs and boundary terms. This supports treating weighted/boundary-sensitive determinant conventions as prior art. | Their weights are not automatically symplectic orientations, Maslov phases, or the factor-orientation convention used here. |
| `bose1989generalized` | **M+C verified.** Cambridge University Press: [DOI 10.1017/S0143385700004788](https://doi.org/10.1017/S0143385700004788); official abstract checked. | Generalized baker transformations are a classical platform for representing stationary stochastic processes and measure-preserving automorphisms. This supports the non-novelty of a generic generalized-baker carrier. | Do not claim Bose supplies this project's PCF graph, exact affine translations, or branchwise sign convention. |
| `bruin2014natural` | **M+C verified.** Springer: [DOI 10.1007/s00605-014-0644-0](https://doi.org/10.1007/s00605-014-0644-0); [arXiv:1306.5451](https://arxiv.org/abs/1306.5451). Full manuscript checked. | Geometric natural extensions for piecewise affine/nonsingular systems can be constructed via Hofbauer towers; the paper uses the ordinary baker map as the basic invertible extension of doubling and proves almost-everywhere invertibility in its measure-theoretic setting. | This does not make the present finite labeled shift homeomorphic to the full topological inverse limit, nor does it prove a globally smooth symplectic lift. |
| `balazs1989quantized` | **M verified / claim restricted.** Elsevier/Crossref: [DOI 10.1016/0003-4916(89)90259-5](https://doi.org/10.1016/0003-4916(89)90259-5); official Elsevier API title/date and journal metadata checked. | A quantized baker transformation was already constructed and studied in 1989; generic baker quantizability is therefore historical precedent, not evidence for a new arithmetic quantization here. | Do not infer that its boundary conditions or quantum operator canonically quantize this labeled PCF carrier. |
| `saraceno1990classical` | **M verified / claim restricted.** Elsevier/Crossref: [DOI 10.1016/0003-4916(90)90367-W](https://doi.org/10.1016/0003-4916(90)90367-W); official Elsevier API title/date and journal metadata checked. | There is established follow-up work on classical structures in the quantized baker transformation, reinforcing that generic baker quantization is mature prior art. | Do not attribute a canonical arithmetic phase, action, or quantization of this candidate to Saraceno. |
| `berry1999riemann` | **M verified / claim restricted.** SIAM/Crossref: [DOI 10.1137/S0036144598347497](https://doi.org/10.1137/S0036144598347497); the [University of Bristol research record](https://research-information.bris.ac.uk/en/publications/5ae13871-7186-49c2-b378-ab0b07b59ee1) independently confirms authors, venue, volume, year, and pages. | Historical mathematical-physics context for discussing Riemann zeros and eigenvalue asymptotics. It may motivate why a genuine spectral/arithmetic mechanism would need far more than a symbolic resemblance. | This project did not test a Berry--Keating Hamiltonian, prove a Hilbert--Pólya realization, or access Riemann-zero data. Do not use this citation to imply any such result. |
| `artin1965periodic` | **M verified / claim restricted.** JSTOR DOI/RIS record: [DOI 10.2307/1970384](https://doi.org/10.2307/1970384), Annals of Mathematics 81(1), 82--99. | Historical source for the periodic-point framework conventionally called the Artin--Mazur zeta function. The manuscript should still state its own counting definition explicitly. | Do not use the name alone to equate the unsigned SFT zeta, the parent quotient, the factor-orientation determinant, and the Lefschetz zeta; this project keeps all four conventions separate. |
| `bowen1970zeta` | **M verified / claim restricted.** American Mathematical Society/Crossref: [DOI 10.1090/pspum/014/9985](https://doi.org/10.1090/pspum/014/9985), *Global Analysis*, Proceedings of Symposia in Pure Mathematics 14, 43--49. | Historical reference for zeta functions of finite-type shift restrictions. It is safe background for the standard finite symbolic-dynamics context. | The present identities (1/\det(I-zA)), the signed matrix (W), and the boundary quotient are derived and checked inside this project; do not outsource their convention-sensitive proof to the citation. |
| `ji2026space` | **M+C verified.** Springer/Crossref: [DOI 10.1007/s00208-026-03361-4](https://doi.org/10.1007/s00208-026-03361-4); [arXiv:2308.00289v3](https://arxiv.org/abs/2308.00289), journal reference *Mathematische Annalen* 394(3), article 62. Publisher metadata, arXiv API metadata, abstract, Definitions 1.1, and Theorems 1.4 and 1.14 were checked. | For every **non-exceptional rational map** (f:\mathbb P^1(\mathbb C)\to\mathbb P^1(\mathbb C)) of degree at least two, the (mathbb Q)-span of finite periodic characteristic exponents is infinite-dimensional. The paper also proves rigidity results involving multiplier/length spectra and a length-spectrum characterization of PCF rational maps. This is strong context that finite symbolic coding does not itself force a finite-rank derivative clock. | Do not extend the theorem from rational maps on (\mathbb P^1) to arbitrary smooth, interval, or symplectic maps. Do not omit the non-exceptional hypothesis: exceptional means Latt\`es or monomial type in that paper. Its characteristic exponent is period-normalized, (n^{-1}\log|\rho_f|), whereas this project's orbit length is unnormalized (\log|\Lambda_u|). |
| `wang2026prime` | **M+C verified.** Taylor & Francis official *Research in Mathematics* volume 13, issue 1 record and Crossref: [DOI 10.1080/27684830.2026.2684334](https://doi.org/10.1080/27684830.2026.2684334), article 2684334. The publisher metadata and an archived author-provided article PDF were checked; the latter has SHA-256 `78a65db26110ef8173c3d7dc50caf2b598e59b854e7b5afa3983891008cb953e`. | Wang's 2026 study supplies the genealogy for the same Logistic family, the band-merging parameter (u_c\simeq1.543689), the (RLR) symbolic skeleton, and the prime-symbolic motivation. It is safe to attribute that inheritance while stating that the present paper asks a different autonomous-carrier/clock question. | Do not treat the earlier paper's prime-sieve assertions as reverified here, do not imply that its prime data entered the frozen experiments, and do not transfer its non-autonomous construction to the present autonomous baker without proof. Page-anchor trust was unavailable in this environment (`pypdf` absent), so the content check used full-text extraction and is not a page-level quotation audit. |
| `lind2021symbolic` | **M+C verified.** Cambridge University Press: [DOI 10.1017/9781108899727](https://doi.org/10.1017/9781108899727); second edition, Cambridge Mathematical Library, print year 2021. Publisher contents and book description checked. | Standard reference for shifts of finite type, higher-block presentations, finite-state codes, factor codes, and periodic-orbit bookkeeping. | The book is background for standard symbolic machinery; it does not contain this paper's arithmetic-prime certificate or particular PCF boundary calculation. |
| `parry1990zeta` | **M+C verified.** Soci\'et\'e Math\'ematique de France: [DOI 10.24033/ast.28](https://doi.org/10.24033/ast.28), Ast\'erisque 187--188 (1990); official open text and contents checked. | Standard treatment of shifts of finite type, suspensions/roof functions, weighted periodic-orbit data, transfer operators, and dynamical zeta functions. | Do not attribute the paper's finite-\(\Q\)-rank prime-log corollary or its convention-specific matrices to this monograph. |
| `marcus1991weight` | **M+C verified.** Cambridge University Press: [DOI 10.1017/S0143385700006052](https://doi.org/10.1017/S0143385700006052), ETDS 11(1), 129--180. Official abstract and publisher PDF metadata checked. | Established work on invariants and normalized weights constructed from periodic orbits of Markov chains; safe context that finite-state weighted periodic data are mature machinery. | It does not state the present multiplier-clock theorem in this arithmetic form, and the manuscript makes no priority claim for the underlying finite-span observation. |

## Safe synthesis for the manuscript

The references support four deliberately limited statements:

1. kneading determinants, Markov diagrams, and boundary-sensitive periodic
   coding are established interval-dynamics machinery
   (`milnor1988iterated`, `hofbauer1985periodic`, `rugh2015kneading`,
   `demelo1993one`);
2. generalized bakers and geometric natural extensions are classical carrier
   constructions (`bose1989generalized`, `bruin2014natural`);
3. baker quantization is established precedent but does not make the present
   candidate canonically quantizable (`balazs1989quantized`,
   `saraceno1990classical`); and
4. the Riemann/spectral literature is motivation only, while this candidate's
   finite-rank obstruction is data-free and does not test Riemann zeros
   (`berry1999riemann`); and
5. the inherited Logistic parameter and prime-symbolic motivation are
   attributed to the author's earlier study, whose prime-sieve claims and data
   are explicitly outside the present audit (`wang2026prime`); and
6. higher-block recoding, locally constant roofs/weights, and periodic-orbit
   weight invariants are standard symbolic-dynamics machinery
   (`lind2021symbolic`, `parry1990zeta`, `marcus1991weight`).

The finite-rank clock theorem itself is proved in the project from finite
block recoding and unique factorization.  No external citation is needed to
replace that proof.  `artin1965periodic` fixes the historical zeta terminology,
not the project's convention-sensitive identities.

## Bibliography integrity notes

- `references.bib` contains exactly these seventeen audited entries; no record was
  generated from memory alone.
- DOI letter case is preserved where useful, although DOI resolution is
  case-insensitive.
- The two arXiv identifiers were confirmed from the arXiv API and manuscripts;
  they supplement, rather than replace, the journal DOI records.
- The *Real Teapot* exact-(\sqrt2) formula must remain qualified until someone
  with full-text access records its page or proposition number.
