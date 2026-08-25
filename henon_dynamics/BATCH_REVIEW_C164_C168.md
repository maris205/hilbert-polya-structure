# Batch review: HCS-C164--HCS-C168

Date: 2026-08-25

System family: five separate Route-A dynamical advances under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain all five papers as explicit theorem progress,
continue Route A, and keep Route B unauthorized**.

## Completed paper outputs

1. **C164** gives the recurrent Thue--Morse S-gap shift a source-native
   first-return operator owner.  On the branch Hilbert space, the fixed gauge
   produces a trace-norm holomorphic rank-one family `K_z` for every
   `|z|<1`, with

   ```text
   Tr(K_z^m)=F(z)^m,
   det_F(I-([z] direct_sum K_z))
     =(1-z)(1-F(z))=zeta_X(z)^(-1).
   ```

   This is separated from the uninduced adjacency
   `A delta_n=delta_(n+1)+t_n delta_0`.  On every positive diagonal weighted
   `l2` realization where that adjacency is bounded, it is noncompact and
   belongs to no finite Schatten class.  Trace continuity transfers the C159
   natural-boundary obstruction: the induced trace-class family cannot
   continue meromorphically through any unit-circle arc.  The paper also
   separates this branch-resolved owner from a tautological scalar
   determinant.
2. **C165** pivots away from a fourth consecutive Rule-90 refinement to a
   reversible two-layer Margolus cellular automaton.  A complete tick moves
   even sites by `+2` and odd sites by `-2`, and the reversed-odd pairing
   conjugates the configuration dynamics to cyclic rotation on four-letter
   words of length `m`.  Therefore, for every `m,n>=1`,

   ```text
   #Fix(T^n)=4^gcd(m,n),
   P_m(d)=sum_(e|d) mu(d/e)4^e,
   C_m(d)=P_m(d)/d,
   zeta_T(z)=product_(d|m)(1-z^d)^(-C_m(d)).
   ```

   Proper periods have mass at most `m/2^m`.  Reflection is a reversor, and
   the finite same-clock Koopman determinant is the inverse source zeta.
   The operator boundary is exact: the permutation unitary is self-adjoint at
   `m=1,2` and non-self-adjoint for every `m>=3`.  The conjugate necklace
   system is not described as chaotic or interacting.
3. **C166** changes subtype again to the `d`-dimensional dyadic Pascal skew
   tower over `q=2^r`.  In the truncated ring, one tick is multiplication by
   `1+t`.  With `a=floor(log_2 d)` and `M=2^(r+a)`, exact binomial valuations
   prove

   ```text
   Fix(T^n)=(Z/qZ)^d iff M divides n,
   Fix(T^n)=empty otherwise.
   ```

   Thus every state has exact period `M`, there are `q^d/M` primitive
   cycles, and

   ```text
   zeta_T(z)=(1-z^M)^(-q^d/M),
   det(I-zU_T)=(1-z^M)^(q^d/M).
   ```

   Substitution `t -> -t/(1+t)` is an involutive reversor and gives the
   same-clock antiunitary.  The valuation statement explicitly treats
   `1<=k<=n`; coefficients with `k>n` vanish, so no implicit `v_2(0)`
   convention remains.  The proposed two-dimensional shear is recorded as
   the already absorbed `d=2` case rather than a separate paper.
4. **C167** advances the square-billiard branch coefficient to every
   rectangle `Q_alpha=(0,1)x(0,alpha)`.  The exact anisotropic Poisson formula
   gives, at every nonzero dual shell,

   ```text
   lim_(epsilon->0+) epsilon^(3/2)
     W_alpha(epsilon-2i*sqrt(E))
   =alpha*exp(i*pi/4)*R_alpha(E)/(8*pi*E^(1/4)).
   ```

   The proof controls the complete trace, the infinite nonmatching tail, and
   coincident simple boundary poles.  At `beta=4,E=4`, two axis pairs and both
   boundary clocks coincide, yet the normalized boundary contribution is
   still lower order.  With `beta=alpha^2`, every non-sign collision parameter
   is positive rational, every pairwise crossing is transverse, irrational
   `beta` has sign-only multiplicity, and rational `beta=u/v` shells are
   exactly the fibres `v*m^2+u*n^2=N`.  No higher-multiplicity transverse-
   stratum claim, uniform irrational gap, or universal divisor formula is
   made.
5. **C168** rejects a freely selected three-phase tensor model and uses the
   natural four-symbol one-hole Walsh gate

   ```text
   A=F_4^* diag(1,0,1,1),
   chi_A(x)=x(x-1)(x^2+i*x/2-1/2).
   ```

   Its nonzero roots are `1,(+/-sqrt(7)-i)/4`.  The normalized phase ratio
   satisfies `r+r^(-1)=-3/2`, so it is nontorsion.  For the full-cycle tensor
   `C_k=A^(tensor k)`, the nonzero secular degree is `3^k`, the generalized
   zero space has dimension `4^k-3^k`, and

   ```text
   mu_hat_k(m)=((1+u_+^m+u_-^m)/3)^k.
   ```

   Every fixed nonzero Fourier mode decays, yielding weak Haar phase
   convergence.  The centered log modulus converges to
   `Normal(0,(log 2)^2/18)`, and the exact mixed transform gives the joint
   Gaussian--Haar product.  The hole-zero model is a torsion four-group
   control with `TV<=(3/2)3^(-k)`.  No all-mode uniform gap, finite-`k` total-
   variation convergence to continuous Haar, distinctness of all phase
   labels, or fixed-hole self-adjoint limit is claimed.

