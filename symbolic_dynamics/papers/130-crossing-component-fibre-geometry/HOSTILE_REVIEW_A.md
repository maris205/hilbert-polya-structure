# Hostile Review A — P130 crossing-component fibre geometry

**Role:** first independent nonauthor manuscript reviewer  
**Review date:** 2026-08-31 UTC  
**Object reviewed:** frozen round0 package in
`papers/130-crossing-component-fibre-geometry/`  
**External status:** **HOLD_EXTERNAL**

## Verdict

**GO_IF_REPAIRED / round0 is not yet signable.**  I found no counterexample
to the literal retraction, the sibling-list product, strict
supermultiplicativity, or the unique consecutive maximizer.  In fact, the
central inverse has a valid short proof.  The current text, however, does not
yet print that proof with enough precision for an all-size theorem: its
converse calls a child interval a gap when it can be only a proper subset of
one, and the parent-comparability sentence leaves the decisive intermediate
parent implicit.  Those are proof obligations, not matters that the
`n<=7` enumeration can discharge.

The ownership ceiling also needs one exact repair.  On a noncrossing
matching, an immediate-sibling list is an exact specialization of Igusa's
parallel-part definition, not merely something “close to” it.  The static
localization/compatible-merge principle must therefore be explicitly
zero-credited; the residual can remain the specified section's decorated,
target-wise fibre product.  These repairs do not require changing the
theorem statements or claim ceiling.

Current disposition: **STOP for round0 internal sign-off**,
**GO_INTERNAL after the repairs and re-entry checks below**, and
**HOLD_EXTERNAL** regardless of the internal result.

## Severity summary

| severity | count | disposition |
|---|---:|---|
| CRITICAL | 0 | no false theorem or counterexample found |
| MAJOR | 2 | all-size gluing proof; exact Igusa subtraction |
| MINOR | 2 | source locators/all-size sequence identification; support-record re-entry |

## 1. Independent mathematical reconstruction

### 1.1 Literal map, factorization, and dynamics

Let `pi(M)` be the partition of endpoints into supports of crossing-graph
components.  The owned component-support lemma makes `pi(M)` a noncrossing
partition with even blocks.  If `s(P)` pairs consecutive elements within
each block, the literal simultaneous update is exactly

```text
Phi_n = s o pi.
```

Thus equations (1) and (2) agree with the stated fixed-cut map.  The cut is
used honestly; no rotation-equivariance or unrooted canonicity is asserted.

Every section `s(P)` is a noncrossing matching.  Conversely, a noncrossing
matching has singleton crossing components and is fixed.  Therefore

```text
Phi_n^2 = Phi_n,
im(Phi_n) = Fix(Phi_n) = NC_2(n).
```

The Catalan image count, exact depth one for nonfixed states, and indegree
zero of every nonfixed state follow.  The indegree assertion is worth
checking: if `Phi(y)=x`, idempotence gives `Phi(x)=Phi^2(y)=x`; hence no
nonfixed `x` has a predecessor.  Since every positive iterate has exactly
`Cat_n` fixed points, the fixed-`n` Artin--Mazur zeta function is correctly

```text
(1-z)^(-Cat_n).
```

The empty boundary is also consistent: the sole state at `n=0` is fixed and
`(-1)!!=Cat_0=1`.

### 1.2 Forward sibling localization

Fix `M` over a noncrossing target `T`, put `P=pi(M)`, and take

```text
B={b_1<...<b_(2k)},
x_i=(b_(2i-1),b_(2i)).
```

The section chords are disjoint.  If `p_i` is the immediate parent of
`x_i`, its endpoints lie in a different block of `P`.  That entire block
lies in one cyclic gap of `B`.  For `p_i` to enclose `x_i`, this must be the
outer cyclic gap, with one endpoint before `b_1` and the other after
`b_(2k)`.  Hence `p_i` encloses every endpoint of `B`, and in particular
every section chord.

This supplies the parent argument that the paper intends.  If `p_i` and
`p_j` were distinct, noncrossing of `T` would make them comparable; say
`p_i` is strictly inside `p_j`.  But `p_i` encloses `x_j`, so it lies
strictly between `x_j` and `p_j`, contradicting that `p_j` is the immediate
parent of `x_j`.  Thus all parents coincide.  If one `x_i` is top-level,
any parent of another `x_j` would enclose `x_i` as well, a contradiction.
The virtual-root case follows.

Once common-parent localization is established, alternating sibling indices
would give alternating endpoints from two blocks of `P`; the induced groups
therefore form a noncrossing partition of the ordered sibling list.  This
direction is mathematically sound, but the manuscript should print the
explicit `p_i subset p_j` argument above instead of the ambiguous phrase
“the inner one would contradict immediacy of the outer one as a parent.”

