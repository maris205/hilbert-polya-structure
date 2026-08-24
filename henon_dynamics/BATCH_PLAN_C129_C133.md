# Route-A structural-gate batch plan: C129--C133

Status: **five complete paper packages; uniform release audit passed**.

Date: 2026-08-24

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

This round keeps Route A first and requires a different explicit structural
advance in every paper.  The five advances are phase sensitivity, nonlattice
clock separation, an all-odd quantization family, intrinsic nonlinear order
sensitivity, and a source-derived unitary scattering owner.  A finite replay
prefix is never used as the proof of an all-period statement.

## Frozen sequence and explicit progress

1. **C129 -- graph-directed phase holonomy.**  A fifth-root character of the
   integer translation lattice is added to C124's strongly separated affine
   Hénon IFS.  The same global Hardy owner remains trace class and, for every
   period,
   \[
   \operatorname{Tr}\mathcal L_\chi^n=
   \frac{\operatorname{Tr}W_\chi^n}
   {(1-8^{-n})(1-16^{-n})}.
   \]
   The corresponding entire Fredholm lattice and primitive-repetition product
   are exact.  Assignments `(-2,0,2)` and `(0,-2,2)` have the same untwisted
   determinant but different twisted determinants, so the new owner repairs
   C124's displayed branch-assignment blindness.  The character still records
   only a modulo-five phase coordinate and does not recover complete geometry.
2. **C130 -- irrational-roof suspension.**  The full binary shift with roof
   values `(1,sqrt(2))` has the exact bivariate owner
   \[
   M(u,v)=\begin{pmatrix}u&v\\u&v\end{pmatrix},\qquad
   \det(I-M)=1-u-v,
   \]
   together with an all-period primitive trace product.  Rational independence
   separates every distinct population-vector clock sector and rules out a
   nonzero imaginary period of the exponential determinant.  The primitive
   necklaces `000111` and `001011` prove that sector separation is not orbit
   injectivity; the rational-roof control `(1,2)` restores a time-two collision
   and vertical periodicity.
3. **C131 -- all-odd metaplectic family.**  For every odd integer `N>=3`, one
   frozen Weyl half-phase, Fourier sign, and chirp give an exact unitary lift of
   \(A=\left(\begin{smallmatrix}3&-1\\1&0\end{smallmatrix}\right)\).
   Unitarity, all `N^2` Egorov identities, clock preservation, and the same
   antiunitary reversor hold uniformly, including at composite levels.  The
   recurrence for `A^n` proves a growing no-action-alias window as `N` grows.
   This closes an all-odd natural-quantization gate, but supplies neither
   cross-level projective compatibility nor a semiclassical trace theorem.
4. **C132 -- nonlinear Möbius--Bergman trace owner.**  The two strict disk
   contractions `phi_a(z)=1/(a+z)`, `a in {3,6}`, have separated images and a
   trace-class composition sum on normalized Bergman space with the explicit
   bound `||L||_1<=89/16`.  Integer word matrices give the fixed point,
   multiplier, composition trace, all-period power traces, and a primitive
   Fredholm product.  The non-cyclic same-count words `33366` and `33636`
   have matrix traces `1344` and `1317`; thus nonlinear composition supplies
   intrinsic order sensitivity rather than an externally attached phase.
5. **C133 -- metric quantum-graph unitary scattering.**  A theta graph with
   lengths `(1,2,3)` and degree-three Kirchhoff scattering produces a unitary
   directed-bond family on `C^6`, the exact antiunitary reversal `J K`, a
   closed secular determinant, and an all-period signed primitive bond-orbit
   product.  This is the first working-series package to reach
   `A4_UNITARY_OR_SCATTERING_CANDIDATE`.  Replacing the Kirchhoff coefficient
   `2/3` by `1/2` destroys unitarity, and a direction-asymmetric reverse length
   produces eight nonzero reversal defects.  The secular divisor remains
   internal to this graph and is not compared with an external target.

## Uniform artifact contract

Every package contains a source audit, research question, theorem package,
experiment and paper plans, narrative report, internal two-round improvement
log, deterministic producer, independent checker, separate SymPy cross-check,
byte replay, hostile mutation suite, results/test/hostile reports, LaTeX
source, three preserved paper snapshots, final PDF, compile report, exact
evidence receipt, a strict Route-A verdict, and a content-addressed release
manifest.

