# Paper 8 candidate lock — source action groupoid and isotropy traces

Lock status: **PHASE 2 TYPED AMENDED v2 — INDEPENDENT RE-LOCK PASS**  
Date: 2026-08-14  
Route scope: Route A audits A0--A3, with at most A1 credit; A4 and Route B closed

Amendment ID: `P8-PH1-AMEND-2026-08-14-v1`.  Original bytes
`d1d11519bd8661be1a62f5cf7bdc34e14a929a79776c52001b2a0d362082cc8a`
retain only their historical `REVISE` reviews.  See `phase1_amendment.md`.

Phase-2 amendment ID: `P8-PH2-TYPED-AMEND-2026-08-14-v1`; see
`phase2_domain_amendment.md`.  It corrects the P8-6 centre/corner domain and
applies the preregistered simultaneous Floquet/character sign correction after
the one-orbit source audit.  No candidate, outcome, normalization, or Route
scope is changed, and no theorem is pre-credited.

This lock separates the source flow groupoid from every representation and
trace placed on it.  It does not import the decomposable algebra or zero-mode
determinant of Paper 7.

## 1. Source owner

### `DEN-WITT-Z-FIN`

- Object: Deninger's rational-Witt `R`-flow over `Spec Z`, restricted to the
  admissible finite-kernel character subsystem `E_f`.
- Source-owned fields: one compact periodic packet `Gamma_p` for each rational
  closed point `(p)`, least period `L_p=log p`, isotropy/repetition
  `(log p)Z`, and exhaustion of the nontrivial periodic set by the packets.
- Not source-owned at lock time: a packet product chart, transverse measure,
  transformation-groupoid trace, isotropy-character disintegration, normal
  representation, or determinant.

## 2. Groupoid records

### `DEN-EF-PACKET-ACTION-GRPD-P`

- Evidence class: `DERIVABLE_NEW_DEFINITION` canonically constructed from the
  source-defined flow; not a groupoid defined or analytically owned by
  Deninger's source.
- Unit space: one actual source packet `Gamma_p` with its inherited source
  topology; the ID denotes the per-prime theorem family, not one global union.
- Arrows: `(x,t)` from `x` to `phi^t(x)`.
- Candidate Haar system: Lebesgue measure in the `R` time coordinate.
- Required gate: locally compact Hausdorff and all countability/amenability
  hypotheses used by the selected groupoid theorems.
- Status at lock: precisely defined candidate; source/topology/operator audit
  pending.

### `DEN-EF-PACKET-ORBIT-QUOTIENT-Q`

- Compact action candidate: `K_p=R/(L_p Z)` acts on `Gamma_p`; exact common
  isotropy predicts that the action is free.
- Quotient: `q_p:Gamma_p -> Q_p=Gamma_p/K_p` with the quotient topology.
- Source boundary: compact Hausdorffness, countability, local triviality, and
  measure lifting are theorem gates.
- Prohibition: `Q_p` is not identified with the abstract `B_p`, and `q_p` is
  not called a trivial bundle, without a T0--T7 theorem.

### `DEN-EF-PACKET-COPROD-GRPD`

- Unit space: the chosen topological coproduct `coprod_p Gamma_p`.
- Role: optional finite-support/global-domain assembly control only.
- It is not the inherited subspace topology on the all-prime periodic set.
- A kernel constant on all prime components is not assumed to be compactly
  supported or trace-integrable.

### `DEN-EF-ORBIT-ACTION-GRPD`

- Unit space: one actual periodic orbit `O_x` contained in `Gamma_p`.
- Intrinsic description: `R/(L_p Z)` as an `R`-homogeneous space, with length
  Haar `du` of total mass `L_p`, separately normalized probability `du/L_p`,
  and isotropy `L_p Z`.
- Role: source-local control that does not assume
  `Gamma_p = B_p x R/(L_p Z)` topologically or measurably.
- Topology status: the inherited-orbit homeomorphism is a preregistered
  `DERIVABLE_NEW_LEMMA` using the corrected `E_f` Morishita restriction; it is
  not source credit at lock time.
- Cross-packet limitation: it does not select an orbit, a transverse measure,
  or a component mass.

### `DEN-PACKET-PROD-ISO-GRPD`

- Unit space:
  `Y=disjoint_union_p B_p x (R/L_p Z)`, where
  `B_p=Zhat_(p)^x/p^Zhat` has its compact-group topology.
