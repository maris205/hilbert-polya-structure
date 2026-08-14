# DERIVATION PACKAGE — SD-C20

## 1. Data-type ledger

The derivation keeps five objects separate:

1. the tensor-subset base shift;
2. the finite-group skew extension;
3. irreducible character blocks of one regular transfer matrix;
4. an edge-separated primitive-word ledger;
5. the infinite trace-class realization on its honest half-plane.

No scalar block is promoted to the whole extension, no marked coefficient is
identified with an unmarked atom-multidegree coefficient, and no finite
polynomial identity is called analytic continuation.

## 2. Arrival matrix and regular decomposition

For \(m=|\mathcal E_P|\), the \(d_\rho m\)-dimensional block matrix is

\[
B_\rho(S,T)=w(T)\rho(\alpha(S,T)).
\]

The right regular representation satisfies

\[
\mathbb C[G]\cong
\bigoplus_{\rho\in\widehat G}V_\rho^{\oplus d_\rho}.
\]

Applying the Fourier transform only in the fiber yields

\[
B_{\mathrm{reg}}cong
\bigoplus_{\rho\in\widehat G}B_\rho^{\oplus d_\rho},
\]

so

\[
D_{\mathrm{reg}}=\prod_\rho D_\rho^{d_\rho}.
\]

This factorization is internal to one symbolic extension.  It does not mix
determinants from different transfer conventions.

## 3. Incidence orbit count

For an ordered pair of nonempty subsets, define

\[
u=|S\setminus T|,
\quad v=|S\cap T|,
\quad w=|T\setminus S|,
\quad z=n-u-v-w.
\]

The quadruple \((u,v,w,z)\) records the sizes of the four Venn regions and
therefore classifies the orbit under \(S_n\).  Counting nonnegative triples
with sum at most \(n\) gives

\[
\#\{(u,v,w):u+v+w\le n\}=\binom{n+3}{3}.
\]

The \(n+1\) triples \((0,0,w)\) have \(S=\varnothing\), and the \(n+1\)
triples \((u,0,0)\) have \(T=\varnothing\).  The zero triple lies in both
sets.  Thus

\[
N(n)=\binom{n+3}{3}-2(n+1)+1.
\]

The first values and increments are

\[
\begin{array}{c|rrrr}
n&1&2&3&4\\ \hline
N(n)&1&5&13&26\\
N(n)-N(n-1)&1&4&8&13.
\end{array}
\]

## 4. Natural gauge algebra

A natural vertex gauge is constant on each subset-cardinality orbit:

\[
b(S)=q_{|S|}.
\]

Gauging the one-letter clock \(a^{|T|}\) gives

\[
\alpha^q(S,T)
=q_{|S|}^{-1}a^{|T|}q_{|T|}
=q_{u+v}^{-1}a^{v+w}q_{v+w}.
\]

For two atoms, let

\[
(a,c,h,u,v)
=\bigl(g_{0,1,0},g_{0,2,0},g_{1,0,1},g_{0,1,1},g_{1,1,0}\bigr).
\]

After \(q_1=e\),

\[
u=a^2q_2,\qquad q_2=a^{-2}u.
\]

Consequently,

\[
h=a,\qquad
v=q_2^{-1}a=u^{-1}a^3,\qquad
c=q_2^{-1}a^2q_2=u^{-1}a^2u.
\]

This is a finite group identity with ordered multiplication; no commutativity
of \(G\) is assumed.

## 5. Atom-local determinant of the counting class

For \(\alpha_a(S,T)=a^{|T|}\), the block rows are identical.  Sylvester's
identity reduces the determinant to

\[
D_{\rho,P}
=\det\left(I-\sum_{T\ne\varnothing}
(-1)^{|T|+1}x_T\rho(a)^{|T|}\right).
\]

Expanding the commuting matrix product

\[
\prod_{p\in P}(I-x_p\rho(a))
\]

gives the matrix inside this determinant.  Hence

\[
D_{\rho,P}=\prod_{p\in P}\det(I-x_p\rho(a)).
\]

The formula survives every vertex gauge by block conjugation.

## 6. Frozen \(S_3\) transfer