Each manifest closes over exactly 27 payload files.  Including the
self-excluded manifest, every package contains 28 release files and no build
cache or LaTeX intermediate.  Two fresh fixed-date builds reproduce each
checked-in PDF.

## Paper and artifact ledger

| paper | dynamical subtype and closed gate | PDF pages | hostile mutations | evidence SHA-256 | manifest SHA-256 | PDF SHA-256 |
|---|---|---:|---:|---|---|---|
| C129 | graph-directed affine IFS; source phase-sensitivity gate | 2 | 35/35 | `191774477cdc635d0ab8f45efd17acc1ca9cac4d2a5f133d685ce61c22b395df` | `bb9c79995dca611cd402488d05d6bf69c571fa04c426bd10c56bcc3c89a25075` | `c3e4fc5b46116583dea7f1dff2c084e0ea348adff269b4484f3579d36e86ae35` |
| C130 | nonlattice symbolic suspension; clock-sector gate | 2 | 44/44 | `7f8f69f41003406bdd6d673520b4af145bb24e2f3f93034f0024644478f981ed` | `0de07a6a8f4c1b5618f7ee064b8bfeae4411e34668cd792ba78233772144929d` | `9ec16deb5b639f29e101c56dd1a74b9662292a875d29e2b8263d82920b3ef9b6` |
| C131 | odd finite metaplectic family; uniform natural-quantization gate | 3 | 30/30 | `676c4469cb52785efb46ed258b9d7207a8db3c0457d7ea8205e22bee382b3869` | `68a09331e851822e67d02ee404984a79e8a9df811cb78347c497df7a621c26bf` | `ba2e47cbc73f27d5340d350fed108604a6bf3a55d717ac3784f1fd7f050acf88` |
| C132 | nonlinear Möbius IFS; order-sensitive Bergman-owner gate | 3 | 37/37 | `4c70c2d50db012f649ff9bc0f716c3bfd6f29d65356486f422f4416cc8b195e4` | `c575137902cb7726f11010662dc293ec25b4c15f1ea27d41bd7c3f3f184a318e` | `8a090802c0bc97694d6173050d15dfacc67028a5f3dbd5734c548cfb30fd0f5e` |
| C133 | metric quantum graph; unitary/scattering-owner gate | 3 | 49/49 | `c09e4c83b76e9fa58b852421e837f6569da8df391fdc737677f32fb9192942c0` | `e9bf63c4844e41a14dbdd42f058e0e5e2dd72d190de77821fc7b7b387a3a351a` | `bc4c75b18083a98ad272b752dff06d95cf658326f4c12973ee0e29daef73f351` |

## Strict Route-A boundary

| paper | A1 | A2 | A3 | A4 |
|---|---|---|---|---|
| C129 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` |
| C130 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` |
| C131 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` |
| C132 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` |
| C133 | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_UNITARY_OR_SCATTERING_CANDIDATE` |

C131 and C133 close different A4 subgates for different candidates; their
coordinates are not combined.  No paper supplies a frozen target divisor,
target zero census, missing/extra-zero audit, target analytic completion, or
target counting-law comparison.  Strict A2 and A3 therefore remain `FAIL` in
all five rows.  The overall status is `ROUTE_A_EXPLORATORY`, the common scope
is `NO_BAD_EULER_OR_ROOT_NUMBER`, and `route_b_invocation_allowed` is `false`
for every candidate.

## Reproduction links

- [C129 paper](henon_graph_directed_phase_holonomy_route_a/paper/main.pdf)
- [C130 paper](henon_irrational_roof_suspension_route_a/paper/main.pdf)
- [C131 paper](henon_odd_level_metaplectic_family_route_a/paper/main.pdf)
- [C132 paper](henon_mobius_bergman_trace_route_a/paper/main.pdf)
- [C133 paper](henon_quantum_graph_unitary_scattering_route_a/paper/main.pdf)

The next internal gates are a phase owner that does not factor through one
finite residue character, a controlled cross-level semiclassical theorem, or
a source-derived infinite-dimensional scattering continuation.  A
target-facing A2/A3 comparison is a separate scope change and is not inferred
from this round.
