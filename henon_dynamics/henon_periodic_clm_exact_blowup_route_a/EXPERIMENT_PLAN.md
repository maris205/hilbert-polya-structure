# Exact-computation plan

The canonical computation uses no floating-point theorem decision. It will:

1. check 256 signed Fourier multipliers and `H²=-I` on nonzero modes;
2. verify the periodic Tricomi identity coefficient by coefficient for 1,024 two-frequency Gaussian-rational polynomials;
3. audit 512 exact zero-mean and 2,048 exact nonzero-mean Möbius cells;
4. classify 2,304 signed one-mode regimes, including the tangent boundary and branch metadata;
5. execute four exact A0 controls: prime/composite mode invariance, a deterministic affine mode relabeling, neighboring mean--amplitude thresholds, and the simpler zero-mean parent;
6. evaluate 1,024 nonzero-mean and 256 zero-mean transverse profile cells;
7. freeze seven boundary cases, source owners, collision owners, nonclaims, and the all-fail Route-A tuple;
8. run an independent checker, SymPy derivation, isolated replay, repaired-hash mutations, smoke tests, deterministic three-round PDF builds, font/text/raster checks, and manifest closure.

Acceptance is exact and fail-closed.
