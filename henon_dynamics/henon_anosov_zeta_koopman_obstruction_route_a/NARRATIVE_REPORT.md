# Narrative report — C125

## Motivation

C119 supplied a natural global trace-class operator but its base contraction
had no nontrivial primitive dynamics.  C121 supplied an all-order algebraic
degree theorem but only a low-period orbit witness.  C125 deliberately puts a
complete primitive-orbit census, an exact global orbit zeta, and a natural
global Hilbert-space action in one source model, then tests whether the two
global objects are determinant-compatible.

## Exact orbit result

For the hyperbolic toral automorphism induced by
\(A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\), every
\(A^n-I\) is nonsingular.  Its torus kernel has size
\(|\det(A^n-I)|\).  Writing \(S_n=\operatorname{tr}(A^n)\), the recurrence
\(S_n=3S_{n-1}-S_{n-2}\) gives
\(N_n=S_n-2\) at every order.  Möbius inversion therefore produces a
complete least-period census, not a finite orbit search.

The first fixed counts are

\[
1,5,16,45,121,320,841,2205,\ldots,
\]

and the first primitive-orbit counts are

\[
1,2,5,10,24,50,120,270,\ldots.
\]

Their primitive Euler product resums exactly to

\[
\zeta_T(z)=\frac{(1-z)^2}{1-3z+z^2}.
\]

## Natural-owner obstruction

The Koopman operator on \(L^2(\mathbb T^2)\) is source-defined and unitary.
On Fourier characters it is the infinite basis permutation
\(e_k\mapsto e_{A^{\mathsf T}k}\).  The orthonormal sequence
\(e_{(j,0)}\) maps to the orthonormal sequence \(e_{(2j,j)}\), so the
operator is not compact, belongs to no finite Schatten class, and has no
ordinary trace-class Fredholm determinant.  Thus rich recurrent dynamics and
a natural global operator coexist, but the orbit zeta is not the ordinary
determinant of this natural owner.

## Controls and validation

The parabolic shear produces nonisolated fixed circles.  Omitting the
absolute value converts cardinalities into negative signed determinants.
Finite cyclic Fourier aliasing gives exact modulus-dependent pseudo-traces;
at iterate three, moduli \(2,3,4,5\) give \(4,1,16,1\).  These controls
separate the source zeta from common finite-section shortcuts.

The independent checker reconstructs every field, the SymPy implementation
passes 238 exact checks, replay fixes the canonical bytes, and all 23 hostile
mutations are rejected.

## Interpretation and limit

The all-order orbit and zeta theorem is clear progress over the finite and
low-period C104--C123 gates.  It does not supply a prime-like correspondence,
target divisor, sealed target comparison, target functional equation, or
trace-compatible natural quantization.  The strict tuple is therefore
`(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`, overall
`ROUTE_A_EXPLORATORY`, and Route B remains unauthorized.
