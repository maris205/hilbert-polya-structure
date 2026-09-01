# Hostile Review B — P148 owner-repair audit

**Package:** `papers/148-even-level-plane-tree-contraction`  
**Reviewer role:** independent owner-focused hostile reviewer; not an author of
P148 and not the author of Hostile Review A  
**Review date:** 2026-09-01 UTC  
**External status:** `HOLD_EXTERNAL`

## Verdict

**ACCEPT.** Severity count: **0 Critical, 0 Major, 0 Minor**.

The Critical owner defect in Review A has been repaired.  The current
manuscript states and proves the exact forgetful equivalence with
Soo--Khoussainov--Linz outward-contraction, cites its v4 primary record, and
assigns the unordered one-step rule, the partition-tree construction, and
bare height compression zero contribution credit.  The reopened source audit
also records its bounded-non-hit limitation instead of converting a search
non-hit into novelty evidence.

My acceptance is deliberately narrower than a novelty judgment.  Iterating
the known unordered contraction already makes depth halving and its height
clock a short consequence, even though the inspected owner does not state the
all-rank formula.  I therefore do **not** treat the temporal formula alone as
an ownership-distinguishing contribution.  What remains paper-sized is the
conjunction on the ordered carrier, especially the complete target-resolved,
size-refined block-and-gap inverse and the resulting exact-layer image
criterion and algebraic series.  No inspected primary source states that
residual conjunction.  This is enough for the internal P148 theorem package
to survive; it is not a novelty, priority, or release certificate.

## Scope and independent tests

I read the complete current package, including `main.tex`, the bibliography,
the verifier, the frozen transcript, all proof/claim/source/build records, and
the preserved `HOSTILE_REVIEW_A.md`.  I separately read
`OWNER_AUDIT_P148_REOPENED.md` and checked the direct owner against the full
text of arXiv:2111.13238v4 rather than relying on either audit's summary.

The following checks were performed independently.

- Reconstructed the quotient in Definition 6.6 of the v4 primary manuscript
  and proved the forgetful equivalence vertex by vertex and edge by edge.
- Screened the complete v4 reference list and bounded later-citation/query
  lanes for an iterated or inverse-enumerative owner.
- Rederived the labelled iterate skeleton, exact clock, recursive global
  inverse bijection, coefficient formula, exact image condition, and
  algebraic image series, including all degenerate cases.
- Cold-ran `verify_p148.py`, compared its output byte for byte with
  `verification_output.txt`, and inspected the verifier's theorem interfaces.
