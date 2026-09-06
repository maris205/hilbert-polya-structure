# Source ownership and scope audit

2026-09-06. Bounded primary-source reading, not an exhaustive priority
certification. The previous round's `wild_dynamics/SOURCE_AUDIT.md` and
`PROOF_PACKAGE.md` were read first and were not modified or rerun.

## Actually used primary sources

| ID | Source | Primary passage checked in this continuation | Owned input and limit |
|---|---|---|---|
| S1 | Jonas Nordqvist and Juan Rivera-Letelier, *Residue fixed point index and wildly ramified power series*, [arXiv:1904.04494](https://arxiv.org/pdf/1904.04494); published identity carried from the sealed audit: J. London Math. Soc. 102 (2020), 470–497, DOI 10.1112/jlms.12325 | Section 1.2, definition of the lower ramification numbers, iterative residue (1.5), Theorem 2, and its explicitly stated restriction to odd characteristic and initial number at most $p-1$ | Used only for the later-return tower when the first-return multiplicity is $p$. Does not determine that initial multiplicity, does not assert that every periodic point has it, and does not provide the orbit-product transfer theorem. |
| S2 | Jonas Nordqvist, *Wildly ramified power series with large multiplicity*, [arXiv:1909.10782](https://arxiv.org/pdf/1909.10782); published identity carried from the sealed audit: J. Number Theory 225 (2021), 174–197, DOI 10.1016/j.jnt.2021.01.019 | Definition 2.2, Proposition 2.5, Section 2.2, and the full statement of Theorem A; also the stated Sen identity when $p$ divides the initial lower ramification number | Used only after the initial multiplicity has been computed. The theorem's variable $q$ denotes multiplicity minus one; it is not our family exponent $q=p^s$. Our application uses initial number $pm-1>p$ and second residue $-(ac)^{-p}\ne0$. Sen's original article was not freshly read. |
| S3 | Andrew Bridy, *The Artin–Mazur zeta function of a dynamically affine rational map in positive characteristic*, [arXiv:1306.5267](https://arxiv.org/pdf/1306.5267); published identity carried from the sealed audit: J. Théor. Nombres Bordeaux 28 (2016), 301–324, DOI 10.5802/jtnb.941 | Introduction's ordinary-count conjecture and difficulty statement; Section 2, Definition 2.2 and the five-family classification discussion | The dynamically affine classification is established input. Our degree and critical-point computations exclude it for the stated exceptional family. The preprint's Conjecture 1.6 is not silently identified by the published article's numbering. No claim to solve that conjecture is made. |

These are the same established local/classification inputs whose publication
metadata were verified in the earlier sealed source audit. The current
continuation rechecked the relevant arXiv body statements; it does not
claim a new publisher-DOI verification pass or a new reading of their
entire articles.

## Additional primary source examined for possible ownership

Mikhail Ershov, *New just-infinite pro-p groups of finite width and
subgroups of the Nottingham group*, [author-hosted PDF](https://m-ershov.github.io/Research/nottf.pdf).
The title/abstract and selected portions of the subgroup discussion were
read, especially Section 8's diagonal subgroups of the form
$t\mapsto tA(t^{p^s})$ and the attribution there to Fesenko. The reading
also surfaced its centralizer calculations. No theorem from this paper
is used in the proof package. The source shows that sparse substitution
groups are established territory. It does not, in the passages read,
state the fixed-finite-field periodic-profile transfer theorem proved
here. That bounded observation is not a claim that the theorem is absent
from the whole Nottingham literature. We did not verify a journal DOI
or read every theorem in this author-hosted PDF.

The local forms $tA(t^q)$ and $(1+v)A(v^q)-1$ must not be silently
identified by a translation of arbitrary formal series: translation away
from the origin is not automatically a valid formal coordinate change.
Nor does their difference by itself establish novelty of the elementary
truncation calculation.

## Claim ownership matrix

| Claim in the new package | Prior owner / status | What is newly derived here |
|---|---|---|
| Ordinary and scheme-theoretic counts must be distinguished | Established; S3 and the prior sealed work | A new explicit failure in the exact previously open linear-$H$ family, at least period $12$ |
| First-return weight is always one for $x+x^{p+1}$, odd $p$ | Rejected | Exact $p=3$, degree-four field certificate, with multiplicity $12$ |
| Local return jet modulo $v^{q^2}$ | Elementary Frobenius and substitution algebra; possible broader sparse-group precedence | A precise product of normalized evaluations of $H$ along an arbitrary nonzero cycle, with leading coefficient and sharp precision |
| Full first-return profile over a fixed finite field for large exponent lifts | Finite-field graph stability itself is elementary | The uniform bound $q>\deg H(|K|-1)$ transfers one finite list of orbit polynomials to every exponent in an infinite congruence family |
| Every later return multiplicity | S1/S2 after the first return is known | Substitution of the newly computed initial multiplicity; no independent ownership claimed for general ramification theory |
| Infinite-degree exceptional family | The degree congruence alone is elementary | The same explicit cycle has first-return multiplicity $4\cdot3^{4j+1}$ for every $j\geq0$, with the low-exponent case independently certified |
| Ordinary full-period count over the algebraic closure | Still unproved | No replacement claim; the finite-field quantifier order is explicit |
| New weighted zeta or natural-boundary theorem | Not proposed | The old weighted theorem is not repackaged |

## Search scope and limitations

Searches included the exact polynomial notation, Bridy and non-affine
ordinary zeta counts, periodic-point multiplicity in positive
characteristic, logarithmic differentials, Frobenius exponent lifting,
and sparse Nottingham-group substitution. Many literal polynomial
queries returned unrelated material; these results are not counted as
support or as novelty clearance. No Zotero or Obsidian connection was
available. The local project paper-library/script lookup returned no
matching arXiv search helper, so the source search used primary web
bodies. No paper PDFs were saved or uploaded to an external model.

The source-supported assessment is deliberately narrower than a novelty
verdict: S1/S2 do not compute the first-return orbit product, while sparse
composition methods are plainly established. A non-author should assess
whether the uniform finite-field profile and the explicit non-affine
exceptional family make the elementary transfer lemma a substantial
standalone result or only a useful technical note.

## Admission self-assessment

**Original ordinary-count contract: reject.** It is false in the stated
linear-$H$ subfamily, and no complete ordinary-count substitute is
proved for one fixed non-affine polynomial on the algebraic closure.

**Replacement transfer contract: mathematically closed, scientifically
provisional.** It is stronger than a single counterexample or a renamed
weighted corollary: arbitrary fixed $H$, every finite field and exponent
residue, every nonzero cycle in that field, a uniform threshold, exact
leading coefficients, sharp jet precision, and an infinite family of
different degrees are covered. On the other hand, the core proof is a
short Frobenius calculation; all return towers are classical-input
corollaries, and the finite-field ordinary count adds no new difficulty.

Under the batch's requirement to select only the two most substantial
remaining contracts, I do **not** recommend automatic admission. This
is a defensible focused technical-note candidate pending non-author
source/substance review. If the arithmetic and geometry lines have
stronger independently closed theorems, this package should remain an
unnumbered research result rather than force a third or weaker paper.
No judgment here is a journal acceptance prediction or a universal
priority certificate.

The work is AI-assisted and internally reviewed, not human peer-reviewed.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains in force; no arithmetic local factor
or target-zero claim follows from these geometric local multiplicities.
