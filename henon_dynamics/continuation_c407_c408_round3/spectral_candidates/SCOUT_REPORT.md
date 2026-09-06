# Spectral alternatives: source ownership and a decisive rejection

2026-09-06. No C-number, paper contract, manuscript, formal route evaluation,
or target-arithmetic claim is assigned to these candidates.

## 1. Two-prime ultrametric tensor Hamiltonian

**Frozen test object.** Let p and r be distinct rational primes. On the
mean-zero unit-ball spaces use the positive order-one Taibleson operators
A_p and A_r, and set H=A_p tensor A_r by the spectral theorem. The native
continuous-time evolution is exp(−itH), with eigenvalue energy T; no nonlinear
change of clock or removal of multiplicities is allowed.

**Classical ownership.** The individual spectra and their spectral zeta
functions are already given in Chacón-Cortés and Zúñiga-Galindo,
*Heat Traces and Spectral Zeta Functions for p-adic Laplacians*,
[arXiv:1511.02146](https://arxiv.org/pdf/1511.02146), Proposition 5.3 and
Example 5.1, pp. 7–8. The primary PDF was opened; those passages were read.
For dimension and order one they give eigenvalues p^j with multiplicities
(p−1)p^(j−1), j≥1. Tensor diagonalization and the geometric-series product
below are elementary consequences, not a proposed new spectral theorem.

Put c=(1−1/p)(1−1/r). Distinct prime factorization gives

    E_(j,k)=p^j r^k,     mult(E_(j,k))=c E_(j,k),   j,k≥1,
    Tr H^(−s) = (p−1)(r−1)/[(p^s−p)(r^s−r)],      Re s>1.

The exponent-one pole is double. The leading counting law does have a
T log T shape:

    N_H(T) ~ c T log(T)/(log(p) log(r)).

For completeness, sum first over k. If
M=floor((log T−log r)/log p), the result is

    N_H(T)=(1−1/p)T sum_(j=1)^M
                r^(−{(log T−j log p)/log r}) + O(T).

The rotation log p/log r is irrational. Uniform equidistribution for an
irrational rotation, applied to this bounded Riemann-integrable function,
gives the mean (1−1/r)/log r, which proves the displayed equivalence.
This uses only ordinary irrational-rotation equidistribution; no error rate
or constant second Weyl coefficient is asserted.

**Decisive failure.** At each E=E_(j,k), the counting function jumps by cE.
Consequently there are no constants A,B with

    N_H(T)=A T log T+B T+o(T).

Indeed, take any increasing sequence of these eigenvalues E and select
E'<E above the preceding eigenvalue with E−E'<E^(−2). The two hypothetical
asymptotic formulas differ by o(E), whereas the exact counts differ by cE.
This is a contradiction. Fixed positive energy rescalings and fixed shifts
do not remove this obstruction. It concerns the multiplicity-counted source
spectrum; it does not require an assumption that target zeros are simple.

**Decision: REJECT AS A NEW PAPER.** Matching the leading shape cannot meet
even the two-term target counting test. More importantly for admission,
the source spectrum is classical and this tensor/jump consequence is too
short and derivative to fill an independent paper contract. Do not append
an artificial perturbation solely to suppress the obstruction or treat a
two-prime source zeta as a target Euler product.

## 2. Gauss/Farey transfer alternatives

The initial browser landscape located classical transfer-operator spectrum
and leading-eigenvalue work, but no focused new theorem contract was obtained.
The repository already includes fixed-discriminant Gauss reduction (C364)
and Farey/BCZ cycle geometry (C395); these are different objects from the
infinite-dimensional transfer family, not a claim of complete overlap.

Search-result leads included [arXiv:1410.8069](https://arxiv.org/abs/1410.8069)
and [arXiv:nlin/0108044](https://arxiv.org/abs/nlin/0108044). Their full papers
were not read in this scout, so no detailed ownership or novelty claim is
based on them. No proof or implementation was started for this alternative.

**Decision: NOT ADMITTED.** A broad spectral family and a list of sources
are not an independent mathematical increment. No statement that the whole
Gauss/Farey class is exhausted or impossible follows from this scouting.

## Scope

The root coordinator now prioritizes an independent h-adic check of the
wild period-12 counterexample and proof-level scrutiny of the proposed
finite-field Frobenius-lifting theorem. Neither that check nor either
rejection above changes the three sealed papers or fills C407/C408.
