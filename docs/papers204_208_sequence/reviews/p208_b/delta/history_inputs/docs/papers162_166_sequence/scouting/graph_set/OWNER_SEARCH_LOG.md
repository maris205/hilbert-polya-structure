# Bounded owner-search log — graph / hypergraph / set-system scout

**Search date:** 2026-09-02 UTC  
**Boundary:** P1–P161 plus all visible P157–P161 scout and kill ledgers  
**External state:** `HOLD_EXTERNAL`

This is an early primary-source owner gate, not a systematic review and not
novelty, priority, or freedom-to-operate evidence.  Search results were used to
subtract standard operations immediately.  Absence of an exact hit in this
bounded pass is recorded only as a non-hit.

## Queries actually used

The bounded web pass used the following literal combinations, with spelling
and notation variants:

```text
graph quotient vertex partition edge between cells quotient graph contraction
surjective graph homomorphism quotient graph direct image edges
iterated quotient graph vertex partition contraction dynamics
dyadic quotient graph iteration
number of graphs fixed quotient graph partition preimage
graph blow-up quotient partition enumerate graphs with given quotient
set system trace projection family subsets Sauer Shelah
direct image set family combinatorics map
image of a hypergraph vertex map quotient hypergraph
trace of a family restriction subset Sauer Shelah original
Edmonds Fulkerson blockers of clutters 1970
Mycielski Sur le coloriage des graphes 1955
Frucht Harary corona of two graphs 1970
Weichsel Kronecker product graphs 1962
Sabidussi graph multiplication Cartesian product 1959
```

Search-engine snippets were never treated as mathematical evidence.  The
records below link the article, publisher, repository, or DOI landing page.

## 1. `BQC` — consecutive-block graph quotient

### Primary records inspected

