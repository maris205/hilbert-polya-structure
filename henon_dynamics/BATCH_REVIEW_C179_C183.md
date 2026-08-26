# Batch review: HCS-C179--HCS-C183

Date: 2026-08-26

Source commit: `bbb809ee198bc9ad5f196383baab1e3d9de38e43`.

Evaluator authority: `flow_systems/skills/route-a-evaluator.md` version 0.2.0, SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Common scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain all five independent source theorems and their exact stopping results; promote C179 only to Route-A exploratory status, keep C180--C183 rejected, and leave Route B unauthorized.**

## Completed paper outputs

### C179 -- Zsigmondy congruence first-return tower

For every coprime (a>b\ge1), C179 turns primitive rational-prime divisors into an intrinsic dynamical predicate. For (p\nmid ab), the prime (p) is a primitive divisor of (a^n-b^n) exactly when (1) first returns at time (n) under multiplication by (ab^{-1}\pmod p). The package attributes the Bang--Zsigmondy existence theorem and its exact exceptions, then proves the full prime-power clock lift: if (e=v_p(a^n-b^n)),

\[
\operatorname{ord}_{p^k}(ab^{-1})=np^{\max(0,k-e)}.
\]

Every admissible finite fibre receives its complete cycle census, fixed iterates, zeta, finite Koopman determinant, root-of-unity spectrum, and inversion reversor. The theorem then exposes a genuine owner ambiguity rather than hiding it. The natural disjoint union has

\[
\#\operatorname{Fix}(T^n)=a^n-b^n,
\qquad
\zeta(z)=\frac{1-bz}{1-az},
\]

whereas the natural profinite inverse limit has no positive-time fixed point and zeta (1). The first-return arithmetic relation is real, but the fibre theorem does not select a unique global phase space; its clock is (n), not (log p), and no prime-weighted global determinant is inserted.

### C180 -- Lattès three-channel Lefschetz collapse

For every complex elliptic curve, every (m\ge2), and every (n\ge1), let (a=m^n) and let (h=1) for even (a), (h=4) for odd (a). The quotient by (P\sim-P) has the exact channel census

\[
N_+=\frac{(a-1)^2-h}{2},\qquad
N_-=\frac{(a+1)^2-h}{2},\qquad
N_{\rm br}=h,
\]

with multipliers (a,-a,a^2), respectively. Thus

\[
\#\operatorname{Fix}(L_m^n)=m^{2n}+1,
\qquad
\zeta_{AM}(z)=\frac1{(1-z)(1-m^2z)}.
\]

The stronger source result is the exact all-moduli Lefschetz cancellation

\[
\frac{N_+}{1-a}+\frac{N_-}{1+a}+
\frac{N_{\rm br}}{1-a^2}=1.
\]

Exact periods and primitive cycles follow by Möbius inversion. For quotient-Haar measure, the natural Koopman isometry on (L^2(\mathbb P^1,\nu)) has Wold model (I_{\mathbb C}\oplus S^{(\aleph_0)}); the even-Fourier double-cover description is its proof model, not a different dynamical owner. The three-channel branch theorem prevents the paper from collapsing into C177's one-dimensional degree count; prime and composite (m) nevertheless obey the same generic formula, so A0 fails.

### C181 -- rotor-router on all strongly connected digraphs

Let (t_v) count in-arborescences rooted at (v), let (d_v^+) be outdegree, and define

\[
M=\gcd_v t_v,
\qquad
L=\frac1M\sum_v d_v^+t_v.
\]

For every finite nonempty strongly connected directed multigraph, including loops and distinguished parallel arcs, and for every cyclic rotor order, C181 proves that the recurrent unicycle phase space consists of exactly (M) orbits of exact length (L). During each orbit, vertex (v) is visited (d_v^+t_v/M) times and every distinguished arc leaving (v) is traversed (t_v/M) times. Consequently

\[
\#\operatorname{Fix}(R^n)=ML\,\mathbf1_{L\mid n},
\quad
\zeta_R(z)=(1-z^L)^{-M},
\quad
\det(I-zU_R)=(1-z^L)^M.
\]

Every (L)-th root occurs with multiplicity (M), and the Eulerian case reduces to (L=|E|). The package keeps a hard firewall from C176: this is sinkless chip-and-rotor traversal, not stabilization or critical-group translation.

### C182 -- periodic box--ball action--angle classification

C182 closes the highest-risk candidate without shrinking it. For every (L\ge2M), every soliton content, every internal-symmetry sector, and every commuting carrier evolution (T_\ell), the periodic inverse-scattering coordinates give a finite lattice quotient

\[
\mathbb Z^H/F_\alpha\mathbb Z^H,
\qquad
T_\ell:I\longmapsto I+h_\ell,
\qquad
(h_\ell)_j=\min(j,\ell).
\]

