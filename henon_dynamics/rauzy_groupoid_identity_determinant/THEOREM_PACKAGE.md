# HCS-C29 theorem package

## 1. Status and scope

This package records the exact Phase-2 results for HCS-C29.  It separates two
objects that must not be conflated:

1. the genuine two-sided natural extension of the positive AGY coding, whose
   forward periodic cocycle products are unchanged; and
2. a newly declared finite symmetric non-backtracking path groupoid obtained
   by adjoining a formal inverse to every frozen Rauzy arrow.

The first object has a trivial regular-group periodic-product determinant
germ.  The second has nonempty reduced identity-holonomy cycles and a
nonconstant dimension-normalized finite-Weil determinant germ.  The second
object is not claimed to carry the AGY roof or an AGY two-sided transfer
operator.

All matrix products use the locked convention

\[
g_{e_1\cdots e_n}=g_{e_n}\cdots g_{e_1},
\]

so later chronological steps multiply on the left.  Only odd primes occur in
finite-Weil statements, and path length is fixed before taking the prime
limit.

## 2. Source-locked hypotheses

The certificate locks six upstream artifacts by SHA-256:

| Input | SHA-256 |
|---|---|
| C25 exact certificate | `a35cee22714abbb9dc9aadcc165720d1ff77aff3b7f29071f53a1b451760bd12` |
| C25 theorem package | `e1835d63bef914b355ceb4f64acc9043d11a842e9f4e59c7573c63ff66d03702` |
| C26 exact certificate | `1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a` |
| C26 theorem package | `4e882cbc332711b4cd2f98e9530f89268c8fcf1712eb150aacfee968dcf50495` |
| C28 exact certificate | `98b9ed10433f5cc7eb56aa04f397caa1ebfbc03acc904552618bd06f30370a1e` |
| C28 theorem package | `3de68629b3c59c958683d79d96fc90fde901efd878896d192595370d02df8a4c` |

The following upstream conclusions are hypotheses of this package.

- C25 reconstructs the literal seven-state Rauzy graph, its integral
  chronological cocycle, a statewise common symplectic frame, and injectivity
  of the positive fixed-start word map.
- C26 supplies the frozen first-return matrices and the locally summable
  one-sided holomorphic AGY branch family.
- C28 proves, for every fixed integral symplectic matrix \(g\),

  \[
  p^{-2}\Theta_p(g)\longrightarrow \mathbf 1_{\{g=I\}}
  \qquad (p\longrightarrow\infty,\ p\text{ odd}).
  \]

No prime table, Riemann-zero table, fitted clock, averaged transition matrix,
or fitted normalization is used.

## 3. Formal inverse groupoid

Let \(E^+\) be the fourteen positive arrows of the frozen C25 graph.  For each
\(e\in E^+\), adjoin a distinct formal inverse \(\bar e\) with reversed
endpoints and matrix \(g_{\bar e}=g_e^{-1}\).  This inverse retains the same
labeled positive-edge identity.  In particular, a formal inverse is not
identified with a different original Rauzy arrow having opposite endpoints.

A word \(w=e_1\cdots e_n\) is admissible when endpoints concatenate.  It is
linearly non-backtracking if \(e_{j+1}\ne\bar e_j\), and cyclically
non-backtracking if additionally \(e_1\ne\bar e_n\).  A closed word is
primitive when it is not a proper power as a marked word.

### Lemma 3.1 -- gauge invariance

For arbitrary vertex gauges \(h_v\) in the same symplectic group, set

\[
g'_e=h_{t(e)}^{-1}g_eh_{s(e)}.
\]

Then formal inverses remain compatible and every based closed word satisfies

\[
g'_w=h_{s(w)}^{-1}g_wh_{s(w)}.
\]

Hence the statement \(g_w=I\) is independent of the chosen statewise
trivialization.

**Proof.**  The intermediate gauge factors telescope in chronological order.
For an inverse arrow the formula gives \(g'_{\bar e}=(g'_e)^{-1}\).  The
certificate also checks this identity with the nontrivial family
\(h_v=(g_{3t})^v\), \(v=0,\ldots,6\), and includes a nonidentity closed-loop
conjugacy sentinel.  \(\square\)

## 4. Exact C25 kernel cycles

### Theorem 4.1 -- two primitive length-six identity cycles

The marked words

\[
\begin{aligned}
C_1&=(0t,1b,0t^{-1},0b,3t,0b^{-1}),\\
C_2&=(4t,6b^{-1},6t,5b,6t^{-1},6b)
\end{aligned}
\]

