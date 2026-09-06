# Independent full-manuscript review: C412

2026-09-06. Reviewer: root coordinator, not the C412 manuscript author.
Decision: `MANUSCRIPT_PROOF_AND_SCOPED_CITATION_PASS`.
No required mathematical or citation repair was found in the actual complete
manuscript. This is internal non-author review, not human peer review,
worldwide priority certification, or final PDF release QA.

## Actual reading and fixed inputs

I read the entire current `main.tex`, `math_commands.tex`, nine included
section files (including every row of Appendix A), and `references.bib`,
then the complete `CITATION_AUDIT.md` and `AUTHOR_REPORT.md`. The proof
review below is of those actual manuscript files, not a relabelled copy
of the earlier research-proof review. The accepted original proof and
its independent complete-set receipts were subsequently consulted for
provenance and consistency, without rerunning them.

Entry points: [manuscript](papers/C412_integer_henon/main.tex),
[initial PDF](papers/C412_integer_henon/author_build/main.pdf),
[source audit](papers/C412_integer_henon/CITATION_AUDIT.md),
[author report](papers/C412_integer_henon/AUTHOR_REPORT.md), and
[sealed earlier proof review](../research_c409_c413/REVIEW_INTEGER_HENON_ROOT.md).
Actual PDF hash at review:
`4974c90cd98a0529d00baf16a47b789fdba3ac37d9be432d2e8a2c3e6a8f7659`.
This receipt does not claim visual inspection of all fourteen PDF pages;
that remains a final-build task.

## Claim and proof audit

The exact object is `H_(a,b)(x,y)=(y,y^2+b y+a-x)`, all `a,b in Z`,
acting on rational pairs with ordinary time. The main theorem covers every
period and coefficient pair, lists every point by cyclic words, and proves
the sharp eight-point bound. Monicity, integrality and Jacobian `+1`
are explicit; no rational-coefficient or opposite-sign conjecture is claimed.

1. **Integrality and conjugacy.** At any p-adic coordinate maximum above
   one, the monic square term has strictly larger norm than both lower
   terms and the neighbouring sum. This excludes every denominator without
   assuming nonzero coordinates or a bounded period. Direct substitution
   verifies `b=2q+e`, `A=a-q^2+(2-e)q`; the conjugacy adds `q`, and
   the original coordinates subtract `q`. Both directions preserve the
   original clock and integer/rational domains.
2. **Upper parameters and centers.** Both cyclic square-sum identities
   are correct. They exclude the stated upper parameter ranges and identify
   the equality cases. The odd recurrence center is `x+1/2`, with
   `c=-A-3/4`; the summation center is separately `x-1/2`. The manuscript
   explicitly prevents their signs from being interchanged. At a real
   maximum, `(R-1)^2<=1+c` and the pointwise residual bound follow exactly.
3. **Two infinite parameter branches.** The integer intervals beginning
   at `c=13` and the odd intervals beginning at `A=-17` are disjoint and
   adjacent. In each case the two rounding regimes `s<=-2` and `s>=-1`
   yield the stated upper bound on `R`; a coordinate of modulus at most
   `r-2` violates the residual bound. The strict inequalities hold already
   at `r=4` and `r=9/2`. The six-symbol representations are unique.
4. **Exact coefficient separation.** The multiplier of `r` is even.
   The right side lies in `[-r-2,r+2]` for integer centers and
   `[-r-3/2,r+5/2]` for half-integer centers, strictly within
   `(-2r,2r)`. Hence both sides vanish exactly. This is not an asymptotic
   leading-term argument. The same two local equations legitimately apply
   to both parity branches.
5. **No hidden period cutoff.** All six possible offset parameters
   `s=-2,-1,0,1,2,3` are explicitly resolved. Forbidden adjacent offsets
   `1,-1` also apply across a cyclic boundary of length one or two.
   The surviving constant, four-, three-, and alternating two-letter
   patterns exhaust arbitrary cyclic solutions. Both signed three-cycles
   and their exact ordinary periods are retained.
6. **Existence and endpoints.** Every table word is verified directly
   in the centered recurrence, independently of the large-parameter
   thresholds. The even three-cycles coincide only at `k=0`; the odd
   second three-cycle becomes a fixed point precisely at `k=0` and is
   correctly excluded from that row. The two-/four-cycle index ranges
   exclude constant degeneracies. Repeated coordinates cause no missed case.
7. **Complete finite complement.** The finite-pruning lemma is valid
   for an injective map once all periodic points lie in its finite starting
   set. Both alphabets contain every possible periodic coordinate by the
   proved bound; the doubled odd map preserves odd integers and is injective.
   All thirteen even and seventeen odd rows specify complete stable pair
   sets via cyclic words, not merely numbers. The explicit algorithm and
   word expansion make each row checkable. The separately described
   whole-box transitive-closure method matches the genuine prior independent
   receipts. Those inputs have not changed; no old census was rerun.