### 1.3 Converse global noncrossing construction

For every parent `v`, choose `rho_v in NC(d_T(v))`.  A block `Q` produces
the endpoint block `B_Q` consisting of the two endpoints of its selected
children.  At a fixed parent, doubling each sibling index to its left/right
endpoint preserves the alternating-pattern test, so the `B_Q` are pairwise
noncrossing.

The missing local-to-global sentence requires two cases.  Let `x` be a child
of `v`, and compare its interval `I_x` with a parent-level block `B_Q`.

- If `x` belongs to `Q`, its two endpoints are consecutive in the sorted
  list of `B_Q`; hence the open interval `I_x` is a gap of `B_Q`.
- If `x` does not belong to `Q`, the whole closed support of `x` lies inside
  the gap between the nearest selected siblings of `Q`, or in the outer gap
  if all selected siblings are on one side.  Thus `I_x` is generally only a
  **subset** of a gap of `B_Q`.

The distinction is real.  For top-level children

```text
(1,2), (3,8), (9,10)
```

and root block `Q={1,3}`, the middle child interval `(3,8)` is contained in
the `B_Q={1,2,9,10}` gap `(2,9)` but is not itself that gap.  Descendant
blocks can live inside the middle interval, so this is exactly the case the
forest induction must cover.

Every block constructed strictly below `x` lies inside `I_x`, and therefore
inside one gap of every block constructed at the parent level.  Blocks below
different children lie in disjoint intervals.  Induction from the leaves,
followed by the identical disjoint-interval argument at the virtual root,
then proves global noncrossing.  This also proves explicitly that different
nesting levels do not merge or cross.

For `Q={i_1<...<i_r}`, the endpoints in `B_Q` occur as the left and right
endpoints of child `i_1`, then child `i_2`, and so on.  Descendant endpoints
are excluded from `B_Q`.  Consecutive pairing therefore recovers exactly the
chosen siblings, and every chord is a child once, so `s(P)=T`.

### 1.4 Decorations and mutual inverse

Order-preserving transport of a crossing-connected decoration to each
`B_Q` is exact.  Chords supported on two different noncrossing partition
blocks cannot cross, while each decoration has connected crossing graph.
Consequently the constructed crossing components have supports exactly the
`B_Q`; there is neither internal splitting nor cross-block merging.

Extraction recovers the component-support partition, the unique sibling
groups, and the standardized connected decorations.  Conversely, exactness
of the constructed components makes extraction recover all local choices.
Repeated block sizes cause no ambiguity because endpoint supports, rather
than sizes, identify the blocks.  Step 4 and the virtual-root handling are
therefore correct once the Step 2 gap containment is written accurately.

Conditional only on that textual repair, equations (3)--(5) follow:

```text
a_d = sum_(rho in NC(d)) product_(B in rho) c_|B|,
Phi_n^(-1)(T) <-> product_v A_(d_T(v)),
|Phi_n^(-1)(T)| = product_v a_(d_T(v)).
```

### 1.5 Formal transform, strictness, and unique maximum

The manuscript correctly labels the ordinary series as formal.  Decomposing
a noncrossing partition by the block containing its first element gives

```text
A(u)=1+C(u A(u)),
```

so equation (6) is correct without any analytic convergence implication.
The displayed coefficients through degree seven agree with the exact
transform.

For positive `i,j`, juxtaposition injects
`A_i x A_j` into `A_(i+j)`.  Its image has at least two partition blocks.  A
one-block object exists outside the image: for `k=i+j`, pair `r` with `r+k`
for `1<=r<=k`; every two chords cross, so the decoration is connected.
Thus equation (7), `a_i a_j<a_(i+j)`, is strict in every required size.

In the virtual-rooted nesting forest, every chord is a child exactly once,
so `sum_v d_T(v)=n`.  Repeated strict merging bounds the fibre product by
`a_n`, with equality only when one vertex has positive degree.  A chord
vertex cannot have degree `n`, because it would be an additional chord
besides its `n` children.  The positive vertex is therefore the virtual root.
All chords are top-level; a nonconsecutive noncrossing chord in a perfect
matching would contain another chord, so the target is uniquely

```text
(1,2)(3,4)...(2n-1,2n).
```

The empty case is separately correct.  The rainbow product is one because
all positive degrees are one and `a_1=1`.  The total-mass corollary is then
just the partition of the finite domain into the proved fibres.  I found no
defect in Theorem 3.1 or Corollary 3.2.

## 2. MAJOR findings and required repairs

### M1. The central all-size proof contains an inaccurate gap assertion

