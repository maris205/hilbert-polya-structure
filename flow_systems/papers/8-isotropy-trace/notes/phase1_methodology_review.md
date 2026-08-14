# Paper 8 Phase-1 independent methodology review

Review date: 2026-08-14  
Review scope: research architecture only; no Phase-2 source search, proof,
computation, or manuscript work  
Decision: **REVISE BEFORE PHASE 2**

## 1. Locked inputs and independence boundary

This review used only the two active Paper-8 design locks and the session-level
proposal and Route-A/Route-B evaluation roadmaps.  It did not use later Paper-8
notes, target-zero data, an Euler-product target, or web browsing.

| Input | SHA-256 verified at review start |
|---|---|
| `notes/research_protocol.md` | `51c85aae8262d6fb8597d49e6c23a1926ebb24ee3c3429d996228565b4d7a547` |
| `notes/candidate_lock.md` | `d1d11519bd8661be1a62f5cf7bdc34e14a929a79776c52001b2a0d362082cc8a` |

The proposal permits operator-algebraic analysis only while it remains tied to
the source flow.  The Route-A roadmap requires a fixed object, clock,
normalization, and data type, and forbids coordinatewise credit assembly.  The
Route-B roadmap is not entered here and its same-object requirements are used
only as a boundary check.

Severity conventions in this review are:

- **Critical:** the question or design is invalid without a fundamental
  replacement;
- **Major:** Phase 2 must not begin until a versioned lock amendment closes the
  issue;
- **Minor:** the core design survives, but the item must close before the
  affected theorem or Route claim is credited;
- **Observation:** useful boundary information that does not itself require a
  lock change.

Finding count: **0 Critical, 3 Major, 4 Minor, 3 Observations**.

## 2. Executive assessment

The local mathematical core is coherent and worthwhile: on an actual periodic
source orbit, P8-2--P8-6 can distinguish the normal regular/Plancherel record
from the return-sensitive trivial-isotropy-character record.  The design is
target-blind, exposes negative outcomes, separates Paper 7's proxy from the
source groupoid, and contains unusually strong stop rules.

The current locks nevertheless do not yet identify one packet-level object and
one primary question with enough precision to start Phase 2.  The same packet
candidate ID is used for a per-prime groupoid and for the all-prime packet
union, although those objects have different topology, test algebras, measure
choices, and trace domains.  In addition, the primary question presents two
claims that may both be true as competing alternatives and uses
`source-intrinsic`/`canonical` without an operational criterion.  Finally, the
common time-return restriction has no frozen local-versus-global domain or
quantified admissible measure class.  These are repairable design defects, not
reasons to abandon the project, but they are pre-Phase-2 blockers.

## 3. Severity-ranked findings

### M1 — Major: one candidate ID currently covers two different unit spaces

**Evidence.**  `candidate_lock.md` section 2 defines
`DEN-EF-PACKET-ACTION-GRPD` on
`X = disjoint_union_p Gamma_p` with the inherited source topology.  In
contrast, `research_protocol.md` section 3 freezes
`G_p = Gamma_p rtimes R`, and P8-1 asks for the topology and completion of
that per-prime object; cross-prime assembly is deferred to P8-7.  The notation
`disjoint_union` also does not decide whether the global topology is the
topological coproduct or the subspace topology inherited from the source.

**Impact.**  A per-prime compact packet groupoid, a family `{G_p}_p`, and one
global groupoid on the union are not interchangeable typed records.  Local
compactness, second countability, compact support of `a_f`, full/reduced
completion, invariant measures, direct-sum/integral structure, and trace
normalization can differ.  The locks themselves state that changing the unit
space or topology creates a new candidate, so proofs cannot be credited while
this ambiguity remains.

**Required repair.**  Introduce separate versioned records, at minimum, for:

1. the per-prime packet groupoid `G_p = Gamma_p rtimes R` (or an explicitly
   parameterized family of such records);
2. the single-orbit restriction `G_{p,x}|O_x`;
3. the source quotient
   `Q_p = Gamma_p/(R/L_p Z)`, after verifying that the induced compact-group
   action is continuous and free and that the quotient has the needed
   separation/countability properties;
4. the global all-prime groupoid, only if its exact source subspace topology is
   frozen and distinguished from a topological coproduct; and
