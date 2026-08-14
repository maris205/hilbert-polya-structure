# Figure Specification — SD-C26

All manuscript figures are pure TikZ vector sources.  They use no raster
assets, target-zero data, fitted trends, or decorative chart elements.
Colors are paired with shape, line style, and explicit text so semantic
distinctions survive grayscale reproduction.

## Figure 1 — Kraft--Fredholm trilemma

**File:** `figures/kraft_fredholm_trilemma.tex`  
**Placement:** Introduction  
**Width:** approximately \(0.98\textwidth\)  
**Role:** hero figure

The figure begins with a finite-alphabet logarithmic certificate and splits
into three closures:

1. private recurrent cycles: clean one-atom primitive ledger, but
   (\ell(p)\gtrsim\log p) and total roof (\log p) leave a nonvanishing
   edge weight, so the whole adjacency is noncompact;
2. shared prefix trie/renewal hub: path reuse, but mixed return necklaces and
   determinant (1-F), so primitive purity fails;
3. one countable symbol/loop per atom: trace-class diagonal and clean Euler
   factors, but external arbitrary inventory and `PROVES TOO MUCH`.

**Caption:** A finite visible logarithmic code cannot close positively into
both a clean prime primitive ledger and a compact whole one-step operator.
Private cycles preserve factors but fail compactness; shared recurrence
creates mixed connected necklaces; the countable diagonal passes Fredholm
only by storing the chosen inventory.

## Figure 2 — candidate-gate matrix

**File:** `figures/family_gate_map.tex`  
**Placement:** candidate-family audit  
**Width:** approximately \(0.98\textwidth\)

The figure compares shared trie/renewal, private finite-code cycles,
factorization/S-adic prefixes, and the countable atom diagonal.  Columns
record literal-ledger, finite-code, whole-Fredholm, and arithmetic-selectivity
gates:

- shared recurrence fails at the literal-ledger gate;
- private finite-code cycles pass the literal ledger but fail whole
  Fredholm compactness;
- factorization/S-adic prefixes retain only scoped or cutoff-dependent
  information;
- the countable diagonal passes the determinant gate only by dropping the
  finite-code and selectivity requirements.

**Caption:** Exact gate map.  A question mark marks a property outside the
frozen theorem rather than a positive result.

## Exclusions

- No finite-prefix compactness is promoted to compactness of an infinite
  stationary union.
- No first-return edge is drawn as the original graph edge.
- No prime table is shown as a source object.
- No color alone encodes pass, stop, or control status.
- No Riemann zeros or critical-line graphics appear.
