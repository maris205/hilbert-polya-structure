# Derivation package

## 1. Invariant object

Let

\[
H_a(q,p)=(1-aq^2-p,q),
\qquad a_0=59/10,\quad a_1=61/10,
\]

and let a word act chronologically as

\[
F_w=H_{a_{w_{n-1}}}\circ\cdots\circ H_{a_{w_0}}.
\]

Put

\[
R=\mathbb Z[1/(2\cdot5\cdot59\cdot61)].
\]

Writing \(x_i\) for the first coordinate after \(i\) steps, the fixed scheme
is

\[
\mathcal X_w
=\operatorname{Spec}A_w,
\]

\[
A_w=R[x_0,\ldots,x_{n-1}]
/\left(
a_{w_i}x_i^2+x_{i-1}+x_{i+1}-1
\right)_{i\bmod n}.
\]

Later letters remain on the left.  Cyclic rotations give conjugate return
maps.  Reversal is recorded as an equality control from the common reversor;
it is not divided out of multiplicity.

## 2. Canonical finite-flat theorem

### Theorem 1

For every word \(w\) of length \(n\ge3\), \(A_w\) is finite free over \(R\)
of rank \(2^n\), with basis

\[
x_0^{\epsilon_0}\cdots x_{n-1}^{\epsilon_{n-1}},
\qquad \epsilon_i\in\{0,1\}.
\]

### Proof

Every \(a_{w_i}\) is a unit in \(R\).  Divide the \(i\)-th cyclic recurrence
by that unit.  Under any degree-compatible monomial order its leading
monomial is \(x_i^2\).  These leading monomials are pairwise coprime, so the
monic Buchberger product criterion applies over \(R\).  The displayed cyclic
equations are a Gröbner basis, and their standard monomials are exactly the
square-free monomials.  The quotient is therefore free of rank \(2^n\).
\(\square\)

This theorem eliminates the compactification-choice kill rule.  The affine
fixed algebra is already finite and flat over the canonical localization.

## 3. Lefschetz element and packet norm

In \(A_w\), define

\[
J_i=
\begin{pmatrix}
-2a_{w_i}x_i&-1\\1&0
\end{pmatrix},
\qquad
M_w=J_{n-1}\cdots J_0.
\]

Each \(J_i\) has determinant one.  If \(t_w=\operatorname{tr}M_w\), then

\[
L_{w,r}=\det(I-M_w^r)
=2-2T_r(t_w/2)\in A_w.
\]

Because \(A_w\) is finite free, the norm

\[
\Delta_{w,r}
=\det_R(\text{multiplication by }L_{w,r})
\]

is canonical up to the harmless choice of a basis ordering.

### Theorem 2

Let \(\ell\notin\{2,5,59,61\}\).  Then

\[
\ell\mid\Delta_{w,r}
\]

if and only if there is a geometric point

\[
x\in\mathcal X_w(\overline{\mathbb F}_\ell)
\]

such that

\[
\det(I-M_w(x)^r)=0.
\]

### Proof

Reduce the finite free algebra and the multiplication endomorphism modulo
\(\ell\).  The determinant vanishes precisely when multiplication by
\(L_{w,r}\) is not invertible.  In a finite-dimensional commutative algebra
over a field, an element is a unit exactly when its image is nonzero in every
residue field, equivalently at every geometric point.  The image of
\(L_{w,r}\) at a geometric fixed point is the displayed determinant.
\(\square\)

For \(r=1\), this is nontransversality of \(\operatorname{Fix}F_w\).  For
general \(r\), it detects a root-of-unity multiplier for the repeated return.
The residue degree of the closed point is retained as a separate axis \(e\).

## 4. Cyclic-resultant baseline

Define the full multiplier-package polynomial

\[
P_w(X)
=\operatorname{Norm}_{A_w/R}
\left(X^2-t_wX+1\right)\in R[X].
\]

It is monic of degree \(2^{n+1}\). Scheme multiplicities are retained by
the norm; no geometric root or multiplier is selected.

### Theorem 3

For every \(r\ge1\),

\[
\boxed{
\Delta_{w,r}
=\operatorname{Res}_X\!\left(P_w(X),X^r-1\right).
}
\]

### Proof

After a faithfully flat extension on which the finite algebra is triangular,
the norm is the product over its geometric points, counted with algebraic
multiplicity. At a point \(x\), area preservation gives the characteristic
polynomial

\[
X^2-t_w(x)X+1=(X-\lambda_x)(X-\lambda_x^{-1}).
\]

Since \(P_w\) is monic, its resultant with \(X^r-1\) is the product of
\(\alpha^r-1\) over all its roots. Pairing the two roots at each fixed point
gives

\[
(\lambda_x^r-1)(\lambda_x^{-r}-1)
=\det(I-M_w(x)^r).
\]

Multiplying over the finite algebra yields \(\Delta_{w,r}\). Both sides
descend to \(R\), proving the identity. \(\square\)

This is a decisive scope correction. For one fixed word, the complete
repetition tower is a classical cyclic-resultant sequence determined by the
single reciprocal polynomial \(P_w\). Its recurrence, divisor behavior, and
finite-determination phenomena are controls, not Hénon-specific novelty.
Only an exact relation coupling different words and different primitive
periods could survive this baseline.

