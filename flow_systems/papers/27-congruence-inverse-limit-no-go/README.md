# Paper 27 — congruence inverse-limit no-go

Working title: *Renormalization Obstructions in Congruence and Homology Towers of Geodesic Flows*

## Current status

- Current pipeline: **Round 9 — ARS Stage 2.5 audited / FAIL-CLOSED**.
  The manuscript and bounded scientific/semantic surfaces are clean within the
  recorded denominators, but the missing scholar-owned experiment-intake
  declaration remains the blocking provenance item `P27-S25-F001`.
- **Round-8 historical snapshot (superseded for pipeline stage):** ARS Stage 1
  RESEARCH was in progress through the reproducible Round-8 campaign.  This
  remains the scientific development history; it is not the current ARS stage.
- Scientific proposal baseline: **Stage 1 Classical Flow Baseline / Route A
  A0--A1**.  The residual and homology-calibrator Route states below remain
  unchanged by the Stage-2.5 audit.
- Concrete mathematical result: for the frozen residual principal-congruence
  tower, the coordinatewise continuous-time geodesic flow on the inverse limit
  has **no periodic points**.
- Local progress tag: **`[PROVED] PROVED_A1_OBSTRUCTION`** for the inverse-limit
  flow itself.  The conservative formal evaluation is now
  **`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`**, overall
  **`ROUTE_A_REJECTED`**.  `A1_FAIL` is proved because
  `Per(M_infinity)=empty`; A2--A4 are `FAIL/NOT_TESTABLE` for this same owner.
  Route-B evaluation is not run and invocation is disallowed.

- Round-3 closest-prior audit: **COMPLETE, SEARCH-BOUNDED**.  Direct structural
  prior work was found, so the theorem is not being positioned as a new general
  aperiodicity theorem.  The candidate contribution is narrowed to the explicit
  `Gamma(3 n!)` specialization, its sign-sensitive residual proof, the
  reproducible finite-level order ledger, and the finite-owner firewall.
- Round-4 theorem: **`[PROVED]` period escape**.  In any descending normal
  finite-index tower with trivial intersection, the finite-quotient orders of
  every infinite-order element divide forward and tend to infinity.  Hence the
  whole-`g`-loop closing times of every fixed hyperbolic owner escape to
  infinity.  This is the minimal time among whole traversals of the selected
  `g`-loop; without a conjugacy-primitivity proof it is not called the
  underlying flow orbit's minimal period.  The 24 frozen rows validate the
  finite prefix; they do not prove the asymptotic theorem.
- Round-5 cocompact control: **`[PROVED]` with reproducible exact-integer
  audit**.  On a closed genus-2 hyperbolic surface, the canonical residual-core
  tower refined by the mod-`n!` homology kernel has trivial intersection.  For
  each frozen primitive-homology owner, its quotient order is divisible by
  `n!`, so the exact minimal lifted-geodesic period is at least
  `n! ell(g)`.  This proves that period escape and inverse-limit aperiodicity
  are not cusp, principal-congruence, or arithmetic-specific phenomena.
- Round-6 positioning audit: **COMPLETE**.  A 13-row claim/source matrix ties
  nine external claim rows to five authoritative source records (four
  research articles and one theorem exposition), with exact URLs and locators
  checked on 2026-08-28.  All nine remain
  `HUMAN_CONFIRMATION_PENDING`; zero are marked `USER_ATTESTED_READ`.
- Frozen three-way decision: short compact-versus-cusped owner-audit
  **GO**; standalone new general aperiodicity theorem **NO-GO**; same-owner
  Route-A A2 **NO-GO**.  Eleven tests and two byte-identical builds pass; the
  Round-6 tree SHA-256 is
  `53b8b332c09f771f97ad45a1504491a7e542d014a9d6ce677d3dc86851efeb5a`.
- Round-7 coefficient-stability theorem: **`[PROVED]`**.  For every fixed
  primitive base owner, its finite-level factor is eventually `1` modulo every
  fixed power of the owner variable because the quotient order tends to
  infinity.  The same holds for every fixed finite owner panel.  A 48-row
  exact/lower-bound ledger and 54 fixed-prefix diagnostics replay this support
  escape without inferring primitivity for the three cusped loop rows.  Core
  SHA-256 is
  `551e92315c46dcbb4d01bd84688bb77eca8fcd4a6c2eaec202fe04f621275845`.
