# A direct causal-sieve Hénon lift fails the canonical symplectic test

**Paper ID:** 133-causal-sieve-henon-symplectic-test  
**Record ID:** ASFS-SCOUT-20260914-97  
**Date / status:** 2026-09-14; PRE-P0 STOP — CANONICAL SYMPLECTICITY FAILS  
**Route state:** classical P0 not admitted; A0/A1/A2 unassigned; Route B NOT INVOKED.

## 1. Question, frozen object, and lineage

Can 050's candidate-support sieve be lifted directly into second-order Hénon
form while keeping its arithmetic fixed-point equation? The [scope card](candidate-card.md)
freezes, for every finite \(N\ge4\), coordinates \(2,\ldots,N\), \(m=N-1\), and

\[
G_n(q)=\prod_{\substack{2\le d\le\lfloor\sqrt n\rfloor\\d\mid n}}(1-q_d),
\quad H_N(x,y)=(y,2G(y)-x),\quad
\omega_N=\sum_{n=2}^N dx_n\wedge dy_n.
\]

The empty product is one. The formula uses divisibility and candidate
coordinates; no prime table or fitted parameter enters. On binary inputs,
\(G\) is exactly 050's finite restriction. The real polynomial extends this
rule, and the lift has diagonal equilibrium equation \(q=G(q)\).
The tested lineage arrow is prime-symbolic sieve → polynomial extension →
Hénon-type dimensional lift. No conjugacy to a previous Logistic or Hénon
parameter is assumed.

| Owner | Frozen definition | Outcome |
| --- | --- | --- |
| Arithmetic rule | divisor polynomial \(G\) | exact source relation |
| Map | \(H_N\) on \(\mathbb R^{2m}\) | polynomial diffeomorphism |
| Proposed symplectic form | canonical \(\omega_N\) | not preserved |
| Arithmetic equilibrium | diagonal solution of \(q=G(q)\) | finite prime-indicator vector |
| Full periodic ledger, roof, suspension | not selected | not evaluated after geometry failure |
| Operator, zeta, quantum lift | not supplied | no transferred owner |

This is a scoped scheme test before classical P0. It does not establish an
obstruction to every conservative or symplectic realization of a sieve.

## 2. Inverse, volume, and equilibrium

Direct substitution gives \(H_N^{-1}(u,v)=(2G(u)-v,u)\). If \(C(x,y)=(y,x)\),
then \(CH_NC=H_N^{-1}\). The derivative is

\[
A=DH_N=\begin{pmatrix}0&I\\-I&2DG(y)\end{pmatrix}.
\]

The map factors as rotation \((x,y)\mapsto(y,-x)\), followed by shear
\((u,v)\mapsto(u,v+2G(u))\). Both determinants are one, so
\(\det DH_N=1\) identically.

The fixed-point equations are \(x=y=q\) and \(q=G(q)\). Since each \(G_n\)
reads only smaller coordinates, induction determines a unique real solution.
For prime \(n\) the product is empty, hence one. For composite \(n\) an earlier
prime divisor \(d\le\sqrt n\) has \(q_d=1\), forcing zero. These values
conversely solve the equations. Thus the unique equilibrium is the diagonal
finite prime-indicator vector. This is a finite arithmetic consistency
result, not a global A0 result or a primitive orbit family.

## 3. Exact symplectic obstruction

Using \(J=\begin{pmatrix}0&I\\-I&0\end{pmatrix}\), direct multiplication yields

\[
A^TJA=
\begin{pmatrix}0&I\\-I&2(DG-DG^T)\end{pmatrix}.
\]

Consequently \(H_N^*\omega_N=\omega_N\) if and only if \(DG=DG^T\) everywhere.
Already

\[
G_2=G_3=1,\quad G_4=1-y_2,\qquad
\partial_{y_2}G_4=-1,\quad \partial_{y_4}G_2=0.
\]

At \(N=4\) the exact defect is

\[
H_4^*\omega_4-\omega_4=2\,dy_2\wedge dy_4\ne0.
\]

The same coefficient persists at every larger \(N\), being determined solely
by the displayed derivatives. Therefore every member of the frozen scheme
fails its specified canonical symplectic test.

More generally, a \(C^1\) force whose ith component reads only coordinates
preceding i has strictly triangular derivative. If this derivative were
symmetric, it would vanish. On a connected open domain the force would then
be constant. A nonconstant strictly causal force cannot remain unchanged in
\((x,y)\mapsto(y,f(y)-x)\) with the canonical two-form.

## 4. Controls, limits, and method

- **Decoupled geometric control:** \(N=3\) gives constant \(G=(1,1)\), hence
  a symplectic map. The first genuine divisor coupling at \(n=4\) is decisive.
- **Volume control:** determinant one holds for arbitrary \(G\), and would
  therefore be an insufficient geometry test.
- **Source control:** the finite prime vector is derived by induction.
  Replacing the force with that vector would change the candidate-support rule.
- **Cutoff control:** the same two-coordinate defect occurs in all \(N\ge4\);
  no extrapolation from a finite orbit enumeration is used.
- **Ownership control:** a different two-form, cotangent lift, gradient force,
  or infinite carrier requires a new card. None is excluded by this proof.

Method: exact block-matrix algebra and coordinate induction. No simulation,
parameter search, numerical precision, or orbit cutoff is used.

## 5. Gate assessment and decision

| Gate | Result | Scope |
| --- | --- | --- |
| Source lineage | exact sieve-polynomial/equilibrium relation | established in the attempted lift |
| Classical geometry/P0 | \(H_N^*\omega_N\ne\omega_N\) for \(N\ge4\) | scoped failure |
| A0 | finite source consistency only | classical gate not evaluated |
| A1 / A2 | not pursued after geometry failure | unassigned |
| Route B | not invoked | no Route-A-ready candidate |

**Portfolio position: stop, then fork.** The first divisor interaction decides
this direct lift. Any future reciprocal-coupling construction must freeze a
new force and prove its arithmetic meaning before studying returns.

## Evidence

- [Scope card](candidate-card.md)
- [Claim ledger](claim-ledger.md)
- [Sources and verification](evidence/README.md)
