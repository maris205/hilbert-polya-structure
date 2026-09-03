# Hostile Review A — Boolean Gram Closure

**Role:** independent theorem, source, boundary, executable, and PDF attack on
the immutable author Round-0 package.  
**Decision:** `ACCEPT_INTERNAL`.  
**Findings:** `0 Critical / 0 Major / 0 Minor`.  
**Theorem verdict:** `PROVABLE AS STATED`.  
**Lifecycle:** `HOLD_EXTERNAL`.

## Pinned Round-0 input

```text
1a1ca296a922d02a12fe8d01ae3c4122eee892ef5f6a5c83e801c218247cc197  main.tex
806c750e41c8226b62fad89a9273859257bf9a882e0a5a1e8b43bf4714d0c7e3  references.bib
1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1  main.pdf
1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1  main_round0_original.pdf
eef567a25b0a6daefdbe926218b4c526392230abaec1033aa7b749e385600abc  verify_p171.py
bc3ba0e2b647ff5c888ad7534ef0088398cc7f58b2b71bde9688e3bc9e11e617  verification_output.txt
```

The review began from the literal Boolean-semiring update and reconstructed
both theorem axes before consulting the author transcript.  The earlier
hostile re-entry gate is candidate-selection evidence, not one of the two
manuscript reviews.

## Independent mathematical attack

### First image and the doubling identity

For a source matrix `A`, the entry of `G=AA^T` at `(i,j)` is one exactly
when rows `i` and `j` share a column.  Hence `G` is symmetric; every vertex
incident with an edge has a loop, and a vertex has a loop precisely when its
row is nonempty.  Once the orbit reaches `G`, symmetry gives

```text
Gamma(G^r) = G^r (G^r)^T = G^(2r).
```

Induction therefore yields `Gamma^t(A)=G^(2^(t-1))` for every `t>=1`.
There is no hidden commutativity assumption: a Boolean power of the single
symmetric matrix `G` is again symmetric, so the transpose equality is
literal at every step.

On an active component, all vertices have loops.  Thus `(G^r)_(ij)=1` iff
there is a path of length at most `r` from `i` to `j`: loops pad a shortest
path to length exactly `r`.  The power first becomes the fully looped clique
when `r` reaches the component diameter.  Inactive vertices remain unlooped
isolates under every power.  This proves the endpoint and shows that the
first stable orbit time after the source is the least `t>=1` satisfying
`2^(t-1)>=D(G)`.

The manuscript's clock treats fixed sources separately.  For every nonfixed
source it is consequently

```text
1 + ceil(log_2 D(G)),
```

with the stated zero ceiling term at `D=0` or `D=1`.  This convention is
necessary: a nonfixed source can have an already-complete first image and
then has depth one.  It does not create a logarithm-of-zero defect.

### Recurrence, census, and sharp height

If `A=AA^T`, then `A` is symmetric.  A nonzero row forces its diagonal entry,
and symmetry plus `A=A^2` makes the active relation transitive.  Its active
components are therefore fully looped cliques.  Conversely, a disjoint union
of fully looped cliques and unlooped isolates is symmetric and idempotent, so
it is fixed.  Since every source reaches such a state, recurrence contains no
longer cycles.

Choosing `k` active vertices and partitioning them gives
`sum_k binom(n,k) B_k`.  The standard distinguished-element bijection gives
`B_(n+1)`: in a partition of `[n]` together with a new point, the other
members of the new point's block are precisely the inactive vertices.  All
periodic points are fixed, so the printed Artin--Mazur zeta conversion is
correct.

The universal diameter bound is `D(G)<=n-1`.  The proposed witness is also
literal: give the edges of the path `1-2-...-n` distinct column labels, put
in row `i` the incident edge labels, and leave one of the `n` columns empty.
Two rows intersect exactly when the path vertices coincide or are adjacent,
so `AA^T` is the fully looped path of diameter `n-1`.  The source is not
fixed, including at `n=2`, and the clock reaches
`1+ceil(log_2(n-1))`.  At `n=1`, direct inspection gives two fixed matrices
and height zero.  Thus both the upper bound and every boundary of the sharp
height are attained.

### Every-target ordered-column fibre

Let `C_r` be the support of labelled column `r` of a prospective source.
Then

```text
AA^T = union_(r=1)^n C_r x C_r.
```

A nonsymmetric target, or a target edge missing an endpoint loop, cannot be
such a union.  For a compatible target `H`, a column creates no forbidden
one exactly when its support is an allowed fully looped clique of `H`, with
the empty support included.  Equality with `H` then holds exactly when every
loop atom and every edge atom is contained in at least one chosen support.