- Bubboloni, *Graph homomorphisms and components of quotient graphs*,
  Rendiconti del Seminario Matematico della Università di Padova 138 (2017),
  39–60, [DOI 10.4171/RSMUP/138-2](https://doi.org/10.4171/RSMUP/138-2).
  Section 3 defines a quotient by a vertex equivalence relation using the
  existence of an original edge between the two cells.  This owns the generic
  quotient operation and receives full credit.
- Hickingbotham, *The product structure of squaregraphs*, Journal of Graph
  Theory (2024), [DOI 10.1002/jgt.23008](https://doi.org/10.1002/jgt.23008).
  Its preliminaries define the loopless quotient on the blocks of a partition:
  distinct blocks are adjacent iff some original adjacent pair crosses them.
  This is exactly the one-step OR convention used by `BQC`, absent the special
  consecutive arithmetic partition.
- Parthasarathy, *Enumeration of Graphs with given Partition*, Canadian
  Journal of Mathematics 20 (1968), 40–47,
  [DOI 10.4153/CJM-1968-005-0](https://doi.org/10.4153/CJM-1968-005-0).
  This is a nearby graph-enumeration control.  It treats ordinary/bicoloured
  graphs with a given partition via Pólya methods; it does not supply the
  labelled every-target fixed-quotient fibre product in the scout's form.

### Subtraction and decision

The terms *quotient graph*, vertex identification, and the existential OR
across block pairs get zero credit.  The only retained conjunction is:

1. the nested consecutive partition has the exact semigroup
   `q_c^t(i)=floor((i-1)/c^t)+1`, a pointwise endpoint-coalescence clock, and
   sharp global height `ceil(log_c n)`; and
2. every time and every supported labelled target have the exact source-edge
   polynomial recorded in `SCOUT.md`, including the short last block and empty
   or impossible targets.

No inspected record states that exact dyadic/`c`-adic self-iteration and
target-resolved weighted fibre atlas together.  This is only a bounded
non-hit.  Because the retained proof is elementary once the quotient is fixed,
the candidate remains `SELECT_FOCUSED_AMBER`, not green.

## 2. `SFC` — direct image of a family under block coalescence

The queries for direct images of families and quotient hypergraphs did not
locate a source with the exact nested product

```text
product_{A in G} (2^[product_{j in A}(2^s_j-1)]-1).
```

That non-hit does not rescue the system.  `SFC` is the direct-image/powerset
lift of the same finite map used by `BQC`: partition the source subsets by
their image, then choose a nonempty subcollection in every requested bin.
This is a complete internal proof-engine transfer, with additional proximity
to P97's relation-image carrier.  Decision:
`KILL_BQC_P97_DIRECT_IMAGE_ENGINE`.  No novelty inference is made.

## 3. `STP` — relabelled coordinate trace

### Primary records inspected

- Sauer, *On the Density of Families of Sets*, Journal of Combinatorial Theory,
  Series A 13 (1972), 145–147,
  [DOI 10.1016/0097-3165(72)90019-2](https://doi.org/10.1016/0097-3165(72)90019-2).
- Shelah, *A Combinatorial Problem; Stability and Order for Models and Theories
  in Infinitary Languages*, Pacific Journal of Mathematics 41 (1972), 247–261,
  [DOI 10.2140/pjm.1972.41.247](https://doi.org/10.2140/pjm.1972.41.247).
- Frankl and Pach, *On the Trace of Finite Sets*, Journal of Combinatorial
  Theory, Series A 34 (1983), 41–45,
  [DOI 10.1016/0097-3165(83)90038-9](https://doi.org/10.1016/0097-3165(83)90038-9).
  This record explicitly defines the trace of a family on `Y` as
  `{F intersect Y:F in family}`.

### Subtraction and decision

Restriction/trace and duplicate removal are standard.  Iterating the scout's
fixed relabelled deletion simply traces on the last `n-t` coordinates.  For
each target set there are `2^t` independent lifts; requiring a nonempty
selection yields `(2^(2^t)-1)^|G|`.  That is a correct exact fibre formula, but
after trace ownership it is a single independent-bin observation paired with
a forced rank schedule.  Decision: `KILL_DIRECT_TRACE_OWNER_THIN`.

## Decisive owner controls among the remaining systems

- `CBL`: Edmonds and Fulkerson, *Bottleneck Extrema*, Journal of Combinatorial
  Theory 8 (1970), 299–306, [primary PDF](https://web.vu.lt/mif/s.jukna/EC_Book_2nd/Edmonds-Fulkerson.pdf),
  define the blocker as the clutter of minimal sets meeting every member and
  state the corollary `b(b(C))=C`.  This directly owns the entire temporal
  theorem, so `CBL` is killed.
- `MYC`: Mycielski, *Sur le coloriage des graphes*, Colloquium Mathematicum 3
  (1955), 161–162,
  [DOI 10.4064/cm-3-2-161-162](https://doi.org/10.4064/cm-3-2-161-162),
  owns the named graph construction.  The scout's canonical labelling only
  makes its inverse `1/0`, so no independent axis remains.
- `COR`: Frucht and Harary, *On the Corona of Two Graphs*, Aequationes
  Mathematicae 4 (1970), 322–325,
  [DOI 10.1007/BF01844162](https://doi.org/10.1007/BF01844162), introduce the
  corona; attaching one leaf at every vertex is exactly corona with `K1`.
- `BDC`: Weichsel, *The Kronecker Product of Graphs*, Proceedings of the
  American Mathematical Society 13 (1962), 47–52,
  [DOI 10.1090/S0002-9939-1962-0133816-6](https://doi.org/10.1090/S0002-9939-1962-0133816-6),
  owns the product whose `K2` specialization is the canonical bipartite double
  cover.
- `PRM`: Sabidussi, *Graph Multiplication*, Mathematische Zeitschrift 72
  (1960), 446–457,
  [DOI 10.1007/BF01162967](https://doi.org/10.1007/BF01162967), is the primary
  Cartesian-product control.  Iterating the prism is only repeated product
  with `K2`.

The parity pushforwards (`BPQ`, `SPP`) were killed by the generic finite-linear
engine before an exact-map owner search.  `EVD`, `ECS`, `ELS`, `HBC`, and `BIM`
were killed by explicit P1–P161 proof-engine transfers.  `TTR` was killed by
its exact unstable small signature.  None of those decisions depends on an
absence-of-owner claim.

## Final gate

```text
BQC: BOUNDED_NON_HIT / SELECT_FOCUSED_AMBER / HOLD_EXTERNAL
SFC: KILL_INTERNAL_ENGINE
STP: KILL_DIRECT_OPERATION_OWNER_THIN
all others: KILL
```

Only `BQC` may enter a deeper owner/theorem-value review.  This log does not
authorize a manuscript or external release.
