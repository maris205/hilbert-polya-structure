# Independent cross-review: hyperbolic FAD detector-image topology

Date: 2026-09-06. Reviewer: the nonauthor `scout_nonaffine_charp` team agent.
Status: **PASS_MATH_AND_2024_SOURCE_SCOPE**. No remaining mathematical
blocker was found. Admission and numbering remain the coordinator's decision.

This is an internal, nonauthor proof/source check, not human peer review,
formal verification, a calibrated journal recommendation, or a worldwide
priority certificate. `NOT_CALIBRATED`. The research-review workflow and the
ARS source-integrity/counterargument discipline informed the check; no
external model API or simulated multi-seat editorial panel was used.

## Reviewed snapshot and scope

The complete 316-line `arithmetic_candidate/PROOF_PACKAGE.md` and 73-line
`arithmetic_candidate/CONTRACT.md` were read independently. Their SHA-256
values at review were:

- Proof: `4bb118cb0149533ab999d185531de94c92d68b37eb43514a638c4d8ea3fb6457`.
- Contract: `9ad1e15d0fb97329dbec88434ec885adc2bc4f29349afa49c05a07df5d8a3d08`.

Line references below refer to this proof snapshot. The author's subsequently
available `SOURCE_AUDIT.md` was read after the reviewer's main mathematical
assessment and independent BCH/2026-source inspection. Its reading claims
are not substituted for this reviewer's own reading. `REALIZED_EXAMPLES.md`
was not independently audited by this reviewer; the coordinator reports
having separately reviewed it. No author-owned files were edited, no old
experiment was rerun, and no C-number was assigned here.

| Criterion | Judgment | Basis |
|---|---|---|
| Exact observable and hypotheses | Pass | Native iteration and the limit set of `N pi_f(N)/Lambda^N`; fixed finite prime set; positive periodic weights; finite nonnegative real exponent types |
| Adaptive-cover quantifiers | Pass | Direct recount of the tree splits and all epsilon estimates |
| Fourier nonconstancy | Pass | Independent coefficient computation, type asymptotics, and dominated-convergence check |
| Detector domain and local perfectness | Pass | Exact CRT domain and active-center construction on every cylinder |
| Imported 2024 theorem scope | Pass | Original version-specific definitions, detector theorem, and open-problem statement checked |
| Worldwide originality / final-book ownership | Not certified | Bounded search only; final EMS book text was not obtained |

## Strongest counterargument and outcome

The serious attempted refutation is that the conclusion might confuse the
topology of a profinite domain with the topology of its real image. A
continuous image can have intervals or isolated values; infinitely many
limits alone is insufficient. A naive depth-`K` partition also has `p^K`
pieces, which would not imply zero box dimension when `K` grows like
`log(1/epsilon)`. Even if a thin image is established, positive kernels
centered at many integers could conceivably cancel their oscillations after
translation, while detector congruences might prevent any active center
from lying in a specified cylinder. These are independent failure modes,
not different descriptions of one missing step.

The submitted argument withstands them. The partition refines only balls
containing one of the finitely many relevant centers, giving `O(LK)` leaves.
Nonconstancy is not inferred from positivity alone: the slowest-decaying
radial Fourier type has a strictly negative normalized high-conductor
coefficient, since each fixed integer translation has character tending to
one. Absolute summability and finitely many types justify passage through
the infinite sum. The exact detector-domain CRT permits independent local
coordinates after fixing the finite residue. Negative integer choices keep
the other factors strictly positive, and the exponent period coprime to its
own prime guarantees an active center in every varying ball. Thus isolated
image values are genuinely excluded, rather than silently assumed absent.

The remaining strongest objection concerns priority, not validity: an
unobtained final book revision could already contain a solution. This
review does not turn failure to locate such a version into proof that none
exists. The permitted conclusion remains source-local to the checked 2024
public version, with a bounded later-literature check.

## 1. Adaptive partition and epsilon-uniform cover

Evidence anchors: `equation/text`, lines 73–133. Confidence: 5/5, direct
reconstruction of the combinatorial count and inequalities.

For a finite center set `E`, at any depth `j<K` there are at most `|E|`
occupied balls. Each occupied ball is split once into `p` children. There
are therefore at most `|E|K` splits and exactly `1+(p-1)*(number of splits)`
terminal leaves. A terminal ball below depth `K` contains no center, so
ultrametricity makes every distance to a center constant on it. A depth-`K`
leaf has constant truncated valuations. This proves the claimed partition
without replacing it by the exponentially larger full residue partition.

For an active finite exponent type, `H(z)<=exp(-c_p K)` on `v_p(z)>=K`.
If `s>0`, use `c=s log p`; if `s=0<t`, use `p^K>=K`. The minimum is positive
because the list is finite and inactive pairs are omitted. This does not
require an exponent lower bound uniform over different systems.