For a set `S` of atoms, `c_H(S)` counts allowed supports avoiding every atom
in `S`; because the `n` columns are independently labelled, the number of
ordered column choices missing all of `S` is `c_H(S)^n`.  Ordinary
inclusion--exclusion gives the displayed every-target fibre.  This argument
is bijective: every counted support sequence produces one source matrix and
every source recovers its ordered support sequence, so there is neither a
factorial quotient nor an unaccounted multiplicity.

The image criterion is the existence statement behind the same identity.
Nonempty supports in a witnessing sequence cover all atoms; conversely, an
allowed cover with at most `n` cliques can be placed into labelled columns
and padded by empty columns.  Repetitions are permitted.  Singleton loop
atoms correctly force isolated active vertices to receive a column.

The looped `K_(2,3)` obstruction is sound.  Its triangle-free graph admits
no allowed nontrivial clique larger than an edge, so its six edges need six
nonempty column supports.  With only five columns it is compatible but not
in the image.  The zero target, isolated-loop targets, repeated columns, and
empty padding all agree with the formula.

## Boundary and counterexample pressure

The proof attack separately checked the following possible failure modes:

- a zero source and a source with empty rows;
- `n=1`, `n=2`, fixed sources, and nonfixed sources with `D<=1`;
- nonsymmetric targets and symmetric edges without endpoint loops;
- isolated loop atoms, empty columns, repeated supports, and labelled-column
  order;
- compatible targets whose clique-cover number exceeds the available column
  count;
- an alleged recurrent symmetric idempotent with a nonclique component.

None produces a counterexample.  In particular, the clock is measured from
the original source rather than from its first Gram image, and the fibre
formula counts matrices rather than unlabelled set representations.

## Exact-control replay

A fresh standard-library process reran the unchanged author verifier.  Its
output matched the frozen transcript byte for byte:

```text
assertions: 594,955
verifier SHA-256:  eef567a25b0a6daefdbe926218b4c526392230abaec1033aa7b749e385600abc
transcript SHA-256: bc3ba0e2b647ff5c888ad7534ef0088398cc7f58b2b71bde9688e3bc9e11e617
decision: AUTHOR_ROUND0_PASS
```

The program exhausts all `2^(n^2)` sources and all `2^(n^2)` targets for
`1<=n<=4`, compares literal and formula fibres, independently checks cover
feasibility, and replays the sharp path family through `n=64`.  The census
`2,5,15,52` agrees with `B_(n+1)`.  These finite tests are falsification
evidence only; the all-parameter verdict above rests on the uniform proofs.
Review B must use an independently implemented carrier rather than this
author program.

## Source, ownership, build, and PDF audit

The cited primary surfaces support the roles assigned to them.  Fitting's
Theorem 8 states the monotone Boolean Gram-power chain and Example 9 supplies
arbitrarily long strict growth across dimensions.  Erdős--Goodman--Pósa own
the set-intersection/complete-subgraph-cover dictionary.  Chen--Song--Tao--
Zhang explicitly formulate symmetric Boolean factorization `M=WW^T` and
its clique-cover interpretation.  Warshall, Kim, Szpilrajn--Marczewski,
Bell enumeration, Boolean powers, and inclusion--exclusion are likewise
properly treated as background.  The manuscript assigns none of those
mechanisms contribution credit and makes no novelty claim.  The bounded
owner-search non-hit is not used as positive evidence.

The two retained source-only Round-0 builds match the canonical PDF under
SHA-256.  Settled logs contain no actual warning, bad box, unresolved
citation/reference, rerun request, or fatal diagnostic; appearances of the
words `warning` and `rerun` are package names or BibTeX's zero-warning
counter.  The PDF has three A4 pages, all 25 font rows are embedded,
subsetted, and Unicode mapped, identifying metadata fields are blank, and
there is no encryption, form, JavaScript, attachment, or raster image.  The
author's rendered-page inspection records no clipping, collision, overflow,
or malformed glyph.

## Findings

### Critical

None.

### Major

None.

### Minor

None.

## Recommendation

Accept the theorem package without repair or weakening.  Preserve the
Round-0 source and PDF, obtain the required independently implemented
Review B, and then freeze the round copies and final manifest.  The direct
mechanism owners keep this a deliberately owner-thin internal note;
external status remains `HOLD_EXTERNAL`, and this review grants no posting
or submission permission.
