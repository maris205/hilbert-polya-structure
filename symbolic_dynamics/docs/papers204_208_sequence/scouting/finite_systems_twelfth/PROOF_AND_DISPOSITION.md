# Twelfth slate: deductions, witnesses and closed boundaries

Author evidence only. The three complete desk proofs are in the immutable
[intake](INTAKE.md); they are not recast as new two-axis research progress.
The actual fixed-box producer and pair receipt are linked in the report.

## STC — what the binary Laplacian factor does and does not prove

Use all unordered vertex pairs as potential edges, in lexicographic order.
Over F2 let B be the reduced incidence matrix and D the diagonal matrix of
edge indicators. Then L=BDB^T. The spanning-tree polynomial is multilinear
in those indicators and equals det L by matrix-tree. Its derivative in
coordinate e counts trees containing e after removing that edge's factor.
Multiplying by its indicator gives the participation parity P_e, including
absent-edge and disconnected-graph cases. Differentiating a determinant
gives `P_e=A_e b_e^T adj(L)b_e`. The adjugate of symmetric L is symmetric,
so its off-diagonal terms cancel in the quadratic form in characteristic
two. Since b_e has its two endpoint coordinates equal to 1 (or one if an
endpoint was deleted), `P_uv=A_uv(d_u+d_v)`, with `d_n=0`.

This establishes a full, zero-credit static adapter: define
`D={u:d_u=1}`. The removed edge set is exactly `E(G) intersect delta(D)`.
Thus each output contains both complete induced graphs on D and its
complement. Corank L at least two forces all cofactors zero. The first
image is contained in the co-bipartite graphs; equality with that class is
not asserted. No conclusion about subsequent cuts follows from this
first-step description: their diagonal cofactor vectors are recomputed.

For every n>=3 the complete graph is fixed. Symmetry of K_n makes the
participation number of each edge `2 n^(n-3)`: count all `n^(n-2)` labelled
trees and their n-1 edges, then divide by `n(n-1)/2`. This number is even.
For n=1 the only graph is fixed, and for n=2 the two graphs swap.

There is also a genuine non-complete recurrent obstruction at n=4. If G
is the path with edges `{01,03,12}`, its only spanning tree is itself, so
STC(G) is its complement `{02,13,23}`, also a path. The next step returns
G. In the frozen bit encoding this is `13 -> 50 -> 13`. Therefore the
unqualified all-n claim that the complete graph is the only core is false.

The pilot proves only finite facts: the cores at n=3,5,6 are the singleton
complete graph, and their maximum tails are 2,4,4; at n=4 the core has
13 states, one fixed point and six two-cycles, with maximum tail 3.
Nothing here proves a uniform four-step bound, or classifies the core for
arbitrary n. Even the observed unique maximum-fibre target K_n is not an
all-n extremal theorem: that fibre counts all graphs whose participation
cut is empty and still requires an evaluated enumeration.

Disposition: `KILL_INCOMPLETE_GLOBAL_CONJUNCTION / NO_PROMOTION`.
The static cut adapter, valid small-n exception and finite table are retained.
No source-completeness or independent-gate claim accompanies this closure.

## PCG — old slices and explicit failure of involutivity

Every r=2 map is coordinate reversal, hence an involution with p^2 fixed
points, `(p^4-p^2)/2` two-cycles and singleton fibres. Those three fixed
pilot boxes are transparent deducted controls, not three new systems.
Characteristic two, excluded before pilot, turns permanent into determinant;
the map is then the transpose of the usual adjugate. Classical adjugation
identities consume that parameter slice completely.

For odd p, permanent is multilinear in each entry. Therefore the coordinate
minor formula is exactly `per(A+E_ij)-per(A)`, even when the increment wraps
modulo p. This second implementation cross-checks every output coordinate
of every matrix in the full boxes. It checks the literal **untransposed**
gradient, not a support version or a signed cofactor map.

