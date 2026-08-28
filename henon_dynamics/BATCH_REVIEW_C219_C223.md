# Route-A batch review: C219--C223

Status: **RELEASE_COMPLETE**
Evaluation date: `2026-08-28`
Source/code baseline: `86c7bb8a39cdd1b8e941e45833b068170ca06287`
Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`
Evaluator authority: `flow_systems/skills/route-a-evaluator.md` v0.2.0,
SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

This round contains five independent Route-A owners.  Each owner makes one
theorem-scale advance in a different dynamical subtype; none of the five
coordinates is combined with another.  `NEW` in the batch means absent from
the workspace owner list, not a literature-priority claim.

## Theorem advances

| ID | dynamical owner | closed advance | finite receipt |
|---|---|---|---:|
| C219 | Rayleigh spherical-cavity collapse | First integral for all pressure signs, incomplete-Beta collapse clock, terminal (2/5) law, sharp wall-speed/acceleration (L^p) thresholds, volume and finite liquid-energy ledger, Lagrangian and (R_0=0,Pi=0) boundaries. | 13 parameter rows (5 collapse, 2 equilibrium, 3 expansion, 3 singular-boundary controls) |
| C220 | continuous-time open TASEP | Exact finite generator and irreducible stationary law, DEHP matrix product, closed (Z_L) with equal-rate divided-difference limit, uniform current, LD/HD/MC/coexistence/critical atlas including `CRIT_CORNER`, and all zero-rate absorbing faces. | 200 positive-rate rows, 40 boundary rows, (L\le 8), 9,575 interior states |
| C221 | one-dimensional focusing cubic NLS | Bright-soliton profile, mass/Hamiltonian/action/VK slope, both real Hessians, complete Pöschl--Teller discrete/essential spectrum, Morse index and symmetry kernels, scaled ladder factorization, and zero-frequency/defocusing/domain boundaries. | 15 profile, 3 integral, 15 spectrum, 15 factorization, 4 boundary rows |
| C222 | bounded double integrator | Whole-plane minimum-time synthesis with switching parabola, direct-brake and one-switch arcs, sharp reachable-moment interval, terminal identities, global optimality, HJB/Pontryagin checks, reflection/scaling and (a=0) boundaries. | 105 states: 3 origin, 8 direct-brake, 94 one-switch |
| C223 | Jaynes--Cummings atom--field model | Exact conservation of excitation, separate vacuum and every (2\times2) dressed block, spectrum/propagator/transition law, finite-support population-versus-state revival criterion, and coupling, resonance, cutoff and full-Fock operator boundaries. | 4 parameter cases, 32 blocks, 64 propagators, 4 vacuum and 7 boundary rows |

The detailed owner contracts and collision decisions are in
`IDEA_REPORT_C219_C223.md`; the per-paper proof/evidence boundaries are in
the five package `THEOREM_PACKAGE.md` and `SOURCE_AUDIT.md` files.

## Independent audit and release hashes

All five packages contain exactly 27 manifest-listed payload files plus one
self-excluded release manifest (28 physical files), with no LaTeX or Python
sidecars.  The producer, producer-independent checker, independent SymPy
reconstruction, clean-process byte replay, repaired-hash/schema mutation
suite, and release-manifest closure all pass.

| ID | checker assertions | SymPy checks | hostile rejects | final pages/fonts | evidence payload SHA-256 | evidence file SHA-256 | final PDF SHA-256 | manifest SHA-256 |
|---|---:|---:|---:|---:|---|---|---|---|
| C219 | 509 | 19 | 15 (14 repaired + 1 stale) | 3 / 17 | `2f3784efb8af4a5e929149eb1ddb6a5f0fe264147fff71b5c791ec1e8a16e0e9` | `67f73fb6cd7a25c6ac6bd8917f78fc42811b2533f1a9c897f5433c54438f38fd` | `bc6958a50b1cf9ce466c1ae0b0b08240306dd677afc552660356964993a7b5c0` | `423a66b69201617114fa32107a9754f1029285e9b879cbfe0154542887367175` |
| C220 | 3,597 | 576 (321 word) | 29 (28 repaired + 1 stale) | 3 / 18 | `82def8f1358aa47442bb4af9cdf412952f2cbe562d3ff0814e2f740a98ccf1ed` | `811f7238aa5b1f44dae8da54dcacbf84b4db699b65e47da9fb85dbb0ec558396` | `c68459c1d85934837d871cf1201c93923e5ac42b2aca784392c688030fe8f018` | `013f9116682f9dd25ca58f7ae76a3e0bc6e328e6b1a55b5f65cde69b97a8f997` |
| C221 | 497 | 19 | 17 (16 repaired + 1 stale) | 2 / 20 | `6ba5517350e15f833f1d099317c374630f0b857a33d7905446ec467f4b3bc02a` | `e7e065580c639b1a903e8afa6640fcc92d392414ff769cbc84ffd59032dbbb55` | `a03e7851eb02c4937c72289768edbb0591311176bc54705913d8beaac81624b4` | `61ffdc85a88ac94ddf9c78c2e88276a72010e940c3483c0c97c0449ac76e2d9c` |
| C222 | 2,278 | 125 | 24 (23 repaired + 1 stale) | 3 / 14 | `5089209bbb8ff78167efe4005c974b1e06b139914c04370ce631540e391db5a0` | `f2b41252efa5b45c47c749da79c5139b81285640e0d5726d308164d5c8c76612` | `7461145393e71f9517e9af55642b1b9f3207981ccc57a2389e5731c540ef16ee` | `545887a9ceccdee51e48abf82a4f01851dbdd8ab18375c11cd69b59b4f16def2` |
| C223 | 1,100 | 109 | 25 (24 repaired + 1 stale) | 3 / 16 | `a6e6b23fe5b6a65c84827096443135ba7624e54fb5955adf4008d6eaf85b688c` | `ac6f6bc8f6ae3fbf4dbae6aa6212e280f403d1a8c9af9b63f61e079dbfe9f848` | `8324bfc2b4f99789df484bd14485f724d27762498cdcfe30d63034f92c459c98` | `1f2911baee4048cc6e14f8d2b51392eaa0a986684d6529855a77eb52b3e75b5c` |

Aggregate totals are 7,981 independent-checker assertions, 847 SymPy
checks, 110 hostile rejections, 135 payload files (140 physical files), and
14 final-paper pages.  The C220 positive-rate coexistence condition is
explicitly (0<\alpha=\beta<1/2); its ((0,0)) endpoint is reserved for
the absorbing zero-rate theorem.

The three content-distinct revision PDF hashes, in round order, are:

- C219: `ae94633ed900d09260958c795c7c22b8da53bea376717e90ea5c6ff75cecaeec`,
  `ce252f5f404dc2d724e070acfba9bdc0fdb0ff2e0a9f872d4d3c7c11a3361bdc`,
  `bc6958a50b1cf9ce466c1ae0b0b08240306dd677afc552660356964993a7b5c0`.
- C220: `77ec4659b233d57ac6a518ce258b5ed5dcfb6905c416666c9ea4642c5847b13a`,
  `cbf78443fb0f9465852d484770249981e8e9a1946f39a4b36d26a1003adabf69`,
  `c68459c1d85934837d871cf1201c93923e5ac42b2aca784392c688030fe8f018`.
- C221: `a570aa76357fc22cc7c0450413dcf64d1506d82fde9f96ae273aa2ca3b504e9a`,
  `ac62e4a1e983501385a408bc9f8c8c191e8f5ac81f969b0553f2a1b757e5c5f6`,
  `a03e7851eb02c4937c72289768edbb0591311176bc54705913d8beaac81624b4`.
- C222: `d7709379b2c6e7d2b53d5689a1ab747be4f1b509486a283ef49523ed0a16414d`,
  `9702ded9a7e53848250ad59900fe9e259b78d3734be21caad5dee423d476ab25`,
  `7461145393e71f9517e9af55642b1b9f3207981ccc57a2389e5731c540ef16ee`.
- C223: `8b4d7d8a7b45bfde1a83fe0600038b1a8c00f3a87de3f8868a7eb083ce254abd`,
  `f4b169233883f4fe7cc17a11a29af0cfb89a3118182ca27dcb4ee243fe72fa9d`,
  `8324bfc2b4f99789df484bd14485f724d27762498cdcfe30d63034f92c459c98`.

For every paper, `main.pdf` equals round 2 byte-for-byte and the three round
hashes are pairwise distinct.  Ten fresh output-directory builds (two final
builds per package) reproduced the release PDFs byte-for-byte.  Fixed
`SOURCE_DATE_EPOCH=1787875200` LuaLaTeX builds have clean settled logs,
extractable text, and every reported font is embedded and subsetted.  A
page-by-page visual pass covered all 14 final pages and found no clipping,
overlap, or unreadable formula.  Internal cross-review and hostile tests are
artifact checks, not external peer review.

## Route-A decision and scope boundary

The final strict tuples are:

| ID | tuple | overall | Route B |
|---|---|---|---|
| C219 | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` | false |
| C220 | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` | false |
| C221 | `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` | `ROUTE_A_REJECTED` | false |
| C222 | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` | false |
| C223 | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` | `ROUTE_A_REJECTED` | false |

The A4 labels are source-local formal or natural-quantization hints only.  No
package introduces target-zero or prime tables, arithmetic local data, Euler
factors, root numbers, automorphy, a target divisor/counting law or functional
equation, a Hilbert--Pólya operator, or Route-B input.  These negative claims
are enforced in each evaluator record and evidence schema; they are not a
claim that the source systems lack their ordinary classical mathematics.