With `B=R/(1-Lambda^(-1))`, the chosen `L` gives tail bound
`B Lambda^(-L)<=epsilon/8`. On a common product atom at a fixed residue
`a`, every active kernel either agrees exactly or has both values in
`[0,epsilon/(8dB)]`. Telescoping the product gives difference at most
`epsilon/(8B)` for each product, and summing the weights gives head
variation at most `epsilon/8`. The two tails contribute at most
`epsilon/4`, leaving diameter at most `3epsilon/8<epsilon`.

Clamping `L,K_p` to one causes no problem for large epsilon: whenever the
unclamped logarithm is negative, the target tail tolerance already exceeds
the relevant trivial bound. For small epsilon each is `O(1+log(1/epsilon))`.
Thus `w product_p[1+(p-1)LK_p]` yields the stated polylogarithmic bound,
uniformly over the detector domain for each fixed system. Restricting to
the CRT-compatible domain cannot increase the number of image pieces.

Compactness plus absence of any interval implies nowhere denseness in
`R`; the cover itself gives upper box dimension zero and, for every
`alpha>0`, vanishing `N_epsilon epsilon^alpha`. No implicit regularity or
injectivity assumption enters this deduction.

## 2. Fourier coefficient, dominance, and local rescaling

Evidence anchors: `equation/text`, lines 140–220. Confidence: 5/5, all
coefficient signs, asymptotic regimes, and limit exchanges checked.

The radial expansion has positive differences
`delta_j=h(j-1)-h(j)` and uniform remainder bounded by `h(K)->0`, including
at zero. For a character of conductor `p^k`, integrating the ball indicator
gives zero for `j<k` and `p^(-j)` for `j>=k`. Hence the nontrivial Fourier
coefficient is exactly `-sum_{j>=k} p^(-j) delta_j`; its sign and the index
`j-1` are correct.

When `t=0<s`, direct geometric summation gives the coefficient in (3).
When `t>0`, the ratio `h(k)/h(k-1)` tends to zero. The first term dominates;
the displayed tail bound divided by `p^(-k)h(k-1)` tends to zero. This
establishes (4) for real, not just integer, exponents.

The lexicographic choice must minimize `t` first, then `s`, exactly as
written. A type with larger `t` loses at the `p^k` scale, regardless of
its smaller possible `s`. With the same `t`, larger `s` loses geometrically.
For `t_*=0`, the exact formula handles the purely tame comparisons and
every positive-wild type is smaller. Finite type sets make all ratios
uniformly bounded in `k`, including the finitely many initial `k` values.

The translation limit is valid for every fixed ordinary integer, including
negative integers. It is not a claim that these characters tend to one
for arbitrary `p`-adic translations, nor that convergence is uniform in all
centers. No such stronger claim is needed: `sum_i b_i<infinity` provides a
dominating summable majorant. The surviving minimal-type coefficient sum
is positive, so the limit is strictly negative and nonzero. This defeats
the proposed cancellation counterexample for the stated class.

On `a+p^K Z_p`, centers outside the ball have constant distance and hence
contribute a constant. For an inside center `l=a+p^K j`, the rescaling is
exactly

`H_{p;s,t}(a+p^K y-l)=p^(-sK) H_{p;s,t p^K}(y-j)`.

It also respects the zero convention. At fixed `K` the transformed type
set remains finite and active, and the new positive coefficients remain
summable. There is no requirement that this new finite set be uniform as
the ball varies. Therefore the global nonconstancy lemma applies locally.

## 3. Detector CRT, active centers, and image perfectness

Evidence anchors: `equation/text`, lines 224–272. Confidence: 5/5, explicit
congruence and slice reconstruction.

The detector group has only the compatibility conditions
`x_p congruent a mod p^(v_p(w))`. Necessity follows by closure; sufficiency
is the generalized CRT for `n mod w` and finitely many specified prime-power
residues. Any compatible finite precision can be attained by arbitrarily
large positive integers. There is no additional hidden coupling among the
prime coordinates.

After fixing a nonempty cylinder, every other coordinate ball contains
negative ordinary integers. Such an integer differs from all centers
`l>=0`, so all other kernel factors are strictly positive. They need not
be bounded away from zero uniformly in `l`: strict positivity and the
summable upper bound `c_l<=R Lambda^(-l)` suffice for Lemma 6.

For the selected active prime, solve
`l congruent b_p mod p^K` and `l congruent a-n_0 mod m_p`.
These moduli are coprime by hypothesis. The resulting progression has
nonnegative members, giving an active center in the specified ball.
Consequently the detector is nonconstant on every nonempty cylinder and
on every nonempty open set.

If an image value were isolated, its nonempty preimage would be open by
continuity. The function is constant on that preimage, contradicting the
preceding property. This proves perfectness even when fibers are large;
it does not require global or local injectivity. Combining with the
compact, nonempty, interval-free image gives the Cantor conclusion.

