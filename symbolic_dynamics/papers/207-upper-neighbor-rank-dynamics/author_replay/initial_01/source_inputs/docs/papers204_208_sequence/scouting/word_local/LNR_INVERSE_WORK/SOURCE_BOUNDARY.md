# LNR inverse — classical adapters and bounded source boundary

2026-09-06 UTC. Author source work, not independent novelty review.
No paper number or admission. Root owns the broader literal/temporal and
repository collision audit. This report identifies exactly what is already
classical and what this bounded author check has not transferred.

## 1. The alternating extremizer is completely classical

Take a labelled alternating target $b=(02)^m$, $m\ge2$. Write its source
heights on the zero sites as $u_j$ and on the two sites as $v_j$. The
literal inverse conditions are exactly
$$u_j\in\{0,1\},\quad v_j\in\{1,2\},\quad u_j<v_j>u_{j+1}.$$
Map a valley to $f(u_j)=u_j+1$ and a peak to $f(v_j)=v_j$. This is a
bijection, with the displayed inverse formulas, onto order-preserving maps
from the alternating $2m$-element crown to the two-element chain.

There is also a full source-set independent-set adapter, not only a
coincidental Fibonacci recurrence. Mark a valley when its height is one,
and mark a peak when its height is one. A strict inequality fails exactly
when adjacent sites are both marked. Thus the marks form an independent
set of the original labelled cycle. Given the set, use height one on
marked sites, height zero on unmarked valleys, and height two on unmarked
peaks. These maps are mutually inverse and preserve every label.

The elementary two-state independent-set transfer has characteristic
polynomial $t^2-t-1$ and cyclic count $L_{2m}$. In the proof package's
coordinates, $A$ has leading block $TT^T$, where
$$T=\begin{pmatrix}1&1\\0&1\end{pmatrix}.$$
Therefore the value $\operatorname{tr}A^m=L_{2m}$, the source set of the
alternating fibre, and its standard transfer proof have zero separate
novelty credit here.

Both odd-length attaining families also have full classical adapters.
For the unique $00$ run, repeat the source height on that zero site of
the alternating cycle; deleting one of the repeated positions reverses
the map. For the unique positive target run $11$, its two boundary
zero heights belong to $\{0,1\}$, because every other positive run is
$2$ and there are at least two positive runs. The local source options
for that run are then $11$ or $22$: exactly the options obtained by
doubling the source peak $1$ or $2$ in the alternating fibre. Deleting
one repeated peak reverses the map. The special mixed strings $12,21$
would require a boundary zero height two and are unavailable. These
coordinate-preserving constructions explain the two odd attaining fibre
counts without claiming that the construction proves global maximality.

## 2. Generic all-target order-map adapter is also deducted

For any source define the cyclic edge sign
$\sigma_i=\operatorname{sign}(x_i-x_{i+1})\in\{-,0,+\}$. Its target
satisfies
$$b_i=\mathbf1_{\{\sigma_i=+\}}+
\mathbf1_{\{\sigma_{i-1}=-\}}.$$
For each sign word satisfying these constraints, contract the zero-sign
edges. Orient each remaining edge from the smaller source block to the
larger block. A directed cycle is infeasible. Otherwise take the transitive
closure to obtain a poset $P_\sigma$ on the contracted blocks, and choose
a strictly order-preserving map $P_\sigma\to\{0,1,2\}$. Expand each
contracted block to all its original positions. This recovers exactly the
source words with that sign pattern. The all-zero sign pattern has one
contracted vertex and gives the three constant sources.

The sign word is recoverable from a source; the expansion is injective for
each sign word. Hence the whole fibre is a disjoint union of these standard
strict order-map sets, with no quotient over labels. This general-purpose
static adapter is valid and is not presented as a new inverse mechanism.
The eight kernels merely evaluate this low-alphabet local information
efficiently. A generic transfer matrix, a standard sign-poset decomposition,
or a faster table alone is not this candidate's proposed separate axis.

This adapter has not, by itself, compared the *union sizes* for all output
targets of a fixed length, proved the optimal length budget, or excluded
all mixed-target equality cases. The explicit comparison in the author
proof uses noncommuting $A,J,B$ products, costlier dominated kernels,
strict $B/J$ bounds, and separate $r=1$ and odd/even budgets. Whether a
prior theorem already transfers that complete comparison remains a matter
for the independent candidate gate. A generic static representation is
not evidence that it does or does not transfer the extremum.

## 3. Primary sources actually inspected

### Currie and Visentin (1991): historical enumeration, body unavailable

