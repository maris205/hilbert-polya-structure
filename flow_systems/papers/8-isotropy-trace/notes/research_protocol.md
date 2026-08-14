# Paper 8 research protocol — isotropy-character trace gate

Protocol status: **PHASE 2 TYPED AMENDED v2 — INDEPENDENT RE-LOCK PASS**  
Date: 2026-08-14  
Primary source candidate: `DEN-EF-PACKET-ACTION-GRPD-P`  
Parent source object: `DEN-WITT-Z-FIN`  
Route scope: Route A audits A0--A3, with at most A1 credit in this paper;
A4 and Route B are not invocable

Amendment ID: `P8-PH1-AMEND-2026-08-14-v1`.  The original protocol bytes
(`51c85aae8262d6fb8597d49e6c23a1926ebb24ee3c3429d996228565b4d7a547`)
retain only the historical independent `REVISE` verdicts recorded in
`phase1_methodology_review.md`, `phase1_devils_advocate.md`, and
`phase1_source_feasibility.md`.  The amendment crosswalk is
`phase1_amendment.md`; no old verdict is inherited by these bytes.

Phase-2 amendment ID: `P8-PH2-TYPED-AMEND-2026-08-14-v1`.  The source audit
proved that the one-orbit algebra is `C(T) tensor K`, whose algebraic centre is
zero.  The amendment in `phase2_domain_amendment.md` replaces every proposed
"continuous-centre point evaluation" argument by a trace-finite full
rank-one-corner argument.  It also applies the preregistered simultaneous sign
correction forced by the sourced induction convention.  It grants no theorem
credit until independently re-locked.

This protocol follows Paper 7 but does not inherit its proxy algebra or its
Route credits.  Paper 7 proved that a selected decomposable type-I proxy has a
locally finite positive-time return record, while its normal trace and
zero-mode determinant have different domains and owners.  The present paper
asks whether the transformation groupoid **canonically newly constructed from
the source-defined flow** owns that return record.  The groupoid is classified
as `DERIVABLE_NEW_DEFINITION`, not as an object defined in Deninger's source.
The protocol preregisters a possible negative mechanism:
normal Plancherel averaging over isotropy characters may erase every nonzero
return, whereas the desired orbit sum may live only in the trivial-character
fibre, which is singular in the regular von Neumann completion.

## 1. Research Question Brief

### Topic area

Transformation groupoids of periodic flows, isotropy representations,
Plancherel and Floquet decomposition, normal semifinite traces, singular
lower-semicontinuous `C*`-traces, and Deninger's finite-kernel prime packets.

### Candidate questions considered

| ID | Candidate question | F | I | N | E | R | Mean | Decision |
|---|---|---:|---:|---:|---:|---:|---:|---|
| A | Does the natural action groupoid of the finite-kernel prime packets own the positive-time return ledger, or does isotropy averaging erase it? | 4 | 5 | 5 | 5 | 5 | **4.8** | Selected |
| B | Can Paper 7's zero-mode determinant be analytically continued? | 2 | 4 | 2 | 4 | 3 | 3.0 | Rejected: wrong owner and premature A3 question |
| C | Can one choose a groupoid trace that reproduces the Euler product? | 5 | 3 | 1 | 3 | 3 | 3.0 | Circular unless the trace is frozen before any target comparison |
| D | Is every measured/groupoid repair of Deninger's packets impossible? | 1 | 4 | 2 | 5 | 3 | 3.0 | Rejected as an unanswerably universal claim |
| E | Can Morishita's adelic map transport a crossed-product trace? | 3 | 4 | 4 | 5 | 4 | 4.0 | Secondary same-object exclusion test |

The novelty score is within-session novelty.  External novelty is provisional
until the Phase-2 primary-source search is complete.

### Primary research question

> Does the trivial-isotropy-character return functional on an actual
> Deninger `E_f` orbit extend to a **normal, source-selected** trace on the
> corresponding packet action groupoid without adding a free transverse
> probability or a free cross-prime mass sequence?

Here **source-selected** means all of the following: the object and
normalization are derived from the frozen `E_f` flow and standard Lebesgue
time, the construction is invariant under source flow-equivariant
automorphisms, no transverse probability or cross-prime weight remains free,
and uniqueness holds literally under the frozen scale (not merely after a
target-motivated rescaling).  If any clause is absent, the trace is a family or
modeling choice rather than source-selected.