5. the product-coordinate proxy already separately typed.

The free compact action, if proved, makes `Gamma_p -> Q_p` a source quotient
and may support a principal-bundle/disintegration theorem.  It does not supply
a global section, a product trivialization, or an identification
`Q_p = B_p`.  Any comparison with `B_p` still requires the appropriate T0--T7
fields and must preserve a possibly nontrivial bundle.

P8-1 must state which hypotheses are proved for which one of these objects.
P8-7 may assemble objects only through an explicit map or direct-sum theorem,
not through reuse of the candidate ID.

**Acceptance test.**  For every P8 target, a reader can identify exactly one
unit space, topology, arrow space, Haar system, completion, and candidate ID;
no statement remains true merely by switching from `G_p` to the global union,
or by replacing the source quotient `Q_p` with the proxy base `B_p`.

### M2 — Major: the primary question is not an exclusive, operational test

**Evidence.**  The primary question asks whether a source-intrinsic
return-sensitive trace exists *or* whether the canonical regular trace keeps
only time zero.  The preregistered hypothesis then predicts both that the
regular trace loses nonzero returns and that the trivial-character trace sees
them.  Both clauses can therefore be true simultaneously.  Moreover, the
typed record is `DEN-EF-GRPD-REG-TRACE-FAM`, explicitly dependent on an
invariant unit measure, while the question calls the regular trace canonical.
No test defines when a trace counts as `source-intrinsic` or `source-selected`.

**Impact.**  The current wording cannot assign an unambiguous confirmation or
refutation outcome.  A measure-dependent singular trace could satisfy the
first clause while every regular trace satisfies the second.  Without an
operational canonicality criterion, P8-7 can be stopped at any convenient
classification depth and the main claim becomes resistant to falsification.

**Required repair.**  Freeze one primary extension/ownership question.  A
methodologically suitable form is:

> Does the frozen trivial-character return functional on an actual Deninger
> orbit extend to a normal, source-selected trace on the corresponding packet
> action groupoid without adding transverse or cross-prime mass choices?

Regular cancellation, trivial-fibre existence, and singularity then become
predeclared subclaims that answer that question.  Define `source-selected`
before Phase 2, for example by a finite conjunction of: determined from the
locked source object, invariant under its relevant automorphisms, requiring no
free transverse or cross-prime weights, and carrying a source-derived
normalization.  State whether uniqueness is literal or only up to a frozen
scalar convention.

**Acceptance test.**  The amended protocol gives disjoint `confirm`, `refute`,
and `not testable` outcomes, and two distinct admissible traces cannot both be
called canonical without satisfying the same frozen uniqueness criterion.

### M3 — Major: the common time-return restriction is not yet a frozen domain

**Evidence.**  `DEN-EF-GRPD-TIME-RETURN-RESTR` is said to contain time-only
kernels `a_f(x,t)=f(t)` for `f in C_c^infinity(R)` *or* a later proved
trace-ideal subspace.  On an infinite packet union, such a kernel has support
over every unit and need not belong to `C_c(G)`; the global weighted expression
`sum_p m_p L_p sum_{r>=1} f(rL_p)` also needs an explicit convergence domain.
P8-7 quantifies over invariant/transverse choices only as far as needed and
does not freeze the admissible class over which the restriction is claimed to
be common.  Within one fixed `p`, normalized transverse probabilities may
have a common time-only value; across different `p`, the clock and masses
change, so that conclusion is not the same statement.

**Impact.**  Algebra membership, trace-ideal membership, independence from
transverse choices, and cross-prime convergence can currently be exchanged
without creating the new candidate/version required by the typed-record rule.
The formal Poisson series could consequently be promoted after the fact to a
functional on a larger algebra.

**Required repair.**  Freeze three levels separately:

- a local orbit/per-prime time-smearing space;
- a finite-packet-support algebra or algebraic direct sum; and
- if attempted, a global weighted domain with an explicit target-free
  summability condition and fixed masses.

