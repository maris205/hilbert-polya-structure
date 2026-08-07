# Derivation package

## 1. Voltage-cover setup

Let \(X\) be a finite connected graph and let
\(\alpha:E^{\pm}(X)\to G\) be a voltage assignment into a finite group, with
\(\alpha(\bar e)=\alpha(e)^{-1}\). A primitive reduced oriented cycle \(P\)
has holonomy \(g_P\), well-defined up to conjugacy. Put
\(o_P=\operatorname{ord}(g_P)\). A positive locally constant roof gives the
cycle length

\[
\tau(P)=\sum_{e\in P}\tau(e).
\]

For a constant finite-dimensional unitary representation \(\rho\), the local
Artin--Ihara factor is

\[
L_P(s,\rho)
=\det(I-\rho(g_P)e^{-s\tau(P)})^{-1}.
\]

The chronological product \(g_P\) is computed before any trace, determinant,
or representation product is taken.

## 2. Canonical aggregation is order-only on each base orbit

### Proposition 1 (regular-minus-trivial local collapse)

Let \(Y\to X\) be the regular cover with deck group \(G\). For a primitive
base orbit \(P\), write \(x=e^{-s\tau(P)}\), \(g=g_P\), and
\(o=\operatorname{ord}(g)\). Then

\[
\prod_{\rho\in\widehat G}L_P(s,\rho)^{\dim\rho}
=(1-x^o)^{-|G|/o},
\]

and the canonical aggregate after removing the trivial representation is

\[
\boxed{
\prod_{\rho\ne\mathbf1}L_P(s,\rho)^{\dim\rho}
=(1-x)(1-x^o)^{-|G|/o}.}
\]

#### Proof

The regular representation decomposes as

\[
\operatorname{Reg}_G\simeq
\bigoplus_{\rho\in\widehat G}(\dim\rho)\rho.
\]

Right multiplication by \(g\) permutes \(G\) in \(|G|/o\) disjoint cycles of
length \(o\). Therefore

\[
\det(I-x\operatorname{Reg}_G(g))=(1-x^o)^{|G|/o}.
\]

Taking inverse determinants and using the regular decomposition proves the
first identity. The trivial representation contributes \((1-x)^{-1}\), so
dividing by it proves the second. \(\square\)

The proposition is standard graph-covering theory. Its consequence for this
project is an observability obstruction: the canonical scalar aggregate
retains the order of \(g_P\), but discards conjugacy information among
same-order holonomies. It does not erase all chronology, because chronology
can change the order itself.

### Corollary 2 (exponent-\(p\) collapse)

If every nonidentity element of \(G\) has order \(p\), the local canonical
aggregate distinguishes only \(g_P=1\) from \(g_P\ne1\). For example,
\(UT_4(\mathbb F_p)\) has this property for \(p\ge5\): if \(g=I+N\), then
\((I+N)^p=I+N^p=I\) because \(N^4=0\).

## 3. A chronology witness beyond first-order transition statistics

Use \(H_7=H(\mathbb F_7)\) with coordinates and multiplication

