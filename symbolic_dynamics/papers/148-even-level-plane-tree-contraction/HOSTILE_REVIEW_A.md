# Hostile Review A — P148

**Package:** `papers/148-even-level-plane-tree-contraction`  
**Reviewer role:** independent hostile reviewer; not an author of this package  
**Review date:** 2026-09-01 UTC  
**External status:** `HOLD_EXTERNAL`

## Verdict

**CRITICAL — owner repair is mandatory before this package can pass the
internal gate.**  Severity count: **1 Critical, 0 Major, 2 Minor**.

I found no counterexample to the mathematical theorem package.  The
divisible-depth iterate law, clock, block-and-gap fibre, exact-size image
criterion, and algebraic equation for `H` all rederive correctly, including
their boundary cases.  The verifier cold-replays exactly and a clean
source-only build is byte-identical to the frozen PDF.

The blocking defect is instead an omitted direct structural owner.  The
outward-contraction of Soo, Khoussainov, and Linz groups every even-level
vertex with all of its odd-level children.  Its partition-tree is precisely
the unordered rooted shadow of the manuscript's one-step map.  This is not
merely generic contraction background.  The inspected owner does not state
the manuscript's ordered all-rank law, target fibres, or image series, so the
derived conjunction may survive after explicit subtraction; nevertheless,
the current source ledger cannot support release.

## Review scope and tests

I read `main.tex`, `references.bib`, the complete verifier and frozen output,
and every Markdown file in the package.  I also checked the frozen P148
theorem contract and the batch owner/collision records.  The following tests
were performed independently of the author-side QA.

- Cold replay:
  `PYTHONDONTWRITEBYTECODE=1 python3 verify_p148.py`, followed by an exact
  byte diff against `verification_output.txt`.
- Manual rederivation of every theorem interface, with special attention to
  `k=0`, the singleton, heights on both sides of powers of two, local degrees
  `d=0,1,2`, the singleton/star fibre, the minimum-size threshold, and the
  formal-series branch at `z=0`.
