# P28 Stage-1 research brief — Semiclassical Tensor-Power Trace

## Exact research question

For the constant magnetic flow with minimal nonzero integral flux on the Bolza
surface, can a source-verified trace regime for the changing family
`H_N=Δ^{L^N}`, acting on `L²(Σ_B,L^N)` as `N→∞`, bind
primitive-orbit holonomy phases in a manner that distinguishes the arithmetic
metric from topology-, flux-, degree-, and regime-matched controls?

## Owner freeze

- Arithmetic substrate: the arithmetic Fuchsian realization of the Bolza
  surface; symmetry alone is not counted as a prime mechanism.
- Classical phase space: unit-speed magnetic energy shell in `T*Sigma_B`.
- Twisted form: `omega_0+pi^*(b Omega_g)` with `b=1/2`.
- Clock: physical unit-speed time.
- Primitive objects: primitive periodic magnetic trajectories.
- Phase owner: holonomy of the fixed degree-one connection, plus separately
  tracked Maslov data.
- Semiclassical operator family: `H_N=Δ^{L^N}` on
  `Hilbert_N=L²(Σ_B,L^N)`, with integer `N>=1` and `N→∞`.
- Operator-dependence boundary: both `H_N` and `Hilbert_N` change with `N`; the
  tensor-power limit is not a fixed-operator high-energy limit.
- Fixed-operator candidate: `Δ^L` on `L²(Σ_B,L)` is tracked separately
  and receives no tensor-family ownership by implication.
- Full-family trace binding: for all `N` and arbitrary degree-one flat twists,
  the energy-window theorem and periodic-orbit ownership remain `[OPEN]` /
  `NOT_ESTABLISHED`.  Round 3 separately proves the narrower source-compatible
  signed-field even-subsequence result.
- Data prohibition: no prime/zero list or target-tuned field strength.

## Derived Stage-1 normalization

Gauss--Bonnet gives `Area(Sigma_B)=4 pi` for genus 2 and curvature `-1`.
Therefore

```text
deg(L_b) = c1(L_b) = (1/(2 pi)) integral b Omega_g = 2b,
deg(L_0)=0,       deg(L_{+})=+1,       deg(L_{-})=-1,
L_{+}=L,          L_{-}=L^*.
```

For `b=+1/2`, the nonzero integral proves `F` is not exact.  Hence there is no
global potential `A`; a well-defined phase uses connection holonomy or an
action modulo `2 pi`.  Holonomy obeys the intrinsic repetition law
`Hol_L(gamma^r)=Hol_L(gamma)^r`, and the induced tensor-power connection obeys
`Hol_{L^N}(gamma)=Hol_L(gamma)^N`.

The three controls are therefore frozen as

```text
b=0       : L_0 of degree  0, chosen trivial with trivial connection;
b=+1/2    : L_+=L of degree +1, H_{N,+}=Δ^{L^N};
b=-1/2    : L_-=L^* of degree -1, H_{N,-}=Δ^{(L^*)^N}.
```

At tensor power `N`, the actual operator-bundle degrees are `0,+N,-N`.

`[PROVED]`: source-verified results put unit-speed `|b|<1` on the
geodesic-like/Anosov side
of the constant-curvature magnetic transition, while `|b|=1` is the horocycle
critical value.
The choice `b=1/2` simultaneously avoids the critical case and supplies the
minimal nonzero integral flux.

## Evidence-token contract and current claims

```text
EVIDENCE_TOKENS=PROVED|HEURISTIC|MODELING_CHOICE|OPEN
```

`[PROVED]`: Bolza arithmeticity, the twisted-symplectic magnetic-flow
framework, line-bundle quantization, and the existence of semiclassical
tensor-power trace-formula literature for magnetic Laplacians.

`[PROVED]`: `Area(Sigma_B)=4 pi`; `deg(L_b)=2b`; the three base-bundle degrees
are `0,+1,-1`; the negative-field bundle is `L^*`; and nonzero flux rules out a
global ordinary potential.

`[PROVED under the Round-3 subtype]`: on the source-compatible square-root
connection and even subsequence `N=2m`, the exact trace observable is
`Tr phi(sqrt(Delta^(L^N)+N^2/4)-(sqrt(5)/2)N)`, with an `O(1)` transformed
window.  It targets the already-frozen unit-speed shell.

