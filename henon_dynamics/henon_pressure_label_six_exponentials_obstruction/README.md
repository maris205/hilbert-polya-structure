# HCS-P48: Six-Exponentials obstruction to all-prime pressure labels

HCS-P45 isolated the pressure-normalized orbit label

\[
P_\gamma=|\Lambda_\gamma|^{h_*},
\qquad 0.277980<h_*<0.277987,
\]

as the only surviving repetition-compatible scalar label. HCS-P48 closes its
termwise all-prime interpretation without assuming that the pressure root is
algebraic or transcendental.

Three explicit primitive orbits of the certified H6 survivor have positive
unstable moduli

\[
L_1=1+\sqrt7+\sqrt{7+2\sqrt7},
\]
\[
L_3=19+21\sqrt5+\sqrt{2565+798\sqrt5},
\qquad
L_4=289+24\sqrt{145}.
\]

Their multiplier fields have compositum degree \(4\cdot4\cdot2=32\).
Independent inversion automorphisms then prove that

\[
\log L_1,\quad\log L_3,\quad\log L_4
\]

are linearly independent over \(\mathbb Q\).  For rational \(h>0\), the
algebraic-unit theorem prevents any \(L_j^h\) from being a rational prime.
For irrational \(h\), the Six Exponentials Theorem shows that at least one of
the three powers is transcendental.  Therefore

\[
\boxed{L_1^h,L_3^h,L_4^h\text{ cannot all be rational primes for any }h>0.}
\]

In particular, the pressure labels of all primitive H6 orbits cannot be
rational primes. The HCS-P45 prime-orbit counting theorem survives; what fails is
the stronger one-rational-prime-per-orbit arithmetic interpretation.

## Reproduce

```bash
bash code/run_c48.sh
cd paper && pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The Route-A verdict for the termwise pressure-label lane is
`ROUTE_A_REJECTED`.  Route B is not authorized.  The next legitimate large
road is collective: prime ideals, Galois packets, cyclic resultants, or a
distributional/scattering trace rather than one rational number per orbit.
