# Stage 3 Source Lock and Trace-Framework Matrix

Search and verification date: **2026-08-13**  
Phase boundary: source verification and theorem-applicability design only  
Primary cases: `DEN-WITT-Z-FIN`, `MOD-GEO`  
Excluded operation: combining the strongest coordinates of the two cases

## 1. Search method

This is a targeted theorem audit, not a claim of exhaustive systematic review.
The starting corpus was the locally acquired primary-source set from Stages 1
and 2.  Gap-filling searches were limited to the exact Selberg identity and a
rigorous statement of the semiclassical Gutzwiller regime.

### Sources and queries

- Local originals under
  [`../../2-flow-zeta/notes/sources/`](../../2-flow-zeta/notes/sources/):
  Deninger, Duistermaat--Guillemin, Kordyukov, ALKL,
  Dyatlov--Zworski, and Fried.
- Stable discovery/metadata endpoints: arXiv, Numdam, GDZ, Springer,
  journal/DOI records, IAS/CERN archival records, and INSPIRE for the original
  Gutzwiller paper.
- Query strings:
  - `Duistermaat Guillemin clean wave trace canonical density theorem 4.5`
  - `Selberg 1956 trace formula PSL2Z hyperbolic continuous spectrum`
  - `foliated flow simple closed orbit Lefschetz distribution b-trace`
  - `Anosov flat trace Poincare map Pollicott Ruelle resonances`
  - `Gutzwiller semiclassical trace formula rigorous hbar theorem`
  - `A proof Gutzwiller trace formula coherent states Theorem 2.3`

### Inclusion criteria

1. Original theorem/derivation or a standard proof monograph needed to state
   the exact cofinite formula.
2. An explicit operator/action, trace functional, fixed-point/orbit
   hypotheses, and locator.
3. Direct relevance to at least one of: local/global extent, fixed versus
   semiclassical regime, coefficient provenance, or same-object identity.
4. Stable bibliographic identity verified by DOI, journal archive, or arXiv.

### Exclusion criteria

- secondary pages used only for discovery;
- a formula with no recoverable hypotheses or test class;
- GUE/statistical analogies, Riemann-zero fitting, or formal Hamiltonians;
- general operator-algebra programmes not tied to a frozen flow;
- recent claims of an “exact quantum trace” that are not needed to interpret
  the established theorem families;
- any source used to justify transferring a coefficient between candidate IDs.

No stable database hit counts were available, so none are invented.  Ten
external works are included as core or standard-authority sources; the Stage-1
support theorem is separately identified as a project-internal proved result.

### Distributional coverage advisories

`DISTRIBUTIONAL_SKEW_ADVISORY`

- Dimension: methodological distribution
- Concentration: theoretical/mathematical source = 10/10 (100%)
- Advisory: this is a coverage signal, not a defect.
- Search response: no expansion; the RQ is a theorem-hypothesis audit and has
  no empirical population.

`DISTRIBUTIONAL_SKEW_ADVISORY`

- Dimension: time distribution
- Concentration: pre-2020 foundational works = 8/10 (80%)
- Advisory: the corpus is intentionally dominated by original trace theorems.
- Search response: ALKL (2024 preprint/2026 monograph) is included for the
  current foliated-flow endpoint; a rigorous 1999 semiclassical theorem is
  included rather than replacing foundational statements with recent surveys.

## 2. Evidence vocabulary

| Label | Meaning in this audit |
|---|---|
| `PROVED` | The cited source states the theorem/definition or the project gives a complete elementary proof. |
| `CONDITIONAL_THEOREM` | Exact after all displayed source hypotheses are assumed. |
| `OPEN` | A meaningful bridge is not supplied or ruled out by the frozen source. |
| `NOT_TESTABLE` | The required operator, domain, topology, trace, or map has not been defined. |
| `NOT_APPLICABLE_HYPOTHESES_FAIL` | A theorem is clear, but the frozen candidate fails at least one named input hypothesis. |
| `SEMICLASSICAL_ASYMPTOTIC` | A theorem controls a smoothed quantity as \(\hbar\to0\); it is not an exact fixed-\(\hbar\) identity. |
| `HEURISTIC` | A physical derivation or analogy without the theorem-level hypotheses/remainder needed here. |

