# Route-A batch review: C214--C218

Date: 2026-08-28
Source baseline locked by the packages: `077a098ac5811e465b69db71b5e6031a4827eb55`
Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`
Evaluator: `flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

## Batch outcome

This is a five-owner cross-subtype round.  Each manuscript closes one
source-native theorem package over its declared parameter family, including
the relevant singular or degenerate boundary.  The owners are a continuous
reset diffusion, a partition-valued genealogy, a singular celestial
Hamiltonian, a conservative geophysical PDE, and a Kelvin--Voigt spectral
PDE.  Their clocks, phase spaces, and normalizations are kept separate.

| ID | Frozen owner | Theorem-scale advance | Route-A tuple | final PDF SHA-256 |
|---|---|---|---|---|
| C214 | Brownian motion with fixed-point Poisson resetting and a separately killed search | exact free renewal propagator and stationary density; killed first-passage/survival transforms; all moment identities; unique positive reset optimum; zero-parameter boundaries | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` | `135989257553d59dadf4fbe2b31a2843c06a892a56b612fc1b9494289b8cde06` |
| C215 | partition-valued Kingman coalescent | all-`n` hypoexponential block transitions; projective genealogy and MRCA law; infinite-sample limit; exact total branch-length transform, moments, and CDF | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` | `a2ce47e6c601a153720c29b907e27d0aae56ffc6e383e04ce54f3853fa718a5c` |
| C216 | planar attractive Kepler Hamiltonian | all-energy conic/Runge--Lenz/action/scattering atlas; finite radial collision times; fixed-energy Levi--Civita configuration continuation; positive-dimensional strobe obstruction | `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` | `10b9769a1ef8be2a10ba6a1f9d8f55e271b8724124a93b7167ebbd64b571cf05` |
| C217 | constant-`f` rotating shallow water on `T^2` | complete three-channel Fourier projectors and unitary group; potential-vorticity split; shell multiplicities; finite-support periodicity criterion; noncompact/Schatten boundary | `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `de12b191d81c6d12fe1c58800cfcc9c95481d69d8d47dfea636d74036177c7d1` |
| C218 | Dirichlet Kelvin--Voigt wave | under/critical/overdamped root atlas; exact generator domain; Weyl singular sequence at the non-eigenvalue point `-1/b`; spectral-abscissa gap and unique optimizer; energy law | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `1d92dd1acfc9fd35d5f1622d32975dab9eac8a7de118624371b5d55eba623d97` |

Every package is `ROUTE_A_REJECTED`; every
`route_b_invocation_allowed` value is `false`.  These are source-mathematics
results and stopping certificates, not claims of a prime carrier, target
divisor, Euler factor, root number, automorphy, or Hilbert--Polya operator.

## Reproducibility and hostile audit

Each directory contains exactly 28 physical files: 27 content-addressed
payloads plus one self-excluded release manifest.  The final PDF equals
`paper/main_round2.pdf`, and the three retained revision hashes are pairwise
distinct.  Two fresh two-pass LuaLaTeX builds from each final source were
performed in independent temporary directories with the package's fixed epoch;
the resulting bytes matched each other and the released PDF.  Final logs had
no overfull/underfull boxes, undefined references, rerun diagnostics, missing
characters, or fatal errors.  `pdffonts` found every font embedded and
subsetted, extracted text retained the scope and Route-A boundary, and every
page was visually inspected.

| ID | checker assertions | SymPy checks | hostile rejections | evidence bytes | pages | embedded/subset font instances |
|---|---:|---:|---:|---:|---:|---:|
| C214 | 2,352 | 122 | 27 (26 repaired + 1 stale) | 126,708 | 3 | 19 |
| C215 | 3,408 | 379 | 27 (26 repaired + 1 stale) | 121,275 | 2 | 23 |
| C216 | 260 | 17 | 25 (24 repaired + 1 stale) | 24,384 | 2 | 21 |
| C217 | 10,568 | 20 | 11 (9 repaired-hash semantic/schema, including the unknown-key case; 1 stale-hash; 1 source-lock) | 320,749 | 3 | 18 |
| C218 | 7,620 | 11 | 11 (9 repaired-hash semantic/schema, including the unknown-key case; 1 stale-hash; 1 source-lock) | 200,063 | 3 | 16 |
| **total** | **24,208** | **549** | **101** | **793,179** | **13** | **97** |

The executable boundaries are independent: C214 checks 81 propagator, 27
stationary, 9 normalization, 108 first-passage, and 27 MFPT rows; C215 checks
312 transitions, 12 holding-time rows, 48 MRCA rows, 60 branch rows, and an
8-row partition ledger; C216 checks 10 conics, 4 radial collision cases, 12
Levi--Civita rows, and 5 fixed-set rows; C217 checks 392 Fourier blocks over
8 parameter faces; and C218 checks 384 roots over 6 damping cases.  Replay
regenerates the canonical evidence bytes in every package.  The finite ledgers
are regression certificates, not replacements for the written all-parameter
arguments.

## Content-addressed release ledger

| ID | semantic payload SHA-256 | evidence-file SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|
| C214 | `9e91c02b51efcae11c92aad31be609905eeca78881dd09a8931209730fe1c8e8` | `23788c3e811083a6b1bdb66a807dd99d31527fe3a92b90d1a6980d04c5b0c810` | `135989257553d59dadf4fbe2b31a2843c06a892a56b612fc1b9494289b8cde06` | `6aa1bfe98e003e3422b51c89dd4452068606f943755ec29c077f53da704505bd` |
| C215 | `15e1666cba6f7f7f97951730154b15c6a4fae8e72bada3a04f8e4573e7acd7a5` | `01635999cc616f51da46f7d127b0df665ac2fb719e05c08fd1803411a30674aa` | `a2ce47e6c601a153720c29b907e27d0aae56ffc6e383e04ce54f3853fa718a5c` | `4fd9df3b3278d02542761328361a4432810eabe00df9f75cc163af9f512d6c97` |
| C216 | `eeac27260e27d0b7dcd6d32fcfe72ccec8e5ce083c2ea1056a1b26c20c799225` | `7dc68924fe22c40bdababe055bf83b25f605ffbf9c16811bcceae9f5cc5fec55` | `10b9769a1ef8be2a10ba6a1f9d8f55e271b8724124a93b7167ebbd64b571cf05` | `6b70bd1b36086be01fa29725928aa2b9374719a98e9902119905eb44984f2fe3` |
| C217 | `343b9751ff140ab5fb0b3dd9a10b6e2e5d913c112e08c0b9b30b10cf051eeced` | `da1efda1cd05802616b904eb46dca3df0ba004da42c5e3099d934340ada8510c` | `de12b191d81c6d12fe1c58800cfcc9c95481d69d8d47dfea636d74036177c7d1` | `f909a015cc4b1f1c75719d7e2829441120d3f74f6dffd11fda11ac8bfcf48e2e` |
| C218 | `14fd04d1389be69d2f8868595210a627602c3a4f1a70f37ed1a43b6edb6ac1ca` | `f37c62fee2b5bc3a96ae54bb35a990d7ea15078ab41a986f162661106d50c239` | `1d92dd1acfc9fd35d5f1622d32975dab9eac8a7de118624371b5d55eba623d97` | `9c864a955dde57a882db77ec7c6a18437bc728a9dd3f5f4597b549446f5bca83` |

There are 135 payloads and 140 physical files across the five packages.

## Cross-review repairs

The internal read-only theorem and release cross-audits found and closed the
following issues.  These checks are not external peer review or novelty
certificates.

- **C214:** separated the free resetting process on `R` from the separately
  killed search on `(-infinity,a)`, made the fixed-time free law explicitly
  absolutely continuous (no reset-point atom), retained all `n >= 0` moment
  identities and boundary branches, corrected the optimal-reset DOI, and
  suppressed optional PDF trailer metadata for deterministic builds.
- **C215:** corrected the Artin--Mazur spelling and the coalescent source
  locator, proved the exact tree-length CDF through exponential order-statistic
  spacings, and separated projective restriction coupling from independent
  fixed-`n` marginal sums.  Optional PDF trailer metadata was suppressed after
  the independent-build audit.
- **C216:** fixed the action normalization
  `(1/(2*pi))` closed-cycle integral, made `T=mP(E)` a continuum fixed-shell
  statement, and kept physical collision incompleteness distinct from
  configuration-level Levi--Civita continuation.  A duplicate equation number
  was removed and the final two-page PDF/manifest were rebuilt.
- **C217:** corrected the author metadata, signed-`f` sentinel, `c >= 0`
  boundaries, maximal graph domain, principal-value convention, and
  all-time noncompactness statement.  The finite-support qualifier on
  periodicity and the zero-frequency branch remain explicit.
- **C218:** corrected all four source metadata records and strengthened the
  theorem with the exact generator domain, an explicit normalized Weyl
  singular sequence, a direct proof that `-1/b` is not an eigenvalue, and the
  distinction between a spectral-abscissa gap and a uniform norm-decay claim.
  Evidence, checks, PDF, and manifest were rerun after those changes.

## Integrity and scope audit

1. **Implementation bug gate: PASS.**  Every producer, independent checker,
   symbolic reconstruction, replay, mutation suite, and release manifest
   completed successfully after the final repair.
2. **Citation/source gate: PASS.**  Source ownership and DOI locators are
   recorded in each package; no priority, novelty, or external-review score is
   claimed.
3. **Result-faithfulness gate: PASS.**  Infinite quantifiers are supported by
   written derivations or explicitly delimited source theorems.  Finite rows
   remain regression evidence.
4. **Scope/firewall gate: PASS.**  No target prime or zero table, arithmetic
   local datum, Euler factor, root number, automorphy object, target divisor or
   functional equation, Hilbert--Polya operator, or Route-B input is used as a
   positive claim.
5. **Frame-lock gate: PASS.**  The five clocks remain diffusion time,
   coalescent time, physical Kepler time (with auxiliary regularization time
   only where stated), PDE time, and Kelvin--Voigt time; no operator or orbit
   ledger is transferred between packages.

## Completion decision

All five theorem packages, evaluator receipts, manifests, cross-review repairs,
registries, README index, deterministic PDF builds, page-level visual checks,
and scope controls are closed for this round.  The mathematical advances are
substantial within their own dynamical families, but all five remain strictly
`ROUTE_A_REJECTED` and Route B remains unauthorized.  The next action is a user
checkpoint before selecting C219--C223.
