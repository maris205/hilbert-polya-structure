# Hostile Review B — Boolean Gram Closure

**Role:** independent nonauthor Review B of the unchanged Round-1 input.  The
literal map, both theorem proofs, all boundary conventions, and owner
subtraction were cold-read before the author control was replayed.  A
reviewer-owned carrier and three-way fibre implementation were then used for
targeted falsification.  Review B changes no manuscript source, bibliography,
author verifier, frozen transcript, PDF, or author ledger.  
**Decision:** `ACCEPT_INTERNAL`.  
**Findings:** `0 Critical / 0 Major / 0 Minor`.  
**Theorem verdict:** `PROVABLE AS STATED`.  
**Lifecycle:** `GREEN_OWNER_THIN / HOLD_EXTERNAL`.

## Pinned Round-1 input

Review A accepted the Round-0 source without a repair, so the Round-1 input is
byte-identical to the author freeze:

```text
1a1ca296a922d02a12fe8d01ae3c4122eee892ef5f6a5c83e801c218247cc197  main.tex
806c750e41c8226b62fad89a9273859257bf9a882e0a5a1e8b43bf4714d0c7e3  references.bib
1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1  main.pdf
1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1  main_round0_original.pdf
eef567a25b0a6daefdbe926218b4c526392230abaec1033aa7b749e385600abc  verify_p171.py
bc3ba0e2b647ff5c888ad7534ef0088398cc7f58b2b71bde9688e3bc9e11e617  verification_output.txt
cd9935b8e7d5456a1ae203389ec6f375cae0a2bb6d07360ca14ae6773ac2d0f3  HOSTILE_REVIEW_A.md
```

The pre-review paper-local manifest passes in full.  Reviewer evidence is
isolated under `docs/papers167_171_sequence/reviews/p171_b/`; this report is
the only Review-B addition to the paper directory.

## Independent mathematical attack

### Literal identity and the diameter clock

For an arbitrary source relation `A`, the first image `G=AA^T` has

```text
G_(ij)=1  iff  row_i(A) and row_j(A) intersect.
```

It is symmetric, a row is active exactly when its diagonal entry is one, and
every active vertex has a loop.  Symmetry is preserved by powers of this one
matrix, so

```text
Gamma(G^r)=G^r(G^r)^T=G^(2r).
```

Induction gives `Gamma^t(A)=G^(2^(t-1))` for every `t>=1`; there is no
commutation step between two unrelated matrices.  In a looped active
component, a shortest path of length at most `r` can be padded by loops to a
walk of length exactly `r`.  Thus the time-`t` relation joins exactly those
pairs at graph distance at most `2^(t-1)`, and the endpoint is the fully
looped clique completion of each active component.

The manuscript correctly separates fixed sources before taking a logarithm.
For a nonfixed source, the first image may already be fixed with either
`D(G)=0` or `D(G)=1`; in both cases its depth is one, as the declared zero
ceiling term gives.  For `D>=2`, the first stable time is the least `t>=1`
with `2^(t-1)>=D`, namely `1+ceil(log_2 D)`.  The path-incidence source uses
`n-1` edge columns and one empty column, has first image the fully looped path
of diameter `n-1`, and is nonfixed even at `n=2`.  It therefore attains the
printed height.  Direct inspection at `n=1` gives two fixed sources and
height zero.

### Recurrence, Bell count, and zeta

If `A=AA^T`, then `A` is symmetric; every nonzero row contains its diagonal;
and `A=A^2` makes the active relation transitive.  Each active component is
therefore a fully looped clique, while inactive vertices are unlooped
isolates.  The converse is symmetric idempotence.  Since every source reaches
such a state, no longer cycle is possible.

Choosing the `k` active labels and partitioning them gives
`sum_k binom(n,k) B_k`.  The distinguished-element bijection is complete:
place every inactive label in the block of a new point and retain each active
clique as a separate block.  This includes the empty active set and proves
the value `B_(n+1)`.  Because every periodic point is fixed,
`#Fix(Gamma^r)=B_(n+1)` for all positive `r`, so the Artin--Mazur zeta factor
is exactly `(1-z)^(-B_(n+1))`.