## 5. Exact quotient computation

The code implements the basis in Theorem 1.  The reduction rule is

\[
x_i^2=a_{w_i}^{-1}(1-x_{i-1}-x_{i+1}).
\]

It constructs multiplication by every \(x_i\), computes \(t_w\) from the
left chronological matrix recurrence, and forms the multiplication matrix of
\(t_w\).  Instead of inserting fractions into the Chebyshev recurrence, it
uses

\[
S_0=2,\qquad S_1=t_w,\qquad
S_{r+1}=t_wS_r-S_{r-1},
\]

where \(S_r=2T_r(t_w/2)\).  Multiplication by

\[
L_{w,r}=2-S_r
\]

is singular precisely at the norm event.

The producer uses exact modular Gauss--Jordan elimination.  The independent
checker reconstructs each decisive quotient and uses SymPy `DomainMatrix`
over \(\mathbb F_\ell\), followed by an independent direct enumeration of
the rational witnesses.

## 6. Decisive chronology theorem

### Theorem 4

The packet-norm ramification event distinguishes both mandatory C22
chronology pairs.

1. The primitive words
   \[
   0000101,\qquad0001001
   \]
   have identical cyclic bigram ledgers, but at \(\ell=11\),
   \[
   11\mid\Delta_{0000101,1},
   \qquad
   11\nmid\Delta_{0001001,1}.
   \]
2. The primitive words
   \[
   00101011,\qquad00101101
   \]
   have identical cyclic trigram ledgers, but at \(\ell=3\),
   \[
   3\nmid\Delta_{00101011,1},
   \qquad
   3\mid\Delta_{00101101,1}.
   \]

### Exact witnesses and nonexistence certificates

For \(w=0000101\), \(\ell=11\), the point \((q,p)=(8,6)\) is fixed and

\[
M_w(8,6)=
\begin{pmatrix}1&10\\0&1\end{pmatrix}.
\]

The multiplication kernel of \(L_{w,1}\) has dimension one.  For its paired
word \(0001001\), that multiplication kernel has dimension zero.  Thus the
second nondivisibility statement holds over the algebraic closure, not only
over \(\mathbb F_{11}\).

For \(w=00101101\), \(\ell=3\), the point \((q,p)=(1,1)\) is fixed and

\[
M_w(1,1)=
\begin{pmatrix}0&1\\2&2\end{pmatrix}.
\]

The multiplication kernel has dimension one.  For its paired word
\(00101011\), the kernel dimension is zero.

All four fixed-algebra ranks are the expected \(128,128,256,256\), and every
cyclic quotient relation is checked on the full basis.  All rotations give
the same nullity; reversal gives the same value but is retained as metadata.

## 7. Prime scan and repetition controls

The release scans every degree-good prime through 43 at \(r=1\).  It does not
select only successful primes.  Additional asymmetric events appear in the
certificate, including period-seven separation at \(\ell=13\) and
period-eight separations at \(\ell=13,17,29\).

At the decisive primes, all repetitions through twelve are computed.  The
event sets are closed upward under divisibility within the tested window, as
they must be from the single-multiplier cyclotomic identity.  This is a
control, not evidence for a new strong-divisibility law.

## 8. Material passport

| Field | Value |
|---|---|
| Candidate | HCS-C23 adelic Lefschetz/ramification spectrum |
| Release | first gate, version 1.0.0 |
| Base ring | \(\mathbb Z[1/(2\cdot5\cdot59\cdot61)]\) |
| Clock | one chronological Hénon letter |
| Primitive controls | certified same-bigram \(n=7\), same-trigram \(n=8\) pairs |
| Prime protocol | every degree-good prime \(\le43\), not fitted |
| Repetition protocol | \(r\le12\) at decisive primes |
| Randomness | none |
| Producer | square-free quotient plus exact modular elimination |
| Independent method | reconstructed quotient plus SymPy finite-field DomainMatrix and direct fixed-point enumeration |
| Forbidden data | Riemann zeros, prime target selection, averaged letters, selected algebraic roots |
| Cyclic-resultant control | \(\Delta_{w,r}=\operatorname{Res}(P_w,X^r-1)\); fixed-word towers are baseline |

## 9. Claim boundary

Theorem 4 passes only the first fast kill: chronology survives full Galois
packetization at explicit primes.  It does not prove that the prime set is
infinite, that new primes appear at every sufficiently large repetition, or
that different periods satisfy a nontrivial strong-divisibility law.

The modular multiplication-kernel dimension is not identified with
\(v_\ell(\Delta_{w,r})\).  A Smith/Fitting computation over the localized
integer algebra is required for valuations.  No Euler product, target
divisor, functional equation, or self-adjoint spectral operator is defined.

The original unrestricted \(n\le10\), \(r\le12\), \(\ell\le251\) ledger is
not authorized merely to search for a pattern. Before more computation, one
must state a falsifiable cross-word, cross-period algebraic law and show that
matched reciprocal-polynomial controls would not force it. Otherwise C23
closes at this exact arithmetic-chronology baseline.
