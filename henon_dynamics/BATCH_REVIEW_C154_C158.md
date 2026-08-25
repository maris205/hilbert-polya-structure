# Batch review: HCS-C154--HCS-C158

Date: 2026-08-25

System family: five separate Route-A dynamical refinements under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain all five papers as explicit source-structural
progress, continue Route A, and keep Route B unauthorized**.

## Completed paper outputs

1. **C154** replaces a freely attached symbolic periodic skeleton by one
   source-defined heteroclinic orbit closure.  A single configuration joins a
   period-three `234` past to a Thue--Morse future, and its closure is exactly
   the union of the Thue--Morse hull, the three phases of the periodic limit,
   and the wandering interface orbit.  The complete two-sided orbit is dense
   by construction, but standard forward topological transitivity fails
   because every interface point is an isolated singleton visited only once.
   The only primitive cycle has length three, so for every `n>=1`,

   ```text
   #Fix(sigma^n)=3 if 3 divides n, and 0 otherwise,
   zeta_AM(z)=1/(1-z^3).
   ```

2. **C155** proves full-period concentration on the periodic image of cyclic
   Rule 90 at every Mersenne circumference `L=2^r-1`.  For each proper clock
   `1<=j<L`, putting `d=gcd(j,L)` gives the exact fixed-kernel reduction and
   `dim Fix(a^j)<=2d<=2L/3`.  Consequently,

   ```text
   Pr(period<L) <= 2L*2^(-L/3),
   abs(L*C_L/2^(L-1)-1) <= 2L*2^(-L/3).
   ```

   A uniform periodic state therefore has full period with probability
   tending to one, and the cycle-equally-weighted mean length divided by `L`
   tends to one.  The neighboring power-of-two family remains nilpotent and
   prevents circumference-independent extrapolation.
3. **C156** gives all-iterate Fibonacci--Lucas factorizations and Smith types
   for the horizontal fixed-class module of the frozen Heisenberg
   automorphism.  The odd module is `(Z/L_n)^2`, while the even module is
   `Z/F_n x Z/(5F_n)`.  The representative-corrected quadratic cocycle has
   polarization

   ```text
   beta_n([m],[u])=v_1*u_2-u_1*v_2+m_1*u_2  (mod 1),
   ```

   and its value denominator divides `L_n` for odd `n` and `5F_n` for even
   `n`.  Orthogonal finite-group primary decomposition makes the zero-rotation
   count multiplicative across coprime primary summands.  “Primary” here is
   group-theoretic and not arithmetic-local or Euler factorization.
4. **C157** derives the genuine Dirichlet Abel half-wave trace of the unit
   square by two-dimensional Poisson summation:

   ```text
   W_D(s)=s/(2*pi) sum_(m in Z^2)(s^2+4*|m|^2)^(-3/2)
          -1/4-1/(exp(pi*s)-1),  Re(s)>0.
   ```

   The zero mode, dual axes, nonaxis primitive clean families, and boundary
   subtraction are separated.  Four sign lifts give the exact nonaxis
   coefficient `2s/pi`; all ordered positive primitive directions and
   repetitions are retained.  The Abel boundary contains `-3/2` branches at
   axis and clean-family lengths, simple boundary-subtraction poles at
   `t in 2Z`, and the Weyl zero mode.  For an integer max-norm cutoff
   `M>=|s|`, complex Taylor remainder and exact `8k` square-shell counting give
   the analytic accelerated-dual truncation bound

   ```text
   |s|^5/(2*pi*3^(5/2)*M^5).
   ```

   The deterministic high-precision centers are sentinels rather than
   interval-arithmetic outputs.
5. **C158** proves the exact full-cycle identity `C_k=B_k^k=A^(tensor k)` for
   the frozen open Walsh gate and hence the complete surviving secular
   factorization

   ```text
   det(I-z*C_k)=product_(j=0)^k
     (1-z*lambda_+^j*lambda_-^(k-j))^binom(k,j).
   ```

   Its degree is `2^k` and its generalized zero space has dimension
   `3^k-2^k`.  Under algebraic-multiplicity weighting, the normalized surviving
   log modulus is an affine fair-binomial variable with mean `-log(3)/4`,
   variance `sigma^2/k`, a Hoeffding bound, weak point-mass limit, and centered
   square-root-`k` Gaussian limit.  A moved-hole control preserves rank and
   mean but changes the variance coefficient, so modulus concentration is not
   a phase or self-adjoint spectral limit.

## Uniform release audit

All five deterministic producers, producer-independent standard-library
checkers, separate SymPy reconstructions, canonical byte replays, and hostile
mutation suites pass.  Their final receipts are:

