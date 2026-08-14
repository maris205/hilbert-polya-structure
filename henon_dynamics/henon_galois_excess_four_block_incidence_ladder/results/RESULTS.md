# Results

## Exact outputs

- Primitive cycle counts through period six: `1,0,1,2,2,2`.
- Infinite relation:
  `N_m(A_m)+N_m(B_(m+2))=N_m(A_(m+1))+N_m(B_(m+1))`.
- Period-six trace: `18062+5352*sqrt(7)`.
- Period-six trace polynomial coefficients: `[1,-36124,125728516]`.
- Period-six multiplier degree: `4`.
- Period-six excess: `8.269228818061161246...`.
- Width-four ladder discrepancy: `-55.547503802226014186...`.
- Exact logarithm-argument margin: `96873`.
- Four-row width-four incidence rank: `3`.
- Seven-row width-five selected determinant: `+1`.

## Validation

- dependency locks: 7/7;
- primary mutations: 20/20 rejected;
- unit tests: 15/15 passed;
- independent DFS/algebra reconstruction: passed;
- finite ladder guard: widths 3 through 64;
- final PDF: compiled with BibTeX and no unresolved references.

Hashes are frozen in `SHA256SUMS.txt` after final review.

## Claim boundary

The result excludes locally constant excess potentials of width at most
four.  It does not exclude width five globally, and it does not prove or
refute an unrestricted Hölder realization.  It adds no rational-prime or
Riemann-zero correspondence.