Set \(P=\{p,q\}\), \(x=x_p\), \(y=x_q\), and order the states
\(p,q,pq\).  Their arrival weights are \(x,y,-xy\).  The transition table is

\[
\begin{array}{c|ccc}
 &p&q&pq\\ \hline
p&e&e&r\\
q&e&e&r\\
pq&t&t&e
\end{array}
\]

with \(r=(12)\) and \(t=(23)\).

### 6.1 One-dimensional blocks

For the trivial character,

\[
B_{\mathbf1}=
\begin{pmatrix}
x&y&-xy\\x&y&-xy\\x&y&-xy
\end{pmatrix},
\]

so the rank-one determinant is \((1-x)(1-y)\).

For the sign character,

\[
B_{\mathrm{sgn}}=
\begin{pmatrix}
x&y&xy\\x&y&xy\\-x&-y&-xy
\end{pmatrix}.
\]

Direct \(3\times3\) expansion again gives

\[
D_{\mathrm{sgn}}=(1-x)(1-y).
\]

Thus abelianization sees no leakage.

### 6.2 Standard block

Use

\[
R=\begin{pmatrix}-1&1\\0&1\end{pmatrix},
\qquad
T=\begin{pmatrix}1&0\\1&-1\end{pmatrix}.
\]

The \(6\times6\) matrix is

\[
B_{\mathrm{std}}=
\begin{pmatrix}
xI&yI&-xyR\\
xI&yI&-xyR\\
xT&yT&-xyI
\end{pmatrix}.
\]

The exact determinant expands to

\[
\begin{aligned}
D_{\mathrm{std}}={}&1-2x-2y+x^2+y^2+4xy
-5x^2y-5xy^2\\
&+3x^3y+3xy^3+7x^2y^2
-3x^3y^2-3x^2y^3\\
&+3x^4y^2+3x^2y^4+6x^3y^3.
\end{aligned}
\]

Subtracting the identity-reference determinant
\((1-x)^2(1-y)^2\) and factoring yields

\[
D_{\mathrm{std}}-(1-x)^2(1-y)^2
=3xy(x+y)(xy+1)(x+y-1).
\]

### 6.3 Trace-log ledger

Let

\[
\Delta\log D
=\log D_{\mathrm{std}}
-2\log(1-x)-2\log(1-y).
\]

Formal expansion gives

\[
\Delta\log D
=-3x^2y-3xy^2-3x^3y-6x^2y^2-3xy^3
+O_{\mathrm{tot}}(5),
\]

where \(O_{\mathrm{tot}}(5)\) denotes monomials of total degree at least five.
Thus the selected bidegree ((2,2)) coefficient is (-6), while the other two
total-degree-four coefficients are also recorded explicitly.  At bidegree
((3,3)), the aggregated coefficient is (-9); it is not the
isolated commutator contribution.

The two degree-three leaks come from primitive cycles
\([p,pq]\) and \([q,pq]\).  Their holonomy is \(rt\), their scalar weights are
\(-x^2y\) and \(-xy^2\), and
\(\chi_{\mathrm{std}}(rt)=-1\) instead of (2) at the identity.

## 7. Commutator marker

Before marking the two-atom commutator word, note that the holonomy image
itself becomes noncommutative on three atoms.  Based at \(p\), the words
\[
p\to\{p,q\}\to p,\qquad
p\to\{p,q\}\to\{p,q,\ell\}\to p
\]
give \(rt\) and \(rrt=t\), which do not commute in \(S_3\).

For

\[
\gamma_\square=[p,pq,q,pq],
\]

the transition word is \(rtrt=(rt)^2\), a nonidentity 3-cycle.  Its four
arrival weights multiply to

\[
(-xy)y(-xy)x=x^3y^3.
\]

The edge set is

\[
\{p\to pq,\ pq\to q,\ q\to pq,\ pq\to p\}.
\]

There are two pairings at the repeated state \(pq\).  One is the connected
four-cycle above; the other is the disconnected union of
\([p,pq]\) and \([q,pq]\).  Hence the connected trace-log word is isolated by
the product of its four commuting edge markers.  Its standard-character
difference from the identity reference is