The exact component period is the least (r>0) with (rh_\ell\in F_\alpha\mathbb Z^H), computed from the Smith normal form of the augmented lattice. Internal-symmetry multiplicities, including the (p_{\max}=0) boundary, aggregate every component back to the complete fixed-mass state count. The package then derives all fixed iterates, exact periods, primitive cycles, zeta, and finite Koopman determinant simultaneously for the whole commuting family. Vacuum and (\ell\ge\max H) are explicit. Soliton lengths and vacancy numbers remain integrable source data, not rational-prime carriers or a logarithmic prime clock.

### C183 -- random-transposition full partition spectrum

For the lazy ordered-pair transposition chain on every (S_n), each partition (lambda\vdash n) contributes

\[
\beta_\lambda=\frac1n+\frac1{n^2}\sum_i
\bigl(\lambda_i^2-(2i-1)\lambda_i\bigr)
\]

with regular multiplicity (d_\lambda^2). One complete ledger yields

\[
\det(I-zP_n)=\prod_{\lambda\vdash n}
(1-z\beta_\lambda)^{d_\lambda^2},
\qquad
\operatorname{Tr}(P_n^k)=\sum_\lambda d_\lambda^2\beta_\lambda^k,
\]

the exact identity-return probability, ordered-pair return-word count, (L^2) density distance, bottom eigenvalue (-1+2/n), and spectral gap (2/n). Zero sectors contribute unit determinant factors, so the actual polynomial degree is their nonzero total multiplicity rather than automatically (n!). On frozen (S_n), (P_n) is not induced by a deterministic map and its determinant is not an unweighted Artin--Mazur determinant. On the changed weighted directed-edge path space, its reciprocal has a canonical primitive-cycle product; that lift changes owner and carries no A0 arithmetic payload, so A1 remains `A1_FAIL`.

