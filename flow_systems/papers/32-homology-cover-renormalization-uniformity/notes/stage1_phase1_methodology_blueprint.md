# P32 Stage-1 Phase-1 Methodology Blueprint

Date: **2026-09-01 UTC**  
Mode: **ARS Deep Research / FULL / Phase 1 only**  
Status: **REVISED PHASE-1 DESIGN — pending independent Checkpoint-1 replay**  
Controlling RQ: see `stage1_phase1_rq_brief.md`

## Research paradigm

**Selected:** proof-first mathematical realism with exact symbolic
certification and a separately gated analytic specialization.  
**Justification:** the RQ first asks whether the fixed cover/normalization gives
the correct owner factors. That question is algebraic and must be settled
before numerical length evaluations or global-product language is allowed.

## Method

**Type:** quantitative exact computational mathematics with theorem-driven
complex analysis.  
**Specific method:** derive the lift factor for arbitrary homology content,
certify target-blind primitive-owner panels, test coefficientwise equality in
independent owner variables, and attempt local-uniform convergence only after
an explicit absolute tail theorem.

Proof precedes computation. Exact computation may replay and stress the proof;
it cannot substitute finite panels for a global theorem.

## Design-freeze registry

| Axis | Frozen value |
|---|---|
| Candidate/tower | Pure homology covers `H_N=ker(Gamma -> H_1(Sigma;Z/NZ))`; never the residual inverse-limit tower |
| Continuous-time object | Unit-speed geodesic flow on a marked closed hyperbolic genus-two surface |
| Owner | Oriented primitive surface-group conjugacy class |
| Group presentation | `Gamma=<a1,b1,a2,b2 | [a1,b1][a2,b2]=1>` with fixed alphabet `a1<a1^-1<b1<b1^-1<a2<a2^-1<b2<b2^-1` |
| Equivalence interface | Fail-closed `SG2OwnerCanonical-v1`: complete equality normal form, exact oriented conjugacy canonicalization, exact primitive root, prefix completeness certificate, deterministic serialization; inverse remains separate |
| Interface status | The theorem/source/implementation binding is `UNBOUND`; no panel may execute until correctness, termination, completeness, and test-vector contracts are immutable and independently verified |
| Owner order | Number of alphabet symbols in the interface's serialized oriented-conjugacy canonical word, then the fixed alphabet lexicographic order, then exact serialized bytes; this order exists only under the bound interface |
| Homology strata | `d=1` primary; `d=2`, `d=3`, and `d=0` stress controls; `d=gcd` of the four absolute homology coordinates |
| Growing panels | Theorem families `P_m^all` and `P_m^(d)` exist for every integer `m>=1`; fixed finite diagnostics use `m in {8,16,32,64,128}` and diagonal-prefix values `m_k=2^k` for `1<=k<=8`; an unclosed prefix is `PANEL_NOT_EVALUABLE`, and insufficient certified population is fail-closed with no padding |
| Theorem schedule | For every integer `k>=1`, `N_k=k!`; the registered diagonal has `m_k=2^k` for every `k>=1`; every limit quantifies over this infinite sequence |
| Execution prefix | Future exact diagnostics may use only `1<=k<=8`; this finite prefix is a consistency certificate and carries no limit or cofinality evidence |
| Clock | Physical lift period multiplied by exactly `1/N` |
| Multiplicity normalization | Raw lift-component log product multiplied by exactly `1/N^3` |
| Owner factor | Reciprocal Ruelle convention `(1-exp(-sT))^(-multiplicity)`; no stability or phase weight |
| Primary topology | `R_+=inverse-limit_(F,D) Q[u_g:g in F]/m_F^(D+1)`, `m_F=(u_g:g in F)`, over finite positive-content owner sets `F` and total degree `D`; equality is every finite-support coefficient projection |
| Scalar map | On `A_F=Q[u_g:g in F][(1-u_g^r)^(-1):g in F,r>=1]`, `sigma_(s,F)(u_g)=exp(-s ell(g)/d(g))`; an infinite scalar specialization exists only after an absolute uniform tail theorem and is not presumed on all of `R_+` |
| Zero-content formal object | Each `d=0` owner is compared in the one-variable nonnegative-rational Hahn ring using `z_g=exp(-s ell(g))`; it is not silently inserted into `R_+` |
| Analytic domain | `K(delta,T,R)={1+delta<=Re(s)<=R, |Im(s)|<=T}` for every `delta>0`, finite `T>=0`, and finite `R>=1+delta`; local uniformity on `Re(s)>1` means uniformity on each such compact rectangle |
| Limit orders | (i) fixed panel then infinite `k->infinity`, then certified cofinal panel growth; (ii) panel growth then infinite `k->infinity` only after a uniform bound; (iii) infinite diagonal `N_k=k!`, `m_k=2^k`; the finite `k<=8` prefix validates none of these limits |
| Ordered endpoints | `FULL_OWNER_RECOVERY` first; separately `CONTENT_ONE_SUBPRODUCT_ANALYTIC`; the second cannot rescue or relabel failure of the first |
| Determinant convention | Finite/growing reciprocal owner product only; no Fredholm determinant or continued global determinant is declared |
| Forbidden adaptations | Content-dependent rescue factors, owner weights, changed tower, changed panel after outcomes, prime/zero targets, best-seed reporting |

