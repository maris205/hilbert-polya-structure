# Batch review: HCS-C169--HCS-C173

Date: 2026-08-26

System family: five separate Route-A dynamical advances under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Evaluator authority: `flow_systems/skills/route-a-evaluator.md` version
0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
The path and hash are frozen because the Hénon-local evaluator still carries
the older 0.1.0 vocabulary.  Package artifact bases are repository-root-
relative and recorded explicitly in every evaluation YAML.

Recommendation: **retain the five source theorems and obstructions as explicit
Route-A research progress, while keeping Route B unauthorized**.

## Completed paper outputs

1. **C169** treats the irrational Furstenberg skew shift

   ```text
   T_alpha(x,y)=(x+alpha,y+x) mod 1.
   ```

   Its exact iterate has first coordinate `x+n*alpha`, so no positive iterate
   fixes a point and the Artin--Mazur zeta is `1`.  The Haar Koopman action

   ```text
   U e_(m,k)=exp(2*pi*i*m*alpha)e_(m+k,k)
   ```

   gives a pure-point `k=0` component whose eigenvalues are dense on the unit
   circle.  Every `k!=0` component is `|k|` copies of the bilateral shift, so
   the orthogonal complement has Lebesgue spectral type with countably
   infinite multiplicity.  The natural unitary is noncompact and belongs to
   no finite Schatten class; it has no ordinary Fredholm determinant.  The
   involution `R(x,y)=(alpha-x,y)` reverses the same clock and yields the
   antiunitary.  These operator statements do not repair the empty primitive-
   orbit layer.

2. **C170** classifies every Kac scatterer ring, not just sampled marker
   words.  With `eta` the product of all marker signs, a gauge removes every
   interior marker and leaves one boundary sign.  Thus `eta=+1` gives two
   exact `N`-cycles and `eta=-1` gives one exact `2N`-cycle.  If
   `L=N` or `2N` respectively,

   ```text
   #Fix(T^n)=2N * 1_(L divides n),
   zeta_T(z)=(1-z^L)^(-2N/L),
   det(I-zU_T)=(1-z^L)^(2N/L).
   ```

   Pulling reflection back through the gauge and unfolded orbit coordinate
   supplies an involutive reversor and same-clock antiunitary.  Marker
   arrangement therefore changes labelled observations but not the
   permutation conjugacy class or cycle zeta; the result is not interpreted
   as chaotic or arithmetic complexity.

3. **C171** closes the full-dimensional spectral law for the Ehrenfest
   hypercube.  Walsh characters of weight `j` have eigenvalue `1-2j/d` and
   multiplicity `binom(d,j)`, hence

   ```text
   Tr(P_d^n)=sum_(j=0)^d binom(d,j)(1-2j/d)^n,
   det(I-zP_d)=product_(j=0)^d
       (1-(1-2j/d)z)^binom(d,j).
   ```

   Every diagonal return probability is `2^(-d)Tr(P_d^n)` and is zero at odd
   times.  Hamming-weight lumping gives the reversible binomial birth--death
   chain with simple Krawtchouk spectrum.  The full and lumped determinants
   therefore distinguish multiplicity from distinct spectral support.  For
   `d>1` these are weighted Markov-loop traces, not deterministic fixed-point
   counts.  The isolated `d=1` operator is the deterministic two-cycle but
   supplies no uniform all-family primitive or arithmetic layer.  Although
   `P_d` is naturally self-adjoint, exponentiating it changes the discrete
   stochastic clock, so A4 remains only a formal hint.

4. **C172** proves a uniform theorem for every finite field and primitive
   multiplier.  Zero is fixed, while the nonzero elements form one cycle of
   length `N=Q-1`.  Therefore

   ```text
   #Fix(T_a^n)=Q if N divides n, and 1 otherwise,
   zeta_T(z)=1/((1-z)(1-z^N)),
   det(I-zU_T)=(1-z)(1-z^N).
   ```

   Field inversion is an involutive reversor.  The Koopman spectrum is the
   union of one fixed-cycle eigenvalue and every `N`th root of unity, and the
   unitary is self-adjoint exactly for `Q<=3`.  The arithmetic gate remains
   weak: the same cycle and determinant law holds on a non-field cyclic
   surrogate, while neither a rational-prime orbit dictionary nor logarithmic
   and von-Mangoldt weights appears.  No global product or local-factor claim
   is made.

