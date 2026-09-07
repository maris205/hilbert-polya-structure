# C415 nonauthor manuscript review

Reviewer: current-team coordinator `root`, not the manuscript author
`scout_charp_c414`. Date: 2026-09-07. This is internal AI-assisted
review, not human peer review or journal approval. Root contributed
to the earlier proposed generalization; the separate full research
proof/source review by `scout_henon_arithmetic` remains the independent
admission evidence. The present review checks the new author's actual
complete article and does not relabel that earlier contribution as
new independent proof authorship.

**Mathematics and manuscript completeness: PASS. One minor final-sentence
precision correction requested before closure.** No missing quantifier,
ordinary-count reduction, fractional-tail gap, source misattribution or
blocking analytic issue was found. R1 below concerns only the phrase
describing the perfected ring, not the theorem or its proof.

## Actual reviewed inputs

Read completely: main.tex, math_commands.tex, references.bib, all nine
section files including abstract, CITATION_AUDIT.md, AUTHOR_HANDOFF.md,
and the actual eleven-page PDF extracted with `pdftotext -layout`.
The source/bib/PDF hashes were checked against the author handoff.
The reviewed PDF SHA256 is
`05a1218006fec9142d7a1387dce44c53cb17ee4976fb99f3bd3d235070a3ea1f`.
The main TeX hash is
`1cf7305d705045cdc75bd75a62071b59f1e574edb8ed20fcaf7dee085cec9bab`.

Also read in full for comparison: FULL_DEGREE_2P_PROOF.md,
PROOF_NOTE.md, the final REVIEW_CHARP_PROOF.md including its affected
root-order/source closure, and the actual C404 PROOF_PACKAGE.md.
The current full degree-2p proof is the previously admitted input,
not the original source-note header's historical pending status.

Fresh primary read-only checks covered Bridy's Numdam metadata/abstract
and displayed BibTeX, the complete Stacks Tag 0CC8 statement and its short
proof reference, the BCH arXiv v2 metadata/abstract, and the Springer
Cox–Little–O'Shea fourth-edition metadata/table-of-contents blocks.
No full 176-page BCH reading or full textbook reading is claimed.
The current review ran no mathematical script, parameter census,
author build, old batch build or external-model API.

## 1. One exact object, one clock and every coefficient

The abstract, equations (1.1)–(1.2), Theorem 1.1 and Section 8 agree:
odd p, q=p^e with e>=3, all g of degree exactly 2p over F_q, a nonzero
constant determinant, geometric affine-plane points and positive ordinary
iteration of S=H^-1 Phi_q. The symbol w is p^{v_p(n)}, not v_p(n).
The lower coefficients and the possible zero y^{p+1} coefficient are
not silently restricted to the prime field or a sparse face.

The high branch is precisely the existence of support in [p+2,2p-1].
Taking its largest exponent leaves no untracked term between ell and
2p, because no multiple of p lies there. Its complement has exactly
the displayed low form. These alternatives are disjoint and exhaustive.
The degree-six numerical values in Example 8.1 are substitutions into
the theorem, not evidence offered in place of these quantifiers.

## 2. Fixed equations, length and reduced ordinary counts

Section 2 gives the actual inverse and S coordinates. Coefficients
fixed by q-Frobenius ensure commutation. Composing both equalizer maps
with H^n preserves their ideal, with H^-n giving the reverse ideal
inclusion; this is a scheme statement rather than a set-only equivalence.
The difference delta is an additive operator, never a polynomial point
map or ring homomorphism.

In Proposition 3.1 the commuting characteristic-p binomial identity
uses w, then s=n/w nonzero in F_q. Both original substitutions preserve
the coefficient and multiply the degree of a unique pure top term by q.
Lower total-degree monomials cannot tie that term. The second fixed
equation therefore has actual top degree q^{n-w}D_w; the first has
top monomial -x^{q^n}, also at n=1.

The displayed S-polynomial representation F_0G-G_0F has terms strictly
below the least common multiple in the graded order, so the coprime
leading-monomial criterion applies. The rectangular monomial basis
proves finite length q^{2n-w}D_w and no hidden infinity contribution.
The Jacobian is DH^n with determinant a^n, not the derivative of an
auxiliary perfected operator. Independent linear parts annihilate the
quotient's cotangent space, and Nakayama reduces each local Artinian
algebra to K. Thus the length is the ordinary point count. No scheme
multiplicity or radicial fiber degree is substituted for it.

## 3. Both complete degree inductions

Section 4 reproduces the first-index lemma and the entire strict-gap
induction. The worst high-support margin remains positive at q=p^3,
p=3. A_j is zero or q-divisible, making v_p(A_j+2p)=1 and
A_j+ell nonzero modulo p. The second monomial's index-one term
regenerates both retained positions; all its later indices, the first
monomial's index-p term and the full mixed remainder fall strictly
below the second retained degree. The degree and nonzero coefficient
recurrences therefore hold for every j and every allowed coefficient.

