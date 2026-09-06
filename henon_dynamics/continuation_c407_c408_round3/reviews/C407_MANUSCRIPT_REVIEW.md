# C407: independent review of the actual manuscript

Date: 2026-09-06. Reviewer: nonauthor team agent
`scout_nonaffine_charp`. Verdict: **PASS_AFTER_ONE_MINOR_CITATION_FIX**.
Remaining mathematical blockers: **0**. Remaining required theorem,
citation, or scope corrections: **0**.

This is an internal nonauthor mathematical/manuscript review, not human
peer review, formal verification, a calibrated journal recommendation, or
a certificate of worldwide priority. `NOT_CALIBRATED`. The research-review
skill and source-integrity/counterargument discipline were used within the
assigned team workflow; no external API review or simulated editorial
panel was claimed. Final compilation, PDF inspection, and release
authorization remain with the coordinator.

## 1. Actual material read and snapshot identity

The author explicitly announced completion and froze the mathematical and
citation text before final signoff. I read the entire actual `main.tex`,
`math_commands.tex`, all eight input section files, and all four inline
bibliography entries: **967 source lines** in the submitted snapshot. This
is not a review of the outline or proof summary in place of the paper.
The theorem and all proof steps were compared with the previously reviewed
proof contract. The current 324-line `PROOF_PACKAGE.md` and 78-line
`CONTRACT.md` were also reread in full after their hashes were seen to have
changed; the changes clarify admission status and classical attribution,
without changing the mathematical statements or proof steps. The complete
95-line `REALIZED_EXAMPLES.md` was independently read during this manuscript
review, superseding the explicit exclusion of those examples in my earlier
proof/source report.

All paths in the following table are relative to `arithmetic_candidate/paper/`.
These are the complete submitted/final mathematical-text hashes at signoff.

| File | Lines | SHA-256 |
|---|---:|---|
| `main.tex` | 73 | `bc73ed483b15bdef0deadf3ac37e223db73f2df26da6a59e20c0546c3849302d` |
| `math_commands.tex` | 26 | `327de1af5eb2b0f271e8ac1bb4588763923822e3263d4cb6e445c7cd6a9218e3` |
| `sections/0_abstract.tex` | 19 | `bac98c451bf237bca5abfccb45e737ebd520d057a443e4fcefc9784fe5eba77f` |
| `sections/1_introduction.tex` | 119 | `4b8ddb97a9f0a6969651ae763a446401fb7b6840aa6fec197d76771b73809769` |
| `sections/2_image_theorem.tex` | 94 | `6afa7d4f00b731dd71691a41db4a17ca5e6e1878573a193b75216a87e27f875e` |
| `sections/3_adaptive_covers.tex` | 125 | `fee110bb4ff52b2740cdcc69bcba2a4d0175c597de7a5a8e6f0b83515ef9ce71` |
| `sections/4_fourier_nonconstancy.tex` | 148 | `e8943deaeefa80bf999c8a9e936eaea72657985b2d753e6d174e0b7458e5a081` |
| `sections/5_perfectness.tex` | 103 | `a1bf37d7a05f1eb3fa840045e0c7155b69928cbe46062117e632255b9e370dbf` |
| `sections/6_dynamical_applications.tex` | 196 | `d0d59bb62102fc640e50feab7b8b5f599ff754cf62edb0ce47c1bd370b076557` |
| `sections/7_scope.tex` | 64 | `63cdb88f6b49d7ae2434ac5da2063c455214e6d717d28e9bf7048a0259484193` |

The supporting files at the current comparison have hashes:

- `PROOF_PACKAGE.md`: `35f436921c019a63f2ce007b8083d1f39611c5253efdbe863b9c726c10a2bf7f`.
- `CONTRACT.md`: `3dcc04b241290ec7ea02c0c17863c92e4e07ed5ed2748ce6479f96779e657d2e`.
- `REALIZED_EXAMPLES.md`: `dc8145e33038fc6506768f8c0cdb5495f333f36c0c76c788cbd61b546ffbb249`.

