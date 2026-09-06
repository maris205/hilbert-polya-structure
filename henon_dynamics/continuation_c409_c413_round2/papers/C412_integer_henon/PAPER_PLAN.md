# Paper plan: C412

Date: 2026-09-06. Status: `BATCH_OUTLINE_FROZEN_DRAFTING_AUTHORIZED`.
This is a manuscript plan, not a completed paper or a new proof-admission
decision. The root coordinator has frozen the batch after its independent
outline review; manuscript drafting is now authorized.

## Contract and presentation

Working title: **Rational periodic points of monic integral conservative
Hénon maps**.

One-sentence contribution: We classify every rational periodic point of
every map
\[
H_{a,b}(x,y)=(y,y^2+by+a-x),\qquad a,b\in\mathbb Z,
\]
and obtain the sharp uniform bound of eight periodic points, with exact
periods restricted to \(1,2,3,4\).

The article answers one complete parameter-and-period classification
question. The even and odd normal forms are two branches of that same
question, not separate contributions or papers. The finite-orbit zeta
formula is a short consequence, not a second contract.

Format: English, anonymous `article`, 11pt, approximately one-inch margins;
no selected journal, conference template, hard page limit, or minimum length.
Use ordinary mathematical numbered citations and section-level source files.
The complete proof belongs in the article and its included appendix. An
internal proof-package link is provenance, not a substitute for a proof.

The current batch contract supersedes the writing skills' default ML venue,
nine-page limit, one-page related-work minimum, mandatory hero image, and
unavailable external reviewer. Their claim-evidence discipline, verified
citations, complete prose, reverse outline, and compilation checks remain
applicable. All edits use `apply_patch`.

## Fixed inputs and boundaries

The following accepted inputs were read completely; their historical
author-side pending labels are not changed:

- [Even-branch complete proof](../../../research_c409_c413/nonlinear_geometry/PROOF_INTEGER_HENON.md), especially Sections 1–7.
- [Odd-branch addendum](../../../research_c409_c413/nonlinear_geometry/ADDENDUM_INTEGER_HENON_ODD.md), including normalization, all seventeen exceptional parameters, and the eight-point equality locus.
- [Root non-author review](../../../research_c409_c413/REVIEW_INTEGER_HENON_ROOT.md), including its later odd-branch review and independent full-graph reconstruction receipts.
- [Five-paper contract](../../BATCH_PLAN.md).

Only this new C412 directory is writable by this author. No edits, new
numbering, or unchanged-input reruns occur in the sealed research snapshot.
Formal Route-A evaluations, global state, final double clean-directory
builds, final page-by-page visual QA, release manifests, and Git belong to
the root coordinator. A later non-author manuscript review is required;
the accepted proof review is not relabelled as manuscript review.

## Main theorem to appear before the proof

Write uniquely \(b=2q+e\), where \(q\in\mathbb Z\) and \(e\in\{0,1\}\),
and set
\[
A=a-q^2+(2-e)q.
\]
Translation \(T_q(x,y)=(x+q,y+q)\) conjugates \(H_{a,b}\) to
\(H_{A,e}\). A coordinate word \((v_0,\ldots,v_{d-1})\) denotes the
orbit of adjacent pairs \((v_i,v_{i+1})\), modulo cyclic rotation.
Subtract \(q\) from every coordinate in the normalized tables to recover
the original orbit. State all ranges and degeneracies in the tables.

### Even normal form \(e=0\)

| Parameter | Coordinate words | Exact period and range |
|---|---|---|
| \(A=1-k^2\) | \((1-k)\), \((1+k)\) | 1, \(k\ge0\); coincide only at \(k=0\) |
| \(A=-k^2-3\) | \((-k-1,k-1)\) | 2, \(k\ge1\) |
| \(A=-k^2-1\) | \((-k-1,k,k)\), \((k-1,-k,-k)\) | 3, \(k\ge0\); coincide only at \(k=0\) |
| \(A=-k^2\) | \((-k,-k,k,k)\) | 4, \(k\ge1\) |

### Odd normal form \(e=1\)

| Parameter | Coordinate words | Exact period and range |
|---|---|---|
| \(A=-k(k+1)\) | \((-k)\), \((k+1)\) | 1, \(k\ge0\); always distinct |
| \(A=-k(k+1)-4\) | \((-k-2,k-1)\) | 2, \(k\ge0\) |
| \(A=-k(k+1)-2\) | \((-k-2,k,k)\) | 3, \(k\ge0\) |
| Same parameter | \((k-1,-k-1,-k-1)\) | 3, \(k\ge1\) |
| \(A=-k(k+1)-1\) | \((-k-1,-k-1,k,k)\) | 4, \(k\ge0\) |