- Clean build from only `main.tex` and `references.bib` in a temporary
  directory using `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- PDF metadata, font embedding, log diagnostics, text extraction, and visual
  inspection of all four rendered pages.
- A bounded primary-source owner search over official arXiv records/full
  text, DOI/publisher pages, and the primary sources already cited by the
  manuscript.  A search non-hit is not treated as novelty evidence.

## Findings and required repairs

### Critical C1 — an omitted prior construction has exactly the unordered one-step rule

The package repeatedly subtracts *generic* ordered-tree promotion, but it
does not cite the substantially closer construction below:

- Khí-Uí Soo, Bakhadyr Khoussainov, and Simone Linz, *Quasi-Isometric Graph
  Simplifications*, arXiv:2111.13238v4 (2022), official
  [arXiv record](https://arxiv.org/abs/2111.13238) and
  [primary full text](https://arxiv.org/html/2111.13238v4), especially
  Definition 6.6 (“outward-contraction”).

That definition roots a finite tree, and for each even-level vertex `v`
places `v` and all downward neighbours of `v` into one super-vertex; the
output is the associated partition-tree.  Let `For` forget the child order
of a plane rooted tree.  In the resulting quotient:

1. the super-vertices are naturally indexed by the original even-depth
   vertices;
2. every edge crossing two super-vertices is an original edge from an
   odd-depth child to one of its even-depth children; and
3. that quotient edge therefore joins an even vertex to an original
   grandchild.

Consequently, with the designated root retained,

```text
For(E(T))  is isomorphic to  outward-contraction(For(T), root(T)).
```

The manuscript adds plane order by concatenating child blocks and then
studies repeated reset-parity contraction.  Those additions are real, but
they do not make the primitive one-step rule unowned.  The current statement
in `SOURCE_VERIFICATION.md` that no inspected source states the deterministic
reset-parity map and residual conjunction is therefore materially incomplete
unless it distinguishes the unmatched ordered/iterated conjunction from its
directly owned unordered one-step shadow.  The batch owner gate itself says
that a later direct owner reopens a contract; that condition is met here.

The primary source studies quasi-isometry and preservation of tree centres
and medians.  In the inspected text it does **not** give P148's plane-order
lift, the `2^k` divisible-depth theorem, the pointwise absorption clock, the
ordered block-and-gap fibre, the exact-layer image criterion, or the `H`
series.  Thus this finding blocks the present ownership posture rather than
falsifying Theorems 1–3 or Corollary 4.

**Required repair:**

1. Cite the outward-contraction primary source in the manuscript and every
   ownership artifact.
2. State the forgetful equivalence above explicitly.  Assign the one-step
   unordered rule, its partition-tree interpretation, and bare height
   compression zero contribution credit.
3. Reframe the contribution as analysis of a known underlying contraction
   after its ordered lift and iteration: the surviving conjunction is
   `ordered all-rank divisibility + sharp pointwise clock + complete
   size-refined ordered fibre + exact-layer image series`.
4. Search the source's references and later primary citations for prior or
   subsequent work on iterated outward-contraction and inverse enumeration.
   Record databases, dates, queries, direct/same-object/nearest-neighbour
   classifications, and the bounded-non-hit limitation.
5. Reconcile `SOURCE_VERIFICATION.md`, `CLAIMS_EVIDENCE.md`, `SELF_QA.md`,
   the batch owner gate, and the prose in Section 1.  Rebuild and obtain a
   fresh independent owner review.  Until then the package remains
   `HOLD_EXTERNAL`.

### Minor m1 — the manuscript compresses the global inverse bijection too far

Lemma 2 correctly counts the odd children inserted immediately below one
target vertex.  Theorem 3 then says only to apply the local factors
independently “working from its child subtrees upward.”  The intended
recursive bijection is recoverable and is described more clearly in
`PROOF_PACKAGE.md`, but the manuscript should expose it at the theorem
interface.  In particular, for
`U=(U_1,...,U_d)` it should write the coefficientwise recursion

```text
F_U(y) = A_d(y) product_j F_{U_j}(y),
F_U(y) = sum_{E(T)=U} y^(|T|-|U|),
```

and explain that each productive odd child carries predecessor subtrees for
one nonempty consecutive block of the `U_j`.  This makes surjectivity,
injectivity, independence, and the absence of double counting explicit.

**Required repair:** add that recursive bijection/induction to the proof of
Theorem 3 and note that all infinite products/sums are coefficientwise
finite.  No formula change is required.

### Minor m2 — the bibliography contains a visible author-name error and an unresolved year convention

The BibTeX source spells the second Berkemer-paper author as
`H{"o}ner` without the required backslash before the accent command.  The
compiled PDF visibly prints `Christian H"oner zu Siederdissen`.  The primary
[publisher record](https://doi.org/10.1007/s11786-020-00496-8) gives
**Christian Höner zu Siederdissen**, online publication on 28 December 2020,
and volume 15, pages 609–630 as the 2021 journal volume.  The package instead
uses volume 15(4) with year 2020 without explaining the online-first
convention.  This also contradicts the unqualified “metadata-verified” and
visual-acceptance claims in `SELF_QA.md` and `BUILD.md`.

**Required repair:** encode the name as `H{\"o}ner zu Siederdissen`, use the
journal issue year 2021 (or explicitly distinguish online-first 2020 from
issue year 2021), rebuild, visually inspect the corrected bibliography, and
update the QA records.

## Independent theorem rederivation

### 1. Literal map and divisible-depth iterates — PASS

The recursive definition deletes precisely the odd-depth vertices and
preserves the left-to-right order of all promoted grandchild blocks.  Suppose
at rank `k` that an original vertex at depth `d` survives exactly when
`2^k | d`; its current depth is then `d/2^k`.  The next application retains
it exactly when that current depth is even, equivalently when
`2^(k+1) | d`.  All intermediate retained ancestors occur at depths
`j*2^k`, so current depth and nearest-retained ancestry are both exact.
Associativity of ordered-list concatenation supplies the contour order.
This handles `k=0` as well as empty child blocks.

### 2. Height, absorption clock, and extremizer — PASS

A deepest root path contains a vertex at every depth `0,...,h`.  Hence after
rank `k` the greatest surviving current depth is
`floor(h/2^k)`, not merely bounded by it.  Absorption occurs exactly when
`2^k>h`, giving

```text
tau(T) = ceil(log_2(h(T)+1)).
```

For `h=0`, this gives `tau=0`.  Every nonsingleton has at least one depth-one
vertex, so each nonterminal step strictly decreases size; the singleton is
therefore the unique periodic/recurrent state.  Since `h<=n-1` and the
`n`-vertex path realizes equality, the all-`n` maximum is
`ceil(log_2 n)`, including both sides of every power-of-two boundary.

### 3. Local and global fibre — PASS, subject to m1's exposition repair

At a target leaf, all inserted odd children must be leaves, giving
`A_0=1/(1-y)`.  At target outdegree `d>0`, choose `r` productive odd children,
split the ordered list of `d` target children into `r` nonempty consecutive
blocks, and distribute arbitrary empty odd leaves among the `r+1` gaps.  The
local series is therefore

```text
sum_{r=1}^d binom(d-1,r-1) y^r/(1-y)^(r+1)
  = y/(1-y)^(d+1).
```

The source child list recovers the blocks and gaps uniquely.  Recursive
choices beneath distinct target vertices use disjoint inserted vertices, so
multiplication gives a numerator `y^I` and denominator exponent
`sum_v(d(v)+1)=(m-1)+m=2m-1`.  Extracting excess degree `n-m` yields exactly

```text
binom(n-m-I+2m-2, 2m-2)
```

when `n-m>=I`, and zero otherwise.  For the singleton target, this reduces
to one source of every size, namely the star.

### 4. Exact-size image and `H` equation — PASS

The fibre coefficient is positive exactly when `m+I(U)<=n`; this is a
source-layer statement and is never used as size preservation.  Weighting a
target by `z^(|U|+I(U))`, a leaf root contributes `z`, while an internal root
contributes `z^2` followed by a nonempty ordered sequence of child trees.
Thus

```text
H = z + z^2 H/(1-H),
H^2 - (1+z-z^2)H + z = 0.
```

The minus square-root branch is the unique formal solution with `H(0)=0`.
Since a target of minimum source weight `w` appears in every exact layer
`n>=w`, cumulative summation gives `H/(1-z)` for the exact-layer image
counts.  The displayed coefficients and table agree with this derivation.

## Verifier and artifact audit

- **Cold verifier:** PASS; the generated transcript is byte-identical to
  `verification_output.txt`.
- **Assertions:** 216,905 exact assertions over all 23,714 plane rooted trees
  through 11 vertices.  The checks include labelled iterate skeletons,
  clocks, every target/source-size fibre, local factors, image sets, and the
  `H` coefficients.
- **Current PDF:** 4 A4 pages, 352,411 bytes, SHA-256
  `ac3aea38bc4ed0580a37cfef9f02fa91699d91b1f8a23e3e1f6cf1baa1f2c8f0`.
- **Round-0 PDF:** 4 pages, 351,696 bytes, SHA-256
  `b32439d6be070d10bd54ff05a60b9920db176dcaf81c6a6a96fc939dd8db88d2`.
- **Clean build:** PASS and byte-identical to the current PDF at the hash
  above.
- **Typesetting:** all fonts are embedded/subsetted; the final log has no
  unresolved citation/reference warning and no overfull/underfull box.  All
  pages render cleanly apart from the visible name error in m2.
- **Metadata/declarations:** title and author metadata are blank; the PDF is
  unencrypted; Limitations, Data Availability, Ethics, Author Contributions,
  Conflict of Interest, and Funding are present.

The finite computation is strong counterexample pressure and reproducibility
evidence, not proof or ownership evidence.

## Source classification after hostile audit

| Class | Primary source | What is owned / what survives |
|---|---|---|
| Direct structural owner | Soo–Khoussainov–Linz, arXiv:2111.13238v4, Definition 6.6 | Owns the unordered rooted one-step contraction.  Does not, in the inspected text, own the ordered all-rank/fibre/image conjunction. |
| Same primitive, broader selection rule | Berkemer–Höner zu Siederdissen–Stadler, DOI `10.1007/s11786-020-00496-8`, Section 9 | Owns ordered-forest deletion with child promotion for arbitrary removed vertices; no parity dynamics or fibre law. |
| Nearest parity/enumeration background | Chen–Li–Shapiro, DOI `10.1016/j.dam.2007.04.020` | Plane-tree decomposition and parity-sensitive enumeration; zero credit. |
| Nearest geometric transition background | Nichols–Pilz–Tóth–Zehmakan, DOI `10.1016/j.disc.2020.111929` | Transition operations on noncrossing straight-line spanning trees, not this rooted ordered carrier; generic transition/logarithmic language gets zero credit. |
| Nearest pruning background | Kovchegov–Zaliapin, DOI `10.1142/S0218348X16500171` | Horton/leaf-pruning framework; pruning clocks and terminology get zero credit. |

The bounded search found no primary source stating the complete surviving
conjunction.  That non-hit does not establish novelty, priority, or freedom
to release.

## Disposition

The theorem package is mathematically **supportable as stated**, but the
paper package is **not owner-cleared as currently documented**.  Repair C1
and m1–m2, rebuild, and commission a fresh owner-focused hostile check.
Until that happens, the only defensible status is:

```text
HOLD_EXTERNAL — CRITICAL OWNER REPAIR REQUIRED
```