A successful *outside-hypothesis* attack confirms the importance of the
coprime-period restriction. Take `p=2`, `w=2`, `r_n=1`, `t_n=0`, and let
`s_n=1` for odd `n`, `s_n=0` for even `n`. This is active but its own-prime
period is forbidden. On the detector `x congruent a mod 2`, an active term
has `a-l` odd, hence `x-l` odd and kernel value one; every inactive term
also equals one. The entire image is the singleton
`{1/(1-Lambda^(-1))}`. Thus simply deleting the period hypothesis would make
the theorem false. The submitted theorem retains the necessary hypothesis.

## 4. Independently checked primary-source boundaries

The following are actual source inspections by this reviewer, not claims
to have read every page of any cited work. No long quotations are used.

- BCH, [arXiv:2209.00085v2](https://arxiv.org/pdf/2209.00085v2): Definition
  2.2.1 makes gcd sequences periodic; Definitions 7.1.1–7.1.2 allow the
  stated real exponent data. Definition 10.3.9 fixes hyperbolicity. Definition
  12.4.1, the text before 12.4.3, equation (12.4), and 12.4.3(ii) give the
  hyperbolic detector reduction. Theorems 12.5.1–12.5.2, Remark 12.5.3,
  Lemma 12.5.4, the negative-integer slice in the proof of 12.5.1, and
  Problem 14.1.1 delimit the known topology. The arbitrary-real Fourier
  proof is not an extrapolation of that lemma's integer-exponent statement.
- Byszewski–Cornelissen, [ANT 2018 publisher PDF](https://msp.org/ant/2018/12-9/ant-v12-n9-p06-p.pdf):
  Theorem 9.5 and its surrounding detector formulas establish the older
  one-characteristic Cantor/finite-set result. That overlap is classical.
- Everest–Miles–Stevens–Ward, [author preprint](https://arxiv.org/pdf/math/0511569):
  Section 2, specifically the displayed one-prime detector series, Lemma
  2.4 and Corollary 2.5, supplies earlier quantitative injectivity. These
  checked statements do not supply the present full-class cover theorem.
- Cornelissen–Park, [arXiv:2605.24504v2](https://arxiv.org/pdf/2605.24504v2):
  abstract, introductory A–D, the FAD setup and Fourier decomposition in
  Section 4/Theorem C, and bibliography entry 6 were inspected. Its
  observable is a Cesaro normalized-fixed-count mean feeding orbit
  decomposition statistics, not this detector-image topology. Full-text
  searches for Cantor/accumulation/nonconstant found no matches; that
  absence is merely supplementary, not the substantive comparison.

The [current BCH arXiv entry](https://arxiv.org/abs/2209.00085) still lists
v2, dated 19 April 2024. The [author's publication page](https://webspace.science.uu.nl/~corne102/publications.html)
still describes the old preprint. The [EMS series page](https://ems.press/books/etm)
and bounded title/author searches did not provide the final book text.
The 2026 paper's bibliography is affirmative evidence of a forthcoming
EMS version, so this version uncertainty must remain explicit.

## 5. Findings, non-defects, and final recommendation

No CRITICAL or MAJOR mathematical issue was found in the reviewed snapshot.

One attribution refinement was communicated to the author and coordinator:
`text`, Contract lines 60–62 under “Proposed new proof work,” can be read as
crediting the negative-integer technique itself as new. BCH already uses
that technique in its cardinality proof (printed pp. 132–133). The new work
is its every-cylinder use together with the new cover/Fourier argument.
Confidence: 5/5, direct source comparison. Severity: MINOR presentation /
attribution issue, not a proof gap. The coordinator confirms that this
classical input is deducted in the admission treatment; this is not a
remaining blocker. No numerical severity score or journal acceptance
probability is assigned.

Non-defects worth preserving:

- The cover exponent is not claimed sharp; `2d` suffices for zero dimension.
- No non-atomic pushforward measure, fiber bound, or injectivity is claimed.
- The `d=0` finite-image formula is classical and is not sold as the new result.
- The proof is for any fixed finite distortion set, not a uniform theorem
  over unbounded prime sets or degenerating exponent values.
- Positive-real weights and integer centers are genuine hypotheses of the
  nonconstancy proof, not removable formal conveniences.
- Resolving the checked 2024 hyperbolic regimes is not a claim to classify
  all nonhyperbolic detector images or to establish worldwide first priority.

Recommendation: the coordinator may proceed to source-local admission and
drafting on mathematical grounds. Keep the source deduction and final-book
version limitation visible. If a later book text or a directly overlapping
theorem becomes available, perform a new ownership comparison; do not
retroactively describe this bounded review as having certified it absent.
