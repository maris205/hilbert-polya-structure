# Claims–Evidence Map

Status: independent cross-hostile A/B pass and final mechanical QA pass;
external release **HOLD**. Computation is used only as finite
falsification evidence, never as an asymptotic proof or a novelty argument.

| Claim | Proof anchor | Independent exact control | Residual risk |
|---|---|---|---|
| The chronological left product is `H(J_n,K_n,C_n)` and `C_n` counts `Y`-before-`X` pairs | Theorem 2.1; explicit Heisenberg law and the two left-multiplication updates | Literal integer multiplication of all 131,071 words through length 16 versus a separately coded word scanner | Reversing the product convention reverses the area orientation; the manuscript fixes `M_n=A_n...A_1` before any theorem |
| Fixed-content area slices are Gaussian-binomial polynomials, and Bernoulli mixing gives the exact biased PGF | Theorem 2.1; last-letter recurrence | 153 exhaustive histogram slices versus an independently generated polynomial recurrence | The Gaussian-binomial law is owned background, not a residual novelty claim |
| Conditional and biased mean/variance formulas are exact | Lemma 3.1 and Theorem 3.2; logarithmic derivatives plus total variance | 231 exact-rational biased distributions through time 32; 306 conditional moment assertions | Differentiation is at `z=e^t`; using ordinary derivatives at `z=1` without the chain rule would change the second cumulant. The fair binary formula is direct prior territory |
| The displayed full variance also follows without Gaussian polynomials | Shared-index covariance calculation in Theorem 3.2 | 231 exact pair-covariance identities checked separately against exhaustive biased moments | This is an independent derivation, not a claim that general inversion-moment methods are new |
| The strong law and explicit `n^(3/2)` CLT hold for `0<p<1` | Centered identity (3.7), summation by parts, triangular-array Lindeberg–Feller, and the `L^1` remainder bound | 24,573 wordwise centered-decomposition checks; 300 exact leading/residual variance identities | Finite checks do not prove convergence; endpoints are deterministic and handled separately |
| The matrix-norm polynomial exponent is two in the interior and one at `p=0,1` | Theorem 4.1; Frobenius identity, SLLN, norm equivalence, direct endpoints | 131,071 literal Frobenius identities and 600 endpoint assertions | This is a logarithmic polynomial exponent, not a positive Lyapunov exponent |
| Maximum and zero area events have the stated exact probabilities | Proposition 5.1; fixed-content extremizers and monotone words | Exhaustive extrema through length 16 and exact-rational probabilities through time 32 | The maximum has one balanced word for even `n` and two for odd `n`; both are included in the probability formula |
| The `n^2` annealed pressure has a kink at zero and differs strictly from the typical rate | Theorem 5.2; exact extremal lower bounds, deterministic upper bounds, and the SLLN | 594 exact exponential-moment squeeze assertions at rational tilts | This pressure concerns the central area observable; it is not the usual `n`-scale generalized Lyapunov exponent |

## Assumption and convention firewall

- `0<=p<=1`, `q=1-p`; probabilistic limit laws with positive variance are
  stated only for `0<p<1`.
- `M_n=A_n...A_1`; `A_1` acts first. A later `X` left-multiplies the current
  product and adds the number of earlier `Y` letters to the central entry.
- `C_n` counts `Y` before `X`, not the reverse inversion orientation.
- The matrix statement concerns any fixed finite-dimensional norm and the
  ratio `log ||M_n|| / log n`; all ordinary Lyapunov exponents are zero.
- The annealed pressure is `lim n^(-2) log E exp(theta C_n)`. The pathwise
  comparator is `lim theta C_n/n^2`, not an expectation of a matrix norm.
- At `p=0,1`, `C_n=0`; endpoint conclusions are direct rather than silent
  continuations of interior ergodic arguments.

## Internal collision firewall

- **P70:** weighted shifts on finite Heisenberg quotients, controlled by
  convolution nullities. P111 instead studies a positive infinite
  unipotent matrix cocycle and one chronological word-area coordinate.
- **P93:** random prefix/shift maps act on a symbolic stack and reduce to a
  reflected one-dimensional walk. P111 instead multiplies positive
  Heisenberg generators and records a quadratic pair statistic.
- **P99:** a deterministic unipotent shear acts on finite-index
  sublattices. P111 has an iid generator environment and no sublattice
  orbit-counting or zeta-function problem.
- **P104:** contracting monomial matrices are governed by a two-state
  occupation chain and singular-value pressure on the `n` scale. P111 is
  unipotent, has polynomial norm growth, and its rare-event pressure lives
  on the `n^2` central-coordinate scale.

## Owner subtraction

Canfield–Janson–Zeilberger own the fixed-content Mahonian/Gaussian-binomial
asymptotic setting (including their corrigendum). Takács directly treats
the uniform binary lattice-path area, and Janson directly treats uniform
random-word inversions, exact moments, limit theorems, and a Hoeffding
decomposition; these sources include the manuscript's `p=1/2`
specialization. Işlak–Özdemir provide general iid random-word subsequence
methods, and Diaconis–Hough provide broad unitriangular random-walk limit
theory. Those fields are background. The arbitrary-bias conjunction is only
a residual scope description, not a novelty claim. Search absence is not
evidence. A specialist direct-owner search is still required before any
external use.
