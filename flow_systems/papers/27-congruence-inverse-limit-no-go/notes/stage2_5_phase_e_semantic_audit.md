# Paper 27 — Stage 2.5 Phase-E semantic audit

Audit date: 2026-08-29 UTC  
Audit role: independent read-only Phase-E semantic reviewer  
Surface: stable selected claims in `notes/stage2_5_claim_registry.json` and their persisted tuples in `notes/stage2_5_evidence_rows.json`  
Route scope: Route A only; Route B remains unauthorized

## Disposition

**Phase-E semantic verdict: PASS for all 70 selected distinct claims.** Each selected claim was checked at its exact registered UTF-8 manuscript span against its definition/theorem/proof chain, exact artifacts and tests where applicable, the documented official-source Phase-A/B audit for source-dependent statements, and the explicit limitations separating the residual candidate from the homology-cover calibrator. The result is **70 VERIFIED, 0 MINOR_DISTORTION, 0 MAJOR_DISTORTION, 0 UNVERIFIABLE_ACCESS, and 0 UNVERIFIABLE**.

This report is a Phase-E semantic subaudit. It does not supersede the overall Stage-2.5 gate or resolve the separate scholar-owned experiment-intake blocker `P27-S25-F001` recorded in `stage2_5_independent_audit.md`.

## Frozen input and audit method

The audit used `BATCH_ROUND9_STAGE2_5_INPUT_FREEZE.json` (SHA-256 `7f50da159c5e8b5f3eefee83979279cc39140574f105ce18d2fd33eac0f8a0cb`, frozen `2026-08-29T01:13:20Z`). A post-report byte check reproduced every Paper-27 frozen hash:

| Frozen object | Expected and observed SHA-256 | Result |
|---|---|---|
| `paper/manuscript.tex` | `c2809011a722b81732952d889f194549adea58875b605dbafe58ada93de9b4b9` | unchanged |
| `paper/references.bib` | `32307e53e52ca8c11f039c0b0609bc7c24f3c2fa4ecedd7d9e3eb9be4a158981` | unchanged |
| `paper/paper.pdf` | `540403e2cfb3c893822f3bcb80fb56e33bff00970f340df3dc9e6e8d2810d65a` | unchanged |

The registry remained SHA-256 `05455f35794381fc5f472baaa56cdd2fedaf3d3cbdb99f58f344364c26893452`; the evidence-row sidecar remained `2f47adea1276a72469fddd8c1ee666796e2b73dcd388acc986c9088756be0496`. All 77 registered byte spans replay exactly against the frozen manuscript. The official registry-coverage validator and evidence-row validator both pass.

Evidence abbreviations used in the ledger are:

- **M** — exact registered span plus the complete written definitions, theorems, proofs, candidate firewalls, and limitations in the frozen manuscript.
- **A4/A5/A7/A8** — exact principal-congruence diagnostics, closed residual/homology control, fixed-prefix certificate, and Round-8 homology-renormalization artifacts.
- **T** — 58/58 historical tests plus Round-8 verify-default, 12/12 tests and two byte-identical builds with core SHA-256 `a1b588724dacb2ab2986326a7a5e1c6aec654c61538c1465e26564357b568b33`.
- **S** — the documented Phase-A/B official-source audit, independently cross-read at the concrete locators below.
- **R** — the Route-A evaluator definitions cross-read against both declared tuples, the owner firewall, and the proves-too-much controls.

Key exact artifacts were re-hashed: Round-8 freeze `88d10c3dcdee3387b16414d2c56d4934b6daeef6728acc689855049840850a72`; locked Round-5 ledger `0c74333b63f6027b16d134f19a320b8148e7fab6f86fa204d213c801106fe825`; validation `afdc51ca7ecfbd8777955c7438f08d4580e6b924419a807191e097b0292d9c10`; Round-8 code `56002ae3e8e2d3d97ff5851a5f9fa820ae4ec131cf17b9488b6c2cc6016ac8d8`; tests `0ca6c3ffd4950b2de8aacfd50afd975e9eb1b823eb32d319c4f4a501bf4e603d`; reproduction script `10b94bdbaf598469f07d9dd4fa492a89b4a7bd6bdbb5e91527c9567d91c1ebaf`; summary `c482c0e48fb1036faed37f123fbdec0b1c54f757a75f35e8a24cee27cb242b1a`; coefficient ledger `63f9632a0a715be26545e645a0f1d238e3ff24baec70fd8f478f1eda6c12c132`; and quadrant ledger `879ce8aec4e041e7cbba947706319511d99bb72592421584e76bbe47fad5ae57`.

