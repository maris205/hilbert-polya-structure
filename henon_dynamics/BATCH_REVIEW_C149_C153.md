# Batch review: HCS-C149--HCS-C153

Date: 2026-08-25

System family: five separate Route-A dynamical refinements under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain C150--C153 as explicit source-structural progress,
retain C149 as a proved source rejection, continue Route A, and keep Route B
unauthorized**.

## Completed paper outputs

1. **C149** forms the compact disjoint union of the aperiodic minimal
   Thue--Morse subshift and tagged cycles of lengths `1,2,3,5`.  A
   self-contained aperiodicity proof shows that the subshift contributes no
   periodic point.  Consequently, for every `n>=1`,

   ```text
   #Fix(sigma^n)=sum_(ell in {1,2,3,5}, ell|n) ell,
   zeta_AM(z)=1/((1-z)(1-z^2)(1-z^3)(1-z^5)).
   ```

   There is exactly one primitive cycle at each declared length and no other
   primitive cycle.  Every nonempty finite disjoint periodic attachment is a
   proper closed invariant subset, so it necessarily destroys minimality.
2. **C150** proves the Mersenne-size Rule-90 theorem.  For
   `L=2^r-1`, the multiplier `a=x+x^(-1)` satisfies `a^(L+1)=a`, has
   one-dimensional kernel and image dimension `L-1`, and permutes its image
   with order dividing `L`.  Every state therefore reaches the periodic image
   after one tick, exactly half of all states are periodic, and every temporal
   period divides `L`.  Polynomial gcds and Mobius inversion recover every
   fixed, exact-period, and geometric-cycle count.  The matched
   power-of-two family is nilpotent and has only the zero periodic state.
3. **C151** resolves the central fibre over every horizontal fixed class of
   the frozen Heisenberg automorphism.  If `m=(A^n-I)v`, the exact rotation is

   ```text
   rho_n(v)=sum_(j=0)^(n-1) q(A^j v)-m_1 v_2  (mod 1).
   ```

   This quantity is representative-independent, and the class lifts to a
   clean fixed circle exactly when `rho_n(v)=0`.  With
   `D=|det(A^n-I)|` and `Q=2D^2`, a finite central cyclic root-of-unity
   projector gives an all-iterate exact zero test.  The independently checked
   component counts through iterate twelve are
   `1,1,4,1,21,4,57,1,148,105,397,144`; the last values reject the tempting
   early Lucas/parity/mod-three extrapolation.  The rotation is generally a
   quadratic map, not a horizontal quotient homomorphism.
4. **C152** defines the ordered-positive primitive billiard-direction heat
   transform

   ```text
   H_prim(t)=sum_(m,n>=1, gcd(m,n)=1) exp(-4t(m^2+n^2)).
   ```

   Absolute convergence justifies its exact Mobius--theta decomposition
   `sum_d mu(d) theta_+(4td^2)^2`, with length collisions retained at their
   ordered-positive multiplicity.  Primitive quarter-disk counting gives
   `N(R)=3R^2/(2*pi)+O(R log R)` and hence
   `H_prim(t)=3/(8*pi*t)+O(t^(-1/2)log(1/t))`.  This is a source-derived heat
   transform, not a clean wave trace, isolated-orbit determinant, or
   Dirichlet spectral heat trace.
5. **C153** proves for the growing open Walsh gate that

   ```text
   rank(B_k^n)=2^min(n,k) 3^(k-min(n,k))
   ```

   for every `k>=1,n>=0`.  At `n=floor(alpha*k)`, the signed log-survival
   rate is `min(alpha,1)log(2/3)` and the positive escape exponent is
   `min(alpha,1)log(3/2)`, including the `alpha=0` boundary.  At fixed period
   `n`, the equality-merged trace cluster is
   `{t_(n/d)^d:d|n}`, and every divisor class occurs infinitely often.
   Dimension-normalized traces vanish.  The period-two odd/even witness
   `t_2-t_1^2=-2q_0!=0` proves that the unnormalized trace need not converge.

## Uniform release audit

