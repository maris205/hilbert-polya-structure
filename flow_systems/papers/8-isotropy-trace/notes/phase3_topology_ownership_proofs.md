# Paper 8 Phase-3 topology and ownership proofs

**Date:** 2026-08-14 (Asia/Shanghai)  
**Decision:** **PASS WITH SCOPED SPLIT**  
**Phase scope:** P8-1, P8-7, the non-operator part of P8-8, and P8-9 only

The actual one-orbit topology/Haar/amenability gate passes.  The packet
Hausdorff/LCH gate does not pass: packet compactness is retained only in the
open-cover (quasi-compact) sense, and packet `Gamma_p` Hausdorffness/LCH and
`Q_p` Hausdorffness remain `OPEN`, so every packet completion, packet normal
trace, and packet same-map analytic transport that needs those hypotheses is
`NOT_TESTABLE`.

This note proves a source-clock scalar ledger with coefficient one per rational
closed point.  It does **not** identify that ledger with a packet groupoid trace.
That ownership separation is load-bearing.

## 1. Exact input lock

The following files were read in full before the proofs below.

| Input | SHA-256 |
|---|---|
| `research_protocol.md` | `e1149ebd9609de24e0df00dcaeafdbcd31ee973e8ebe04b15cf86541f8084535` |
| `candidate_lock.md` | `8a5a460bac51843e532c9894fcb99470247c7de7833449c3660813ccd183d64e` |
| `phase2_domain_amendment.md` | `412e6d24c43ab5a995d135c6ecb207f5225414fac223fcf63080486af6fc3de3` |
| `phase2_final_gate.md` | `22fd0376ad8e69e6816b3d005d88f4cde2cc5f4b243749c95aa2f19ab8164a3f` |
| `phase2_source_topology_audit.md` | `f76dc87df56bacc54ea420447b28cb37020fc2625fa97d2eca2f173278ee83a3` |
| `phase2_groupoid_source_audit.md` | `39fcd460018a38a2b23107b0cb2f59195b7fa4110ad6742b66a334af0f4bad42` |
| `phase2_trace_source_audit.md` | `101d447a238cbf9ec6ea33a78b3f6be7456a1be30fdc206e13db91697d75c5f0` |

No active lock, gate, manuscript, YAML evaluation, or source file is changed by
this note.

### Status language

- `SOURCE_THEOREM`: stated in the retained primary source at the cited locator.
- `DERIVABLE_NEW_LEMMA` or `DERIVABLE_NEW_THEOREM`: proved here or in the
  hash-locked Phase-2 audit from source-owned inputs plus stated standard
  theorems.
- `OPEN`: a meaningful mathematical assertion for which the retained evidence
  and present proofs do not close the hypotheses.
- `NOT_TESTABLE`: a downstream assertion whose owner or prerequisite object is
  unavailable because an upstream gate remains open.
- `N/A (typed boundary)`: the field is not part of the declared object type;
  this is not a pass and cannot be used to promote that object to a trace or
  operator.

## 2. Source premises and exact boundary

Fix a rational prime `p` and write `L_p=log p`.

1. Deninger survey Theorem 4.2 (physical pp. 11--12) gives the compact packet
   `Gamma_p` and compact periodic orbits.  This is `SOURCE_THEOREM`.
2. Deninger v4 Theorem 6.1 (physical p. 39) gives exact stabilizer
   `L_p Z` for every point of `Gamma_p`.  This is `SOURCE_THEOREM`.
3. Deninger v4 Proposition 7.6, Proposition 7.7, Corollary 7.8, and Corollary
   7.9 (physical pp. 44--45), together with the admissible-`E` paragraph after
   Theorem 7.10 (physical p. 47), support the Phase-2 proof that the relevant
   pre-suspension and the `E_f` spaces are second countable.  Hence each
   `Gamma_p` is second countable.  This is `DERIVABLE_NEW_LEMMA`.
4. Those source statements do not prove the diagonal suspension quotient
   Hausdorff.  Therefore `Gamma_p` Hausdorffness and LCH remain `OPEN`; compact
   is not silently read as compact Hausdorff.