are closed, primitive, cyclically non-backtracking, and satisfy
\(g_{C_1}=g_{C_2}=I_4\).  Their oriented rotation classes are distinct, each
has six marked rotations, neither inverse word is a rotation of the original,
and the two unoriented classes are distinct.  Consequently

\[
N^{\mathrm{C25}}_6\ge 24,
\]

where \(N_n\) counts all marked cyclically non-backtracking closed words with
identity holonomy.

**Proof.**  Exact state replay gives the state sequences
\((0,1,1,0,3,3,0)\) and \((4,4,6,5,5,6,4)\).  Separate exact integer
products in the raw and fixed frames give \(I_4\).  Direct word-period,
rotation, inverse-rotation, and cyclic-closure tests establish all remaining
claims.  The \(24\) marked contributions are the six rotations of each word
and of its distinct inverse class.  \(\square\)

### Proposition 4.2 -- exact bounded census

An exhaustive dynamic enumeration of the frozen 28-dart graph gives, for
\(1\le n\le9\),

\[
(N_1,\ldots,N_9)=(0,0,0,0,0,24,0,32,144).
\]

The corresponding numbers of oriented rotation classes are
\((0,0,0,0,0,4,0,4,16)\), and the numbers of dihedral classes are
\((0,0,0,0,0,2,0,2,8)\).  No primitive class in this window is self-inverse
up to rotation.  All-word and primitive counts are stored in distinct fields;
they happen to agree only in this length window.

The census is a bounded exact theorem, not a statement about all lengths.
The explicit cycles in Theorem 4.1, rather than extrapolation from the census,
prove nonconstancy below.

## 5. Exact C26 branch relation

Let \(A\) be the frozen C26 `gamma_star` return matrix.  Let \(H\) and \(K\)
be the two frozen elementary return bridges and let

\[
B=AHA,\qquad C=AKA,\qquad Y=H^{-1}KH.
\]

The exact matrices obey

\[
K-I=v\phi^{\mathsf T},\qquad
Y-I=w\psi^{\mathsf T},
\]

where

\[
v=(0,1,1,1)^{\mathsf T},\quad \phi=(1,0,0,0)^{\mathsf T},
\quad w=(-1,1,0,1)^{\mathsf T},\quad \psi=(1,0,0,1)^{\mathsf T},
\]

and

\[
\phi^{\mathsf T}v=\psi^{\mathsf T}w=0,
\qquad \phi^{\mathsf T}w=-1,
\qquad \psi^{\mathsf T}v=1.
\]

### Theorem 5.1 -- C26 braid relation and kernel word

The rank-one identities imply

\[
KYK=YKY=\Delta,
\qquad
\Delta=
\begin{pmatrix}
-1&0&0&-1\\
2&1&0&0\\
0&0&1&-1\\
2&0&0&1
\end{pmatrix}.
\]

Moreover, \(\Delta\ne I\), \(\Delta^2\ne I\), and \(\Delta^4=I\).  Expanding
the braid relation, substituting

\[
H=A^{-1}BA^{-1},\qquad K=A^{-1}CA^{-1},
\]

and freely reducing gives a nonempty length-24 word \(W(A,B,C)\) with
\(g_W=I\).  The producer derives \(W\) programmatically rather than accepting
it as an input sentinel.  The word is cyclically reduced, primitive, has 24
distinct rotations, and its inverse is not a rotation.  Therefore

\[
N^{\mathrm{C26}}_{24}\ge48.
\]

This is a lower bound, not a complete length-24 census.

**Proof.**  Multiplication of the two rank-one unipotents with the four scalar
contractions above gives the braid identity.  Separate written-order and
later-on-the-left path-order evaluations of the derived word give \(I_4\).
Exact word reduction and rotation tests give the combinatorial assertions.
Direct powers of the displayed integer matrix give the order-four statement.
\(\square\)

### Corollary 5.2 -- the C26 branch subgroup is not free

The subgroup generated by the three frozen C26 matrices \(A,B,C\) is not a
free group on those generators.  This does not contradict C25 positive-monoid
freeness because every certified group relation uses inverse symbols.

## 6. Normalized finite-Weil determinant germ

Let \(\mathcal G\) be either the finite C25 symmetric graph or the six-symbol
C26 symmetric rose.  Let \(B_p\) be its non-backtracking oriented-edge
operator, with each legal transition twisted by the full
\(p^2\)-dimensional finite Weil matrix \(\rho_p(g_e)\).  Write \(M=3\) for the
C25 Hashimoto row/column degree and \(M=5\) for the C26 rose.

Every block has norm one.  The block Schur estimate, using at most \(M\)
nonzero blocks in every row and column, gives