- Round-8 collective-renormalization theorem: **`[PROVED]`** for a separately
  registered pure homology-cover finite-panel calibrator.  For each primitive
  content-one owner, the deck order, lift count, and physical period are
  `N`, `N^3`, and `N ell(g)`.  Physical time alone gives support escape;
  `1/N` time alone gives multiplicity divergence; `1/N^3` logarithmic
  normalization alone still gives support escape; applying both recovers
  `(1-x_g)^(-1)` exactly at every level.  The 96 quadrant rows and 1,248 exact
  coefficient rows have core SHA-256
  `a1b588724dacb2ab2986326a7a5e1c6aec654c61538c1465e26564357b568b33`.
  This new generic finite-panel object is `ROUTE_A_REJECTED`; it does not alter
  the Round-7 same-owner verdict.

### Round-8 four-quadrant collective renormalization — 2026-08-28

For `H_N=ker(Gamma -> H_1(Sigma;Z/NZ))`, the genus-two deck group has degree
`N^4`.  A primitive-content-one owner has order `N`, so its preimage has `N^3`
primitive components of period `N ell(g)`.  The four clock/multiplicity choices
are therefore

```text
(1-x_g^N)^(-N^3),  (1-x_g)^(-N^3),
(1-x_g^N)^(-1),    (1-x_g)^(-1).
```

Only the last row, which explicitly changes both clock and normalization,
recovers the base finite-owner factor.  The pure homology tower is not
residual—its intersection is the commutator subgroup—and the result is generic
for every marked genus-two metric.  It is a proves-too-much calibration, not a
rational-prime candidate or full determinant.  See the
[Round-8 theorem](notes/round8_homology_renormalization_theorem.md) and
[paper research spine](paper/round8_research_spine.md).

### Round-7 same-owner coefficient escape — 2026-08-28

For a fixed primitive base owner `g`, let `o_n(g)` be its quotient order and
`x_g=exp(-s ell(g))`.  Since `o_n(g)->infinity`,

```text
(1-x_g^(o_n(g)))^(-1) = 1 mod x_g^(N+1)
```

for every fixed `N` at all sufficiently large levels.  Thus no fixed finite
base-owner panel retains a nontrivial coefficientwise Euler prefix under the
unchanged clock.  In physical time, all of its lifted periods leave every
bounded window.

This is a stronger same-owner A2 no-go, not a statement about an undefined
collective renormalized candidate.  The latter would need a new object, clock,
normalization, determinant, and source lock.  See the
[Round-7 theorem](notes/round7_owner_factor_escape_theorem.md) and
[paper research spine](paper/round7_research_spine.md).

### Round-6 compact-versus-cusped positioning — 2026-08-28

Both frozen examples are instances of the same theorem: a descending normal
finite-index residual tower with one common arclength clock has no
inverse-limit periodic point, and every fixed infinite-order owner's quotient
orders divide forward and diverge.  The cusped `Gamma(3n!)` tower supplies the
explicit PSL-sign specialization and exact quotient orders; the closed
genus-2 tower supplies `n!` lower bounds for exact minimal lifted periods.

Direct structural prior rules out a broad novelty claim.  The defensible paper
unit is a short comparative methods/explicit-case note centered on ownership
discipline and the finite-to-limit firewall.  Source records are web-verified,
but author locator confirmation remains pending before submission prose.  See
the [Round-6 positioning audit](notes/round6_compact_cusped_positioning_audit.md),
[go/no-go decision](notes/round6_go_no_go_decision.md), and
[contribution lock](paper/round6_contribution_lock.md).

### Round-5 cocompact control — 2026-08-27

For the closed genus-2 surface group `Gamma`, let `R_n` be the intersection of
all normal subgroups of index at most `n`, let `H_n` be the kernel of homology
modulo `n!`, and put `Gamma_n=R_n intersection H_n`.  Finite generation and
residual finiteness make this a descending normal finite-index residual tower.
If the integral homology vector of `g` has content `d`, then