For comparison, the earlier independent proof/source review used proof hash
`4bb118cb0149533ab999d185531de94c92d68b37eb43514a638c4d8ea3fb6457`
and contract hash
`9ad1e15d0fb97329dbec88434ec885adc2bc4f29349afa49c05a07df5d8a3d08`.
Its detailed source inspection remains documented in
`wild_ordinary/CROSS_REVIEW_ARITHMETIC_TOPOLOGY.md`; no unmodified old
experiment or numerical certificate was rerun here.

## 2. Required correction and affected recheck

**MINOR C407-M1, resolved.** The first partial introduction, lines 51–54,
summarized the abelian-variety finite-set/Cantor-set conclusion without
stating the unique-dominant-root standing assumption of the cited section.
The citation also benefits from specifying the branch that is not very
inseparable. I sent the exact condition and primary-source locator to the
author and coordinator. The author, not this reviewer, made the correction.

The partial-draft introduction hash was
`bf59864e316c2417c624e491d0a1e0c602285bfffc1bdd3b51f1a1c0c607ff2f`.
The corrected introduction is the 119-line file hashed in the table above.
Its lines 51–55 now state both conditions. I reread the entire corrected
introduction and checked the affected citation against the actual source's
Section 9 standing assumption and Theorem 9.5(iii)(b). No theorem, proof,
example, normalization, or grade changed as a result of this fix. All other
files in the first six-file partial snapshot retained their hashes when
the complete manuscript was submitted.

A precautionary author message also highlighted the wild example's entropy
wording. This was not a discovered false statement in the submitted paper:
the final text correctly defines FAD entropy algebraically as `log Lambda`
and does not assert an ordinary limit of normalized logarithmic fixed-point
counts or equality with topological entropy for arbitrary realizations.

## 3. Proof and theorem audit

### Exact owner and quantifiers

The abstract, image theorem, and orbit-counting corollary agree on the
observable: the real accumulation set of `N pi_f(N)/Lambda^N` on native
positive integer iterates. The analytic theorem fixes a finite prime set,
positive periodic weights, and finitely many nonnegative real exponent
pairs. Constants may depend on this fixed data; uniformity as exponents
approach zero or as the prime set varies is expressly excluded. The
dynamical corollary requires an actual confined realization with the
stronger FAD gcd-sequence conditions. It does not silently realize every
formal analytic detector as fixed-point counts.

Removing inactive primes is harmless because their kernels are identically
one. The zero convention correctly distinguishes active and inactive
kernels. The finite `d=0` formula is obtained by summing the geometric
series in each residue class and agrees with the contract.

### Adaptive covers: `sections/3_adaptive_covers.tex`

The partition lemma now permits any finite center set in `Z_p`; this modest
strengthening of the integer-center wording in the proof package is valid,
since only occupied balls and ultrametric distances enter its proof. There
are at most `L` occupied balls per depth, at most `LK` splits, and at most
`1+(p-1)LK` leaves. Unoccupied terminal balls give exact valuation constancy;
depth-`K` leaves give constancy after truncation.

The positive constant `c_p` is taken over active pairs only, so inactive
pairs do not invalidate the valuation tail estimate. The choices of `L`
and `K_p`, including their lower bound of one, control both tails even if
`B` is small. On a fixed-residue product atom the coordinate differences
are at most `epsilon/(8dB)`. The product telescope and summable weights give
head variation at most `epsilon/8`; two series tails add at most
`epsilon/4`. Thus a single interval of length `epsilon` covers each
nonempty restricted atom. The resulting product count has logarithmic
exponent `2d`. The upper box and Hausdorff conclusions follow directly,
and compactness turns empty interior into nowhere denseness. Perfectness
is deliberately not inferred from this argument.

### Fourier conductor, signs, indices, and infinite sums