All five deterministic producers, producer-independent checkers, separate
SymPy reconstructions, canonical byte replays, and hostile mutation suites
pass.  Their receipts are:

- C149: 395 checker assertions, 277 symbolic checks, and 42/42 mutation
  rejections;
- C150: 153 checker assertions, 276 symbolic checks, and 45/45 mutation
  rejections;
- C151: 168,146 checker assertions, 72 symbolic checks, and 37/37 mutation
  rejections;
- C152: 20,047 checker assertions, 503 symbolic checks, and 39/39 mutation
  rejections;
- C153: 6,193 checker assertions, 213 symbolic checks, and 53/53 mutation
  rejections.

The batch totals are 194,934 checker assertions, 1,341 symbolic checks, and
216/216 rejected hostile cases.  The mutation split is 211 repaired-hash
semantic mutations plus five stale-hash controls.

Every release manifest has an exact 27/27 payload ledger with no missing,
extra, size-mismatched, or hash-mismatched file.  Each package therefore has
28 physical release files including its self-excluded manifest, for 140
physical files in the batch.  No Python cache, bytecode, or LaTeX
auxiliary/log/recorder artifact remains.

Fresh isolated fixed-epoch double builds reproduce all five checked-in PDFs
byte for byte.  The six rendered pages use embedded/subset fonts and show no
clipping, collision, truncation, malformed formula, broken table, blank
content, or unreadably small text.  Final build logs contain no warning,
overfull/underfull box, undefined reference or citation, or multiply-defined
label.

## Content-addressed release ledger

| paper | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|
| C149 | `774babf27a162728f63f4d1a76877e8d7c412c9f1c62286e3463868875084dfc` | `af25f7ee7a2b381a538300c6d68c589b524fb776382824ee74770514f06e3b0f` | `50da268cff1adbdcfba03c8261f3e042f0fa4d2a29f7c328ee6ec7ad1a85b7a6` |
| C150 | `8ea85c5644c028c23c0dc004d4674e98c760c86554c8ce124fd18d88ee0bee06` | `cfe7edcc402d84f3217433e3643b04986d99ab1196373880aea34c4204886959` | `1deac52357dfcd0bde0cd8ba639e4d7e601e2a0a0443dd0ca05371a18ee3f0cd` |
| C151 | `5fe26d210e6c848789ee769f9f0fbaa0ba67baef06cb93cb3d2f2d403ef18419` | `e2aed63c9da2e5af6fc5be41f8b618db19289c7355b2b269542cfef5ff25802e` | `df444a4a29c3ff3d79d5c26d59a7ddbc77b661f5bfcb9e18253f6c86d6ff04e5` |
| C152 | `9592c29b9a4449b7616721fd48776e968e308aad3b0d824c34047b3baeea6eb9` | `d028843b5606cec8609f37c616584731637f7bff42df0bb06c4ae6fe48cd2b68` | `0b9afd2cc5edec5affb8882f3052dd68a1b1c54687065e102230a72f6f4ae67b` |
| C153 | `c413ef3a0e872c378f319ab66b79aab4f9139e03b704fda0ef8206247b64249e` | `3cb61a11554f1b54dd7d951c5722791f5881f792655b4989878409884c82508c` | `d2b0fc7aa61ab97d23efd739b27febd9ed56d06c1a509c1ed7202d55e93f5235` |

## Internal cross-review and repair ledger

The reviews were evidence-anchored internal theorem/scope audits, not
external peer review.  No acceptance, novelty, model-independence, or
reviewer-independence score is claimed.  They produced the following
release-relevant repairs:

- C149 replaced a compressed aperiodicity bridge by an explicit aligned-block
  argument that quantifies the needed language-window length.  It keeps the
  freely tagged cycles outside the Thue--Morse component and reports lost
  minimality as the conclusion.
- C150 made the all-`r` multiplier identity, one-dimensional kernel, image
  permutation, and power-of-two nilpotence proofs explicit; finite tables are
  only sentinels for these theorems.
