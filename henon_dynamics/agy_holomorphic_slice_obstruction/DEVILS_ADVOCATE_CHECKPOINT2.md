# HCS-C26 devil's-advocate checkpoint 2

## Final pre-implementation verdict

**GO for the sharp scalar/twisted dichotomy and Perron trace theorem.**

The first checkpoint held scalar nuclearity because real Hilbert contraction
does not automatically extend to one complex neighborhood.  Two independent
audits found a different proof: every return matrix has the fixed strictly
positive left factor `P=B_gamma*^T`, while the remaining factor is
nonnegative.  This projective algebra creates a uniform complex gap and
survives all countably many branches.

## Strongest attempted counterexamples

### Counterexample 1: poles approach a real contracting interval

A family of rational maps can send one real interval strictly into itself,
have a uniform real derivative bound, and still have poles converging to the
interval.  Therefore “uniform real contraction implies a common complex
domain” is false in general.

**Why C26 survives:** every AGY branch is a projective map with a fixed
positive matrix factor.  Nonnegative projective maps preserve the canonical
complex positive cone, and the fixed positive map sends the entire closed
cone strictly inside.  No branch-dependent pole can approach the selected
intermediate domain.

### Counterexample 2: use the natural complexified AGY cell itself

If all branch images were contained in one compact subset of the natural
complex cell, their real restrictions could not partition the full real cell
up to measure zero near its boundary.

**Resolution:** C26 uses a larger domain `Omega` containing the closure of
the natural positive-prefix image.  All branch images lie in the smaller
natural cell, compactly inside `Omega`.

### Counterexample 3: characteristic polynomial loses chronology

Different words can share a characteristic polynomial, so a formula using
only `chi_word` might appear to average time order.

**Resolution:** the formula is evaluated word by word with

\[
A_{word}=A_{\gamma_n}\cdots A_{\gamma_1}.
\]

No words are identified.  Equal scalar trace values are allowed, but the
ordered integer matrix is constructed before its characteristic polynomial.

### Counterexample 4: complex powers make an algebraic claim false

The Perron root is an algebraic unit, but `lambda^(-(s+1))` is generally not
algebraic for complex `s`.

**Resolution:** the arithmetic claim concerns the chronological integral
matrix, its algebraic-unit Perron root, and its characteristic derivative.
No algebraicity of the complex-powered trace value is claimed.

### Counterexample 5: scalar trace class transfers to the oscillator fibre

It does not.  Tensoring a nonzero compact scalar operator with an
infinite-dimensional unitary repeats each nonzero singular value infinitely
often.

**Resolution:** C26 proves absolute boundedness of the vector branch sum and
then applies an exact evaluation slice.  The resulting metaplectic atom sum
has a strictly positive essential norm.

## Convention locks

1. Use raw `A_gamma=B_gamma^T in SL(4,Z)` in the Perron formula; never use a
   normalized matrix there.
2. In `T_gamma1 ... T_gamman`, the map is
   `h_gamman o ... o h_gamma1` and the matrix is
   `A_gamman ... A_gamma1`.
3. Keep projective complex dimension `3` distinct from Jacobian exponent
   `4`.
4. Weight summability is locally uniform on compact `s`-sets, not uniform as
   `|Im(s)|` tends to infinity.
5. The word trace sum is valid for fixed `n`; the logarithmic determinant
   series is asserted only for sufficiently small determinant variable.
6. The scalar Perron formula has no metaplectic sign or Weil character.
7. The invariant-density-normalized AGY operator is not holomorphically
   extended.

## Release criterion

Release only after the independent implementation catches mutations of:

- transpose and later-on-left chronology;
- loss of strict positivity in the fixed prefix;
- the `3` versus `4` dimension distinction;
- the weight exponent before and after trace-denominator cancellation;
- exact source matrix, point, normalizer, and Jacobian;
- producer/checker coupling.

If those gates pass, further Hardy/Bergman norm variations are explicitly
out of scope.  The next large door is the finite Weil fibre.