Also freeze the admissible class of invariant/transverse measures for the
P8-7 independence statement.  Its natural source-side parameter space, if the
compact free action is proved, is the quotient `Q_p`; a probability on `B_p`
is proxy data until transported by a theorem.  State and prove whether lifting
a probability on `Q_p` with normalized orbit Haar gives all invariant packet
probabilities or only a subclass.  If the common object is only an equality of
values on a small operator system rather than a trace on an algebra, call it
exactly that.

**Acceptance test.**  Every displayed trace or packet sum states its algebra,
positive/linear domain, measure parameters, and convergence mode.  Failure of
global membership forces the finite-support/local stop without changing the
test space after observing the result.

### m1 — Minor: the averaging measure and the factor `1/L` need separate names

The identity

```text
(1/(2 pi L)) integral T_theta(f) dtheta = f(0)
```

is algebraically consistent with the displayed Poisson formula.  It is not,
however, the probability-Haar average `dtheta/(2 pi)`, which gives `L f(0)`.
The additional covolume/Plancherel factor may be exactly right for the regular
trace normalized by the invariant unit probability, but calling the whole
expression merely an `isotropy-Haar average` obscures which normalization owns
`1/L`.  P8-2/P8-4 must freeze the Haar measure on `L Z`, its dual measure, the
orbit probability (for example, the convention induced by `dt/L`), and the
fibre-trace normalization separately.  More importantly, the regular trace
and the trivial-character trace must be evaluated with **one common length and
orbit-probability convention**; neither side may be rescaled independently to
make the comparison look clean.  A source-forced factor different from the
target is a versioned result, not a renormalization chosen to restore `f(0)`.

### m2 — Minor: P8-6 must distinguish point evaluation from its extensions

Pointwise evaluation is not intrinsically well-defined on equivalence classes
in `L-infinity(T, dtheta)`.  The continuous central subalgebra can carry the
character `g -> g(0)`, and positive extensions to a larger algebra may exist,
but no such extension is normal with respect to diffuse Haar measure and it
need not be unique.  P8-6 and the `POINT-EVAL-NONNORMAL` control should test
these three statements separately: representative-independence,
existence/nonuniqueness of singular extensions, and nonexistence of a normal
extension.

### m3 — Minor: add normalization and global-domain controls

The eleven frozen controls cover phase cancellation, regular-versus-trivial
ownership, transverse ambiguity, copied packets, arbitrary/composite clocks,
normality, zero time, and nonredundancy.  Add two target-free controls:

1. rescale the invariant measure or dual Plancherel normalization and verify
   exactly which trace value changes, while confirming that the frozen
   regular/trivial comparison uses the same orbit probability and length
   convention on both sides; and
2. compare one packet, a finite packet set, and the proposed infinite packet
   domain so that compact support and summability failures are visible.

A representative-change test in the `L-infinity` centre should accompany m2.

### m4 — Minor: preregister the Route-A ceiling, not only the forbidden credit

The design correctly forbids A4 and Route B and says that no A3 credit is
available.  It should additionally state that these groupoid/trace records
contain no frozen A2 dynamical Zeta or Fredholm determinant.  Thus exact return
formulas can at most support an A1 analytic ledger result for the correctly
typed restriction; A2 is `A2_FAIL` or `NOT_TESTABLE` as appropriate and A3 is
`A3_FAIL`.  `route_b_invocation_allowed` remains `false`.  This makes the
Route-A output schema executable and prevents the phrase `Route A / A0--A3`
from being read as an A2/A3 target.

## 4. FINER audit

| Criterion | Independent score | Assessment |
|---|---:|---|
| Feasible | 3/5 | The one-orbit P8-2--P8-6 chain is finite and technically plausible.  Packet topology, measure classification, and global assembly make the full nine-target scope less certain; the existing orbit-only stop preserves feasibility. |
| Interesting | 5/5 | It directly tests whether moving from Paper 7's decomposable proxy to the source flow groupoid changes trace ownership. |
| Novel | 4/5 | The question is clearly new within this session.  External novelty cannot be scored 5 before the expressly deferred Phase-2 primary-source search. |
| Ethical / evidence-safe | 5/5 | No human data, target-zero fitting, or outcome-selected parameters are permitted. |
| Relevant | 5/5 | The regular-versus-singular trace boundary is the next source-ownership gate and remains tied to a continuous-time flow. |
| **Mean** | **4.4/5** | The FINER threshold passes; no criterion is below 2. |

