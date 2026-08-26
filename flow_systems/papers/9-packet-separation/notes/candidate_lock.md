# Paper 9 candidate lock

Lock date: 2026-08-14 (Asia/Shanghai)  
Status: **PHASE 1 AMENDED v1 — EXACT-BYTE RE-LOCK PENDING**

## 1. Primary record

```yaml
candidate_id: DEN-EF-PACKET-QUOTIENT-TOPOLOGY-P
family: continuous-time arithmetic suspension
source_scheme: Spec Z
character_class: E_f
prime_scope: one fixed rational prime p
pre_suspension: Xcheck_0(C)_{E_f}
suspension: (Xcheck_0(C)_{E_f} x R_{>0}) / Q_{>0}
action: (P,u)q = (F_q P, q^{-1}u)
packet: Gamma_p with inherited subspace topology
clock: log p from exact stabilizer p^Z
normalization: multiplicative time u; additive time t=log u
determinant_convention: none
orbit_cutoff: none
precision: exact theorem; deterministic integer controls only
training_data: none
forbidden_data: Riemann zeros, fitted clocks, fitted weights, substituted topology
route_b_invocation_allowed: false
```

## 2. Exact exponent model used only for proof

Convention: `N={1,2,...}` and every denominator exponent satisfies
`k in Z_{>=0}`.

For a chosen geometric point above `p`, fix an injective character `chi`.
Write

```text
A_p = Zhat_(p) = product_{ell != p} Z_ell,
U_p = Zhat_(p)^x,
H_p = p^{Zhat} subset U_p.
```

An exponent `a in U_p` gives an injective character `chi^a`.  An exponent
`m p^{-k}` with `m in N`, `k in Z_{>=0}` gives a finite-kernel character and hence remains
in `E_f`.  Galois quotienting identifies the unit exponent only modulo `H_p`.
This model does not authorize a product topology on `Gamma_p`.

Freeze the three levels

```text
Ptilde_a=(x,chi^a),       P_a=pi_G(Ptilde_a),       j(P_a) in Xcheck.
```

At raw-character level `F_{m/p^k}` is represented by exponent
`a m p^{-k}`.  The equality `F_{m/p^k}(P_a)=F_m(P_a)` uses the packet
stabilizer and is asserted only at the quotient point; the analogous raw
character equality is forbidden.

## 3. Exact restricted quotient object

```text
C_p^{E_f} = Deninger's Q_{>0}-invariant packet fibre in Xcheck,
Z_p       = C_p^{E_f} x R_{>0},
R_p       = {((P,u),(F_qP,q^{-1}u)): q in Q_{>0}},
Gamma_p   = Z_p/R_p.
```

`Z_p` is saturated for the global diagonal action.  The global orbit quotient
is open, hence the restricted quotient map is open and the quotient topology
on `Z_p/R_p` equals the subspace topology inherited by `Gamma_p`.  This lemma
must be proved on the source object before any coordinate argument is used.

## 4. Frozen approximation candidate

The candidate approximation set is

```text
D_p = {m/p^k : m in N, k >= 0} subset R_{>0} x A_p.
```

The independent arithmetic lemma tests whether `D_p` is dense in
`R_{>0} x A_p`.  The source separation theorem uses only targets in
`R_{>0} x U_p`, so its limiting character stays inside `E_f`.  A target in
`A_p` whose exponent has infinite kernel is an ambient negative control and
confers no `E_f` convergence.  The constructive witness must use finite CRT congruences
and a real interval estimate.  Merely citing density of rational numbers is
invalid because the real and profinite requirements are simultaneous.

## 5. Frozen point comparison

For

```text
x = class of (P_b,u),
y = class of (P_a,v),
```

the proposed same-class representatives are

```text
z_j = (F_{q_j}(P_b), q_j^{-1}u),
q_j in D_p.
```

Every `z_j` must map to `x` under the suspension quotient.  The proposed limit
is `(chi^a,v)` when

```text
q_j -> u/v in R_{>0},
q_j -> a b^{-1} in U_p.
```

The legal convergence route is first raw and fixed-stage:

```text
chi^{b q_j} -> chi^a pointwise in the initial p-fibre,
P_{b q_j}   -> P_a after the continuous Galois quotient,
j(P_{b q_j})-> j(P_a) through the named open colimit-stage inclusion.
```

Only then may the suspension quotient be applied.  The proof must
independently show that every packet point admits a unit-exponent/time
representative, prove its exact set equivalence modulo `p^{Zhat}` and `p^Z`,
and distinguish `x` from `y` when required.

## 6. Object namespace

