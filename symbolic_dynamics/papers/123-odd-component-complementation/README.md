# P123: Odd-Component Complementation

Anonymous internal round-2 support freeze of a short paper on the finite graph map that complements each odd connected component synchronously and leaves each even component unchanged. Both hostile reviews returned `GO_INTERNAL`; external release remains HOLD.

## Frozen contribution ceiling

The paper claims only the residual package proved in `main.tex`:

1. the pointwise parity-pruned component/co-component split-tree clock and the complete recurrent/fixed classification;
2. the sharp maximum transient depth `floor((n-1)/2)` with witnesses for every order;
3. the all-depth labelled EGF recurrence, exact depth layers, recurrent/fixed census, two-cycle count, and finite-order dynamical zeta function.

Gallai decomposition, cographs/cotrees, labelled SET calculus, connected-graph enumeration, and the elementary co-connected count are background and receive zero contribution credit. The direct-owner search was bounded. Novelty, priority, and external release remain **HOLD**.

## Reproduction

```bash
python3 code/verify_odd_component_complementation.py
cmp -s code/verify_odd_component_complementation.out <(python3 code/verify_odd_component_complementation.py)
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The repaired canonical verifier performs 203,244 exact assertions over all labelled graphs through order six, including literal split-clock and fixed/recurrent iff checks. See `BUILD.md` and `CONTROL_RESULTS.md` for frozen hashes and build checks.
