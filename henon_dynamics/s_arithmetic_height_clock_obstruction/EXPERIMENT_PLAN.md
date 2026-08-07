# Scoped Route-A assessment plan

## Claim-driven question

For one explicit compact quaternionic $S$-arithmetic quotient, can a pair of
projective $S$-units supply a canonical primitive real/$p$-adic clock, and
which parts of a rank-one Hilbert--Pólya route fail for that baseline?

The study is theorem-first. It does not fit zeros, primes, scales, or offsets,
and it does not attempt to construct a global higher-rank determinant.

## Frozen arithmetic object

```yaml
candidate_id: HCS-C16
family: compact quaternionic S-arithmetic dynamics
phase_space: Gamma quotient of H times the Bruhat-Tits tree T_13
quaternion_algebra: B=(-1,3)_Q
order: O=Z[1,i,j,ij]
group: Gamma=P(O[1/13]^times)
quadratic_torus: K=Q(sqrt(3))
generators:
  epsilon: 2+sqrt(3)
  pi: 4+sqrt(3)
clock:
  joint_signed: (m*A+n*C,n)
  real_length: abs(m*A+n*C)
  tree_length: abs(n)
  A: 2*log(2+sqrt(3))
  C: log((4+sqrt(3))/(4-sqrt(3)))
canonical_scalar: H=real_length+log(13)*tree_length
primitive_rule: gcd(m,n)=1 for nonzero pairs, modulo simultaneous sign
determinant_convention: one-flat class product used only as a falsification object
cutoff: finite numerical enumerations at the stated joint and height bounds
precision: exact Fraction algebra; high-precision Decimal real logs and boundary decisions
allowed_data: algebraic generators and identified mathematical sources
forbidden_data: prime tables, Riemann-zero tables, fitted spectral parameters
code_commit: 24553c8
```

Commit `24553c8` freezes the hardened producer, checker, tests, and generated
numerical artifacts. The complete paper/documentation package is bound
separately by the release manifest and Git release tag.

## Gates and falsifiers

| Gate | Pass condition | Immediate falsifier |
|---|---|---|
| Arithmetic host | $B$ is division globally and split at $(\infty,13)$ | wrong Hilbert symbol or failure of the lattice setup |
| Independent clock | signed clock matrix has rank two | zero determinant or proportional local coordinates |
| Primitive ledger | roots and repetitions are controlled by the centralizer | a root outside the declared projective centralizer |
| Rank-one interpretation | isolated primitive periodic orbits and a convergence region | periodic-flat families or factors failing to tend to one |
| Scalar repair | coefficient is intrinsic and the scalar clock is proper | fitted place weight or an infinite bounded-height sequence |
| Analytic determinant | a regulator-weighted global construction | only a formal one-flat class product |
| Self-adjoint baseline | the same clock and $T\log T$ counting | a bounded-Hecke $T^2$ Weyl law |
| Positioning | claims remain within directly checked prior-art and theorem scope | general novelty or no-go language |

## Proof obligations

1. Compute the Hilbert symbols at $2$, $3$, $13$, and infinity and invoke the
   standard $S$-arithmetic lattice theorem.
2. Identify the projective centralizer, including the projective-scalar step,
   and prove the primitive/repetition rule for nonzero pairs.
3. Derive the signed real/tree clock from local eigenvalue ratios and
   valuations.
4. Prove $C/A\notin\mathbb Q$ by valuations above $13$ and obtain a primitive
   near-wall sequence from continued fractions.
5. Deduce failure of the necessary local-factor condition for the real-only
   one-flat product.
6. Derive the Weil-height identity using normalized local absolute values and
   prove properness.
7. Prove the primitive-direction asymptotic by visible-lattice-point density.
8. Prove the bounded-Hecke Weyl statement by the min--max principle.

## Reproducible numerical checks

These checks illustrate and regression-test the proofs; they are not proofs of
the asymptotic or divergence statements.

1. Recompute exact rational norm, trace, discriminant, and matrix identities
   for frozen sample pairs.
2. Evaluate real logarithms with a high-precision `Decimal` policy.
3. Enumerate primitive near-wall records through denominator $1000$.
4. Enumerate primitive joint boxes through $X=Y=320$.
5. Enumerate the height ball through $H=640$.
6. Reimplement the algebra and enumeration logic in a checker that does not
   import the producer.
7. Record numerical boundary margins or interval decisions so finite counts
   are reproducible without labeling them exact.

## Structural controls

- **Simpler parent:** the $n=0$ subgroup has tree length zero and recovers the
  real unit direction.
- **Inert-place control:** at $p=5$, the torus is nonsplit because $3$ is a
  quadratic nonresidue; the projective $p$-adic action is compact.
- **Split-place control:** $3\equiv4^2\pmod{13}$ and
  $13=(4+\sqrt3)(4-\sqrt3)$, giving tree displacement one.
- **Independent arithmetic:** trace, norm, and discriminant checks avoid
  numerical $13$-adic diagonalization.
- **Orientation control:** reduce by $(m,n)\sim(-m,-n)$ only after retaining the
  signed joint direction.
- **Data control:** no zero list, prime list, randomized seed, or selected best
  run is used.

## Decision rule

Promotion to a positive rank-one Hilbert--Pólya route would require, together,
isolated primitive periodic objects, a correct global determinant with its
weights, a natural self-adjoint lift preserving the clock, and intrinsic
$T\log T$ counting. The tested baseline does not supply those ingredients.
The successful output is therefore a scoped Route-A assessment of this
explicit example, not a universal rejection of $S$-arithmetic approaches.