```text
n!/gcd(n!,d) divides ord(g Gamma_n).
```

The three frozen owners have primitive homology (`d=1`), which also proves
that their base conjugacy classes are primitive.  Their certified lower-bound
sequence at levels 1--8 is

```text
1, 2, 6, 24, 120, 720, 5040, 40320.
```

The landed ledger has 24 rows, ten tests pass, two builds are byte-identical,
and the combined artifact SHA-256 is
`f8b04a5bbc323bf2161cfe675b40c9b9dc16f2c67a12082dad29794396ade4ea`.
The canonical residual cores are not enumerated and no full quotient order is
reported as computed; the exact values are homology lower bounds.  See the
[Round-5 cocompact theorem](notes/round5_cocompact_control_theorem.md).

### Round-4 period-escape result — 2026-08-27

For `o_n=ord(g Gamma_n)` in `Gamma_1/Gamma_n`, normal tower maps give
`o_n | o_(n+1)`.  If this sequence were bounded, it would be eventually
constant, forcing a positive power of the infinite-order element `g` into
`intersection_n Gamma_n={e}`.  This contradiction proves `o_n -> infinity`
and therefore the whole-`g`-loop closing time `o_n ell(g) -> infinity` for
hyperbolic lifts.

The exact specialization applies to `Gamma(3 n!)`.  The executable audit
rechecks all 21 divisibility transitions for the three frozen elements; their
last-to-first order growth factors are `288`, `2880`, and `576`.  The theorem
strengthens the finite-owner firewall without reviving a general novelty claim.
See the [Round-4 theorem](notes/round4_period_escape_theorem.md).

### Round-3 closest-prior result — 2026-08-27

The strongest prior-work overlap is substantive:

- Martínez--Matsumoto--Verjovsky (2016) give a compact hyperbolic lamination
  example without periodic geodesic orbits and separately describe the
  universal hyperbolic solenoid as an inverse limit with simply connected
  leaves.
- Penner--Šarić (2008) define the noncompact punctured solenoid as the inverse
  limit over finite-index subgroups of `PSL_2(Z)` and state that its leaves
  are unit disks.
- Alcalde Cuesta--Carballido Costas--Martínez--Verjovsky (2026) treat exactly
  the object class of noncompact finite-area surface-covering inverse limits,
  call the regular-cover case a hyperbolic McCord solenoidal surface of finite
  type, and define its leafwise geodesic flow.

No checked primary source stated the exact factorial-chain proposition
`Gamma(3 n!)` verbatim.  That negative search result is bounded by the
recorded strings and sources; it is not an absolute novelty claim.  In light of
the direct structural prior, the no-period theorem is treated as an explicit
specialization/case study rather than a standalone new general theorem.  See
the [Round-3 source audit](notes/round3_closest_prior_audit.md), [Round-3
conclusion](notes/round3_conclusion.md), and [Stage-1 research
spine](paper/stage1_research_spine.md).

### Round-2 finite-level diagnostic — 2026-08-27

The prespecified eight moduli `3,6,18,72,360,2160,15120,120960` have now
been executed for three frozen hyperbolic elements of `Gamma(3)`.  The landed
ledger has 24 rows.  Every projective reduction order was computed by both
sequential matrix multiplication and an independent finite-group-bound factor
reduction; all `24/24` pairs agree.  The observed order sequences are

```text
G3-A: 1,3,3,6,6,36,72,288
G3-B: 1,1,3,12,60,360,360,2880
G3-C: 1,2,6,12,12,72,72,576
```

These are `[NUMERICALLY_CERTIFIED]` finite-quotient diagnostics.  Their owner
is the frozen congruence tower plus the three matrices, not the inverse-limit
flow.  Consequently they do not weaken or compensate for the `[PROVED]`
identity `Per(M_infinity)=empty`, and they receive no formal A1/A2 credit for
that flow.  Positive-word primitivity is checked exactly, while primitivity as
a full `Gamma(3)` conjugacy class remains `[OPEN]` because it is unnecessary
for the reduction-order diagnostic.

## Frozen dynamical system

For `n>=1`, let

