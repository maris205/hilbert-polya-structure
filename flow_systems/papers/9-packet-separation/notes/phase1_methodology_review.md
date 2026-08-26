# Paper 9 Phase-1 independent methodology and same-object review

Review date: 2026-08-14 (Asia/Shanghai)  
Review scope: Phase-1 design, same-object ownership, topology feasibility,
Paper-8 supersession, and Route ceiling only  
Decision: **PASS TO PHASE 2 ON THE EXACT LOCKED BYTES**  
Open findings: **0 Critical / 0 Major / 0 Minor**

## 1. Independence boundary and exact input lock

This is an independent ARS methodology/reviewer/integrity review.  It does
not inherit Paper 8's one-orbit topology verdict.  It uses no web search,
Riemann-zero data, fitted parameter, manuscript claim, or Route-coordinate
maximum.  No active lock, source file, manuscript, or Route YAML is edited by
this review.

The exact Paper-9 design bytes reviewed are:

| Artifact | SHA-256 |
|---|---|
| `README.md` | `d11c93dbf1126029620bbbe075883b50fdd9482b3211dbe35a4873ec479d8c8a` |
| `notes/research_protocol.md` | `187255115b5d930a50fadb89f0ea83f6cc375a3e5b704005e4103cfb1c4f478d` |
| `notes/candidate_lock.md` | `1dedf333d5142cc66c4fdf5a08b4a2f8c55f449fb1c836a7046a2df2e919d0ac` |
| `notes/pipeline_state.md` | `f3d2c04a14552310526e97d2145f3d8f58ab8d436181dcb99877d6f8dc98731e` |

The Paper-8 historical claims were audited against these exact current
records:

| Artifact | SHA-256 |
|---|---|
| `notes/proof_audit.md` | `1bbcc8f7faadb331ff0840c26472ee16722894b6dff2cae2687216e4638a5990` |
| `notes/route_audit.md` | `355cf28868a1c9beaa30924a87d8cfc34214b5160c2ca4ca21d72824f5f37b4e` |
| `notes/release_audit.md` | `f4912ff10e92d481e08ec8b41f5dbc6750a048e9d6ed38ac51a72f298106b641` |
| `notes/peer_review_round1.md` | `02bb7301376aa5b3644a6796c62b870b36b6f6825b085f47ee121bc5ab17b4a7` |
| `notes/phase3_topology_ownership_proofs.md` | `209989444b48a625777c0c4626b92429ed08b58f3dc4c31b03f7d23b067dca14` |
| `notes/phase2_source_topology_audit.md` | `f76dc87df56bacc54ea420447b28cb37020fc2625fa97d2eca2f173278ee83a3` |

The local retained primary manifestations used only to stress-test whether
the proposed topology theorem is feasible have SHA-256 values
`edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09`
(Deninger v4) and
`3a5a34165a4bedfefb2c06f43f4e40e416882ae3406a9cd043f6ac12aebb21ae`
(Morishita v5).  Formal source/locator credit remains a Phase-2 obligation.

## 2. Executive methodology verdict

The research question is important, feasible, two-sided, and correctly
placed upstream of every analytic claim.  The locks freeze one actual
Deninger `Spec Z`, `E_f`, fixed-`p` suspension packet with its quotient/subspace
topology and separately type the inherited orbit, standard-circle retopology,
set parametrization, intrinsic quotient, and Morishita target.  They forbid
exactly the topology, measure, completion, and scalar splices that invalidated
the Paper-8 ownership chain.

The proposed simultaneous-approximation mechanism survives an independent
constructive stress test.  More strongly, it has a direct route to universal
singleton closure, not merely to two nonseparable points.  This does not make
the theorem a Phase-1 result: Phase 2 must still close every source-topology
arrow, and Phase 3 must state the proof on the exact locked object.  It does
show that the design is neither vacuous nor dependent on an unavailable
disintegration theorem.

No lock amendment is required before Phase 2.  The acceptance conditions in
Sections 4--10 below are applications of obligations already written into
P9-1--P9-9 and the stop rules; they may not be weakened during execution.

## 3. Falsifiability and status-language audit

The four primary outcomes in `research_protocol.md` Section 5 are mutually
exclusive once the exact topology arrows are fixed:

| Outcome | Required evidence |
|---|---|
| `CONFIRM_STRONG` | For arbitrary actual packet points `x,y`, a net or sequence constantly equal to `x` in the quotient converges to `y`; nontriviality is separately proved. |
| `CONFIRM_MINIMAL` | One explicitly distinct pair `x != y` has `y in closure({x})`, or an explicit convergent sequence of related prequotient pairs has an unrelated limit. |
| `REFUTE_OBSTRUCTION` | A named approximation, domain, topology, quotient, or distinctness arrow fails and a positive closed-relation/Hausdorff theorem is actually proved. |
| `NOT_TESTABLE` | The exact source topology/action cannot be reconstructed well enough to prove either the obstruction or its negation. |

Two status boundaries are load-bearing:

1. If nonseparation is proved, the assertion that the actual inherited orbit
   or packet is a Hausdorff standard circle/LCH unit space is **refuted**.
2. A normal-extension assertion on a standard LCH completion that cannot be
   constructed for that actual object is then **not testable**.  It is not
   promoted to `REFUTED` merely because its prerequisite was refuted.

Conversely, the already proved no-normal-extension theorem on a separately
retopologized standard-circle proxy remains a genuine proxy-level
`REFUTED` result.  The same word therefore may occur on two different claims,
but never on one spliced owner.

## 4. Independent feasibility stress test of P9-1--P9-3

This section is a methodology stress test, not a substitute for the formal
Paper-9 proof audit.

### 4.1 Constructive simultaneous approximation

Let `A_p=prod_(ell != p) Z_ell`.  Choose a cofinal sequence of positive
moduli `M_j`, each prime to `p`, such that convergence modulo all `M_j`
detects convergence in `A_p`.  Given `c>0` and `a in A_p`, choose `k_j` and
the residue `r_j` satisfying

```text
r_j = a p^(k_j)  (mod M_j).
```

Choose a positive integer `m_j` in the residue class `r_j mod M_j` nearest
to `c p^(k_j)`.  Taking `k_j` sufficiently large gives

```text
|m_j/p^(k_j) - c| <= M_j/(2 p^(k_j)) -> 0,
m_j/p^(k_j) = a                    (mod M_j A_p).
```

Thus `q_j=m_j/p^(k_j)` tends simultaneously to `c` in `R_{>0}` and to `a`
in `A_p`.  Positivity causes no obstruction.  If a numerator formulation is
preferred, choose `k_j` additionally in a multiple of the order of `p`
modulo `M_j`; then `p^(k_j)=1 mod M_j` and `m_j -> a` profinitely as well.
The proof must not silently interchange `m_j -> a` and `q_j -> a` without
recording this gauge choice.

For the separation theorem the target is in `U_p=A_p^x`.  Density in all of
`A_p` is a stronger elementary statement, but a limit exponent outside the
finite-kernel domain may not be used as an `E_f` endpoint.

### 4.2 Fixed-stage character convergence

For every root of unity `zeta` of order prime to `p`, profinite convergence
`q_j -> a` implies eventual congruence modulo `ord(zeta)`, hence

```text
zeta^(b q_j) = zeta^(b a)
```

eventually.  Rational exponentiation by `p^(-k_j)` is the inverse Frobenius
automorphism on `Fbar_p^x`; multiplying by `m_j` leaves a finite kernel.
Consequently every finite-stage character is legal in `E_f`, and pointwise
convergence occurs already in one fixed residue-character stage.  Phase 2
must still cite the exact pointwise, Galois-quotient, admissible-`E`, and
colimit topology maps.  The proof may use continuity of those maps, but may
not infer convergence from Deninger's set bijection (38).

The equality `F_p(P)=P` holds at the Galois-quotient point over `p`; it does
not license equality of arbitrarily chosen raw character representatives.
The two equivalent proof gauges are therefore:

- work with the raw exponent `q_j` and then pass through the Galois quotient;
  or
- use `F_(q_j)P=F_(m_j)P` and choose numerator congruences compatible with
  the `p^{Zhat}` quotient.

Mixing the raw and quotient gauges in one unlabelled equation would fail the
same-object test.

### 4.3 Constant-class convergence

Normalize packet endpoints as

```text
x = [(chi^b,u)],    y = [(chi^a,v)],
```

with `a,b in U_p`.  The universal claim must include the elementary
normalization lemma: every finite-kernel exponent `a nu` can be moved by the
diagonal action to a representative with unit exponent, with the factor
`nu` transferred to the real coordinate.  This is set normalization, not a
product-topology assertion.

