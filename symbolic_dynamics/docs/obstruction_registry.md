# Symbolic-Dynamics Obstruction Registry

This registry is append-only.  An entry is added only after its proof or exact
certificate exists.  Every obstruction states its scope so that it cannot be
silently generalized to all symbolic dynamics.

| ID | Scope | Status | Statement | Artifact |
|---|---|---|---|---|
| SD-O01 | finite graph, finite-range roof/weight, finite-dimensional cocycle | **PROVED** | A nonzero determinant is a finite exponential polynomial with disk divisor count \(O(R)\), hence cannot carry the completed Riemann \(\Theta(R\log R)\) divisor | [proof](../finite_state_arithmetic_skeleton/PROOF_PACKAGE.md) |
| SD-O02 | squarefree admissible subshift with every \(p^2\) exclusion | **PROVED** | The all-zero sequence is the only periodic point; \(\zeta(z)=1/(1-z)\) | [proof](../squarefree_admissible_shift/PROOF_PACKAGE.md) |
| SD-O03 | freely concatenable shared-base renewal code | **PROVED** | Two atoms create a mixed primitive necklace; the renewal zeta is not an independent Euler product over atoms | [proof](../renewal_inverse_design_obstruction/PROOF_PACKAGE.md) |
| SD-O04 | shared-base renewal with free complex first-return weights | **PROVED** | Every holomorphic germ \(H(0)=1\) is representable as \(1-F\); analytic fitting alone is non-identifying | [proof](../renewal_inverse_design_obstruction/PROOF_PACKAGE.md) |
| SD-O05 | unary regular or context-free return grammar | **PROVED** | Accepted lengths are ultimately periodic and therefore cannot equal the rational primes | [proof](../renewal_inverse_design_obstruction/PROOF_PACKAGE.md) |
| SD-O06 | finite-dimensional unitary twist of a shared-base renewal | **PROVED** | The mixed primitive factor \(\det(I-tU)\) is nonconstant and cannot be erased identically | [proof](../renewal_inverse_design_obstruction/PROOF_PACKAGE.md) |
| SD-O07 | recursive wheel-sieve graph with only level-increasing edges | **PROVED** | The recursion generates the primes and intrinsic log-scale increments but has no periodic paths | [proof](../wheel_sieve_level_shift/PROOF_PACKAGE.md) |

## Scope warning

SD-O01 is not a theorem about all finite-alphabet thermodynamic formalism:
an infinite-memory Hölder potential can lead to an infinite-dimensional
transfer operator.  SD-O03–SD-O06 are not theorems about every countable
Markov shift.  Any proposed escape must freeze a new same-object grammar and
pass A0 independently.
