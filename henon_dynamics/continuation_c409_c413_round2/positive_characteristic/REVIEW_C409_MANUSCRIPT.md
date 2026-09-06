# Independent full-manuscript review: C409

Date: 2026-09-06. Reviewer: current-team non-author agent responsible for the
positive-characteristic branch. This is a new review of the actual C409
manuscript, not a reuse of the frozen proof review, a self-review, a formal
Route-A score, or an external peer-review certificate.

## Disposition

**The mathematical statements survive this review. Two small manuscript
repairs are requested: one exact source locator and one introductory
quantifier.** I found no counterexample or unresolved proof gap in the
active-fibre dichotomy, its meromorphic conclusion, the stated FAD corollary,
or the realized nonhyperbolic wild example. Neither requested repair changes
a theorem, requires new experiments, or authorizes changes to frozen inputs.

The admitted difference remains the exact complex-coefficient active-fibre
criterion and its genuinely wild multiple-phase application. The no-wild
deduction, classical FAD framework, and Fourier-to-boundary principle remain
credited to their earlier sources. This is an assessment against the stated
inspected-version boundary, not a worldwide priority certification.

## Actual reading and artifact boundary

I read `main.tex`, all seven complete section sources, `references.bib`,
`PAPER_PLAN.md`, `CITATION_METADATA.md`, and `BUILD_REPORT.md` in
`../papers/C409_wild_fad/`. I also read the 11-page PDF text, including a
separate extraction of page 6 to recover a truncated combined extraction.
The compiled document contains Theorem 2.2, Lemmas 3.1/4.1/4.2, Corollary 5.1,
the complete example and the seven-entry bibliography. It is not a skeleton
whose mathematical content exists only in a separate proof package.

Comparison inputs read in full were the frozen
`research_c409_c413/arithmetic/PROOF_PACKAGE.md`, `REALIZED_EXAMPLE.md`,
`POSTCLASSICAL_DELTA.md`, `SOURCE_AUDIT.md`, and the root's
`REVIEW_ARITHMETIC_ROOT.md`. This review did not alter those inputs, rerun an
old census, create a new experiment, rebuild the author's PDF, or change Git,
registries, ledgers or formal evaluations. The coordinator owns final clean
builds and all-page visual QA. PDF text reading is not a claim of that visual
or deterministic-build certification.

## Requested repairs

### R1. Cite both realizability propositions in the no-wild deduction

