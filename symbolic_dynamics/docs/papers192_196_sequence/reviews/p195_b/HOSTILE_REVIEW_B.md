# P195 process-separated hostile Review B

## Verdict

`PASS / ZERO OPEN FINDINGS / ACCEPTED_NO_CHANGE / HOLD_EXTERNAL`

The frozen Round-1 theorem package survives an independent reroot-array and
exact rational-series audit.  Review B imports neither author nor Review-A
code and made no change under `papers/195-odd-side-least-neighbor-trees/`.

## Representation and attack route

Each tree is rooted once at label `1`.  One bottom-up subtree-size pass assigns
both oriented sizes to every edge; all root updates are then read from this
fixed oriented-edge array.  This avoids edge-deletion traversal.  Recurrent
EGFs are expanded independently as exact `Fraction` series from Cayley's
coefficients and compared with the literal reroot census.

The control reconstructs all 2,223,278 rooted states through order eight and
checks 9,390,311 predicates.  It attacks:

- opposite/same edge-side parity for odd/even order;
- odd degree in the even-order odd-cut forest and the complete period support;
- the nested-side and off-path-witness tail bounds;
- explicit sharp witnesses for both parity classes;
- both recurrent EGF families and the oriented two-cycle factor;
- the every-target local predecessor criterion;
- the odd/even maximum fibres and their bouquet/star witnesses;
- the six-vertex connected `H` component with two distinct mutual edges.

## Findings

- Critical: `0`
- Major: `0`
- Minor: `0`

The manuscript correctly avoids the false assertion that an `H` component has
only one attracting edge.  Review A's P123/P159 subtraction and exact release
state are present.  No residual mathematical, source, build, or presentation
defect was found.

## Exact receipt

```text
reviewer transitions: 2,223,278
reviewer assertions: 9,390,311
reviewer digest: 4126ec772a597e46c2b387681c46df7bf96b83c1774b9f3436d515c03361b354
reviewer canonical SHA-256: a60ac08ca5b3950ae5ec8649dfa486cbbff648afb03dae0f97d92449effd37f9
Round-1 PDF SHA-256: d5dbac8ed78f1f3eccc3c7aeccda852e6f44f77a513091032120254119ff9c0a
replay 1 / replay 2: byte-identical
```

The decision authorizes only a byte-identical internal Round-2 receipt.
`OWNER_AMBER / HOLD_EXTERNAL` remains binding; no novelty, priority, or
ownership conclusion is drawn.