Theorem 2.1 is the paper's substantive residual, so its local-to-global step
cannot rest on finite reconstruction.  Step 2 currently says that a child's
open interval “is a single gap of every block created at the parent level.”
That is false when the child is not selected by the parent-level block; it
can be a proper subset of a larger gap, as the explicit three-sibling example
above shows.  The desired noncrossing conclusion remains true.

**Required repair:** replace the assertion by the two-case gap-containment
lemma in Section 1.3 of this review.  State separately that blocks below
different children have disjoint supports and apply the same argument at the
virtual root.  In Step 1, name the two parents `p_i,p_j`, order them by
containment, and identify the inner parent as a strict intermediate container
of the chord whose alleged parent is the outer one.  This closes parent
comparability without appealing to `n<=7`.

### M2. Igusa's boundary is an exact specialization, not merely “close”

Igusa, *A Category of Noncrossing Partitions*, Definition 1.7 defines two
parts to be parallel when they are both maximal, or when they are covered by
one part with no point of that covering part between them; Proposition 1.8
connects parallelism to permissible merging.  For the noncrossing partition
of endpoints into the two-element chord blocks of `T`, top-level chords are
exactly the first case.  Immediate children of a chord are the second case:
they share that covering chord, whose only two endpoints lie outside their
supports.  Thus every ordered immediate-sibling list used here is precisely
a parallel set in this specialization.

The current phrases “close to Igusa's parallel parts” and “generic
parallel-part geometry” understate this overlap.  Since the manuscript's
contribution boundary depends on this subtraction, the issue is major even
though it does not invalidate the formula.

**Required repair:** cite Definition 1.7 and Proposition 1.8 (or their final
published numbering), state the specialization above, and give zero credit
to sibling localization and compatible noncrossing merges themselves.  Then
state the residual narrowly: for this fixed-cut section, connected
decorations turn those local choices into the exact crossing components and
yield the product over every specified target.  Do not claim the static
sibling principle as new.