`[PROVED under the Round-3 subtype]`: Kordyukov--Taimanov Theorem 3 binds
primitive magnetic conjugacy classes to the selected trace on the signed-field
even subsequence.  The full all-`N` family, arbitrary flat twists, zero-field
control, and fixed-operator candidate remain `[OPEN]` / `NOT_ESTABLISHED`.

`[HEURISTIC]`: the arithmetic substrate survives into individual magnetic
primitive orbits strongly enough to create a rational-prime Euler ledger.
Nothing in the background sources proves this.

The degree-one fixed operator remains a separate candidate with the exact
status tokens

```text
FIXED_OPERATOR_HIGH_ENERGY_TRACE=OPEN
FIXED_OPERATOR_MAGNETIC_ORBIT_OWNERSHIP=NOT_ESTABLISHED
```

## Falsification contract

1. Field reversal `b <-> -b` and the zero-field case, implemented with base
   bundles of degree `+1,-1,0`; the negative field uses the dual bundle.
2. Non-arithmetic genus-2 metric perturbation with fixed area, field,
   base-bundle degree, tensor power `N`, energy window, and trace regime.
3. Symmetry-resolved versus unsymmetrized orbit ledger.
4. Holonomy and Maslov phases retained; absolute-value amplitudes are not a
   substitute.
5. Every comparison uses the same `N`, spectral scaling, energy-window rule,
   trace regime, and orbit-selection rule.
6. A natural fixed self-adjoint candidate does not authorize Route B until
   A0--A3 and its own fixed-operator trace and orbit-ownership obligations are
   independently established.

## Historical Round-2 artifact contract

Round 2 was required first to prove a family-owner lemma fixing the
octagon/group, `L`, its dual,
induced connections, classical generators, every `Hilbert_N`, every `H_N`,
operator domains, tensor-power scaling, base and operator-bundle degrees, and
holonomy repetition.  The lemma must explicitly keep orbit ownership
`[OPEN]` with pipeline state `NOT_ESTABLISHED` until an exact trace theorem was
matched.  It then created
`results/bolza_semiclassical_tensor_trace_ledger.csv` for
`b=0,+1/2,-1/2` with the schema frozen in `results/README.md`.

## Round-2 execution — 2026-08-27

The family-owner lemma is now `[PROVED]` and recorded in
`round2_tensor_family_owner_lemma.md`. It closes degree, tensor-connection,
dual-bundle, antiunitary field-reversal, operator-domain, holonomy-repetition,
and family-versus-fixed ownership bookkeeping. It also proves that a
changing-bundle `N→∞` result cannot be transferred to the high-energy limit of
fixed `Δ^L` without a separate uniform two-parameter theorem.

The deterministic owner ledger contains 12 rows for
`b=0,+1/2,-1/2` at common `N=1,2,4,8`; 7/7 unit tests and a byte-identical
replay passed. Every row keeps the rescaled operator unassigned, the energy
window open, magnetic-orbit trace ownership `NOT_ESTABLISHED`, and fixed-owner
credit transfer false. The ledger is therefore a prerequisite contract, not
the planned primitive magnetic-orbit ledger. The formal Route-A tuple remains
unassigned.

## Round-4 execution — 2026-08-27

The first explicit Bolza primitive-owner seed ledger is now `[PROVED]` within
the frozen source-compatible signed-field even subtype.  The published regular
octagon side-pairing matrices give four generators of trace
`2(1+sqrt(2))`; their translation length equals the proved Bolza systole, so
they cannot be proper powers.  The polygon presentation's abelianization proves
that `f_j` and `f_j^-1` are not conjugate in `Gamma`.  The Round-4 counting
schema nevertheless treats `{f_j,f_j^-1}` as one inverse-paired primitive axis
owner and uses the sign of equation (19)'s `k` only to distinguish trace
branches; the nonconjugacy fact does not mint a second owner credit.