\[
\lVert B_p\rVert\le\sqrt{M\,M}=M.
\]

Thus \(|u|<1/M\) implies \(\lVert uB_p\rVert<1\), so \(I-uB_p\) is invertible
and its logarithm is the unique power-series branch based at the identity.

For \(|u|<1/M\), define the root by the analytic logarithm at the origin:

\[
D_p^{\mathrm{norm}}(u)
=\exp\!\left[p^{-2}\operatorname{Log}_0\det(I-uB_p)\right],
\qquad \operatorname{Log}_0\det(I)=0.
\]

### Theorem 6.1 -- group-trace limit

Let \(N_n\) be the number of all marked, cyclically non-backtracking closed
length-\(n\) paths in \(\mathcal G\) with identity chronological holonomy.
Then

\[
D_p^{\mathrm{norm}}(u)
\longrightarrow
D_\infty(u)
:=\exp\!\left[-\sum_{n\ge1}\frac{N_n}{n}u^n\right]
\]

locally uniformly for \(|u|<1/M\) as odd \(p\to\infty\).  In particular,
both the C25 and C26 limiting germs are nonconstant.  For C25,

\[
[u^6]\log D_\infty=-\frac{N_6}{6}=-4.
\]

For C26,

\[
[u^{24}]\log D_\infty=-\frac{N_{24}}{24}\le-2.
\]

Both statements hold on the common strict disc \(|u|<1/5\).

**Proof.**  The finite-dimensional trace-log identity gives

\[
p^{-2}\operatorname{Log}_0\det(I-uB_p)
=-\sum_{n\ge1}\frac{u^n}{n}
  \sum_{|w|=n\atop w\text{ marked closed CNB}}p^{-2}\Theta_p(g_w).
\]

For fixed \(n\), the path sum is finite.  C28 sends each summand to one when
\(g_w=I\) and to zero otherwise.  Unitarity of the blocks and the finite
Hashimoto degree give the prime-independent bound

\[
p^{-2}|\operatorname{Tr}B_p^n|\le |E^{\pm}|M^n.
\]

Dominated convergence of the power series is therefore locally uniform on
every smaller disc.  The C25 equality and C26 bound follow from Sections 4
and 5.  \(\square\)

### Corollary 6.2 -- finite-order primitive factor

Optionally attach a scalar mark \(x_e\) to each oriented edge by multiplying
the transition block that traverses \(e\) by \(x_e\).  On the smaller disc
\(|u|M\max_e|x_e|<1\), a primitive oriented cyclic orbit class \(P\) with
holonomy of exact order \(m\) has combined mark

\[
z_P=u^{\ell(P)}\prod_{e\in P}x_e.
\]

Its repetitions contribute

\[
 -\sum_{j\ge1}
 \frac{\ell(P)}{jm\ell(P)}z_P^{jm}
 =-\frac1m\sum_{j\ge1}\frac{z_P^{jm}}j
 =
\frac1m\operatorname{Log}_0(1-z_P^m)
\]

to the logarithm and hence the determinant factor

\[
\exp\!\left[\frac1m\operatorname{Log}_0(1-z_P^m)\right]
=(1-z_P^m)^{1/m},
\]

where every branch is fixed at \(z_P=0\).  The unit-weight model used in
Theorem 6.1 is the specialization \(x_e=1\).  The character atom at the
fourth repetition of the C26 torsion control is \(\Theta_p(\Delta^4)\), not
\(\Theta_p(\Delta)^4\).

This corollary does not assert a globally convergent primitive Euler product.

## 7. Natural-extension no-go

Let \(\mathcal H=A^2(\Omega)\) be the locked C26 scalar Bergman space, and let
\(\sigma_0\) be its source-locked summability constant.  For
\(\Re s>-\sigma_0\), write the one-sided branch operator as

\[
\mathcal L_s=\sum_\gamma T_{s,\gamma},
\qquad
\sum_\gamma\lVert T_{s,\gamma}\rVert_1<\infty,
\]

with the trace-norm sum locally uniform in \(s\).  Let \(G\) be the discrete
group generated by the positive AGY return holonomies, let \(\lambda\) be its
left regular representation, and let
\(\tau_G(\lambda(g))=\mathbf1_{\{g=e\}}\).  In the semifinite von Neumann
algebra

\[
\mathcal B(\mathcal H)\,\bar\otimes\,L(G)
\]

with trace \(\operatorname{Tr}_{\mathcal H}\otimes\tau_G\), form the regular
twist of the one-sided C26 operator,

\[
\mathcal L_{\mathrm{reg}}(s)
=\sum_\gamma T_{s,\gamma}\otimes\lambda(g_\gamma).
\]