- Built from only `main.tex` and `references.bib` in a fresh temporary
  directory with `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- Checked final logs, PDF metadata and fonts, text extraction, and rasterized
  visual output for every one of the five pages.

Finite enumeration is treated only as counterexample pressure and artifact
reproducibility evidence, never as proof or ownership evidence.

## 1. Direct-owner equivalence

### 1.1 Exact reconstruction of Definition 6.6 — PASS

Let `For(T)` forget the order of the children of a plane rooted tree `T` but
retain its designated root.  In Soo--Khoussainov--Linz Definition 6.6, every
even-level vertex `v` and all downward odd-level neighbours of `v` form one
supervertex.  These sets partition the original vertices: every even vertex
belongs to its own supervertex and every odd vertex belongs to the
supervertex of its unique parent.

Map each resulting supervertex to its unique even-level vertex.  This is a
bijection from quotient vertices to the vertices retained by `E`.  An
original edge within a supervertex joins an even parent to an odd child and
is contracted.  Every edge between two supervertices instead joins an odd
vertex to one of its even children.  Under the bijection it therefore becomes
an edge from the odd vertex's even parent to that original even grandchild.
Those are exactly the promoted parent--grandchild edges in `E(T)`.  The
supervertex containing the designated root maps to the retained root.
Consequently there is a natural rooted-tree isomorphism

```text
For(E(T))  ≅  OutContr(For(T), root(T)).
```

This is an exact same-object hit, not an analogy and not merely generic
contraction background.  Equation (2) in the repaired manuscript now states
this equivalence, and its following paragraph gives the same quotient-vertex
and quotient-edge argument.  The source and ownership ledgers classify the
paper as a direct structural owner.

### 1.2 Full claim subtraction — PASS, with a conservative reading

The following material is no longer eligible for contribution credit in the
current package:

1. the unordered rooted one-step rule;
2. grouping every even vertex with its downward odd children;
3. the corresponding partition-tree interpretation;
4. generic deletion with promotion of children;
5. bare one-step height compression; and
6. generic Catalan, parity, transition, or pruning language.

These exclusions appear in the introduction, the Limitations section,
`SOURCE_VERIFICATION.md`, `CLAIMS_EVIDENCE.md`, `NARRATIVE_REPORT.md`, and the
reopened batch audit.  The manuscript also expressly says that its bounded
audit makes no novelty or priority claim and remains under `HOLD_EXTERNAL`.

There is one credit-boundary nuance worth making explicit.  The owner defines
an operator on arbitrary rooted finite trees, so one may designate the root
supervertex again and iterate it.  Once the one-step quotient is known, the
unordered depth-`2^k` survivor law and binary height clock are elementary
consequences.  They were not found as stated in the owner, but their absence
from its prose is not strong novelty evidence.  The current paper is still
honest because it calls the retained object a conjunction, zero-credits bare
height compression, and disclaims novelty and priority.  This acceptance
does not authorize scoring the unordered temporal axis as a standalone new
result.

The residual that survives owner subtraction is instead:

```text
the plane-order lift and induced contour order under reset-parity iteration
+ a complete every-target ordered inverse by source size
+ the exact-size image threshold
+ the algebraic exact-layer image series.
```

The temporal theorem supplies the dynamics of that literal ordered map; the
inverse and image theorems supply the ownership-distinguishing quantitative
axis.  This residual is materially more than a notational plane-order wrapper
around Definition 6.6.

## 2. Primary-source and bounded later-citation audit

### 2.1 Direct source — verified

The direct source is Khí-Uí Soo, Bakhadyr Khoussainov, and Simone Linz,
*Quasi-Isometric Graph Simplifications*, arXiv:2111.13238v4 (2022), especially
Definition 6.6.  I inspected the primary v4 full text.  Section 6 uses
outward-contraction to construct partition-trees with zero centre shift.  It
does not state a plane-order lift, iterated depth-divisibility law,
target-resolved predecessor generating function, exact-size image criterion,
or algebraic image series.

The package uses the current official arXiv author/title metadata and
identifies version 4 and Definition 6.6 in the printed bibliography.  The
repaired manuscript cites the owner both where the equivalence is introduced
and in Limitations.  The owner is not buried as generic background.

### 2.2 References and later works — bounded non-hit only

I screened the complete reference list of the v4 manuscript.  Its sources
concern graph contraction, partitioning and summarization, metric
approximation, centrality, and tree optimisation.  None is an owner for
iteration of outward-contraction or ordered predecessor enumeration.

I also checked the recorded query lanes:

```text
"outward-contraction"
"outward contraction"
iterated outward contraction tree
plane rooted tree odd level contraction promotion grandchildren
partition-tree inverse enumeration contraction
works citing arXiv:2111.13238
```

The exact-phrase lanes produced no second relevant primary paper.  The
OpenAlex discovery record for DOI `10.48550/arxiv.2111.13238` reported zero
later citing works at this checkpoint; it was used only as an index, not as
claim evidence.  No later primary citing paper was located.  A separate
index endpoint was rate-limited, which further reinforces the correct
bounded wording.  The manuscript and ledgers explicitly say that these
non-hits do not establish novelty, priority, exhaustive ownership, or release
clearance.  That limitation is adequate.

### 2.3 Nearest primary source and metadata — PASS

The broader ordered-promotion source is Berkemer, Höner zu Siederdissen, and
Stadler, *Compositional Properties of Alignments*, DOI
`10.1007/s11786-020-00496-8`.  The publisher record gives *Mathematics in
Computer Science* 15(4), 609--630 (2021), with online publication on 28
December 2020.  The repaired BibTeX entry now uses the version-of-record year
2021 and encodes `H{\"o}ner zu Siederdissen` correctly.  Text extraction and
visual inspection of page 4 print “Christian Höner zu Siederdissen.”  Review
A's metadata and visible-name defect is closed.

That source owns generic ordered deletion/contraction with promotion.  It
does not state this parity-reset dynamical system or its target fibres.  The
other four primary references are correctly treated as zero-credit nearby
background rather than as support for an ownership claim.

## 3. Independent mathematical rederivation

### 3.1 Literal finite map and every iterate — PASS

Writing a plane tree as an ordered child list and each child as an ordered
list of grandchildren gives exactly the recursive update in equation (1).
Only vertices are removed, so `E` is a self-map of `PT_{<=N}`.  The manuscript
correctly avoids calling it a self-map of an exact Catalan layer `PT_n`.

At rank `k`, assume an original vertex at depth `d` survives exactly when
`2^k` divides `d`; its current depth is then `d/2^k`.  The next update retains
it exactly when this current depth is even, equivalently when `2^(k+1)`
divides `d`.  Promoted edges join each survivor to its nearest retained
ancestor.  Associativity of ordered block concatenation preserves the order
induced by the original contour.  This proves the theorem for all `k>=0`,
including empty child lists and the singleton.

A deepest path contains every depth from zero to `h(T)`, hence

```text
h(E^k(T)) = floor(h(T)/2^k).
```

Absorption occurs exactly when `2^k>h(T)`, so
`tau(T)=ceil(log2(h(T)+1))`.  This gives zero for the singleton and behaves
correctly on both sides of every power of two.  Every nonsingleton loses a
depth-one vertex, hence strictly decreases in size; the singleton is the
unique recurrent state.  Finally `h<=n-1`, and the `n`-vertex path attains
equality, yielding the exact maximum `ceil(log2 n)`.

### 3.2 Recursive `F_U` bijection — PASS

Fix a target `U=(U_1,...,U_d)`.  Immediately below the source root, an
inserted odd child is either:

- empty, hence an odd leaf that disappears; or
- productive, carrying predecessor subtrees for one nonempty consecutive
  block of the ordered list `(U_1,...,U_d)`.

If there are `r` productive odd children, the `d` target children split into
`r` nonempty consecutive blocks in `binom(d-1,r-1)` ways.  Arbitrarily many
empty odd leaves occupy each of the `r+1` exterior/interior gaps.  Weighting
each inserted odd vertex by `y` gives

```text
A_0(y) = 1/(1-y),
A_d(y) = sum_{r=1}^d binom(d-1,r-1) y^r/(1-y)^(r+1)
       = y/(1-y)^(d+1)                 for d>0.
```

This construction is genuinely reversible.  A predecessor child list
uniquely identifies its empty children, its productive children, and the
consecutive target block carried by each productive child.  For every target
child `U_j`, the subtree hung below that productive child is independently a
predecessor counted by `F_{U_j}`.  Thus, coefficientwise,

```text
F_U(y) = A_d(y) product_{j=1}^d F_{U_j}(y).
```

Injectivity follows from unique recovery of blocks, gaps, and recursive
subtree predecessors.  Surjectivity follows by assembling any such data.
Different target vertices use disjoint inserted roots, so there is no double
counting.  At any fixed coefficient only finitely many inserted vertices can
occur, so the formal-series induction is legitimate.  These details now
appear in the proof of Theorem 3, closing Review A's compressed-bijection
finding.

For a target with `m` vertices and `I(U)` internal vertices, every internal
vertex contributes one numerator factor and

```text
sum_{v in U}(d_U(v)+1) = (m-1)+m = 2m-1.
```

Therefore

```text
F_U(y) = y^I(U)/(1-y)^(2m-1).
```

Extracting `y^(n-m)` gives

```text
binom(n-m-I(U)+2m-2, 2m-2)
```

when `n-m>=I(U)`, and zero otherwise.  The boundary cases agree:

- for a target leaf, there may be any number of empty odd children;
- for `d>0`, at least one productive odd child is forced;
- for the singleton target, there is exactly one predecessor of each size,
  namely a star; and
- equality `n=m+I(U)` is realized by the unique minimum-excess choices
  encoded by the formula.

### 3.3 Exact-layer image and algebraic series — PASS

The coefficient above is positive exactly when
`|U|+I(U)<=n`, proving the exact-source-layer image criterion.  It is not
mistaken for a size-preserving map statement.

Weighting a target by `z^(|U|+I(U))`, a leaf root contributes `z`.  An
internal root contributes `z^2` and a nonempty ordered sequence of child
trees, so

```text
H = z + z^2 H/(1-H).
```

The displayed minus-square-root branch is the unique formal solution with
zero constant term.  A target with minimum source weight `w` appears in every
exact layer `n>=w`; multiplying by `1/(1-z)` therefore gives `H/(1-z)` for
the exact-layer image series.  The manuscript's coefficients and table agree
with this derivation.

## 4. Verifier, build, and five-page visual audit

### 4.1 Cold replay — PASS

- The cold verifier completed with `P148_THEOREM_INTERFACES_PASS`.
- It reported **216,905 assertions** over all **23,714** plane rooted trees
  through 11 vertices.
- The new transcript is byte-identical to `verification_output.txt`; both
  have SHA-256
  `78a66ac2130e81d8b040e591a1cdea2967ae8259ab428d31e3cb2c94385f166b`.
- The output reports image counts
  `1,1,2,3,5,9,17,34,71,153,338`, matching the manuscript.

The verifier checks labelled iterate survivors rather than only unlabeled
state counts, every state clock, every target/source-size fibre through the
bound, local factor coefficients, exact image sets, and the `H` recurrence.
Its scope matches the frozen transcript and the claims ledger.

### 4.2 Isolated deterministic build — PASS

A clean directory containing only `main.tex` and `references.bib` built
successfully via `pdflatex -> bibtex -> pdflatex -> pdflatex`.  Its PDF is
byte-identical to both checked-in current PDFs:

```text
main.pdf
main_round1.pdf
SHA-256 5c681793e5e97abb0ad718f876a2e0af11bd2d41585d860dc0c5b8c3992ed957
```

The current PDF is **5 A4 pages** and **357,397 bytes**, exactly as recorded
in the hostile-repair section of `BUILD.md`.  Five of five bibliography
entries resolve.  The settled final log has no unresolved citation or
reference, rerun request, bad box, or build error.  All fonts are embedded
and subsetted.  Intermediate first-pass logs retain the expected pre-BibTeX
warnings; they do not occur in the settled log or PDF.

### 4.3 Visual inspection — PASS

All five pages were rasterized and inspected at high resolution.

- Page 1 cleanly prints the direct owner citation, the forgetful equivalence,
  and the zero-credit subtraction without collision or clipping.
- Pages 2--3 render every theorem, binomial coefficient, recursion, radical,
  and proof-ending symbol legibly.
- Page 4 cleanly renders the audit table, all required declarations, and the
  corrected Höner entry.
- Page 5 is a sparse bibliography continuation but has no orphaned heading,
  truncation, overlap, or malformed link.

The anonymous author presentation and blank PDF title/author metadata remain
consistent with internal anonymous status.

## Severity ledger

| Severity | Count | Finding |
|---|---:|---|
| Critical | 0 | Review A's direct-owner omission is repaired and fully visible. |
| Major | 0 | The residual ordered inverse/image conjunction survives the bounded owner audit and rederives correctly. |
| Minor | 0 | The recursive-bijection exposition and Höner/2021 metadata repairs are complete; artifact checks pass. |

## Final disposition

P148 may remain in the batch as an internally accepted short theorem paper.
Its defensible centre is the complete ordered, size-refined inverse and
exact-layer image theory for the plane-order lift; the temporal theorem is a
supporting analysis and not a standalone ownership claim.  The direct
unordered outward-contraction remains fully credited to
Soo--Khoussainov--Linz.

This verdict closes the requested independent Review B gate only.  It does
not remove the package's explicit external restriction:

```text
ACCEPT — HOLD_EXTERNAL remains in force.
```