\[
(a,b,c)(a',b',c')=(a+a',b+b',c+c'+ab').
\]

Let lower-case letters denote \(x=(1,0,0)\), \(y=(0,1,0)\), and upper-case
letters their inverses. Direct chronological multiplication gives

\[
P=\mathrm{XXXyxxyxYY}\longmapsto(0,0,3),
\qquad
Q=\mathrm{XXXyxyxxYY}\longmapsto(0,0,2).
\]

Both words are cyclically reduced and primitive. They each contain three
\(x\)'s, three \(X\)'s, two \(y\)'s, and two \(Y\)'s. Their nonzero cyclic
directed-bigram counts are also identical:

\[
xx:1,\ xy:1,\ xY:1,\ XX:2,\ Xy:1,\ yx:2,\ YX:1,\ YY:1.
\]

They are not cyclic shifts and \(Q\) is not a cyclic shift of \(P^{-1}\).
The holonomies \(z^3\) and \(z^2\) are distinct central conjugacy classes and
are not inverses modulo seven. Both have order seven, so Proposition 1 gives
the same aggregate factor

\[
(1-x)(1-x^7)^{-49}.
\]

In the seven-dimensional Schrödinger representation with central character
\(\rho_k(z)=e^{-2\pi i k/7}I\), the two resolved local inverse determinants
are

\[
(1-e^{-6\pi i k/7}x)^{-7},\qquad
(1-e^{-4\pi i k/7}x)^{-7},
\]

which differ for a fixed \(k\ne0\). Thus an irrep ledger restores the
discarded conjugacy information, but the selection of one \(k\) requires
extra arithmetic structure and is not canonical under Galois permutation of
central characters.

## 4. Fixed finite roofs have only linear divisor growth

### Theorem 3 (finite-roof zero-density obstruction)

Let

\[
B(s)=\sum_{j=1}^r e^{-s\tau_j}B_j,
\qquad
B_j\in M_d(\mathbb C),\quad \tau_j>0,
\]

where \(r,d\) are fixed and the \(B_j\) do not depend on \(s\). The same
conclusion holds if each entry is a finite exponential sum. Then

\[
D(s)=\det(I-B(s))
\]

is a nonzero entire exponential polynomial. Its number of zeros, counted
with multiplicity, in any fixed strip

\[
a\le\Re s\le b,\qquad |\Im s|\le T
\]

is \(O(T)\).

#### Proof

Expanding the determinant gives a finite set
\(\Lambda\subset[0,\infty)\) and coefficients \(c_\lambda\) such that

\[
D(s)=\sum_{\lambda\in\Lambda}c_\lambda e^{-\lambda s}.
\]

All roofs are positive, so \(B(\sigma)\to0\) and \(D(\sigma)\to1\) as
\(\sigma\to+\infty\); in particular \(D\not\equiv0\). Put
\(L=\max\Lambda\) and choose a real \(\sigma_0\) with
\(|D(\sigma_0)|\ge1/2\). For \(|z|=2R\),

\[
|D(\sigma_0+z)|\le C e^{2LR}
\]

for a constant \(C\) independent of \(R\). Jensen's formula on the disk of
radius \(2R\) centered at \(\sigma_0\) yields

\[
n_D(R)\log2
\le \log C+2LR-\log|D(\sigma_0)|,
\]

because each zero in the concentric disk of radius \(R\) contributes at
least \(\log2\). Hence \(n_D(R)=O(R)\). Every fixed vertical rectangle of
height \(2T\) lies in such a disk with \(R=T+O(1)\). \(\square\)

Finite products and quotients of these determinants have \(O(T)\) total
divisor count. A fixed affine spectral change preserves the linear order. In
the commensurable case \(D\) is a polynomial in \(e^{-hs}\), so its zeros
repeat vertically on a lattice. The theorem shows that choosing finitely many
incommensurable roofs removes periodicity but not the density obstruction.

### Corollary 4 (Riemann divisor exclusion)

Riemann--von Mangoldt gives

\[
N_\xi(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}+O(\log T).
\]

Consequently, no fixed determinant in Theorem 3, no finite product or
quotient of such determinants, and no multiplication by a zero-free entire
factor can have the full nontrivial divisor of \(\xi\) under a fixed affine
spectral identification.

This corollary does not cover infinite-dimensional Fredholm determinants,
infinitely many roofs, non-locally-constant potentials, \(s\)-dependent
coefficients carrying Gamma or Dirichlet structure, nonlinear spectral
changes, or a moving tower limit whose dimension or exponential type grows
with \(T\).

## 5. Uniform new-sector gap fails in the Heisenberg congruence tower

Put \(q_m=3^m\) and let

\[
X_m=\operatorname{Cay}
\left(H(\mathbb Z/q_m\mathbb Z),
\{x,x^{-1},y,y^{-1}\}\right).
\]

These are four-regular graph covers. Two explicit exact-conductor sectors
show that the registered uniform Ramanujan/new-sector-gap mechanism fails:
nontrivial spectrum returns to the trivial branch. This does not rule out a
separately renormalized infinite determinant or subtraction scheme.

### Proposition 5 (exact-conductor abelian return)

The character

\[
\chi_m(x)=e^{2\pi i/q_m},\qquad \chi_m(y)=1
\]

does not factor through level \(m-1\), since its frequency is not divisible
by three. Its adjacency eigenvalue is

\[
\lambda_m^{\rm ab}=2+2\cos(2\pi/q_m)\longrightarrow4.
\]

For a four-regular graph, the Ramanujan bound is \(2\sqrt3\). Thus this
conductor-new sector violates the bound for \(m\ge2\). The associated Bass
quadratic

\[
1-\lambda_m^{\rm ab}u+3u^2
\]

has two real roots tending to \(1/3\) and \(1\).

### Proposition 6 (primitive nonabelian return)

Let \(U_m,V_m\) be the \(q_m\times q_m\) Weyl pair with

\[
U_mV_m=e^{-2\pi i/q_m}V_mU_m.
\]

For the presentation \([x,y]=z\), the representation is
\(x\mapsto U_m\), \(y\mapsto V_m\), and
\(z\mapsto e^{-2\pi i/q_m}I\).

More explicitly, with \(\omega_m=e^{-2\pi i/q_m}\),

\[
\rho_m(a,b,c)=\omega_m^cV_m^bU_m^a.
\]

The relation \(U_m^aV_m^{b'}=\omega_m^{ab'}V_m^{b'}U_m^a\) verifies the
Heisenberg group law. Its commutant is scalar: commuting with the
simple-spectrum operator \(V_m\) forces an operator to be diagonal, and
commuting with the cyclic shift \(U_m\) forces a constant diagonal.

The primitive central-character block is the self-adjoint Harper matrix

\[
H_m=U_m+U_m^*+V_m+V_m^*.
\]

The phase operator has \(q_m\) distinct eigenvalues and the shift acts
transitively on their eigenlines, so this Weyl representation is irreducible.
Its central frequency one does not factor through level \(m-1\), because the
central element \(z^{q_m/3}\) acts by \(e^{-2\pi i/3}\ne1\). Moreover,

\[
\lambda_{\max}(H_m)\longrightarrow4.
\]

#### Proof

The upper bound \(\|H_m\|\le4\) is immediate. Let
\(L_m=\lfloor\sqrt{q_m}\rfloor\) and let \(f_m\) be the normalized indicator
of the consecutive residues \(-L_m,\ldots,L_m\). For all sufficiently large
\(m\), the interval does not wrap around the cycle. With
\(n_m=2L_m+1\),

\[
\langle f_m,(U_m+U_m^*)f_m\rangle
=2\left(1-\frac1{n_m}\right),
\]

while

\[
\langle f_m,(V_m+V_m^*)f_m\rangle
\ge2\cos(2\pi L_m/q_m).
\]

The sum tends to four, proving the lower bound and hence the limit.
If equality \(\lambda_{\max}(H_m)=4\) held at a finite level, equality in
both unitary numerical-radius bounds would force a nonzero vector fixed by
both \(U_m\) and \(V_m\). The Weyl relation forbids this because
\(e^{-2\pi i/q_m}\ne1\). Thus the top eigenvalue is strictly below four at
every finite level.
\(\square\)

The numerical table is illustrative, but a completely rational threshold
certificate is available at \(q=243\), \(L=15\). Using
\(\cos x\ge1-x^2/2\) and \(\pi^2<10\), the displayed Rayleigh quotient is
larger than

\[
\frac{60}{31}+2-\frac{1000}{6561}
=\frac{769442}{203391},\qquad
\frac{769442}{203391}-\frac72
=\frac{115147}{406782}>0,\qquad
\frac72>2\sqrt3.
\]

Therefore removing all one-dimensional sectors still leaves
exact-conductor nonabelian eigenvalues above \(2\sqrt3\) for all sufficiently
large \(m\). For each finite level these eigenvalues are strictly below four,
so their Bass roots do not equal or cancel the trivial roots; they converge
to \(1/3\) and \(1\).

## 6. Route-A consequence

The HCS-C15 clock is finite word or roof length, not an intrinsic logarithmic
prime clock. Canonical aggregation destroys conjugacy-level holonomy; finite
representation resolution has the wrong divisor density; and the natural
amenable tower has nontrivial branch-pole return. No fixed self-adjoint
compact-resolvent operator or \(\xi\)-determinant emerges.

The scoped Route-A tuple is

~~~text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
~~~

with overall decision **ROUTE_A_REJECTED** and research outcome
**PROVED_SCOPED_OBSTRUCTION**.