Apply P9-1 with

```text
q_j -> u/v        in R_{>0},
q_j -> a b^(-1)  in U_p.
```

Then

```text
z_j=((chi^b)^(q_j),u/q_j) -> (chi^a,v)
```

in the exact prequotient topology, while every `z_j` represents `x`.  By
continuity of the suspension quotient map, the constant sequence `x,x,...`
converges to `y`.  This argument uses the locked inverse sign.  The wrong-sign
control changes the required real target to its inverse; because the density
mechanism is symmetric, that control catches orientation errors but is not
expected to restore Hausdorffness.

For a minimal distinctness witness, take `a=b` and choose `u/v` outside
`p^Z`.  Exact isotropy then gives `x != y`.  For universal closure, use the
unit-normalization lemma and arbitrary `a,b,u,v`.

### 4.4 Restricted equivalence relation

Let `R_p` be the diagonal orbit relation restricted to the preimage of the
packet.  The pairs

```text
((chi^b,u), z_j) in R_p
```

converge to `((chi^b,u),(chi^a,v))`.  With the distinctness choice above, the
limit pair is not in `R_p`.  This gives the explicit nonclosed-relation
witness required by P9-6.  It is stronger and more informative than invoking
the general slogan that a quotient is non-Hausdorff.

## 5. Exact topology consequences to test

If the Phase-2 topology arrows in Section 4 close, the Phase-3 theorem should
state the following without euphemism:

| Object | Separation | Compactness/local property | Function/Borel consequence |
|---|---|---|---|
| actual packet `Gamma_p` | indiscrete; non-`T0`, non-`T1`, non-Hausdorff once nontriviality is stated | quasi-compact and second countable; locally quasi-compact in the non-Hausdorff sense, but not LCH in the frozen Hausdorff groupoid sense | every continuous map to a Hausdorff space is constant; Borel sigma-algebra is trivial |
| one actual inherited orbit | indiscrete and non-`T0/T1` (it has more than one set point by exact stabilizer `p^Z`) | quasi-compact, not a Hausdorff circle | its standard-circle set parametrization is not a homeomorphism |
| `Q_p=Gamma_p/K_p` | quotient topology is indiscrete; state separately whether the set has more than one point | always a meaningful topological quotient and quasi-compact; not a Hausdorff transverse base when nontrivial | `C(Q_p)` is constant and the Paper-8 separation clause is vacuous |

“Locally compact” has incompatible conventions outside the Hausdorff
category.  The paper should report locally quasi-compact and Hausdorffness
separately, and use `LCH` only for the standard locally compact Hausdorff
framework.  It must not claim that non-Hausdorffness alone rules out every
possible non-Hausdorff groupoid algebra.

No disintegration theorem is needed to prove the topology obstruction.  A
Radon/Riesz disintegration theorem would be needed only for a later analytic
promotion, and its Hausdorff/LCH hypotheses fail on the actual object under
the strong result.  P9-7 correctly requires that branch to stop.

## 6. Morishita `C_p` topology audit

Morishita equation (1.1.5) defines `C_p` as an orbit inside the double
quotient `Q^x\A/U_K`.  The phrase “by projection to the infinity component,
`C_p` is isomorphic to the circle” does not prove that the subspace topology
from this quotient is the usual topology on `R_{>0}/p^Z`.

Indeed, write `e_p(r)` for the adele with finite components `0` at `p`, `1`
away from `p`, and infinity component `r`.  For the simultaneous
approximants above, all `q_j e_p(r)` represent the same quotient point as
`e_p(r)`, while in the adele space they converge to a vector whose away-`p`
components form a unit `a` and whose infinity component is `cr`.  Right
quotienting by that unit identifies the limit with `e_p(cr)`.  Hence the same
constant-class convergence mechanism applies to the actual inherited
`C_p` subspace.  Its orbit topology is therefore expected to be indiscrete,
while the usual circle is a separate retopology.

This resolves the apparent contradiction in Paper 8.  Morishita's continuous
map may still restrict to a bijection (indeed a homeomorphism) between the
actual indiscrete Deninger orbit and the actual indiscrete adelic orbit.  What
fails is the additional identification of the latter with a Hausdorff
standard circle.  Phase 2 should use two explicit labels in prose and later
typed records:

```text
MOR-CC-PRIME-ORBIT-Cp-INHERITED
MOR-CC-PRIME-ORBIT-Cp-STD-CIRCLE-PROXY
```

This is an execution requirement already entailed by the active lock's
no-substitution rule, not a request to modify the lock bytes reviewed here.

## 7. T0--T7 same-object verdict

The Paper-3 certificate and the Paper-9 theorem labels remain correctly
disjoint.  The exact post-theorem ownership ceiling is:

| Field | Actual packet / inherited orbit | Standard-circle proxy |
|---|---|---|
| `T0` object identity | PASS: exact `Spec Z`, `E_f`, fixed `p` source object | PASS only as a newly typed modeling choice; not source topology |
| `T1` topology/Borel | expected strong result: inherited topology indiscrete, so the Paper-8 Hausdorff claim is REFUTED | PASS by definition for the imposed standard circle |
| `T2` flow/clock | PASS for continuous source flow, exact action sign, and stabilizer/clock; “topological circle” does not pass | PASS for the retopologized translation flow, with source clock retained only through an explicit set/action comparison |
| `T3` groupoid/Haar/completion | topological action groupoid remains definable, but the frozen second-countable LCH Hausdorff completion framework is REFUTED at its topology gate; replacement theory is not tested | Paper-8 LCH groupoid/Haar/completion proofs may be re-owned here after versioning |
| `T4` measure | no transverse source probability; inherited Borel sigma-algebra is trivial under the strong result | orbit Haar is a modeling measure, not a packet transverse measure |
| `T5` representation/trace | actual-source standard completion and normal-extension question are NOT_TESTABLE | Paper-8 regular and character trace theorems survive on their exact proxy maps |
| `T6` test algebra/formula | no actual-source operator formula follows from topology | local Poisson/trace formulas survive with proxy ownership only |
| `T7` arithmetic promotion | PASS only for `(p)` and `log p`; no analytic weight/determinant promotion | at most a weak source relation through the copied label/clock |

The scalar `Theta_+` record is outside this two-column transport.  Its one
closed point per prime and `log p` clock remain source-owned; its status is
not repaired or damaged by either packet topology.

## 8. Exact Paper-8 supersession boundary

Paper 9 must preserve the Stage-8 files as historical byte records and issue
new Stage-9 versions.  If `CONFIRM_STRONG` closes, the correct supersession
matrix is:

| Paper-8 assertion | Stage-9 status | What survives |
|---|---|---|
| every actual inherited orbit is a compact Hausdorff standard circle | **REFUTED**; the Morishita target topology was mis-typed | the set orbit, exact `p^Z` stabilizer, flow sign, and clock |
| actual one-orbit action groupoid is in the standard LCH Hausdorff framework | **REFUTED at T1/T3 prerequisite** | the abstract action formulas after explicit retopology |
| `A_L ~= C(T) tensor K`, Zak/Floquet formulas, FNS trace, character trace, and no-normal-extension theorem belong to the actual inherited orbit | **SUPERSEDED AS OWNER ATTRIBUTION**; actual completion claims become `NOT_TESTABLE` | the mathematics remains valid on `DEN-EF-ORBIT-STD-CIRCLE-PROXY`, subject to new typed version records |
| packet Hausdorff/LCH is open | **RESOLVED NEGATIVELY** at the topology gate | packet set, flow, exact common clock, quasi-compactness, and second countability |
| packet normal extension is `NOT_TESTABLE` | **REMAINS `NOT_TESTABLE`**, now because its frozen completion premise is refuted rather than merely open | no negative analytic theorem on a nonexistent actual completion |
| `Q_p` is an open quasi-compact second-countable quotient, not `B_p` | **SURVIVES**, sharpened to indiscrete topology | no Hausdorff/Radon/product-chart credit |
| continuous-function orbit average exists | **SURVIVES BUT BECOMES VACUOUS FOR SEPARATION** because the relevant continuous functions are constant | the algebraic averaging identity and total mass only |
| positive-time scalar `Theta_+` is a locally finite Radon ledger on `(0,infinity)` | **UNCHANGED** | exact closed-point coefficient and source clock, still not a packet trace |

The Paper-8 release verdict remains historically valid for its locked bytes;
Paper 9 supplies a mathematical supersession notice, not a retroactive edit
or a claim that the old topology attribution remains current.

## 9. Route-A and Route-B ceiling

