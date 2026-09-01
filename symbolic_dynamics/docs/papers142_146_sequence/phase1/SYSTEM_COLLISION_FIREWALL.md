# System collision firewall — P142–P146

**Checkpoint:** pre-drafting literal and proof-engine comparison.
**External status:** `HOLD_EXTERNAL`.

## P142 — valuation–gcd divisor tent

- **Literal carrier/update:** divisors (p^a\mid p^e), (d\mapsto\gcd(p^e,d^2+p^e/d)), with (p) odd.
- **Nearest occupied rows:** P133 totient/Pratt divisor dynamics, P131 Euclidean queues, P137 rank-feedback (p)-group splitting.
- **Separation:** P142 is a single prime-power valuation chain with two scalar inverse branches; it has neither a prime-support DAG, quotient queue, nor group-isotype split.  Its sharp clock is logarithmic and uniquely attained at (p^{e-1}).
- **External compression:** the normalized map (x\mapsto\min(2x,1-x)) is a piecewise-linear tent variant.  General interval-map and finite-grid tools are zero credit.  The arithmetic lift remains potentially cosmetic.

## P143 — row-inclusion residual dynamics

- **Literal carrier/update:** all (n\times n) Boolean relations; replace the relation by the preorder comparing row supports by inclusion.
- **Nearest occupied rows:** P127 parity-transpose looped digraphs, P106 MIS polarity, relation-cubing reserve from P137–P141.
- **Separation:** no parity, degree, graph polarity, or relation product drives the update.  The image is the full class of labelled preorders, the recurrent involution is order reversal, and fibres are induced embeddings of quotient posets into (B_n).
- **External compression:** self-residuation (R\backslash R) producing a preorder is standard relation algebra and is explicitly subtracted.  Only the iterated (T^3=T) package and full inverse atlas remain.

## P144 — first-component Dyck reassociation

- **Literal carrier/update:** a Dyck path (C_1C_2\cdots C_k) with (C_1=UA D) and (k\ge2) maps to (UA C_2D C_3\cdots C_k).
- **Nearest occupied rows:** P126 balanced compositions, P134 border feedback, P139 Lyndon starts, Catalan/word controls in earlier kill ledgers.
- **Separation:** the update is a leftmost ground-level reassociation; its state statistic is the number of primitive Dyck components, not a composition-balancing, border, or factor-start mask.  Target fibres retain the depth grading rather than only one-step segmentation.
- **External compression:** first-return decomposition, Catalan/ballot enumeration, and the atomic Tamari rotation are classical.  The deterministic leftmost iteration and conjunction of exact layer/fibre results are retained only as owner-thin residual.

## P145 — random vertex-push orientation chain

- **Literal carrier/update:** one push-equivalence orbit of orientations of a fixed simple graph; uniformly choose a vertex and reverse every incident arc.
- **Nearest occupied rows:** P127 parity-transpose digraphs, P123 component complement, P141 weighted greedy MIS, generic finite-group walks.
- **Separation:** states form an orientation torsor under cut translations.  The retained output is a disconnected weighted factorisation and input-only inverse theorem for connected-component orders, not a deterministic parity loop, complement map, or greedy endpoint law.
- **External compression:** vertex pushing and push equivalence are directly owned; every connected factor is a standard folded hypercube, whose spectrum, bipartiteness, and random-walk setting are also directly owned; Fourier diagonalisation is generic zero-credit machinery.  The repaired residual is only the labelled multi-component weighted product and the known-`n` spectral inverse with explicit failure modes.

## P146 — random convex-polygon ear deletion

- **Literal carrier/update:** shrink a labelled convex polygon by uniformly deleting any current vertex and record the new diagonal; endpoint is a triangulation.
- **Nearest occupied rows:** P114 forest leaf peeling, P130 chord retraction, P140 shrinking majority windows.
- **Separation:** the stochastic state is a polygon, not a fixed forest or word.  The endpoint is a triangulation and the main object is its root-face-resolved probability through the weak dual.  No majority, matching, or deterministic leaf layer occurs.
- **External compression:** ear clipping, triangulation/dual-tree correspondence, and the generic rooted-tree hook formula are zero credit.  The full endpoint law and sharp path-dual least-mass theorem form the residual.

## Cross-batch diversity gate

The five selected carriers are respectively arithmetic divisors, Boolean relations, Catalan paths, graph orientations, and shrinking polygons.  Their principal proof engines are valuation branches, relational residual/poset embeddings, first-return reassociation, Fourier/root separation, and dual-tree leaf orders.  No two selected systems are literal restrictions, relabellings, state-quotients, complement conjugates, or scheduler variants of one another.

The two closest reserve mechanisms—dihedral normalizer towers and Boolean Gram graph squaring—remain excluded from the five.  This prevents a second group tower or second Boolean-matrix paper from reducing diversity.

**Gate result:** `5/5 GO_INTERNAL`, with P143, P144, and P146 marked
`OWNER_THIN`, and P145 marked `OWNER_REPAIRED`; all external actions remain
`HOLD`.
