# P170 replacement breadth lane

**Date:** 2026-09-03  
**Fresh forms tested:** 18  
**Fresh-lane verdict:** `NO_FRESH_SURVIVOR / REENTER_RPS_RESERVE`  
**External status:** `HOLD_EXTERNAL`

The lane deliberately left integer partitions and inventory maps after the MPD
kill.  It tested labelled binary relations, hypergraph families, binary words,
and finite-field pairs.  A candidate could survive only with (i) an early,
stable all-size temporal anomaly, (ii) an independent exact inverse/census/zeta
axis, and (iii) no proof transfer from P1--P169 or a direct primary owner.

`breadth_pilots.py` exhausts all `n x n` relations through `n=4`, all families
of nonempty subsets through four vertices, all binary words through length 10,
and all pairs over `F_p` for `p=2,3,5,7,11,13,17,19`.  It made **507,153**
exact closure/orbit assertions.  Two cold runs were byte-identical with
transcript SHA-256
`e03ca367814363fb25543d0ca4ba7c8a74c4be1ba1fb8a02266315badda6b3ba`.
The canonical payload SHA-256 is
`a16de1f5676adc53298c2f8ef7ef40830dba794cfe38b813e9dbc9e8bde193e8`;
the verifier SHA-256 is
`6f541a21d16255b23098359dcf3aa7a396bb51126e76a6f17d0d898f7a4253df`.
These are bounded falsification results, not ownership evidence.

## Implemented relation forms

For a Boolean relation matrix `A`, write `R_i` for row `i`, `r_i=|R_i|`, and
`c_j` for column `j`'s weight.

| ID | Literal update | strongest box signal | decisive gate |
|---|---|---|---|
| `R01` | `B_ij=1` iff `R_i` is a proper subset of `R_j` | at `n=4`: image 219, only the empty fixed state, 74 period-two states, tail 2 | tempting “second image is always a weak order” law holds through `n=4` but a random `n=5` counterexample appears immediately; no stable spine |
| `R02` | `B_ij=1` iff `r_i<r_j` | image sizes `1,3,13,75`, the ordered Bell numbers; one fixed state and all other image states in reversal two-cycles; maximum tail 1 | exact one-step statistic collapse to a weak order; target fibres are a routine sum over strictly increasing row weights, so no temporal axis |
| `R03` | `B_ij=1` iff `r_i<c_j` | at `n=4`: image 2,721, 15 fixed points, 1,522 period-two states, sharp observed tail 3 | strongest fresh signal, but inverse cells are arbitrary binary matrices under coupled row/column-degree inequalities; no uniform fibre/census theorem emerged, and random larger boxes do not expose a clean clock law |
| `R04` | `B_ij=1` iff `i!=j` and `R_i` meets `R_j` | image sizes `1,2,8,64`, fixed-only recurrence, tails `1,2,3,3` | row-intersection graph is a static intersection-graph projection with enormous collapsing fibres; clock already flattens |
| `R05` | `B_ij=<R_i,R_j> mod 2` | at `n=4`: image 996, periods 1--4, tail 3 | classical Boolean Gram map `A -> AA^T`; direct linear-algebra engine and collision with P143/P168-style subspace/Gram machinery |

`R03` is retained only as an unproved future reserve.  A bounded phrase search
did not locate its exact iteration; that non-hit has zero weight.  Its current
inverse problem is harder than its observed temporal signal and therefore it
does not meet the present paper gate.

## Implemented hypergraph forms

The carrier is the set of all families of nonempty subsets of `[n]`.

| ID | Literal update | `n=4` signal | decisive gate |
|---|---|---|---|
| `H01` | clutterize, then take all minimal transversals | 167-state image; 13 fixed and 154 period-two states; tail 1 | exact blocker involution on clutters is classical; see Cordovil--Fukuda--Moreira, [*Clutters and matroids*](https://doi.org/10.1016/0012-365X(91)90364-8), and the modern blocker literature |
| `H02` | adjoin all nonempty pairwise intersections | 4,542 fixed closures; tail 2 | ordinary meet-subsemilattice closure by repeated squaring |
| `H03` | adjoin all pairwise unions | 2,480 fixed closures; tail 2 | ordinary join-subsemilattice closure by repeated squaring |
| `H04` | adjoin all nonzero pairwise symmetric differences | 67 fixed states; tail 2; maximum fibre 23,552 | span closure in an `F_2` vector space; same sumset/squaring engine as occupied P97 and nearby affine lanes |
| `H05` | clutter of unions of intersecting edge pairs | image sizes `1,1,2,17`; fixed only at empty; tails `1,1,2,3` | very high information collapse (maximum `n=4` fibre 26,778) and no target-resolved inverse; line/intersection-component coalescence silhouette is owner-dense |

## Implemented word forms

| ID | Literal update | length-10 signal | decisive gate |
|---|---|---|---|
| `W01` | toggle a bit iff the same symbol appeared earlier | image 512, all image states in two-cycles, tail 1 | prefix-used-symbol statistic collapse |
| `W02` | mark the left-to-right strict record minima of suffixes | image 201, unique fixed state, sharp observed tail 10 | exact literal collision with P139: the suffix-record mask is the Chen--Fox--Lyndon factor-start mask |
| `W03` | cyclically mark isolated bits whose two neighbours agree | image 217, 31 fixed states, tail 2 | local cellular-automaton projection beside P164 and mature elementary-CA ownership; no growing clock |
| `W04` | replace every linear run by its run-length parity | image 89, 22 fixed states, tail 2 | static run projection; image sizes are Fibonacci, but the mechanism and proof transfer directly to the P117/P147 run lanes |

The apparent best word signal, `W02`, is not merely similar to P139.  P139's
verifier already checks equality of its Duval factor-start mask with this
exact suffix-record definition, and its source ledger credits
Mantaci--Restivo--Rosone--Sciortino's static theorem.

## Implemented finite-field pair forms

| ID | Literal update on `F_p^2` | observed signal through `p=19` | decisive gate |
|---|---|---|---|
| `F01` | `(x,y)->(x+y,xy)` | every fibre at most two, but periods vary among `1,4,6,8,10`; maximum tails `2,4,4,8,13,18,14,26` | inverse is the classical quadratic discriminant; temporal graph is arithmetically irregular and has no uniform theorem spine |
| `F02` | `(x,y)->(x+y,x^2+y^2)` | fibres at most two; period sets and tails vary erratically with `p` | polynomial reparameterization of the same elementary-symmetric data; no independent axis |
| `F03` | `(x,y)->(x+y^2,y+x^2)` | fibres at most four; variable periods and tails | generic planar polynomial dynamics; too close to P125/P150/P153/P161 without a stable exceptional law |
| `F04` | `(x,y)->(x+inv0(y),y+inv0(x))` | fibres grow to `p`; short but prime-dependent periods | totalized-inverse singular stratification is already the P150/P168 neighbourhood; early signal is weaker |

## Decision and reserve handoff

The fresh lane produced one exact internal collision (`W02`), four direct
classical closure/projection mechanisms, several flat statistic maps, and
finite-field maps whose temporal data vary before a uniform theorem appears.
`R03` is the only genuinely fresh-looking reserve, but it lacks both a proved
all-size clock and a tractable independent inverse/census axis.  It is not
promoted on bounded non-hit evidence.

Therefore the honest result is

```text
NO_FRESH_SURVIVOR
REENTER_RPS_RESERVE_FOR_AN_INDEPENDENT_HOSTILE_GATE
HOLD_EXTERNAL
```

No paper directory is allocated from these eighteen forms.
