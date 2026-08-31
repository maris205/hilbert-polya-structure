# Route-A batch review C254--C258

Reviewed: 31 August 2026

Frozen baseline: `b89544f1f7b1043f4158dfdf9db77787b332f146`

Evaluator: `flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`

Common scope: `NO_BAD_EULER_OR_ROOT_NUMBER`

## Five independent advances

- **C254 (Monod chemostat):** exact total-nutrient relaxation closes the
  washout, critical, and survival chambers, including the transcritical
  spectrum, invariant-leaf implicit transient, critical algebraic rate, and
  proof that every recurrent state is an equilibrium.
- **C255 (Suslov rigid body):** the positive-energy reduction is solved on
  both heteroclinic components, while its endpoints reconstruct to clean
  two-dimensional families of periodic attitudes; the Poisson half-planes,
  singular invariant density, reversor, principal-axis face, and zero-energy
  face are all explicit.
- **C256 (KdV traveling waves):** the cubic root topology exhausts all bounded
  real traveling profiles, giving the cnoidal family, exact fundamental
  period and first two moments, soliton and harmonic degenerations, Galilean
  covariance, and the physical circle-return clock.
- **C257 (quadratic Newton dynamics):** one global Cayley coordinate closes
  both root basins, the Julia line, double-exponential errors, every periodic
  and preperiodic point, exact multipliers and cycle counts, source dynamical
  zeta, and the invariant Cauchy boundary law for every `z^2-a^2`, `a != 0`.
- **C258 (mixed congruential maps):** prime-power valuations and CRT prove the
  all-modulus Hull--Dobell criterion, count all full-period parameters, and
  close the fixed/primitive ledgers, source zeta, and canonical finite
  Koopman spectrum.  This is exploratory only: quotient prime powers are not
  rational-prime primitive orbits.

These are five different dynamical owners--a dissipative ecological ODE, a
nonholonomic rigid body, a nonlinear dispersive PDE, a complex rational map,
and a finite affine arithmetic system.  No result is an installment of
another paper.

## Executable and PDF audit

| ID | checker | SymPy | hostile mutations | PDF pages | embedded/subset fonts |
|---|---:|---:|---:|---:|---:|
| C254 | 244 | 14 | 28/28 | 2 | 20 |
| C255 | 244 | 18 | 30/30 | 2 | 18 |
| C256 | 602 | 245 | 49/49 | 3 | 21 |
| C257 | 1,317 | 88 | 41/41 | 2 | 24 |
| C258 | 300,210 | 69 | 37/37 | 2 | 21 |
| **total** | **302,617** | **434** | **185/185** | **11** | **104** |

For every package, the producer, independent checker, symbolic cross-check,
clean-process byte replay, repaired-hash semantic mutation suite, and release
manifest were rerun from the package root.  Every package contains exactly
27 hashed payloads plus its self-excluded manifest, hence 28 physical files
and 140 physical files across the round.

All three retained revision PDFs in each package have distinct hashes.  The
revision-2 PDF equals `paper/main.pdf`; two fresh LuaLaTeX passes in an empty
temporary directory at `SOURCE_DATE_EPOCH=1788048000` reproduce its bytes.
All 11 final pages were inspected, all 104 font records are embedded and
subset, and the final logs contain no layout, reference, citation, or package
warning.

## Content-addressed release ledger

| ID | evidence-file SHA-256 | final PDF SHA-256 | self-excluded manifest SHA-256 |
|---|---|---|---|
| C254 | `b61ec6508e3d2abdc6752a662742ea64245cd3edcdaf8e182153ffe83545bd83` | `b5cf728e479ac429e44f424a23fb8e3f7fd15ef461966fbce61e352b9eecb585` | `62e343066cde71700ff1943be113c05b84fb6c70f5aed658a97d86311eb72b99` |
| C255 | `84c2c312d4b8d4cd1d2386d0e9d5a4834f775b9dd55662592bd8feb354eebe71` | `e6a7a93d3528e4d685c5bbd5c79592a73268c2d027041ae80f8ffb5b820a3e81` | `456719d3f848c805695ee05507753e3de43deb1165134b60aa04fd48cab15087` |
| C256 | `0cdf43e788abc9c76374e2b2ceea00c0388420902c92fafb2861f89686860bb4` | `803a7637889627a99cd962a97ad1798719424a33b6e9d6bdbcd828cb5b5d186e` | `c3ae78ec188c819f996305ae7fd0e7a78b7a4b1361ddd3f3a66156afc9dac789` |
| C257 | `639c109ff487179b91503f79b2ac3066da0b7573b20a5a1acaa7c85b0c405def` | `10ee0b0fd7a4e2e8b8bda30e181ce6b667666d52601cd6e041d6b0b14938281f` | `0b0e25e5e786252f60de9d2c0eab52c62209ec55103c8e000a9a1ce332048648` |
| C258 | `16bd2f35138e18d748fa275cec2cf0296e96899756a465cd2952f18e643da3a9` | `533ae5616e925f9025a8db853da9dfd9ef84541245d61a811d4f996a1b9b9fc2` | `a59b727e8dd4481f938d0b71f8376c1228d73d8f0af2de5bda8a453d3c8682c0` |

## Route-A decision

| ID | strict tuple | overall |
|---|---|---|
| C254 | `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` | `ROUTE_A_REJECTED` |
| C255 | `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` |
| C256 | `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` |
| C257 | `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` | `ROUTE_A_REJECTED` |
| C258 | `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` | `ROUTE_A_EXPLORATORY` |

Coordinates are not mixed across candidates.  None of the five supplies a
target-weighted primitive census, target determinant, global target analytic
structure, or target zero/operator match, so Route B remains false for all
five.  No target prime or zero table, arithmetic local datum, Euler factor,
root number, automorphy statement, target divisor/counting law or functional
equation, Hilbert--Polya operator, or Route-B input is introduced.