### Every-target inclusion--exclusion

Let `C_r` be the labelled support of source column `r`.  The identity

```text
AA^T = union_(r=1)^n C_r x C_r
```

is bijective at the level needed for the fibre count: an ordered sequence of
`n` supports is exactly one Boolean source matrix.  A target must be symmetric
and every incident endpoint must carry a loop.  Under this compatibility
condition, a column creates no forbidden one precisely when its support is an
allowed fully looped clique, with the empty support allowed.

The loop and unordered-edge atoms are exactly the remaining obligations.
For a selected atom set `S`, every labelled column must avoid covering each
atom in `S`, giving `c_H(S)` choices per column and `c_H(S)^n` ordered
sequences.  Inclusion--exclusion over missed-atom events is therefore the
printed formula.  Empty and repeated supports need no quotient, and isolated
loops are retained by their singleton atoms.  The zero, identity, looped
three-path, and all-one targets independently give fibres `1,6,30,175`.

### The `<=n` image criterion and the looped `K_(2,3)` boundary

Every source supplies at most `n` nonempty column supports covering every
target atom.  Conversely, any allowed cover of size at most `n` can be placed
in labelled columns and padded by empty supports.  This proves the criterion
in both directions; repeats do not create an extra case because deleting a
duplicate does not reduce the covered atom set.

The fully looped `K_(2,3)` on five labels is compatible.  It is triangle-free,
so every nontrivial allowed clique is one edge.  Its six distinct edge atoms
therefore require six nonempty supports, while a `5 x 5` source has only five
columns.  The exact cover number is six and both the ordered coverage count
and inclusion--exclusion fibre are zero.  Review B additionally exhausted all
1,024 fully looped graphs on five labelled vertices: precisely ten have cover
number six, and all ten are the labelled copies of `K_(2,3)`.  Hence the
printed example is a genuine first-dimension compatible nonimage boundary,
not a loop convention artifact.

## Independent exact controls

### Author-control double replay

Two fresh processes reran the unchanged author verifier.  Their 952-byte
outputs matched one another and `verification_output.txt` byte for byte:

```text
assertions: 594,955
verifier SHA-256:  eef567a25b0a6daefdbe926218b4c526392230abaec1033aa7b749e385600abc
transcript SHA-256: bc3ba0e2b647ff5c888ad7534ef0088398cc7f58b2b71bde9688e3bc9e11e617
decision: AUTHOR_ROUND0_PASS
```

### Reviewer-owned carrier and inverse engine

The Review-B program is retained at
`docs/papers167_171_sequence/reviews/p171_b/verify_review_b.py`.  It imports
no author, gate, scouting, or Review-A code.  Unlike the packed-row author
engine, it represents a matrix as an ordered tuple of column-support
frozensets and a relation as a frozenset of ordered pairs.  It predicts
iterates from independently constructed shortest-path balls.

For every target through `n=4`, it compares three separately implemented
counts:

1. the literal histogram of all ordered source-column tuples;
2. a coverage-state dynamic program over labelled columns; and
3. atomwise inclusion--exclusion.

It also compares fibre positivity with a minimum nondominated-clique cover,
checks every arbitrary invalid codomain relation, reconstructs every clock
and fixed iterate, proves the Bell-transform numbers computationally through
`n=20`, follows the sharp path family through `n=64`, and performs the full
five-vertex looped-graph cover scan above.  Two fresh reviewer processes were
byte-identical:

```text
assertions: 729,535
verifier SHA-256:  61b6897e90f1f8acf5a33b34fdfb48e13b7d1bf0c2c0abbf5dac74c9d580cc7d
canonical SHA-256: d0ce57fad9db938f07569d07aded3866f6c5672225720efb59ad8995846c219b
payload SHA-256:   72b0c2587814348a42748fbe00c0d3a69b6e4a4d3e6c8b66210c237a56d4281d
decision: REVIEW_B_INDEPENDENT_CONTROL_PASS
```