- Arrows: the product translation action groupoid `Y rtimes R`.
- Role: explicit calculation and deterministic controls.
- Ownership boundary: separate proxy.  A set-level packet parametrization is
  insufficient to transport its topology, measure, groupoid algebra, or
  trace to `DEN-EF-PACKET-ACTION-GRPD-P`.

## 3. Trace records

### `DEN-EF-GRPD-REG-TRACE-FAM`

- Inputs: one per-prime source action groupoid and a verified
  `nu_p in Prob(Q_p)`; the candidate unit measure uses length Haar along each
  orbit.  Packet and cross-prime masses are not hidden parameters.
- Representation: regular groupoid/crossed-product representation fixed by a
  primary-source construction.
- Trace type: FNS trace if the unimodular invariant-measure hypotheses prove
  traciality; otherwise the exact Plancherel weight type must be stated.
- Proposed time-only value at the common length scale: dual-Haar averaging
  cancels every nonzero return and gives `L_p f(0)`.
- Status: theorem targets P8-1, P8-2, and P8-4; unproved at lock time.

### `DEN-EF-GRPD-TRIVCHAR-TRACE-FAM`

- Isotropy character: the group-theoretically distinguished trivial character
  of `L_p Z`; it is frozen before any Euler-product comparison.
- Representation: representation induced from that character on each selected
  source orbit or on a proved packet disintegration.
- Trace type: proposed lower-semicontinuous semifinite trace/weight on the
  corresponding groupoid `C*`-algebra image.
- Proposed time-only value:
  `L_p sum_(r in Z) f(rL_p)`.
- Normality boundary: expected to be singular and to have no normal extension
  to the regular von Neumann completion; this must be proved.
- Finite-corner gate: after proving the exact one-orbit model
  `A_L ~= C(T) tensor K(H)`, fix a full rank-one projection
  `p=1 tensor e` with `tau_theta(p)=1`.  The bounded character evaluation lives
  on `p A_L p ~= C(T)`, not on a central subalgebra of `A_L`.  Here
  `Z(A_L)=0`; on the multiplier centre `C(T) tensor 1`, the uncompressed
  character weight is generally infinite.
- Assembly boundary: a canonical isotropy character does not select a
  transverse measure, normalize a packet, or set cross-prime masses.

The **one-orbit** completion diagram is the first mandatory map:

```text
A_L=C*(O rtimes R) -> A_(L,r)=C*_r(O rtimes R) -> M_L^reg,
A_L -> pi_(L,theta)(A_L) subset K(H_(L,theta)).
```

The full packet diagram is a separate conditional record:

```text
C*(G_p) -> C*_r(G_p) -> M_(p,nu)^reg,
C*(G_p) -> pi_(q,theta)(C*(G_p)) subset B(H_(q,theta)).
```

Full/reduced equality, factorization of the fibre representation, its
compact-operator image, and any extension to the regular von Neumann algebra
must each be proved.  Morita equivalence alone supplies none of these arrows.
The rank-one corner belongs to `A_L`.  A local no-normal-extension result does
not transfer to `M_(p,nu)^reg` without a packet restriction/disintegration
same-map theorem; absent packet Hausdorff/LCH, that promotion is
`NOT_TESTABLE` rather than `REFUTED`.

### `DEN-EF-GRPD-TIME-RETURN-LOCAL`

- Domain: one per-prime packet and only the frozen time-only kernels
  `a_(p,f)(x,t)=f(t)` with `f in C_c^infinity(R)` on the proved pullback trace
  domain.
- Candidate definition: the common restriction, at the frozen common scale, of
  trivial-character traces, if P8-5/P8-7 prove independence from orbit and
  transverse choices.
- Status: a restricted functional, not a full canonical packet trace and not
  a determinant.

### `DEN-EF-GRPD-TIME-RETURN-FIN`

- Domain: algebraic finite-prime-support direct sum of local time kernels.
- Coefficients: one per source closed point under counting measure; arbitrary
  weights create a different candidate.
- Status: a finite assembly only; it makes no global `C*` or `L1` claim.

### `DEN-EF-GRPD-TIME-RETURN-POS`

- Test class: `f in C_c^infinity((0,infinity))`.
- Definition target:
  `Theta_+(f)=sum_p L_p sum_(r>=1) f(rL_p)`.
- Convergence: locally finite by compact positive-time support.
- Type: positive-time Radon distribution/measure, not a star-algebra trace and
  not evaluation of a global all-prime operator unless a separate domain
  theorem is later frozen and proved.

## 4. Frozen conventions

