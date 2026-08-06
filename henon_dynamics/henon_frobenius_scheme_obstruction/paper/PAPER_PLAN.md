# Paper plan

## One-sentence contribution

For the integral area-preserving Hénon family, we prove that every fixed-time
periodic scheme is finite flat of rank \(2^n\) away from coefficient
degree-drop primes, and that its fixed-\(n\) Frobenius zeta is necessarily a
nilpotent-blind finite-permutation determinant, which rules out the registered
local-zeta anomaly mechanism.

## Epistemic status

This is a scoped negative note.  The finite-flat presentation is an elementary
family-specific theorem; Frobenius rationality is a standard zero-dimensional
fact applied as an obstruction.  The period-five \(S_6\) calculation is a
reproduction and prior-work collision, not a novelty claim.

## Claims--evidence matrix

| Claim | Status | Evidence |
|---|---|---|
| \(X_n\) is finite flat rank \(2^n\) over \(\mathbb Z[A,A^{-1}]\) | PROVED | cyclic scheme isomorphism and monic Gröbner basis |
| `degree_good` and `etale_good` are distinct | PROVED | direct uninverted \(a=0\) reduction gives \(H_0^4=I\); cyclic Jacobian/Hill identity on the degree-good locus |
| fixed-\(n\) local zeta is a permutation determinant | PROVED/STANDARD | finite-support Frobenius action and Grothendieck trace formula |
| ordinary counts ignore nilpotents | PROVED/STANDARD | reduction invariance of field-valued points |
| \(N(r,n)\) loses relative Frobenius/Hénon rotation | PROVED | two reversor-paired five-cycle actions with equal ordinary traces |
| low-period formulas and bad-prime firewall are correct | EXACTLY CERTIFIED | producer, independent finite-field checker, 8 unit tests |
| \(a=6,n=5\) sextic is not new | CERTIFIED COLLISION | coefficient equality after \(x=6q\) with Endler--Gallas (2006) |
| registered fixed-\(n\) Route-A promotion | REJECTED / SCOPED NO-GO | universal local factor and absence of a new target divisor/operator; other global mechanisms remain open |

## Section plan

1. Introduction: state the no-go result and why separating \(r\) from \(n\)
   is necessary but insufficient.
2. Setup and source boundary: Paper-5 map, periodic schemes, compactification
   caveat, and related zeta/Galois literature.
3. Finite-flat periodic schemes: cyclic presentation, Gröbner proof,
   degree-drop and étale criteria.
4. Frobenius collapse: permutation determinant, nilpotent blindness, global
   Dedekind interpretation, and joint trace replacement.
5. Exact certificate: \(a=6,n=1,2\), good and bad cells, information-loss
   control, period-five collision.
6. Route-A evaluation and residual research question.
7. Conclusion and limitations.
8. Appendix: proof details and reproducibility ledger.

## Quantitative facts to surface

- finite-flat rank is exactly \(2^n\);
- all fixed-\(n\) Frobenius eigenvalues are roots of unity;
- 8/8 unit tests pass;
- 36 frozen low-period cells pass independent enumeration;
- period-five coefficient vector equals the published vector in all 7
  coefficients;
- Galois certificate factor types are \([6]\), \([5,1]\), and
  \([2,1,1,1,1]\), but this structure is prior work.

## Intended readership and format

Short anonymous mathematical research note, not a conference ML paper.  Use a
plain `article` layout, theorem environments, modular section files, and only
verified primary citations.
