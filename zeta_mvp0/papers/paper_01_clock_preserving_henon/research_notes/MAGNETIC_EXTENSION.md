# Magnetic Hénon--Weyl Extension

> **Authoritative status.**  The current quantum statement is Theorem
> `thm:magnetic-weyl` in `paper/sections/04_quantum_weyl.tex`.  In particular,
> the analytic \(+1\) below belongs only to the exact classical comparison
> function; the proved quantum remainder does not resolve a constant term.

## Theorem

Let \(a>-1\), \(a\ne0\), and let \(n\ge1\) and \(B\in\mathbb R\) be fixed.
Set

\[
 r_a=\frac{1}{1+\sqrt{1+a}},\qquad
 c_a=2ar_a=2(\sqrt{1+a}-1),
\]

\[
 \widetilde H_a(x,y)=(-c_ax-ax^2-y,x),\qquad
 \Psi_{a,n}=\widetilde H_a^n,
\]

and use the symmetric-gauge vector potential

\[
 A_B(x,y)=\frac B2(-y,x).
\]

The Friedrichs operator

\[
 \boxed{
 \mathcal H_{a,n,B}
 =\frac12(-i\nabla-A_B)^2
 +2\pi\exp\!\left(\pi|\Psi_{a,n}(q)|^2\right)}
\]

is self-adjoint, lower semibounded, and has compact resolvent.  If
\(D=2^n\), then

\[
 \boxed{
 N_{a,n,B}(E)
 =\frac{E}{2\pi}\log\frac{E}{2\pi}
  -\frac{E}{2\pi}
  +O_{a,n,B}\!\left(
    E^{3/4}(\log E)^{1+D/2}
  \right).}
\]

The \(+1\) belongs to the classical comparison function below.  The error is too
large to identify a quantum constant term.

**Status:** proved by extending the independently audited nonmagnetic
bracketing argument; independently audited again for the magnetic local
counts and symmetry clauses.

## Exact classical clock

The classical symbol is

\[
 h_B(q,p)=\frac12|p-A_B(q)|^2+V_{a,n}(q).
\]