The mutually exclusive primary outcomes are:

- **CONFIRM:** such a normal source-selected extension is constructed on one
  fixed packet completion and owns the stated domain;
- **REFUTE:** the frozen return functional has no normal extension along the
  fixed comparison map, or every extension necessarily retains a free source
  choice prohibited above; or
- **NOT_TESTABLE:** the source topology/completion map required to formulate
  the extension does not close.

### Primary hypothesis and competing outcome

For one periodic orbit of least period `L`, the isotropy group is `L Z` and
its unitary dual is a circle.  The preregistered mechanism is:

```text
character fibre theta:
    Tr_theta(C_f) = sum_n fhat((2 pi n - theta)/L)
                  = L sum_r f(rL) exp(+i r theta),

dual-Haar average at the length-Haar scale:
    (1/(2 pi)) integral_0^(2pi) Tr_theta(C_f) dtheta = L f(0),

trivial character theta=0:
    Tr_0(C_f) = L sum_r f(rL).
```

The exact normalization and sign must be derived from the frozen groupoid,
Haar, Fourier, representation, and Weil conventions; the display is a theorem
target, not evidence.  Dividing both displayed traces by `L` produces the
orbit-probability scale; rescaling only one side is forbidden.  If proved, the
two following subclaims may hold simultaneously:

- the regular normal trace is source-related but erases all nonzero returns;
- the trivial-character fibre sees the returns but is non-normal in the
  regular von Neumann completion.

The trivial isotropy character is algebraically distinguished.  That fact
does **not** by itself select a transverse measure, a packet trace, a
cross-prime mass, or a determinant.

### FINER assessment

| Criterion | Score | Justification |
|---|---:|---|
| Feasible | 4/5 | The local orbit groupoid and Floquet calculation are explicit; the source packet bridge has a finite typed gate. |
| Interesting | 5/5 | It decides whether the first genuine source groupoid repairs or sharpens Paper 7's trace-ownership obstruction. |
| Novel | 5/5 | No prior session paper separated the regular isotropy average from the trivial-character return fibre. |
| Ethical / evidence-safe | 5/5 | No human subjects or target-zero data; phases, masses, and clocks cannot be fitted. |
| Relevant | 5/5 | It directly addresses the next gate recorded after Paper 7: a geometry-sensitive groupoid newly derived from the source-defined flow. |
| **Average** | **4.8/5** | No criterion below 2. |

## 2. Scope and typed candidate freeze

### In scope

- the finite-kernel admissible subsystem `E_f` of Deninger's `Spec Z` flow;
- each compact prime packet `Gamma_p`, its restricted continuous `R`-flow,
  its periodic orbits, and isotropy `(log p) Z`;
- the transformation groupoid of one actual source packet, subject to the
  topology/Haar hypotheses being source-verified;
- the intrinsic compact-circle quotient
  `Q_p=Gamma_p/(R/(log p)Z)`, without identifying it with `B_p`;
- the restriction of that groupoid to one actual periodic orbit;
- a separate explicit product-coordinate groupoid used only for calculation;
- full versus reduced groupoid `C*`-algebras, their equality only if
  amenability is proved, and the regular von Neumann representation;
- invariant unit measures, Haar systems, normal semifinite trace/weight
  domains, isotropy characters, induced representations, and singular
  lower-semicontinuous traces;
- exact Poisson/Floquet formulas and target-free finite controls;
- trace classification only as far as proved for the frozen object;
- the T0--T7 same-object certificate and separate Route-A records.

### Out of scope

- Riemann zeros, ordinates, unfolding, scale fitting, or spectral matching;
- choosing `theta=0`, packet masses, or cross-prime weights because an Euler
  product is desired;
- calling a Haar system a transverse measure or a transverse measure a trace;
- assuming `Gamma_p` is homeomorphic or Borel-isomorphic to
  `B_p x R/(log p)Z` from a set-level parametrization;
- calling a Morita equivalence an algebra isomorphism or a trace-preserving
  same-object identification;
- identifying a `C*`-trace with a normal trace on a particular von Neumann
  completion;
