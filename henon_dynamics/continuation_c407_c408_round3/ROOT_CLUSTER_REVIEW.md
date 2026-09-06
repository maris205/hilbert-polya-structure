# Non-author proof audit and direct local-algebra controls

2026-09-06. Reviewer: current-team root coordinator. This is an internal
mathematical review, not external or human peer review. The reviewed artifact
is `cluster_boundary/PROOF_PACKAGE.md`, Sections 1–9 in its initial 345-line
candidate version. The author's later source notes and generating-function
extension require their own affected review.

## Mathematical assessment

No blocking mathematical error was found in the proposed full alternating-
zero local-length formula after reading and checking the entire argument.
The following were checked explicitly, not inferred from numerical examples:

- The odd-coordinate implicit eliminations use nonzero derivatives, and
  the constant root products are one. Formal logarithms replace each
  relation by a unit multiple. For m=1 the loop contributes twice in the
  derivative; for m=2 the repeated edge contributes twice as required.
- The product-generator intersection expansion does not assume radicality.
  Every final choice has finite colength once the path/cycle calculations
  are known. Intermediate choices are parameter sequences in a regular
  local ring; the remaining one-dimensional quotient is Cohen–Macaulay.
  Its two factors are parameters/nonzerodivisors, so the length-additivity
  exact sequence is legitimate. Disjoint path factors multiply lengths.
- The path Hessian kernel vector has nonzero self-pairing, so its standard
  orthogonal complement is nondegenerate over C. For L=4r−1 the displayed
  alternating even-coordinate correction solves all endpoint equations.
  Its residual has order at least k+1, including k=3 where (k−1)^2=k+1.
  The subsequent correction changes the potential only at degree at least
  2k+2. Direct substitution gives r(k^2−1)/2, or −23r for k=3.
- Cyclic shift by four and uniqueness of the complementary solution really
  reduce m=4r to r times the four-cycle potential. The two graph reflections
  flip a and b separately on the kernel; no nonexistent global sign
  symmetry of an odd-degree unary term is being assumed.
- At the four-cycle, the kernel pair potential has mixed quartic coefficient
  one. The cubic complementary correction contributes −9 when k=3, hence
  alpha=−8. On an axis, the pair and unary contributions give
  beta=(k^2−2)/4 for odd k≥5 and beta=−5 for k=3. Both are nonzero.
- The two-variable argument needs no unproved Newton-nondegeneracy claim.
  The invertible Jacobian of (W_A,W_B) implies their ideal is (A,B);
  after square substitution its colength is four. The two axis orders are
  2k−2. Four-term intersection additivity therefore gives 4k+1.

## Direct independent controls from the original equations

The root coordinator wrote `ROOT_CLUSTER_CHECK.sing`. It uses rational
coefficients, the original cyclic exchange equations, and the literal
coordinate shift to `(0,−1,0,−1,...)`. A local `ds` standard basis computes
the local quotient length. It does not use the author's logarithmic
potential, effective-potential expansion, or coefficient-check output.

Actual completed execution:

```sh
Singular -q henon_dynamics/continuation_c407_c408_round3/ROOT_CLUSTER_CHECK.sing
```

Environment: Singular 4.2.1 (4212, 64 bit), Debian 1:4.2.1-p3+ds-1.
Exit status 0. The six completed exact values were:

| k | m=1 | m=2 | m=3 |
|---|---:|---:|---:|
| 3 | 2 | 6 | 11 |
| 5 | 2 | 10 | 17 |

All six agree with the theorem. They are bounded consistency controls,
not a proof for all periods or parameters.

An initial direct attempt at k=3,m=4 was stopped after more than 77 seconds,
at roughly 0.9 GiB RSS, without producing its local length; its process
returned exit status 1 after termination. It is **not a passed check**.
The final reproduction script excludes that costly case. The two-dimensional
resonance is supported here by the independently checked analytic argument,
not by a fictitious completed standard-basis computation.

## Scope clarification requested before admission

The observable belongs to the full finite cyclic exchange-equation algebra.
Its alternating-zero points are outside the original torus domain of
`F_k=(y,(1+y^k)/x)`. Do not identify these local thickenings with ordinary
periodic points, or with fixed-point schemes of a smooth cluster-surface
extension, without a separate scheme comparison. For example, the displayed
completed presentation has embedding dimension m, since all its generators
have order at least two. When m>2 it cannot be the fixed-point local scheme
of an endomorphism of a smooth two-dimensional surface. The original
relation algebra and a saturated/extended dynamical model must be kept apart.

This clarification was sent to the author. Source ownership is still an
admission gate: the known deep-point support must be attributed and deducted.
The proof's actual candidate increment is its all-m, all-odd-k local
thickness classification, not discovery of the alternating support.

No C-number, final route verdict, or paper acceptance is conferred by this
review alone. No sealed round-2 payload was modified or rechecked.

## Affected follow-up and source admission, 2026-09-06

The coordinator subsequently read the full 426-line revised proof package,
including Section 10, and the author's complete source audit. The marked-
separator double count is valid for labeled cyclic subsets: with q omitted
vertices, q times the weighted count is m times the coefficient of the qth
power of the separator/run series. Its logarithmic sum gives the stated
quartic determinant; the all-selected correction is exactly
`1+4(k-1)*1_(4|m)`. The native-clock parity weights yield
`Z_k(u^2)^((k+1)/2) Z_k(-u^2)^((k-1)/2)` because k is odd. There is no
identification of this formal local-length series with an Artin–Mazur zeta.

For source comparison, the coordinator actually read Beyer–Muller,
arXiv:2403.15589v1, all of Section 4, and Benito–Faber–Mourtada–Schober,
arXiv:2401.06758v2, all of Section 5 (original arXiv HTML, retrieved on
2026-09-06). The former owns the alternating deep-point support; the
latter's Theorem 5.2.3 confirms the relevant characteristic-zero rank-two
cluster surface is smooth. These sources do not identify its fixed scheme
with the unsaturated cyclic relation algebra. The revised proof now states
that distinction and the embedding-dimension obstruction explicitly.

No blocking issue remains in the reviewed proof or these actual citation
dependencies. The retained increment is the complete local-thickness
classification for all odd k>=3 and all m, including its two resonance
calculations and the resulting rational local-length series. This is a
substantial scoped intersection problem, not a claim to solve the entire
boundary or torus orbit-counting problem. The coordinator admits it for
C408 manuscript development. Full manuscript review and release gates
remain pending; this is not a claim of publication priority or peer review.
