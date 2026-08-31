# C261 results

## Analytic result

The periodic Airy flow is an exact unitary cubic Fourier group with least
full-space period `2*pi`.  Every reduced rational time has a finite cubic-DFT
translation formula of exact order `q`; its fixed modes are precisely the
multiples of `product ell^ceil(v_ell(q)/3)`.  Finite-support state periods and
the irrational fixed-space boundary are complete.

## Executable receipt

- 2,806 reduced rational strobes through `q=96`;
- 101 cubic DFT coefficient/inverse/Parseval reconstructions through `q=18`;
- ten finite-support state-period rows;
- 50,765 independent-checker assertions;
- 301,200 exact SymPy/modular identities;
- clean-process byte replay;
- 41/41 repaired-hash semantic mutation rejections.

Evidence payload SHA-256 and final PDF hashes are recorded in the release
manifest.

```text
(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)
ROUTE_A_REJECTED; Route B false.
```

The finite receipt verifies formulas and conventions, not the continuum
theorem by enumeration.  No nonlinear KdV, target determinant, arithmetic
local data, or Hilbert--Pólya conclusion follows.