Kordyukov--Taimanov Theorem 3 and equation (19) then supply trace and physical
periods, total even-`N` action, Maslov index zero, ordered Poincare multipliers,
and the signed trace denominator for `k=+-1,+-2,+-3`.  There are four axis
owners, eight `|k|=1` branches, and 24 total signed trace branches per field;
both fields therefore produce 48 rows.  Field reversal maps `(b,k)` to
`(-b,-k)` on the same axis-owner ID.  Twelve tests and two byte-identical
builds passed.  The ledger contains no target data and assigns no arithmetic
labels.  It is explicitly incomplete outside the four side-pairing axes.

## Route mapping

```text
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1
A0_SCREEN=ARITHMETIC_SUBSTRATE_PRESENT_PRIME_LINK_UNPROVED
A1_PROGRESS=4_INVERSE_PAIRED_AXIS_OWNERS_PER_FIELD_48_SIGNED_K_BRANCH_ROWS
A1_COMPLETENESS=NOT_COMPLETE_BOLZA_PRIMITIVE_SPECTRUM
A4_ARCHITECTURE_NOTE=SEMICLASSICAL_TENSOR_POWER_FAMILY_NO_CREDIT_YET
ROUND2_OWNER_LEMMA=PROVED
ROUND2_OWNER_LEDGER=12_ROWS_REPLAY_PASS
FULL_ALL_N_ARBITRARY_TWIST_TRACE_REGIME=OPEN
FULL_ALL_N_ARBITRARY_TWIST_MAGNETIC_ORBIT_OWNERSHIP=NOT_ESTABLISHED
ROUND3_EVEN_SUBSEQUENCE_TRACE_REGIME=SOURCE_BOUND
ROUND3_EVEN_SUBSEQUENCE_MAGNETIC_ORBIT_OWNERSHIP=PROVED_UNDER_FROZEN_SUBTYPE
ROUND3_FULL_ALL_N_SEQUENCE=OPEN
ROUND4_BOLZA_GROUP_REPRESENTATION=SOURCE_LOCKED
ROUND4_INVERSE_PAIRED_AXIS_OWNERS_PER_FIELD=4
ROUND4_FIELD_AXIS_OWNER_PAIRS=8
ROUND4_SIGNED_TRACE_BRANCHES_PER_FIELD=24
ROUND4_ORIENTATION_OWNER_CREDIT=0
ROUND4_SIGNED_FIELD_LEDGER_ROWS=48
ROUND4_UNIT_TESTS=12_PASS
ROUND4_COMPLETE_PRIMITIVE_ENUMERATION=false
FIXED_OPERATOR_HIGH_ENERGY_TRACE=OPEN
FIXED_OPERATOR_MAGNETIC_ORBIT_OWNERSHIP=NOT_ESTABLISHED
FORMAL_A0_A4_TUPLE=UNASSIGNED
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
```

## Primary sources checked through 2026-08-27

- Katz, Katz, Schein, and Vishne, *Bolza Quaternion Order and Asymptotics of
  Systoles Along Congruence Subgroups*,
  https://doi.org/10.1080/10586458.2015.1073642 and
  https://arxiv.org/abs/1405.5454.  Supports the arithmetic Fuchsian/quaternion
  origin of the Bolza surface.
- Contreras, Macarini, and Paternain, *Periodic orbits for exact magnetic flows
  on surfaces*, https://doi.org/10.1155/S1073792804205050.  Supports the
  twisted-symplectic/Lorentz-force convention and the importance of exactness
  for a global ordinary magnetic action.
- Guillemin and Uribe, *Circular symmetry and the trace formula*,
  https://doi.org/10.1007/BF01393968.  Supports the foundational magnetic-flow
  and quantum trace setting.
- Kordyukov and Taimanov, *Trace formula for the magnetic Laplacian on a compact
  hyperbolic surface*, https://doi.org/10.1134/S1560354722040050 and
  https://arxiv.org/abs/2202.06055.  Supports constant fields, line-bundle
  quantization, the magnetic Laplacian trace, the critical regime, and
  holonomy/action phases.
- Ebbens, Iordanov, Teillaud, and Vegter, *Delaunay triangulations of
  generalized Bolza surfaces*, https://doi.org/10.20382/jocg.v13i1a5 and
  https://arxiv.org/abs/2103.05960, checked on 2026-08-27.  Equation (5)
  supplies the opposite-side-pairing matrices, equation (6) the polygon
  relator, and Theorem 2 the Bolza systole used by the Round-4 primitive-owner
  certificate.
