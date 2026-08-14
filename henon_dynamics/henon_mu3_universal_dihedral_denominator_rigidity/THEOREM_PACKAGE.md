# HCS-C54 theorem package

## 1. Source and category

Let

\[
K=\mathbf Q(\rho),\qquad \rho^2+\rho+1=0,
\qquad N=2n,\qquad n\ge2,
\]

and define

\[
C_n=\sum_{i=0}^{N-1}x_i^3,
\qquad
Q_{n,\rho}=\sum_{i=0}^{N-2}x_ix_{i+1}+\rho x_{N-1}x_0.
\]

Write

\[
\operatorname{PMonStab}(C_n,Q_{n,\rho})
\]

for the subgroup of \(\operatorname{PGL}_N(K)\) represented by monomial
matrices that stabilize the homogeneous ideal \((C_n,Q_{n,\rho})\).  The
word “full” below always means full in this projective monomial category.  It
does not mean the full projective linear automorphism group.

Our convention is

\[
\operatorname{Dih}(C_m)
=\langle r,s\mid r^m=s^2=1,\ srs=r^{-1}\rangle,
\]

so this group has order \(2m\).

## 2. Universal projective monomial source group

**Theorem A (full universal source group).** For every \(n\ge2\),

\[
\operatorname{PMonStab}(C_n,Q_{n,\rho})
\cong\operatorname{Dih}(C_{3n}),
\qquad
\left|\operatorname{PMonStab}(C_n,Q_{n,\rho})\right|=6n.
\]

The support map gives an exact sequence

\[
1\longrightarrow C_3\longrightarrow
\operatorname{PMonStab}(C_n,Q_{n,\rho})
\longrightarrow\operatorname{Dih}(C_n)\longrightarrow1,
\]

where the support image consists of the even rotations and odd reflections
of the \(2n\)-cycle.

One can choose generators

\[
(rx)_i=\rho^{a_i}x_{i+2},
\qquad
a_i=
\begin{cases}
1,&i=N-2,\\
2,&i=N-1,\\
0,&\text{otherwise},
\end{cases}
\]

and

\[
(sx)_i=\rho^{b_i}x_{1-i},
\qquad
b_i=
\begin{cases}
1,&i=1\text{ or }(i\ge2\text{ even}),\\
0,&\text{otherwise}.
\end{cases}
\]

Indices are taken modulo \(N\).  They satisfy

\[
C_n(rx)=C_n(sx)=C_n(x),
\quad Q_{n,\rho}(rx)=Q_{n,\rho}(x),
\quad Q_{n,\rho}(sx)=\rho Q_{n,\rho}(x),
\]

and

\[
r^{3n}=s^2=1,\qquad srs=r^{-1}.
\]

Moreover,

\[
r^n=\operatorname{diag}(1,\rho,1,\rho,\ldots,1,\rho)
\]

projectively, so \(r\) has exact order \(3n\).
Every element of \(\langle r\rangle\) has rotation support, whereas \(s\)
has reflection support.  Thus \(s\notin\langle r\rangle\), and
\[
r^k,\quad r^ks,\qquad 0\le k<3n,
\]
are \(6n\) distinct elements.  The exhaustive count below shows that these
elements are the full stabilizer.

### Exhaustiveness mechanism

An ideal stabilizer preserves the quadratic line.  In degree three it has

\[
g^*C_n=aC_n+LQ_{n,\rho}.
\]

The first two cubic forms contain only pure cubes, while \(LQ_{n,\rho}\)
contains no pure cube.  Pure-cube comparison gives \(g^*C_n=aC_n\), and
then \(LQ_{n,\rho}=0\) gives \(L=0\).  Thus both equation lines are
preserved.

After projective normalization, every candidate is

\[
x_i\longmapsto\rho^{e_i}x_{\sigma(i)},
\qquad e_i\in\mathbf F_3,\qquad e_0=0.
\]

The support \(\sigma\) is dihedral.  Let \(E_j=\{j,j+1\}\), and let
\(c_j=0\) except \(c_{N-1}=1\).  If the quadric scale is \(\rho^q\),
coefficient comparison gives

\[
e_{j+1}=q+c_{\sigma(E_j)}-c_j-e_j\pmod3. \tag{A.1}
\]

Here \(q\in\mathbf F_3\) is a consequence, not an assumption.  If
\(g^*Q_{n,\rho}=\beta Q_{n,\rho}\), then on any edge the transformed
coefficient and the corresponding target coefficient both lie in \(\mu_3\).
Their ratio is \(\beta\), hence \(\beta\in\mu_3\) and
\(\beta=\rho^q\) for a unique \(q\in\mathbf F_3\).