## Data strategy

**Data type:** read-only P27 exact artifacts plus later exact, target-blind
owner panels generated under the frozen order.  
**Sampling:** deterministic censuses of declared prefixes, not statistical
samples.  
**Time frame:** inherited P27 Round-5/8 source snapshot and the new frozen
panel specification.

Primary inherited bindings, relative to the P27 directory:

| Artifact | SHA-256 | Role |
|---|---|---|
| `results/round5_cocompact_homology_escape_ledger.csv` | `0c74333b63f6027b16d134f19a320b8148e7fab6f86fa204d213c801106fe825` | Three certified content-one owners and marked group convention |
| `results/round5_cocompact_homology_escape_validation.json` | `afdc51ca7ecfbd8777955c7438f08d4580e6b924419a807191e097b0292d9c10` | Read-only source validation |
| `results/round8_renormalization_quadrants.csv` | `879ce8aec4e041e7cbba947706319511d99bb72592421584e76bbe47fad5ae57` | Frozen four-quadrant factor convention |
| `results/round8_renormalization_prefix_coefficients.csv` | `63f9632a0a715be26545e645a0f1d238e3ff24baec70fd8f478f1eda6c12c132` | Exact coefficient replay baseline |
| `results/round8_homology_renormalization_summary.json` | `c482c0e48fb1036faed37f123fbdec0b1c54f757a75f35e8a24cee27cb242b1a` | Candidate identity, boundary, and route baseline |

## Proof-first analytical framework

### P1 — complete owner-panel construction

Panel construction is governed by a fail-closed interface rather than an
unnamed “normal form.” The fixed presentation is

```text
Gamma = <a1,b1,a2,b2 | [a1,b1][a2,b2]=1>,
alphabet = a1<a1^-1<b1<b1^-1<a2<a2^-1<b2<b2^-1.
```

Before execution, one immutable binding for `SG2OwnerCanonical-v1` must name
the exact theorem/proof or verified algorithm, version, implementation hash,
serialization version, and test-vector manifest, and must implement:

```text
equality_normal_form(word)
oriented_conjugacy_canonical(word)
primitive_root(word) -> (primitive_owner, exponent)
enumerate_prefix(stratum, m) -> (ordered owners, completeness_certificate)
verify_certificate(payload)
```

The contract must guarantee termination and the following biconditionals:
normal forms agree iff group elements agree; oriented canonical representatives
agree iff elements are conjugate in `Gamma`; the root exponent is maximal and
the returned root is primitive; the prefix contains exactly the first `m`
eligible oriented primitive owners under the registered order. Canonicalize an
inverse independently and link it; never quotient by orientation.

Candidate raw words are processed in freely reduced shortlex order. The owner
order is `(canonical symbol count, alphabet-lex canonical word, serialized
bytes)`. A prefix certificate must store the presentation/alphabet/contract
hashes, raw-enumeration frontier, proof that no unprocessed raw word can map to
an earlier canonical owner, all accepted canonical representatives, equality
and conjugacy decisions, root witnesses/completeness certificates, inverse
IDs, exact abelianization vectors, content, exclusion reasons, and
`unresolved=0`. Thus the interface must prove prefix completeness; a search
frontier alone is not evidence.