- C151 rejected the early component-count extrapolation using the `n=10` and
  `n=12` values, proved representative invariance, and replaced ambiguous
  “character projector” wording by “central cyclic root-of-unity projector.”
  An explicit `n=2` witness confirms that `rho_n` is not generally a
  horizontal homomorphism.
- C152 fixed the counting variable as the Euclidean radius, preserved ordered
  collision multiplicity, and separated the proved heat transform from both
  clean-family amplitudes and a Dirichlet operator trace.
- C153 promoted the moved-hole check to a proof that every positive one-site
  power has rank two, distinguished the power-sum initial value `t_0=2` from
  `Tr(A^0)=3`, and repaired the divisor-power formula and display numbering.

## Academic failure-mode audit

This section is the batch-level ARS seven-mode checklist.  It is distinct
from the package-local hostile-audit axes, which test evidence tampering and
scope drift rather than claiming to reproduce this checklist.

1. **Mode 1 -- implementation bug passing self-review: CLEAR.**  Every
   producer is checked by a separately implemented standard-library path, a
   distinct SymPy reconstruction, byte replay, and repaired-hash semantic
   mutations.
2. **Mode 2 -- hallucinated citation: CLEAR.**  No external citation,
   target table, or literature-derived numerical claim enters the five
   packages.  Imported mathematical conventions are declared in each source
   audit, so there is no bibliographic attribution to invent.
3. **Mode 3 -- hallucinated result: CLEAR.**  Every displayed finite count,
   rank, histogram, hash, and witness is generated by canonical evidence and
   independently reconstructed; all-parameter statements have explicit
   proofs rather than ledger extrapolations.
4. **Mode 4 -- shortcut reliance: CLEAR.**  Finite tables are labeled as
   sentinels only.  The release proves the Thue--Morse separation, Rule-90
   image theorem, Heisenberg representative invariance, billiard asymptotic,
   and Walsh tensor-rank law for their full declared parameter ranges.
5. **Mode 5 -- bug reframed as insight: CLEAR.**  False or incomplete steps
   were repaired before release: the C149 alignment bridge, the C151 guessed
   count and terminology, the C152 trace-ownership boundary, and the C153
   moved-hole power-rank and trace notation are recorded as repairs, not
   promoted as discoveries.
6. **Mode 6 -- methodology fabrication: CLEAR.**  Review is described only
   as evidence-anchored internal review; no unavailable external reviewer,
   cross-model independence, acceptance score, unperformed experiment, or
   unavailable source is claimed.  Commands, ledgers, snapshots, and
   manifests are present.
7. **Mode 7 -- early frame-lock: CLEAR.**  Five distinct subtypes and strict
   provisional tuples were frozen before the computations.  Destroyed
   minimality, the neighboring-size obstruction, the rejected component
   pattern, heat/trace nonidentity, and trace oscillation remain visible
   negative results instead of being forced into the initial positive frame.

## Route-A assessment

The strict tuples are:

```text
C149 (A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
C150 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C151 (A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
C152 (A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
C153 (A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)
```

C149 is `ROUTE_A_REJECTED`; C150--C153 are `ROUTE_A_EXPLORATORY`.
C151's formal Koopman/fibre hint, C152's natural Dirichlet quantization, and
C153's finite unitary/scattering parent belong to different source systems
and are not combined.  No package has a frozen target divisor, target zero
census, target functional equation, target counting-law comparison,
arithmetic local factor, Euler factor, root number, automorphy object, or
Hilbert--Polya operator.  Every package has
`route_b_invocation_allowed=false`.

## Next gate

The next five-paper Route-A round should continue subtype diversity while
turning one exact residual boundary into a new theorem per paper: a
source-derived nonminimal symbolic interaction rather than a free periodic
attachment; normalized growing-`r` Rule-90 cycle statistics with a matched
size-family control; a proved all-iterate evaluation or sharp structure
theorem for the finite Heisenberg root-of-unity sum; a genuinely derived
clean-family amplitude/regularization or a proof of its obstruction; and a
moving-period or full-secular open-Walsh limit only under a controlled
normalization.  Any target-facing comparison remains a separately frozen
protocol requiring explicit authorization.