The general ARS seven-level empirical evidence pyramid is not meaningful for
mathematical theorem provenance.  These are single theoretical works, but the
original theorem is the gold-standard source for a claim about its own
hypotheses and conclusion.  Grades below indicate fitness for the cited claim,
not an RCT-style study rank.

## 3. Verified source ledger

| ID | Source and stable entry | Exact locator used | Acquisition / verification | Claim supported | Limitation for this paper | Evidence / grade |
|---|---|---|---|---|---|---|
| `DEN` | C. Deninger, *Dynamical Systems for Arithmetic Schemes*, Indag. Math. 37 (2026), 25--136, DOI [10.1016/j.indag.2024.05.007](https://doi.org/10.1016/j.indag.2024.05.007); [arXiv:1807.06400v4](https://arxiv.org/abs/1807.06400) | Introduction pp. 2--3; Theorem 5.2; §6, Theorem 6.1, printed pp. 38--39; §11, eqs. (104)--(114) | [local PDF](../../2-flow-zeta/notes/sources/deninger-dynamical-systems-arithmetic-schemes-v4.pdf), SHA-256 `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09`; metadata and v4 date rechecked 2026-08-13 | Every periodic orbit belongs to one compact closed-point packet and has period \(\log N x_0\); §11 defines a different group convolution | No packet smooth atlas, linearized return, trace domain, cohomological action, or quantum operator is supplied | object claims `PROVED`, interface `OPEN/NOT_TESTABLE`; A |
| `DG` | J.J. Duistermaat and V.W. Guillemin, *The Spectrum of Positive Elliptic Operators and Periodic Bicharacteristics*, Invent. Math. 29 (1975), 39--79, DOI [10.1007/BF01405172](https://doi.org/10.1007/BF01405172) | Definition 4.1; Lemmas 4.2--4.4; Theorem 4.5, printed pp. 59--61 (local PDF pp. 22--24) | [GDZ local scan](../../2-flow-zeta/notes/sources/duistermaat_guillemin_1975.pdf), SHA-256 `bf7dcd0a3ae339bc237045be79a88f4433507a1fc01f9ab9e404621ffc4f2149`; scan locator inherited from a visual check, metadata rechecked | For a positive self-adjoint elliptic operator, wave-trace singularities lie at bicharacteristic periods; under clean fixed geometry a local expansion and canonical leading density are obtained | The orbit information is local near a period and requires smooth Hamiltonian/PDO/FIO data; it is not a packet probability or a general global orbit sum | `PROVED`; A |
| `SEL` | A. Selberg, *Harmonic Analysis and Discontinuous Groups in Weakly Symmetric Riemannian Spaces with Applications to Dirichlet Series*, J. Indian Math. Soc. 20 (1956), 47--87, DOI [10.18311/JIMS/1956/16985](https://doi.org/10.18311/JIMS/1956/16985); [CERN bibliographic record](https://cds.cern.ch/record/427143) | Full article pp. 47--87; an acquired full source would be required before freezing a local cofinite normalization | Existence, author, venue, year, and page range verified from bibliographic metadata; original PDF not stored locally. The registered DOI endpoint returned HTTP 404 on 2026-08-13, while the CERN record remained available. Metadata verification is not full-text acquisition, so formula-level transcription must be cross-checked against an acquired full source, not guessed | Exact trace-formula source relating the same hyperbolic quotient's spectral and conjugacy-class data | The modular cofinite formula has identity, elliptic, parabolic/cusp, and continuous/scattering terms; a hyperbolic-only excerpt is not the full identity | source existence `PROVED`; local formula convention `NOT_TESTABLE`; A with locator caveat |
| `HEJ` | D.A. Hejhal, *The Selberg Trace Formula for PSL(2,R), Vol. 2*, LNM 1001, Springer (1983), DOI [10.1007/BFb0061302](https://doi.org/10.1007/BFb0061302) | Chapters 6--9; especially “Version B” and the spectral expansion for the cofinite case (publisher contents pp. 267ff., 316ff.) | Springer bibliographic record verified 2026-08-13; no local copy | Standard detailed derivation that could freeze the complete cofinite test-function convention and continuous spectrum after full-text acquisition | Authority source rather than the original 1956 article; no claim uses a page/formula not transcribed from an acquired copy | framework authority `PROVED`; local convention `NOT_TESTABLE`, acquisition pending before formula-level transcription |
| `KOR` | Yu. Kordyukov, *The Trace Formula for Transversally Elliptic Operators on Riemannian Foliations*, [arXiv:math/0001182](https://arxiv.org/abs/math/0001182) | pp. 1--3, assumptions (A1)--(A2) and Proposition 2; Definition 5, pp. 5--6; Theorem 6, pp. 6--7, eqs. (2.5)--(2.7) | [local PDF](../../2-flow-zeta/notes/sources/kordyukov_2000_transversally_elliptic_trace.pdf), SHA-256 `0d75baa55d4709725bc29f2b20078cc699d2045cb6105f64896f065425d71a9c`; text checked with `pdftotext` | A foliated relative wave trace still needs a compact smooth foliated manifold, transversally elliptic essentially self-adjoint operator, groupoid smoothing, and a clean relative fixed set | Demonstrates what positive-dimensional/relative fixed geometry requires; does not create those data from Deninger packet Haar probability | `PROVED`; A |
| `ALKL` | J.A. Álvarez López, Yu.A. Kordyukov, E. Leichtnam, *A Trace Formula for Foliated Flows*, [arXiv:2402.06671v2](https://arxiv.org/abs/2402.06671); Springer LNM 2387 (2026), DOI [10.1007/978-3-032-15413-2](https://doi.org/10.1007/978-3-032-15413-2) | Abstract; §1.1; §§1.3.1--1.3.10, especially Theorems 1.3.7--1.3.10; §4.1.1, printed pp. 99--100 | [local v2 PDF](../../2-flow-zeta/notes/sources/alvarez_kordyukov_leichtnam_2024_trace_foliated_flows.pdf), SHA-256 `b7037a1ee76b75ab215b9682d3cd570075c9e2b3fdb0fa08d272f6e807e4ed49`; arXiv version and current monograph metadata checked | Exact Lefschetz distribution from conormal/dual-conormal reduced leafwise cohomology with smoothing b-PDO/b-trace regularization, simple closed orbits, and transversely simple preserved leaves | Positive-dimensional terms are preserved leaves, while closed orbits are simple/isolated; the theorem does not cover a compact family of closed orbits in one packet | `PROVED`; A |
| `DZ` | S. Dyatlov and M. Zworski, *Dynamical Zeta Functions for Anosov Flows via Microlocal Analysis*, Ann. Sci. ENS 49 (2016), 543--577, DOI [10.24033/asens.2290](https://doi.org/10.24033/asens.2290); [Numdam](https://www.numdam.org/item/ASENS_2016__49_3_543_0/) | pp. 543--545, eqs. (1.5)--(1.6); §2.2, eqs. (2.4)--(2.5); Appendix B | [local PDF](../../2-flow-zeta/notes/sources/dyatlov_zworski_2016.pdf), SHA-256 `1ba0b0eaa826b785d9a2b9d2b4948c1e8309176a6ff8551ca624d1ef98e194ae`; text and metadata checked | Exact flat-trace orbit distribution for compact smooth Anosov flows, its normal determinant/primitive-period coefficient, and the microlocal route to Ruelle meromorphy/resonances | The generator on anisotropic spaces is not thereby a self-adjoint quantum Hamiltonian; the compact-manifold hypotheses do not directly cover the finite-area cusped modular surface | `PROVED`; A |
| `GUT` | M.C. Gutzwiller, *Periodic Orbits and Classical Quantization Conditions*, J. Math. Phys. 12 (1971), 343--358, DOI [10.1063/1.1665596](https://doi.org/10.1063/1.1665596); [INSPIRE record](https://inspirehep.net/literature/67627) | Abstract; article pp. 343--358 | Metadata and original abstract verified; no local PDF | Historical quasiclassical derivation: actions, conjugate/Maslov information, periods, and stability enter approximate spectral contributions | Original treatment is not the generic exact fixed-operator identity required here; rigorous hypotheses/remainder are taken from `CRR` | historical derivation `HEURISTIC/SEMICLASSICAL`; A for historical claim |
| `CRR` | M. Combescure, J. Ralston, D. Robert, *A Proof of the Gutzwiller Semiclassical Trace Formula Using Coherent States Decomposition*, Commun. Math. Phys. 202 (1999), 463--480, DOI [10.1007/s002200050591](https://doi.org/10.1007/s002200050591); [arXiv:math-ph/9807005](https://arxiv.org/abs/math-ph/9807005) | §2, assumptions (H.0)--(H.5), Definition 2.2, Theorem 2.3, eqs. (12)--(13) | Original full text checked in arXiv HTML on 2026-08-13; no local PDF | A smoothed regularized density of states has a periodic-orbit expansion modulo \(O(\hbar^\infty)\) as \(\hbar\to0\), with finite time support, compact energy localization, and nondegenerate or clean hypotheses | It is an asymptotic for a family \(\widehat H_\hbar\), not a global exact spectral identity for a single \(\hbar=1\) operator | `SEMICLASSICAL_ASYMPTOTIC`, theorem `PROVED`; A |
| `FRI` | D. Fried, *The Zeta Functions of Ruelle and Selberg. I*, Ann. Sci. ENS 19 (1986), 491--517, DOI [10.24033/asens.1515](https://doi.org/10.24033/asens.1515); [Numdam](https://www.numdam.org/item/ASENS_1986_4_19_4_491_0/) | Introduction pp. 491--494; definitions and Theorems 1--7 | [local PDF](../../2-flow-zeta/notes/sources/fried_1986_ruelle_selberg_i.pdf), SHA-256 `c603627f3754aa103714d0efcca1759a35c38d796619f0d761a6b1475b1e958c`; text checked | Exact relationships among Ruelle/Selberg-type zetas in hyperbolic/geodesic settings and the distinction between dynamical products and Laplace spectral information | Does not turn every Ruelle resonance generator into a self-adjoint quantum operator and does not alter the rational-prime support | `PROVED`; A |

### Project-internal proved source

`papers/1-classical-flow/notes/mathematical_results.md`, Theorem 1 and its
“disjoint atomic supports” corollary, proves that for the frozen modular clock

\[
\{r\ell_\gamma\}\cap\{k\log p\}=\varnothing.
\]

This is not an external citation and will be reproved in Stage 3 before it is
used.  It is the candidate-specific theorem that prevents an atomwise
clock-preserving fusion of the exact modular trace with the Deninger arithmetic
ledger.

## 4. Applicability matrix: what each framework actually certifies

| Framework | Analytic object and trace functional | Classical/fixed-set hypotheses | Extent and coefficient | Fixed self-adjoint spectral side? | `DEN-WITT-Z-FIN` | `MOD-GEO` | Exact non-implication |
|---|---|---|---|---|---|---|---|
| Duistermaat--Guillemin wave trace | positive self-adjoint elliptic order-one PDO \(P\), with real scalar principal symbol, on a closed manifold; an order-\(m\) input is normalized by its positive \(m\)-th root; \(\operatorname{Tr}e^{-itP}\) is a distribution | smooth Hamiltonian bicharacteristic flow; fixed set clean; symbol, half-density, Poincaré/Maslov data | singular support is contained in the period set; local expansion near a clean period; leading term integrates a canonical density (isolated case has the familiar normal determinant and phase) | **Yes**, for the specified \(P\); the orbit theorem is local information about its global wave trace | `NOT_APPLICABLE_HYPOTHESES_FAIL`: no finite-dimensional smooth cotangent/Hamiltonian/PDO object, clean fixed locus, or \(P\) | original compact-boundaryless theorem is not directly applicable to the cusped orbifold; Selberg supplies the exact cofinite framework | local singular germ or singular-support inclusion does not determine the full trace, smooth term, or arithmetic support |
| Selberg exact trace | automorphic Laplacian/regularized kernel for one hyperbolic quotient; equality of spectral and conjugacy-class distributions after testing | same quotient supplies geodesic flow and Laplacian; cofinite formula requires cusp/scattering and elliptic/parabolic accounting | exact global smoothed identity; hyperbolic coefficient is derived from primitive length, repetition, and stability; all non-hyperbolic terms remain | **Yes**, with continuous spectrum/scattering included rather than hidden | `NOT_APPLICABLE_HYPOTHESES_FAIL`: not a hyperbolic quotient and no associated Laplacian/source-defined transfer | **Applicable and strongest benchmark**, once one full cofinite convention is frozen | exactness does not turn quadratic-unit geodesic norms into rational primes; T7 still fails |
| ALKL foliated Lefschetz | induced action on conormal and dual-conormal reduced leafwise cohomologies; Lefschetz distribution defined through smoothing b-PDO and b-(super)trace limits | closed smooth \(M\), transversely oriented codimension-1 foliation, smooth foliated flow, simple closed orbits, transversely simple preserved leaves | exact distributional formula including zero/preserved-leaf and isolated repeated-orbit terms; coefficient \(\ell(c)\epsilon_c(k)\) follows from the setup | **No self-adjoint quantum spectrum is claimed**; the analytic ledger is cohomological/renormalized | `NOT_APPLICABLE_HYPOTHESES_FAIL`: packet is a family of periodic orbits, not a simple orbit or preserved leaf; required smooth/cohomological objects absent | no such foliation/cohomological object is frozen for `MOD-GEO`; Selberg remains the relevant certificate | a Deninger-motivated theorem is not automatically a theorem about Deninger's rational-Witt packet space |
| Ruelle flat trace / PR resonances | for generator \(P_V=(1/i)\mathcal L_V\), pullback of the flow propagator kernel to the diagonal (flat trace); meromorphic generator/resolvent on anisotropic spaces | compact smooth Anosov flow; nondegenerate normal return; wavefront pullback; orientability/sign hypotheses or replacements | exact scalar (\(k=0\)) positive-time orbit distribution \(\sum_\gamma T_\gamma^\#/|\det(I-P_\gamma)|\,\delta(t-T_\gamma)\); the form-bundle formula carries \(\operatorname{tr}(\wedge^kP_\gamma)\), and resonance statements retain their own domains/remainders | **No**, generally a non-self-adjoint resonance generator, not a quantum Hamiltonian | `NOT_APPLICABLE_HYPOTHESES_FAIL`: topological packet flow is not source-proved compact smooth Anosov and lacks a flat-trace kernel | original compact theorem does not directly cover the noncompact modular surface; compact hyperbolic surfaces are valid controls | exact classical flat trace and meromorphic resonances do not imply a fixed self-adjoint quantum trace or rational-prime ledger |
| Gutzwiller semiclassics (rigorous CRR form) | family \(\widehat H_\hbar=\operatorname{Op}_\hbar(H)\); regularized smoothed density \(\rho_A(E)\) | compact regular energy shell, bounded time support, discrete nondegenerate or clean periodic sets, observable/test hypotheses | asymptotic as \(\hbar\to0\), modulo \(O(\hbar^\infty)\) after smoothing; leading orbit term contains action, Maslov phase, primitive period, and \(|\det(I-P_\gamma)|^{-1/2}\) | Each \(\widehat H_\hbar\) may be self-adjoint under hypotheses, but the result concerns a **varying family**, not one fixed global spectrum | `NOT_TESTABLE`: no source-defined \(H\), quantization, energy shell, or \(\hbar\)-family | can be formulated for a suitable semiclassical Laplace family as a comparator, but exact Selberg is stronger for the frozen modular geometry | \(\hbar\downarrow0\) in a localized window is not \(\hbar=1\), \(E\to\infty\), globally and exactly |

## 5. Local contribution versus global trace: mandatory distinctions

| Question | Wave trace | Selberg | Foliated Lefschetz | Ruelle flat trace | Gutzwiller |
|---|---|---|---|---|---|
| Is a trace functional defined globally on a test space? | yes, from the fixed elliptic operator | yes, with regularization in the cofinite case | yes, as the constructed Lefschetz distribution | yes, as flat trace after wavefront control | yes for the smoothed regularized quantity at each \(\hbar\) |
| Is the periodic-orbit theorem a full global equality? | generally **no**: local singular expansion / Poisson relation | **yes** for the complete tested formula | **yes** under the full hypotheses and renormalizations | orbit-side flat trace is exact for positive times; resonance-side formulas retain stated domains/remainders | **no**: semiclassical asymptotic with energy/time localization |
| Can one certified orbit determine the trace? | no | no; every geometric and spectral term matters | no | no | no |
| Are smooth/zero/non-orbit terms fixed by the orbit germ? | no | fixed only by the full formula | fixed only by the full cohomological/b-trace construction | not by one orbit coefficient | no |
| Does the theorem itself supply rational primes? | no | no; it supplies hyperbolic conjugacy classes/norms | no | no | no |

The first row prevents a second confusion: a global trace distribution can be
well defined while the available periodic-orbit information about it remains
local.  The paper's smooth-ambiguity lemma concerns inference from orbit germs,
not the prior existence of the operator-defined distribution.

## 6. Same-object gate: provisional candidate matrix

This is a Phase-1 applicability baseline, not the final A3--A4 evaluation.

| Gate | `DEN-WITT-Z-FIN` | Evidence state | `MOD-GEO` | Evidence state |
|---|---|---|---|---|
| T0 one candidate/source lock | yes | `PROVED` by freeze | yes | `PROVED` by freeze |
| T1 classical primitive/repetition ledger | packet-level periods/completeness only; individual orbit multiplicity/phase/stability unavailable | mixed `PROVED` / `NOT_TESTABLE` | primitive/repeated hyperbolic geodesics, length, stability | `PROVED` |
| T2 trace functional and test class | absent | `NOT_TESTABLE` | complete cofinite Selberg framework established, but no local convention/test-class transcription | framework `PROVED`; convention-dependent field `NOT_TESTABLE` |
| T3 analytic object and domain | absent | `NOT_TESTABLE` | Laplace spectral decomposition plus scattering/continuous part | `PROVED` |
| T4 local/global and exact/asymptotic extent | cannot be stated | `NOT_TESTABLE` | exact global smoothed identity | `PROVED` |
| T5 coefficient provenance | period only; no trace coefficient | `NOT_TESTABLE` | hyperbolic coefficient derived from the same quotient | `PROVED` |
| T6 common clock/normalization | arithmetic clock fixed; trace normalization absent | partial / `NOT_TESTABLE` | standard arc-length clock fixed; exact Fourier/scattering normalization not locally transcribed | clock `PROVED`; convention-dependent field `NOT_TESTABLE` |
| T7 rational-prime arithmetic promotion | \(\log p\) packet/repetition support succeeds; trace weights fail | support `PROVED`, weights `NOT_TESTABLE` | standard repeated length support is disjoint from \(k\log p\) | `REFUTED` for the target arithmetic map |

Taking the first candidate's T7 period coordinate and the second candidate's
T2--T6 coordinates is forbidden: it fails T0, and the project-internal support
theorem shows that the two atomic clocks cannot be identified without a new
time change.

## 7. Source-verification limitations

1. The ARS PDF preflight sidecars in Stage 2 are `UNAVAILABLE` because `pypdf`
   is absent.  Local page counts were checked with `pdfinfo`; text PDFs were
   checked with `pdftotext`; the DG scan's theorem locator relies on the prior
   visual page audit.  No unavailable preflight is reported as `PASS`.
2. The original Selberg article is not stored locally.  Its registered DOI
   endpoint returned HTTP 404 on 2026-08-13, although the stable CERN metadata
   record remained available; bibliographic metadata is not a full-text
   manifestation.  Before any formula-level transcription, one acquired full
   source (Selberg or Hejhal) must be used to freeze the exact
   cofinite test class, Fourier convention, signs, and continuous-spectrum
   terms.  Until then, no equation number is assigned in this project.
3. The Hejhal locator currently comes from the publisher's contents/metadata,
   not a locally read copy.  It is an acquisition obligation, not fabricated
   coverage.
4. Gutzwiller's original paper supports the historical quasiclassical claim;
   theorem-level hypotheses and remainders are supported by CRR Theorem 2.3.
5. No source in this matrix proves that all quantizations of the Deninger flow
   are impossible.  The matrix proves only that the named theorems cannot be
   applied to the frozen source object with its current data.

## 8. Search stop rule and handoff

The source search stops here because every required semantic distinction has a
primary theorem source:

- local fixed-operator wave singularity: `DG`;
- exact same-geometry hyperbolic trace: `SEL`/`HEJ`;
- smooth foliated/cohomological Lefschetz distribution: `ALKL` (with `KOR` as
  the clean relative-wave comparison);
- classical flat trace and PR resonance architecture: `DZ`/`FRI`;
- rigorous \(\hbar\to0\) trace asymptotic: `CRR` (with `GUT` for provenance);
- arithmetic packet source: `DEN`.

The next phase should transcribe the selected formulae under one notation,
prove the smooth-ambiguity and clock-support lemmas, and run an independent
devil's-advocate check for overclaiming.  It should not expand the bibliography
unless a proof step reveals a named missing theorem.