The interface defines the theorem family for every integer `m>=1`. For each
requested finite diagnostic size in `{8,16,32,64,128}` or diagonal-prefix
size `{2,4,8,16,32,64,128,256}`, and each stratum `all,0,1,2,3`, the terminal
panel status is exactly one of:

```text
CERTIFIED_PREFIX
PANEL_NOT_EVALUABLE
INSUFFICIENT_CERTIFIED_POPULATION(stratum,m)
```

No panel is padded, re-ordered, or replaced after outcomes. The interface is
currently **UNBOUND**, so this Phase-1 file reports no panel as constructed.
The preexecution test-vector manifest is outcome-independent. It contains the
first 64 freely reduced raw words and their inverses; for `i=1,...,32`, the
known-conjugate pair `(w_i,c_i w_i c_i^-1)`, where `w_i` and `c_i` are the
`i`-th and `(i+32)`-th nonidentity freely reduced shortlex words; the relator,
its inverse, and all cyclic shifts as identity/equality fixtures; and square
and cube inputs of `a1*b1^j` for `j=0,...,15`, whose primitive base status must
be certified independently from the primitive abelianization vector
`(1,j,0,0)`. It must be serialized and hashed before any scientific prefix is
requested. If the contract cannot make every required decision exactly, or if
an expected fixture verdict lacks a separate word-equation/abelianization
proof, the panel endpoint remains not evaluable.

### P2 — general-content lift theorem

For `d=d(g)>=1`, put `q_N(g)=gcd(N,d)`. Prove

```text
order_N(g)              = N/q_N(g),
primitive lift count    = N^3 q_N(g),
physical lift period    = (N/q_N(g)) ell(g).
```

The proof must separately certify that the lifted components are primitive.
After the frozen `1/N` clock and `1/N^3` logarithmic normalization, derive the
exact owner factor

```text
F_N,g(s) = (1 - exp(-s ell(g)/q_N(g)))^(-q_N(g)).
```

For `d=0`, the deck-group order is one, the primitive lift count is `N^4`, the
physical lift period is `ell(g)`, the rescaled period is `ell(g)/N`, and the
normalized exponent is `N`. The separately typed factor to prove is

```text
F_N,g^(0)(s) = (1 - exp(-s ell(g)/N))^(-N).
```

It is never obtained by substituting `d=0` into the `d>=1` formula. Define the
one-owner Hahn ring

```text
H_g = {sum_(q in S) a_q z_g^q : a_q in Q,
       S subset Q_{>=0} is well ordered},
```

with equality by every rational-exponent coefficient projection and
`z_g=exp(-s ell(g))` only at scalar specialization. Both
`(1-z_g^(1/N))^(-N)` and base `(1-z_g)^(-1)` lie in `H_g`. For every `N>1`,
the registered fixed-`N` disposition is an ownerwise mismatch if the proof
verifies the coefficient at exponent `1/N`. No multivariate `d=0` product is
needed because one certified mismatch terminates universal recovery. The
separate scalar-limit proof obligation is to establish
`F_N,g^(0)(s)->+infinity` for each real `s>0`; until that proof is closed its
scalar-limit field is `D0_SCALAR_LIMIT_NOT_EVALUATED`, while the fixed-`N`
recovery obstruction remains separately typed.

### P3 — ownerwise recovery/obstruction theorem

Let `O_+` be the countable set of certified oriented primitive owners with
`d(g)>=1`. For a finite `F subset O_+`, put

```text
m_F = (u_g : g in F),
R_(F,D) = Q[u_g : g in F] / m_F^(D+1).
```

If `F subset F'`, the transition map sets variables in `F'\F` to zero; if
`D<=D'`, it truncates total degree. The ambient ring is the inverse limit

```text
R_+ = inverse-limit_(F,D) R_(F,D).
```

An element is determined by its coefficient at every finite-support owner
monomial. Equality and coefficientwise convergence mean equality or eventual
stability under every projection `pi_(F,D)`. A finite panel product embeds by
using factor one for every owner outside the panel, and certified finite owner
sets are directed by inclusion. This definition makes panel serialization
irrelevant while preserving every owner coordinate.

For `d=d(g)>=1`, set `u_g=exp(-s ell(g)/d)` only as notation before scalar
specialization. With `q_N=gcd(N,d)`, compare in `R_+`