No coordinate may be taken from a different row merely because all rows use
the clock `log p`.

| New/versioned owner | Maximum licensed Route interpretation |
|---|---|
| actual packet/topology record | `A0_ANALYTIC_ARITHMETIC_ORIGIN`; at most `A1_WEAK` for the source topology theorem itself; `A1_FAIL` for the frozen standard-LCH packet-groupoid branch; `A2_FAIL/A3_FAIL/A4_FAIL` |
| actual inherited-orbit standard-LCH groupoid record | `A0_ANALYTIC_ARITHMETIC_ORIGIN`, `A1_FAIL` at the topology prerequisite, `A2_FAIL/A3_FAIL/A4_FAIL` |
| retopologized standard-circle bare groupoid | at most `A0_WEAK_ARITHMETIC_RELATION`, `A1_WEAK`, `A2_FAIL/A3_FAIL/A4_FAIL` |
| retopologized regular-trace proxy | retain the mathematical `A1_FAIL` return-blind result, but only under a new proxy owner |
| retopologized trivial-character proxy | retain `A1_PASS_ANALYTIC` for the local repetition ledger and proxy-map `REFUTED` normal-extension result; no actual packet credit |
| scalar `DEN-EF-GRPD-TIME-RETURN-POS` | historical source-clock `A0/A1` result survives unchanged; it lends no topology or completion coordinate |

Route-B invocation remains Boolean `false`.  There is no same-object
self-adjoint generator, completed divisor, determinant identity, functional
equation, or A4 input.  Therefore no Route-B YAML is permitted, whether the
topology obstruction is confirmed or refuted.

## 10. Controls, integrity gates, and stop rules

The locked controls are sufficient if executed with the following exact
acceptance tests:

1. **CRT witness:** verify both the real error and the correct rational
   congruence `m_j p^(-k_j) mod M_j`; a numerator congruence alone is accepted
   only when `p^(k_j)=1 mod M_j` is also recorded.
2. **Character witness:** for a finite cyclic subgroup, compare the rational
   exponent modulo its exact order and verify finite kernel at every finite
   stage.
3. **Action sign:** show which of `u/v` and `v/u` is required.  Do not treat
   wrong-sign persistence of nonseparation as a failed control.
4. **Distinctness:** separately verify non-equivalence using exact stabilizer
   `p^Z` and, for transverse points, the quotient by `p^{Zhat}`.
5. **Fixed-stage topology:** the convergent characters must be displayed in
   one legal `E_f` stage before applying continuous quotient/colimit maps.
6. **`p^Z`-only negative control:** the properly discontinuous real
   suspension yields the usual Hausdorff circle and has no transverse
   real/profinite approximation channel.
7. **Illegal limit control:** an exponent with infinite kernel is not an
   `E_f` endpoint even if it is a limit in the larger full-character space.
8. **Morishita control:** distinguish the actual adelic quotient subspace
   from the standard-circle retopology before using the word “isomorphic”.

Finite computations remain illustrations and regression checks.  They cannot
prove density, indiscreteness, or nonclosedness.  After a negative separation
theorem, the analytic branch must stop; defining a non-Hausdorff groupoid
completion would be a new project and a new lock.

## 11. FINER and phase-gate decision

| Criterion | Score | Assessment |
|---|---:|---|
| Feasible | 5/5 | The constructive CRT and fixed-stage character route is short, exact, and target-free. |
| Interesting | 5/5 | It resolves the strongest unresolved Paper-8 same-object gate and changes the interpretation of an entire local operator package. |
| Novel | 4/5 | Novelty is clear within the project; external novelty remains for the bounded Phase-2 source audit. |
| Ethical/evidence-safe | 5/5 | No human data, zero fitting, hidden target, or adaptive topology is permitted. |
| Relevant | 5/5 | The theorem directly governs whether the actual arithmetic suspension can enter the intended LCH analytic framework. |

**Exact-lock verdict: PASS TO PHASE 2.**  The question, candidate, decision
rule, controls, T0--T7 boundary, historical-artifact rule, and Route ceiling
are mutually consistent on the exact hashes in Section 1.  Phase 2 is
authorized to verify source manifestations and topology arrows.  It is not
authorized to edit the active locks, claim the theorem from finite controls,
transport Paper-8 proxy analysis to the actual inherited topology, or create
Route-B records.
