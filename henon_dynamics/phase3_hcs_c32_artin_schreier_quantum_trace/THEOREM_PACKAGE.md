# HCS-C32 Phase 3 theorem package

Status: `MORSE_LOCAL_GATE_STOPPED_BY_THEOREM_AND_EXACT_COLLISION`

This package separates three statements that must not be conflated:

1. critical points of the cyclic action are chronological periodic points of
   the area-preserving Hénon map;
2. a good-characteristic Morse germ is classified by its critical value and
   quadratic form;
3. that local classification does not classify the full global
   Artin--Schreier cohomology.

Throughout, (k=mathbb F_p) with (p>3), and

\[
H_6(q,p_0)=(1-6q^2-p_0,q),
\qquad
S_6(q,Q)=qQ-q+2q^3.
\]

For clock length (n), put

\[
\Phi_n(x_0,\ldots,x_{n-1})
=\sum_{i\bmod n}
\left(x_i x_{i+1}-x_i+2x_i^3\right).
\]

## Theorem 1: the critical equations preserve chronological dynamics

The critical equations of (Phi_n) are

\[
x_{i-1}+x_{i+1}-1+6x_i^2=0
\qquad(i\bmod n).
\]

Consequently, if (z_i=(x_i,x_{i-1})), then

\[
z_{i+1}=H_6(z_i).
\]

Thus the critical scheme of (Phi_n) is the chronological fixed scheme of
(H_6^n).  No averaged transition matrix is introduced.

### Proof

Differentiate the two action terms containing (x_i).  This gives the stated
equation, which rearranges to

\[
x_{i+1}=1-6x_i^2-x_{i-1}.
\]

This is exactly the first coordinate of (H_6(x_i,x_{i-1})), while its
second coordinate is (x_i).  The cyclic indices give closure after (n)
chronological steps.  The converse follows by reading the recurrence
backwards.  (square)

## Theorem 2: cyclic Hill identity in the frozen convention

Let (z=(x_0,\ldots,x_{n-1})) be a critical word, and define

\[
A(x)=
\begin{pmatrix}
-12x&-1\\
1&0
\end{pmatrix},
\qquad
M_z=A(x_{n-1})\cdots A(x_0).
\]

If (B_z=D^2\Phi_n(z)), with every cyclic action term differentiated before
identifying indices, then

\[
\boxed{
\det B_z=(-1)^{n+1}\det(I-M_z).
}
\]

The term-by-term rule is essential: at (n=1), the cyclic bilinear term adds
(2) to the diagonal; at (n=2), the two oriented cyclic terms give an
off-diagonal entry (2).

### Status of the result

The general discrete Hill formula is prior art.  The formula above is its
one-dimensional Hénon specialization with mixed derivative
(S_{qQ}=1), and its sign is independently replayed by the exact checker.

## Theorem 3: good-prime Morse-local classification

Let (f:X\to\mathbb A^1_k) be a function on a smooth (n)-fold and let
(x\in X(k)) be an isolated nondegenerate critical point.  Let
(c=f(x)) and let (B=D^2f(x)).  Since (p\ne2), the henselian function germ
is equivalent to

\[
c+\frac12 y^{\mathsf T}By.
\]

In particular, if two such germs have the same (c) and their Hessians obey

\[
C^{\mathsf T}B_1C=B_2,
\qquad C\in\operatorname{GL}_n(k),
\]

then the two henselian function germs, their Morse vanishing-cycle objects,
and their standard local Fourier transforms are isomorphic after the same
choice of additive character and shift convention.

For a nontrivial additive character
(psi_r=\psi\circ\operatorname{Tr}_{k_r/k}), (t\in k_r^\times), and the
quadratic character (chi_r), the raw quadratic Fourier factor is

\[
\sum_{y\in k_r^n}
\psi_r\!\left(t\left(c+\frac12y^{\mathsf T}By\right)\right)
=
\psi_r(tc)\,
\chi_r(t)^n\,
\chi_r(\det B)\,
\chi_r(2)^{-n}\,
G(\chi_r,\psi_r)^n.
\tag{1}
\]

The standard Fourier--Deligne transform includes a cohomological shift
([1]); with the convention frozen in the certificate, its trace function is
the negative of the unshifted raw Fourier integral.  The isomorphism claim is
independent of this common sign.

### Proof

