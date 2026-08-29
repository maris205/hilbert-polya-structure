# Hostile Review B — P114, rooted-forest leaf peeling

**Role and independence.** This is an independent second review of the
current manuscript and its public support files. I did not read
`HOSTILE_REVIEW_A.md`. I made no change to the manuscript, verifier, build
record, or bibliography. External posting, novelty language, priority claims,
and submission remain **HOLD**.

**Provisional verdict: MAJOR REVISION (owner-scope), with the mathematics
provisionally accepted.** I found no counterexample to the stated finite-map
theorem. The remaining blocking issue is not a false formula: the primary-owner
subtraction still omits a literal prior parallel leaf-rake source, an earlier
height-enumeration source, and the direct all-minors theorem source. Those
omissions matter because nearly the entire theorem package is an assembly of
classical primitives. The local fibre formula may remain a useful compact
observation, but the bounded search does not establish its priority.

## 1. Reconstruction from the update, not from the prose

Let a state be a parent map on a subset of `[n]`, with loops exactly at roots
and no other directed cycles. The map deletes every nonroot vertex with no
child and restricts the parent map to the survivors.

### 1.1 The update is well defined

If a deleted nonroot leaf `v` points to `p(v)`, then `p(v)` has the child `v`
and is therefore not deleted in that round. Thus restriction really is a map
on the surviving set. Roots are never deleted. The empty parent map is a state
and maps to itself.

### 1.2 The clock is height

For a nonroot vertex `v`, let `a(v)` be the largest downward distance from `v`
to a descendant leaf. A leaf has `a(v)=0` and disappears in round one. If
`a(v)>0`, its last child disappears in round `a(v)`, so `v` disappears in round
`a(v)+1`. On a longest root-to-leaf path of length `h`, the child of the root
therefore disappears in round `h`. Conversely no vertex can survive beyond
that round. Hence the entry time is exactly the usual root-vertex height, with
the empty and edgeless forests assigned height zero.

This also proves strict descent: a nonfixed state loses at least one vertex.
Consequently there are no nontrivial cycles.

### 1.3 Endpoints, fixed points, and zeta

The root set is invariant, and all nonroots are eventually deleted. The
endpoint is therefore the edgeless forest `E_R` on the original root set `R`.
Conversely every `E_R` is fixed. There are `2^n` fixed states and, because
there are no longer cycles,

\[
 |\operatorname{Fix}(T^q)|=2^n\quad(q\geq1),\qquad
 \zeta_T(z)=\exp\!\left(\sum_{q\geq1}\frac{2^nz^q}{q}\right)
 =(1-z)^{-2^n}.
\]

The fixed count alone recovers `n` as `log_2 |Fix(T)|`; the same information
is visible in the zeta exponent and in the number of fixed vertices of the
functional graph.

### 1.4 Exact basin of a fixed root set

Fix `R`, with `r=|R|>0`, and choose `k` nonroot labels. On the resulting
`m=r+k` labels, the reduced complete-graph Laplacian is

\[
 mI_k-J_k.
\]

Its all-ones eigenvalue is `m-k=r` and its other `k-1` eigenvalues are `m`, so
the specified-root forest count is `r m^{k-1}`. Therefore

\[
 B_{n,r}=\sum_{k=0}^{n-r}\binom{n-r}{k}r(r+k)^{k-1},
\]

with the separately stated `k=0` value one. If `r=0`, no nonempty forest can
have no root, so only the empty state occurs and `B_{n,0}=1`. This also gives
the phase count after summing over root sets (or, equivalently, adjoining an
extra vertex to encode all roots):

\[
 |\mathcal F_n|=\sum_{m=0}^n\binom nm(m+1)^{m-1}.
\]

The `m=0` contribution is the empty state and equals one.

### 1.5 Bounded-height basin and exact shells

For one distinguished root, let `A_h(x)` be the EGF in the nonroot labels for
trees of height at most `h`. Height zero gives `A_0=1`. At height at most `h`,
the root carries a set of child-rooted trees whose roots consume one label and
whose remaining height is at most `h-1`; hence