The displayed majorant places this sum locally uniformly in

\[
L^1\!\left(
\mathcal B(\mathcal H)\bar\otimes L(G),
\operatorname{Tr}_{\mathcal H}\otimes\tau_G
\right),
\]

and makes every fixed power's word trace expansion absolutely meaningful.

### Theorem 7.1 -- unchanged positive products give the constant germ

For every \(\Re s>-\sigma_0\) and \(n\ge1\),

\[
(\operatorname{Tr}\otimes\tau_G)
  \bigl(\mathcal L_{\mathrm{reg}}(s)^n\bigr)=0.
\]

For every compact \(K\Subset\{\Re s>-\sigma_0\}\), the trace-log series is
defined whenever \(|u|\sup_{s\in K}\lVert\mathcal L_{\mathrm{reg}}(s)\rVert<1\).
On this small disc the analytic regular-trace periodic-product germ is

\[
\exp\!\left[-\sum_{n\ge1}\frac{u^n}{n}
(\operatorname{Tr}\otimes\tau_G)
\bigl(\mathcal L_{\mathrm{reg}}(s)^n\bigr)\right]=1.
\]

**Proof.**  Each trace term is supported on a positive periodic word and is
multiplied by \(\tau_G(\lambda(g_w))\).  Locked C25 positive-monoid
injectivity gives \(g_w\ne e\) for every nonempty positive word.  Hence every
term vanishes.  Absolute trace-norm summability justifies the word expansion
and the locally uniform small-\(u\) trace logarithm.  \(\square\)

### Corollary 7.2 -- semantic natural-extension control

Transporting the same forward periodic-product germ from the one-sided coding
to its genuine symbolic natural extension leaves it equal to one.  The
natural extension supplies past coordinates for the same forward periodic
orbits; it does not replace forward cocycle letters by group inverses and
therefore cannot manufacture the kernel cycles of Sections 4 and 5.

This corollary concerns only the transported unchanged-forward
periodic-product germ.  It does not claim construction or a trace theorem for
a new operator on a two-sided Banach space.

## 8. Reproducibility theorem

### Theorem 8.1 -- independent exact replay

The release producer emits a canonical JSON payload using only Python integer
and rational arithmetic.  A separate checker that does not import the
producer reconstructs the Rauzy graph, frames, formal inverses, C25 witnesses,
gauge control, bounded census, C26 relation, repetitions, determinant theorem,
and semantic firewalls.  It passes all 14 fail-closed gates.

The regression suite passes 38 tests.  It includes 250 random unimodular
matrix-inversion comparisons and rehashed mutations of the source lock,
chronology, inverse semantics, identity words, all-versus-primitive moments,
C26 matrices and count scope, repetition character law, finite-Weil limit,
determinant type, natural-extension identity, roof claim, and payload schema.

Certificate hashes:

- canonical payload: `d3bde8d574b64fc146a9a65e1215654ee3516a20b3c07a4cb1f0a76ff0f2ab35`;
- certificate file: `412840c37d2e474462b39ce7072614323023ac8e3f968bc16a9219cc3a0c0cca`;
- independent report: `f87ab0efb191be7ac68936c5eb25e95ba2dbfa2719614750c99f1934e918b215`.

## 9. Route-A boundary

The certified tuple is

\[
\boxed{(A1\_WEAK,\ A2\_ANALYTIC\_DETERMINANT,\
A3\_PARTIAL\_ANALYTIC\_STRUCTURE,\ A4\_FORMAL\_HINT)}.
\]

The overall status is `ROUTE_A_EXPLORATORY`.

- A1 is weak because the groupoid has intrinsic primitive cycles and exact
  repetition bookkeeping, but its unit-edge clock is a modeling choice, no
  all-length orbit-completeness or stability law is proved, and no prime-orbit
  clock or von-Mangoldt amplitude appears.
- A2 recognizes an exact, independently checked analytic determinant germ;
  there is no comparison with the divisor of \(\xi\).
- A3 is partial because only a common small disc and an exact coefficient
  theorem are known; there is no continuation, functional equation, gamma
  factor, trivial-zero mechanism, or counting law.
- A4 is only a formal hint because the cocycle and finite-Weil fibres are
  symplectic and natural at fixed prime, while the inverse-edge dynamics,
  positive roof, Hilbert space, and operator domain are not geometrically
  constructed.

Route B is not authorized.  The next large gate is to derive an intrinsic
positive reversible roof and a two-sided trace theorem.  If that gate cannot
be crossed, this dynamics should be closed as a finite combinatorial
determinant model and the exploration should pivot.
