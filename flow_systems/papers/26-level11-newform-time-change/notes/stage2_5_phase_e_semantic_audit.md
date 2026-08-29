# Paper 26 — Stage 2.5 Phase-E semantic audit

Audit date: 2026-08-29 UTC  
Audit role: independent read-only Phase-E semantic reviewer  
Surface: stable selected claims in `notes/stage2_5_claim_registry.json` and their persisted tuples in `notes/stage2_5_evidence_rows.json`  
Route scope: Route A only; Route B remains unauthorized

## Disposition

**Phase-E semantic verdict: PASS for all 68 selected distinct claims.** Every selected claim was checked at its exact registered UTF-8 manuscript span against the adjacent proof chain, the exact local artifacts and tests where applicable, the documented official-source Phase-A/B audit for source-dependent statements, and the paper's explicit scope limitations. The result is **68 VERIFIED, 0 MINOR_DISTORTION, 0 MAJOR_DISTORTION, 0 UNVERIFIABLE_ACCESS, and 0 UNVERIFIABLE**.

This is a claim-semantic subaudit, not an override of the overall Stage-2.5 gate. In particular, it does not resolve the separate scholar-owned experiment-intake blocker `P26-S25-F001` recorded in `stage2_5_independent_audit.md`.

## Frozen input and audit method

The audit used `BATCH_ROUND9_STAGE2_5_INPUT_FREEZE.json` (SHA-256 `7f50da159c5e8b5f3eefee83979279cc39140574f105ce18d2fd33eac0f8a0cb`, frozen `2026-08-29T01:13:20Z`). A post-report byte check reproduced every Paper-26 frozen hash:

| Frozen object | Expected and observed SHA-256 | Result |
|---|---|---|
| `paper/manuscript.tex` | `00a21246f496b12f98389522d762ad6c4e10683e0eb21163b881d7b035f9c2fe` | unchanged |
| `paper/references.bib` | `9b061c02006f07f1c93df68d8577d44906122f55db71e6f529f43cf3f6483ed8` | unchanged |
| `paper/paper.pdf` | `b2911495fff88a1e351c4b7cc65989f998df47822b3a2bae0db60b543c34d5aa` | unchanged |

The registry itself remained SHA-256 `1d27b238ae1fd5485192c7044f135e530d68aba6c997041fd441d7db4ded9cf2`; the evidence-row sidecar remained `7cdc6095fae6ef317059ce46104bfaeee4a7707f51fb4dcd78005e1bf8f0a842`. All 72 registered byte spans replay exactly against the frozen manuscript. The official registry-coverage validator and evidence-row validator both pass.

The evidence abbreviations used below are:

- **M** — exact registered span plus the complete written definition/theorem/proof/limitation chain in the frozen manuscript.
- **A4/A6/A7/A8** — the exact Round-4 cycle ledger, Round-6 quadratic-degree-moment ledger, Round-7 rational Schreier model, and Round-8 taxonomy ledgers/summary.
- **T** — 74/74 historical tests plus the Round-8 verify-default replay, 18/18 tests, two byte-identical builds, tree SHA-256 `cc36c1f952c9ce89050996f4bb4c9905571f9ef09a0d7115be8a985e02a5621d`.
- **S** — the documented Phase-A/B official-source audit, independently cross-read at the concrete locators listed below.
- **R** — the Route-A evaluator definitions cross-read against the manuscript's declared tuple and controls.