Because \(N\) is even, the alternating sum of the \(q\)-terms vanishes.
Closure occurs precisely when the inverse image of the closing edge has odd
edge index.  Thus rotations \(i\mapsto i+k\) survive exactly for even
\(k\), and reflections \(i\mapsto k-i\) survive exactly for odd \(k\).
There are \(n+n\) supports and three values of \(q\) for each, giving
exactly \(6n\) normalized elements.

Theorem A is characteristic-zero equation algebra and needs no smoothness.

## 3. Semilinear rational group form

Let \(\tau(\rho)=\rho^2\).  Put \(\eta_0=0\), put \(\eta_i=1\) for
nonzero even \(i\), and put \(\eta_i=0\) for odd \(i\).  The HCS-C53
semilinear reversal is

\[
(M_nx)_i=\rho^{\eta_i}x_{-i}.
\]

It satisfies

\[
C_n(M_nx)=C_n(x),
\quad
Q_{n,\rho}(M_nx)=\rho Q_{n,\rho^2}(x),
\quad
M_n\tau(M_n)=I.
\]

**Theorem B (nonconstant rational group form).** Transport through this
descent datum acts on the generators of Theorem A by

\[
\delta(g)=M_n\tau(g)M_n^{-1},
\qquad
\delta(r)=r^{-1},
\qquad
\delta(s)=rs=sr^{-1}. \tag{B.1}
\]

Consequently \(G_n=\operatorname{Dih}(C_{3n})\) descends to a finite
etale \(\mathbf Q\)-group scheme \(\mathscr G_n\) of rank \(6n\), split
by \(K\), acting on the rational equation model.  It is nonconstant for
every \(n\ge2\), and

\[
\mathscr G_n(\mathbf Q)\cong C_2.
\]

More precisely, the fixed geometric elements are

\[
\begin{cases}
1,\ r^{3n/2},&n\text{ even},\\
1,\ r^{(3n+1)/2}s,&n\text{ odd}.
\end{cases}
\]

Indeed,

\[
\delta(r^k)=r^{-k},\qquad
\delta(r^ks)=r^{1-k}s,
\]

so the fixed congruences are \(2k=0\) and \(2k=1\) modulo \(3n\).
Exactly two of the \(6n\) geometric elements are rational.

### Reynolds scope

On a certified smooth row, the geometric Reynolds correspondence is

\[
e_{G_n}=\frac1{6n}\sum_{g\in G_n}\Gamma_g.
\]

For the quadratic base-change map \(q\), rational descent is

\[
e_{\mathscr G_n}=\frac12q_*e_{G_n},
\qquad
q^*e_{\mathscr G_n}=e_{G_n}.
\]

The Reynolds denominator \(6n\) and the transfer denominator \(2\) have
different origins.  No all-\(n\) Chow-motive statement follows from
Theorem B.

## 4. Packet-admissible smooth rows

A row \(n\) is **packet-admissible** when the source row is smooth and
actual rational compatible realizations \(\mathsf E_n\) and
\(\mathsf O_n\) have been constructed, pure of weights zero and one, with

\[
e_n:=\operatorname{rank}\mathsf E_n=\frac{4^n+5}{3},
\qquad
o_n:=\operatorname{rank}\mathsf O_n
=\frac{2(4^n-4)}3=2(e_n-3).
\]

HCS-C53 certifies these packet data only for \(n=2,3,4\).  It does not
prove semisimplicity.  For \(n\ge5\), packet-admissibility is a hypothesis,
not a conclusion.

For a good rational prime \(p\), write

\[
L_p(\mathsf V,u)=\det(1-F_pu\mid\mathsf V)^{-1},
\qquad
\operatorname{Log}_0L_p(\mathsf V,u)
=\sum_{m\ge1}\frac{\operatorname{Tr}(F_p^m\mid\mathsf V)}m u^m.
\]

All Frobenius operators here are geometric.

## 5. Ordinary split-factor rigidity

Here **ordinary** is project shorthand for realization by an actual
finite-rank compatible system with integral multiplicities.  It is unrelated
to \(p\)-adic or Newton-polygon ordinarity.

**Theorem C (ordinary split-factor classification).** Let \(n\ge2\) be
packet-admissible.  The following are equivalent.

