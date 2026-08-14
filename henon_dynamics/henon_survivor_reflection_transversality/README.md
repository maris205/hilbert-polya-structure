# HCS-P61: survivor reflection transversality

This project resolves the physical part of the all-period effectivity gate
left by HCS-P60.  For the area-preserving map

\[
H_6(q,p)=(1-6q^2-p,q),
\]

an odd mixed-axis closure root in the certified H6 hyperbolic survivor is
always transverse and therefore simple.  The key exact implication is

```text
symmetry-line tangency
    => eigenvalue 1 for DH_6^n
    => contradiction with survivor hyperbolicity.
```

The symmetry-equivariant coding then gives exactly one such root for each
primitive reversible necklace.  Hence at odd period `n`

\[
P_n=\sum_{d\mid n}\mu(n/d)F_{(d+3)/2}
\]

distinct physical roots occur with coefficient `+1` in the formal P60
dynatomic divisor.  Their entropy is `(1/2)log(phi)`, whereas the formal
degree entropy is `(1/2)log(2)`.  Thus the certified physical incidence has
exponentially vanishing density `Theta((phi/2)^(n/2))` in the formal degree.

## Strongest status

- **PROVED:** all-period transversality for primitive odd roots in the
  certified real H6 survivor.
- **PROVED:** one-to-one physical reversible-necklace/root incidence and
  local coefficient `+1` in the formal divisor.
- **COMPUTER_CERTIFIED_EXACT:** rational interval separation of all primitive
  roots through odd period 11, with physical counts `1,1,2,4,6,12`.
- **OPEN:** all-period transversality/effectivity for ambient algebraic roots
  outside the survivor.
- **Route A:** exploratory; the physical reflection A1 interface improves,
  but no arithmetic A2/A4 promotion follows.
- **Route B:** not authorized.

## Reproduce

```bash
bash code/run_c61.sh
cd paper && pdflatex paper && bibtex paper && pdflatex paper && pdflatex paper
```

## Main artifacts

- [`paper/paper.pdf`](paper/paper.pdf)
- [`PROOF_PACKAGE.md`](PROOF_PACKAGE.md)
- [`results/c61_certificate.json`](results/c61_certificate.json)
- [`results/c61_independent_check.json`](results/c61_independent_check.json)
- [`route_a_evaluation.yaml`](route_a_evaluation.yaml)

Author: **Liang Wang**, School of Artificial Intelligence and Automation,
Huazhong University of Science and Technology.