```text
tower factor B_N,g = (1-u_g^(d/q_N))^(-q_N),
base factor  B_g   = (1-u_g^d)^(-1).
```

The proof obligations are:

- for `d=1`, prove `B_N,g=B_g` for every `N`;
- for `d>1`, once `d|N_k` on the infinite factorial schedule, prove or refute
  equality by an explicit coefficient projection to the singleton owner
  `{g}` at a declared degree;
- for `d=0`, use only the separate Hahn-ring comparison in P2.

Because a singleton projection kills every other owner variable, a proved
mismatch cannot cancel against another owner or disappear under a different
certified panel order. No scalar length evaluation may precede this formal
decision.

The primary endpoint `FULL_OWNER_RECOVERY` has exactly three dispositions:

```text
FULL_OWNER_RECOVERY_PROVED
FULL_RECOVERY_OBSTRUCTED_OWNERWISE(owner_id,content,N_or_tail,coefficient)
FULL_RECOVERY_NOT_EVALUABLE(reason)
```

The first requires a theorem quantified over every oriented primitive owner,
not a finite prefix. One certified owner mismatch triggers the second. An
unbound canonicalization/panel interface, an uncertified owner, or incomplete
coverage triggers the third. This Phase-1 blueprint predeclares the proof and
stopping rules but reports none of the three as a scientific result.

Their scientific interpretations are frozen: proved universal recovery would
be a formal statement about this nonresidual calibrator only; an ownerwise
obstruction means the fixed normalization is content-sensitive and cannot
define the full base owner product; not evaluable means the ownership/exhaustion
frame did not close and is neither positive nor negative evidence.

### P4 — growing-panel and analytic theorem

For finite positive-content owner set `F`, define the localization

```text
A_F = Q[u_g:g in F][(1-u_g^r)^(-1):g in F, r>=1]
```

containing every displayed finite tower/base factor, and define only the
finite evaluation

```text
sigma_(s,F)(u_g) = exp(-s ell(g)/d(g)).
```

Because all denominators are nonzero for `Re(s)>0`, this is a well-defined
algebra homomorphism `A_F -> C` and maps the formal factors to their scalar
factors. There is no automatic scalar map from all of `R_+`: an infinite
specialization `sigma_s` is declared only if a proof gives an absolutely
summable owner tail, uniformly on the claimed compact set, so that finite-panel
evaluations converge and are independent of certified cofinal exhaustion.

The analytic domain is the genuine compact rectangle

```text
K(delta,T,R) = {s in C : 1+delta <= Re(s) <= R, |Im(s)| <= T},
```

with universal quantifiers `delta>0`, finite `T>=0`, and finite
`R>=1+delta`. “Locally uniform on `Re(s)>1`” means uniform on every such
rectangle; no unbounded half-strip norm is claimed.

The theorem-level schedule is `N_k=k!`, `m_k=2^k` for every integer `k>=1`.
Each iterated limit and the diagonal limit quantifies over all sufficiently
large `k`. A future execution may inspect only `1<=k<=8`; that finite prefix is
logged as a consistency certificate and cannot validate convergence,
cofinality, or limit interchange. The neighboring stress schedule is
`N'_k=2*(k!)` for every `k>=1`, with its own separately labeled finite prefix.

After the full-owner endpoint in P3 is recorded, a separate secondary endpoint
may study only the content-one owner set:

```text
CONTENT_ONE_SUBPRODUCT_LOCALLY_UNIFORM
CONTENT_ONE_SUBPRODUCT_OBSTRUCTED
CONTENT_ONE_SUBPRODUCT_NOT_EVALUABLE
```

It requires a certified cofinal exhaustion, absolute tail bound on every
`K(delta,T,R)`, and explicit justification of each iterated/diagonal order.
Success cannot change `FULL_RECOVERY_OBSTRUCTED_OWNERWISE` or
`FULL_RECOVERY_NOT_EVALUABLE`, cannot be described as the full primitive
product, and cannot rescue any residual inverse-limit owner.

## Target-blind exact computational plan

1. Verify all inherited hashes and reject any candidate-identity drift.
2. Refuse panel generation while the `SG2OwnerCanonical-v1` theorem,
   implementation, serialization, and test-vector manifest remain unbound.