- using point evaluation on `L-infinity(T)` as though it were normal;
- importing Paper 7's decomposable algebra, trace, masses, or determinant;
- meromorphic continuation, a functional equation, completed `xi`, a
  self-adjoint Hilbert--Polya operator, or any Route-B promotion;
- a universal claim excluding every future groupoid or cohomological repair.
- treating the inherited subspace topology on the all-prime periodic set as
  the topological coproduct of the individual packets;
- calling the positive-time restriction a `C*`-trace: its test class is not a
  star-subalgebra and its output is a distributional ledger.

### Typed records

The following records remain separate throughout:

| Candidate ID | Frozen role |
|---|---|
| `DEN-WITT-Z-FIN` | Published finite-kernel rational-Witt flow; source owner of prime packets, periods, and repetitions. |
| `DEN-EF-PACKET-ACTION-GRPD-P` | The per-prime family `G_p=Gamma_p rtimes R`, with the inherited topology on each actual source packet. |
| `DEN-EF-ORBIT-ACTION-GRPD` | Restriction to one actual periodic source orbit; local source control independent of a packet product chart. |
| `DEN-EF-PACKET-ORBIT-QUOTIENT-Q` | Intrinsic quotient family `Q_p=Gamma_p/K_p`, `K_p=R/L_pZ`; not identified with proxy `B_p`. |
| `DEN-EF-PACKET-COPROD-GRPD` | Optional topological coproduct `coprod_p G_p`; a new assembly object, not the inherited all-prime source subspace. |
| `DEN-PACKET-PROD-ISO-GRPD` | Explicit calculational proxy `B_p x (R/L_p Z)` with the translation action; no source credit without transport. |
| `DEN-EF-GRPD-REG-TRACE-FAM` | Regular/Plancherel trace family associated with verified invariant unit measures; normality and domain must be proved. |
| `DEN-EF-GRPD-TRIVCHAR-TRACE-FAM` | Trivial-isotropy-character induced `C*`-trace family; potentially return-sensitive but not presumed normal or uniquely assembled. |
| `DEN-EF-GRPD-TIME-RETURN-LOCAL` | Common per-prime restriction, if proved choice-independent, of trivial-character traces to the frozen time-smearing test space. |
| `DEN-EF-GRPD-TIME-RETURN-FIN` | Algebraic finite-prime-support assembly of the local restrictions. |
| `DEN-EF-GRPD-TIME-RETURN-POS` | Positive-time locally finite distribution obtained by restricting `f` to `C_c^infinity((0,infinity))`; not a full trace. |

Changing the unit space, topology, arrow convention, Haar system, invariant
measure, isotropy character, representation, completion, test algebra, trace
domain, or cross-prime mass creates a new candidate or version.

## 3. Frozen mathematical conventions

### Per-prime source action groupoid and intrinsic quotient

Let `X_p=Gamma_p` with source flow `phi_p^t`.  Conditional on the verified
topological hypotheses, define

```text
G_p = X_p rtimes R
```

with arrow `(x,t)` from `x` to `phi_p^t(x)`:

```text
s(x,t)=x,
r(x,t)=phi_p^t(x),
(phi_p^t(x),u) o (x,t)=(x,t+u),
(x,t)^(-1)=(phi_p^t(x),-t).
```

Lebesgue measure in the time coordinate is the proposed Haar system.  Phase 2
must verify whether the source packet is locally compact Hausdorff and whether
the resulting groupoid has the countability/regularity hypotheses required by
each cited theorem.  Failure of a packet-level hypothesis does not invalidate
the single-orbit restriction; the records must then remain separate.

The exact common stabilizer `L_p Z` implies that the action factors through

```text
K_p = R/(L_p Z).
```

Conditional on the verified Hausdorff/continuity hypotheses, the `K_p` action
is free and compact and the source-intrinsic orbit quotient is

```text
q_p: Gamma_p -> Q_p=Gamma_p/K_p.
```

Compact Hausdorffness, second countability, local triviality, and every measure
lifting statement are separate proof/source gates.  Even if `Q_p` is compact
Hausdorff, it is not called `B_p`, and `q_p` is not called a trivial principal
bundle, without a theorem.

For compactly supported **per-prime** kernels the frozen convolution convention is

```text
(a*b)(x,t) = integral_R a(phi_p^u(x),t-u)b(x,u) du,
a*(x,t)    = conjugate(a(phi_p^t(x),-t)).
```