Evidence: `sections/4_fourier_nonconstancy.tex`, lines 3–143. The character
has conductor `p^k`; integration over `p^j Z_p` is zero for `j<k` and equals
`p^{-j}` for `j>=k`. Consequently the kernel coefficient is **negative**
with the stated tail index starting at `j=k`. The geometric closed form
for `t=0` and the wild first-term asymptotic both have the correct powers.
The displayed remainder bound is negligible relative to the first term.

For the translated series, the chosen transform convention gives exactly
the conjugated translation factor written in the paper. Among the finite
types actually present, minimizing `t` and then `s` selects the slowest
decay. All other normalized coefficients tend to zero, and the finite
family of convergent ratios is uniformly bounded for integer `k>=1`.
Uniform absolute convergence justifies termwise integration. Dominated
convergence then applies to the normalized infinite sum using the summable
positive coefficients. Crucially, character convergence to one is used
only at each fixed **ordinary integer** center, not asserted for every
`p`-adic point or uniformly over infinitely many centers. The limit is a
strictly negative real number, hence the complex coefficients are nonzero
for all sufficiently large conductors.

The local rescaling changes `t` to `t p^K` and multiplies the coefficient
by `p^{-sK}`. Zero values, inactive terms, centers outside the ball, and
summability are all handled explicitly. The transformed finite type set
is held fixed while the Fourier conductor tends to infinity. No invalid
uniformity in the ball depth is needed.

### Detector CRT and exclusion of isolated image values

Evidence: `sections/5_perfectness.tex`, lines 3–102. The exact diagonal
closure has only the congruences `x_p = a mod p^{v_p(w)}`. Compatible finite
residues therefore admit the asserted CRT progression. After fixing the
finite residue, the chosen product cylinders genuinely lie in the domain.
Negative ordinary integers in the frozen coordinates make every remaining
coefficient strictly positive, because all centers are nonnegative. A
uniform positive lower bound is neither claimed nor needed; the geometric
upper bound supplies summability.

The active pair is found using the period belonging to the varying prime.
Its coprimality with that prime is precisely what makes the two active-center
congruences solvable in every prescribed ball. Nonconstancy is established
on a slice of every cylinder, rather than on one globally selected slice.
An isolated real image value would have nonempty open preimage, directly
contradicting this result. Together with the cover, this proves the stated
Cantor-space conclusion. The argument does not rely on the false principle
that every continuous image of a profinite space is totally disconnected.

## 4. Genuine examples and boundary example

Evidence: all of `sections/6_dynamical_applications.tex` and
`sections/7_scope.tex`, not just `REALIZED_EXAMPLES.md`.

- **Two-prime solenoid.** The finite quotient of `Z[1/15]` by
  `(2^n-1)Z[1/15]` removes exactly the 3- and 5-primary parts. The two
  valuation formulas, positive gcd weight of period four, own-prime
  coprime exponent periods, dominant root two, and two active primes all
  check. The bound's exponent is four. The map is called the dual of
  multiplication by two, not incorrectly required to be an automorphism.
- **Wild additive map.** Writing `n=p^a m` in the Frobenius composition
  ring gives lowest Frobenius power `p^a` and highest power `n`. After
  factoring through `x^{p^{p^a}}`, the remaining additive polynomial has
  nonzero derivative `m` and degree `p^{n-p^a}`. The algebraic closure's
  Frobenius bijection therefore gives the exact count claimed, including
  the endpoint `n=p^a`. The empty matrix, `c=Lambda=p`, and constant wild
  exponent one satisfy the stipulated representation. The covering
  exponent is two. Equal cellular-automaton counts are not promoted to
  conjugacy.
- **Product example.** Multiplication of the genuine counts gives
  multiplicative part `14^n-7^n`, unique dominant root fourteen, and
  active primes `{3,5,7}`. Period four remains compatible with each
  own-prime exponent period. The covering exponent is six. This is one
  product system illustrating two regimes, not a new fixed-point formula.