3. Request each frozen panel size and emit the entire prefix-completeness
   certificate. Preserve `PANEL_NOT_EVALUABLE` and
   `INSUFFICIENT_CERTIFIED_POPULATION` rather than adapting the panel.
4. For every certified `(owner,N_k)` in the finite execution prefix
   `1<=k<=8`, derive `q_N`, deck order, component count, rescaled period
   descriptor, normalized exponent, and formal factor using exact integers.
5. Expand formal coefficients through total degree 24 as a finite consistency
   diagnostic and record the first mismatch projection; this cannot prove a
   theorem quantified over all owners or all `k`.
6. Keep all-owner, `d=1`, `d=2`, `d=3`, and `d=0` panel statuses separate and
   use no arithmetic or target label in their selection.
7. Rebuild twice in isolated trees and require byte identity; run an
   independently implemented certificate verifier and coefficient checker.
8. Only after exact finite ledgers close may interval arithmetic evaluate
   scalar factors on frozen grids inside `K(1/2,25,3)` and `K(1/4,50,5)`;
   these are diagnostics on compact rectangles, never proof of equality,
   convergence, cofinality, or a limit.

## Frozen controls

| Control | Frozen role |
|---|---|
| `d=2` and `d=3` primitive-owner panels | Detect whether one universal `1/N`, `1/N^3` normalization survives higher content |
| `d=0` primitive-owner panel | Stress the order-one/null-homology regime under a separately derived formula |
| Raw/renormalized quadrants `Q00`, `Q01`, `Q10`, `Q11` | Preserve the inherited intervention comparison; `Q11` is primary, the other three are controls |
| Row permutation / panel-order reversal | Serialization and finite commutative-product reproducibility only; not analytic evidence |
| Distinct certified cofinal exhaustions | Analytic robustness control only after absolute convergence is proved for both; without that proof no rearrangement conclusion is allowed |
| Infinite schedules `N_k=k!` and `N'_k=2*(k!)` | Theorem-level stress sequences for every `k>=1`; their `k<=8` prefixes are finite diagnostics only, and no best schedule may be selected |
| Marked-metric controls | The proof must quantify over every marked hyperbolic metric; secondary stress points use the frozen Fenchel--Nielsen tuples below |

The three target-blind asymmetric Fenchel--Nielsen stress points `(cuff
lengths; twists)` are

```text
M1 = ((1, 4/3, 7/5);   (1/11, -2/13, 3/17)),
M2 = ((6/5, 3/2, 11/7);(-1/9,  2/15, 4/21)),
M3 = ((5/4, 8/5, 13/8);(2/19, -3/23, 5/29)).
```

They are metric stress controls, not asserted arithmetic/nonarithmetic
classifications. The exact content obstruction is metric-independent; a
favorable or unfavorable scalar grid cannot alter it.

## Validity criteria

| Criterion | Required strategy |
|---|---|
| Construct validity | Keep residual and pure-homology towers, physical/rescaled clocks, raw/normalized multiplicities, and owner content as separate typed fields |
| Panel completeness | Bound `SG2OwnerCanonical-v1` contract plus exact canonical-prefix certificate at every declared `m`; zero unresolved equality, conjugacy, or primitivity rows; fail-closed insufficient-population status |
| Formal validity | Use `R_+`, its finite-support projections, and the separate `d=0` Hahn object; establish singleton-owner mismatch before scalar specialization |
| Algebraic validity | Integer proof of order and lift count plus exact coefficient comparison; no floating equality decision |
| Analytic validity | Explicit absolute/local-uniform tail bound on every claimed finite `K(delta,T,R)`, an infinite-`k` proof, and an explicit order-of-limits justification |
| Reliability | Two byte-identical builds and an independent read-only verifier |
| Target blindness | Interface version, owner order, panel sizes/statuses, metric controls, compact domains, infinite schedules, and finite prefixes are frozen before outcomes and use no prime/zero targets |
| External validity | Structural theorem tested across homology-content strata and quantified over marked metrics; no arithmetic specificity inferred |
| Route validity | A0 remains absent; finite A1 certificates do not automatically become A2 |

## Kill gates

- Any inherited hash mismatch or attempt to merge the residual and homology
  candidates: **STOP — candidate identity failure**.
