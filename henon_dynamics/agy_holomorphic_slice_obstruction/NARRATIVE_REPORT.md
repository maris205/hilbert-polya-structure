# HCS-C26 narrative report

## One-sentence contribution

For one source-faithful countable AGY return system, a fixed positive Rauzy
prefix creates a common complex domain on which the scalar transfer operator
is trace class with algebraic Perron trace atoms, while the literal
unsmoothed infinite-dimensional oscillator twist is noncompact on the same
domain.

## Why this was the next large gate

HCS-C25 proved noncompactness on vector-valued `C_b^1` by a localized bump
and on normalized `L^2` by measure-theoretic branch compression.  Neither
argument transferred to a holomorphic space, because a nonzero holomorphic
function cannot be supported inside one branch cylinder.  The open question
was whether holomorphic base contraction could overcome the infinite
oscillator fibre.

The answer separates the scalar and fibre mechanisms sharply.  The fixed
strictly positive matrix prefix in every AGY return branch produces a common
three-complex-dimensional domain.  Countable scalar weights are summable
there, so standard holomorphic transfer theory yields a trace-class operator.
Constants and evaluation at one real point then expose the entire
metaplectic atom sum.  C24 and C25 force a positive essential norm, without
isolating any branch.

## Main results

1. **Common complex domain.**  The canonical complex positive cone is
   preserved by every nonnegative Rauzy remainder.  The fixed positive
   prefix maps its closure strictly inside.  An intermediate domain `Omega`
   therefore satisfies `h_gamma(Omega) compactly contained in Omega`
   uniformly over all countably many returns.
2. **Scalar determinant.**  The principal branch of
   `q_gamma(z)^(-(s+4))` is common to all branches, and its sup norms are
   summable for every `Re(s)>-sigma_0`.  The scalar Bergman operator belongs
   to exponential class `E(c,1/3)` and is trace class.
3. **Arithmetic trace atom.**  For a chronological word matrix
   `A_word in SL(4,Z)` with Perron root `lambda_word`, the fixed-point trace
   atom is exactly

   \[
   \lambda_{word}^{-(s+1)}/\chi_{word}'(\lambda_{word}).
   \]

   The projective dimension cancels the Jacobian exponent, and every Perron
   root is an algebraic unit.
4. **Same-domain obstruction.**  The vector-valued Bergman branch series is
   bounded and absolutely convergent, but evaluation on constants compresses
   it to an `ell^1` sum of distinct infinite-dimensional metaplectic atoms.
   Its essential norm is bounded below by the coefficient `ell^2` norm.
5. **Exact witness.**  The length-128 source branch supplies an exact
   rational one-atom lower bound, independently reconstructed by producer
   and checker scripts.

## What the result does not show

- The scalar determinant is not matched to the Riemann xi function.
- The twisted operator is not self-adjoint and has no ordinary Fredholm
  determinant.
- The theorem does not close a non-tensor anisotropic space with no bounded
  point or fibre slice.
- The AGY invariant-density normalization is not holomorphically extended.
- A distributional Weil character is not promoted to an ordinary trace.

## Decision

The holomorphic/no-localizer escape for the literal infinite oscillator
model is closed.  More variations of the base norm are small doors.  The
next large experiment should reduce the exact chronological symplectic
cocycle modulo odd primes and twist the scalar trace-class operator by
finite Weil representations of dimension `p^2`.