5. The corrected actual-`E_f` restriction in the topology audit proves that
   every inherited orbit `O_x subset Gamma_p` is homeomorphic to Morishita's
   Hausdorff circle `R_+/p^Z`, with the source/target flow sign stated there.
   The source orbit has the same exact stabilizer.  This limited result is a
   `DERIVABLE_NEW_LEMMA`; it supplies one-orbit T1/T2 only and forgets the
   transverse packet coordinate.

The disjoint union in Deninger Theorem 6.1 is a set decomposition, not a
source theorem that the inherited all-prime periodic subspace has the
topological-coproduct topology.  Deninger v4 Remark 2 after Theorem 7.10
(physical p. 47) expressly prevents upgrading the relevant continuous
bijections to homeomorphisms in general.  Per-prime groupoids, a separately
chosen topological coproduct, and the inherited global periodic set therefore
remain three different typed objects.

## 3. P8-1: actual one-orbit topology, Haar, and amenability

### Theorem 3.1 — one actual source orbit closes the topological gate

Let `x in Gamma_p`, let `O_x={phi^t(x):t in R}` with its inherited topology,
and put `L=L_p`.  Then:

1. `O_x` is homeomorphic to `R/(L Z)`;
2. `O_x` is compact Hausdorff, locally compact, and second countable;
3. the inherited flow is translation by `R`, up to the already recorded
   harmless source/target sign; and
4. its stabilizer is exactly `L Z`.

**Proof.**  Item 1 is the corrected genuine-`E_f` one-orbit lemma in the
hash-locked topology audit: the restricted Morishita map is a continuous
flow-anti-equivariant bijection from the compact source orbit to the Hausdorff
circle `R_+/p^Z`, hence a homeomorphism.  Logarithmic time identifies the
latter with `R/(L Z)`.  Items 2--4 follow from that homeomorphism and Deninger
v4 Theorem 6.1.  The possible sign changes translation `t` to `-t`; it changes
neither topology, stabilizer, Haar measure, nor amenability.  QED.

This proof applies to **every already chosen actual orbit**, but it does not
canonically choose one orbit from the packet and it is not a packet chart.

### Theorem 3.2 — the locked one-orbit action groupoid has a Haar system

Use the locked arrow convention

```text
G_x = O_x rtimes R,
s(z,t)=z,
r(z,t)=phi^t(z).
```

Then `G_x` is a second-countable LCH Hausdorff topological groupoid.  Its
arrow space is `O_x x R`.  For `y in O_x`, define the measure on the range
fibre `G_x^y=r^(-1)(y)` by

```text
lambda^y(F) = integral_R F(phi^(-t)(y),t) dt,
F in C_c(G_x).
```

The family `(lambda^y)_(y in O_x)` is a continuous left Haar system.

**Proof.**  Theorem 3.1 and the standard product topology give the LCH,
Hausdorff, and second-countability assertions; the action groupoid structure
maps are continuous because the source flow is continuous.  The map
`t -> (phi^(-t)y,t)` parametrizes `G_x^y`, so each `lambda^y` is the pushforward
of Lebesgue Haar `dt` and has full fibre support.

For continuity, the projection of `supp(F)` to the time coordinate is a
compact set `C`.  The function `(y,t) -> F(phi^(-t)y,t)` is continuous and is
zero outside `O_x x C`; uniform continuity on the relevant compact set shows
that `y -> lambda^y(F)` is continuous.

For left invariance, take an arrow `gamma=(z,s)` from `z` to
`y=phi^s(z)`.  The range-fibre arrow with time `t` ending at `z` is
`eta_t=(phi^(-t)z,t)`, and

```text
gamma eta_t = (phi^(-t)z,t+s)
            = (phi^(-(t+s))y,t+s).
```

The substitution `v=t+s` and translation invariance of `dt` give
`(L_gamma)_*lambda^z=lambda^y`.  QED.

### Theorem 3.3 — one-orbit amenability and completion gate

`G_x` is amenable.  Consequently its full and reduced groupoid crossed-product
completions agree.

**Proof.**  `R` is an amenable locally compact group.  Anantharaman-Delaroche,
Examples 2.7(2) (manuscript p. 6 / published p. 4158), states that every action
of an amenable locally compact group is amenable.  Her Theorem 5.3 (manuscript
p. 14 / published p. 4166) supplies full/reduced equality under the hypotheses
now verified in Theorem 3.2.  QED.

This theorem proves only the P8-1 one-orbit completion gate.  It does not prove
the exact tensor model, Floquet/Poisson formula, trace-class statement,
nonnormality, or any P8-2--P8-6 operator theorem.