## Counts by tier and verdict

| Selection tier | Selected distinct claims | VERIFIED | MINOR_DISTORTION | MAJOR_DISTORTION | UNVERIFIABLE_ACCESS | UNVERIFIABLE |
|---|---:|---:|---:|---:|---:|---:|
| HIGH-IMPACT | 67 | 67 | 0 | 0 | 0 | 0 |
| RANDOM | 3 | 3 | 0 | 0 | 0 | 0 |
| TOP-UP | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total selected** | **70** | **70** | **0** | **0** | **0** | **0** |

The registry contains 77 claims. Seven are explicitly `NOT-SELECTED`: `P27-E1-002`, `P27-E1-003`, `P27-E1-007`, `P27-E1-024`, `P27-E1-040`, `P27-E1-057`, and `P27-E1-067`. They are outside the stable selected population and receive no implicit Phase-E verdict here.

## Selected-tuple coverage

The canonical tuple key is `(claim_id, selection_tier, ref_slug-or-null)`. Source-bearing claims expand to one tuple for each registered source.

| Coverage check | Expected | Persisted/audited | Result |
|---|---:|---:|---|
| Selected distinct claim IDs | 70 | 70 | exact set; 100% |
| Internal claim tuples | 66 | 66 | exact set and order |
| Source-bearing claim IDs | 4 | 4 | exact set |
| Source tuples on those claims | 5 | 5 | exact `(claim_id, ref_slug)` set |
| All selected tuples | 71 | 71 | exact set and order; 0 duplicates |
| Persisted row verdicts | 71 VERIFIED | 71 VERIFIED | consistent with the distinct-claim audit |

The source expansion is `P27-E1-008 × {martinez2016}`, `P27-E1-009 × {penner2008}`, `P27-E1-010 × {alcalde2026}`, and `P27-E1-011 × {hurder2019, nica2013}`.

## Official/author-source locators for the source-bearing claims

The strings below are optional, human-facing exact-excerpt candidates of no more than 25 words. They are not inserted into the evidence-row sidecar and do not convert an anchorless row into a source-bound receipt.