- **Forbidden-period singleton.** With `p=2`, exponent one on odd indices,
  and exponent zero on even indices, every active term is evaluated at a
  2-adic unit because `x=a mod 2`. Every kernel is therefore one and the
  series is the stated constant. The example correctly lies outside the
  own-prime-coprime FAD hypotheses, while remaining inside the enlarged
  analytic data class. It separates perfectness from the covering bound
  and is not a counterexample to the theorem as stated.

In particular, along `n=p^a` the wild fixed-point count is one, so an
ordinary limit `log Fix(U^n)/n = log p` would be false. The actual final
manuscript makes no such assertion. The entropy definition and source
reduction are explicit in section-file 6, lines 38–72.

## 5. Every actual citation context

The four bibliography entries are the four cited works; no undefined source
key or uncited imported theorem was found in the TeX. The source audit is
version-specific, and the locators below refer to original source texts
actually inspected by this reviewer during the proof and manuscript checks.
This does not claim to have reread every page of each work or to have
obtained the final EMS book.

| Actual source | Manuscript use and checked locators | Finding |
|---|---|---|
| [Byszewski–Cornelissen–Houben, public v2](https://arxiv.org/pdf/2209.00085v2) | Intro, perfectness, applications, scope: Definitions 7.1.1–2, 9.1.2, 10.3.4, 10.3.9, 12.4.1; Lemmas 10.3.2 and 10.3.10; Examples 7.1.3, 7.2.6–7; Proposition 9.1.4; equation (12.4), Theorem 12.4.3(ii), Theorems 12.5.1–2, Remark 12.5.3, Problem 14.1.1 | Correct reduction, examples, and version-local comparison. Classical negative-integer slices are explicitly credited. |
| [Byszewski–Cornelissen, ANT 2018](https://msp.org/ant/2018/12-9/ant-v12-n9-p06-p.pdf) | Corrected intro: Section 9 standing assumption, Proposition 9.4, Theorem 9.5(iii)(b), and the local-injectivity argument | Correct after C407-M1; no general abelian-variety statement outside those conditions remains. |
| [Everest–Miles–Stevens–Ward, author preprint](https://arxiv.org/pdf/math/0511569) | Intro: Theorem 1.1, Lemma 2.4, Corollary 2.5 | Supports compact-group detection and a quantitative special one-prime injectivity result. The paper distinguishes that work's terminology from FAD hyperbolicity. |
| [Cornelissen–Park, public v2](https://arxiv.org/pdf/2605.24504v2) | Intro and scope: Theorem C, Section 4, reference 6 | Different observable is identified; the forthcoming-book reference supports the stated unresolved version-comparison limitation, not proof of worldwide originality. |

The new citations to dominant-root positivity, the leading factor equal to
one, and the algebraic entropy definition were checked directly in the
source, not inferred from an author's citation list. The formula for the
ordinary additive map is explicitly attributed through the cited BCH
example; the manuscript also supplies its own complete elementary
verification, without claiming an independent rereading of Bridy here.

Bibliographic titles, authors, versions, journal/page data, and links agree
with the inspected source records. Preprint theorem locators are explicitly
identified as such, avoiding an unverified claim that every locator carries
unchanged to the published version. The 2024-public-source and final-book
gap is stated in the introduction and final section, not hidden in an
auxiliary audit only.

## 6. Handoff boundaries

The manuscript maintains the admitted source-local theorem and its native
orbit-counting observable. It does not claim rational-prime ownership, a
target-zero identification, a self-adjoint target operator, a Route-B
construction, sharp logarithmic covering exponent, detector injectivity,
nonatomic Haar pushforward, or the nonhyperbolic interval classification as
new work. The provenance statement accurately calls the result an
AI-assisted internal draft with no invented human authorship or peer review.

Only this reviewer-owned file was written. No author-owned proof, manuscript,
evaluation, registry, build product, or sealed earlier-round artifact was
edited. The coordinator may proceed to final build and PDF QA for this
mathematical snapshot. Later source changes require affected-file review
and updated hashes; successful compilation alone does not replace that
check or remove the final-book priority limitation.