**FINER result:** substantively **PASS**, but the research-question wording and
object/domain freeze require M1--M3 before the design itself passes Phase 1.
To keep the project one-paper feasible, designate P8-2--P8-6 on the actual
orbit as the mandatory theorem core and P8-1/P8-7 packet promotion as a
conditional second tier.  The stop rule must permit an orbit-level paper when
the packet tier is `NOT_TESTABLE`.

## 5. Typed-record audit

| Record | Separation status | Required action |
|---|---|---|
| `DEN-WITT-Z-FIN` | PASS | Source-owned packet, clock, and repetition data are not treated as trace data. |
| `DEN-EF-PACKET-ACTION-GRPD` | REVISE | Split per-prime packet family from the global all-prime union and freeze the latter's topology; see M1. |
| `DEN-EF-ORBIT-ACTION-GRPD` | PASS WITH CLARIFICATION | Parameterize by `p,x` or state explicitly that it is a uniform theorem family; orbit selection supplies no packet mass. |
| Source quotient `Q_p` (record to add) | REVISE | Verify the free compact `R/L_p Z` action and quotient properties; do not identify `Q_p` with proxy base `B_p` or assume a trivial principal bundle. |
| `DEN-PACKET-PROD-ISO-GRPD` | PASS | Proxy status and the T0--T7 transport prohibition are explicit. |
| `DEN-EF-GRPD-REG-TRACE-FAM` | PASS WITH CLARIFICATION | Retain measure-indexed family status and attach the normalization in m1 to each member. |
| `DEN-EF-GRPD-TRIVCHAR-TRACE-FAM` | PASS WITH CLARIFICATION | Keep representation image, pullback algebra, positive domain, and singular extension as separate assertions. |
| `DEN-EF-GRPD-TIME-RETURN-RESTR` | REVISE | Split local, finite-packet, and possible global weighted domains; see M3. |

The four principal owners relevant to any eventual result remain distinct:
source groupoid, regular trace family, trivial-character trace family, and the
small time-return restriction.  No owner may inherit Paper-7 proxy credit or a
Route coordinate from another owner.

## 6. P8-1--P8-9 audit

| Target | Design verdict | Falsifiable outcome / needed repair |
|---|---|---|
| P8-1 | REVISE | Separately gate `G_p`, its source quotient `Q_p`, and the global union.  Verify the compact free action without assuming `Q_p=B_p` or a product trivialization.  Failure yields the already specified orbit-only/`NOT_TESTABLE` result. |
| P8-2 | PASS | The result type is explicitly required to be isomorphism, stable isomorphism, Morita equivalence, or measurable decomposition; no silent strengthening is allowed. |
| P8-3 | PASS | Trace-class membership and the signed Floquet/Poisson formula can both fail independently and are testable under the frozen Fourier convention. |
| P8-4 | PASS WITH m1 | Domain, tracial-versus-weight status, and normalization precede the cancellation claim.  A nonzero-return counterformula is an accepted falsification. |
| P8-5 | PASS | Lower semicontinuity, semifiniteness, traciality, and the actual positive domain are explicit obligations; formal Poisson values alone cannot pass. |
| P8-6 | PASS WITH m2 | The no-normal-extension claim is falsifiable, but `L-infinity` representative and singular-extension statements must not be conflated. |
| P8-7 | REVISE | Replace `classify ... far enough` with a frozen admissible measure class on the verified source quotient `Q_p`, an explicit lift/disintegration theorem, explicit uniqueness equivalence, local/global domains, and finite stopping criteria. |
| P8-8 | PASS WITH m3 | The current controls are target-free and mechanism-specific; add normalization and infinite-domain controls. |
| P8-9 | PASS WITH m4 | T0--T7 are disjoint from P8 theorem labels.  Route records remain owner-specific, with A2/A3 failures and Route-B closure explicit. |

## 7. Falsifiability, controls, and stop-rule audit

### What is already strong

- The sign of the character phase and every normalization are theorem
  obligations, not evidence.
- Regular cancellation may be refuted by an exact counterformula.
- A failed or nontracial trivial-character weight is abandoned rather than
  rescued by a formal series.
- Packet-topology failure cannot be repaired by silently substituting the
  product proxy.