## Uniform release audit

All five deterministic producers, producer-independent checkers, separate
SymPy reconstructions, canonical byte replays, and hostile mutation suites
pass on the released claim surfaces:

- C164: 668 checker assertions, 197 symbolic checks, and 62/62 hostile
  rejections;
- C165: 723 checker assertions, 481 symbolic checks, and 58/58 hostile
  rejections;
- C166: 53,348 checker assertions, 7,519 symbolic checks, and 36/36 hostile
  rejections;
- C167: 1,362 checker assertions, 28,585 symbolic checks, and 31/31 hostile
  rejections;
- C168: 682 checker assertions, 386 symbolic checks, and 113/113 hostile
  rejections.

The batch totals are **56,783 checker assertions, 37,168 symbolic checks,
and 300/300 rejected hostile cases**.  The hostile split is 295 repaired-hash
semantic/schema mutations plus five stale-hash controls.  These are internal
artifact checks, not external peer review or a claim of an independent error
process.

Every release manifest closes an exact 27/27 payload ledger.  Each package
therefore has 28 physical release files including its self-excluded manifest,
for 140 physical files and 135 manifested payloads in the batch.  All five
Route-A YAML records parse, contain the required evaluator inputs, use only
allowed evidence labels, and retain `route_b_invocation_allowed=false`.
Target, arithmetic-local, Euler-factor, root-number, automorphy,
Hilbert--Polya, and Route-B flags remain disabled.  No Python cache, bytecode,
LaTeX auxiliary, log, recorder, or build-cache artifact remains.

Ten fresh fixed-epoch empty-directory builds reproduce the five released PDFs
byte for byte.  The ten rendered A4 pages use embedded fonts and have no
clipping, collision, truncation, blank page, malformed formula, missing glyph,
or unreadable text.  Fresh final logs contain no warning, overfull/underfull
box, undefined reference/citation, or multiply defined label.  Every paper
contains independently phrased English and Chinese abstracts, six or seven
keywords in each language, and data/code, ethics, contribution, conflict,
funding, and AI-use declarations.  The round-zero, round-one, and round-two
PDFs are content-distinct in every package, and each `main.pdf` is
byte-identical to its round-two snapshot.

## Content-addressed release ledger

| paper | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|
| C164 | `8ff039990ef2b4ba320bcc36c317c475915e2f5d5d52ea43f57060ef33b97629` | `f4fa297a1f63d43ba0676096e6c3418a492dbeafcd93baff9aab5befbfa11223` | `354bf8a01d103ff3cb1193fd070c7afb6a2b10ba3e536c44530ac9095c9dccc5` |
| C165 | `70a7fc44fb48f5cd2b471e21df4e406c8f4cc928c928165f05ef71a3dcbef763` | `8902e83f58d04aee5f754e97c8c142db113f8c591ab5a23c868b9396648f3be3` | `5d5b11b9f7d8d8d8fb10522beb3e981db64056604668b0599452c0f151e23cbc` |
| C166 | `3272e01ce32f4d58f609ebfc76dba60584636bc8225970c01e6659af2ae4aaca` | `1f1d7620b8e734f6bf3a866f3357e5d77aee4991c35c4144597548894627d8e1` | `98164f2d2036ea7b66089d8fe6012276a7dc2499673fbd8769366481e27b269b` |
| C167 | `bc7eb8399f780387c9d4cc236a0fcc852e81e1a11159693cdb0f76fc3a7f52f9` | `03ce3fe4f1827d9f781dcd7a07575458d0f26f7c76cf0073cb25d9a9a787ba08` | `53f7114a88cf31a0f8f9b239aeaade7297fa1219a5b7add2ac55517dfe300faa` |
| C168 | `5a39872527a3cc43b4a54be151d8ce16f2c8ed54874dfa29b26fce16b13cd477` | `68dcb55469222603236d6d496af5fc691fca882277b6bea20d5a89b3db39c679` | `0cb2c393c1980f8a05a89fe3c7ca5931014a8963ea60aa0c256a580be5b627d1` |

## Internal cross-review and repair ledger

The reviews below were evidence-anchored internal theorem, scope, and release
audits.  They were not external peer review and do not claim reviewer or
error-process independence.

- C164 proved the uninduced all-weight noncompactness obstruction before
  assigning analytic ownership to the induced return family.  A release audit
  found that an earlier PDF depended on an existing auxiliary directory; the
  checked PDF was replaced by the byte sequence reproduced from two empty
  fixed-epoch builds.  The out-of-schema evidence label
  `PROVED_OBSTRUCTION` was also replaced by the allowed `PROVED` label.