1. There is an actual finite-rank rational compatible system
   \(\mathsf V_n\) such that, at every good rational prime \(p\) split in
   \(K\),

   \[
   \operatorname{Tr}(F_p\mid\mathsf V_n)
   =\frac4n\operatorname{Tr}
   (F_p\mid\mathsf E_n\oplus\mathsf O_n).
   \]

2. There is such a system satisfying the complete split-local factor
   identity

   \[
   \operatorname{Log}_0L_p(\mathsf V_n,u)
   =\frac4n\operatorname{Log}_0
   L_p(\mathsf E_n\oplus\mathsf O_n,u)
   \]

   at every good split prime.
3. \(n\mid4\).

Thus, for \(n\ge2\), the only rows are \(n=2\) and \(n=4\).

### Necessity

Condition 2 implies condition 1 by taking the coefficient of \(u\).  Under
condition 1, fix a coefficient prime \(\ell\), restrict the three
\(\ell\)-adic realizations to \(G_K\), and take their semisimplifications.
Semisimplification preserves traces, characteristic polynomials, ranks, and
purity.  Thus this proof step does not assert semisimplicity of any inherited
HCS-C53 packet.  The degree-one prime ideals of \(K\) form a
Dirichlet-density-one set and, outside the finite ramified set, lie over split
rational primes.  Chebotarev density and the
characteristic-zero Brauer--Nesbitt lemma give

\[
n[(\operatorname{Res}V_{n,\ell})^{\mathrm{ss}}]
=4[(\operatorname{Res}E_{n,\ell})^{\mathrm{ss}}]
+4[(\operatorname{Res}O_{n,\ell})^{\mathrm{ss}}] \tag{C.1}
\]

in the semisimple Grothendieck group.  Different pure weights have no common
irreducible constituent, so (C.1) separates by weight and forces

\[
n\mid4e_n,\qquad n\mid4o_n. \tag{C.2}
\]

Since \(o_n=2(e_n-3)\), (C.2) implies that \(n\) divides both
\(8e_n\) and \(8(e_n-3)\), hence \(n\mid24\).  The complete divisor
check is

| \(n\) | 2 | 3 | 4 | 6 | 8 | 12 | 24 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| \(4e_n\bmod n\) | 0 | 2 | 0 | 2 | 4 | 8 | 20 |
| \(4o_n\bmod n\) | 0 | 1 | 0 | 4 | 0 | 4 | 16 |

Only \(n=2,4\) survive.

### Sufficiency

If \(n\mid4\), take

\[
\mathsf V_n=
\mathsf E_n^{\oplus4/n}\oplus
\mathsf O_n^{\oplus4/n}.
\]

This actual system matches every power trace, so it satisfies the complete
local logarithm identity.

### Both pure rails are essential

At \(n=3\), the total scaled rank is the integer

\[
\frac43(e_3+o_3)=\frac43\cdot63=84,
\]

but the separate scaled ranks are \(92/3\) and \(160/3\).  A proof using
only total rank is invalid.

## 6. Exact third-row equivariant no-go

Over \(K\), the common geometric source group is

\[
G_3=\operatorname{Dih}(C_9),\qquad |G_3|=18.
\]

Its element orders are \(\{1:1,2:9,3:2,9:6\}\).  Let
\(\varepsilon\) be the reflection-sign representation and let
\(U_j\), \(1\le j\le4\), be the two-dimensional irreducibles with

\[
\chi_{U_j}(r^k)=\zeta_9^{jk}+\zeta_9^{-jk},
\qquad
\chi_{U_j}(r^ks)=0.
\]

**Theorem D (exact \(n=3\) common-group character).** The
residue-corrected Cayley--Jacobian quotient is

\[
H^{2,1}(X_3)\cong R_{1,-1},
\qquad \dim R_{1,-1}=27-7=20.
\]

The residue action is polynomial pullback multiplied by
\(\det(M_g)/\det(A_g)\).  Its rotation traces are

\[
(20,-1,-1,2,-1,-1,2,-1,-1),
\]

and every reflection trace is \(-2\).  Hence

\[
H^{2,1}(X_3)
=2\varepsilon+2U_1+2U_2+3U_3+2U_4
\]

and

\[
\mathsf O_3
=4\varepsilon+4U_1+4U_2+6U_3+4U_4. \tag{D.1}
\]

For the Fermat rail, including its extra trivial line, the rotation traces
are

\[
(23,2,2,-4,2,2,-4,2,2),
\]

every reflection trace is \(-1\), and

