# COPRIME-0001 scalar continuation and endpoint barrier

This is the second paper stage for the frozen countable coprime suspension
candidate. It audits the scalar Fredholm determinant after the initial
trace-class/cycle-ledger stage.

The stage proves two complementary facts:

1. A squarefree-divisor Sylvester lift gives the explicitly named scalar
   representation `det_2(I-C_s)` on `Re(s)>1/2`, `s != 1`, agreeing with the
   original `det_F(I-L_s)` on `Re(s)>1`.
2. Finite prime-coordinate min--max compressions force infinitely many
   positive real zeros of the original determinant to approach `s=1`; hence
   no holomorphic or meromorphic germ crosses that endpoint.

The auxiliary `det_2` expression is not called the original bounded
counting-measure `ell^2` operator below `Re(s)=1`. No prime/zero tables,
determinant values, root locations, or target fitting are used. Route B remains
closed.

## Reproduction

Run from this project directory:

```bash
PYTHONPATH=. python3 experiments/coprime_0001_scalar_boundary.py \
  --quiet --output artifacts/coprime_0001/scalar_boundary_certificate.json
PYTHONPATH=. python3 -m unittest -v tests/test_coprime_0001_scalar_boundary.py
sha256sum -c results/ARTIFACT_HASHES.sha256
```

The manuscript is [paper/main.pdf](paper/main.pdf).

## Route-A checkpoint

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_CONTROLLED_CONTINUATION, A4_FAIL)
```

Scoped verdict: `STOP_SCOPED`. The completed-ξ target tuple remains failed.
