# P27 Stage-1 paper research spine

Date: **2026-08-27**

    ARS_STAGE=1_RESEARCH
    DOCUMENT_ROLE=RESEARCH_SPINE_METHODOLOGY_SECTION_PLAN
    MANUSCRIPT_DRAFT=false
    ABSTRACT_DRAFT=false
    ARS_STAGE_2_STARTED=false
    FORMAL_ROUTE_A_TUPLE=UNASSIGNED
    A2_A4=NOT_EVALUATED
    ROUTE_B_EVALUATION=NOT_RUN
    ROUTE_B_INVOCATION_ALLOWED=false

This file organizes a possible paper. It is intentionally a Stage-1 plan and
contains no submission-ready abstract, introduction, or section prose.

## Search-bounded working title

*Finite-Level Closed Geodesics without Inverse-Limit Periodic Orbits: an
Explicit Congruence-Tower Ownership Audit*

The title is provisional. It avoids presenting inverse-limit aperiodicity as a
new general discovery.

## Research spine

### Frozen object

For n at least 1:

    Gamma_n = Gamma(3 n!) < PSL_2(Z)
    Y_n = Gamma_n backslash H
    M_infinity = inverse_limit_n T^1 Y_n

The bonding maps are tangent maps of finite regular coverings. The flow is the
coordinatewise unit-speed geodesic flow with one hyperbolic-arclength clock. In
current literature this is a noncompact hyperbolic McCord solenoidal surface of
finite type, not the compact universal hyperbolic solenoid.

### Central theorem already landed

    Per(M_infinity) = empty.

Proof spine:

1. A period T of one coherent inverse-limit point projects to a period at level
   one.
2. Relative to a primitive hyperbolic representative gamma, T equals
   m times ell(gamma) for one fixed positive integer m.
3. Normality of every Gamma(3 n!) removes the coordinate-dependent conjugator.
4. Closing at every level forces gamma^m into the intersection of all
   Gamma(3 n!).
5. In PSL_2(Z), choose an SL_2(Z) representative A. The congruences
   A congruent to epsilon_n I modulo 3 n! have a constant sign because
   3 n! does not divide 2.
6. Unbounded divisibility gives A equal to plus or minus I, hence the
   projective intersection is trivial.
7. A hyperbolic gamma cannot have gamma^m equal to the identity.

Evidence status: [PROVED]. Novelty status: the exact specialization was not
located verbatim in the frozen search, but the broad theorem mechanism is
structurally prior and no absolute novelty is claimed.

### Finite-owner firewall

For a frozen hyperbolic element gamma and level q, the projective reduction
order o_q(gamma) gives the finite-level closing period

    T_q = o_q(gamma) times ell(gamma).

The sequence of finite periods T_q does not define a period of M_infinity.
The latter requires one fixed T greater than zero and one coherent point that
returns at every coordinate. Therefore:

    FINITE_OWNER = congruence tower + frozen matrix + level convention
    LIMIT_OWNER = coordinatewise flow on M_infinity
    FINITE_TO_LIMIT_PERIOD_CREDIT = FORBIDDEN

This logical distinction is the methodological center of the proposed note.
It must be presented as claim discipline and owner identity, not as a
replacement for the prior solenoid literature.

### Reproducible finite diagnostic

Round 2 freezes three Gamma(3) hyperbolic matrices and eight levels:

    q = 3, 6, 18, 72, 360, 2160, 15120, 120960.

The resulting order sequences are:

    G3-A: 1, 3, 3, 6, 6, 36, 72, 288
    G3-B: 1, 1, 3, 12, 60, 360, 360, 2880
    G3-C: 1, 2, 6, 12, 12, 72, 72, 576

Required evidence report:

- two independent exact-integer algorithms agree in 24 of 24 rows;
- 21 of 21 nontrivial adjacent-level compatibility checks pass;
- the two reproduction runs are byte-identical for all four tracked artifacts;
- five of five unit tests pass;
- positive-word primitivity is exact, while full Gamma(3) conjugacy-class
  primitivity remains [OPEN] and is not needed for the order diagnostic.

Evidence status: [NUMERICALLY_CERTIFIED] for the finite diagnostic only.

## Contribution map after the closest-prior audit

| Component | Proposed role | Novelty discipline |
|---|---|---|
| General existence of aperiodic laminated geodesic flows | Prior-work context | Do not claim novelty. |
| Simply connected leaves in universal or punctured solenoids | Prior-work mechanism | Cite Martínez et al. and Penner--Šarić. |
| Noncompact finite-area regular-cover inverse limits | Object taxonomy | Cite Alcalde Cuesta et al.; use their terminology. |
| Exact Gamma(3 n!) residual proof | Explicit case proposition | Search-bounded specialization only; no “first” claim. |
| 3-by-8 order ledger | Reproducible case evidence | Project-specific numerical artifact, not theorem novelty. |
| Finite-owner firewall | Methodology and claim discipline | Present as an explicit audit framework, not a deep general theorem. |

## Methodology plan

### M1. Object and clock freeze