Key exact artifacts were re-hashed: Round-4 cycle ledger `f906df349b8f1fa2864fed592792e0fff63ba246a069179b7bd8cfdf46520662`; Round-6 quadratic-degree-moment ledger `f95e1435c9293f8e008cebf80084ea2b522b76186dbd684b5e3997c5e588edea`; Round-8 builder `3bb9c72e1a798559481e71219a6151a90527fd46150fbc14b0d6257f3cb7582b`; tests `9c0c9480196ddf6e4df75bc8c8c6c5fbb9468c0f71b0eb72a8046e9834a391b3`; reproduction script `3e322784c5eba8af8eae729ab9b1304bd5b48c7ffa0fdfc950c9f6d5d97794d3`; Round-8 freeze note `2831c064a41353c15f348a3f690dafdd4c8e0672827738de53476894e37ebc8d`; instance ledger `beb363e4080b794e33ec6bc729b1f3e4dd7ef322be63fc59755e18fdf6bc889f`; group ledger `532e799686dd8afefa3a7529717208305fedede3f3e74e14ccf761ab35d74f69`; and summary `4ba5de801dfd06c8b03bfe5fc07297b8c4e074bcf26c70ec6566de401ae2384d`.

## Counts by tier and verdict

| Selection tier | Selected distinct claims | VERIFIED | MINOR_DISTORTION | MAJOR_DISTORTION | UNVERIFIABLE_ACCESS | UNVERIFIABLE |
|---|---:|---:|---:|---:|---:|---:|
| HIGH-IMPACT | 65 | 65 | 0 | 0 | 0 | 0 |
| RANDOM | 3 | 3 | 0 | 0 | 0 | 0 |
| TOP-UP | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total selected** | **68** | **68** | **0** | **0** | **0** | **0** |

The registry contains 72 claims in total. Four are explicitly `NOT-SELECTED`: `P26-E1-004`, `P26-E1-012`, `P26-E1-013`, and `P26-E1-071`. They are outside this stable selected population and are not silently counted as Phase-E verdicts.

## Selected-tuple coverage

The canonical tuple key is `(claim_id, selection_tier, ref_slug-or-null)`. Source-bearing claims expand to one tuple per registered source.

| Coverage check | Expected | Persisted/audited | Result |
|---|---:|---:|---|
| Selected distinct claim IDs | 68 | 68 | exact set; 100% |
| Internal claim tuples | 65 | 65 | exact set and order |
| Source-bearing claim IDs | 3 | 3 | exact set |
| Source tuples on those claims | 5 | 5 | exact `(claim_id, ref_slug)` set |
| All selected tuples | 70 | 70 | exact set and order; 0 duplicates |
| Persisted row verdicts | 70 VERIFIED | 70 VERIFIED | consistent with the distinct-claim audit |

The source-tuple expansion is `P26-E1-009 × {lmfdb112aa, manin1972}`, `P26-E1-017 × {merel1991}`, and `P26-E1-018 × {fried1986, ruelle1976}`.

## Official-source locators for the source-bearing claims

The excerpt strings below are optional, human-facing exact-excerpt candidates of no more than 25 words each. They are not inserted into the evidence-row sidecar and do not convert an anchorless receipt into a source-bound receipt.