```text
fhat(xi) = integral f(t) exp(-it xi) dt,
chi_theta(rL)=exp(ir theta),
xi(u+rL)=exp(-ir theta)xi(u),
T_theta(f)=sum_n fhat((2pi n-theta)/L)
             =L sum_r f(rL)exp(+ir theta).
```

The sign follows from the locked arrow/convolution convention together with
the sourced induced-function rule `xi(u+rL)=chi_theta(rL)^(-1)xi(u)`.  The
simultaneous correction is versioned in the Phase-2 typed amendment and is
independent of any target formula.

The regular average and trivial fibre are different owners at one common
length-Haar scale:

```text
(1/(2pi)) integral T_theta(f) dtheta = L f(0),
T_0(f)=L sum_r f(rL).
```

At orbit-probability scale both values are divided by `L`.  These are
preregistered targets, not established facts at lock time.

## 5. Controls

- `FINITE-ISOTROPY-CHAR-GRID`;
- `NONTRIVIAL-CHAR-PHASE`;
- `REGULAR-VS-TRIVCHAR`;
- `SINGLETON-TRANSVERSE-BASE`;
- `ARBITRARY-TRANSVERSE-PROB`;
- `COPIED-PACKET-GROUPOID`;
- `ARBITRARY-CLOCK-ISOTROPY`;
- `COMPOSITE-CLOCK-ISOTROPY`;
- `POINT-EVAL-NONNORMAL`;
- `ZERO-TIME-REGULAR-TRACE`;
- `COMMON-SCALE-NORMALIZATION`;
- `LOCAL-FINITE-GLOBAL-DOMAIN`;
- `CENTER-REPRESENTATIVE-EXTENSION`;
- a transverse-observable test that distinguishes full traces even when their
  time-only restrictions agree.

All controls are deterministic and target-free.

## 6. Ownership and Route boundary

- A newly derived source-flow action groupoid inherits its unit and arrow data
  from the source flow, but neither the groupoid definition nor any trace is a
  Deninger source theorem merely from that construction.
- A Haar system supplies convolution; it is not an invariant/transverse unit
  measure and not a normal trace.
- A Morita equivalence is recorded as such; it is not silently strengthened
  to an isomorphism or same-object transport.
- The regular trace and character-fibre trace have different completions and
  normality properties and cannot exchange credits.
- Choice-independence on the time-only test algebra does not prove uniqueness
  of a full packet trace.
- Closed-point counting, packet normalization, and cross-prime masses require
  a target-free T7 provenance argument.
- No candidate owns a Ruelle/Fredholm/semifinite determinant in this paper
  unless a new typed determinant record is separately frozen after Phase 1.
- The maximum possible positive result is a typed A1 analytic ledger.  Every
  record has `A2_FAIL` or `A2 NOT_TESTABLE`; A3 is `A3_FAIL`.
- A4 and Route B are not invoked, `route_b_invocation_allowed=false`, and
  Hilbert--Polya claims are forbidden.

## 7. Forbidden inputs and promotions

- Riemann zero data or any fitted spectral statistic;
- a desired Euler product used to select `theta`, masses, normalization, or
  completion;
- the Paper 7 proxy algebra or zero-mode projection treated as groupoid-owned;
- Morishita's enlarged full-character object substituted for `E_f`;
- point evaluation on `L-infinity(T)` called normal;
- a local orbit trace called a canonical packet trace;
- a product chart or measure transport without a T0--T7 theorem;
- an analytic continuation, completed function, or quantum operator claim.

## 8. Phase-1 pass conditions

Independent review must confirm that:

1. all groupoid, quotient, trace, and three return-domain records above are
   non-overlapping;
2. source, orbit restriction, and product proxy cannot be coordinate-spliced;
3. regular/FNS and singular `C*` traces are correctly distinguished;
4. the trivial character is frozen algebraically rather than target-selected;
5. packet/transverse/cross-prime normalizations remain explicit;
6. the theorem targets can refute the primary hypothesis without tuning; and
7. A1 is the maximum possible positive analytic credit, A2/A3 cannot pass,
   and Route B remains closed.

## 9. Source-selected extension criterion

The primary question is confirmed only if the trivial-character return
functional extends normally along the fixed completion diagram and the
resulting trace is determined by the source flow, invariant under its
flow-equivariant automorphisms, uses the frozen Lebesgue/length normalization,
and contains no free `nu_p` or cross-prime weight.  Failure of normal extension
or unavoidable free choices refutes that primary claim.  Missing topology or
comparison maps yield `NOT_TESTABLE`.

Regular cancellation and a singular return-sensitive `C*` trace may both be
proved; they are complementary subresults, not mutually exclusive answers.