- Arbitrary and composite clocks deliberately test that the isotropy
  mechanism is generic rather than arithmetic by itself.
- Zero-time support prevents the regular contribution from being hidden.
- The nonredundancy control prevents Paper 7's mass ambiguity from being
  republished as the only result.
- No control uses target zeros, a desired Euler product, fitted phases, fitted
  clocks, or fitted masses.

### Stop rules to add in the amendment

1. If per-prime and global topologies cannot be separated under distinct
   candidate IDs, stop all packet-level claims before P8-1 credit.
2. If a global time-only kernel is outside the groupoid algebra or trace ideal,
   stop at the local/finite-support theorem; do not move it silently to a
   multiplier or distribution space.
3. If the admissible measure class or source-selected criterion cannot be
   frozen independently of the result, mark packet canonicality
   `NOT_TESTABLE`.
4. If regular cancellation and existence of a return-sensitive singular trace
   are both proved, report both; do not present them as exclusive outcomes.

With these additions, the hypothesis chain is capable of producing positive,
negative, counterformula, limited-domain, and `NOT_TESTABLE` outcomes without
tuning.

## 8. Same-object and Route boundary

The T0--T7 certificate is well designed.  In particular, it prevents a set
bijection or Morita equivalence from transporting topology, measure,
representation, trace, or arithmetic mass automatically.  M1 and M3 are
required precisely so that T0, T1, T4, T5, and T6 have a single owner before
that certificate is applied.

The permissible Route interpretation is:

- A0 belongs only to the verified arithmetic source record and cannot be
  inferred from isotropy analysis;
- an exact source-orbit repetition functional may support A1 for that exact
  typed restriction;
- the generic arbitrary-clock and composite-clock controls prevent the local
  analytic mechanism from being promoted as arithmetic evidence;
- no dynamical Zeta/determinant record is frozen, so A2 cannot pass;
- no continuation, functional equation, Gamma factor, counting law, or Weil
  compression is attempted, so A3 cannot pass;
- A4 is closed and Route-B invocation is false.

No coordinatewise maxima across the source, regular family, singular family,
and common restriction form a valid Route certificate.

## 9. One-paper nonredundancy and scope decision

**Within-session nonredundancy: PASS, conditionally.**  Paper 7 studied a
selected decomposable proxy and separated its trace, return ledger, and
zero-mode determinant owners.  Paper 8 asks a genuinely different question:
what the actual source transformation groupoid's regular and
isotropy-character representations do, and whether the return-sensitive fibre
has a normal source-owned extension.  A proof or refutation of P8-4 together
with P8-6 on an actual source orbit is a new result.  A rigorous packet-level
extension/obstruction would strengthen it further.

The project becomes redundant if it proves only that packet masses are
noncanonical, or if all calculations remain on
`DEN-PACKET-PROD-ISO-GRPD`.  The existing nonredundancy control correctly
forbids that outcome.  External-literature novelty remains unassessed by this
Phase-1 review.

The project also remains within the Flow Systems session only while the trace
classification is the minimum needed to answer the source-flow extension
question.  A general von Neumann/groupoid trace-classification program beyond
P8-4--P8-7 should be recorded as a later clue rather than expanded here.

## 10. Phase-1 decision and re-review gate

**Decision: REVISE.  Phase 2 is not authorized on the current byte locks.**

The design can pass a short exact-byte re-review after a versioned amendment
does all of the following:

1. splits the per-prime packet, orbit, and global packet-union groupoids and
   freezes each topology, while separately verifying the source quotient
   `Q_p` and forbidding an unproved identification with `B_p`;
2. replaces the nonexclusive primary question and defines
   `source-selected`/`canonical` operationally;
3. freezes local, finite-packet, and any global time-return domains together
   with the admissible measure class and convergence conditions;
4. names the Haar, quotient, Plancherel, and trace normalizations separately
   and uses one common length/orbit-probability convention for the regular and
   trivial-character traces;
5. refines P8-6's `L-infinity` statement and adds the normalization/domain
   controls; and
6. preregisters the owner-specific Route ceiling with A2/A3 unable to pass and
   Route-B invocation false.

No source conclusion, Phase-2 theorem, Route promotion, or manuscript claim is
made by this review.
