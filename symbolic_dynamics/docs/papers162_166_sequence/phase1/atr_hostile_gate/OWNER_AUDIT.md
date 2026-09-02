# ATR independent owner and collision audit

**Decision:** `KILL`  
**External status:** `HOLD_EXTERNAL`  
**Novelty or priority claim:** none  
**Search date:** 2026-09-03 UTC

## 1. Primary-source audit of the assignment lineage

The bibliographic records are direct and verified:

- H. W. Kuhn, *The Hungarian Method for the Assignment Problem*, **Naval
  Research Logistics Quarterly 2** (1955), 83--97,
  DOI [`10.1002/nav.3800020109`](https://onlinelibrary.wiley.com/doi/10.1002/nav.3800020109).
  The publisher page confirms author, title, date, volume, and pages.  A
  [primary scan](https://www.math.utoronto.ca/mccann/1855/KuhnNRL55.pdf)
  was inspected at the construction of the initial cover and at Routine II.
- James Munkres, *Algorithms for the Assignment and Transportation
  Problems*, **Journal of the Society for Industrial and Applied Mathematics
  5** (1957), 32--38,
  DOI [`10.1137/0105003`](https://epubs.siam.org/doi/10.1137/0105003).
  The SIAM record confirms the metadata and its citation of Kuhn.

### Exact subtraction boundary

Kuhn's formulation uses dual row/column covers and an initial cover chosen
from row maxima or column maxima according to their total.  The primary text
therefore does **not** literally own the exact finite endomorphism
`A -> R(A)^T`, nor does it state ATR's sequential row-minimum then
column-minimum two-pass identity.  It does own the assignment-method lineage
in which row/column additive potentials and equality-producing cost
reductions are basic.

Accordingly, the following receive zero contribution credit:

- subtracting a constant row potential or column potential;
- creating a zero in each row and column by the familiar two-pass cost
  preprocessing;
- preservation of the assignment objective up to additive potentials;
- describing the twice-reduced matrix as a reduced-cost core.

ATR does not claim an assignment algorithm, matching optimality theorem,
covering/augmentation step, or complexity improvement.  The safe historical
claim is “standard Hungarian/Kuhn--Munkres cost-reduction lineage,” not
“Kuhn 1955 states the exact ATR iteration.”

## 2. Bounded direct-map search

The hostile audit repeated and broadened exact/equivalent searches around:

```text
"row normalization transpose" dynamics matrix minima
"subtract row minimum" transpose iterate
alternating row column minimum reduction finite matrix
tropical normalization transpose functional graph
preimages Hungarian reduced cost matrix
zero-cover fibres row column reduced matrices
```

The search included publisher records, the primary Kuhn scan, mathematical
formula searches, and nearby normalization literature.  No inspected source
stated all of the following together:

1. the literal self-map on the bounded integer matrix alphabet;
2. the exact two-step functional graph;
3. the every-target zero-cover/potential fibre polynomial; and
4. the exact depth census.

This is only a bounded non-hit.  It does not establish novelty, priority,
ownership, or freedom to circulate.  More importantly for this gate, lack
of an exact direct-map hit does not restore the standard temporal primitive
to the contribution ledger.

## 3. Internal P1--P161 collision audit

### P116 — vocabulary collision only

`papers/116-max-plus-switching-induced-growth` studies random products of a
fixed pair of `2 x 2` max-plus matrices, projective states, reset words, and
growth laws.  ATR has no matrix products, random switching, pressure, or
Lyapunov/growth axis.  “Tropical/max-plus” and additive normalization are
shared vocabulary, not a mechanism collision.

**Result:** no internal kill from P116.

### P127 — significant packaging collision

`papers/127-parity-transpose-looped-digraphs` acts on full binary matrix
spaces, uses a state-dependent transpose update, identifies a recurrent
image, enumerates periods and zeta data, and gives every-target fibre rules.
Its parity/rank-one mechanism and possible periods through four are different
from ATR's minima.  Thus there is no literal conjugacy, but full-matrix,
transpose, image/fibre, cycle, and zeta packaging is already occupied.

**Result:** substantial zero-credit background; reinforcing collision, not
the decisive one by itself.

### P143 — decisive architectural collision

`papers/143-boolean-row-inclusion-residual` maps a full Boolean matrix in one
step onto a structural core (the labelled preorders), acts as transpose on
that core, has only fixed points and strict two-cycles, derives fixed-iterate
and zeta counts, and completes the note with an every-target inverse atlas.
ATR changes the projection from relational self-residuation to two-pass
minimum reduction and changes the fibre coordinates from quotient-poset
embeddings to zero-cover potentials.  Nevertheless its theorem silhouette is
the same:

```text
full matrix carrier
    -> constant-depth projection/core
    -> transpose involution on the core
    -> fixed + strict 2-cycle census and zeta
    -> every-target inverse atlas.
```

Because the ATR temporal projection is separately zero-credit under the
Hungarian reduction audit, the distinct local fibre calculation is not
enough to support a second paper using this occupied silhouette.

**Result:** decisive internal allocation kill.

## 4. Residual ledger

| item | mathematical status | paper credit after subtraction |
|---|---|---|
| two-pass landing on row/column-zero core | correct | zero: standard cost reduction |
| transpose on the core, periods 1 and 2 | correct | zero: elementary and P143-occupied |
| recurrent/fixed inclusion--exclusion | correct | zero: elementary IE |
| one-step product fibre | correct | zero/thin |
| two-step zero-cover/potential polynomial | correct and placement-sensitive | positive but narrow |
| exact depth shells | correct | zero/thin after temporal subtraction |
| closed source-side depth IE from hostile audit | correct | useful control, not a new axis |

The sole clear positive residue is the target-wise zero-cover polynomial.
It cannot furnish both the temporal and independent structural axes demanded
by the P162--P166 problem anchor.

## 5. Owner ruling

`KILL_KUHN_MUNKRES_INITIALIZATION_AND_P143_CORE_TRANSPOSE_TEMPLATE`.

This ruling does not say that Kuhn or Munkres wrote the exact ATR map or its
inverse formula, and it makes no global novelty assertion.  It says that the
mandatory subtraction leaves too little independent mathematical content
for a new batch slot.  Status remains `HOLD_EXTERNAL`.
