# HCS-P62: full-horseshoe algebraic exhaustion

This project closes the ambient algebraic-effectivity gate left by HCS-P60
and HCS-P61 for

\[
H_6(q,p)=(1-6q^2-p,q).
\]

The scaling `S(q,p)=(6q,6p)` conjugates this map to the area-preserving
Hénon map `(x,y) -> (6-x^2-y,x)`.  Arai's certified hyperbolic plateau
contains the connected parameter interval `[6,10]`, while the
Devaney--Nitecki large-parameter theorem supplies a full two-shift at the
anchor `a=10`.  Structural stability transports that full shift to `a=6`.
Friedland--Milnor's algebraic fixed-point count then gives the exact
exhaustion

\[
\#\operatorname{Fix}_{\mathbb C}(H_6^n)=2^n
=\#\operatorname{Fix}_{\mathbb R}(H_6^n)
\]

for every `n>=1`, with every point distinct, hyperbolic, and simple.

Consequently, for every odd `n=2m+1`, the P60 mixed-axis closure

\[
F_n(X)=q_{m+1}(X)-q_m(X)
\]

is totally real and squarefree.  Its recursively defined Möbius primitive
quotient is a reduced effective divisor of exact least-period roots.  The
actual primitive reflection count is therefore

\[
D_n=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2},
\]

with entropy `(1/2)log(2)`.

## Strongest status

- **SOURCE_BACKED_PROVED:** the real chain recurrent set at `H6` is a
  uniformly hyperbolic full two-shift.
- **PROVED:** every complex periodic point of `H6` is real, distinct,
  hyperbolic, and simple.
- **PROVED:** every odd mixed-axis closure is totally real and squarefree;
  every primitive quotient is finite étale and totally real.
- **COMPUTER_CERTIFIED_EXACT:** exact Sturm isolation of all primitive roots
  through odd period 13; independent symbolic and high-precision checks.
- **OPEN:** uniform height/Galois-excess pressure and any source-native
  rational-prime or von Mangoldt trace law.
- **Route A:** exploratory, with an analytic all-period A1 layer and an
  inherited symbolic determinant; no arithmetic promotion.
- **Route B:** not authorized.

## Reproduce

```bash
bash code/run_c62.sh
cd paper && pdflatex paper && bibtex paper && pdflatex paper && pdflatex paper
```

## Main artifacts

- [`paper/paper.pdf`](paper/paper.pdf)
- [`PROOF_PACKAGE.md`](PROOF_PACKAGE.md)
- [`results/c62_certificate.json`](results/c62_certificate.json)
- [`results/c62_independent_check.json`](results/c62_independent_check.json)
- [`route_a_evaluation.yaml`](route_a_evaluation.yaml)

Author: **Liang Wang**, School of Artificial Intelligence and Automation,
Huazhong University of Science and Technology.
