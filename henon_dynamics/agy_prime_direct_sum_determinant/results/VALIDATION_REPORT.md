# HCS-C28 validation report

## Status

`PASS` for the declared source-locked theorem and exact arithmetic controls.

The independent checker imports no producer code.  It replays the C26 word
with list arithmetic, uses a Bareiss determinant and explicit minors for the
C24 fixed-plane proof, trial factorization for the discriminant sentinel,
and a separate Jacobi/Kronecker implementation for the quadratic controls.

Release totals are **32/32 independent decisive fields**, **21/21
regression and rehashed-mutation tests**, and a passing canonical payload
digest.  A separate audit compared the Bareiss backend with SymPy on 12,000
random integer matrices without a discrepancy.

## Independent gates

The release checker verifies:

1. all four upstream SHA-256 source locks;
2. the C26 later-on-the-left chronological matrix replay;
3. the exact gamma-star determinant, factorization, squarefree kernel, and
   character residue classes;
4. the P073 symplectic identity, determinant, rank, minor gcd, quotient
   matrix, and all-odd-prime character conclusion;
5. the complete 146-cycle fixed-space census;
6. the sharp Schatten phase boundary and ordinary trace-class threshold;
7. the normalized-character and normalized-moment conclusions;
8. the direct-sum Fredholm domain, locally normal product, joint holomorphy,
   and repetition firewall as certificate contract fields;
9. every terminology/scope flag and the denial of Route B;
10. the canonical payload hash of the complete producer certificate.

## Theorem versus exact computation

- **Theorem:** normalized finite-Weil characters converge pointwise to the
  regular character of the integral cocycle group.
- **Theorem:** \(\|\mathcal L_{s,p}\|_{S_q}\asymp p^{2/q}\) and the weighted
  direct-sum \(S_q\) criterion is necessary and sufficient.
- **Theorem:** the prime-graded ordinary Fredholm determinant exists exactly
  for \(\operatorname{Re}z>3\) and retains chronological word traces.
- **Theorem:** the normalized-trace positive-AGY determinant germ is one.
- **Exact computation feeding a theorem:** P073's minors and Thomas quotient
  imply \(\Theta_p=p\) for every odd prime, so the marked normalized sum
  diverges.
- **Exact finite census:** P073 is the only fixed-dimension-two item among
  the 146 frozen C24 eventually-positive controls.

The P073 conclusion is explicitly limited to the full C24 Rauzy ledger.  No
finite scan is promoted to an all-word theorem about the C26 induced
language.

## Precision and order

Every decision uses integer, rational, symbolic, or exact finite-field
arithmetic.  Prime enumeration order is irrelevant in the proved
trace-class domain.  The code does not evaluate a truncated global product
and does not use floating tolerances.
