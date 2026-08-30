# HCS-C241 — Classical Lüroth countable-branch periodic atlas

This Route-A package studies the source-local classical Lüroth map

\[
T_L(x)=\lfloor 1/x\rfloor(\lfloor 1/x\rfloor+1)x-\lfloor 1/x\rfloor,
\qquad T_L(0)=0,
\]

with branches \(I_m=(1/m,1/(m-1)]\), \(m\ge2\).  Each branch maps
affinely onto \((0,1]\) (the value 0 is only the excluded left-endpoint
limit), has slope \(a_m=m(m-1)\), and inverse
\(\phi_m(y)=(y+m-1)/a_m\).  Every finite branch word therefore gives one
exact fixed point of an affine contraction and an exact multiplier product.
Primitive cyclic words are recorded as necklaces.  The alphabet is countably
infinite, so every positive period has countably infinitely many coded points;
the finite \(M\) rows are reproducibility slices, not a claim of finiteness of
the mathematical map.

The weighted source identity is
\[
 Z_M(z,s)=\frac1{1-z\sum_{m=2}^M[m(m-1)]^{-s}}.
\]
The full sum \(A(s)\) is absolutely convergent for \(\Re(s)>1/2\).  The
primitive product/log expansion is absolutely convergent only when both
\(\Re(s)>1/2\) and \(|z|A(\Re(s))<1\).  In the larger half-plane,
\(1/(1-zA(s))\) is a meromorphic continuation away from denominator zeros;
these domains are deliberately distinguished.  At \(s=1\), telescoping gives
\(A(1)=1\), so \(z=1\) is a denominator pole/boundary.

## Reproducibility receipt

The deterministic producer writes `results/c241_luroth_evidence.json` with
11 branch rows, 780 word rows (alphabet 2–6, lengths 1–4), 30 necklace rows,
88 finite weighted rows, 3 limit rows, and 2 exact finite-product rows.
`c241_luroth_checker.py` rebuilds the fractions independently; the SymPy
cross-check proves affine, telescoping, and formal-series identities; replay
compares producer bytes; mutation tests repair hashes before checking semantic
rejection.  The source and evaluator locks are baseline
`489506cf92bfed721f94f22dd0444a60427f90a5` and evaluator SHA
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

## Route-A boundary

The tuple is `A0_FAIL, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FORMAL_HINT`.
The exact word/point theorem is an analytic source-local advance (A1), but the
countable branch labels have no intrinsic rational-prime carrier and the
weighted identity is not a target Euler product or divisor.  No target primes,
zeros, arithmetic local data, Euler factors, root numbers, automorphy,
functional equation, Hilbert–Pólya operator, or Route-B invocation is claimed.

## Primary sources

* Barrionuevo, Burton, Dajani & Kraaikamp, *Ergodic properties of generalized
  Lüroth series*, Acta Arithmetica 74(4), 311–327 (1996), DOI
  [10.4064/aa-74-4-311-327](https://doi.org/10.4064/aa-74-4-311-327).
* Galambos, *Some remarks on the Lüroth expansion*, Czechoslovak Mathematical
  Journal 22(2), 266–271 (1972), DOI
  [10.21136/CMJ.1972.101097](https://dml.cz/dmlcz/101097).
