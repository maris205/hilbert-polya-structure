# P195 hostile Review A

**Reviewer relation:** process-separated internal reviewer; did not author
P195 and did not import its implementation.  
**Frozen input:** Round-0 sources and PDF pinned in `PINNED_INPUTS.sha256`.  
**Decision:** `PASS`.  
**Historical findings:** `0 Critical / 1 Major / 1 Minor`, all closed.  
**Open findings:** `0 Critical / 0 Major / 0 Minor`.  
**Mathematical decision:** `PASS`.  
**External state:** `OWNER_AMBER / HOLD_EXTERNAL`.

## Outcome first

The parity classification, sharp clock, two EGF families, zeta conversion,
local inverse atlas, and sharp fibre maxima all survived independent proof and
complete reconstruction through order eight.  The reviewer verifier checked
2,223,278 root transitions and 6,551,603 predicates without importing the
author code.  It also found the first connected odd-cut component with two
attracting edges at order six, confirming that the manuscript's warning is
necessary and correctly formulated.

The source/status revision has been accepted.  No theorem or formula changed.

## Closed finding P195-A1 — Major — P123/P159 history boundary omitted

P123, odd-component complementation, is the closest internal theorem
silhouette: it already combines a parity-triggered graph map, fixed and
period-two recurrence, sharp maximum transient
`floor((n-1)/2)`, labelled generating functions, and a dynamical zeta
function.  P159 additionally owns parallel odd-vertex pruning and a
rank-transfer inverse atlas.  Neither literal map equals P195: P123 changes
all edges inside odd connected components and uses a parity-pruned split-tree
clock; P159 deletes every current odd-degree vertex; P195 keeps one labelled
tree fixed and moves only a distinguished root according to odd edge sides
and least labels.  Still, the shared parity/tail/zeta and parity/pruning
surfaces must receive explicit zero credit.

The required repair was:

1. add P123 and P159 to the internal firewall in `main.tex` and
   `SOURCE_VERIFICATION.md`;
2. state the literal distinctions above; and
3. state that the shared `floor((n-1)/2)` scale, fixed/two-cycle dichotomy,
   labelled EGF/species machinery, zeta conversion, and generic local fibres
   supply no separation credit.

**Acceptance:** `CLOSED`.  The repaired manuscript and source ledger name P123
and P159, state both literal distinctions, and zero-credit the shared tail,
parity-recurrence, EGF/species, zeta, and fibre surfaces.  The retained
residual is limited to P195's literal marker map, parity geometry, integrated
least-label count, and incident-edge inverse atlas.

## Closed finding P195-A2 — Minor — incomplete release-state string

The batch gate is `OWNER_AMBER / HOLD_EXTERNAL`, but the abstract and closing
limitations print only `HOLD_EXTERNAL`.

**Acceptance:** `CLOSED`.  The abstract and final limitations now print the
exact dual state `OWNER_AMBER/HOLD_EXTERNAL`; the bounded non-hit language was
not strengthened.

## Hostile mathematical attacks

- **Parity orientation:** for every oriented edge through order eight, checked
  opposite parities at odd order and odd `H`-degree at even order.
- **Functional cycles:** reconstructed all orbits.  Period support is `{1}`
  for odd order and `{2}` for even order, including `n=1,2`.
- **Tail count:** independently used nested odd sides and off-path witnesses;
  exhaustive depth histograms attain exactly `floor((n-1)/2)`.
- **False component uniqueness:** searched every `H`-component.  The first
  multiple-attractor example occurs at `n=6`, with tree edges
  `1-3,2-4,3-4,3-5,4-6` and attracting edges `(1,3)` and `(2,4)`.
- **Even EGF orientation factor:** counted recurrent *root states*, not
  `H`-components or unoriented edges.  A separate weighted census of rooted
  sides verifies `1/(k+1)` before the ordered product is formed.
- **Independence point:** after cutting the recurrent edge, the comparison set
  `{v plus odd A-branch roots}` is disjoint from
  `{u plus odd B-branch roots}`; induced relative orders are independent.
- **Fibre edge cases:** accumulated direct incoming roots and compared them
  target by target with the self term plus neighbour test.  The odd
  two-edge bouquet and even star realize the stated maxima.

## Verifier and build record

```text
author replay: PASS, byte-equal, n=1..8
reviewer replay: PASS, byte-equal, n=1..8
reviewer transitions: 2,223,278
reviewer checks: 6,551,607
reviewer digest: 80a123832d9e869492b8e833db108521319a4715718498294a140c819033d0d9
cold repaired PDF: 3 pages, 318,096 bytes
cold repaired PDF SHA-256: d5dbac8ed78f1f3eccc3c7aeccda852e6f44f77a513091032120254119ff9c0a
```

All three pages were rasterized and inspected.  Fonts are embedded,
subsetted, and Unicode mapped; no warning, bad box, unresolved
citation/reference, clipping, overlap, malformed display, or blank page was
found.

P195 now passes Review A with zero open findings and preserves
`OWNER_AMBER / HOLD_EXTERNAL`.
