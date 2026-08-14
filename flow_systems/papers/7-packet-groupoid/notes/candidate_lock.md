# Paper 7 candidate lock

Lock status: **PHASE 3 AMENDED (v1) — INDEPENDENT EXACT-BYTE RE-LOCK
PENDING**  
Date: 2026-08-14

Amendment ID: `P7-PH3-AMEND-2026-08-14-v1`; normative crosswalk:
`phase3_protocol_amendment.md`.  The pre-amendment bytes with SHA-256
`0a5712af3f1e9ad83db5191f588e43631510b066e2128cdf77b6b94802da62fa`
retain their historical Phase-1 PASS only.  The amended record does not inherit
that exact-byte verdict.

## Candidate records

### `DEN-WITT-Z-FIN`

- Object: published rational-Witt `R`-flow over `Spec Z` under the frozen
  finite-kernel admissibility condition.
- Owns: closed-point packet indexing, least periods `log p`, and repetitions.
- Does not yet own: a choice-independent transverse measure, decomposable
  algebra, trace ideal, return distribution, zero-mode family, or determinant.
- Current status: ordinary orbitwise product refuted; measured analytic fields
  remain `NOT_TESTABLE`.

### `DEN-WITT-PACKET-DECOMP-MASS-FAM`

- Object: explicit product proxies `Y_p=B_p x R/(log p)Z`.
- Topology/Borel structure: chosen product structure.
- Local measure: normalized Haar probability on the abstract compact `B_p`.
- Representation:
  `L2(B_p,mu_p) tensor L2(R/(log p)Z,du)`.
- Algebra:
  `M_p=L-infinity(B_p,mu_p) bar-tensor B(L2(S1_logp))`, assembled as the
  bounded von Neumann direct product.
- Trace family: on the positive cone,
  `tau_m=sum_p m_p tau_p`, `0<m_p<infinity`.
- Status: explicit decomposable operator-algebra enrichment; not claimed to be
  flow-generated or a groupoid von Neumann algebra.

### `DEN-WITT-PACKET-DECOMP-RETURN-DIST-M`

- Object: one frozen mass sequence plus the component time-smearings
  `C_(p,f)=integral f(t)U_p(t)dt`.
- Proposed functional:
  `Theta_m(f)=sum_p m_p Tr(C_(p,f))` on positive-time test functions.
- Ownership boundary: a locally finite componentwise return distribution; not
  `tau_m(direct-sum C_(p,f))` unless the global `L1(tau_m)` criterion holds.
- Status: theorem targets P7-1--P7-3 unproved at lock time.

### `DEN-WITT-PACKET-DECOMP-K0-M1`

- Object:
  `K_s=direct-sum_p p^(-s)(1_Bp tensor P_(0,p))` with unit central masses.
- Trace-domain gate: for unit masses the affiliated `L1` condition, bounded
  relative trace-ideal condition, and `||K_s||<1` gate coincide on exactly
  `Re(s)>1`; this unchanged unit-mass equivalence must be proved.  For general
  masses, affiliated and bounded criteria remain the separate P7-4 statements
  in the amended protocol.
- Principal trace-log direction: only for `Re(s)>1`, use the branch fixed at
  the identity,

  ```text
  Log_0(I-K_s) = -sum_(r>=1)K_s^r/r,
  D_tau^pr(s) = exp(tau(Log_0(I-K_s))),
  Z(s) = D_tau^pr(s)^(-1).
  ```

  `D_tau^pr` is the precise name of this local complex scalar lift.  It is not
  the ordinary Hilbert Fredholm determinant, the Fuglede--Kadison determinant
  as a complex function, a “Breuer determinant,” or an unqualified global
  semifinite determinant.
- Historical deviation: the pre-amendment lock used the unqualified symbol
  `Det_tau(I-K_s)`.  That label is preserved here only as amendment history
  and is superseded by `D_tau^pr`; no prior global determinant entitlement is
  inferred.
- Mass provenance: `MODELING_CHOICE` until the closed-point counting transport
  obligation is proved independently of the Euler product.
- Control boundary: base-blind and arbitrary-clock-compilable; it may be an
  exact ledger determinant while failing to validate packet geometry.

## Controls

- `SINGLETON-BASE-LOGP`;
- `GENERIC-PROB-BASE-LOGP`;
- `COPIED-PACKET-DECOMP`;
- `MASS-PERTURBED-PACKET-DECOMP`;
- `ARBITRARY-CLOCK-K0-COMPILER`;
- `COMPOSITE-CLOCK-K0-COMPILER`;
- ordinary Hilbert-trace and zero-time controls.

## Frozen ownership and Route boundary

- A source/proxy bridge must transport set, topology/Borel structure, flow,
  clock, measure/disintegration, algebra, representation, trace domain, test
  class, return distribution, zero mode, analytic family, and determinant.
- A measurable flow equivalence alone is insufficient.
- The flat-return record and zero-mode determinant have different analytic
  owners and cannot exchange credits merely because they share a parent.
- The proxy restarts A0.  It does not inherit the parent's Route verdict.
- Right-half-plane exactness gives no A3 continuation, functional equation,
  Gamma factor, completed divisor, or Weil-compression credit.
- A4 and Route B are not invoked; Hilbert--Polya claims are forbidden.

## Unit-mass provenance gate

Before `M1` is promoted above `MODELING_CHOICE`, verify:

1. source packet/closed-point correspondence;
2. target-free closed-point counting measure;
3. transport to central trace weights of this same proxy algebra;
4. duplication and coordinate-change compatibility; and
5. source theorem versus new theorem versus modeling-choice status.

Target equality or Dirichlet-series uniqueness cannot satisfy this gate.

## Forbidden inputs

- Riemann zeros or zero ordinates;
- fitted clocks, masses, shifts, phases, cutoffs, or branches;
- `zeta(s)` or its coefficients as the definition of a trace or mass;
- imported Selberg/Ruelle weights;
- an unproved source/proxy identification;
- an undefined groupoid label or flow-generation claim.
