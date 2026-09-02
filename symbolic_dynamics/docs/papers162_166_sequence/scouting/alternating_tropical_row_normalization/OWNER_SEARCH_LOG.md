# ATR owner and internal-collision audit

**Scope:** bounded primary-source and P1--P161 audit  
**External status:** `HOLD_EXTERNAL`  
**Novelty/priority claim:** none

## Direct primitive owner

H. W. Kuhn, *The Hungarian Method for the Assignment Problem*, **Naval
Research Logistics Quarterly 2** (1955), 83--97,
DOI `10.1002/nav.3800020109`, introduced the Hungarian assignment method.
James Munkres, *Algorithms for the Assignment and Transportation Problems*,
**J. Soc. Indust. Appl. Math. 5** (1957), 32--38,
DOI `10.1137/0105003`, gives a direct algorithmic formulation.  Row- and
column-minimum subtraction are standard cost reductions in this line.

**Subtraction consequence.**  ATR receives zero contribution credit for
subtracting a row minimum, subtracting a column minimum, preserving assignment
cost up to potentials, or creating zeros in every row and column.  It does
not claim a faster assignment algorithm, an optimality criterion, or the
later covering/augmentation stages of the Hungarian method.

## Bounded exact-map search

Searches combined exact and equivalent phrases including `subtract row
minimum transpose iterate`, `row normalization transpose dynamics`,
`alternating row column minimum reduction finite matrix`, `tropical matrix
normalization transpose functional graph`, `preimages of row column reduced
cost matrices`, and `enumeration matrices zero every row and column`.
Publisher/DOI records and primary texts were preferred.  The strongest hit
was the Kuhn--Munkres primitive above.  No inspected source stated the literal
endomorphism `A -> R(A)^T`, its functional graph, the target zero-cover
preimage polynomial, or the exact depth census.  This is only a bounded
non-hit and is not evidence of global novelty.

## Internal P1--P161 collision firewall

| nearest occupied paper | shared surface | decisive separation |
|---|---|---|
| P116, max-plus switching-induced growth | tropical/max-plus matrices and additive normalization vocabulary | P116 iterates random products of two fixed `2 x 2` max-plus matrices and studies projective growth/reset words.  ATR acts deterministically on the full finite cost-matrix carrier; no matrix product or Lyapunov axis transfers. |
| P127, parity-transpose looped digraphs | full binary matrices and transpose | P127 transposes according to a parity gate and has a different image/fibre engine.  ATR's numerical row minima, two-step row/column core, and bounded-potential inverse formula do not occur there. |
| P143, Boolean row-inclusion residual | Boolean matrices, transpose, and a short eventual-period identity | P143 maps a relation to its row-inclusion preorder and uses quotient-poset fibres.  Neither the literal map nor its fibre proof transfers to (1). |
| P103/P125 matrix families | finite full-matrix carriers and quadratic/transpose invariants | their maps are algebraic over finite fields.  ATR is order/tropical and its zero-cover potential sum has no field-linear reduction. |

Generic transpose involutions and elementary inclusion--exclusion are also
zero-credit background.  The proposed paper must keep (14)--(15) as its
second theorem axis; without the target-wise inverse result the temporal
statement alone would be too close to a standard row/column reduction.

## Owner-side decision

`PASS_OWNER_THIN_PENDING_HOSTILE_GATE`.  The residual conjunction is narrow
but presently nonempty: literal alternating normalization, exact two-step
functional graph, and zero-pattern-sensitive inverse fibres.  Any claim of a
new normalization primitive, Hungarian-method result, general tropical
matrix theory, or absolute novelty crosses the firewall.

