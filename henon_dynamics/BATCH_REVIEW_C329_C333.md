# Batch review: HCS-C329--HCS-C333

## Outcome

This round delivers five independent theorem packages from baseline
`5ca65027918c0fce7ef9af82f3faf2e46ed6530c`.  Each package has its own
research question, analytic proof, producer-independent exact evidence,
strict Route-A evaluation, hostile audit, three retained manuscript rounds,
final PDF, and content-addressed release manifest.  The five results concern
different state spaces and proof mechanisms rather than successive sections
of one paper: a finite-field edge shift, a Diophantine interval map, a charged
magnetic flow and bundle Laplacian, a rate-independent moving-set inclusion,
and an iid stochastic matrix product.

## Independent theorem increments

- **C329:** for every odd prime power `q=1 mod 4`, the complete Paley strongly
  regular parameters and adjacency spectrum from finite-field characters; a
  convention-explicit Bass elimination; the entire Hashimoto spectrum and
  determinant; all power traces and oriented primitive-cycle counts; and the
  source Ihara zeta.  The proof closes extension-field representation, the
  `q=5` five-cycle, reversal, multiplicity, degree, and source Ramanujan
  boundaries.
- **C330:** one theorem separates terminating rational arithmetic from
  periodic irrational dynamics in the Romik map.  The possibly empty Barning
  word gives every primary primitive Pythagorean triple exactly once, while
  every nonpure word has one interior quadratic-irrational fixed point.  This
  yields `#Fix(T^n)=3^n-2`, every exact-period and oriented primitive count,
  source zeta `(1-z)^2/(1-3z)`, and exact determinant, orientation and
  instability data for every word, including both terminal and parabolic
  faces.
- **C331:** the conserved Poincare vector and every positive-energy magnetic
  circle on the monopole sphere, with exact least period and the stationary,
  uncharged and charge-reversal boundaries.  The same package then gives the
  full natural covariant-Laplacian spectrum
  `n(n+|q|+1)+|q|/2`, every multiplicity, heat trace, lowest level, Chern
  integrality, and conjugate-line-bundle symmetry.
- **C332:** the exact monotone-segment projection and one-period clamp for the
  scalar periodic Moreau play process.  One idempotent map gives the complete
  subthreshold-memory, threshold, and superthreshold-entrainment atlas,
  together with order, nonexpansion, admissible rate independence, exact
  variation splitting, and dissipation `2r(D-2r)_+`, including zero radius,
  constant input, plateaux, corners and equality.
- **C333:** the exact first moment and the complete second-moment transfer for
  relaxed randomized gossip on `K_N`.  Three explicit orthogonal invariant
  blocks give all projectors, scalar restrictions and multiplicities, the
  matrix-valued second moment, true statistical covariance, the sharp energy
  identity, finite-time tail bound and almost-sure consensus.  The theorem
  separately closes `N=1,2,3`, ordinary averaging, zero relaxation and the
  random-transposition endpoint.

The strict tuples, in order, are
`(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`,
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, and
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.  C329 and C330 are
`ROUTE_A_EXPLORATORY`; C331--C333 are `ROUTE_A_REJECTED`.  All five keep
Route B locked.

## Exact release accounting and hashes

Finite evidence units are package-specific regression receipts; none is used
as a finite extrapolation proof of an all-parameter theorem.

| ID | finite evidence | checker assertions | symbolic identities | hostile rejections | evidence bytes | final pages/fonts |
|---|---:|---:|---:|---:|---:|---:|
| C329 | 13 fields / 25,901 adjacency cells / 156 trace rows / 1,117 leaves | 13,048 | 692 | 70/70 | 38,668 | 3 / 7 |
| C330 | 9,840 word rows / 9,841 tree nodes / 12 count rows / 196,908 leaves | 290,403 | 2,833 | 72/72 | 6,025,765 | 2 / 7 |
| C331 | 39 classical rows / 357 spectral cells / 18 reversal rows / 3,167 leaves | 4,414 | 2,621 | 80/80 | 129,342 | 3 / 21 |
| C332 | 12 rational cases / two-period trajectories / 893 leaves | 792 | 4,788 | 69/69 | 26,117 | 3 / 21 |
| C333 | 56 spectral rows / 48 word rows / 4,242 words / 2,966 leaves | 1,392 | 350 | 140/140 | 82,824 | 4 / 26 |
| **total** | **205,051 audited leaves** | **310,049** | **11,284** | **431/431** | **6,302,716** | **15 / 82** |