Any change forced by an authoritative source must be recorded as a versioned
protocol amendment before proofs are credited.

No global inherited packet-union groupoid is frozen.  If needed, the
topological coproduct `coprod_p G_p` is the distinct candidate
`DEN-EF-PACKET-COPROD-GRPD`.  A time-only function constant on every component
is not in `C_c(coprod_p G_p)`; the global return record is therefore assembled
first on finite prime support and then, on positive-time test functions only,
as a locally finite distribution.

### Orbit and isotropy conventions

For `x in Gamma_p`, let `O_x` be its source orbit and put

```text
L_p = log p,
H_x = G_x^x = {(x,rL_p): r in Z} isomorphic to L_p Z,
chi_theta(rL_p)=exp(i r theta),  theta in [0,2pi).
```

The trivial character is `chi_0`.  It is group-theoretically distinguished;
no target formula is used to select it.

Standard Lebesgue time induces the **length Haar measure** `du` on
`R/(L_pZ)`, of total mass `L_p`.  The probability Haar measure is separately
named `dubar=du/L_p`.  The primary comparison uses the length scale on both
the regular and character-fibre sides.  A probability-scale control divides
both sides by `L_p`; independent rescaling is prohibited.

For any Borel probability `nu_p` on a proved compact Hausdorff `Q_p`, the
candidate length-scale invariant unit measure is defined without a section by

```text
mu_(p,nu)(h)
  = integral_Qp [ integral_0^Lp h(phi_p^t(x_q)) dt ] dnu_p(q),
```

because the bracket is independent of the representative `x_q` on the orbit.
This construction, its regularity, and whether all invariant measures arise
this way are theorem obligations.  The family over `nu_p` is not a canonical
measure merely because every member has the same time-only value.

The explicit product proxy is

```text
Y_p = B_p x (R/L_p Z),
G_p^prod = Y_p rtimes R,
B_p = Zhat_(p)^x / p^Zhat.
```

`G_p^prod` is a calculational object.  A set bijection between `Gamma_p` and
`Y_p` does not transport topology, Borel structure, Haar systems, invariant
measures, representations, or traces.

### Fourier and time-smearing convention

Freeze

```text
fhat(xi) = integral_R f(t) exp(-i t xi) dt,
f(t)     = (1/(2pi)) integral_R fhat(xi) exp(i t xi) dxi.
```

For `f in C_c^infinity(R)`, define the time-only groupoid kernel

```text
a_f(x,t)=f(t).
```

The induced representation associated with `chi_theta` uses the sourced
Green/Williams convention

```text
xi(u+rL_p)=chi_theta(rL_p)^(-1)xi(u)=exp(-ir theta)xi(u),
(U_t xi)(u)=xi(u-t).
```

Thus its Floquet eigenfrequencies are `(2pi n-theta)/L_p` and its trace target
is

```text
T_(p,theta)(f)
  = sum_(n in Z) fhat((2pi n-theta)/L_p)
  = L_p sum_(r in Z) f(rL_p) exp(+i r theta).
```

This is the preregistered `theta -> -theta` correction applied simultaneously
to the spectral shift and return phase.  It follows from Williams's induced
function convention, not from a target comparison.  Dual-Haar averaging and
the `theta=0` result are unchanged.

### Three distinct trace notions

1. **Regular groupoid trace/weight.**  From a verified invariant unit measure
   and the time Haar system, construct the regular representation and its FNS
   trace or Plancherel weight.  Whether it is a trace, its normalization, and
   the domain containing `a_f` must be proved, not inferred from notation.
2. **Character-fibre `C*`-trace.**  Induce from `chi_theta`, then compose with
   the ordinary trace on the compact-operator image only on its natural
   positive domain.  Lower semicontinuity, semifiniteness, and the tracial
   identity are theorem obligations.
3. **Common time-return restriction.**  If different orbit/transverse choices
   yield the same value on all `a_f`, record only that restricted functional.
   Agreement on this small test algebra does not make the full traces equal or
   canonical.

No object is called a normal trace until its von Neumann algebra, positive
cone, faithfulness/normality/semifiniteness, and `L1` domain are fixed.

### Completion and comparison diagram

Two completion maps are frozen and may not be spliced.  For an actual source
orbit `O ~= R/(LZ)`, the local map is

