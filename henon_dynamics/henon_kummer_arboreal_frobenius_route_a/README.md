# HCS-C374: Kummer arboreal Frobenius dynamics

For the quadratic map `f(z)=z^2` and basepoint `2`, level `n` of the
preimage tree is

```text
R_n={z:z^(2^n)=2},   K_n=Q(R_n).
```

This package proves, for every `n>=3`, the radical--cyclotomic
intersection, the exact compatible Galois image, its restriction maps, the
complete fixed-root law, and the Chebotarev density of primes for which
`x^(2^n)=2` has a root.  The image is the index-two entangled affine group

```text
H_n={(a,b): (-1)^b=(2/a)} <= AGL_1(Z/2^n),
```

and the root-prime density is

```text
delta_n = 7/24 + 1/(3*4^(n-1))  ->  7/24.
```

The theorem, not a finite table, establishes every all-level statement.
The executable evidence exhausts all 5,592,400 image elements at levels
3 through 12 and 95,910 odd-prime/level cells with `p<=100000` as
regression receipts.

## Route decision

`(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`

Overall: `ROUTE_A_EXPLORATORY`.  This is a source-arithmetic arboreal
representation and a compatible family of finite permutation unitaries.
The present fixed-root law is not a complete all-level primitive-cycle,
repetition, orientation, phase, or monodromy atlas, and it supplies no
intrinsic prime-to-orbit or `log p` law.  It is not a target Euler product,
target divisor, or Hilbert--Pólya operator.  Route B is locked by
`NO_BAD_EULER_OR_ROOT_NUMBER`.

The A0 decision is stress-tested by three distinct controls: neighboring
basepoint `3` has trivial radical--cyclotomic intersection and the full
affine image; the simpler full `AGL_1` parent restores the four-fixed-root
stratum removed by the basepoint-two character; and the 25 odd composite
labels below 100 split into five prime powers retained as `Frob_p^r`
repetition controls and twenty mixed composites lacking a single-prime
Frobenius owner.
Finite empirical density earns no A0 credit.

The real finite permutation unitaries give a canonical Koopman realization,
but no family-wide antiunitary time reversal, nontrivial phase/weight law, or
global self-adjoint Hamiltonian is supplied.  Thus A4 is only a formal hint.

## Reproduce

```bash
python -B code/c374_release_manifest.py --write --build-pdfs
python -B code/c374_release_manifest.py
python -B -m unittest tests/test_c374_smoke.py
```

The final manuscript is `paper/main.pdf`; the three substantive sources
and PDFs are `paper/main_round{0,1,2}.tex` and
`paper/main_round{0,1,2}.pdf`.
