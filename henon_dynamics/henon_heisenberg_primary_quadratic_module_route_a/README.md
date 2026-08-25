# HCS-C156: Heisenberg primary quadratic module

This package refines the C151 fixed-fibre classification for the frozen
Heisenberg automorphism.  It proves the all-iterate Smith type of
`A^n-I`, lowers the universal rotation denominator from `2D_n^2` to the
horizontal-group exponent

```text
h_n = L_n       (n odd),
h_n = 5 F_n     (n even),
```

and decomposes the resulting finite quadratic module orthogonally into its
group-theoretic primary components.  Exact component enumeration through
`n=14` gives the fixed-circle count as a product of primary zero counts.

The word *primary* is purely finite-abelian-group terminology.  The package
does not assert arithmetic local factors, Euler factors, root numbers,
automorphy, a target trace formula, or a Route-B construction.

## Reproduce

```bash
python code/c156_primary_module_producer.py
python code/c156_primary_module_checker.py
python code/c156_sympy_crosscheck.py
python code/c156_replay.py
python code/c156_mutation.py
```

The final paper is `paper/main.pdf`; the content-addressed release ledger is
`C156_RELEASE_MANIFEST.json`.