```text
A_L=C*(O rtimes R)  --lambda_L-->  A_(L,r)=C*_r(O rtimes R)
                                      --pi_(L,reg)--> M_L^reg.
```

The character representations `pi_(L,theta)` start on `A_L`.  P8-2--P8-6 are
proved first on this exact local map.  The finite projection
`p=1 tensor e` and its corner belong to `A_L`, not to a packet algebra.

Separately, **conditional on the packet LCH gate**, the packet map is

```text
C*(G_p)  --lambda-->  C*_r(G_p)  --pi_reg-->  M_(p,nu)^reg
   |
   +--pi_(q,theta)--> K(H_(q,theta)) subset B(H_(q,theta)).
```

`lambda` is an isomorphism only after amenability proves full/reduced equality.
The fibre representation may factor through the reduced algebra only after
that fact is proved.  Morita equivalence alone is insufficient.  The
local trivial-character weight is first

```text
Tr o pi_(L,0)
```

on its positive pullback domain in `A_L`.  P8-6 first asks whether this exact
functional extends normally **along the fixed local map** to `M_L^reg`.  On
the one-orbit completion
`A_L ~= C(T) tensor K(H)`, one must first prove and fix a trace-finite full
projection `p=1 tensor e`, with `e` rank one, so that
`p A_L p ~= C(T)` and the character weight is finite on `p`.  Point evaluation
is then tested in this finite corner, followed separately by singular-state
extension/nonuniqueness and by nonexistence of a normal extension.  The corner
is not central and its chosen rank-one projection is not source data.

The algebraic centre of `A_L` is zero.  Its multiplier centre is
`C(T) tensor 1`, but `delta_theta tensor Tr` takes value `+infinity` on a
positive multiplier `f tensor 1` whenever `f(theta)>0`.  Therefore neither the
multiplier centre nor an untyped `L-infinity` representative can serve as the
bounded point-evaluation witness.

A local no-normal-extension theorem does not by itself answer the packet-level
primary question.  Transporting that obstruction to `M_(p,nu)^reg` requires a
separate restriction/disintegration/compression theorem through the packet
map.  If packet Hausdorff/LCH or that same-map bridge remains open, the primary
packet extension outcome is `NOT_TESTABLE`, even when the local orbit analogue
is refuted.

### Local, finite, and positive-time domains

For one `p`, `a_(p,f)(x,t)=f(t)` lies in the per-prime compact-support test
space when `f in C_c^infinity(R)` and `Gamma_p` is compact.  Define the
algebraic finite-prime-support space

```text
A_time^fin = direct_sum_p {a_(p,f_p): f_p in C_c^infinity(R)}.
```

No all-prime time-only operator is asserted in a groupoid `C*`-algebra or an
`L1` trace ideal.  After the two-sided trace is proved, restrict the **test
function**, not the algebra, to

```text
f in C_c^infinity((0,infinity)).
```

Then zero and negative repetitions vanish and the proposed scalar assembly is

```text
Theta_+(f)=sum_p L_p sum_(r>=1) f(rL_p).
```

This is locally finite because compact positive-time support bounds `p` and
`r`.  `Theta_+` is a positive-time Radon distribution/measure, not a
`C*`-trace, and unit cross-prime coefficients come from counting the source
closed points.  A weighted variant creates a distinct mass-family candidate;
it is not part of the primary record.

### Weil and Plancherel normalization gate

Phase 2 must obtain and Phase 3 must prove the exact normalization chain.  The
frozen desired convention is the Weil identity

```text
integral_R g(t) dt
  = integral_[0,L) sum_(r in Z) g(u+rL) du
  = L integral_(R/LZ,dubar) sum_r g(u+rL),
```

with counting Haar on `LZ`, length Haar `du`, probability Haar `dubar=du/L`,
and dual probability Haar `dtheta/(2pi)`.  At the common length scale,

```text
(1/(2pi)) integral_0^(2pi) T_theta(f)dtheta=L f(0),
T_0(f)=L sum_r f(rL).
```

At the probability scale both are divided by `L`.  The source theorem may
force a different but internally consistent convention; if so it is reported
as a versioned result and never repaired after comparison.

## 4. Pre-registered theorem targets