| ID | Type | Source ownership |
|---|---|---|
| `DEN-EF-PACKET-QUOTIENT-TOPOLOGY-P` | actual packet | source object and topology |
| `DEN-EF-ORBIT-INHERITED-TOPOLOGY-P` | actual orbit subspace | source orbit; topology under test |
| `DEN-EF-ORBIT-STD-CIRCLE-PROXY` | compact-Hausdorff retopology | `MODELING_CHOICE`; control only |
| `DEN-EF-PACKET-SET-PARAM` | set parametrization | source set bijection; no topology credit |
| `DEN-EF-PACKET-ORBIT-QUOTIENT-Q-P` | `Q_p=Gamma_p/K_p`, quotient topology, `K_p=R_{>0}/p^Z` | intrinsic derived quotient; always defined; not `B_p` |
| `MOR-CC-Cp-INHERITED` | adelic target orbit with actual quotient subspace topology | exact printed topology must be audited |
| `MOR-CC-Cp-STD-CIRCLE-PROXY` | ordinary `R_{>0}/p^Z` topology | separate retopology/control; no inherited-topology credit |

No record may inherit another row's topology, measure, completion, trace, or
Route coordinate.

The flow-kernel action defining `Q_p` is continuous.  If `Gamma_p` is proved
indiscrete then `Q_p` is indiscrete by the quotient definition.  An orbit-only
verdict does not classify `Q_p`; no outcome identifies it with a transverse
product base or gives it T3--T7/analytic Route credit.

## 7. Primary claims under test

```text
C1  simultaneous real/profinite approximation exists;
C2  unit-target approximation acts inside the exact E_f source domain;
C2a full A_p density is arithmetic-only and may converge outside E_f;
C3  one diagonal suspension class has more than one topological limit;
C4  Gamma_p is non-T1/Hausdorff, possibly indiscrete/non-T0;
C5  the standard-circle/product set parametrization is not a homeomorphism;
C6  the restricted diagonal equivalence relation is not closed;
C7  the standard LCH-Hausdorff packet groupoid branch is refuted;
C8  Paper-8 actual-orbit ownership and standard-circle proxy formulas are
    adjudicated claim by claim;
C9  no analytic/determinant/Route-B promotion follows.
```

`C4` is explicitly tiered: non-closed singleton is the minimum theorem;
indiscreteness requires the universal two-point approximation.

## 8. Decision tiers and Paper-8 correction branches

The primary tiers are `CONFIRM_MINIMAL`, `CONFIRM_ORBIT`, `CONFIRM_STRONG`,
`REFUTE_OBSTRUCTION`, and `NOT_TESTABLE` exactly as defined in the protocol.
No orbit-only result may be promoted to a packet result.

| Branch | Required Stage-9 action if the obstruction is proved |
|---|---|
| actual inherited orbit and its LCH-Hausdorff action groupoid | `supersedes`: failed actual-topology premise and downstream ownership |
| standard-circle calculations | `retypes`: proxy-only mathematics; no actual-source topology/trace transport |
| packet standard LCH-Hausdorff route | `supersedes`: route refuted, without universal non-Hausdorff no-go |
| positive-time coefficient-one scalar ledger | preserve as an independent typed analytic ledger |

## 9. Negative and positive controls

| Control | Expected role |
|---|---|
| replace `Q_{>0}` by `p^Z` | standard Hausdorff circle; must reject the indiscrete mechanism |
| standard-circle proxy | validates local Poisson/groupoid algebra only after explicit retopology |
| finite CRT modulus | exact finite witness, never an infinite proof |
| wrong action `(P,u)q=(F_qP,qu)` | sign test; expected formula changes |
| exponent with infinite kernel | domain-negative control; excluded from `E_f` |
| several small primes `p` | theorem-uniformity check; not statistical evidence |

## 10. Route lock

Primary evaluation scope is A0--A1 only.  A2/A3/A4 are frozen `FAIL` absent
independent complete inputs.  Route B is false and no Route-B YAML may be
written.

If the inherited topology is non-Hausdorff, the correct consequence is a
versioned obstruction and ownership correction—not a claim that all
non-Hausdorff groupoids or noncommutative quotients are impossible.

## 11. Historical-artifact rule

Paper 8 and its Stage-8 YAMLs are immutable historical records.  If Paper 9
finds a topology error, it must:

1. state the exact failed premise and proof locator;
2. preserve every algebraic formula that remains valid on the retopologized
   standard-circle proxy;
3. create new Stage-9 evaluations rather than overwrite Stage-8 YAMLs; and
4. update shared registries with an explicit supersession link.