| Claim / `ref_slug` | Concrete official or author locator checked | Exact-excerpt candidate (≤25 words) | Semantic result |
|---|---|---|---|
| `P27-E1-008` / `martinez2016` | [Official AIMS article](https://www.aimsciences.org/article/doi/10.3934/jmd.2016.10.113) and [author-uploaded arXiv v4 full text](https://arxiv.org/pdf/0711.2307), §2.2 pp. 2–3, Example 4 p. 12, Example 6 pp. 15–16 | “A small twist yields a more general example which is similar in spirit, but without periodic orbits for the geodesic flow.” | Supports the leafwise framework and explicit aperiodic example; Example 6 separately supports simply connected leaves; VERIFIED. |
| `P27-E1-009` / `penner2008` | [Official Springer article](https://link.springer.com/article/10.1007/s10711-007-9226-9) and [author-uploaded arXiv full text](https://arxiv.org/pdf/math/0508476), Introduction pp. 1–2, Definition 2.1 and following paragraph | “Each leaf is homeomorphic to the unit disk and is dense in H.” | Supports the inverse-limit punctured-solenoid setting and disk-leaf statement; VERIFIED. |
| `P27-E1-010` / `alcalde2026` | [Official EMS Press article](https://ems.press/journals/ggd/articles/14299725) and [author-uploaded arXiv v2 full text](https://arxiv.org/pdf/2411.18418v2), Definition 4 p. 7, Definition 5 p. 8, Definition 7 and tower setup pp. 12–14 | “The geodesic flow g_t is the flow on Y for which all leaves are invariant” | Supports the leafwise geodesic-flow and solenoidal object terminology; the factorial propositions remain local; VERIFIED. |
| `P27-E1-011` / `hurder2019` | [Official AMS article](https://www.ams.org/tran/2019-371-07/S0002-9947-2018-07339-1/) and [author-uploaded arXiv full text](https://arxiv.org/pdf/1702.03032), p. 17, Definition 5.5 and following paragraph | “is naturally identified with the fundamental group” | Supports only the compact weak-solenoid structural comparison; VERIFIED. |
| `P27-E1-011` / `nica2013` | [Author-uploaded arXiv full text](https://arxiv.org/pdf/1306.2385), p. 1, displayed Malcev theorem and following definition | “A finitely generated linear group is residually finite.” | Supports the residual-finiteness premise for the closed surface group; VERIFIED. |

## Per-claim semantic ledger

Every selected distinct claim is listed exactly once. “VERIFIED” applies only at the scope and owner declared in the registered text.

| Claim | Tier | Exact locator | Proof/evidence chain checked | Verdict |
|---|---|---|---|---|
| `P27-E1-001` | HIGH-IMPACT | L47–L48 | M+A4+A5+A7+A8+T+R: abstract no-go, prefix escape, exact cover formulas, quadrants, finite/generic boundary, and Route exclusions all agree. | VERIFIED |
| `P27-E1-004` | HIGH-IMPACT | L66 | M: normality, residuality, and one common clock prove no inverse-limit period and quotient-order escape. | VERIFIED |
| `P27-E1-005` | HIGH-IMPACT | L68 | M+A8: deck order `N`, `N³` lifts, clock and logarithmic renormalizations yield exactly the stated four behaviors. | VERIFIED |
| `P27-E1-006` | HIGH-IMPACT | L70 | M+S+A4+A5+A7+A8: prior mechanisms and the paper's bounded local contributions are accurately separated. | VERIFIED |
| `P27-E1-008` | HIGH-IMPACT | L76–L79 | S+M: Martínez–Matsumoto–Verjovsky support the leafwise framework, explicit aperiodicity, and simply-connected-leaf example; novelty is not claimed. | VERIFIED |
| `P27-E1-009` | HIGH-IMPACT | L81–L84 | S+M: Penner–Šarić support the inverse-limit punctured solenoid and disk leaves; the manuscript distinguishes its factorial chain. | VERIFIED |
| `P27-E1-010` | HIGH-IMPACT | L86–L89 | S+M: Alcalde Cuesta et al. support leafwise flow, finite-type objects, and McCord terminology, not the local factorial-chain theorems. | VERIFIED |
| `P27-E1-011` | HIGH-IMPACT | L91–L96 | S+M: Hurder–Lukina support the group-chain/leaf comparison and Nica states Malcev residual finiteness; the congruence case still receives a direct proof. | VERIFIED |
| `P27-E1-012` | HIGH-IMPACT | L98 | S+M: general mechanisms are prior, exact owner audits are local, and a negative literal-chain search is not presented as novelty proof. | VERIFIED |
| `P27-E1-013` | HIGH-IMPACT | L102–L111 | M: descending normal finite-index residual tower, inverse limit, tangent maps, and common unit-speed clock are consistently defined. | VERIFIED |
| `P27-E1-014` | HIGH-IMPACT | L113–L115 | M: a periodic owner requires one coherent point and one common `T`; level-dependent closing times are correctly excluded. | VERIFIED |
| `P27-E1-015` | HIGH-IMPACT | L122–L129 | M: residual-tower theorem correctly states no periodic point, forward divisibility, and divergence for every infinite-order owner. | VERIFIED |
| `P27-E1-016` | HIGH-IMPACT | L131–L140 | M: compatibility gives conjugators, normality removes them, and trivial intersection contradicts a fixed nontrivial hyperbolic power. | VERIFIED |
| `P27-E1-017` | HIGH-IMPACT | L142–L143 | M: quotient bonding gives `o_n(g) | o_{n+1}(g)`; bounded divisibility would stabilize and contradict infinite order plus residuality. | VERIFIED |
| `P27-E1-018` | HIGH-IMPACT | L145–L149 | M: for primitive `g`, the cyclic axis stabilizer gives minimal lift period `o_n(g)ℓ(g)`; uncertified rows retain weaker loop-closing language. | VERIFIED |
| `P27-E1-019` | HIGH-IMPACT | L153 | M: fixed-level closure and a single inverse-limit return are correctly separated by their quantifier order. | VERIFIED |
| `P27-E1-020` | HIGH-IMPACT | L155 | M: the level-dependent conjugator explains exactly why normality is needed and why the theorem is not extended to arbitrary nonnormal chains. | VERIFIED |
| `P27-E1-021` | HIGH-IMPACT | L157 | M: residuality's separate role in excluding a fixed power and forcing unbounded quotient orders is correctly stated. | VERIFIED |
| `P27-E1-022` | HIGH-IMPACT | L161–L165 | M+A4: `Γ(3n!)` is nested, normal, finite index; the projective-sign issue is explicitly identified. | VERIFIED |
| `P27-E1-023` | HIGH-IMPACT | L174–L180 | M: sign compatibility modulo successive levels and unbounded divisibility prove the projective residual intersection is trivial. | VERIFIED |
| `P27-E1-025` | HIGH-IMPACT | L184–L194 | A4+T+M: 3 matrices, 8 moduli, 24 exact order rows, 21 bonding checks, two algorithms, plateau boundary, and primitivity caveat agree. | VERIFIED |
| `P27-E1-026` | HIGH-IMPACT | L190 | A4+T: `G3-A` sequence `1,3,3,6,6,36,72,288` reproduces exactly. | VERIFIED |
| `P27-E1-027` | HIGH-IMPACT | L191 | A4+T: `G3-B` sequence `1,1,3,12,60,360,360,2880` reproduces exactly. | VERIFIED |
| `P27-E1-028` | HIGH-IMPACT | L192 | A4+T: `G3-C` sequence `1,2,6,12,12,72,72,576` reproduces exactly. | VERIFIED |
| `P27-E1-029` | HIGH-IMPACT | L196 | M+A4: plateaus are compatible with divisibility; asymptotic escape comes from proof, not extrapolation of eight levels. | VERIFIED |
| `P27-E1-030` | RANDOM | L198 | A4+T+M: direct multiplication and finite-group-bound factor reduction agree on all 24 rows and serve as independent checks. | VERIFIED |
| `P27-E1-031` | HIGH-IMPACT | L202–L207 | M+A5: the closed residual core and its homology quotient control are distinctly defined for the marked genus-two group. | VERIFIED |
| `P27-E1-032` | HIGH-IMPACT | L209–L218 | M: residuality of the characteristic-core tower and factorial homology lower bounds are proved without asserting unenumerated full quotient orders. | VERIFIED |
| `P27-E1-033` | RANDOM | L220–L221 | M: finiteness of subgroups of bounded index supplies the characteristic-core residuality step at the stated generality. | VERIFIED |
| `P27-E1-034` | HIGH-IMPACT | L223–L224 | M+A5: a primitive homology vector has order `n!` modulo `n!`, giving the certified lower bound and primitive-owner certificate. | VERIFIED |
| `P27-E1-035` | HIGH-IMPACT | L226 | A5+M: three content-one owners and the eight-level factorial schedule are exactly the registered closed-control population. | VERIFIED |
| `P27-E1-036` | HIGH-IMPACT | L226–L230 | A5+T+M: all 24 rows equal the lower-bound sequence through 40320 while full quotient status remains explicitly not enumerated. | VERIFIED |
| `P27-E1-037` | HIGH-IMPACT | L234–L241 | M: the fixed-owner formal Euler factor uses quotient order in its support and is not mislabeled as a full orbit product. | VERIFIED |
| `P27-E1-038` | HIGH-IMPACT | L243–L249 | M+A7: unbounded quotient order proves every fixed coefficient prefix eventually equals 1 under the physical clock. | VERIFIED |
| `P27-E1-039` | HIGH-IMPACT | L251–L257 | M: the proof is a direct support argument for each fixed owner and fixed degree, with correct quantifier order. | VERIFIED |
| `P27-E1-041` | HIGH-IMPACT | L263 | M: fixed-prefix formal convergence is explicitly not promoted to analytic convergence, uniform growing-panel convergence, or an inverse-limit orbit product. | VERIFIED |
| `P27-E1-042` | HIGH-IMPACT | L265 | M: the same-owner variable is retained across levels; changing owners would not prove the stated owner firewall. | VERIFIED |
| `P27-E1-043` | HIGH-IMPACT | L267 | M: multiplicity is correctly identified as a separate observable not controlled by support escape alone. | VERIFIED |
| `P27-E1-044` | HIGH-IMPACT | L271–L275 | M+A8: `H_N`, deck group `(Z/NZ)^4`, nonresidual intersection, three-owner panel, and factorial schedule are all exact. | VERIFIED |
| `P27-E1-045` | HIGH-IMPACT | L275 | A8+T+M: the three primitive content-one owners and `N=n!`, `n=1,…,8`, match the immutable owner registry. | VERIFIED |
| `P27-E1-046` | HIGH-IMPACT | L277–L285 | M+A8: degree `N⁴`, deck order `N`, `N³` primitive components, and physical period `Nℓ(g)` hold for every content-one owner. | VERIFIED |
| `P27-E1-047` | HIGH-IMPACT | L287–L288 | M: surjective abelianization and Bézout's identity prove the cover degree and exact deck order. | VERIFIED |
| `P27-E1-048` | HIGH-IMPACT | L290–L295 | M: deck-cycle counting gives `N³`, the subgroup intersection gives period `Nℓ(g)`, and the unique-root argument proves lift primitivity. | VERIFIED |
| `P27-E1-049` | HIGH-IMPACT | L297 | M+R: the homology tower, owner declaration, and clock differ materially from the residual candidate and are correctly registered as a new candidate. | VERIFIED |
| `P27-E1-050` | HIGH-IMPACT | L299 | M: content one is exactly the hypothesis for order `N`; the `N/gcd(N,d)` variation and base primitivity statement are correct. | VERIFIED |
| `P27-E1-051` | HIGH-IMPACT | L303–L306 | M: physical/rescaled clocks and raw/log-normalized multiplicities are explicitly defined before comparison. | VERIFIED |
| `P27-E1-052` | HIGH-IMPACT | L308–L310 | M+A8+T: all four exact factors reproduce; only simultaneous clock and multiplicity renormalization recovers the base factor at every level. | VERIFIED |
| `P27-E1-053` | HIGH-IMPACT | L312–L326 | M+A8: the four table entries and their support/multiplicity behaviors are algebraically exact for each owner and level. | VERIFIED |
| `P27-E1-054` | HIGH-IMPACT | L328–L329 | M: `N³` lift factors, clock support, and exponent normalization derive the four quadrants directly. | VERIFIED |
| `P27-E1-055` | HIGH-IMPACT | L331–L332 | M: fixed-prefix escape in `Q00/Q01`, coefficient divergence in `Q10`, and exact equality in `Q11` follow from the displayed factors. | VERIFIED |
| `P27-E1-056` | HIGH-IMPACT | L334–L342 | A8+T+M: the exact binomial coefficient formula is correct; 96 quadrant rows and 1,248 degree-0–12 coefficient rows reproduce. | VERIFIED |
| `P27-E1-058` | HIGH-IMPACT | L344–L350 | M+A8: ownerwise multiplication gives the finite-panel `Q11` identity at the formal logarithm level without a complex fractional-power branch. | VERIFIED |
| `P27-E1-059` | HIGH-IMPACT | L352 | M: the identity includes `N=1` and the text immediately denies that exactness alone establishes canonicity. | VERIFIED |
| `P27-E1-060` | HIGH-IMPACT | L352 | M+R: clock and exponent are read from deck order/component count; missing intrinsic arithmetic and infinite-product convergence remain explicit. | VERIFIED |
| `P27-E1-061` | HIGH-IMPACT | L354–L366 | M: within positive scalar clock/exponent renormalizations, all-large-`s` equality forces `c_N=1/N` and `b_N=1/N³`. | VERIFIED |
| `P27-E1-062` | HIGH-IMPACT | L368–L375 | M: leading exponent and leading coefficient of the logarithmic series prove both uniqueness equations. | VERIFIED |
| `P27-E1-063` | HIGH-IMPACT | L377 | M: uniqueness is correctly bounded to the registered two-scalar class and does not exclude owner-dependent or operator-valued alternatives. | VERIFIED |
| `P27-E1-064` | HIGH-IMPACT | L379 | M+A8: factorials are only the finite validation schedule; the cover and uniqueness proofs hold for every positive integer `N`. | VERIFIED |
| `P27-E1-065` | HIGH-IMPACT | L383–L395 | Direct hashes+A8+T+M: printed freeze/input/validation/core hashes, 12 tests, owner separation, and byte-identical builds all match. | VERIFIED |
| `P27-E1-066` | HIGH-IMPACT | L397 | T+M: default reproduction verifies checked-in files without mutation; refresh is explicit. | VERIFIED |
| `P27-E1-068` | HIGH-IMPACT | L405 | A4+A5+A8+T+M: the executable validates immutable owners, exact cover/factor data, integer coefficients, counts, locks, and two-build identity as described. | VERIFIED |
| `P27-E1-069` | HIGH-IMPACT | L407 | M+A4+A5+A7+A8: residual, closed-control, prefix, and calibrator artifacts remain separated; universal conclusions rest on written proofs. | VERIFIED |
| `P27-E1-070` | HIGH-IMPACT | L411–L416 | R+M: residual candidate tuple `(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` follows from absent periodic owners and missing higher layers. | VERIFIED |
| `P27-E1-071` | HIGH-IMPACT | L418–L423 | R+M+A8: homology panel supports only `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FAIL)`; generic nonarithmetic validity is the decisive control. | VERIFIED |
| `P27-E1-072` | HIGH-IMPACT | L425 | R+M: `Q10/Q01` isolate one-intervention failures; exact `Q11` remains arithmetically nonselective and cannot inherit residual-owner credit. | VERIFIED |
| `P27-E1-073` | RANDOM | L429 | M+A4+A5: normal/common-clock scope, cusped primitivity limitation, and closed full-order nonenumeration match the proofs and artifacts. | VERIFIED |
| `P27-E1-074` | HIGH-IMPACT | L431 | M+A8+R: fixed finite panel, nonresidual tower, no growing-product limit, imposed normalization, and absent target/operator inputs are explicit. | VERIFIED |
| `P27-E1-075` | HIGH-IMPACT | L433 | M: no contradiction exists because the residual and homology constructions change tower, quantified owner, clock, components, and observable. | VERIFIED |
| `P27-E1-076` | HIGH-IMPACT | L435 | M+A8: future growing-panel question correctly lists missing counting, uniform multiplicity, and summability inputs not supplied by 96 rows. | VERIFIED |
| `P27-E1-077` | HIGH-IMPACT | L439 | M+A4+A5+A7+A8+R: conclusion accurately combines same-owner no-go and separately registered finite calibration without A2 or Route-B promotion. | VERIFIED |

## Findings and limitations

No selected claim requires a distortion or unverifiability issue ID. Stable claim-finding set: **empty**.

`P27-E-ADV-ANCHORLESS-1` is a non-verdict advisory: all **71/71** persisted evidence tuples have `anchor.kind = none` and `excerpt.state = anchorless`; no source span, source-content hash, or captured excerpt is bound into a row. The independent semantic checks still support VERIFIED, but the receipts alone cannot replay an exact source quotation or establish which source bytes were read. The optional source excerpts above are review notes only and do not mutate or upgrade the evidence rows.

The registry-coverage sidecar reports seven mechanically detectable candidates and zero unregistered candidates, but its declared `semantic_extraction_coverage` is `not_machine_detectable`. This audit therefore establishes completeness for the **stable selected registry population**, not an automated guarantee that every semantically possible claim in the manuscript was registered.