- Define every level, bonding map, phase space, and flow before using any orbit
  statistic.
- State that “periodic in the inverse limit” means one common positive real
  time for a coherent point.
- Distinguish the noncompact finite-type McCord object from the compact
  universal hyperbolic solenoid.

### M2. Exact theorem proof

- Give the homogeneous-space proof in PSL_2(R).
- Isolate normality, the group-chain intersection, and the PSL sign issue as
  separate lemmas.
- Include a leaf-topology interpretation only after the direct proof, because
  compact weak-solenoid theorems cannot silently replace the noncompact
  argument.

### M3. Finite quotient computation

- Freeze matrices and moduli before reporting results.
- Define projective equality A equivalent to minus A.
- Compute each order by sequential multiplication and finite-group-bound factor
  reduction.
- Report exact matrix and sign witnesses, order divisibility, length, and
  period scaling.
- Bind each table row to its finite owner.

### M4. Owner audit

- For every formula, state whether its primitive objects are finite-level
  closed geodesics, compatible inverse-limit orbits, or a normalized tower
  statistic.
- Reject any A1 or A2 inference that changes the owner.
- Explain why a projective limit of finite zeta functions, if later defined,
  would be owned by the tower and normalization rather than by
  Per(M_infinity).

### M5. Prior-work and novelty protocol

- Cite only primary sources for technical positioning.
- Reproduce the Round-3 search date, strings, include and exclude criteria, and
  source locators.
- Use “the frozen search did not locate” instead of “no prior work exists.”
- State directly that the general aperiodicity phenomenon and
  simply-connected-leaf mechanism are prior.

## Planned section architecture

### 1. Scope and bounded contribution

- Problem: incompatible ownership between finite closed geodesics and a total
  inverse-limit flow.
- Contribution: explicit factorial congruence case, reproducible ledger, and
  owner firewall.
- Non-contribution: no claim of the first aperiodic solenoidal geodesic flow.

### 2. Prior work and object taxonomy

- Laminated geodesic flow and direct aperiodic example.
- Universal and punctured solenoids with disk leaves.
- Hyperbolic solenoidal surfaces of finite type and McCord terminology.
- Group-chain kernel and leaf fundamental group, with compact-domain caveat.

### 3. The frozen factorial congruence tower

- Gamma(3 n!), Y_n, tangent-cover bonding maps, and M_infinity.
- One common hyperbolic-arclength clock.
- Precise definition of total-space periodicity.

### 4. Explicit no-period proposition

- Level-one primitive representative.
- Normality and the common exponent.
- PSL-sign residual-intersection lemma.
- Per(M_infinity) is empty.
- Comparison with the prior simply-connected-leaf mechanism.

### 5. Finite reduction-order experiment

- Frozen elements and levels.
- Two exact order algorithms.
- CSV schema and reproducibility checks.
- Order sequences and finite closing periods.

### 6. The finite-owner firewall

- Finite-level period versus one common inverse-limit time.
- Owner table for orbit, zeta, and normalized tower candidates.
- Why finite data cannot repair an empty total-space periodic set.

### 7. Limits and controls

- Exact-chain result is an explicit specialization.
- Full conjugacy-class primitivity remains open but irrelevant to the landed
  diagnostic.
- Cocompact residual-tower control remains to be executed.
- Any future normalized finite-level statistic needs a new owner and a new
  evaluation.

### 8. Conclusion

- State the mathematical obstruction and the methodological lesson.
- Preserve the Route-A boundary without assigning a formal tuple.
- List the next control rather than proposing Route B.

## Figures and tables allowed at Stage 2, if authorized later

1. A three-column owner diagram: finite level, inverse limit, normalized tower
   statistic.
2. The 24-row reduction-order table, or a condensed 3-by-8 order matrix with a
   machine-readable CSV pointer.
3. A short implication diagram:

       one common inverse-limit period
           implies one fixed group power lies in every Gamma_n
           implies membership in the residual intersection
           implies identity
           contradicts hyperbolicity.

No figure should imply that level-dependent periods converge to or constitute
a periodic orbit of M_infinity.

## Claims forbidden in a later draft

- “This is the first aperiodic hyperbolic solenoidal geodesic flow.”
- “No prior work studies this phenomenon.”
- “The finite-level closed geodesics are periodic orbits of M_infinity.”
- “The finite-level zeta functions provide an A2 determinant for the limit
  flow.”
- “The exact-chain negative search proves novelty.”
- Any formal A0--A4 tuple or Route-B invocation not produced by its authorized
  evaluator.

## Stage-1 exit criteria before any Stage-2 draft

1. Complete the cocompact residual-tower control.
2. Decide whether there is a genuinely broader proposition beyond the known
   simply-connected-leaf mechanism.
3. Perform a human verification of S1--S4 and their citation chains.
4. Make a written go or no-go decision on the narrow paper class.
5. If the decision is go, freeze the exact contribution statement and target
   article type before drafting prose.

Until all five conditions are handled, this file remains a Stage-1 research
plan and the manuscript status remains NOT STARTED.