[Publisher article page](https://link.springer.com/article/10.1007/BF00383399):
J. D. Currie and T. I. Visentin, *The number of order-preserving maps of
fences and crowns*, Order 8, 133–142 (1991), DOI 10.1007/BF00383399.
The publisher metadata and abstract were actually read on 2026-09-06.
They establish an earlier enumeration treatment of fence/crown order maps.
The body is subscription-only in the retrieved page and was **not read**;
no particular theorem, formula or global LNR maximum is attributed to it.
Some secondary metadata say 1992; the actual publisher says June 1991.

### Huang (2026), version 2: explicit cyclic order-map trace

[Version-pinned primary preprint](https://arxiv.org/html/2607.22767v2),
*Bernstein Transfers and Greedy Records for Fence and Circular-Fence Order
Polynomials*, arXiv:2607.22767v2, 31 July 2026. Actually read: the order-map
definition in Section 1; Section 4's orientation hypotheses, Proposition
4.1 and full trace proof; Definition 4.2; Theorem 4.3 and its full proof.
Proposition 4.1 supplies the ordinary trace of weak-comparison matrices
for maps from an oriented cycle to a chain. Applying its two-letter
alternating case supports the classical side of Section 1 above. This
preprint concerns a fixed oriented poset and a record interpretation,
not the literal LNR feedback or a demonstrated maximum over LNR targets.
The latter distinction is the present author's scope comparison, not a
novelty certification. No uninspected later fixed-record-fibre theorem
is being used to declare the LNR residual clear.

### Tropp (2022): exact analytic inequality needed by the proof

[Author-hosted lecture notes](https://www.tropp.caltech.edu/notes/Tro22-Matrix-Analysis-LN.pdf),
Joel A. Tropp, *ACM 204: Matrix Analysis*, Caltech CMS Lecture Notes 2022-01,
Winter 2022, DOI 10.7907/nwsv-df59; typeset 22 August 2022. Actual download
via curl succeeded after the web PDF opener returned an internal error.
The saved PDF and its layout text are in this directory. Actually read:
title/citation pages and printed pp. 49–53, including Example 6.18,
Theorem 6.32, its proof sketch and surrounding norm hypotheses. Theorem
6.32 is the two-factor unitarily invariant norm Hölder inequality; the
proof package states the exact Schatten substitution and induction used.
This inequality is wholly prior, not a contribution of the LNR proof.

The PDF SHA-256 is
`d8e9da8b7a6f4b3d3d5845cc1f7ebafb6d5f2224c9b48244fb7371d6557aadf8`.
The source is kept for private verification, not licensed here for release.

### Baumgartner (2011): narrower alternative inspected, not overused

[Primary version-pinned text](https://arxiv.org/html/1106.6189v2),
Bernhard Baumgartner, *An inequality for the trace of matrix products, using
absolute values*. Actually read the two-factor Matrix Hölder Theorem 2,
equation (15), and its complete proof. It is a useful tracial two-factor
reference, but that statement alone was not silently substituted for the
multifactor product-norm estimate. The proof instead uses Tropp's explicitly
applicable norm theorem and the displayed induction.

## 4. Bounded discovery queries and local comparison

Queries actually run on 2026-09-06 included:

- `Currie Visentin 1991 fence crown posets order polynomials independent sets Fibonacci Lucas`
- `Ruskai 1972 Inequalities for Traces on von Neumann Algebras 26 280 pdf Holder products`
- `Schatten Hölder inequality multiple matrices trace product proof Tropp notes`
- `"cellular automaton" "number of" "smaller" "neighbors"`
- `"local rank" "cellular automata"`
- `"ternary" "preimages" "Lucas"`
- `"cycle" "maximum" "fibre" "Lucas"`

General cellular-automaton and secondary/aggregation results were not
used as theorem-level evidence. The exact-rule queries supplied no
primary full LNR adapter in the inspected output; this nonhit proves
nothing about priority. An attempted Euclid Ruskai URL also returned an
internal error; no Ruskai body-read claim or theorem dependence is made.

As a narrow local check, P112's actual `main.tex`, abstract and
introduction, lines 31–119, were read. That map reorients the edges of a
complete tournament according to endpoint outdegrees and **retains ties**;
LNR replaces numeric heights by strict lower-neighbour counts on a cycle.
The literal definitions do not identify the carriers or tie convention.
This is not a claim to have excluded every factor or graph extension.
Root owns the broader collision audit and temporal source comparison.

## 5. Honest current boundary

The all-target source reconstruction and all-n maximum/equality have a
complete author proof and finite checks, but no independent gate verdict.
The count and source sets of every attaining family are fully classical
under the adapters above. The proposed remaining extremal content is only
the exact comparison against all other labelled targets. An assessor may
still eliminate it through a fuller primary adapter. No acceptance,
external expert opinion or global novelty claim is implied. HOLD_EXTERNAL.