8. **All intersections and sharpness.** Difference-of-squares factorization
   yields only even-branch overlaps `A=-1,-4`; the first has seven points.
   Pronic differences 2 and 4 yield exactly odd overlaps `A=-2,-4,-6`,
   with counts 5,8,4. The odd four-cycle family has odd negative parameter
   while the other families have even negative parameter. These facts
   exclude further overlaps or a hidden triple overlap. At `A=-4,e=1`,
   the three displayed words have lengths 2,3,3 and give eight distinct
   points. Translation gives exactly the announced two-parameter locus.
9. **Returns and scope.** Each d-cycle contributes d points iff d divides
   n. The finite rational-point orbit product has the correct exponents
   and formal/analytic domain. It is not a count of all algebraic fixed
   points or a scheme length. No target arithmetic or operator follows.

The complete point words in Appendix A agree with the two main tables and
with the accepted original complete-set receipts. The intermediate pruning
cardinalities are supplementary to the reproduced explicit finite procedure
and full stable sets; they are not used as an unsupported infinite extrapolation.

## Independent primary-source reading for the actual citations

- [Pezda 2002 original journal record](https://dml.cz/handle/10338.dmlcz/120574)
  and its linked original scan: after the browser PDF parser failed, I
  retrieved the actual linked PDF as a read-only stream and read the cover
  and printed pages 95–96. The definitions and Theorem 2.1 give the exact
  allowed integral-plane cycle lengths, with maximum 24. This correctly
  deducts a generic uniform period bound, not the present point tables.
- [Ingram actual arXiv v1](https://arxiv.org/pdf/1111.3609v1): I read the
  introductory statements through Conjecture 1.5 and Proposition 1.6.
  The map in that conjecture has the opposite determinant sign. The source
  also explicitly credits Silverman's prior arithmetic finiteness theorem.
  I use the recorded v1 text, not a claim to have read final-journal wording.
- [Kim–Krieger–Postolache–Szeto v2](https://arxiv.org/html/2412.01668v2):
  the introduction, Theorems A–B, and integer-valued polynomial description
  indeed concern determinant `+1` in growing odd degree. Rational
  coefficient integer-valued polynomials are not conflated with monic
  integral-coefficient quadratics. The actual version header is July 2025;
  the regenerated HTML date is not a replacement version date.
- [Hénon open problems, Section 11](https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html):
  I read the family definition, Question 46, and Conjectures 2–5, including
  the exact determinant-sign convention and finite-exception Jacobian
  quantifier. The manuscript neither proves nor refutes the latter by a
  fixed Jacobian-one result.
- [Silverman publisher record](https://link.springer.com/article/10.1007/BF02571713):
  title, author, volume, pages, date and DOI are verified, but subscription
  full text remains unavailable. Its general background attribution is
  independently supported by the actually read Ingram introduction. The
  manuscript explicitly discloses this access boundary and does not invent
  a theorem number or claim to have excluded all unread examples.

The five actual cited entries and their use are consistent with the
manuscript's bounded ownership claim. No bibliography padding, invented
publication, or uncited hidden mathematical dependency was found.
This does not exclude an unknown prior owner or establish global priority.

## Reviewed source identity and remaining gates

Selected actual SHA256 values:

```text
4a7e5b6023a9fcbf8a62917f22ae972fe44d26743669c22b93e4a7da54b471dd main.tex
39c2ebf5822412c61d5b043ccd08776865dbc106e8b25ba38719ca5c3e0ffa80 references.bib
b12b9f0dcc2364f1517f0e07050ef9ee6bbeb6abefce74e4ef4a9c1e942f0cb1 sections/2_normalization.tex
4a14d4f05bc1c7b6a0f5d94b3b55ec38f7fb7c77597e306e2d2ae8e419083478 sections/3_six_symbols.tex
f8c37d71e608b7ba36e69daed3a15547b8032d48c9d4326777c777e4fec57068 sections/4_local_classification.tex
5abecb90085d0e80429ae16a91f0068cff00cc9f8b53e6c83d38979cf8ad06ba sections/5_finite_complement.tex
aa8769164a104b0b1651481f16dc941cdee9eac9d1001b28a6a2905f66cce6fe sections/6_sharp_bound.tex
32b728900c6affdf0611ee6c0a6973d2a306c7126322b51974965dc02bd904e7 sections/A_certificates.tex
```

No manuscript revision is required by this review. The final deterministic
two-fresh-directory builds, PDF byte comparison, fonts/text/warnings checks,
all-page visual QA, formal evaluation consistency, payload sealing and Git
synchronization are still distinct release obligations. This receipt closes
only non-author full-manuscript mathematical and scoped citation review.
