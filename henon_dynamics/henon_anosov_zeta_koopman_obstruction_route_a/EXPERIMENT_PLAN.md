# Experiment plan — C125

## Frozen objects

- phase space: \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\) with normalized Haar
  measure;
- matrix: \(A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\);
- clock: one torus iterate;
- orbit convention: unsigned fixed-point cardinality;
- zeta convention:
  \(\exp(\sum_{n\ge1}\#\operatorname{Fix}(T_A^n)z^n/n)\);
- replay cutoff: periods one through twelve, subordinate to an all-order
  theorem;
- Hilbert owner: Koopman composition on \(L^2(\mathbb T^2)\);
- controls: parabolic shear, omitted absolute value, cyclic Fourier aliasing
  at moduli two through twelve;
- scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Gates

1. Verify \(A\in SL(2,\mathbb Z)\), its exact eigenvalues, and hyperbolicity.
2. Prove \(\#\operatorname{Fix}(T_A^n)=|\det(A^n-I)|\) for every \(n\).
3. Derive the trace recurrence and replay fixed counts through \(n=12\).
4. Recover exact-period points and primitive orbits by Möbius inversion.
5. Derive and series-check \((1-z)^2/(1-3z+z^2)\).
6. Prove the Fourier action, unitarity, noncompactness, non-Schatten status,
   and absence of an ordinary trace-class Fredholm determinant.
7. Run all three negative-control families without reinterpreting their
   outputs as the source zeta.
8. Run producer, independent checker, SymPy reconstruction, byte replay, and
   at least twenty hostile mutations.
9. Compile in two isolated fixed-date directories, audit fonts and logs,
   render both pages, and close the manifest.

## Failure conditions

- a fixed-count row disagrees with the integer kernel determinant;
- a primitive-point count is negative or not divisible by its period;
- the logarithm of the rational zeta fails to recover \(N_n/n\);
- the signed determinant is reported as an unsigned cardinality;
- a parabolic nonisolated fixed set is forced into the finite zeta convention;
- a cyclic wrap-around pseudo-trace is presented as cutoff-independent;
- the Koopman unitary is called compact, Schatten, trace class, or an owner of
  the Artin--Mazur zeta;
- an internally exact zeta is upgraded to A2 without target-divisor tests;
- A4 is promoted beyond a formal hint;
- any accepted hostile mutation, nondeterministic PDF, unembedded font,
  warning, layout defect, or manifest mismatch.