5. **C173** converts a tempting finite-order nonlinear model into an exact
   determinant obstruction.  Direct iteration of
   `F(x,y)=(y,(1+y)/x)` gives `F^5=id`.  The golden-ratio point is the unique
   fixed point and every other positive point has exact period five.  Thus
   fifth iterates have an uncountable fixed set and the classical
   Artin--Mazur zeta is not defined.  The density `dx dy/(xy)` is invariant,
   coordinate swap is a reversor, and the natural Koopman unitary satisfies
   `U^5=I`.  A measurable fundamental-domain construction proves that all
   five fifth-root eigenspaces are infinite-dimensional.  Consequently this
   unitary is noncompact, belongs to no finite Schatten class, is not
   self-adjoint, and has no ordinary Fredholm determinant.

## Strict Route-A record

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C169 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C170 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C171 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C172 | `A0_WEAK_ARITHMETIC_RELATION` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_EXPLORATORY` |
| C173 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |

The A4 entries belong to different natural source operators and are never
merged.  In particular, no A4 entry can compensate for a failed A0 or A1.
C172's prime-power state space is not an arithmetic local factor.  No paper
contains a target zero or prime census, target divisor, functional equation,
target counting law, Euler factor, root number, automorphy object, or
Hilbert--Polya operator.

## Uniform release audit

The final deterministic and content-addressed counts are populated only from
the released packages:

| paper | checker assertions | SymPy checks | hostile rejections | payload closure | PDF pages |
|---|---:|---:|---:|---:|---:|
| C169 | 1,574 | 940 | 17/17 | 27/27 | 2 |
| C170 | 114,056 | 221 | 17/17 | 27/27 | 2 |
| C171 | 2,990 | 914 | 39/39 | 27/27 | 2 |
| C172 | 663 | 486 | 45/45 | 27/27 | 2 |
| C173 | 891 | 207 | 50/50 | 27/27 | 2 |
| **total** | **120,174** | **2,768** | **168/168** | **135/135** | **10** |

Finite evidence rows are regression sentinels.  They do not prove a statement
for an untested parameter; each all-parameter result above is discharged in
the corresponding theorem package.  Producer-independent checkers must not
import producer code, and the separate symbolic pass must reconstruct the
headline identities rather than compare copied strings.  Byte replay binds
the exact released evidence.  Semantic mutations repair their payload hashes
before rejection, while the stale-hash mutation is tested separately.

Every final manifest must close exactly 27/27 payload files.  Each package has
28 physical release files including the self-excluded manifest.  Fresh
fixed-epoch builds must reproduce the released PDF bytes; fonts must be
embedded, final logs warning-free, pages visually intact, and round 0, round
1, and round 2 content-distinct with `main.pdf==main_round2.pdf`.

## Content-addressed release ledger

| paper | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|
| C169 | `3203a596fc28802760bf29e9750fc36657b40310686d29c4284c54804af9d8df` | `447af4e9468fa8001f0a0bbe42230532f3a6f2254a4f4f8f2513a04a14b5113d` | `95b292bb0d1c617e3116de8629aaabde3ff27a56a11a63f2b37e4010f4f879d5` |
| C170 | `b1a841ebb171c6d7da94b8837ca0785766ebb50eed15e690730024e1c60b76cf` | `fdd0782265a5049bbb30211655e8cf8e79ad8e3c52896644e9563ca0a3743db7` | `1e060325b5d7e698d7fb5ae4d2770ba8f20c13ca68fd4855729adfca12457cdd` |
| C171 | `6fa5dd685c4cbde5f0e00cb87d3e53fbfae25d3792dd0ef5a80e545cb1c954ff` | `592c9a57b5592bdc9e07e4e3554c884e8ca1daaf4154c8bafed02e5dd3cc4c26` | `51f62303af88ca0334a676648909c1d5110d9d74c7cf7989c212a556299cb778` |
| C172 | `30f505f729e54c6aa1f1d5ceaa8de16277ff4529ff5cec8543b91a7dd83b4260` | `e33678ba00be91542797fd3c8625c33159b6f9dfcef65e1ad92f9674e7895a37` | `ecdfc64b91907ae7f5f15a5bc48e227fcf2ffdacde3ba88f22d81aa1059147c9` |
| C173 | `6695e3ad62be2f1125d7a9e5488f6a78c7ad2c101c9fee1e896770e69fb28240` | `74d495da262be5ee425e0a61772553809929249f63a7335d62ca9dc96d442570` | `f44abdad0e715d7cfadecdbaccbb9f09d0a38b2c7ed13ef259e78b1ec0046bec` |

## Internal cross-review and repair ledger

These are evidence-anchored internal theorem, scope, and release audits.  They
are not external peer review and do not claim reviewer or error-process
independence.

- **C169:** the review distinguishes dense point spectrum from density of the
  pure-point subspace.  It also requires a diagonal unitary conjugacy on each
  residue class before assigning bilateral-shift spectral type.  The machine
  ledger now separates the Fourier-grid bound `fourier_k_max=8` from the
  spectral-sector sentinel `sector_k_max=12`.
- **C170:** the review requires the reversor to be pulled back explicitly from
  the marker gauge and unfolded cycle, including `N=1`; abstract finite-
  permutation reversibility alone is not accepted as the advertised theorem.
  The paper plan was repaired to match the actual equation-first presentation.
- **C171:** the review separates deterministic periodic points from weighted
  closed Markov walks, assigns `A1_FAIL` because no primitive-orbit owner is
  defined, and lowers A4 because `exp(-itP_d)` changes the source clock.  The
  `d=1` and bipartite odd-time boundaries remain explicit.
- **C172:** the review includes `Q=2,3` in the self-adjoint boundary and uses a
  composite cyclic surrogate to prevent finite-field cardinality from being
  promoted to a rational-prime orbit law.
- **C173:** the review treats uncountable fifth-iterate fixed sets as a
  stopping theorem.  Infinite multiplicity of all five spectral values is
  proved through a measurable fundamental domain rather than inferred from
  `U^5=I`.  Its Stage 2.5/4.5 audit was rewritten to name the mandatory seven
  failure modes rather than a substitute taxonomy.

## ARS Stage 2.5 failure-mode audit

This is the theorem/evidence checkpoint before final manuscript release.

1. **Implementation bug passing self-review: CLEAR.**  All five separate
   checkers, symbolic reconstructions, byte replays, mutations, and declared
   edge cases pass against the final evidence bytes.
2. **Hallucinated citation: CLEAR.**  The registered reference and citation
   populations are both zero.  The papers make no literature-priority claim.
3. **Hallucinated result: CLEAR AT PROOF LAYER.**  Every headline is paired
   with an explicit all-parameter proof; finite rows are not extrapolated.
4. **Shortcut reliance: CLEAR AT DESIGN LAYER.**  Every finite table is
   labelled a regression sentinel, and the checker reconstructs formulas.
5. **Bug reframed as insight: CLEAR.**  The Anosov, baker, and Hashimoto
   collisions are recorded as killed ideas; none is repackaged as progress.
6. **Methodology fabrication: CLEAR.**  Review is internal, with no external
   reviewer, acceptance score, cross-model independence, or unperformed run.
7. **Early frame-lock: CLEAR.**  Three colliding proposals were replaced;
   C171 was lowered to `A1_FAIL`, and C172 remains only exploratory where the
   source clock or arithmetic link does not survive the strict gates.

## ARS Stage 4.5 failure-mode audit

This is a fresh final manuscript/artifact pass and does not inherit Stage 2.5
as evidence.

1. **Implementation bug passing self-review: CLEAR.**  Every released byte
   passes its exact pipeline, 27/27 package manifest closure, and fresh-build
   PDF reproduction; post-repair re-audits found no remaining blocker.
2. **Hallucinated citation: CLEAR.**  Final registered citation/reference
   denominator is zero; no attribution is introduced during revision.
3. **Hallucinated result: CLEAR AT PROOF LAYER.**  Final prose is bounded by
   the theorem packages and explicit nonclaims.
4. **Shortcut reliance: CLEAR AT DESIGN LAYER.**  Final evidence remains a
   sentinel rather than the authority for parameter-uniform claims.
5. **Bug reframed as insight: CLEAR.**  Every repaired boundary remains in the
   paper's limitations or hostile-audit record.
6. **Methodology fabrication: CLEAR.**  Final process language remains
   internal and deterministic where claimed; prose review is not called
   externally validated or byte-reproducible.
7. **Early frame-lock: CLEAR.**  The final five subtypes remain separate, with
   A0 failures visible and no cross-candidate coordinate aggregation.

## Release conclusion

`RELEASE COMPLETE`: all five evidence ledgers, PDFs, evaluator records, and
self-excluded manifests close under the stated hashes.  This is a release of
five scoped source theorems and obstructions, not a Route-A success claim.
`route_b_invocation_allowed=false` remains fixed throughout.