The complete reviewer census reproduces image sizes `2,5,18,113`, fixed
counts `2,5,15,52`, maximum fibres `1,7,175,17887`, and the author depth
histograms through `n=4`.  These programs are bounded falsification evidence;
the uniform verdict rests on the derivations above.

## Primary-source and ownership attack

The strongest owner surfaces were reopened rather than inferred from citation
titles.

- Fitting's author-hosted primary paper,
  [*Bisimulations and Boolean Vectors*](https://id144254.securedata.net/melvinfitting/bookspapers/pdf/papers/BisimBool.pdf),
  has Theorem 8 giving `A <= AA^T A` and the induced increasing alternating
  power chain; the paragraph preceding Example 9 explicitly says the strict
  chain can be arbitrarily long as dimension grows.  This owns the post-Gram
  Boolean-power growth mechanism.
- Erdős--Goodman--Pósa,
  [*The Representation of a Graph by Set Intersections*](https://doi.org/10.4153/CJM-1966-014-3),
  owns the graph set-intersection/complete-subgraph-cover dictionary used in
  the image interpretation.
- Chen--Song--Tao--Zhang,
  [*Symmetric Sparse Boolean Matrix Factorization and Applications*](https://doi.org/10.4230/LIPIcs.ITCS.2022.46),
  explicitly formulates `M=WW^T` over the Boolean semiring and interprets the
  columns of `W` as cliques.  This directly owns the symmetric-factorization
  and reconstruction framing.
- Warshall, Kim, Szpilrajn--Marczewski, Bell enumeration, Boolean transitive
  closure, edge clique covers, and inclusion--exclusion are likewise kept as
  background.

The manuscript assigns every one of these ingredients zero contribution
credit and does not call the residual conjunction novel.  The bounded search
did not expose a direct owner for both the literal feedback functional graph
and the complete fixed-width ordered fibre, but that non-hit has no positive
evidentiary weight.  The declared `GREEN_OWNER_THIN / HOLD_EXTERNAL` ceiling
is therefore appropriate.

## Source-only builds, PDF, and anonymity

Two Review-B directories began with only `main.tex` and `references.bib`.
Each ran `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.  Both settled logs have
zero actual warning, bad box, unresolved citation/reference, rerun request,
or fatal diagnostic.  Both PDFs match one another, the live canonical, and
the preserved Round-0 copy byte for byte:

```text
cold build 1: 1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1
cold build 2: 1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1
live main.pdf: 1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1
Round-0 copy:  1d7a74390c08d48d84364f0fe6cd221fe553e0c838b993d3dbabae6185d28fc1
```

The artifact has three A4 pages and 329,559 bytes.  All 25 font rows are
embedded, subsetted, and Unicode mapped.  Title, subject, keywords, author,
creator, and producer metadata fields are blank; there is no custom metadata
stream, encryption, form, JavaScript, embedded file, or raster image.
Extracted text contains no email, local path, affiliation, acknowledgment,
unresolved marker, review identity, or nonanonymous byline.

All three pages were rendered at 144 dpi and independently inspected.  The
theorem split, diameter convention, boxed fibre sum, union identity, small
fibre table, census, lifecycle line, bibliography URLs, running heads, and
page numbers are legible and inside the A4 page box.  No clipping, collision,
overflow, malformed glyph, broken link text, or orphaned heading was found.

## Findings

### Critical

None.

### Major

None.

### Minor

None.

## Recommendation

Accept P171 internally without source repair.  The complete theorem package
is provable as stated, the ordered fibre really counts labelled matrices, and
the `D<=1` and looped `K_(2,3)` boundaries are sound.  Preserve the explicit
zero-credit assignment to Boolean-power closure and symmetric factorization.
This review grants no external release, posting, or submission permission;
the lifecycle remains `GREEN_OWNER_THIN / HOLD_EXTERNAL`.