At `sections/05_dynamics.tex:129`, the draft attributes integrality of $c$
and rationality of $r_n$ and $p^{s_{p,n}}$ to Proposition 10.2.1 alone.
The actual inspected source separates them: Proposition 10.2.1 gives the
first conclusion; Proposition 10.2.2 gives the other two when the wild
exponents are integral. That hypothesis is satisfied when every $t_{p,n}=0$.
These are on printed pages 97–99, PDF pages 107–109 (one-based), of
[BCH arXiv:2209.00085v2](https://arxiv.org/pdf/2209.00085v2).

The minimal repair is `\citep[Propositions 10.2.1--10.2.2]{bch2024}`.
Update the manuscript's `CITATION_METADATA.md` locator list as well. The
claim is correct with those two inputs; this is an attribution/locator
repair, not a failure of the BHN deduction. The inherited frozen audit's
abbreviated locator does not justify reproducing it in the final paper;
leave that historical input immutable.

### R2. Match the introductory conductor quantifier to the proved one

At `sections/01_introduction.tex:35`, the phrase “at each sufficiently high
conductor” is stronger than the conductor assertion explicitly established
by Lemmas 4.1–4.2. The proof establishes an unbounded sequence of supported
conductors, and constructs a full nonzero grid at each chosen supported
conductor. That is entirely sufficient for density.

Replace the phrase by, for example, “along an unbounded sequence of
conductors” or “at each sufficiently high conductor occurring in the nonzero
support”. I am not asserting that the stronger statement is false for this
kernel class; it is an unnecessary additional assertion not proved by the
present argument. The abstract and the two lemmas already use the needed,
correct quantifier. No additional conductor theorem should be added merely
to preserve an introductory phrase.

## Proof audit

### Exact coefficient class and the inactive alternative

The finite prime set, finite unit-modulus phase sum, periodic complex
$r_n$, and periodic nonnegative real exponent pairs are all stated. The
abstract theorem does not silently assume realizability, algebraicity,
positive coefficients, own-prime-coprime periods, or a Diophantine condition.
The active kernel extends continuously by zero at the origin; the inactive
kernel is one. Empty prime sets, empty phase sums and zero periodic weights
are allowed consistently.

Phase classes are taken modulo root-of-unity ratios before testing the
weights. The residue condition $a=0\pmod{p^{v_p(W)}}$ detects precisely the
fibres on which the valuation can be unbounded. Enlarging $W$ does not change
the condition: the lifting congruence is compatible with the old residue,
and the grouped weights and exponent pairs retain their old values.

If AF fails, every active factor on a nonzero grouped fibre has a fixed
valuation strictly below $v_p(W)$; thus the fibre value is constant. The
finite residue-class geometric sum (17) follows, including the zero series.
Example 2.3 is an exact control for torsion masking: its even-residue weight
vanishes, while its odd-residue kernel equals one, giving $2z/(1-z^2)$.
It rules out the invalid inference that separate natural boundaries must
survive addition.

### Fourier norm and actual aggregation

The CRT description (7) is the closure of the diagonal integers, with the
finite coordinate retained. The strictly positive telescoping differences
of each active radial sequence are summable. Each ball indicator has
Fourier norm one, so the local norm bound at most two is valid, also for
arbitrary nonnegative real exponents. The finite residue sum, finite prime
product, restriction to $D$, and collection of equal characters preserve
absolute summability. The subsequent Haar-orthogonality argument identifies
the collected coefficients with genuine Fourier coefficients.

This uses the displayed monotone radial kernels, not an unsupported
absolute-Fourier theorem for general continuous functions. Evaluation at
$g_0$ is injective because its integer multiples are dense. All characters
in the expansion are finite-order restrictions. Distinct phase classes
therefore cannot collide after multiplying those character values by
$\rho_C$. Formula (15) is the actual finite-total-variation measure, not a
formal sum whose apparent atoms may still cancel.

### Unbounded conductor, grids and meromorphic obstruction

On an AF witness fibre, fixing nonzero values of the other local coordinates
leaves a nonzero scalar times an active $p$-kernel. Its values at zero and
$p^K$ differ for every $K\geq\nu_p$. If every supported character were
trivial on the stated subgroup, the uniformly convergent expansion would
make those values equal. Thus actual nonzero support has unbounded
$p$-conductor; no unproved lower bound on the sizes of those coefficients
is required.

For $\kappa=\max(1,\nu_p)$, multiplication by
$v\equiv1\pmod{p^\kappa}$ preserves the compatibility group, its Haar
measure and the radial function. It consequently preserves the actual
Fourier coefficient. A primitive numerator at conductor $p^k$ produces
exactly the full rotated grid of order $p^{k-\kappa}$ in (14). This also
covers $p=2$ and $p\nmid W$. The grid points are distinct by evaluation
injectivity. Unbounded grid orders, not merely an infinite frequency set,
give density.

The bound preceding the radial limit is valid uniformly against the total
variation measure. Dominated convergence extracts exactly the individual
atom, even for complex masses and even when the chosen point is not an
atom. Nonzero atoms prohibit a locally bounded holomorphic extension. A
meromorphic continuation on any boundary neighborhood would have poles at
a dense subset of its enclosed arc, contradicting discreteness. This
establishes the stated local meromorphic natural boundary, not merely a
failure of one proposed global continuation.

### Realized FAD corollary

Nonzero realizability is used correctly to exclude root-of-unity
eigenvalues: a positive $f_m$ forces a positive count at every multiple of
$m$, which contradicts determinant vanishing at multiples of the torsion
order. The normalized dominant determinant factor is strictly positive at
every positive integer, not just nonnegative or positive on a generic set.
Pairing conjugate unit eigenvalues proves that assertion and permits
grouping any coincident phases afterward.

The own-prime coprimality of the exponent period is exactly what makes the
CRT conditions in the proof compatible. If every $b_C(a)$ vanished at the
chosen active residue, the positive leading sequence would vanish on the
whole associated progression. Therefore AF holds in at least one class.
No positivity is imposed on every individual Fourier coefficient.

The local factors and periodic multiplier are bounded, so the subdominant
error has a genuinely larger analytic disc and cannot change a nonzero
radial mass. The logarithmic derivative transfer handles meromorphic
continuation of $\zeta_f$ by first avoiding its discrete zero/pole set. It
does not mistakenly assume the continued zeta is everywhere nonvanishing.
Counting entropy, rather than an unproved topological entropy identity, is
the entropy used throughout.

### Classical no-wild deduction and the example

After R1's locator repair, rationality and the $O(\log n)$ height bound of
$g(n)$ are justified. For nonempty $S$, the displayed $d_k$ grow strictly;
good residue classes fix every valuation and have density tending to one.
For the harmless empty-$S$ edge case, $g$ is already periodic (use growing
multiples of $W$ if an explicit increasing sequence of moduli is desired).
The positive essential determinant part establishes stability on every
progression. These checks match Definition 2.11 and Theorem 2.14 of
[BHN arXiv:2307.07910v1](https://arxiv.org/pdf/2307.07910v1).
Thus the no-wild conclusion really is a classical deduction and is not
silently retained as a second contribution.

The quartic companion matrix, mod-two irreducibility test, reciprocal-root
calculation, toral lattice-index count and nontorsion unit pair are correct.
For $U=1+\Phi$, the least nonzero Frobenius exponent is $p^{v_p(n)}$.
Factoring the corresponding ordinary inseparable power leaves a separable
polynomial of degree $p^{n-p^{v_p(n)}}$, so the stated count is the number
of distinct roots, not the polynomial's total degree. The product is an
actual confined set map and has the three claimed dominant roots in
different torsion-ratio classes; no iterate collapses them.

The height obstruction at $n=p^a$ and the obstruction after moving $p^n$
into the perturbation are exact. The embedding $\lambda\mapsto\lambda^{-1}$
fixes the integer counts and multiplies the normalized coefficient by
$\lambda^{2n}$. On $n=1\pmod p$, irrational rotation gives the required
subsequence bounded away from cancellation. Thus the conjugated radius is
$\lambda^{-2}<1$, violating the all-embeddings hypothesis actually stated
in Theorems 1.2/1.6 of
[BGNS arXiv:2206.00862v1](https://arxiv.org/pdf/2206.00862v1).
The manuscript correctly treats these as failed sufficient hypotheses,
not proofs of worldwide novelty or impossibility of every other method.

## Citation and version boundary

I reopened the actual BCH v2, BHN v1 and BGNS v1 source texts at the
relevant definitions/theorems, including the two distinct realizability
propositions responsible for R1. I also checked the corresponding
finite-place/unique-dominance locators in the
[Bell–Miles–Ward accepted manuscript](https://shura.shu.ac.uk/17223/1/Miles-TowardsaPoly-CarlsonDichotomy%28AM%29.pdf)
and the [Byszewski–Cornelissen publisher PDF](https://msp.org/ant/2018/12-9/ant-v12-n9-p06-p.pdf),
and the FAD phase treatment in Section 4 of
[Cornelissen–Park v2](https://arxiv.org/pdf/2605.24504v2).
Knill–Lesieutre's actual revised Proposition 2.2 and adjacent remarks were
read from the existing downloaded primary text after the browser's fresh
request failed; the primary locator remains the
[author-hosted revised manuscript](https://people.math.harvard.edu/~knill/kam/papers/denjoy_revised.pdf).

The paper credits those analytic precedents and the recent Fourier
near-owner without claiming their conclusions are identical to Theorem 2.2.
The bibliography correctly keeps Royals and Ward as appendix authors, not
main-article coauthors. Journal metadata for BHN is not represented as a
full comparison with the final publisher text, and an inaccessible final
EMS book is not represented as read. This review preserves those limits;
it did not conduct a new global novelty search or obtain missing final
texts. The theorem itself does not depend on a negative literature claim.

## Build observations and reviewed hashes

Read-only searches in the current `main.log` and `main.blg` found no
Warning, undefined-reference/citation, multiply-defined-label, overfull or
underfull match. `pdfinfo` reports 11 pages, 326636 bytes, letter size and
blank Author metadata. These observations agree with the author report;
they do not replace the coordinator's final two-directory build and visual
checks after R1–R2.

The reviewed snapshot hashes are:

```text
9fc2031fd6186f8f890d901175fbc7f8129775ddfabd4141869b756bb425f186  main.tex
4590f84523255ad3aa345edcae4ae84f22c9fea5a6df602abb1d65a4f0603bbe  main.pdf
f45cb625f171cabc3b862ebd5512befa6599b174fa50ea57b77709e3e110c053  references.bib
4a1bbf3d595b75b0f3aaa610df417b7bdb767d6b80dea4621230d4f5497a5612  sections/01_introduction.tex
4d44c26052f0a776d68f2e23c59754b1188701365237064f23de5561d010ab4c  sections/02_criterion.tex
4512b2e21ef0448ced5051a8f00f8bd589ebe6841c6a635d436d0f78d7216509  sections/03_fourier.tex
5ae51a430be6f53ba3b6f18290bde9c3fb7d9819f920f8ccf4a123c289e0ff84  sections/04_boundary.tex
f4293622a00d6a9ed6e1778f6b8fe52f4e6b9c10d5bcffbc7852f5717d885d42  sections/05_dynamics.tex
5de7d480e79633c3c27e8650d8d300e379e7d3de6648b51cc6b01389ae3259fe  sections/06_example.tex
a2e68002981632e96c2887d7892e01c69f9a7ddc950828a22959246c0ce5e90d  sections/07_scope.tex
```

Final internal disposition: retain the complete theorem package after the
two narrow manuscript repairs and the already scheduled release checks.
No target Euler-factor, root-number, zero/divisor or Hilbert–Polya conclusion
is established by this manuscript.

## Affected-passage confirmation after R1–R2 (2026-09-06)

I read the actual revised introduction and no-wild subsection, the updated
`CITATION_METADATA.md`, `REVISION_NOTES.md`, and the appended build receipt.
I also checked the affected prose in the rebuilt PDF text and verified the
three revised hashes below. This is a targeted follow-up to the complete
review above, not a second claimed full review or a final visual certificate.

R1 is resolved: Proposition 10.2.1 is cited for $c$-integrality, Proposition
10.2.2 for the rational values, and the latter's integer-wild hypothesis is
explicitly satisfied by $t=0$. The added empty-$S$ sentence correctly handles
the already-periodic case. The provenance supplement distinguishes the
author's new primary-text reading from the immutable old audit.

R2 is resolved: the introduction now specifies an unbounded sequence of
conductors in the nonzero Fourier support, with a common nonzero coefficient
on each resulting grid. It does not add an unproved all-conductor assertion.
Neither repair changes the accepted mathematical statements or their proof.
Read-only searches of the revised log and bibliography log again found none
of the warning/undefined/overfull/underfull/multiply-defined patterns.

```text
9331b86c333f1511d17327f8a9feec1c49ae164e638c2d64ec8964406b97ffc4  sections/01_introduction.tex
c928ffb04b0ddd6c09196a091ce9d1fd19f34924583e76b519566fc54ee9e8c8  sections/05_dynamics.tex
cd39541113b917b391dabdc37b24335f5c439b5578ca4c3456b32a059fa17c7c  main.pdf
```

There is no remaining requested mathematical or source-locator repair from
this reviewer. The coordinator's final deterministic builds, all-page
visual QA and formal evaluation remain separate release tasks.