| Claim / `ref_slug` | Concrete official or author locator checked | Exact-excerpt candidate (≤25 words) | Semantic result |
|---|---|---|---|
| `P26-E1-009` / `lmfdb112aa` | [Official LMFDB orbit 11.2.a.a](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/11/2/a/a/): Properties (level 11, weight 2, dimension 1), Newform invariants (coefficient field), q-expansion, eta quotient | “Dimension: 1” | Supports the stated level/weight/dimension/field/normalization data; VERIFIED. |
| `P26-E1-009` / `manin1972` | [Official MathNet record and English PDF](https://www.mathnet.ru/eng/im2290), pp. 19–25 for modular symbols, homology classes, and integration; the readable PDF was also cross-checked at the corresponding passage | “the right side of (22) contains the periods of ω over integral homology classes.” | Supports homological-period positioning, not the paper's new time-change theorem; VERIFIED. |
| `P26-E1-017` / `merel1991` | [Official Centre Mersenne article/full text](https://aif.centre-mersenne.org/articles/10.5802/aif.1264/), Introduction and §§1–2, pp. 519–526 | “We recall that Manin describes the singular homology relative to the cusps of the modular curve” | Supports the projective-line relative-homology/Hecke setting; does not assert a primitive dynamical recurrence; VERIFIED. |
| `P26-E1-018` / `fried1986` | [Official Numdam article/full text](https://www.numdam.org/articles/10.24033/asens.1515/), §2, pp. 496–502, prime closed-orbit product and iterate bookkeeping | “where γ runs over the prime closed orbits of φ.” | Supports prime-orbit versus iterate bookkeeping; VERIFIED. |
| `P26-E1-018` / `ruelle1976` | [Official Springer article](https://link.springer.com/article/10.1007/BF01403069), abstract, Introduction, and flow-product discussion, pp. 231–242 | “A zeta function for Anosov flows is shown to be meromorphic” | Supports the broad historical flow-zeta claim only; the manuscript correctly withholds a continuation theorem for its flow; VERIFIED. |

## Per-claim semantic ledger

Every selected distinct claim appears exactly once below. “VERIFIED” means the registered wording is supported at its stated scope; it does not grant stronger conclusions excluded by the manuscript.

| Claim | Tier | Exact locator | Proof/evidence chain checked | Verdict |
|---|---|---|---|---|
| `P26-E1-001` | HIGH-IMPACT | L36 | M: title accurately names the level-11 time change and the exact finite taxonomy developed in §§2–9. | VERIFIED |
| `P26-E1-002` | HIGH-IMPACT | L46–L47 | M+A4+A6+A7+A8+T+R: abstract theorem bundle, 138-instance 2/2/134 split, 55-group law counts, and non-global Route boundary all agree. | VERIFIED |
| `P26-E1-003` | HIGH-IMPACT | L61 | M+S: level-11 differential setup and the conjugacy/orientation/repetition laws are proved below; the Euler-product motivation is framed as a test. | VERIFIED |
| `P26-E1-005` | HIGH-IMPACT | L65–L67 | M+A6+A8: research question is explicitly restricted to the frozen owner multiset and two scalar all-$s$ laws. | VERIFIED |
| `P26-E1-006` | HIGH-IMPACT | L69 | M+A4+A6+A8: sum-valued Hecke ownership, branch degree, inverse-pair parity, and degree-wise quadratic moments establish the stated obstruction. | VERIFIED |
| `P26-E1-007` | HIGH-IMPACT | L71 | M+A4+A6+A7+A8+T: all four enumerated contributions have corresponding definitions, proofs, exact ledgers, and tests. | VERIFIED |
| `P26-E1-008` | HIGH-IMPACT | L73 | M+A8+R: the finite obstruction, 134/4 split, and exclusions of a global determinant, exhaustive primitive census, target data, and Route match are explicit. | VERIFIED |
| `P26-E1-009` | HIGH-IMPACT | L79–L97 | S+M: LMFDB and Manin support the newform and homological-period setup; descent follows from the weight-two transformation law. | VERIFIED |
| `P26-E1-010` | HIGH-IMPACT | L99–L105 | M: the density/speed convention is internally consistent; cusp-form decay gives bounded `a`, and the displayed ε-bound guarantees positivity. | VERIFIED |
| `P26-E1-011` | HIGH-IMPACT | L107–L115 | M: direct integration of the new time element and path concatenation prove the affine period and repetition formulas. | VERIFIED |
| `P26-E1-014` | HIGH-IMPACT | L125–L131 | M: quotient invariance, orientation reversal, and concatenation prove the three owner laws and keep inversion distinct from repetition. | VERIFIED |
| `P26-E1-015` | HIGH-IMPACT | L133–L135 | M: the proof correctly transports the axis segment, reverses its orientation, and sums translated segments. | VERIFIED |
| `P26-E1-016` | RANDOM | L137 | M: oriented-flow ownership and primitive-versus-iterate bookkeeping are consistent with the product convention fixed later. | VERIFIED |
| `P26-E1-017` | HIGH-IMPACT | L141–L144 | S+M: Merel supports the Hecke/relative-homology setting; the manuscript explicitly denies that the source supplies its dynamical recurrence. | VERIFIED |
| `P26-E1-018` | HIGH-IMPACT | L146–L151 | S+M: Ruelle/Fried support primitive-orbit and iterate bookkeeping; the finite-formal-only limitation prevents overextension. | VERIFIED |
| `P26-E1-019` | HIGH-IMPACT | L153 | S+M+A8: prior/local contributions are accurately separated and no global inference is made from the finite taxonomy. | VERIFIED |
| `P26-E1-020` | HIGH-IMPACT | L157–L167 | M: the Hecke action and normalization are defined at the cycle/homology owner level before any orbit interpretation. | VERIFIED |
| `P26-E1-021` | HIGH-IMPACT | L169–L177 | M: the Hecke eigenperiod statement has the correct sum-valued owner and scalar eigenvalue. | VERIFIED |
| `P26-E1-022` | RANDOM | L179–L188 | M: linearity of integration and the homological Hecke eigenrelation prove the theorem without a one-orbit substitution. | VERIFIED |
| `P26-E1-023` | HIGH-IMPACT | L190–L200 | M+A4: permutation-cycle decomposition produces the registered closed owners and retains their branch-cycle degrees. | VERIFIED |
| `P26-E1-024` | HIGH-IMPACT | L194 | M: the displayed branch-cycle product follows directly from iteration around a permutation cycle. | VERIFIED |
| `P26-E1-025` | HIGH-IMPACT | L197 | M+A4: the product element is the declared closed owner; the exact ledger records its primitive-root decomposition separately. | VERIFIED |
| `P26-E1-026` | HIGH-IMPACT | L202 | M: the statement correctly warns that the theorem is sum-valued and does not map one primitive orbit to one primitive orbit. | VERIFIED |
| `P26-E1-027` | HIGH-IMPACT | L206 | M+A4: branch degree, primitive-root exponent, and zeta repetition are separately defined and separately serialized. | VERIFIED |
| `P26-E1-028` | HIGH-IMPACT | L208 | A4+T+M: exact root certification gives primitive-root exponent one for all 138 registered outputs without equating it to branch degree. | VERIFIED |
| `P26-E1-029` | HIGH-IMPACT | L210 | M: the zeta repetition index belongs to the logarithmic expansion and is not reused as either owner index. | VERIFIED |
| `P26-E1-030` | HIGH-IMPACT | L214–L222 | M: the finite inverse-closed formal product, multiplicities, degrees, periods, and finite-scope quantifier are defined coherently. | VERIFIED |
| `P26-E1-031` | HIGH-IMPACT | L224–L237 | M: exact differentiation of the logarithmic factors gives the stated first/second variations and inverse-pair cancellation/addition. | VERIFIED |
| `P26-E1-032` | HIGH-IMPACT | L239–L245 | M: termwise differentiation is legitimate for the finite formal family and the parity calculation is correct. | VERIFIED |
| `P26-E1-033` | HIGH-IMPACT | L247–L251 | M+A4+A6: degree-wise square moments and root exponents are kept distinct; registered root exponent one is an exact finite fact. | VERIFIED |
| `P26-E1-034` | HIGH-IMPACT | L253–L264 | M+A6: coefficient comparison and Möbius inversion prove the necessary-and-sufficient all-$s$ degree-moment criterion. | VERIFIED |
| `P26-E1-035` | HIGH-IMPACT | L266–L272 | M: the proof correctly derives coefficient `n Σ_{d|n} Q_d/d`, compares with the source, and inverts degree by degree. | VERIFIED |
| `P26-E1-036` | RANDOM | L274 | M: the claimed algebraic obstruction follows before root finding and is not promoted to a global dynamical theorem. | VERIFIED |
| `P26-E1-037` | HIGH-IMPACT | L278–L294 | M: the linear eigenperiod constraint does not determine the quadratic square moments; the explicit decomposition demonstrates the missing information. | VERIFIED |
| `P26-E1-038` | HIGH-IMPACT | L290 | M: the displayed piecewise target moment has the correct degree-one value and zero nonunit-degree obligations. | VERIFIED |
| `P26-E1-039` | HIGH-IMPACT | L296 | M: the rigidity depends on equality for all $s$; the manuscript correctly distinguishes it from a single-value numerical fit. | VERIFIED |
| `P26-E1-040` | HIGH-IMPACT | L298 | A7+A8+M: all 11 frozen source coordinates are nonzero (`k=±1` or `±2`), so the registered comparison is nondegenerate. | VERIFIED |
| `P26-E1-041` | HIGH-IMPACT | L300–L302 | M+A6: the nonunit-degree corollary follows from the moment criterion under nonzero source period. | VERIFIED |
| `P26-E1-042` | HIGH-IMPACT | L304–L306 | M: a sum of real squares vanishes exactly when every contributing period vanishes, proving the corollary. | VERIFIED |
| `P26-E1-043` | HIGH-IMPACT | L308 | A6+A8+M: the stated failure mechanisms and their counts agree with all 165 group/law rows. | VERIFIED |
| `P26-E1-044` | HIGH-IMPACT | L312–L320 | A7+T+M: the exact Schreier counts (12 cosets, 24 arcs, 35 relations, rank 21, dimensions 3/2/1) reproduce. | VERIFIED |
| `P26-E1-045` | HIGH-IMPACT | L322–L328 | A7+T+M: the real involution `τ(x,y,z)=(-x,y+z,-z)` is exact and compatible with the quotient model. | VERIFIED |
| `P26-E1-046` | HIGH-IMPACT | L330–L338 | A7+M: the real-period coordinate `k=2y+z` and rational normalized ratios follow from the exact homology model. | VERIFIED |
| `P26-E1-047` | HIGH-IMPACT | L340–L346 | M+A7: the proof identifies the one-dimensional compact real-period direction without adding an unsupported absolute normalization. | VERIFIED |
| `P26-E1-048` | HIGH-IMPACT | L348–L352 | A7+A8+M: square moments become exact rational sums of squares, so all zero decisions are exact rather than floating-point. | VERIFIED |
| `P26-E1-049` | HIGH-IMPACT | L356 | M+A7: full complex-period kernel and real-projection-only kernel are explicitly different predicates. | VERIFIED |
| `P26-E1-050` | HIGH-IMPACT | L358 | M+A7+A8: the decision hierarchy uses exact homology first and numerical residuals only as a cross-check. | VERIFIED |
| `P26-E1-051` | HIGH-IMPACT | L360 | M+A8: exhaustion is correctly limited to the frozen output multiset, not all primitive Γ-classes. | VERIFIED |
| `P26-E1-052` | HIGH-IMPACT | L364 | A4+A8+T+M: 11 sources × 5 primes yield 55 groups and 138 owner instances in the frozen population. | VERIFIED |
| `P26-E1-053` | HIGH-IMPACT | L366–L368 | A8+T+M: exhaustive exact classification is 2 full kernels, 2 projection-only kernels, 134 true nonkernels, 0 unresolved. | VERIFIED |
| `P26-E1-054` | HIGH-IMPACT | L370–L387 | A8+M: every per-prime row and total in the taxonomy table agrees with the exact instance ledger. | VERIFIED |
| `P26-E1-055` | HIGH-IMPACT | L389–L391 | A7+A8+T+M: the enumeration proof applies the exact coordinate predicates to every locked row with no omitted or duplicated instance. | VERIFIED |
| `P26-E1-056` | HIGH-IMPACT | L393 | A8+M: all four kernel instances occur at `p=5`, degree 5, with the listed words and correct 2+2 split. | VERIFIED |
| `P26-E1-057` | HIGH-IMPACT | L395–L397 | A8+T+M: each primary law passes 4/fails 51 of 55; control `a_p^2-p` fails all 55. | VERIFIED |
| `P26-E1-058` | HIGH-IMPACT | L399–L401 | A8+M: mechanism counts reproduce: 51 nonunit failures for `a_p`; 47 double + 4 nonunit-only for `a_p²`; control 51 double + 4 degree-one-only. | VERIFIED |
| `P26-E1-059` | HIGH-IMPACT | L403 | M+A8: the interpretation attributes survivors to exact kernel mechanisms and does not treat them as evidence for a global recurrence. | VERIFIED |
| `P26-E1-060` | HIGH-IMPACT | L405 | M+A6: the frozen Selberg-style denominator is common within each degree, so the degree-moment comparison is semantically and algebraically consistent. | VERIFIED |
| `P26-E1-061` | HIGH-IMPACT | L407 | M+A8: the four finite survivors are explicitly bounded and cannot establish an unrestricted law. | VERIFIED |
| `P26-E1-062` | HIGH-IMPACT | L411–L422 | Direct hash checks+A4+A6+A8+M: every manuscript-printed locked input, builder, test, script, and freeze hash matches. | VERIFIED |
| `P26-E1-063` | HIGH-IMPACT | L424 | A8+M: 138 instance rows, 165 group/law rows, 165 numerical-verdict agreements, and the printed maximum residual reproduce. | VERIFIED |
| `P26-E1-064` | HIGH-IMPACT | L426–L430 | T+M: verify-default is nonmutating, 18/18 passes, two four-file trees are byte-identical, and the tree hash matches. | VERIFIED |
| `P26-E1-065` | HIGH-IMPACT | L432 | M+A7+A8: the layered certificate accurately distinguishes exact homology, exact combinatorics, and numerical cross-checks. | VERIFIED |
| `P26-E1-066` | HIGH-IMPACT | L434 | T+M: tamper cases are rejected by locks, schema/count checks, exact predicates, and reproducibility comparison as described. | VERIFIED |
| `P26-E1-067` | HIGH-IMPACT | L438 | R+A8+M: weak arithmetic provenance and the finite analytic owner ledger support only `(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, …)`. | VERIFIED |
| `P26-E1-068` | HIGH-IMPACT | L440–L445 | R+A8+M: A2–A4 fail for the stated missing census/determinant, analytic structure, and natural operator-lift obligations; Route B is closed. | VERIFIED |
| `P26-E1-069` | HIGH-IMPACT | L447 | R+A8+M: zero use of prime-target/Riemann-zero tables and generic/proves-too-much controls correctly prevent inherited Route credit. | VERIFIED |
| `P26-E1-070` | HIGH-IMPACT | L451 | M+A8: finite-population, multiplicity, convergence, continuation, and global-owner limitations are explicit and consistent with the proofs. | VERIFIED |
| `P26-E1-072` | HIGH-IMPACT | L457 | M+A4+A6+A7+A8+R: conclusion is exactly the bounded owner obstruction and finite taxonomy established above, with no Hilbert–Pólya promotion. | VERIFIED |

## Findings and limitations

No selected claim requires a distortion or unverifiability issue ID. Stable claim-finding set: **empty**.

`P26-E-ADV-ANCHORLESS-1` is a non-verdict advisory: all **70/70** persisted evidence tuples have `anchor.kind = none` and `excerpt.state = anchorless`; no source span, source-content hash, or captured excerpt is bound into the row. This does not change the independently established VERIFIED verdicts, but it means the receipts alone cannot replay a source quotation or prove what exact source bytes were read. The optional source excerpts above are review notes only; they neither mutate the rows nor confer a human-read or source-captured state.

Finally, the registry coverage sidecar reports four mechanically detectable candidates and zero unregistered candidates, but its declared `semantic_extraction_coverage` is `not_machine_detectable`. Thus this audit establishes completeness for the **stable selected registry population**, not an automated proof that every semantically possible claim in the entire manuscript was registered.
