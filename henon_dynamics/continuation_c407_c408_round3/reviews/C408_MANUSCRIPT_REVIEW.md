# C408 nonauthor full-manuscript and actual-citation review

2026-09-06. Reviewer: current-team root coordinator, not the theorem or
manuscript author. Status: **PASS_AFTER_TWO_LEMMA_HYPOTHESIS_CLARIFICATIONS**.
This is an internal mathematical/editorial check, not human peer review,
formal verification, or a publication-priority certificate.

## Actual reviewed text and disposition

The coordinator read all eleven TeX inputs: main, macros, references and
all eight section files, including the complete proofs, both generating-
function conventions, finite controls and scope discussion. The accepted
input set is [SOURCE_INPUTS.sha256](../cluster_boundary/paper/final_build/SOURCE_INPUTS.sha256),
relative to `cluster_boundary/paper/`, SHA-256
`d4e34d0621b8fdcd4d7de4cb58f2156d58c0ee71aba1d2eb31467cdb14052632`.
`sha256sum -c` on those eleven actual inputs returned exit 0, all OK.
The accepted seven-section outline was also read in full before completion.

The stand-alone manuscript preserves the admitted theorem for all odd
k>=3 and every m>=1, and does not omit the difficult cancelled path or
two-dimensional cycle calculation. No remaining mathematical, citation or
scope issue requires revision. Final dual-build byte comparison, font/text
checks and all-page visual QA remain separate release gates; the author's
clean 12-page draft is not counted as those completed gates by this review.

## Proof comparison and attempted failures

- The elementary Groebner finiteness argument uses k>2 and gives the
  literal small-clock equations. Alternating phases and permitted roots
  are classified without counting them as exact-period orbits.
- The implicit root elimination and logarithm replace equations by unit
  multiples, not only by equations with the same reduced zero set. Loop
  and double-edge derivatives are counted twice exactly where needed.
- The nonradical product-generator lemma uses proper parameter ideals and
  a one-dimensional Cohen--Macaulay quotient. The exact sequence's map
  is multiplication by the nonzerodivisor b. Tensor-factor lengths and
  the later finite-colength verification are not circular.
- The path complement is nondegenerate for the specified bilinear form.
  In the cancelled case the first correction solves the endpoint
  equations, the full residual has order at least k+1, and the potential
  error is at least 2k+2. Direct paired-series substitution gives the
  nonzero coefficients `r(k^2-1)/2` and `-23r`, not a fitted rule.
- Every 4r-cycle really reduces to r times the four-cycle by symmetry and
  uniqueness of the complementary solution. The separate sign symmetries
  are graph reflections, not an assumed sign symmetry of an odd unary
  term. The mixed coefficients 1/-8 and pure-axis coefficients
  `(k^2-2)/4`/-5 are computed in the body, including the cubic correction.
- Formal inversion of `(W_A,W_B)` gives the ideal `(A,B)` before square
  substitution. The four finite intersections have lengths
  `1,2k-2,2k-2,4`, proving `4k+1` without a hidden Newton-nondegeneracy
  condition. The earlier factor-splitting lemma then closes the full sum.
- The labeled marked-separator identity does not divide by orbit size or
  overlook rotational stabilizers. The proper-subset subtraction is
  `4*1_(4|m)` and the full-cycle correction gives the stated quartic
  determinant. The native-clock parity exponents reproduce `b_(2m)/(2m)`.
- The additional scope identity in Section 7 follows by multiplying the
  relations at i-1 and i+1 and substituting the relation at i. Its quotient
  is polynomial, and its unit-bracket conclusion is local. It does not
  claim the unclassified zero patterns are absent.

The six direct original-equation controls and bounded symbolic checks
match the stated receipts. The terminated k=3,m=4 computation remains
explicitly uncompleted. No finite check substitutes for any of the above
all-parameter reasoning, and no unchanged mathematical code was rerun
merely to repeat its earlier PASS.