Primary record checked 2026-08-31:
[Igusa, DOI 10.1007/s10485-025-09838-8](https://doi.org/10.1007/s10485-025-09838-8).

## 3. MINOR findings

### m1. Pin the Alman--Lian--Tran identification at theorem level

The attribution is now correct and the zero-credit language is appropriate.
The primary paper gives the full-wiring recurrence in Theorem 4.1.6, names
A111088 in Remark 4.1.7, gives the coefficient identity in Theorem 4.1.8,
and proves the asymptotic in Theorem 4.2.1.  Add those locators and one
sentence explaining that the all-size `a_d` transform, not merely its first
eight displayed values, is the same owned sequence.  This avoids making an
OEIS-name/initial-value match carry an all-size identification.

Primary record checked 2026-08-31:
[Alman--Lian--Tran, DOI 10.1016/j.jcta.2014.11.004](https://doi.org/10.1016/j.jcta.2014.11.004).
Thomas Lam's attribution and generic-uncrossing subtraction are already
correct; the primary paper is
[Lam, DOI 10.1016/j.jcta.2015.04.004](https://doi.org/10.1016/j.jcta.2015.04.004).

### m2. Support records must not pre-close the repaired proof

`README.md`, `IMPROVEMENT_LOG.md`, `PAPER_PLAN.md`, and
`CLAIMS_EVIDENCE.md` describe the four-step inverse as fully closed.  After
repairing the manuscript, update those records to point to the explicit
parent-containment and two-case gap lemma, record the more exact Igusa
subtraction, and pin fresh source/PDF/control hashes.  Do not mark round1
closed solely because the unchanged enumerator still passes.

## 4. Owner and collision audit

The remaining owner statements are disciplined.

- Kreweras, Flajolet--Noy, Nabergall, Acan, and Callan receive zero credit
  for noncrossing partitions, crossing-component/decorated even-block
  decomposition, intersection graphs, connected counts, and the generic
  transform.
- Alman--Lian--Tran receive zero credit for A111088, its recurrence,
  coefficient identity, and asymptotics.  No analytic asymptotic is claimed.
- The uncrossing paper is correctly attributed to **Thomas Lam**, not to
  Alman--Lian--Tran, and generic uncrossing receives zero credit.
- The manuscript explicitly separates P110's chord-edge update, P120's tree
  involution, P123's graph-component complementation, and the
  run/composition systems P117/P122/P126.  The nesting forest is used only as
  an inverse coordinate.  I found no internal theorem identity, but generic
  componentwise, tree-coordinate, fibre-product, and extremal templates must
  remain zero credit.

The bounded primary-source check found no source in the reviewed set that
states the exact conjunction of this literal fixed-cut section, connected
component decorations, every-target product, and unique target maximizer.
That is only a bounded non-hit.  It is not evidence of novelty, priority, or
permission to release.  **HOLD_EXTERNAL remains mandatory.**

## 5. Fresh exact-control evidence

I reran the paper-local standard-library verifier from a stable snapshot and
byte-compared fresh stdout with the canonical transcript.  Result: `cmp=0`.

```text
n=0 | states=1      | targets=1   | connected=0     | a_n=1
n=1 | states=1      | targets=1   | connected=1     | a_n=1
n=2 | states=3      | targets=2   | connected=1     | a_n=2
n=3 | states=15     | targets=5   | connected=4     | a_n=8
n=4 | states=105    | targets=14  | connected=27    | a_n=52
n=5 | states=945    | targets=42  | connected=248   | a_n=464
n=6 | states=10395  | targets=132 | connected=2830  | a_n=5184
n=7 | states=135135 | targets=429 | connected=38232 | a_n=68928
TOTAL | states=146600 | targets=626 | reconstructed=146600
ASSERTIONS=735609
STATUS=PASS
```

The verifier separately checks the literal map, component-support
noncrossing, idempotence, forward localization, every target product,
formal coefficients, strictness, and exact source-set equality for the
independent converse constructor.  This is strong counterexample pressure,
not an all-size proof.

Pinned hashes from the review run:

```text
abd519009e877fa1fa98ece4e6cc290a5fb55bda47f07d4e79b9ccad43568a3d  code/verify.py
89b6142c21feac945f9d0dd362b5edf78aed78530596330be0c237e9088d60b4  code/verification_output.txt
89b6142c21feac945f9d0dd362b5edf78aed78530596330be0c237e9088d60b4  fresh stdout
```

## 6. Isolated build, visual, font, and anonymity QA

I copied only `main.tex` and `references.bib` to a fresh temporary directory
and ran the required isolated sequence

```text
pdflatex -> bibtex -> pdflatex -> pdflatex.
```

All four stages returned status `0`.  Expected unresolved items occurred in
the early passes only; the settled fourth-stage log had no errors, warnings,
undefined citations/references, rerun request, or overfull/underfull box.
The isolated PDF was byte-identical to both frozen PDFs:

```text
251180a52ede34157036a010037f8b2a87b955b2d39409719a2653f830fac7fc  main.tex
276dcdfad779b9802d7e73ee63930198670ef64262b9670e436e906570ad5bae  references.bib
4d914ae6857739b11955dc9ec0db356e8bca5ae5cb67c1fd852ff3d4c2e796c9  isolated main.pdf
4d914ae6857739b11955dc9ec0db356e8bca5ae5cb67c1fd852ff3d4c2e796c9  main.pdf
4d914ae6857739b11955dc9ec0db356e8bca5ae5cb67c1fd852ff3d4c2e796c9  main_round0_original.pdf
```

`pdfinfo` reports 4 A4 pages, 342,739 bytes, rotation zero, no encryption,
forms, JavaScript, custom metadata, or metadata stream.  Title, Subject,
Keywords, and Author metadata are blank, and dates are omitted.  Every font
reported by `pdffonts` is embedded, subsetted, and Unicode-mapped.  I
rasterized and inspected all four pages: no clipping, collision, missing
glyph, bad break, illegible citation, or anonymity leak was found.  The
visible author is only “Anonymous.”

## 7. Re-entry test and claim ceiling

The admissible claim ceiling remains:

1. the literal fixed-cut map and its zero-credit retraction consequences;
2. the repaired four-direction target-wise sibling-decoration inverse;
3. the resulting pointwise forest product;
4. strict supermultiplicativity and the unique consecutive-target maximum,
   whose value is the already-owned A111088 sequence;
5. the formal transform and total-mass identity as zero-credit consistency
   facts.

No novelty, priority, unrooted canonicity, general parallel-part theorem,
new connected-diagram or A111088 enumeration, analytic asymptotic, generic
uncrossing, or external-release claim is allowed.

**GO_INTERNAL on re-entry only if:**

- Step 1 prints the explicit comparable-parent/intermediate-container
  contradiction;
- Step 2 replaces the false gap equality by the two-case gap-containment
  lemma and explicitly closes disjoint child intervals plus virtual root;
- the manuscript identifies matching sibling lists as the exact Igusa
  parallel-set specialization and narrows the residual accordingly;
- the Alman--Lian--Tran theorem locators/all-size identification are pinned;
- all support records describe those actual repairs; and
- a fresh canonical comparison, isolated four-stage build, all-page visual
  audit, font check, metadata check, and frozen-round PDF preservation pass.

Until then: **STOP / HOLD_EXTERNAL**.