At r=p=3 there are 41 fixed points, 468 two-cycles, 72 four-cycles and
288 six-cycles, altogether 2,993 recurrent states. The full six-cycle

```
849 -> 9810 -> 851 -> 3249 -> 850 -> 16371 -> 849
```

uses row-major base-three encoding, first entry most significant. All six
states are distinct. It disproves a universal period-at-most-two statement.
The maximum tail is six; one complete entrance path is

```
3202 -> 19075 -> 16406 -> 7038 -> 2924 -> 243 -> 0.
```

The unique largest finite fibre in this box is the zero fibre, of size 211.
Neither a formula for this extremum for arbitrary p/r nor a global temporal
identity is proved. Classifying permanental critical points at a single
field/size, or writing the gradient equations, is not the missing evaluated
two-axis theorem. No enlargement to 3x3/F5 was attempted.

Disposition: `KILL_INCOMPLETE_GLOBAL_CONJUNCTION / NO_PROMOTION`.

## UMP — triple dynamics is a fully deducted affine action

Distinct unordered pairs in a three-point set have distinct sums: equality
of two pair sums would force equality of their nonshared points. Thus UMP
preserves every three-point set's cardinality. If S={a,b,c} and s=a+b+c,

`UMP(S) = (s-S)/2`.

The sum of the three output points is again s. Consequently the same affine
map `x -> (s-x)/2` acts on every subsequent step. If p is not three, put
`c0=s/3`; all iterates are

`UMP^t(S) = c0 + (-1/2)^t (S-c0)`.

The period is exactly the multiplicative order of -1/2 modulo the scalar
stabilizer of the centred set. In particular it divides `ord_p(-1/2)`.
For p=3, the map is translation by -s, so the period divides three. This
works in every affine dimension. It is an elementary scalar/translation
action, not an untransferred temporal contribution. It explains, for
example, the three-point period-three signals over F7 and F3^2 and the
period-five three-point signals over F11.

Empty and singleton inputs go to empty; a pair goes to its midpoint and
then empty. These observations do not characterize all larger subsets.
In the frozen F11 box the four-point starting set `{0,1,2,3}` has the
genuine period-ten orbit (binary subset encoding):

```
15 -> 326 -> 1584 -> 1046 -> 329 -> 1049 -> 550 -> 553 -> 1360 -> 864 -> 15.
```

The maximum tail in that box is four. Its core has one fixed point,
33 five-cycles and 11 ten-cycles. Thus an all-subset period-at-most-two
claim is false, and the three-point affine adapter does not classify the
remaining core. Across the tested boxes, empty is the unique maximum-fibre
target, but no evaluated all-parameter maximum-fibre theorem is proved.
The one-step condition is a restricted representation-count constraint,
not a solution of its inverse enumeration.

Disposition: `KILL_INCOMPLETE_GLOBAL_CONJUNCTION / NO_PROMOTION`.

## Desk proof clarification

The NCS proof in intake also verifies its stated core: S cannot be contained
in any two-dimensional plane Z+L, so it maps to zero; zero maps to S.
Nilpotent lines L map to themselves. Thus its global one-step entrance
bound is exact (for example Z is transient). The Gaussian-binomial sum
used there is

`1+(q^3+q^2+q+1)+(q^4+q^3+2q^2+q+1)+(q^3+q^2+q+1)+1`.

This gives exactly the intake polynomial. A correct evaluated inverse
does not repair its completely transferred centralizer time axis.

SRS and QSZ are closed by the full intake arguments, with no numerical
verification claimed for their unexecuted carriers. They remain desk
deductions, not an extra 59,387-state execution or independent proof audit.

## Final boundary

All six literals close `NO_PROMOTION`; only STC, PCG and UMP were executed.
No full new conjunction survived, so there is no author admission package,
independent candidate review, paper ID, reserve or manuscript. Negative
findings and the original complete boxes are preserved. This bounded task
does not authorize a thirteenth slate.