\[
\chi_{\mathrm{std}}((rt)^2)-\chi_{\mathrm{std}}(e)=-1-2=-3.
\]

The coefficient gap has magnitude three.

## 8. Primitive and repetition expansion

Attach edge markers if needed and write

\[
\log D_\rho=-\sum_{n\ge1}\frac{\operatorname{tr}(B_\rho^n)}n.
\]

A primitive necklace of length \(\ell\) has \(\ell\) based rotations.  Its
\(m\)-fold traversal occurs in the \(n=m\ell\) trace and contributes

\[
-\frac1m
\chi_\rho(H(\gamma)^m)w(\gamma)^m.
\]

Exponentiating over primitive necklaces gives

\[
D_\rho
=\prod_{[\gamma]\ \mathrm{primitive}}
\det(I-w(\gamma)\rho(H(\gamma))).
\]

This regrouping uses rotation only.  Reversal changes the directed edge word
and is not identified.

## 9. Exact enumeration boundary

For two atoms every natural table is a five-tuple
\((a,c,h,u,v)\in G^5\).  For each tuple and irreducible \(\rho\), compare

\[
\det(I-B_\rho(x,y))
\]

with

\[
\det(I-x\rho(a))\det(I-y\rho(a)).
\]

The search uses exact group multiplication and exact representation matrices.
Modular polynomial grids reject most candidates; every survivor is certified
symbolically over the integer polynomial ring and then tested against

\[
h=a,\qquad v=u^{-1}a^3,\qquad c=u^{-1}a^2u.
\]

The completed counts are

\[
\begin{array}{c|r|r|r|r}
G&|G|^5&\text{weak clean}&\text{all-irrep clean}&\text{nongauge clean}\\ \hline
S_3&7{,}776&972&36&0\\
D_4&32{,}768&\text{not promoted}&64&0\\
Q_8&32{,}768&512&64&0.
\end{array}
\]

The all-irrep-clean count equals \(|G|^2\), the number of pairs \((a,u)\), in
all three groups.  This is finite evidence for a restricted conjecture, not
an all-group theorem.

## 10. Symmetric Fredholm realization

Let \(Q=\operatorname{diag}(q_S)\), \(q_S^2=w(S)\), and
\(A_\rho(S,T)=\rho(\alpha(S,T))\).  Then

\[
K_\rho=QA_\rho Q,\qquad B_\rho=A_\rho Q^2.
\]

Sylvester's identity gives

\[
\det(I-K_\rho)=\det(I-B_\rho)
\]

for finite cutoffs.  In the infinite prime inventory, set

\[
L(\sigma)=\prod_p(1+p^{-\sigma/2})-1.
\]

For \(\sigma>2\), \(L(\sigma)<\infty\) and

\[
\|K_\rho(s)\|_1\le d_\rho L(\sigma)^2.
\]

If \(L_N\) is the same product over the first \(N\) primes and \(\Pi_N\) the
corresponding projection, then

\[
\|K_\rho-\Pi_NK_\rho\Pi_N\|_1
\le d_\rho\bigl(L(\sigma)^2-L_N(\sigma)^2\bigr).
\]

Together with

\[
|\det(I+A)-\det(I+B)|
\le\|A-B\|_1
\exp(1+\|A\|_1+\|B\|_1),
\]

this supplies an explicit cutoff error envelope on every
\(\sigma\ge2+\delta\).

## 11. Route derivation

The strict same-object tuple is

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)
```

- A0 records the tensor-irreducible atom source and entropy clock; the
  incidence fiber itself is inventory-blind.
- A1 records intrinsic primitive cycles, repetitions, and holonomies, but no
  prime/prime-power bijection.
- A2 records exact finite character determinants and a trace-class same-object
  Fredholm realization for \(\operatorname{Re}s>2\).
- A3 fails because no completed/global analytic structure or Weil
  compression exists.
- A4 fails because no natural operator or geometric lift is defined.

Matched inventories reproduce the full algebra, so the adversarial verdict is

```text
STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH
```

and the overall decision is `ROUTE_A_REJECTED`; Route B remains locked.
