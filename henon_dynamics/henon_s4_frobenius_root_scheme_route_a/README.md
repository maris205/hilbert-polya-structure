# HCS-C369: quartic S4 Frobenius root-scheme dynamics

This package proves a complete source-arithmetic theorem for

\[
f(x)=x^4-x-1,\qquad \operatorname{disc}(f)=-283.
\]

For every good prime `p != 283`, arithmetic Frobenius `alpha -> alpha^p`
permutes the four geometric roots.  Factor degrees give the cycle lengths,
all five conjugacy classes of `S4` occur, primitive cycles are recovered by
Möbius inversion, and the finite-fiber dynamical zeta is exactly a
four-dimensional permutation determinant.  The Galois group is proved to
be `S4`; Chebotarev then gives the five densities.  At `p=283` the repeated
root makes the fiber non-étale and ends the four-point atlas.

The universal zero-dimensional fact that Frobenius is a finite permutation
and that its local zeta is a reciprocal permutation determinant already
belongs to workspace package C12A.  C369 does not reclaim it.  C369 owns the
`x^4-x-1`-specific `S4` proof, five-class all-good-prime
factor/fixed/primitive/density atlas, `p=283` boundary, and
convention-locked executable ledger.

The evidence exhausts all 1,228 good primes at most 10,000 and all iterates
through 12.  Its finite counts are regression receipts, not the proof of the
all-prime theorem.

## Route decision

`(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`

Overall: `ROUTE_A_ARITHMETIC_CANDIDATE`.  A1 is only the exact finite-fiber
determinant and records applicability, not new ownership of its universal
mechanism.  There is no global autonomous owner across primes, cross-prime
Fredholm direct sum, target Euler product, target zero match, or
Hilbert--Pólya operator.  Route B remains locked by
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python -B code/c369_release_manifest.py --write --build-pdfs
python -B code/c369_release_manifest.py
python -m unittest tests/test_c369_smoke.py
```

The canonical paper is [paper/main.pdf](paper/main.pdf).  See
[THEOREM_PACKAGE.md](THEOREM_PACKAGE.md) for the exact theorem and
[REPRODUCIBILITY.md](REPRODUCIBILITY.md) for the independent lanes.