The table union is intended at overlapping parameters. Every rational
periodic point is integral. The global bound is eight, attained precisely
when \(e=1\) and \(A=-4\), equivalently
\(b=2q+1\) and \(a-q^2+q=-4\). The even-branch bound is seven, attained
only at \(A=-1\). These equality statements count points, not cycles.

## Claims–evidence matrix

| Claim | Accepted evidence and proof obligation in the article | Placement |
|---|---|---|
| Rational periodic points are integral; integer translations give exactly two normal forms | Direct nonarchimedean maximum and explicit substitution, addendum Section 1 | Sections 1–2 |
| Every sufficiently negative normalized parameter reduces to the same six-symbol problem | Even proof Section 3; addendum Section 2; include both interval partitions and strict inequalities | Section 3 |
| Only the displayed cyclic words survive, with no period cutoff | Even proof Section 4, transferred through the two rigorously derived lattices; complete six-case local argument | Section 4 |
| The tables cover every remaining parameter and every point | Even proof Section 6 and addendum Section 4; pruning theorem, all 13+17 tables, independent full-set receipts | Section 5 and Appendix A |
| All entries exist with the stated least period; all overlaps and the sharp bound are exact | Even proof Sections 5, 7; addendum Sections 3, 5 | Sections 4 and 6 |
| The ordinary-time rational-point return law follows from cycle multiplicities | Finite-orbit identity in the accepted proof; no external analytic continuation theorem needed | Section 7 |

No claim relies on a finite parameter screen outside the explicitly proved
finite complement. No new numerical experiment is planned.

## Section plan and intended files

### Abstract — `sections/0_abstract.tex`

Plan a compact self-contained abstract, approximately 150–190 words, with
no citations. Lead with the displayed two-parameter family and complete
classification. Explain that the difficult quantifiers are all parameters
and all rational periods. Identify the arithmetic six-symbol reduction
and finite exceptional complement as the proof mechanism. End with the
period set, sharp eight-point bound, and exact equality locus. Do not use
global priority language or suggest that a general uniform-boundedness
conjecture has been settled.

### 1. Introduction and classification — `sections/1_introduction.tex`

Define the map, determinant sign, ordinary iteration, rational periodic
set, and coordinate-word convention. State the full theorem and the two
classification tables early. Give one short paragraph explaining why
uniform period bounds do not list the points at every parameter.

Position the theorem against three distinct questions: Hénon height
finiteness; allowed cycles for arbitrary integral polynomial maps; and
rational periodic points beyond the present coefficient/degree/sign
hypotheses. Cite the five planned references only where they support
these comparisons. A compact comparison table may replace repetitive
prose if useful, but is not required for a length quota. Give the proof
dependency chain and a brief roadmap. The reader should know the exact
eight-point statement before any technical reduction.

### 2. Integrality and normal forms — `sections/2_normalization.tex`

Prove the p-adic maximum lemma for general integral \(a,b\). Derive
\(A=a-q^2+(2-e)q\) with the direction of conjugation explicit. Summation
of the coordinate recurrence excludes \(A>1\) in the even case and
\(A>0\) in the odd case; treat equality and \(A=0\) accurately.
Introduce centered coordinates on \(\mathbb Z\) or
\(\mathbb Z+1/2\), and prove the real maximum and pointwise residual
bounds. Do not confuse the odd summation center \(x-1/2\) with the
recurrence center \(u=x+1/2\).

### 3. A common six-symbol reduction — `sections/3_six_symbols.tex`

Present the integer-center and half-integer-center estimates as two
lemmas feeding one algebraic separation step. Keep the exact thresholds:
\(c=-A\ge13\), \(r\ge4\) in the even case; \(A\le-17\),
\(r\ge9/2\) in the odd case. Prove the adjacent interval partitions and
both radius-rounding branches, including all strict inequalities.

Once \(u_i=\varepsilon_i r+\delta_i\) is established, write the exact
identity and use the even coefficient with the right-side bound
\(<2r\) to obtain the two local equations. The half-integral value of
\(r\) does not invalidate the even-coefficient argument. No asymptotic
coefficient matching is allowed.

### 4. The local periodic words — `sections/4_local_classification.tex`

State and prove the common symbolic lemma for cyclic sequences of any
length, including lengths one and two. Explain the forbidden adjacent
offsets \(+1,-1\), then cover every value
\(s=-2,-1,0,1,2,3\). The empty cases \(-2,2\) and surviving cases
\(-1,0,1,3\) must each have a complete argument. Translate to both
tables, verify their polynomial identities for every listed parameter,
and prove all least-period and coincidence statements. In particular,
the odd second three-cycle degenerates at \(k=0\) to an already-listed
fixed point; it must not be counted as a three-cycle.