1. **P8-1 — source groupoid and quotient gate.**  Verify the exact topology
   and continuity of each `Gamma_p`, construct per-prime `G_p`, prove or fail
   its Haar/amenability/countability hypotheses, and derive the free compact
   action and quotient `Q_p`; do not identify `Q_p` with `B_p`.  The optional
   coproduct is a separate object and is not needed for the local theorem.
2. **P8-2 — orbit imprimitivity/Floquet decomposition.**  For one source orbit
   of period `L`, identify the isotropy-dual field of induced
   representations.  State precisely whether the result is an isomorphism,
   stable isomorphism, Morita equivalence, or measurable decomposition.
3. **P8-3 — character-fibre Poisson trace.**  Prove trace-class membership for
   `a_f` in every Floquet fibre and the exact phase-weighted return formula.
4. **P8-4 — regular isotropy cancellation.**  Prove the FNS/Plancherel trace
   domain and the full Weil normalization chain, then show that dual-Haar
   averaging over `theta` kills every `r != 0` term and retains only the
   identity-time coefficient at the same scale as P8-5.
5. **P8-5 — trivial-character return trace.**  Prove that `theta=0` yields the
   full repetition ledger and defines a lower-semicontinuous semifinite
   `C*`-trace/weight on its actual domain.
6. **P8-6 — fixed-map singularity/no-normal-extension theorem.**  On the
   fixed **one-orbit** completion map `A_L -> A_(L,r) -> M_L^reg`, first prove
   the regular image of a trace-finite full rank-one corner
   `p A_L p ~= C(T)`.  Separately prove point-evaluation
   independence inside that continuous corner, existence or nonuniqueness of
   singular state extensions from the corner, and absence (or existence) of
   a normal extension of the same extended-positive trace to `M_L^reg`.  Do
   not call the corner central and do not use the
   multiplier centre, where the character weight is generally infinite.
   Any promotion to `M_(p,nu)^reg` is a separate packet same-map theorem; if
   the packet LCH/completion gate remains open, record it `NOT_TESTABLE`.
7. **P8-7 — quotient-measure and domain boundary.**  For
   `nu_p in Prob(Q_p)`, prove the section-free lift, state whether it exhausts
   invariant packet measures, decide whether full traces vary with `nu_p`
   while their local time-only restrictions agree, and keep local,
   finite-prime, positive-time, and any weighted global domains separate.
8. **P8-8 — blindness and falsification controls.**  Prove which conclusions
   survive singleton bases, arbitrary transverse probabilities, copied
   packets, arbitrary clocks, composite clocks, and nontrivial isotropy
   characters.
9. **P8-9 — ownership and Route evaluation.**  Complete the T0--T7 transport
   certificate separately for the per-prime action groupoid, quotient,
   regular trace family, trivial-character family, and three time-return
   domains.  A1 is the maximum possible positive analytic credit; no A2
   determinant, A3 structure, or Route-B credit is inherited.

## 5. Source and analysis order

1. Reverify Deninger's finite-kernel packet topology, compactness,
   Hausdorffness, source flow, and isotropy statements from retained primary
   manifestations.
2. Search primary sources for transformation-groupoid Haar systems,
   transitive-groupoid imprimitivity, induced isotropy representations,
   crossed-product FNS traces/weights, and trace disintegration.
3. Freeze full/reduced and representation conventions before using a Morita
   or Floquet theorem.
4. Prove P8-2--P8-6 first on one actual source orbit.  Re-prove and lock the
   limited `E_f` orbit homeomorphism suggested by Deninger plus Morishita only
   if its hypotheses close; it may supply T1/T2 on one orbit, never a packet
   measure or analytic bridge.  The product proxy is a
   calculation check, not a substitute.
5. Address packet assembly and source ownership only after the local theorem
   is stable.
6. Run deterministic controls after all signs and normalizations are frozen.
7. Evaluate every typed record separately under Route A.

**Forbidden evidence:** Riemann zero data; a target Euler product; fitted
phases, masses, clocks, cutoffs, or branches; an unverified secondary summary
for a load-bearing operator theorem; and any result imported from Paper 7
without a new same-object certificate.

## 6. Falsification controls

1. **Finite character grid.**  Average `theta_j=2pi j/N`; verify exact
   cancellation of repetitions not divisible by `N`, and take `N` beyond the
   finite repetition window without claiming a proof of Haar integration.