### Proposition 3.4 — the three Haar normalizations are distinct

Under `O_x ~= R/(L Z)`, with counting Haar (unit mass per element) on
`L Z`:

- `dt` is arrow Haar on the acting group and on the range fibres;
- quotient length Haar `du` on `O_x` has total mass `L`; and
- `du/L` is the invariant probability on the orbit.

The Weil normalization is

```text
integral_R g(t) dt
 = integral_[0,L) sum_(n in Z) g(u+nL) du.
```

Uniqueness of Haar measure on the compact homogeneous circle implies that
every finite invariant Borel measure on this one orbit is a scalar multiple of
`du`; fixing probability selects `du/L`.  The one-orbit quotient is a point,
so no transverse choice occurs.  Neither `du` nor `du/L` is the arrow measure
`dt`, and neither defines a probability on a nontrivial packet quotient.

### P8-1 one-orbit verdict

`DEN-EF-ORBIT-ACTION-GRPD` is **PASS** for topology, Haar, amenability, and
full/reduced existence.  The result is a `DERIVABLE_NEW_THEOREM` built from an
actual source orbit plus the cited groupoid source theorems.  It is not a
Deninger/Morishita source theorem and supplies no packet analytic bridge.

## 4. P8-1 packet remainder: `K_p` and `Q_p`

### Proposition 4.1 — the intrinsic free compact action

Put `K_p=R/(L_p Z)`.  The source `R` action on `Gamma_p` descends to a
continuous free `K_p` action.

**Proof.**  The exact common stabilizer `L_p Z` is the common kernel, so the
action is constant on cosets.  The quotient map `R -> K_p` is open; hence its
product with the identity on `Gamma_p` is an open quotient map, and the
descended action is continuous by the quotient property.  If `[t] in K_p`
fixes a point, then `t` belongs to that point's exact stabilizer `L_p Z`, so
`[t]=0`.  Thus the action is free.  QED.

This is `DERIVABLE_NEW_LEMMA`, not a source-attributed group action theorem.

### Proposition 4.2 — exact properties of the quotient

Let

```text
q_p: Gamma_p -> Q_p=Gamma_p/K_p
```

carry the quotient topology.  Then:

1. `q_p` is an open quotient map;
2. `Q_p` is compact in the open-cover (quasi-compact) sense; and
3. `Q_p` is second countable.

**Proof.**  For open `U subset Gamma_p`, its saturation is
`q_p^(-1)(q_p(U))=union_(k in K_p) kU`, hence open.  Therefore `q_p(U)` is
open.  The continuous image of the compact packet is quasi-compact.  If
`(B_n)` is a countable base of `Gamma_p`, then the open sets `q_p(B_n)` form a
base of `Q_p`: lift an open neighbourhood, choose a contained `B_n`, and use
openness of `q_p`.  QED.

### Mandatory non-conclusions

The following remain `OPEN`:

- `Gamma_p` Hausdorffness and LCH;
- `Q_p` Hausdorffness or even the separation consequences needed for the
  usual compact-Hausdorff quotient theory;
- proper/principal-bundle status and local triviality of `q_p`; and
- any homeomorphism `Q_p ~= B_p` or packet product chart.

Freeness alone closes none of these items because the domain has not been
proved Hausdorff.  Consequently the standard LCH groupoid completion of
`G_p=Gamma_p rtimes R`, packet Haar/completion theorems, and packet trace
disintegrations remain `NOT_TESTABLE`.  This is not a refutation of their
existence; it is the exact upstream gate.

### P8-1 packet verdict

The topological action groupoid is a legitimate
`DERIVABLE_NEW_DEFINITION`, and the continuous action, common isotropy,
compactness, second countability, `K_p` action, and quotient properties above
pass.  The **analytic packet branch of P8-1 remains `NOT_TESTABLE`** because
Hausdorff/LCH is open.

## 5. P8-7: what a section-free quotient average does and does not prove

### Proposition 5.1 — continuous orbit averaging without a section

For `h in C(Gamma_p)`, define

```text
(A_p h)(q_p(x)) = integral_0^(L_p) h(phi^t(x)) dt.
```

This is a well-defined positive linear map

```text
A_p: C(Gamma_p) -> C(Q_p),
```