\[
\mathsf E_3
=\mathbf1+2\varepsilon+3U_1+3U_2+U_3+3U_4. \tag{D.2}
\]

No nonzero central \(G_3\)-isotypic summand of
\(\mathsf E_3\oplus\mathsf O_3\) has both rail multiplicities divisible
by three.  Therefore no such summand makes the factor \(4/3\) ordinary on
both pure rails.

The multiplicity pairs are

| sector | \(\mathsf E_3\) | \(\mathsf O_3\) | both divisible by 3? |
|---|---:|---:|:---:|
| \(\mathbf1\) | 1 | 0 | no |
| \(\varepsilon\) | 2 | 4 | no |
| \(U_1\) | 3 | 4 | no |
| \(U_2\) | 3 | 4 | no |
| \(U_3\) | 1 | 6 | no |
| \(U_4\) | 3 | 4 | no |

Over the coefficient field, \(U_1,U_2,U_4\) form one orbit block with
multiplicity pair \((3,4)\).  Rational coefficient packaging does not
remove the obstruction.

### Descent-data caveat

The frozen Fermat packet has its standard rational model, while the
complete-intersection packet uses \(M_3\)-descent.  Theorem D is first a
theorem for their common geometric \(G_3\)-action over \(K\).  To place
both rails under the same rational group scheme \(\mathscr G_3\), one must
use the \(M_3\)-twisted rational form of the Fermat rail.  That form has the
same split trace but can differ at inert primes.  The no-go is independent
of the choice because it already holds after restriction to \(K\).

## 7. Split-invisible counterpacket firewall

Fix a coefficient prime \(\ell\), a finite extension
\(E_\ell/\mathbf Q_\ell\) containing the in-scope traces, and one finite
set \(S\) containing \(\ell\), the ramified primes, and the bad primes of
all compatible systems under discussion.  For \(F=\mathbf Q\) or \(K\),
let \(S_F\) be the primes of \(F\) above \(S\), and write

\[
K_{0,\ell}^{\mathrm{ss}}(F;S_F)
\]

for the Grothendieck group generated by finite-dimensional continuous
semisimple \(E_\ell\)-representations of \(G_F\) arising from the
fixed-\(\ell\) realizations of those compatible systems and their
semisimple subquotients, all unramified outside the primes above \(S\).
Thus the category is not the unrestricted class of all representations of
\(G_F\).  Restriction gives

\[
\operatorname{Res}:K_{0,\ell}^{\mathrm{ss}}(\mathbf Q;S)
\longrightarrow K_{0,\ell}^{\mathrm{ss}}(K;S_K).
\]

**Proposition E (counterpacket firewall).** If a virtual rational class
\(D\) in this fixed-\(\ell\), finite-ramification category has trace zero
at all but a relative-Dirichlet-density-zero subset of the good rational
primes split in \(K\), then

\[
\operatorname{Res}(D)=0.
\]

Indeed, the prime ideals of \(K\) of residue degree one form a
Dirichlet-density-one set, and the exceptional rational split primes lift to
a density-zero subset of that set.

If \(D\) is actual, then \(D=0\).  For virtual classes the kernel can be
nonzero; for example

\[
\mathbf1-\chi_{K/\mathbf Q}
\]

is a nonzero split-invisible class because \(K/\mathbf Q\) is a nontrivial
quadratic extension.  More generally,
\(U-U\otimes\chi_{K/\mathbf Q}\) is a kernel class and is nonzero whenever
\(U\not\simeq U\otimes\chi_{K/\mathbf Q}\).  Every kernel class has rank
zero and changes neither a
\(K\)-rail rank nor a \(K\)-side source-isotypic multiplicity.  Quadratic
twists can change the rational extension and inert traces, but they cannot
clear the denominators in Theorems C or D.

## 8. Split/global firewall

At a good inert prime, if

\[
P_p(U)=\prod_i(1-\alpha_iU),
\]

then

\[
P_{K,v}(U^2)=P_p(U)P_p(-U),
\]

which is generally not a square.  Theorems C and D prove no global root,
inert root, continuation, functional equation, automorphy, or RH.

## 9. Complete exclusions

The package does not prove:

- that \(\operatorname{PMonStab}\) is the full PGL automorphism group;
- smoothness, a Chow motive, or packet-admissibility for \(n\ge5\);
- descent of all \(6n\) geometric automorphisms as rational points;
- a Reynolds average over rotations alone;
- a global or inert fractional Euler root;
- uniqueness of a rational extension from split traces;
- automorphy, meromorphic continuation, a functional equation, or RH.