2. **Nontrivial character.**  Verify the exact phase `exp(+ir theta)` and show
   that return coefficients are not positive multiplicities in general.
3. **Trivial versus regular.**  Compute both records from the same finite
   kernel and verify that only the former retains nonzero returns.
4. **Singleton transverse base.**  The local isotropy result must survive.
5. **Arbitrary transverse probability.**  Time-only values may remain common,
   while at least one transverse observable must distinguish the full traces.
6. **Copied packet.**  Full traces and unrestricted ledger masses must respond
   additively; any normalized time-only equality must disclose the
   normalization.
7. **Arbitrary clock.**  Replace `log p` by a target-free locally finite list;
   the isotropy mechanism should persist, proving it is not arithmetic by
   itself.
8. **Composite clock.**  Insert `log n` for composite `n`; the analytic
   mechanism may persist while prime provenance must fail.
9. **Ordinary/normal trace boundary.**  In a proved trace-finite rank-one
   corner, demonstrate that point evaluation on `C(T)` has no normal extension
   to the corresponding regular `L-infinity(T)` corner; do not hide it behind
   a finite discretization or call the corner central.
10. **Zero-time support.**  Test functions meeting zero must expose the
    regular trace contribution rather than being silently removed.
11. **Non-redundancy.**  The final result must establish a new
    isotropy-average/singular-fibre theorem or a rigorous obstruction to it;
    merely repeating Paper 7's mass ambiguity is insufficient.
12. **Common-scale normalization.**  Compare length and probability scales,
    rescaling regular and character traces together; reject independent
    post-result renormalization.
13. **Local/finite/global domain.**  Compare one packet, finite prime support,
    and the positive-time locally finite sum, verifying that no global
    `C*`/`L1` operator is inferred from scalar convergence.
14. **Finite-corner representative.**  Distinguish a continuous function in
    `p A_L p ~= C(T)` evaluated at `theta=0` from an `L-infinity` equivalence
    class, from a singular positive extension, and from a multiplier-centre
    element on which the uncompressed character weight may be infinite.

No control may use target zeros or compare fitted residuals to a zeta target.

## 7. Same-object certificate

Every proposed transport is audited field by field:

| Field | Required evidence |
|---|---|
| T0 — object identity | Actual `E_f` packet/orbit, not Morishita's enlarged full-character object or Paper 7's proxy |
| T1 — topology/Borel | Source topology and Borel structure, including any orbit restriction or product chart |
| T2 — flow/clock | Intertwining of `phi^t` and preservation of `L_p=log p` |
| T3 — groupoid/Haar | Unit/arrow maps, Haar system, amenability, and completion |
| T4 — measure | Invariant unit or transverse measure and normalization |
| T5 — representation/trace | Exact representation, positive domain, and normal or `C*` trace type |
| T6 — test algebra/formula | The same `a_f`, Fourier convention, and return distribution |
| T7 — arithmetic promotion | Closed-point/component mass transport independent of target equality |

Coordinate splicing fails if any required field is absent.  A Morita
equivalence does not automatically close T0, T4, T5, or T7.

## 8. Validity, Route, and stop rules

| Criterion | Required safeguard |
|---|---|
| Construct validity | “Haar,” “Plancherel,” “normal,” “singular,” and “trace” always name an owner and domain. |
| Internal validity | The same completion and representation own the trace and time-smearing. |
| Source validity | Primary manifestations, page/theorem locators, hashes, and limitations are recorded. |
| Same-object validity | Product-model calculations do not transfer without T0--T7. |
| Falsification | Character, base, copy, clock, composite, and zero-time controls are mandatory. |
| Reproducibility | Deterministic standard-library code and hash-locked target-free outputs only. |

Permissible maximum claims before proof:

- `DEN-WITT-Z-FIN` retains its existing source packet/clock verdict only;
- `DEN-EF-PACKET-ACTION-GRPD-P` may receive
  `DERIVABLE_NEW_DEFINITION` credit only after P8-1; source origin belongs to
  its underlying packet/flow fields, not to the groupoid or trace.  Merely
  writing `Gamma_p rtimes R` is not a trace theorem;
- `DEN-EF-GRPD-REG-TRACE-FAM` may receive analytic credit only for a proved
  normal/FNS domain and must disclose zero-time-only cancellation;