with `A_p(1)=L_p`, `||A_p h|| <= L_p ||h||`, and
`A_p(h circle phi^s)=A_p h` for every `s in R`.

**Proof.**  Replacing `x` by `phi^s(x)` translates an `L_p`-periodic
integrand through one full period, so the value is representative-independent.
The pullback `(A_p h) circle q_p` is continuous by parameter-dependent
integration over the compact interval `[0,L_p]`.  Since `q_p` is a quotient
map, `A_p h` is continuous.  Positivity, the norm bound, the value on `1`, and
flow invariance are immediate.  QED.

### Corollary 5.2 — the maximal presently legal quotient functional

For any **given Borel probability** `nu` on `Q_p`, define

```text
Lambda_(p,nu)(h) = integral_(Q_p) A_p h(q) dnu(q).
```

Then `Lambda_(p,nu)` is a positive, flow-invariant functional on
`C(Gamma_p)` and `Lambda_(p,nu)(1)=L_p`.  It is section-free.  For an invariant
observable `h=g circle q_p`,

```text
Lambda_(p,nu)(g circle q_p) = L_p integral_(Q_p) g dnu.
```

Thus two probabilities are detected whenever some `g in C(Q_p)` separates
them.  Time-only/constant observables are blind to `nu`.

This corollary deliberately says **functional**, not Radon packet measure and
not normal trace.  Because `Gamma_p` and `Q_p` are not known Hausdorff, the
compact-Hausdorff Riesz representation/disintegration step cannot be invoked.
The proof does not establish:

- a Radon lift of every `nu` to `Gamma_p`;
- exhaustion or uniqueness of invariant packet measures;
- separation of all distinct Borel probabilities by `C(Q_p)`;
- existence or variation of full packet groupoid traces; or
- a same-map relationship to either locked trace family.

On one actual orbit `Q={point}`, the functional is integration against the
actual length Haar `du`, and division by `L_p` gives the unique invariant
probability.  That special case cannot be promoted across the packet.

### P8-7 measure verdict

The section-free **continuous-function average** is
`DERIVABLE_NEW_LEMMA / PASS`.  The protocol's stronger Radon-lift,
invariant-measure-exhaustion, full-trace-variation, and packet-domain claims
remain `OPEN -> NOT_TESTABLE`.  No source-selected transverse probability or
cross-prime mass has appeared.

## 6. P8-7 domain ledger and source coefficient one

The following theorem concerns scalar measures on the time line.  It uses no
packet completion and is not a claim about a groupoid trace.

### Theorem 6.1 — local, finite, and positive-time scalar ledgers

For each prime define the locally finite measure on `R`

```text
R_p = L_p sum_(r in Z) delta_(r L_p).
```

For a finite set `S` of primes define

```text
R_S = sum_(p in S) R_p.
```

Finally define on `(0,infinity)`

```text
Theta_+ = sum_p L_p sum_(r>=1) delta_(r L_p).
```

Then `R_p`, `R_S`, and `Theta_+` are positive Radon measures on their stated
domains.  In particular, for `f in C_c^infinity((0,infinity))`,

```text
Theta_+(f) = sum_p L_p sum_(r>=1) f(r L_p)
```

is a finite sum.

**Proof.**  A single lattice is locally finite, and a finite sum of locally
finite measures is locally finite.  For `Theta_+`, put
`supp(f) subset [a,b]` with `0<a<=b`.  If `r log p in [a,b]`, then
`p<=exp(b)`, leaving finitely many primes; for each such prime,
`r<=b/log p`, leaving finitely many repetitions.  Thus every compact subset of
`(0,infinity)` meets finitely many atoms.  A locally finite positive Borel
measure on this LCH second-countable time domain is Radon.  QED.

### Proposition 6.2 — exact ownership of the coefficient

The cross-prime coefficient in Theorem 6.1 is exactly one because
`Spec Z` has one rational closed point `(p)` for each prime and the frozen
assembly uses counting measure on those source closed points.  `L_p` is the
source orbit clock and the length-Haar scale.  It is not a free transverse
mass.

This is a target-free T7 statement for the **scalar source-clock ledger**.
It is not a theorem that:

- the packet contains one orbit;
- a packet probability or packet trace has total mass one;
- `R_p` is the restriction of `DEN-EF-GRPD-TRIVCHAR-TRACE-FAM`;
- `Theta_+` is evaluation of a global all-prime operator; or
- arbitrary weights `w_p` are licensed.  A choice of `w_p` defines a different
  candidate.

The domain split is necessary.  Summing the two-sided local combs over all
primes would put mass `sum_p L_p=infinity` at time zero and is not locally
finite on `R`.  Finite-prime assembly is algebraic and finite.  The global
unweighted statement is legal only on the frozen positive-time test class.

### P8-7 domain verdict

- local scalar comb: **PASS as a scalar measure**, but its equality to the
  locked local groupoid trace restriction is `NOT_TESTABLE` here;
- finite-prime scalar sum: **PASS as a finite scalar assembly**, with no global
  `C*` or `L1` owner;
- positive-time record: **PASS as a Radon measure**, exactly of the type frozen
  for `DEN-EF-GRPD-TIME-RETURN-POS`;
- weighted/all-time/global-operator extensions: **not part of this theorem**.

## 7. P8-8: blindness and falsification controls in scope

| Control | Exact outcome | Ownership consequence |
|---|---|---|
| singleton transverse base | The one-orbit topology, arrow `dt`, length `du`, probability `du/L`, amenability, and scalar comb all survive; the quotient is a point. | This validates the local theorem only; it does not show a nontrivial packet has no transverse ambiguity. |
| arbitrary transverse probability | For every given Borel `nu`, `Lambda_(p,nu)(1)=L_p`; the scalar time-only value is independent of `nu`.  If `g in C(Q_p)` separates two probabilities, `g circle q_p` distinguishes their functionals. | Time-only blindness does not imply equality or uniqueness of full packet measures/traces. |
| copied packet | Replacing a source component by `m` artificial copies and using counting measure multiplies the scalar ledger coefficient by `m`.  Probability-normalizing across the copies can instead hide the copy number from time-only observables. | Coefficient one comes from source closed-point counting, not from Haar or trace uniqueness.  A copied object is a different candidate. |
| one arbitrary clock `L>0` | All one-orbit topology/Haar/amenability proofs and the local comb work verbatim for `R/(L Z)`. | The local mechanism is generic; arithmetic credit comes only from the source derivation `L_p=log p`. |
| arbitrary clock family `(ell_j)` | A sufficient sharp ownership gate for the unweighted positive ledger is properness: for every `B`, only finitely many indices have `ell_j<=B`. | Without such a gate, clocks can accumulate at zero or occur with infinite multiplicity and destroy local finiteness.  Local formulas alone do not license a global ledger. |
| composite-only clocks `ell_n=log n` (`n>=4` composite) | The properness condition holds (`n<=exp(B)`), so the same scalar positive-time construction is locally finite. | Composite `n` are not closed points of `Spec Z`; treating each composite as a primitive component fails T7/A0 source ownership even though the analytic mechanism compiles. |
| inherited global union versus chosen coproduct | No source theorem identifies the two topologies.  Finite-prime sums need neither identification. | No compact-support, Haar, or trace claim may move from a chosen coproduct to the inherited periodic subspace. |

The arbitrary-family condition is more than cosmetic.  If infinitely many
clocks tend to zero, then on any fixed interval of positive length each
sufficiently small lattice contributes order-one total weighted mass, so the
unweighted positive ledger is not locally finite.  If infinitely many clocks
remain in a compact subinterval of `(0,infinity)`, their first repetitions
already give infinite mass there.

The following preregistered controls are operator-specific and are **not
proved or refuted in this note**: finite character grids, nontrivial-character
phases, regular-versus-trivial character comparison, point-evaluation
nonnormality, finite-corner extension, and the zero-time regular trace.  They
belong to P8-2--P8-6 and the sibling Phase-3 operator proofs.  The present
P8-8 verdict is therefore **PARTIAL PASS for the non-operator controls**.

## 8. P8-9: T0--T7 ownership certificate

The table records feasibility/ownership fields, not Route credit.  `P*` means
that only the explicitly stated subfield passes; it cannot be read as a full
pass.

