# HCS-C44 derivation package

## Question

Can the conjugate-paired, full-kernel Hénon moments left by HCS-C43 descend
across split Eisenstein primes to a pure self-dual compatible system over one
fixed number field?

The first necessary condition is elementary and decisive: the first moment at
every prime must lie in one fixed finite extension of \(\mathbf Q\).

## Step 1 — Recover the exact chronological first moment

HCS-C43 proves

\[
A_p(1;\psi)=2\operatorname{Tr}(R_pU_p^2)
            =\frac2p\sum_{x,y\in\mathbf F_p}\psi_p(f_p(x,y)),
\]

where

\[
f_p(x,y)=2x^3+2y^3+(1+\rho)xy.
\]

Pairing the additive character with its inverse gives

\[
B_{p,1}=A_p(1;\psi)+A_p(1;\psi^{-1})
       =\frac2p\sum_rH_p(r)\zeta_p^r.
\]

There is no hidden choice between the two nontrivial cubic roots: replacing
\(\rho\) by \(\rho^2\) leaves the value histogram unchanged because
\(f_\rho(\rho^2x,y)=f_{\rho^2}(x,y)\).

No chronological averaging occurs.  The clock remains
\(\log N\mathfrak p=\log p\) at a split Eisenstein prime.

## Step 2 — Convert field generation into a finite-field stabilizer

The Galois group of \(\mathbf Q(\zeta_p)\) scales the residue label \(r\).
Because the only rational relation among
\(1,\zeta_p,\ldots,\zeta_p^{p-1}\) is the cyclotomic all-ones relation,
and because scaling preserves the total mass of \(H_p\), the Galois
stabilizer of \(B_{p,1}\) is precisely

\[
\operatorname{Stab}(H_p)
=\{a\in\mathbf F_p^\times:H_p(ar)=H_p(r)\ \forall r\}.
\]

This is stronger than checking a numerical minimal polynomial.

## Step 3 — Detect the stabilizer using two moments

Write \(p-1=3m\).  For even \(k\),

\[
M_k=\sum_r r^kH_p(r)=2\sum_{x,y}f_p(x,y)^k\pmod p.
\]

Finite-field monomial orthogonality kills all multinomial terms except one at
each of the two chosen exponents:

\[
M_{2m}=2\binom{2m}{m}4^m,
\]

and, for \(p\ge13\),

\[
M_{2m+2}
=2\frac{(2m+2)!}{(m-2)!^2 6!}
  2^{2m-4}(1+\rho)^6.
\]

Both are nonzero modulo \(p\).  A stabilizer element therefore obeys both
\(a^{2m}=1\) and \(a^{2m+2}=1\), hence \(a^2=1\).  At \(p=7\), the first
power moment \(M_4=3\ne0\) gives \(a^4=1\), while
\(|\mathbf F_7^\times|=6\) gives \(a^6=1\); together they give the same
conclusion.  Evenness supplies the reverse inclusion.

## Step 4 — Close the fixed-field gate

The stabilizer is \(\{\pm1\}\), so

\[
\mathbf Q(B_{p,1})=\mathbf Q(\zeta_p)^+.
\]

The degrees \((p-1)/2\) are unbounded on the infinite set of split primes.
Consequently no fixed number field contains all first moments.  A fixed-field
compatible system is impossible before one asks about its rank, purity,
conductor, or functional equation.  A place-dependent choice of Galois
conjugate does not help, since every conjugate has the same degree.

## Step 5 — Identify the next canonical descents

Direct Galois trace is computable.  The zero level of \(f_p\) has \(p-3\)
points, which gives

\[
\operatorname{Tr}_{\mathbf Q(\zeta_p)^+/\mathbf Q}B_{p,1}=-6.
\]

Thus additive descent is canonical but highly lossy.  Galois trace and norm
are the two minimal invariant descents to test, not an exhaustive
classification: restriction of scalars and other Galois-invariant
constructions remain logically possible.  C45 next tests the Galois norm of
the whole local determinant and asks whether that multiplicative descent
produces bounded rational dynamics or merely replicates a growing cyclotomic
divisor.

## Route-A interpretation

This paper proves a sharp obstruction, not a positive Hilbert--Pólya
construction.  The paired moment retains the Hénon chronology, but the
proposed global arithmetic bridge cannot even acquire a fixed coefficient
field.  The appropriate evaluation is

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_ANALYTIC\_DETERMINANT},
  \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}).
\]