Sections 5–6 retain the essential extra work in the low branch:

- The concrete perfected ring contains finite expressions at finite
  denominator levels, with injective ordinary-ring inclusion.
- Frobenius commutation gives delta^j=L^j Dcal^j, while the coefficient
  action is sigma-semilinear. No F_q-linearity shortcut is made.
- The mixed-monomial estimate is uniform over denominator levels and
  x/y support, so omitted terms need not remain univariate.
- For E congruent to 2 modulo p, the retained exponents are E' and
  E'-(p-1)/p. The exceptional fractional exponent has numerator
  p(E-1)+1 and its exact image degree is E'-2+2/p < E'-1.
  The finite expansion is correctly taken in the perfected ring,
  even when v_0 itself has fractional exponents.
- The old remainder goes to degree at most E'-2. Consequently only
  the leading term determines both new retained coefficients;
  vanishing C causes no division or missing case.
- Raising the jth state to p^j returns an ordinary polynomial.
  Both the secondary exponent and the whole tail stay below the
  unique top term. The resulting c_{j+1}=2b^{p^j}c_j correctly
  includes every coefficient Frobenius twist.

The displayed closed degrees are integers by their recurrences, not
field divisions. Their strict inequalities 0<D_j<q^j are proved
before Proposition 3.1 is applied. No infinite-parameter statement
rests on the old finite diagnostics.

## 4. Analytic corollary, ownership and clarity

The normalization in Section 7 is A+B_0 theta=2p/q; it does not
incorrectly reuse C404's A+B=1. The telescoping expansion is absolutely
interchanged on compact subdisks, and the positive exponents are
summable. Primitive root order is indexed by r>=1, distinct from the
determinant and w. This excludes the initial (1-u) factor's singular
point. Dominated radial logarithmic orders give positive tails tending
to zero, so every fixed positive integral power has noninteger orders
at a dense set of high-order roots. The claimed meromorphic boundary,
exact radius and transcendence follow.

The article credits C404's conversion and analytic mechanism and
does not split the high branch, pure face, degree-six example or zeta
corollary into further papers. Bridy's projective-line dynamically
affine scope and BCH's smooth-group/FAD framework are represented only
at their accessed level. Stacks is cited for universal homeomorphism,
not for finiteness of arbitrary Frobenius. The specific finite-plane
map and finite reduced equalizers are proved directly. The textbook
reference supplies framework attribution, with the actual special
Gröbner argument included. Bibliography entries resolve in the PDF.

The author correctly omitted C405: its actual critical-divisor topic
is not a dependency. The coordinator accepts the correction to the
outline's tentative C404/C405 citation line; it changes no contract,
theorem or proof. The resulting article follows its claim/evidence
map and has no artificial experiment or incomplete proof appendix.

## R1 — finite expressions, not a finite ring

Location: `sections/8_scope.tex`, final paragraph. The phrase
“The perfected ring is a finite algebraic device” is ambiguous because
the ring itself is an infinite union and is not finite or finitely
generated as an F_q-algebra. Section 5 defines it correctly, so this
is a local summary precision issue, not a mathematical gap.

Minimum requested change: say that the perfected-ring calculation
uses only finite algebraic expressions, with each iterate at a finite
denominator level. Preserve the theorem, all equations and the clock.
No mathematical script or full proof re-review is needed. After the
author changes that sentence, this reviewer will read it and the
affected PDF paragraph to close the finding. Final deterministic
double builds and every-page visual checks remain coordinator gates.

## R1 affected closure — PASS / CLOSED

On 7 September 2026 the same nonauthor manuscript reviewer read the
revised final paragraph, the appended author revision receipt, and the
actual text of page 11 extracted from the updated `main.pdf`. The
sentence now says that the calculation uses only finite algebraic
expressions, each iterate at a finite denominator level; it no longer
describes the infinite perfected ring itself as finite. This resolves
R1 without changing the theorem or its proof.

The affected inputs were checked read-only against the author's receipt:

```text
fd8333304100cfb07c594bb6e5974ae98ea0537857e8410dd18f000a6d0b0e21  sections/8_scope.tex
f99a764cef94525d88acb427e9d89040a6ab2ba98c2c3b7ce7f72f79e94f20cf  main.pdf
```

The mathematical and completeness PASS above is unchanged. The actual
manuscript gate is now **PASS / CLOSED**, with no remaining required
repair. No mathematical script or full proof review was repeated for
this prose-only revision. Final double builds and every-page visual
inspection remain separate release gates.