\[
 A_h(x)=\exp(xA_{h-1}(x)).
\]

For the `r` distinguished roots the factors are indexed by those roots, so the
EGF is `A_h(x)^r`. Choosing the `k` nonroot labels gives

\[
 B_{n,r}^{(h)}=
 \sum_{k=0}^{n-r}\binom{n-r}{k}k![x^k]A_h(x)^r.
\]

Together with `B_{n,r}^{(-1)}=0`, this makes the shell formula
`B_{n,r}^{(h)}-B_{n,r}^{(h-1)}` valid even at `h=0`. For `r=0`, the declared
value `B_{n,0}^{(h)}=1` correctly isolates the empty state.

### 1.6 Every local fibre

Let the target `G` have vertex set `S`, `m=|S|`, and `s` nonroot leaves. In a
predecessor, every vertex outside `S` must be a leaf pointing directly into
`S`; if a new vertex pointed to another new vertex, the latter would survive
and appear in the target. Every nonroot leaf of `G` must be hit by at least one
new child. For a fixed `ell`-set of new labels, inclusion-exclusion gives

\[
 \sum_{j=0}^s(-1)^j\binom{s}{j}(m-j)^\ell.
\]

Choosing the new labels and applying the binomial theorem gives

\[
 |T^{-1}(G)|=
 \sum_{j=0}^s(-1)^j\binom{s}{j}(m-j+1)^{n-m}.
\]

The empty target is separate and has only the empty predecessor. Three useful
hostile checks all agree with the formula:

- an edgeless `m`-vertex target has `s=0` and fibre `(m+1)^{n-m}`;
- a singleton root has fibre `2^{n-1}`;
- a root with one nonroot leaf has fibre
  `3^{n-2}-2^{n-2}`, because that leaf must be hit.

### 1.7 Sharp depth and deepest states

A forest on at most `n` vertices has height at most `n-1`. Equality requires
all `n` labels in one component and no branching: it is a rooted Hamilton
path. Reading from its opposite leaf to its root gives a unique permutation,
so for `n>=2` there are exactly `n!` deepest states. For `n=0`, the empty state
has depth zero. For `n=1`, both states have depth zero. The manuscript now
states these boundaries explicitly.

## 2. Boundary and counterexample ledger

| Attack | Literal outcome | Status |
|---|---:|---|
| `n=0` | phase 1, fixed 1, depth histogram `{0:1}` | pass |
| `n=1` | phase 2, fixed 2, depth histogram `{0:2}` | pass |
| `n=2` | phase 6, fixed 4, shells 4 at depth 0 and 2 at depth 1 | pass |
| empty target | exactly one predecessor | pass |
| empty root set | exactly the empty basin | pass |
| shell `h=0` | uses the declared `B^{(-1)}=0` | pass |
| nonfixed cycle search | impossible by strict vertex loss | pass |
| maximum-depth branching | any branch or second component prevents height `n-1` | pass |
| local fibre dependence | literal counts depend only on `(m,s)` through `n=6` | pass |

No small-state counterexample was found. More importantly, each arbitrary-`n`
claim above has a short structural proof; the computation is a convention and
regression control, not the proof.

## 3. Findings by severity

### CRITICAL

**None found.** I found no false update orientation, false basin formula,
incorrect fibre, hidden periodic orbit, or failure at `n=0,1` in the current
version.

### MAJOR (math)

**None found.** The determinant, EGF, inclusion-exclusion, fixed-point, zeta,
and sharp-depth arguments reconstruct correctly. Mathematical acceptance is
still conditional on preserving the present explicit conventions
`H(empty)=0`, `B_{n,0}^{(h)}=1`, and `B_{n,r}^{(-1)}=0`.

### MAJOR (owner-scope)

#### O1. The direct owner chain is still incomplete

The manuscript cites several relevant sources and explicitly assigns zero
credit to classical primitives. That is good, but three direct primary sources
are still missing from the chain:

1. Miller and Reif's original parallel tree-contraction paper introduces the
   literal `RAKE` primitive that removes leaves in parallel. Per component,
   repeated root-preserving RAKE is the update used here before any enumerative
   packaging. See [Miller--Reif, *Parallel Tree Contraction and Its
   Application*](https://doi.org/10.1109/SFCS.1985.43).
2. Riordan enumerated rooted trees by height before the cited 1967 work. See
   [Riordan, *The Enumeration of Trees by Height and
   Diameter*](https://doi.org/10.1147/rd.45.0473). The currently cited
   [Rényi--Szekeres paper](https://doi.org/10.1017/S1446788700004432) goes
   further and displays the nested exponential recursion for labelled trees.
   Thus the `A_h` recurrence itself carries zero residual credit.
3. Equation (3.1) explicitly invokes the all-minors matrix-tree theorem, whose
   direct primary source should be cited: [Chaiken, *A Combinatorial Proof of
   the All Minors Matrix Tree
   Theorem*](https://doi.org/10.1137/0603033). Cayley and Moon support the
   resulting count, but they do not replace a citation for the named theorem.

The already cited [Kovchegov--Zaliapin generalized pruning
paper](https://doi.org/10.1007/s10955-020-02593-1) and
[Addario-Berry et al. parallel leaf-stripping
paper](https://doi.org/10.1002/rsa.70023) are also genuine neighbors. The
former places leaf-originating pruning in a general dynamical framework; the
latter studies recursive parallel stripping in a random-tree/root-finding
setting. Neither appears, from the checked primary text, to state this exact
union-of-subsets functional graph or the displayed local-fibre formula.

**Required repair.** Add Miller--Reif, Riordan, and Chaiken to the bibliography
and owner paragraph. Explicitly subtract:

- the parallel leaf-removal primitive and height clock;
- exact/bounded height enumeration and nested exponential recursion;
- specified-root Cayley-forest counts and their determinant proof;
- absorption, fixed-point/zeta conversion, and Hamilton-path extremality.

After that subtraction, describe the residual only as this manuscript's
endpoint-indexed assembly plus the elementary `(m,s)` fibre calculation. Do not
call either novel, first, new, or priority-bearing while external posting is on
hold.

#### O2. The bounded search cannot support a positive priority inference

I searched exact-system phrases, predecessor/fibre phrases, parallel
leaf-rake literature, height-enumeration sources, and cited-source reference
chains. I did not locate a primary source stating the exact local fibre formula
or the complete finite functional graph on all subsets of `[n]`. That is only a
bounded negative search result. It is not evidence of novelty. The manuscript's
current HOLD sentence must remain, and the abstract's “claim is only this
finite-map conjunction” should be read as scope description, not priority.

### MINOR

#### M1. “Ordered product” is needlessly dangerous

The roots are distinguished by their labels, so `A_h(x)^r` is an **indexed
product** of `r` factors. “Ordered product” can suggest an extra `r!` ordering
that is not present. Replace the phrase even though the displayed coefficient
is correct.

#### M2. The abstract compresses three proof engines into two

The labelled-species route controls bounded basins, not local fibres. The fibre
formula comes from a third inclusion-exclusion argument. Replace the sentence
claiming that a metric argument and a species route “close” everything by a
three-part description: peeling clock, determinant/species basin controls, and
target-leaf inclusion-exclusion.

#### M3. State the orientation reversal at the matrix-tree invocation

The parent maps orient edges toward roots, while common all-minors statements
use the opposite arc convention. On an undirected complete graph reversal is a
bijection, so the count is unchanged. One sentence would remove a needless
convention trap.

#### M4. Make the empty phase term typographically explicit

The `m=0` term in `(m+1)^{m-1}` is mathematically `1^{-1}=1`, so there is no
error. Still, write “the `m=0` term is the empty state and equals one” beside
the phase formula; the basin formula already gives its analogous `k=0`
convention.

#### M5. Keep the coefficientwise qualifier attached to stabilization

`A_h` does not become the full rooted-tree series at one finite height. Each
fixed coefficient eventually stabilizes as `h` grows. The current word
“coefficientwise” is correct and should not be dropped in compression.

## 4. Fresh exact verification

I ran the checked-in verifier in a fresh temporary directory without bytecode
output:

```text
temporary run: /tmp/p114-reviewB.ZlAP9p/verification_output.txt
fresh output size: 422 bytes
stored output size: 422 bytes
byte comparison exit: 0
PASS: 400,105 exact assertions
```

The literal phase/depth rows were:

```text
n=0: phase=1, fixed=1, depths={0: 1}
n=1: phase=2, fixed=2, depths={0: 2}
n=2: phase=6, fixed=4, depths={0: 4, 1: 2}
n=3: phase=29, fixed=8, depths={0: 8, 1: 15, 2: 6}
n=4: phase=212, fixed=16, depths={0: 16, 1: 88, 2: 84, 3: 24}
n=5: phase=2117, fixed=32, depths={0: 32, 1: 505, 2: 920, 3: 540, 4: 120}
n=6: phase=26830, fixed=64, depths={0: 64, 1: 3036, 2: 9930,
      3: 9120, 4: 3960, 5: 720}
```

I also wrote a separate in-memory enumerator, rather than importing the
checked-in verifier. Through `n=5` it independently generated every subset
parent map, rejected non-loop cycles, applied the literal update, and compared
phase size, every endpoint basin, every local fibre, fixed counts, maximum
depth, and deepest counts. It passed 2,454 aggregate/formula checks. This is a
useful independence control; it is not an additional repository artifact.

The checked-in verifier has good hostile coverage: it enumerates all states
through `n=6`, checks literal updates and endpoints, evaluates bounded-height
EGFs with exact rational arithmetic, checks every target fibre, and attacks the
deepest layer. The assertion total is inflated somewhat by repeated update
validity checks, but the coverage is substantive rather than self-referential.

## 5. Fresh isolated build, fonts, and all-page visual inspection

I copied only `main.tex` and `references.bib` to
`/tmp/p114-reviewB.ZlAP9p/build` and ran the documented sequence
`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.

```text
pages: 3
fresh PDF size: 314,217 bytes
fresh/stored PDF byte comparison exit: 0
final TeX warnings: 0
BibTeX warnings: 0
overfull boxes: 0
underfull boxes: 0
undefined references/citations: 0
font rows: 24
nonembedded fonts: 0
nonsubset fonts: 0
fonts without Unicode maps: 0
```

The PDF metadata is anonymous and date-free. I rendered and visually inspected
all three pages, not a sample. Equations (1.1)--(1.6), the page break through
Theorem 1, the determinant and EGF displays, the fibre inclusion-exclusion,
references, running heads, and page numbers are legible. I found no clipping,
collision, missing glyph, visible TeX token, or suspicious blank page. The
large lower margin on page 3 is ordinary `\raggedbottom` whitespace and not a
layout failure.

## 6. Actionable repair list and verdict

1. **Owner block:** add the Miller--Reif, Riordan, and Chaiken primary sources
   and perform the explicit subtraction in O1.
2. **Scope block:** retain external/priority HOLD and make clear that a failed
   exact-owner search for the local fibre is not a novelty result.
3. **Precision:** replace “ordered product” by “root-indexed product,” name the
   inclusion-exclusion route in the abstract, and state the harmless
   matrix-tree orientation reversal.
4. **Boundary polish:** spell out the empty `m=0` phase term while retaining all
   current `n=0,1`, empty-basin, and `h=-1` conventions.
5. **Regression discipline:** rerun the exact verifier and isolated build after
   these prose/bibliography changes; the present mathematical output should
   remain byte-for-byte unchanged apart from bibliography pagination/content.

**Verdict:** no mathematical rejection and no theorem-level counterexample;
**MAJOR REVISION for owner-scope, then re-review. EXTERNAL HOLD remains
mandatory.**