The henselian Morse lemma reduces the two function germs to their quadratic
models.  The displayed congruence identifies those models by the linear
change of variables (y=C y').  Formula (1) follows by diagonalizing the
quadratic form and multiplying the one-dimensional Gauss sums.  Because the
matrix (C) is defined over (k), the same change of variables works after
every finite extension (k_r/k).  Functoriality of vanishing cycles and local
Fourier transform then gives the representation-level statement.  (square)

### What the theorem forgets

For fixed (n,c,psi), the unframed Morse-local object sees the quadratic
form through its isometry class, hence through rank and discriminant square
class over a finite field of odd characteristic.  It does not retain a chosen
coordinate volume form, so it cannot retain the field element (det B)
beyond multiplication by a square.

## Theorem 4: exact Hénon collision at (p=61,n=5)

Over (mathbb F_{61}), the words

\[
z_A=(12,12,40,27,40),
\qquad
z_B=(33,58,36,36,58)
\]

represent distinct primitive cyclic period-five orbits of (H_6).  Both are
critical points of (Phi_5) and satisfy

\[
\Phi_5(z_A)=\Phi_5(z_B)=45.
\]

Their Hessians are

\[
B_A=
\begin{pmatrix}
22&1&0&0&1\\
1&22&1&0&0\\
0&1&53&1&0\\
0&0&1&19&1\\
1&0&0&1&53
\end{pmatrix},
\]

\[
B_B=
\begin{pmatrix}
30&1&0&0&1\\
1&25&1&0&0\\
0&1&5&1&0\\
0&0&1&5&1\\
1&0&0&1&25
\end{pmatrix}.
\]

The exact invariants are

\[
\det B_A=44,
\qquad
\det B_B=7,
\qquad
\chi_{61}(44)=\chi_{61}(7)=-1.
\]

Moreover,

\[
44/7=15=25^2\pmod {61}.
\]

The independently checked congruence matrix

\[
C=
\begin{pmatrix}
9&45&15&55&29\\
46&30&6&10&27\\
16&29&0&20&15\\
0&0&0&11&12\\
0&0&0&0&7
\end{pmatrix}
\]

has determinant (22\ne0) and satisfies

\[
C^{\mathsf T}B_A C=B_B\pmod {61}.
\]

The chronological monodromies are

\[
M_A=
\begin{pmatrix}
49&10\\42&31
\end{pmatrix},
\qquad
M_B=
\begin{pmatrix}
10&11\\14&46
\end{pmatrix},
\]

and

\[
\det(I-M_A)=44,
\qquad
\det(I-M_B)=7.
\]

Thus the full Hill values differ while the henselian Morse germs and their
Morse-local Fourier--Deligne representations are isomorphic.

### Computational scope

The registered scan covers

\[
p\in\{5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61\},
\qquad 1\le n\le5.
\]

It contains 80 ((p,n)) cells.  Under the frozen collision criterion, the
only collision group in this window is the one above.  This uniqueness is a
finite-window census, not a theorem beyond the registered window.  The
witness was discovered before the protocol freeze; its mathematical force is
exact, but it is not a preregistered prediction.

## Corollary 5: the Morse-local Hill-information gate stops

There is no invariant of the unframed good-prime Morse-local
vanishing-cycle/Fourier representation that recovers the actual field element
(det(I-DH_6^n)) for every Hénon periodic orbit.

Indeed, Theorem 4 gives two different Hill values with isomorphic local
function germs and hence isomorphic local representations.

This is the precise decision

\[
\boxed{
\texttt{GOOD\_PRIME\_MORSE\_LOCAL\_HILL\_INFORMATION\_GATE}
=\texttt{STOP}.
}
\]

## Theorem 6: escape routes that remain open

Corollary 5 does not imply any of the following stronger statements:

1. that the global compactly supported Artin--Schreier cohomology is the same
   for the two actions;
2. that the contribution at infinity is determined by Morse germs;
3. that degenerate critical points forget higher jets;
4. that monodromy in a parameter family is determined by individual fibers;
5. that a framed local theory, carrying an externally chosen coordinate
   volume, forgets the determinant;
6. that arithmetic variation across primes contains no information.

The first four are intrinsic mathematical escape routes.  The fifth retains
the missing value only by adding framing data.  The sixth can at most begin
with global square-class information and requires a new assembly theorem.

## Route-A ruling

This Phase-3 result is a valuable obstruction, but it does not produce the
objects needed for a positive Route-A evaluation.  The Hénon clock and
periodic orbits are genuine, while the finite-field unitary family remains a
formal spectral hint; there is no canonical global determinant, prime-orbit
law, critical-line theorem, or Hilbert--Pólya operator.

The certificate therefore records formal Route-A status `NOT_TESTABLE`.  If
one forces the available material into the evaluator's four-axis vocabulary,
the conservative ceiling remains

\[
(A1\_\mathrm{WEAK},A2\_\mathrm{FAIL},A3\_\mathrm{FAIL},
A4\_\mathrm{FORMAL\_HINT}),
\]

with no Route-B authorization.