## Strict Route-A record

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C179 | `A0_WEAK_ARITHMETIC_RELATION` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_EXPLORATORY` |
| C180 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C181 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C182 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C183 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |

C179 is the only A0 advance. Its coordinate cannot borrow C181/C182's finite unitaries, C180's holomorphic cancellation, or C183's self-adjoint spectrum. Every `route_b_invocation_allowed` value is false.

## Uniform release audit

| paper | checker assertions | SymPy checks | hostile rejections | payload closure | PDF pages |
|---|---:|---:|---:|---:|---:|
| C179 | 320,291 | 6,674 | 65/65 | 27/27 | 3 |
| C180 | 43,184 | 18,065 | 24/24 | 27/27 | 3 |
| C181 | 93,786 | 24,890 | 26/26 | 27/27 | 3 |
| C182 | 55,907 | 38,979 | 65/65 | 27/27 | 4 |
| C183 | 2,597 | 2,427 | 58/58 | 27/27 | 2 |
| **total** | **515,765** | **91,035** | **238/238** | **135/135** | **15** |

Every final package contains exactly 27 content-addressed payloads and one self-excluded manifest. Checkers do not import producer implementations. Separate SymPy paths reconstruct headline identities. Canonical replay binds released evidence bytes. Semantic mutations repair payload hashes before rejection; stale-hash attacks are separate.

All five manuscripts preserve three pairwise-distinct drafting rounds with `main.pdf == main_round2.pdf`. Fresh fixed-epoch builds reproduce each released final byte for byte, listed fonts are embedded/subset, final logs are clean, and rendered pages have been inspected. Classical citations are source-locks, not external reviews or novelty certifications.

## Content-addressed release ledger

| paper | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|
| C179 | `0a756181a775171a6c7de06afced94a75d835cd265d14f38ab825c1119525066` | `caba3bffcd0b1081f7fd93d1660cf3b317f994e96cb975f7d34ae6795f3d5374` | `ff3ca3a2b8008eef68efe4a2f3da192268e1bad4bce9a5d939f3e29645d101a5` |
| C180 | `1a059d8843579bc893bf3460117434fa828d46a294cda6a18e7a298b02ca82ec` | `ed64388d59e5717f588ec6b750c079eeb3aa99df4879236d2bb18ea3fb6c4a93` | `592e407bdb355ff7e891d50eca52adc2791ff707b0ac2494b96740b33ddd55b4` |
| C181 | `48f5f825d26909aa6998dc45f4192e86a2e36bd3c95906c7d66dbb00b0079754` | `7db8d34f3107f78dcfe7dbcff63b2f422dc48b0f8c18a23df0fb1281edd1e617` | `71c4d0e2bf12e6c04f4116391b818af0b995a2d305891d9e16622bec2ef776ae` |
| C182 | `d35fa9b5a4f5577498aa016ef0773d708f8628c7cc82aefa7fbc58137c9a096f` | `3cc392c7ebbd40c72920054aeef3ac0b71559b255b3cecccd9daecac066acbfc` | `0f971c9fff10af66d12580be2542662f050ed54b49aa865558afd70a5f51121b` |
| C183 | `99bf7c1e245c929095a98db1e68523716abf77d7b5e0c0e0556227b981a77766` | `adb2790ddb8044151177f7b30ef93b2bc3dcc10ad3bf2ad62e8128ac569fc319` | `4568d2b0cd5f4a75dbb67d94b7954a1c66c4a82d8a8edca3362690e4b419a78f` |

## Internal cross-review and repair ledger

These are evidence-anchored internal theorem, scope, and release audits. They are not external peer review and do not claim reviewer or error-process independence.

- **C179:** classical Zsigmondy ownership is explicit. The global stopping claim was narrowed from absolute nonexistence to the proved nonuniqueness of two natural owners; a prime-weighted union or (log p) roof remains forbidden extra modeling. The checker now exact-matches the attribution, theorem, Route-A, scope, and integrity ledgers; four appended repaired-hash attacks reject novelty, logarithmic-clock, target-operator, and absolute-owner escalations.
- **C180:** branch parity, channel intersections, three multipliers, and the Lefschetz identity are inseparable from the fixed count. The natural quotient-Haar Wold theorem is proved through the even-Fourier double-cover model and is not used to erase the orbifold branch data. The evaluator record and evidence were upgraded to the complete Route-A v0.2 source-lock and artifact contract.
- **C181:** directed-tree orientation, loops, distinguished parallel arcs, arbitrary rotor orders, visit frequencies, and the Eulerian edge count are all checked. A hostile review caught the gap in deriving first return from flow balance alone: Pham's exact orbit-size theorem now supplies the length/count step before flow balance derives local frequencies. Abstract orbit reversors require noncanonical cycle basepoints; no source-canonical reversal is claimed. The manuscript's first visual pass also caught and repaired title clipping. Sandpile vocabulary is excluded from the owner theorem, and the evaluator/evidence records now meet the complete Route-A v0.2 contract.
- **C182:** the highest-risk generic-period shortcut was rejected. Internal symmetries, sector multiplicities, (p_{\max}=0), vacuum, large carriers, and augmented-Smith order are present before aggregation; every level sums back to its exact state count. A stale prior-round source commit was found and corrected throughout the producer, checker, evidence, evaluator record, and manifest before release.
- **C183:** development caught the false assumption that (deg\det(I-zP_n)=n!) even with zero eigenvalues. The theorem, producer, checker, SymPy path, evidence, and paper now distinguish ambient dimension from nonzero determinant degree. The hostile audit also rejected the overbroad assertion that no primitive factorization exists after changing phase space: the weighted path owner has a canonical primitive-cycle product, but it is not frozen (S_n) and supplies no A0 payload. Control-character corruption, manifest provenance omissions, factor/cutoff checker blind spots, and five named semantic attacks were repaired across the release.

## ARS Stage 2.5 failure-mode audit

1. **Implementation bug passing self-review: CLEAR.** Five independent checkers, five symbolic paths, byte replays, repaired-hash mutations, direct small-system dynamics, and edge-case controls agree with final evidence.
2. **Hallucinated citation: CLEAR.** Classical theorems are tied to verified source records; no citation supplies a package result by title association alone.
3. **Hallucinated result: CLEAR AT PROOF LAYER.** Every all-parameter headline has a written proof or an explicitly attributed source theorem plus a proved package-level consequence. Finite scans remain sentinels.
4. **Shortcut reliance: CLEAR.** No finite cutoff proves an infinite theorem. Generic box--ball periods, bare Lattès counts, and fitted prime roofs were explicitly rejected.
5. **Bug reframed as insight: CLEAR.** The C183 determinant-degree bug and overbroad no-factorization statement were repaired across all artifacts; neither was promoted as an insight.
6. **Methodology fabrication: CLEAR.** Every producer, checker, SymPy, replay, mutation, build, font, visual, and manifest procedure is executable and artifact-bound.
7. **Frame-lock: CLEAR.** C179's weak A0 is not upgraded by another candidate's A1--A4 data, and no positive finite unitary repairs a failed arithmetic or determinant gate.

## ARS Stage 4.5 post-manuscript audit

The seven modes were repeated against the final PDFs, evaluator YAMLs, evidence bytes, and manifests. Clocks and determinant conventions remain source-specific: congruence return, elliptic quotient iteration, one rotor step, one carrier evolution, and one random ordered-pair draw are never merged. Corrections that changed bytes triggered evidence/PDF/manifest regeneration. All papers retain limitations, nonclaims, declarations, and source ownership.

No target zero or prime census, target divisor, target functional equation/counting law, arithmetic local datum, Euler factor, root number, automorphy object, Hilbert--Pólya operator, or Route-B input appears as an affirmative package claim.

## Batch conclusion

The batch makes five separate large advances. Most important for the roadmap, C179 moves A0 from failure to a weak intrinsic relation: rational primes appear as first-return moduli without a prime table. The same theorem also proves why that relation is not yet a Route-A determinant candidate. C180--C183 contribute large exact source theorems and sharper controls, while independently showing that holomorphic cancellation, deterministic graph tours, integrable action--angle tori, and complete stochastic spectra do not by themselves supply the missing global arithmetic owner and clock.