| ID | evidence SHA-256 | round 0 PDF SHA-256 | round 1 PDF SHA-256 | round 2 / final PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|---|
| C329 | `1e59fd2b2dafa17e2ee00c3ef20d82b38539e85e708ac8e73c087485cd545c7a` | `7e371366ca0af6079530e53a7bed822f6b610080fab6feed4cceea061811ae20` | `196219a52d213118f9f1f3daae73b5828fb7e5b92b91705ff79fa7046eb2068c` | `286ba44628b8f27df7fd352f11d53514c6388f0bea2b3e4c0818b910c8bed502` | `f3e6f94a1cc4ddd3a296e630e825547d18cb230d9a972f444927aca6f326fb74` |
| C330 | `756fe52e75e29486eed3f6e2f75edf4ec5e0273c2e17caac14a93e2ce9bac2bb` | `a060ef72a42e7bf896128596f689470337caec33fc798d7e99eb891884bd3c3a` | `2185d3deee561d61e865c9fec4334eebfecf3a2617224cb31f077e393082ab2b` | `4c1e9b10af22eaff1401790668e797f32d41bd2151a95251d621473c75cf77e2` | `9a2138d851723010e74a977bed8e6ce9e6a05637704bca68b9b38044c997a7b0` |
| C331 | `170a072a4d406243e6e6e395a28e73cd9c388273a098f61c9a19fe2f11ed2326` | `72d5d3beff2bf88817b640022dc6b891d2802cd3859d7b1156e48aa031a48146` | `b279ee7b0e44126bdcea0a680f2c6577ae210833f474664a7251a44ce032fb38` | `679a8ba2b778610da80eb774aa47da8a4e047106afea735cf408b91ece16e3ac` | `3908f79ac68f315dc9b5bd66515a1f0eba620daba4fb88b20c53ee6c5b6e1eb3` |
| C332 | `26c9943fe605e91a07c206b6eb30cf2470e200653dc74f418c7a9efd77c029ef` | `fece7433cb66d238394f9353a0eed4bf2897028a673343b59cf8ad479d76f209` | `04a6d93e6f073c54c8f3a745e61145921467e2950e7fe560811d2e6d5c394976` | `0fd91d8d949aa6e6b86ceb9e109b9e4c5b982ba4fe4c435ef1a99dbd9c41fedf` | `cc4200d8478400e429bfd42b9da2e8f93d200dae0e0f833cc10e8cef63040f29` |
| C333 | `29a67f77766c1e40385dd4a1aa4719eba3ec5d2cd3f985a3e3ebdd4cf06baf39` | `b482073ac460c56c434987949079d93707720b39fa7e7d0840141943d1864503` | `fbdfdf7cf12c9f586dfa35657ef4247e42a98b5d15ce536da9b6acc810ac5b54` | `db444df6d1f778a1c1b821b68c79abe1321ec9a643a43b37024d4b095c04422c` | `076363b2ea493328e102cedc40cd7665ffbf4ad88e4b74464a6504db9a9fadc4` |

Every row has three distinct revision hashes and a final PDF identical to
Round 2.  The five manifests cover 135 payloads and 140 physical package
files.  All 15 final pages were visually inspected; all 82 final font rows
are embedded and subset.  Settled builds contain no layout, citation,
reference, destination, rerun, missing-character, or missing-glyph warning.
The final five no-write release programs pass from the same workspace state.

## Adversarial proof corrections and integrity

Review changed mathematical boundaries rather than merely polishing prose.
C329 made the finite-field additive character and trace explicit, inserted
the exact source Ramanujan inequality, and corrected the Bass bibliographic
metadata.  C330 made the empty Barning word own `(3,4,5)` and proved the
denominator and trace positivity needed by its chosen spectral-radius formula.
C331 replaced an incorrect same-initial-data charge-sign formulation by the
exact time-reversal statement: reversing time and initial velocity changes
`q` to `-q` and traverses the same geometric circle oppositely.  Its
author-swapped review also closed the previously implicit quantum bridge:
line-bundle classification and `H^1_dR(S^2)=0` give unitary gauge equivalence
to the homogeneous monopole connection, while the smooth energy form fixes
the Friedrichs realization and unique self-adjoint elliptic closure.  C333's
author-swapped review caught the zero-relaxation collision of all three scalar
values: the three spaces are invariant blocks for every parameter, become
full eigenspaces only for positive relaxation, and merge into the single
identity eigenspace at zero.  That repair was propagated through the theorem,
evidence schema, independent checker, mutation suite and rebuilt PDFs.

Every checker imports no producer code.  JSON parsing rejects duplicate keys
and nonfinite constants.  Evaluation parsing rejects aliases, anchors,
merges, non-string keys, implicit timestamps, unknown fields and type changes;
field-level semantic checks and raw/semantic hashes lock the authority,
source commit, date, tuple, gate statuses, theorem status, source owners,
scope flags and Route-B prohibition.  Hostile suites repair evidence hashes
before semantic attacks, every Python entry point rejects optimized execution,
and two isolated producer runs replay byte for byte in every package.

## Citation and scope integrity

The source audits assign the Paley graph to Paley and finite graph zeta to
Hashimoto and Bass; the Pythagorean map and its geodesic-section relation to
Romik; monopole charge, classical dynamics and harmonics to Dirac and
Wu--Yang; moving convex-set evolution to Moreau; and randomized gossip to
Boyd--Ghosh--Prabhakar--Shah.  No workspace noncollision or packaging result
is presented as literature priority.

All five evaluations set `route_b_invocation_allowed: false` under literal
scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  No target arithmetic local datum, Euler
factor, bad-prime datum, root number, automorphy object, target
divisor/counting law or functional equation, target zero match,
Hilbert--Polya operator, or Route-B input is asserted.  The two source zetas,
Pythagorean integrality, Chern quantization, hysteresis loop and covariance
spectrum retain only their explicitly evaluated source-side meanings.