- C165 records the Rule-90 pivot rather than treating lineage exhaustion as a
  theorem.  Hostile review corrected a blanket non-self-adjoint sentence by
  exposing the exact `m=1,2` self-adjoint boundaries and the `m>=3` period-
  cycle witness.  Producer, checker, evidence, manuscript, YAML, PDF, and
  manifest were rebuilt together.
- C166 records the collapsed two-dimensional candidate as the `d=2` member
  of the stronger tower theorem.  Hostile proof review restricted the
  displayed binomial valuation to `1<=k<=n` and separated the vanishing
  `k>n` coefficients, eliminating an implicit valuation-of-zero convention.
- C167 promoted a fixed-square coefficient to an all-aspect theorem only
  after adding uniform tail domination and the double-axis/double-boundary
  control.  Review removed Markdown whitespace, tightened every collision
  surface to pairwise transversality, and retained the no-uniform-gap and
  no-general-divisor-formula controls.
- C168 replaced a post-hoc freely chosen phase gate with a natural single-hole
  rank-three gate.  Its proof keeps finite atomic TV distance one, all-mode
  gap failure, phase-label collisions, the torsion control, and the moved-hole
  antiunitary boundary visible.  Final hostile review also made the clock
  self-contained by defining all four hole gates, the hole-zero phase law,
  and the cyclic register map before using `A_0`, `A_1`, `A_3`, `nu_k`, or
  `B_k^k=A^(tensor k)`.

## ARS Stage 2.5 failure-mode audit

This is the theorem/evidence checkpoint before final manuscript release.

1. **Implementation bug passing self-review: CLEAR.**  Producer-independent
   exact reconstruction, SymPy checks, replay, hostile mutations, and separate
   mathematical audit exposed the C165 self-adjoint boundary, C166 valuation
   domain, and C167 transversality wording before release.
2. **Hallucinated citation: CLEAR.**  The five source-locked theoretical notes
   make no literature-priority claim and contain no external bibliography or
   citation-derived number.
3. **Hallucinated result: CLEAR.**  Every all-parameter headline is supported
   by an analytic or algebraic proof.  Finite evidence is not extrapolated.
4. **Shortcut reliance: CLEAR.**  Branch rows, finite rings, word lengths,
   coordinate-24 fibres, register-24 spectra, and decimal columns are labeled
   regression sentinels.
5. **Bug reframed as insight: CLEAR.**  The rejected model continuations and
   all scope/edge repairs are recorded as pivots or corrections, never as
   positive findings.
6. **Methodology fabrication: CLEAR.**  Review is described only as internal
   artifact-level review; no unavailable external reviewer, acceptance score,
   cross-model independence, or unperformed computation is claimed.
7. **Early frame-lock: CLEAR.**  An exhausted Rule-90 continuation, a
   subsumed shear, a free phase tensor, a uniform irrational gap, and all
   overbroad operator interpretations were changed, narrowed, or rejected.

## ARS Stage 4.5 failure-mode audit

This is the final manuscript/artifact checkpoint, separate from Stage 2.5.

1. **Implementation bug passing self-review: CLEAR.**  Released bytes pass
   56,783 checker assertions, 37,168 symbolic checks, 300 hostile cases, five
   byte replays, manifest closure, and fresh-build reproduction.
2. **Hallucinated citation: CLEAR.**  Final PDFs contain no unsupported
   attribution or bibliography; source ownership is stated directly.
3. **Hallucinated result: CLEAR.**  Displayed finite receipts agree with the
   content-addressed evidence, while the all-parameter claims are proved in
   the theorem packages and papers.
4. **Shortcut reliance: CLEAR.**  Every manuscript visibly distinguishes
   theorem ranges from finite sentinels and negative controls.
5. **Bug reframed as insight: CLEAR.**  The C164 build/schema repair, C165
   operator edge, C166 valuation quantifier, and C167 pairwise wording are
   preserved in the release record.
6. **Methodology fabrication: CLEAR.**  Commands, source locks, tests,
   manifests, declarations, deterministic builds, and AI-use disclosures are
   present; internal review is never represented as external peer review.
7. **Early frame-lock: CLEAR.**  The final tuples remain conservative, every
   package retains its obstruction, the five source systems are not merged,
   and Route B remains disabled.

## Route-A assessment

The strict tuples are:

```text
C164 (A1_WEAK,A2_FAIL,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)
C165 (A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
C166 (A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
C167 (A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
C168 (A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)
```

All five are `ROUTE_A_EXPLORATORY`.  C165 and C166 retain finite same-clock
Koopman owners for different source systems; C167 retains its natural
rectangular Dirichlet half-wave generator; C168 retains only its own finite
subunitary scattering parent.  These A4 coordinates are not combined.  C164
has source-side analytic structure on the disk plus a proved unit-circle
extension obstruction, not a target continuation theorem.  No paper has a
target divisor or counting comparison, arithmetic local data, Euler factors,
root numbers, automorphy, a Hilbert--Polya operator, or Route-B permission.