- `DEN-EF-GRPD-TRIVCHAR-TRACE-FAM` may receive analytic trace credit only as a
  `C*`-level singular family unless a normality theorem says otherwise;
- a common time-return restriction may receive A1 ledger credit, but not A2
  determinant credit;
- every typed record has `A2_FAIL` or `A2 NOT_TESTABLE`; no dynamical
  determinant is frozen.  Every record has `A3_FAIL`: no record receives
  continuation, functional equation, Gamma factor,
  completed divisor, or counting credit;
- A4 and Route B remain forbidden, and `route_b_invocation_allowed=false`.

**Scoped stop conditions**

- If the actual packet groupoid fails the necessary local compactness,
  Hausdorffness, or countability hypotheses, finish the source-orbit theorem
  and mark the packet
  transport `NOT_TESTABLE`; do not replace the source silently by the proxy.
- If regular cancellation is false, report the exact counterformula and its
  owner; do not tune normalization to recover it.
- If the trivial-character trace is not densely defined or tracial, abandon
  that candidate rather than using its formal Poisson series.
- If full trace selection remains noncanonical but the time-only restriction
  is common, state precisely that limited positive result.
- If the mechanism compiles arbitrary clocks, classify arithmetic promotion
  as failed or exploratory even when the local theorem is exact.
- If the all-prime kernel is absent from `C_c`, the groupoid `C*`-algebra, or
  the relevant `L1` domain, stop at the local/finite trace and positive-time
  distribution; scalar convergence cannot promote it to a global trace.

## 9. Ethics, reporting, and AI boundary

- Human subjects / IRB: not applicable.
- Reporting standard: theorem/proof/source/reproducibility and mathematical
  integrity; no EQUATOR checklist applies.
- Preregistration: this file and `candidate_lock.md` are the Phase-1 design
  freeze.  Later corrections require a dated amendment and independent
  exact-byte re-lock.
- AI disclosure: AI assists source triage, formal checking, code, writing, and
  adversarial review; the named author retains mathematical responsibility.
- Cross-model upload: disabled; no unpublished manuscript is sent to an
  external review service.

## 10. Phase-1 closure gate

Phase 1 passes only after independent reviews confirm:

1. actual source groupoid, one-orbit restriction, and product proxy are not
   conflated;
2. Haar system, invariant measure, normal trace, and singular fibre trace are
   separately typed;
3. the proposed Floquet/Poisson signs and normalizations are testable and not
   assumed;
4. the regular and trivial-character records cannot borrow each other's
   domains or Route credits;
5. transverse probabilities, packet masses, and cross-prime counting remain
   separate provenance gates;
6. P8-1--P8-9 and T0--T7 use disjoint namespaces;
7. no target zero, Euler equality, fitted phase/mass, or fitted normalization
   is admitted as evidence after the freeze; and
8. A4 and Route B remain closed.

## 11. Amendment ledger

`P8-PH1-AMEND-2026-08-14-v1` closes the initial reviews' object, question,
domain, normalization, completion-map, quotient-path, positive-time, and Route
findings.  It does not claim any theorem: `Q_p` properties, invariant-measure
lifting, full/reduced equality, fibre factorization, trace domains,
singularity, common restriction, and arithmetic promotion all remain Phase-2
source or Phase-3 proof obligations.  Independent exact-byte re-review is
required before Phase 2 begins.

`P8-PH2-TYPED-AMEND-2026-08-14-v1` supersedes the Phase-1 wording that placed
finite point evaluation on a continuous centre.  The exact one-orbit source
theorem instead gives `A_L ~= C(T) tensor K(H)`, with `Z(A_L)=0`.  Accordingly
P8-6 and controls 9/14 now use a trace-finite full rank-one corner.  The same
amendment applies the preregistered representation-sign correction:
`chi_theta(rL)=exp(ir theta)` yields frequencies `(2pi n-theta)/L` and return
phase `exp(+ir theta)` under Williams's induced-function convention.  The
primary question, outcome trichotomy, normalization, completion map,
P8-1--P8-5/P8-7--P8-9, stop rules, and Route ceiling are otherwise unchanged. See
`phase2_domain_amendment.md`; independent exact-byte re-lock is mandatory
before Phase 3.