| Typed record | T0 object | T1 topology/Borel | T2 flow/clock | T3 groupoid/Haar | T4 measure | T5 representation/trace | T6 test algebra/formula | T7 arithmetic promotion |
|---|---|---|---|---|---|---|---|---|
| `DEN-EF-ORBIT-ACTION-GRPD` | PASS: actual `E_f` orbit | PASS: inherited orbit is a Hausdorff circle | PASS: actual flow, exact `L_p` | PASS: LCH groupoid, `dt`, amenable, full=reduced | PASS locally: `du` or `du/L`; no transverse field | NOT TESTED here | NOT TESTED here | P*: source `(p),L_p`; no analytic amplitude/trace promotion |
| `DEN-EF-PACKET-ACTION-GRPD-P` | PASS as `DERIVABLE_NEW_DEFINITION` from actual packet/flow | P*: compact + second countable; Hausdorff/LCH OPEN | PASS: source flow and common `L_p` | P*: topological maps exist; standard Haar/completion branch NOT_TESTABLE | OPEN: no selected transverse/Radon packet measure | NOT_TESTABLE | NOT_TESTABLE | P*: source label/clock only; no packet/component mass |
| `DEN-EF-PACKET-ORBIT-QUOTIENT-Q` | PASS as intrinsic quotient; not `B_p` | P*: quasi-compact + second countable; Hausdorff/local chart OPEN | PASS: continuous free `K_p` action | N/A (typed quotient, not a groupoid) | P*: `A_p` and `Lambda_(p,nu)` functionals; Radon lift/exhaustion NOT_TESTABLE | N/A; supplies no trace | N/A; supplies no return formula | OPEN: quotient does not select packet or cross-prime mass |
| `DEN-EF-GRPD-REG-TRACE-FAM` | P*: tied to actual `G_p`, whose analytic gate is open | inherits packet T1 gate | PASS for clock only | NOT_TESTABLE at packet completion | NOT_TESTABLE | NOT TESTABLE in this note; no FNS/normal owner awarded | NOT TESTED | no mass promotion; zero-time claim not used |
| `DEN-EF-GRPD-TRIVCHAR-TRACE-FAM` | PASS locally / packet branch NOT_TESTABLE | PASS locally / packet T1 open | PASS locally | PASS for local groupoid only / packet NOT_TESTABLE | local `du` PASS; transverse packet field open | NOT TESTED: P8-5/P8-6 excluded | NOT TESTED: no Poisson claim here | source clock only; trace amplitude withheld |
| `DEN-EF-GRPD-TIME-RETURN-LOCAL` | P*: actual prime clock; trace owner unproved | scalar lattice PASS; packet transport open | PASS: `L_p` | NOT_TESTABLE as packet trace | time-only scalar is transverse-blind; no packet measure selected | NOT_TESTABLE as a trace restriction | PASS as scalar comb / trace equality NOT_TESTABLE | PASS for scalar unit coefficient only |
| `DEN-EF-GRPD-TIME-RETURN-FIN` | PASS: finite actual prime set | PASS on finite-labelled scalar time domain | PASS | N/A for scalar sum / no global groupoid | no hidden packet or cross-prime probability | N/A for scalar sum / local trace ownership withheld | PASS as finite sum / no global operator | PASS: one per source closed point in the finite set |
| `DEN-EF-GRPD-TIME-RETURN-POS` | PASS: actual source prime/clock fields; declared scalar type | PASS: Radon measure on `(0,infinity)` | PASS: repetitions `rL_p` | N/A by declared scalar-measure type | N/A: no transverse measure is asserted | N/A: expressly not a star-algebra trace | PASS: exact locally finite `Theta_+` | PASS for coefficient-one scalar ledger; no trace promotion |

### Certificate interpretation

1. T0--T7 closes completely only for the fields actually required by the
   one-orbit topology/Haar theorem and by the declared scalar positive-time
   measure.
2. A `PASS` in scalar T6/T7 does not repair packet T1, T3, T4, or T5.
3. `N/A` for a scalar measure is a type barrier: it forbids calling the record
   a groupoid trace, not permission to skip a trace proof.
4. The regular and trivial-character families may not borrow each other's
   completion, domain, normality, or Route fields.
5. The limited Morishita bridge supplies actual-orbit T1/T2 only.  Paper 7's
   product proxy supplies no missing packet T-field.

Thus P8-9 **passes as an ownership audit**, while several candidate theorem
fields legitimately remain `OPEN` or `NOT_TESTABLE`.

## 9. Route-A ceiling, kept separate from T0--T7

No coordinatewise maximum is taken across the following records.