- Any incomplete normal-form, conjugacy, or primitivity decision before a panel
  prefix closes, any unbound interface contract, or any absent prefix proof:
  emit `PANEL_NOT_EVALUABLE`; **STOP — growing panel uncertified**.
- Fewer than `m` certified owners in a requested stratum: emit
  `INSUFFICIENT_CERTIFIED_POPULATION(stratum,m)`; do not pad, replace, shrink,
  or reorder the panel.
- Any need for content-dependent clock, exponent, owner weight, or panel repair:
  **STOP_SCOPED — that is a new candidate**.
- Any higher-content owner whose exact factor differs from the base factor:
  emit `FULL_RECOVERY_OBSTRUCTED_OWNERWISE`; **STOP the full-owner recovery
  claim** and do not hide it by scalar aggregation.
- Any certified `d=0` factor mismatch at `N>1`: emit the separately typed
  ownerwise obstruction; do not apply the `d>=1` formula or await a favorable
  scalar limit.
- Any unproved primitive tail bound: **STOP the local-uniform/global-product
  claim**; set the content-one analytic endpoint to not evaluable and retain
  only whatever exact formal endpoint was independently proved.
- Any use of `k<=8` as convergence, cofinality, diagonal-limit, or interchange
  evidence: **STOP — finite prefix cannot carry an infinite limit**.
- Any disagreement among limit orders without a common uniform bound: report
  noncommutation/undetermined status; do not select the favorable order.
- Any attempt to use a positive content-one result to alter P27's residual
  `A1_FAIL`, to supply A0, or to open Route B: **STOP_SCOPED**.

## Limitations by design

- The canonical word order is reproducible only after its fail-closed interface
  and prefix theorem are bound; even then it is a panel device, not a natural
  arithmetic ordering.
- The finite `k<=8` prefix and coefficient degree 24 are certificate
  diagnostics only and cannot approximate a theorem-level limit by themselves.
- The exact factor theorem can disprove full recovery without establishing
  analytic continuation or a Fredholm determinant.
- A locally uniform content-one subproduct, if proved, remains a restricted
  nonarithmetic calibrator and cannot overwrite the full-owner endpoint.
- Metric universality strengthens the proves-too-much control and weakens, not
  strengthens, arithmetic specificity.
- Novelty remains **PROVISIONAL** pending Phase-2 source verification.

## Ethical considerations and human-subjects status

This theoretical and computational mathematics study involves no human
participants, personal data, animals, clinical material, or intervention.
Human-subjects administrative review is **not applicable**.

## Reporting standard

- **Recommended discipline standard:** theorem/proof plus exact
  computer-assisted certificate reporting; distinguish `PROVED`,
  `NUMERICALLY_CERTIFIED`, `NUMERICAL_OBSERVATION`, and `OPEN`.
- Report panel definitions, all limit quantifiers, convergence domains, tail
  bounds, negative controls, first mismatch coefficients, source hashes, and
  deterministic receipts.
- **EQUATOR guideline:** none applicable; this is not a human, clinical,
  observational, or systematic-review design.
- A strict obstruction, a positive restricted subproduct, or an analytic
  nonclosure are all publishable outcomes under the same frozen design.

## Preregistration (#672 declaration only)

- Recommended: **Yes**, before execution, because the panel, domains,
  normalizations, controls, and orders of limits are confirmatory.
- Platform: **OSF Registries** if the scholar later supplies a completed record.
- Status: **not provided**.
- Completed artifact declaration: **not_provided**.
- Companion handle: **none**.
- Sidecar/advisory ownership: **dispatcher only**. This Phase-1 architect file
  does not compute a digest or create/update `preregistration-artifact/1.0`;
  the #672 dispatcher operation has not been run.

## Route boundary

P32 cannot recover arithmetic A0: the pure homology-cover calculation is
generic across marked metrics and contains no intrinsic rational-prime owner or
`log p` clock. A formal or locally uniform result remains an A1/A2-boundary
calibration until a separately complete Route-A evaluation says otherwise.
P27's residual owner stays rejected and Route B stays closed.

## Phase boundary

This blueprint authorizes no scientific execution by itself and contains no
Phase-2 bibliography, Phase-3 synthesis, manuscript draft, review, result,
claim registration, Route promotion, or canonical refresh.