- C154: 549 checker assertions, 357 symbolic checks, and 48/48 mutation
  rejections;
- C155: 2,291 checker assertions, 2,255 symbolic checks, and 54/54 mutation
  rejections;
- C156: 507,331 checker assertions, 1,842 symbolic checks, and 54/54 mutation
  rejections;
- C157: 1,022 checker assertions, 1,198 symbolic checks, and 104/104 mutation
  rejections;
- C158: 439 checker assertions, 62 symbolic checks, and 86/86 mutation
  rejections.

The batch totals are **511,632 checker assertions, 5,714 symbolic checks, and
346/346 rejected hostile cases**.  The hostile split is 341 repaired-hash
semantic or schema mutations plus five stale-hash controls.  Additional
read-only regression suites rejected all 33 C157 and all 23 C158 probes that
had been designed outside their package-local mutation lists.

Every release manifest has an exact 27/27 payload ledger with no missing,
extra, size-mismatched, or hash-mismatched file.  Each package therefore has
28 physical release files including its self-excluded manifest, for 140
physical files in the batch.  All five Route-A YAML records parse, contain the
required evaluator inputs, use only allowed evidence labels, and retain
`route_b_invocation_allowed=false`.  No Python cache, bytecode, LaTeX
auxiliary, log, recorder, or build-cache artifact remains.

Fresh isolated fixed-epoch double builds reproduce all five checked-in PDFs
byte for byte.  The ten rendered A4 pages use embedded/subset fonts and show
no clipping, collision, truncation, malformed formula, broken table, blank
content, or unreadably small text.  Final build logs contain no warning,
overfull/underfull box, missing-glyph, undefined-reference/citation, or
multiply-defined-label message.  Every paper contains independently phrased
English and Chinese abstracts, six or seven keywords in each language, and
data, ethics, contribution, conflict, funding, and AI-use declarations.

## Content-addressed release ledger

| paper | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|
| C154 | `051b5c486be9f68a87017f260ba983be02b4eb3383b60c5f3b30ee124bfd1dd1` | `8bc0c81c91c2979528d5df724564de829e316271454d82288f53006f9cea2405` | `7fa510063fda61792dea27bfd654f503e37c416a11ef30a63dd1a666d941f6ac` |
| C155 | `d1c63b082265ba2906be1f7a5aeb51b95224f0d1efaaed01dd9bb62986a8f399` | `3a48e621ebe71d3e57f07d4ee4143f8e98b3e62221132cc41e4cfc83fffdcd12` | `5791ccb94168b1ca4c136039bced93451e270f9aa98fddce532026402e920b1d` |
| C156 | `06791bf5734a48d0fe84d0e752e5d156172e637fe9a6a5e29792dfb3b2637b40` | `dbae62ad7e14a599501c7050216c03116978ef43fccb87f4a7e211b04e9965ea` | `99571673772e7ce63d020e13585f51ed6739f9817a47a2175b638d99dcacb431` |
| C157 | `de4f1a278c576fd4584e7a20ff5d35144f68b4369a4e93a5acdcf625f09af567` | `3b9c8f688532e933782b7d8227e5ee86e58fa6f74c1149196eaf22a2eaa33ed8` | `16c1e6fcac6459172b96468305df4599fdda89586f8de0c62f9757d8e587d1c6` |
| C158 | `286d8e813b96f9770e3fc42d922e87248288c337a032169fc2f6de462d262a45` | `dd20bab5f66b84e18995c35b1647f1bdea6ddb6d2771c02a812cc66b93689bd9` | `b1f728ae36147cc59cda5239c1961e7dc8d3aa86bddf3ccf3d4b1daa526effa5` |

## Internal cross-review and repair ledger

The reviews below were evidence-anchored internal theorem, scope, and release
audits.  They were not external peer review and do not claim reviewer or
error-process independence.

- C154 distinguished a dense complete `Z`-orbit from a dense forward orbit,
  supplied the explicit singleton-cylinder witness to failed forward
  transitivity, and rebalanced the two-page layout after the first release
  rendering placed nearly all mathematical content on page one.
- C155 made the `L=3` finite exception and the cycle-equally-weighted meaning
  of average length explicit.  Its two-page layout and complete Route-A input
  schema were repaired without changing the theorem or evidence.
- C156 corrected the polarization variable, preserved signed half-coefficients
  in the canonical quadratic serializer, added the all-iterate
  Fibonacci--Lucas parity bridge, and replaced an incomplete evaluator record
  and nonstandard evidence label by the complete allowed schema.