| Record | Route status justified by this note | Reason and ceiling |
|---|---|---|
| source `DEN-WITT-Z-FIN` | unchanged: `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | Packet/clock source theorem is unchanged; this note does not turn the source packet into one canonically weighted orbit. |
| `DEN-EF-ORBIT-ACTION-GRPD` | at most `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | The unit orbit and clock are actual source data, but choosing one orbit and defining its groupoid supplies no canonical packet multiplicity or analytic trace amplitude. |
| `DEN-EF-PACKET-ACTION-GRPD-P` and `Q_p` | no promotion beyond the inherited source ceiling; packet analytic fields are `NOT_TESTABLE` | A new groupoid/quotient definition is not a source trace theorem, and Hausdorff/LCH plus measure ownership remain open. |
| regular and trivial-character trace families | no new Route tuple is earned in this scoped proof | P8-2--P8-6 trace/representation claims were deliberately not proved here.  Underlying A0/A1 source evidence cannot be relabelled as trace-family evidence. |
| local and finite time-return records | scalar prerequisites pass; trace-owned A1 promotion is withheld | Their locked interpretation as restrictions/assemblies still depends on P8-5/P8-7 same-owner theorems. |
| declared scalar aspect of `DEN-EF-GRPD-TIME-RETURN-POS` | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | Theorem 6.1 is a complete source-indexed closed-point/repetition Radon ledger with intrinsic clocks and source coefficient one.  This A1 credit belongs only to the typed scalar measure, not to a packet trace, a claim of one orbit per packet, or the source record itself. |

The positive-time A1 result remains `ROUTE_A_EXPLORATORY`: it owns no
dynamical zeta/Fredholm determinant (`A2_FAIL`), no continuation, functional
equation, Gamma factor, completed divisor, or Weil-compression structure
(`A3_FAIL`), and no natural quantization (`A4_FAIL`).  Route B remains closed,
`route_b_invocation_allowed=false`, and no Hilbert--Polya statement follows.

The composite-clock control is decisive for interpretation: local finiteness
and the repetition architecture are generic once a proper clock family is
given.  The actual record retains strong A0 only because `(p)` and `log p` are
source-derived rather than inserted or fitted; the same construction on
composite clocks receives no arithmetic promotion.

## 10. Scoped theorem status and stop boundary

| Target | Final status in this note |
|---|---|
| P8-1, actual one orbit | **PASS**: Hausdorff/LCH/second countable, explicit arrow Haar, amenable, full=reduced |
| P8-1, packet `Gamma_p rtimes R` analytic branch | **OPEN -> NOT_TESTABLE**: `Gamma_p` Hausdorff/LCH absent |
| `K_p` / `Q_p` | **PASS** for continuous free action, open quotient, quasi-compactness, second countability; **OPEN** for `Q_p` Hausdorff/local triviality/`B_p` |
| P8-7 quotient average | **PASS** at continuous-function level; packet Radon lift/exhaustion/full traces **NOT_TESTABLE** |
| P8-7 local/finite/positive scalar domains | **PASS** as stated scalar measures; no packet/global operator ownership |
| P8-8 | **PARTIAL PASS** for singleton/transverse/copy/clock/composite/coproduct controls; operator controls deferred |
| P8-9 | **PASS as an ownership/status certificate**, with no illegal transport or Route aggregation |

Work must stop at the following boundaries in this proof stream:

- do not construct `C*(Gamma_p rtimes R)` in the standard packet framework
  until packet Hausdorff/LCH is proved or a theorem with explicitly weaker
  hypotheses is separately frozen and audited;
- do not call `Lambda_(p,nu)` a packet Radon measure, FNS trace, normal trace,
  or exhaustive disintegration;
- do not identify `Q_p` with `B_p` or infer a product/principal bundle;
- do not identify `R_p`, `R_S`, or `Theta_+` with an operator trace without
  the exact P8-5/P8-7 same-owner proof;
- do not pass local orbit nonnormality, Poisson formulas, or finite corners to
  a packet completion; and
- do not turn a finite or positive-time scalar domain into a global all-prime
  `C*`, `L1`, determinant, A3, A4, or Route-B object.

Within those boundaries, there is no fatal topology/source obstruction to the
actual one-orbit theorem, and the coefficient-one positive-time scalar ledger
is exact and locally finite.
