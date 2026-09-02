# Paper improvement log

## Round 0: algebraic core

The first complete draft froze the matrix orientation, proved diagonal similarity, solved the continuant by Chebyshev polynomials, and stated the simple real OBC spectrum.  It deliberately did not yet claim a complete boundary atlas.

## Round 1: spectral dynamics and normalization repair

The second draft added the canonical left/right sine basis, the exact gauge-specific eigenbasis condition number, propagator and resolvent similarity, resolvent entries, and norm bounds.  It made the decisive distinction between right-amplitude skin bias and the pointwise biorthogonal density.  The “canonical sine gauge” qualifier was added because arbitrary eigenvector column rescaling changes a basis condition number.

## Round 2: full boundary closure and hostile audit

The third draft added the PBC Fourier ellipse, Hermitian diagonal, both one-sided Jordan axes, zero corner, orientation reversal, the singular OBC/PBC limit, and the `N=2` coincident-neighbor convention.  Registry red-team review removed false collisions with C185/C242/C293 and retained only verified neighbors C267/C288/C297/C303.  Scope language now excludes topology, disorder, interactions, and Hilbert--Polya claims.  Evidence lanes were hardened against repaired semantic hashes, stale hashes, duplicate/nonfinite JSON, YAML duplicate/merge/anchor/alias attacks, exact-type confusion, list truncation, collision-value tampering, and `python -O`.