- C157 separated boundary-subtraction simple poles from the `-3/2` clean
  branches and Weyl term, then exposed the complex Taylor and square-shell tail
  proof.  Final review added `M>=|s|`, corrected the second sentinel display to
  `3.92e-12`, and distinguished rigorous analytic truncation bounds from
  non-interval high-precision centers.  Nested checker closure and hostile
  probes were expanded before release.
- C158 corrected an early moved-hole claim: the mean is unchanged while the
  variance changes.  The final checker was strengthened from selected leaf
  checks to exact nested key/value/list closure after repaired-hash probes
  exposed accepted claim-bearing mutations.  The Route-A schema and exact
  compile command were also completed.

## ARS Stage 2.5 failure-mode audit

This is the pre-manuscript integrity checkpoint applied after theorem and
evidence construction.

1. **Implementation bug passing self-review: CLEAR.**  Independent algebraic
   derivations and differently implemented finite paths exposed and repaired
   the C156 polarization/serializer and C157/C158 checker-closure defects.
2. **Hallucinated citation: CLEAR.**  No external citation or
   literature-derived numerical claim enters the five theorem paths; each
   source audit states the imported conventions directly.
3. **Hallucinated result: CLEAR.**  Every finite count, shell, polynomial,
   histogram, and probability receipt is canonically generated and separately
   reconstructed.  All-parameter conclusions have proofs.
4. **Shortcut reliance: CLEAR.**  Finite ledgers are labeled as sentinels.
   Dense-orbit decomposition, Mersenne concentration, primary-module
   factorization, Poisson regrouping, and tensor secular scaling are not
   inferred from their finite tables.
5. **Bug reframed as insight: CLEAR.**  The transitivity distinction,
   polarization repair, boundary-pole inventory, moved-hole mean correction,
   and checker gaps are recorded as repairs rather than discoveries.
6. **Methodology fabrication: CLEAR.**  Review is reported only as internal
   artifact-level review; no unavailable external reviewer, acceptance score,
   cross-model independence, or unperformed experiment is claimed.
7. **Early frame-lock: CLEAR.**  Five different source systems retain their
   negative controls and failed coordinates.  No positive source theorem is
   forced into a target-facing Route-A success.

## ARS Stage 4.5 failure-mode audit

This is the final artifact and manuscript checkpoint, separate from Stage 2.5.

1. **Implementation bug passing self-review: CLEAR.**  Final producers,
   checkers, SymPy paths, byte replays, 346 hostile cases, and the additional
   C157/C158 probe suites all pass on the released bytes.
2. **Hallucinated citation: CLEAR.**  Final PDFs contain no bibliography or
   unsupported attribution; source ownership and imported conventions remain
   explicit.
3. **Hallucinated result: CLEAR.**  Displayed finite values agree with the
   content-addressed evidence, while PDF, evidence, and manifest hashes are
   independently recomputed in the batch audit.
4. **Shortcut reliance: CLEAR.**  The manuscripts visibly separate theorem
   ranges from finite cutoffs, high-precision sentinels, and matched controls.
5. **Bug reframed as insight: CLEAR.**  All release-relevant corrections are
   preserved in the two-round improvement and batch repair ledgers.
6. **Methodology fabrication: CLEAR.**  Commands, source locks, test receipts,
   manifests, declarations, and deterministic build instructions are present;
   the papers disclose AI assistance without treating it as external review.
7. **Early frame-lock: CLEAR.**  Final tuples remain conservative, every
   package keeps its obstruction visible, and Route B remains disabled.

## Route-A assessment

The strict tuples are:

```text
C154 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C155 (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
C156 (A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
C157 (A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
C158 (A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)
```

All five are `ROUTE_A_EXPLORATORY`.  C156's Koopman hint, C157's natural
Dirichlet quantization, and C158's finite scattering parent belong to distinct
source systems and are not combined.  No package freezes or compares a target
zero census, target divisor, target functional equation, target counting law,
arithmetic local datum, Euler factor, root number, automorphy object, or
Hilbert--Polya operator.  Every package has
`route_b_invocation_allowed=false`.

## Next gate

The next five-paper Route-A round, if explicitly confirmed, should preserve
subtype diversity while attacking one remaining boundary per source: a
recurrent symbolic interaction rather than a one-pass interface; a sharper
Mersenne Rule-90 cycle-length distribution or subleading law; an all-iterate
evaluation of the Heisenberg finite quadratic sums; a clean-family amplitude
normalization with a proved regularization boundary; and a phase-resolved or
phase-obstruction theorem for the open-Walsh full-cycle limit.  Any
target-facing comparison remains a separately frozen protocol requiring
explicit authorization.