```text
Gamma_n = Gamma(3 n!) < PSL_2(Z),
Y_n = Gamma_n \ H,
M_infinity = inverse_limit_n T^1Y_n.
```

The bonding maps are the finite covering maps, and the flow is defined
coordinatewise by the unit-speed geodesic flows.  The clock is hyperbolic
arclength at every level.  In the terminology of Alcalde Cuesta et al. (2026),
this normal regular-cover tower is a noncompact hyperbolic McCord solenoidal
surface of finite type.  It is not the compact universal hyperbolic solenoid;
`principal-congruence inverse-limit geodesic lamination` remains an
unambiguous project-local description.

## Stage-1 no-go theorem

Write the level-`n` coordinate as `Gamma_n h_n`.  Compatibility with the first
coordinate gives `h_n=eta_n h_1` for some `eta_n in Gamma_1`.  If the first
projection has primitive hyperbolic representative `gamma` and primitive length
`ell(gamma)`, then a common period has `T=m ell(gamma)` and

```text
h_n a_T h_n^{-1} = eta_n gamma^m eta_n^{-1}.
```

The level-`n` lift returns after `T` exactly when this element lies in
`Gamma_n`.  Since every `Gamma_n=Gamma(3 n!)` is normal in `Gamma_1`, this is
equivalent to `gamma^m in Gamma_n`.  Hence a compatible periodic point would
force `gamma^m` into every level.

For completeness, if `[A] in PSL_2(Z)` belongs to every `Gamma(3 n!)`, choose
`A in SL_2(Z)`.  For each `n` there is a sign `epsilon_n` with
`A = epsilon_n I mod 3 n!`.  Reducing the level `n+1` congruence modulo `3 n!`
shows the signs agree, because `3 n!` never divides `2`.  All entries of
`A-epsilon I` are therefore divisible by the unbounded sequence `3 n!`, so
`A=epsilon I` and `[A]=1`.  Thus

```text
intersection_n Gamma(3 n!) = {1},
```

so `gamma^m=1`, contradicting hyperbolicity.  Therefore

```text
Per(M_infinity) = empty.
```

This proves `Per(M_infinity)=empty` and establishes the local progress tag
`[PROVED] PROVED_A1_OBSTRUCTION`.  The formal evaluator maps the same fact to
`A1_FAIL` because this owner has no primitive periodic-orbit population.
Finite-level zeta functions may still have a renormalized projective limit,
but that would be a different owner and must be labeled separately.

## Bold residual hypothesis and kill gate

`[HEURISTIC]`: normalized finite-level trace/zeta data may retain local congruence
splitting information.  The kill gate is owner identity: if the proposed
analytic object is not defined by primitive orbits of `M_infinity`, it cannot
receive A1/A2 credit for the limit flow.

Evidence labels follow `skills/route-a-evaluator.md`.  `PROVED_A1_OBSTRUCTION`
is a local theorem-progress tag; the formal same-owner verdict is `A1_FAIL`.

## Files