### 5. The finite complement and completeness — `sections/5_finite_complement.tex`

Prove the finite partial-permutation pruning lemma: a decreasing finite
set eventually stabilizes, and injectivity turns its stable image into
a permutation. This proves exactness without imposing a maximum period.
Specify the even integer alphabet \(S_c\), the odd doubled alphabet
\(S_A\), both bounds, and the exact successor maps. Include short
language-independent pseudocode using integer square roots and exact
set membership. Explain how the full cycle words specify the stable
point sets, while successive cardinalities document the computation.

Refer to the two fully printed Appendix A tables, not to an external
proof document. Record that the already executed independent check
reconstructed the entire bounding square/rectangle and used Boolean
transitive closure, comparing every vertex and cycle word; it was not
merely a comparison of totals. Do not imply that it was rerun for this
manuscript. Finish the proof of the main classification theorem by
joining the large-parameter and finite-complement branches.

### 6. Parameter intersections and the sharp bound — `sections/6_sharp_bound.tex`

Show the even overlaps \(A=-1,-4\) by square differences, accounting for
excluded degeneracies. Show the odd overlaps \(A=-2,-4,-6\) by parity
and \((k-\ell)(k+\ell+1)\), with counts \(5,8,4\) respectively.
Prove that no triple intersection was omitted. Derive the exact equality
locus in the original \((a,b)\)-coordinates.

### 7. Return counts and scope — `sections/7_returns_scope.tex`

Define the numbers \(N_d\) of exact cycles for \(d=1,2,3,4\), with
degeneracies removed. Derive
\[
\#\operatorname{Fix}(H_{a,b}^{\,n},\mathbb Q)
=\sum_{d\mid n}dN_d,
\qquad
\zeta_{a,b,\mathbb Q}(t)=\prod_{d=1}^4(1-t^d)^{-N_d}.
\]
State that this concerns rational points, not all algebraic fixed points
or scheme lengths. Give a concise final synthesis and limitations:
nonintegral rational coefficients, other leading coefficients, and
Jacobian \(-1\) lie outside the theorem; no target Euler factors, root
numbers, automorphy, zero correspondence, or Hilbert–Pólya realization
has been proved. Avoid importing workflow labels into the mathematical
paper.

### Appendix A. Exact finite certificates — `sections/A_certificates.tex`

Print all thirteen even rows \(c=0,\ldots,12\) and all seventeen odd rows
\(A=0,-1,\ldots,-16\), with the exact bound, every successive pruning
cardinality, and the stable coordinate words. State that the final set
is unchanged by one more pruning step. The two fully specified initial
alphabets and successor rules in Section 5 make each row reproducible.
Preserve all words, including differently rotated but equivalent words;
use one consistent canonical presentation in the final table.

The final structure has seven numbered sections, one appendix section,
and a separate abstract file. `main.tex` will input exactly these nine
section files. No padded experiments section or decorative figure is
planned. Completeness determines the actual page count.

## Tables and source plan

Tables 1–2: the exact parity classification, sourced from the accepted
proofs and already displayed above. Their captions define coordinate
words and union at overlaps; they carry the main result for a skim reader.
Tables A.1–A.2: complete finite-complement certificates, not sample data.
No raster illustration, new plot, or new experimental run is needed.

The five-entry bibliography and its verified metadata are in
[references.bib](references.bib). The exact access versions, publication
date distinctions, cited roles, and limitations are recorded in
[CITATION_AUDIT.md](CITATION_AUDIT.md). Silverman 1994 subscription text
was not obtained; do not turn that access limitation into a claim that
its unread content excludes this classification. Ingram's detailed
quadratic conjecture has Jacobian \(-1\). The recent long-cycle
constructions do have Jacobian \(+1\), but use unbounded odd degrees and
rational-coefficient integer-valued polynomials. Both distinctions must
survive editing.

## Review and next gates

The batch's [independent outline review](../../positive_characteristic/REVIEW_BATCH_OUTLINE.md)
has completed, and root has frozen `BATCH_PLAN.md`. Its C412 clarification
R4 is included above: the exact equality locus, conjugacy direction,
coordinate back-translation, and complete 13+17 certificates. This author
does not represent that outline audit as manuscript review.
Write the complete English LaTeX
article, verify all citation keys and labels, run the reverse-outline
test, and perform an author compilation check if needed. Retain actual
logs and distinguish the author check from root's final deterministic
build and visual QA. Hand the entire manuscript and provenance to the
assigned non-author reviewer; repair only issues identified by that
review or by actual checks.