For fixed \(q\), the translation \(p'=p-A_B(q)\) preserves momentum Lebesgue
measure.  It is not claimed to be a global canonical change when \(B\ne0\).
It gives

\[
 \mathcal N_{\rm cl,B}(E)
 =\frac1{2\pi}\int(E-V_{a,n}(q))_+\,dq.
\]

The determinant-one substitution \(u=\Psi_{a,n}(q)\) then yields exactly

\[
 \mathcal N_{\rm cl,B}(E)
 =\frac{E}{2\pi}\log\frac{E}{2\pi}
  -\frac{E}{2\pi}+1.
\]

Thus a fixed magnetic field can change the antiunitary symmetry while leaving
the entire classical mean clock unchanged.

## Self-adjointness and compactness

The natural closed form is

\[
 \mathfrak h_{a,n,B}[u]
 =\frac12\|(-i\nabla-A_B)u\|_2^2
 +\int V_{a,n}|u|^2.
\]

Properness of \(\Psi_{a,n}\) implies \(V_{a,n}(q)\to\infty\).  On bounded
sets \(A_B\) is bounded, so the magnetic gradient controls the local
\(H^1\) norm.  Rellich compactness on bounded sets plus the potential's tail
control makes the form-domain embedding compact.  The Friedrichs realization
therefore has compact resolvent.

## Local magnetic square count

Let \(Q\) be a square of side \(\ell=E^{-1/4}\) with center \(c_Q\).  The
gauge

\[
 \chi_Q(q)=A_B(c_Q)\cdot q
\]

removes the constant part of the vector potential.  The residual

\[
 a_Q(q)=A_B(q)-A_B(c_Q)
\]

satisfies, uniformly in the square's location,

\[
 \alpha_Q:=\|a_Q\|_\infty
 \le \frac{|B|}{2\sqrt2}\ell.
\]

For either the Dirichlet form domain \(H_0^1(Q)\) or the magnetic Neumann form
domain \(H^1(Q)\), and for \(0<\varepsilon<1\),

\[
 (1-\varepsilon)k_{0,Q}[u]
 -\frac{\alpha_Q^2}{2\varepsilon}\|u\|^2
 \le k_{B,Q}[u]
\]

and

\[
 k_{B,Q}[u]
 \le(1+\varepsilon)k_{0,Q}[u]
 +\frac{1+\varepsilon^{-1}}2\alpha_Q^2\|u\|^2.
\]

The Neumann condition here is the covariant condition

\[
 \nu\cdot(-i\nabla-A_B)u=0,
\]

not the ordinary normal derivative condition.  Min--max comparison with the
free square counts and the choice \(\varepsilon=\ell\) give, uniformly for
\(0\le A\le E\),

\[
 n_{B,D/N}(A)
 =\frac{\ell^2A}{2\pi}
 +O_B(\ell\sqrt E+1).
\]

The additional \(\ell^3A\) comparison term has the same size as
\(\ell\sqrt E\) at \(\ell=E^{-1/4}\).  Multiplication by the relevant-square
count

\[
 M(E)=O_{a,n}\!\left(
 \frac{L}{\ell^2}+\frac{L^{D/2}}{\ell}+1
 \right),
 \qquad L=\log(E/2\pi),
\]

fits inside the original
\(O_{a,n,B}(E^{3/4}L^{1+D/2})\) envelope.  The potential-oscillation and
first-exit estimates are unchanged.  Strict local counts and the final
\(E+1\) squeeze are used exactly as in `PROOF_PACKAGE.md`.

The theorem requires fixed \(B\).  It does not justify an arbitrary
energy-dependent field \(B(E)\).

## Time reversal and why centering matters

Let \(\mathcal C\) be complex conjugation.  Since \(A_B\) and \(V\) are real,

\[
 \mathcal C\mathcal H_{a,n,B}\mathcal C
 =\mathcal H_{a,n,-B}.
\]

At \(B=0\), \(\mathcal C\) is an internal antiunitary symmetry with
\(\mathcal C^2=+1\).  At \(B\ne0\), bare conjugation is not an internal
symmetry.  A reflection \(S\) preserving the potential could nevertheless
make \(U_S\mathcal C\) an internal antiunitary symmetry, because orientation
reversal also flips the magnetic pseudoscalar.

For the centered potential at \(a\ne0\) and \(n=1,2\), no such
orientation-reversing Euclidean isometry exists.  Indeed:

1. \(|\widetilde H_a^n(q)|^2\) has the unique zero \(q=0\), so a preserving
   Euclidean isometry must be an orthogonal linear map.
2. Its highest homogeneous term is \(C_{a,n}x^{2^{n+1}}\), forcing an
   orientation-reversing candidate to have the diagonal form
   \(S=\operatorname{diag}(s,-s)\), \(s=\pm1\).
3. With
   \[
   A=D\widetilde H_a(0)=
   \begin{pmatrix}-c_a&-1\\1&0\end{pmatrix},
   \]
   the off-diagonal entries of \(A^TA\) and
   \((A^2)^TA^2\) are respectively \(c_a\) and \(c_a^3\).  A diagonal
   reflection changes their signs, so it cannot preserve the quadratic
   Taylor form when \(c_a\ne0\).

This covers the production cases \(a=1.02,6\) for \(n=1,2\).  By contrast,
the uncentered one-iterate potential has an \(x\mapsto-x\) reflection, and the
radial \(a=0\) control retains reflections.  Centering is therefore a
structural symmetry choice, not merely a conditioning trick.

The argument excludes standard local geometric antiunitary symmetries; it
does not prove that no abstract nonlocal antiunitary exists.  It also does not
cover every \(n\ge3\) without a separate symmetry audit.  Constant magnetic
coupling supplies a unitary-class candidate, not the \(T^2=-1\) spin/GSE
structure.

## Non-claims

- The theorem supplies Q and W, not a prime-power trace P.
- Broken standard time reversal does not by itself prove GUE statistics.
- GUE-like statistics do not identify individual zeta zeros.
- No value of \(B\) is selected by number theory in the present construction.