- [Stage-1 theorem brief](notes/stage1_research_brief.md)
- [pipeline state](notes/pipeline_state.md)
- [executed finite-level diagnostics](results/README.md)
- [Round-2 conclusion and owner firewall](notes/round2_conclusion.md)
- [Round-3 closest-prior audit](notes/round3_closest_prior_audit.md)
- [Round-3 conclusion](notes/round3_conclusion.md)
- [Round-4 period-escape theorem](notes/round4_period_escape_theorem.md)
- [Round-4 reproducibility receipt](experiments/round4_reproducibility_receipt.json)
- [Round-5 cocompact control theorem](notes/round5_cocompact_control_theorem.md)
- [Round-5 reproducibility receipt](experiments/round5_reproducibility_receipt.json)
- [Round-6 compact-versus-cusped positioning audit](notes/round6_compact_cusped_positioning_audit.md)
- [Round-6 go/no-go decision](notes/round6_go_no_go_decision.md)
- [Round-6 contribution lock](paper/round6_contribution_lock.md)
- [Round-6 reproducibility receipt](experiments/round6_reproducibility_receipt.json)
- [Round-6 Route-A evaluation](../../evaluations/route_a/P27-CONGRUENCE-INVERSE-LIMIT-GEODESIC-FLOW/2026-08-28-round6.yaml)
- [Round-7 owner-factor escape theorem](notes/round7_owner_factor_escape_theorem.md)
- [Round-7 freeze contract](experiments/round7_owner_factor_escape_freeze.json)
- [Round-7 validation](experiments/round7_validation.md)
- [Round-7 paper research spine](paper/round7_research_spine.md)
- [Round-7 Route-A evaluation](../../evaluations/route_a/P27-CONGRUENCE-INVERSE-LIMIT-GEODESIC-FLOW/2026-08-28-round7.yaml)
- [Round-8 homology-renormalization theorem](notes/round8_homology_renormalization_theorem.md)
- [Round-8 freeze contract](experiments/round8_homology_renormalization_freeze.json)
- [Round-8 validation](experiments/round8_validation.md)
- [Round-8 paper research spine](paper/round8_research_spine.md)
- [Round-8 new-owner Route-A evaluation](../../evaluations/route_a/P27-HOMOLOGY-RENORMALIZED-GEODESIC-PANEL/2026-08-28-round8.yaml)
- [Round-9 manuscript](paper/manuscript.tex)
- [Stage-2.5 independent integrity audit](notes/stage2_5_independent_audit.md)
- [Stage-2.5 Phase-E semantic audit](notes/stage2_5_phase_e_semantic_audit.md)
- [Stage-1 paper research spine](paper/stage1_research_spine.md)
- [reproduction entry point](experiments/reproduce.sh)

### Round-8 historical snapshot — superseded by the Round-9 manuscript

The no-periodic-orbit theorem remains the Route-relevant landed result.  The
finite-level tables are reproducible diagnostics only.  The Round-5 control
closes the planned compactness/cusp check and narrows the publishable claim to
a comparative owner-audit paper.  Round 6 freezes that narrow paper as GO but
rejects standalone novelty and same-owner A2.  **At that Round-8 cutoff**, a
manuscript had not yet been started and ARS Stage 2 had not begun; this sentence
is retained only as historical state and is superseded by the Round-9 paper and
Stage-2.5 audit below.  Round 7 had strengthened the same-owner NO-GO from orbit
absence to coefficientwise factor escape.

## Round 9 paper and Stage 2.5 status

The residual-owner no-go and homology-cover calibration now form a 4,099-word,
12-page paper. Stage 2.5 checked 5/5 references, 5/5 contexts, all 13 data
families, 21/67 originality paragraphs, and a 77-claim registry.

- **Structural closure:** the corrected Phase-E selection contains 67
  HIGH-IMPACT plus three RANDOM claims.  All 70/70 selected claim IDs and all
  71/71 `(claim_id, selection_tier, ref_slug-or-null)` tuples are present,
  unique, ordered, and validator-clean.  This closes the registered selection
  and carrier structure; semantic extraction completeness for the whole
  manuscript remains `not_machine_detectable`.
- **Evidence-carrier limitation:** all 71/71 persisted evidence rows have
  `anchor.kind = none` and `excerpt.state = anchorless`.  They carry verdict
  metadata but cannot themselves replay source-bound excerpts; this is a
  non-gating advisory, not a downgrade of the claim verdicts.
- **Independent semantics:** the independent
  [Phase-E semantic audit](notes/stage2_5_phase_e_semantic_audit.md) cross-read
  every selected claim against the manuscript proof chain, exact artifacts and
  tests, and the documented official-source contexts.  It supports 70/70
  distinct claims and 71/71 tuples as `VERIFIED`, with no distortion or
  unverifiable finding.

The scientific surfaces are clean within the stated scope.  The residual model
stays
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` /
`ROUTE_A_REJECTED`; the homology model stays
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FAIL)` /
`ROUTE_A_REJECTED`.  It remains a generic finite-panel calibrator; neither
candidate earns A2 or Route-B credit.  The pipeline stays **`FAIL-CLOSED`**
solely because the scholar-owned experiment intake/provenance declaration is
absent; C4/Mode 6 must be rechecked after scholar resolution.  See the
[integrity report](notes/stage2_5_integrity_report.md) and
[independent audit](notes/stage2_5_independent_audit.md).