## Closed findings and affected checks

1. **General elimination lemma, MINOR statement defect.** A specification
   of the quadratic part alone permits a nonzero linear term, in which
   case a complementary solution vanishing at zero need not exist. The
   author added `dP(0)=0`. The coordinator reread the resulting statement
   and proof: the formal implicit and Taylor estimates now follow with
   their stated hypotheses. All actual potentials already satisfied this
   condition, so the theorem and coefficient calculations did not change.
2. **General product-splitting lemma, MINOR proof-domain precision.** The
   supplied parameter-sequence proof needs the factors in the maximal
   ideal; merely writing them in R allowed unit-factor cases not addressed
   by that proof. The author added the maximal-ideal hypothesis. It holds
   for every coordinate and gradient factor used here. The affected
   proper-ideal/CM/length proof was reread and is closed.
3. **Transient source control byte, editorial.** The initial formal-model
   file contained a NUL immediately before one `partial` command. It was
   removed before the accepted build; the coordinator reread that line.
   The final control-byte scan belongs to the build record, not a theorem
   modification.

The first draft also exposed two long-filename overfull boxes. The author's
replacement of those literal typewriter commands by breakable path commands
was inspected; it changed presentation only. The accepted-draft `main.log`
had no matches for the case-sensitive Warning/Overfull/Underfull/undefined/
Error/Fatal/Missing-character pattern (rg exit 1, meaning no match).

## Every actual citation and reading boundary

Only three entries occur, all cited in their actual relevant contexts:

| Key | Actual primary material checked by this reviewer | Supported use, and what is not inferred |
|---|---|---|
| BM | Beyer–Muller, arXiv:2403.15589v1, entire Section 4; arXiv metadata and the Oxford journal article record for IMRN 2025(4), rnaf027, DOI 10.1093/imrn/rnaf027 | Known alternating deep support is deducted. Manuscript locators explicitly refer to arXiv v1, not the differently numbered published revision. No cyclic-algebra thickness theorem is attributed to this source. |
| BFMS | Benito–Faber–Mourtada–Schober, arXiv:2401.06758v2, entire Section 5 with Theorem 5.2.3 and proof; version metadata and DOI linkage | Ambient rank-two characteristic-zero smoothness only. It does not identify the nonreduced cyclic algebra with a surface fixed scheme. |
| GKQR | Grigorev–Kalidindi–Quintero Santander–Roeder, arXiv:2607.08125v2, metadata, abstract and introductory defining maps/equation (1) and nearby context | The equal-exponent mutation composition is exactly F_k squared. Broader stable-model/entropy proofs were not newly audited or used as proof inputs. |

The BM DOI redirect could not be opened directly in the browser, so the
actual Oxford article record was retrieved through a publisher-domain
search; its title, authors, issue, article ID and DOI agree. Primary links:
[BM journal](https://academic.oup.com/imrn/article/2025/4/rnaf027/8020560),
[BM inspected version](https://arxiv.org/html/2403.15589v1#S4),
[BFMS inspected version](https://arxiv.org/html/2401.06758v2#S5),
[GKQR inspected version](https://arxiv.org/html/2607.08125v2).
No uncited filler entries, fabricated human identity, unread proof
dependency or unqualified worldwide priority assertion was found.

## Final scope check

The abstract, theorem, formal model, conclusion and references all preserve
the unsaturated cyclic-relation object. Its embedding dimension m for
m>=3 is explicitly incompatible with the fixed subscheme of an
endomorphism of a smooth surface. The author does not transfer a torus
quantization, ordinary Artin–Mazur product or full boundary count to it.
Even k, positive characteristic and other zero-support patterns remain
outside scope. The strong source theorem does not promote the C408
Route-A tuple, whose five target layers remain FAIL.

Proceed to final reproducible build and all-page QA of these accepted
inputs. No further mathematical rewrite or unmotivated additional review
round is required by the findings above.
