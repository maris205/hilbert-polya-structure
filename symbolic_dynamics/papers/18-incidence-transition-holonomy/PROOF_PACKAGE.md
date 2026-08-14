# PROOF PACKAGE — SD-C20

## Claim

For the source-locked tensor-subset full shift, functorial transition
cocycles are stable functions of three incidence counts.  Their natural
one-letter gauge subclass has atom-local character determinants.  Outside
that subclass, the frozen \(S_3\) refinement/coarsening cocycle has genuine
noncommutative periodic holonomy: its trivial and sign blocks remain
atom-local, but its standard block has an explicit mixed leakage term.  A
cycle-separated nonreference holonomy must leak in some irreducible
character.  The same symbolic mechanism is inventory-blind, so it does not
provide arithmetic selectivity.

## Status

`PROVABLE AS STATED`, with three explicit qualifications.

1. The clean-versus-gauge classification for all finite groups is not
   proved.  The \(S_3,D_4,Q_8\) counts are exact finite evidence.
2. Character determinants are not claimed to classify cocycles.
3. The arithmetic no-go is for the source-locked incidence mechanism and
   its matched-inventory controls, not for every symbolic grammar.

## Assumptions

- \(P\) is a finite nonempty atom set and
  \(\mathcal E_P=2^P\setminus\{\varnothing\}\).
- Every ordered pair in \(\mathcal E_P^2\) is an allowed directed edge.
- \(G\) is a fixed finite group with no atom-label action.
- The cocycle is one-step, relabeling-natural, and compatible with
  restriction to smaller atom inventories.
- \(x_p\) are independent commuting variables,
  \(x_S=\prod_{p\in S}x_p\), and
  \(w(S)=(-1)^{|S|+1}x_S\).
- Primitive closed words are quotiented by rotation only.
- Ordinary commuting edge variables are used as isolating markers only when
  the relevant edge multiset has a unique connected cyclic traversal.
- All representation matrices are finite-dimensional and unitary up to an
  equivalent exact realization.

## Notation

For an irreducible representation \(\rho\),

\[
B_{\rho,P}(S,T)=w(T)\rho(\alpha(S,T)),
\qquad D_{\rho,P}=\det(I-B_{\rho,P}).
\]

For a closed word
\(\gamma=(S_0,\ldots,S_{n-1},S_0)\), write

\[
H_\alpha(\gamma)=\prod_{j=0}^{n-1}\alpha(S_j,S_{j+1}),
\qquad
w(\gamma)=\prod_{j=0}^{n-1}w(S_{j+1}).
\]

## Proof strategy

The argument moves from invariants to a minimal witness.  Relabeling orbits
of ordered subset pairs give the incidence classification.  Natural vertex
gauges then identify the complete count+coboundary subclass and its
atom-local determinant.  The frozen \(S_3\) rule violates this subclass and
has a nonidentity closed-word holonomy.  Exact block determinants show that
one-dimensional characters miss the obstruction while the standard
representation detects it.  A marked-cycle trace-log lemma gives the general
character-separation statement.  Finally an entrywise nuclear estimate gives
the honest Fredholm half-plane, while free-variable naturality proves the
arithmetic control no-go.

## Dependency map

1. Theorem 1 proves the same-object Artin decomposition and trivial block.
2. Theorem 2 proves gauge invariance and the simultaneous-holonomy test.
3. Theorem 3 classifies functorial incidence data and counts its types.
4. Theorem 4 identifies the natural counting gauge class and determinant.
5. Theorem 5 proves that the \(S_3\) candidate is not one-letter cohomology
   and has a noncommutative holonomy image.
6. Theorem 6 calculates all two-atom \(S_3\) character blocks.
7. Theorem 7 turns separated holonomy into unavoidable character leakage.
8. Theorem 8 proves the trace-class Fredholm realization on
   \(\operatorname{Re}s>2\).
9. Corollary 9 combines free-variable naturality and controls into the
   arithmetic selectivity no-go.

## Proofs

### Theorem 1 — same-object Artin blocks and the trivial Euler factor

For every finite \(P\), finite \(G\), and edge cocycle \(\alpha_P\), the
right-regular determinant decomposes as

\[
D_{\mathrm{reg},P}
=\prod_{\rho\in\widehat G}D_{\rho,P}^{d_\rho}.
\]

The trivial block is

\[
D_{\mathbf1,P}=\prod_{p\in P}(1-x_p).
\]

#### Proof

The right regular representation is unitarily equivalent to
\(\bigoplus_{\rho\in\widehat G}\rho^{\oplus d_\rho}\), up to replacing every
representation by its contragredient under the opposite multiplication
convention.  Applying this fixed fiber Fourier transform at every symbolic
state block-diagonalizes \(B_{\mathrm{reg},P}\).  Taking finite determinants
gives the stated product.

For the trivial representation,
\(B_{\mathbf1,P}(S,T)=w(T)\); all rows are identical.  The matrix has rank at
most one and its only possible nonzero eigenvalue is
\(\sum_Tw(T)\).  Therefore

\[
D_{\mathbf1,P}=1-\sum_{\varnothing\ne T\subseteq P}
(-1)^{|T|+1}x_T.
\]

Finite inclusion--exclusion gives

\[
1-\sum_{T\ne\varnothing}(-1)^{|T|+1}x_T
=\prod_{p\in P}(1-x_p).
\]

This proves both statements. ∎

### Theorem 2 — gauge invariance and simultaneous holonomy

Let

\[
\alpha^b(S,T)=b(S)^{-1}\alpha(S,T)b(T).
\]

Then \(D_{\rho,P}^{\alpha^b}=D_{\rho,P}^{\alpha}\), and every closed-word
holonomy is conjugated by the gauge value at its base state.  Two cocycles on
the finite connected presentation graph are gauge equivalent exactly when a
spanning-tree recursion produces a vertex gauge satisfying every non-tree
edge; equivalently, all fundamental based closed-walk holonomies agree under
one simultaneous root conjugator.

#### Proof

Let \(C_b\) be block diagonal with state block \(\rho(b(S))\).  Since scalar
arrival weights commute with representation matrices,

\[
B_\rho^{\alpha^b}=C_b^{-1}B_\rho^\alpha C_b.
\]

The determinant is invariant under conjugation.  Multiplying the transformed
edge values around a based closed word telescopes all intermediate \(b\)
factors and gives

\[
H_{\alpha^b}(\gamma)=b(S_0)^{-1}H_\alpha(\gamma)b(S_0).
\]

For the converse criterion, adjoin a formal inverse dart to every directed
edge, assigning inverse gain.  Fix a root, a spanning tree, and a proposed
root conjugator.  Along each tree edge the gauge equation uniquely determines
the gauge at the next vertex.  The resulting map is a gauge equivalence if
and only if it satisfies every remaining directed edge.  Closing a non-tree
edge with the unique tree paths converts precisely that check into equality
of its fundamental based holonomy under the same root conjugator.  The
conditions are therefore equivalent. ∎

### Theorem 3 — functorial incidence classification

Under the source-lock naturality assumptions,

\[
\alpha_P(S,T)=g_{u,v,w},\qquad
(u,v,w)=(|S\setminus T|,|S\cap T|,|T\setminus S|).
\]

For \(|P|=n\), the number of possible stable types is

\[
N(n)=\binom{n+3}{3}-(2n+1).
\]

#### Proof

Partition \(P\) into the four regions
\(S\setminus T\), \(S\cap T\), \(T\setminus S\), and
\(P\setminus(S\cup T)\).  Two ordered pairs \((S,T)\) and \((S',T')\) are in
the same orbit under atom bijections if and only if the four region sizes
agree.  Since \(|P|=n\), the fourth size is determined by \(n-u-v-w\).
Relabeling naturality thus makes the cocycle constant on each triple
\((u,v,w)\); restriction compatibility identifies the same triple across
larger inventories.  Conversely, any stable table on those triples defines a
relabeling-natural restriction-compatible local rule.

There are \(\binom{n+3}{3}\) nonnegative triples with
\(u+v+w\le n\).  The forbidden condition \(S=\varnothing\) is \(u=v=0\),
giving \(n+1\) triples.  The forbidden condition \(T=\varnothing\) is
\(v=w=0\), also giving \(n+1\) triples.  Their intersection is the zero
triple, counted twice.  Inclusion--exclusion therefore subtracts
\(2(n+1)-1=2n+1\). ∎

### Theorem 4 — natural counting gauge class

A natural vertex gauge has \(b_P(S)=q_{|S|}\).  The natural gauge orbit of

\[
\alpha_a(S,T)=a^{|T|}
\]

is exactly

\[
g_{u,v,w}=q_{u+v}^{-1}a^{v+w}q_{v+w}.
\tag{P.1}
\]

Every member of this orbit satisfies

\[
D_{\rho,P}=\prod_{p\in P}\det(I-x_p\rho(a)).
\tag{P.2}
\]

For two atoms, after \(q_1=e\), (P.1) is equivalent to

\[
h=a,\qquad v=u^{-1}a^3,\qquad c=u^{-1}a^2u.
\tag{P.3}
\]

#### Proof

Relabeling acts transitively on subsets of a fixed cardinality, so a natural
vertex map is constant on each cardinality orbit.  Restriction compatibility
makes those values stable across inventories; write them \(q_k\).  Applying
the gauge formula to \(\alpha_a\) gives (P.1), because
\(|S|=u+v\) and \(|T|=v+w\).

It remains to prove (P.2) before gauging.  Since
\(\alpha_a(S,T)\) depends only on \(T\), all block rows of \(B_\rho\) agree.
The finite matrix determinant lemma or Sylvester's identity reduces the
determinant to

\[
\det\left(I-\sum_{\varnothing\ne T\subseteq P}
(-1)^{|T|+1}x_T\rho(a)^{|T|}\right).
\]

All powers of \(\rho(a)\) commute.  Inclusion--exclusion inside the matrix
algebra gives

\[
I-\sum_{T\ne\varnothing}(-1)^{|T|+1}x_T\rho(a)^{|T|}
=\prod_{p\in P}(I-x_p\rho(a)).
\]

Taking determinants proves (P.2), and Theorem 2 extends it over the gauge
orbit.

For two atoms, let \(u\) denote the refinement value.  The formula
\(u=a^2q_2\) yields \(q_2=a^{-2}u\).  Substitution into the other four types
gives (P.3).  The reverse substitution constructs the required \(q_2\), so
the condition is exact. ∎

### Theorem 5 — the frozen \(S_3\) cocycle is genuinely non-one-letter

Let \(r=(12)\), \(t=(23)\), and assign \(r\) to strict refinements, \(t\) to
strict coarsenings, and \(e\) otherwise.  This cocycle is functorial under the
source lock and is not gauge equivalent, even by a non-natural gauge on the
two-atom graph, to any one-letter counting reference.

#### Proof

The rule depends only on whether
\((u,w)=(0,>0)\), \((>0,0)\), or neither, so Theorem 3 gives functoriality.
Assume it is gauge equivalent to \(a^{|T|}\).  On the singleton loop
\(p\to p\), the candidate holonomy is \(e\), while the reference holonomy is
\(a\).  Loop holonomy is preserved up to conjugacy, hence \(a=e\).  The
reference holonomy of every closed word is then \(e\).  The candidate
two-cycle \(p\to pq\to p\) has holonomy \(rt\), a nonidentity 3-cycle.  This
contradicts Theorem 2.

For genuine noncommutativity, pass to three atoms.  The based closed words
\[
p\to\{p,q\}\to p
\quad\text{and}\quad
p\to\{p,q\}\to\{p,q,\ell\}\to p
\]
have ordered holonomies \(rt\) and \(rrt=t\).  In \(S_3\), \(rt\) and \(t\)
do not commute. ∎

### Theorem 6 — exact two-atom character leakage

For the cocycle in Theorem 5,

\[
D_{\mathbf1}(x,y)=D_{\mathrm{sgn}}(x,y)=(1-x)(1-y),
\tag{P.4}
\]

while

\[
D_{\mathrm{std}}(x,y)
=(1-x)^2(1-y)^2
+3xy(x+y)(xy+1)(x+y-1).
\tag{P.5}
\]

Relative to the identity reference,

\[
[x^2y]\Delta\log D=-3,\qquad
[xy^2]\Delta\log D=-3,\qquad
[x^2y^2]\Delta\log D=-6.
\tag{P.6}
\]

#### Proof

Order the states as \(p,q,pq\), whose arrival weights are \(x,y,-xy\).
The trivial block has identical rows and Theorem 1 gives the first equality
in (P.4).  In the sign representation both \(r\) and \(t\) act by (-1).
The exact \(3\times3\) determinant is again \((1-x)(1-y)\).

For the standard representation use

\[
R=\begin{pmatrix}-1&1\\0&1\end{pmatrix},\qquad
T=\begin{pmatrix}1&0\\1&-1\end{pmatrix}.
\]

Then \(R^2=T^2=I\), \((RT)^3=I\), and

\[
B_{\mathrm{std}}=
\begin{pmatrix}
xI&yI&-xyR\\
xI&yI&-xyR\\
xT&yT&-xyI
\end{pmatrix}.
\]

Expansion of the exact \(6\times6\) determinant and collection relative to
\((1-x)^2(1-y)^2\) gives the factored remainder in (P.5).  This is a finite
polynomial identity, so direct multiplication verifies it coefficient by
coefficient.  Expanding

\[
\log\frac{D_{\mathrm{std}}}{(1-x)^2(1-y)^2}
\]

as a formal power series through total degree four gives (P.6). ∎

### Theorem 7 — cycle-separated character leakage

Let \(\gamma\) be a primitive directed cycle whose cyclic word is isolated by
its marker, either because its edge multiset has a unique connected cyclic
traversal or because a phase-lift/cyclic-word marker is used.  If
\(H_\alpha(\gamma)\) is not conjugate to the reference holonomy
\(H_0(\gamma)\), then some irreducible block has a different first-traversal
coefficient.  If \(H_0(\gamma)=e\) and
\(H_\alpha(\gamma)\ne e\), the coefficient differs from \(d_\rho\) for some
irreducible \(\rho\).

#### Proof

Attach an edge marker \(y_{S,T}\).  The formal trace-log identity is

\[
\log\det(I-B_\rho)
=-\sum_{n\ge1}\frac{\operatorname{tr}(B_\rho^n)}n.
\]

If \(\gamma\) has primitive length \(\ell\), its \(\ell\) cyclic starting
positions contribute the same scalar marker and conjugate holonomies to
\(\operatorname{tr}(B_\rho^\ell)\).  Division by \(\ell\) leaves the
first-traversal coefficient

\[
-\chi_\rho(H_\alpha(\gamma))w(\gamma)y_\gamma.
\]

The isolation hypothesis prevents another connected primitive word from
being aggregated into this marker.  Irreducible characters form a basis of
the class functions on a finite group and therefore separate conjugacy
classes.  Nonconjugate candidate and reference holonomies differ in at least
one irreducible character.

When the reference is \(e\), suppose every irreducible character had value
\(d_\rho\) at \(H_\alpha(\gamma)\).  In a unitary finite-order matrix, trace
equal to dimension forces every eigenvalue to equal one.  Thus every
irreducible representation would kill the holonomy.  Their direct sum in the
regular representation is faithful, forcing the holonomy to be \(e\), a
contradiction. ∎

### Corollary 7.1 — the explicit commutator gap

The primitive cycle \(\gamma_\square=[p,pq,q,pq]\) has holonomy
\(rtrt=(rt)^2\ne e\), scalar weight \(x^3y^3\), and an edge multiset with a
unique connected cyclic traversal.  In the standard representation its
isolated coefficient differs from the identity reference by magnitude three.

#### Proof

The four edge values are \(r,t,r,t\), so the holonomy is the nonidentity
3-cycle \((rt)^2\).  The standard character is (-1) on this class and (2)
at the identity.  Their difference has magnitude three.  The alternative
pairing of the four edges splits into the two disjoint cycles
\([p,pq]\) and \([q,pq]\), so it is not a competing connected traversal. ∎

### Theorem 8 — trace-class realization in the honest half-plane

Let

\[
q_S(s)=\eta_Se^{-sT(S)/2},\qquad \eta_S^2=\varepsilon(S),
\]

and

\[
K_\rho(s)_{S,T}=q_S(s)\rho(\alpha(S,T))q_T(s)
\]

on \(\ell^2(\mathcal E_\infty)\otimes V_\rho\).  If
\(\operatorname{Re}s>2\), then \(K_\rho(s)\) is trace class,

\[
\|K_\rho(s)\|_1
\le d_\rho\left(
\prod_p(1+p^{-\operatorname{Re}s/2})-1
\right)^2,
\tag{P.7}
\]

finite cutoffs converge in trace norm, and their determinants converge
locally uniformly.  For finite \(P\),
\(\det(I-K_{\rho,P})=D_{\rho,P}\).

#### Proof

For \(\sigma=\operatorname{Re}s>2\),

\[
\sum_{S\in\mathcal E_\infty}|q_S(s)|
=\sum_{\varnothing\ne S\subset_{\mathrm{fin}}\mathbb P}
\prod_{p\in S}p^{-\sigma/2}
=\prod_p(1+p^{-\sigma/2})-1<\infty.
\]

The last product converges because
\(\sum_pp^{-\sigma/2}<\infty\).  Decompose every block entry into rank-one
matrix units.  Since \(\rho(\alpha(S,T))\) is unitary, its trace norm is
\(d_\rho\).  Summing the entrywise nuclear norms gives (P.7).

Let \(\Pi_N\) project onto subsets of the first \(N\) primes.  If
\(L=\sum_S|q_S|\) and \(L_N=\sum_{S\subseteq P_N}|q_S|\), then

\[
\|K_\rho-\Pi_NK_\rho\Pi_N\|_1
\le d_\rho(L^2-L_N^2)\longrightarrow0.
\]

Trace-norm continuity of Fredholm determinants gives local uniform
convergence on closed half-planes \(\sigma\ge2+\delta\).

For finite \(P\), write \(Q=\operatorname{diag}(q_S)\) and
\(A_\rho(S,T)=\rho(\alpha(S,T))\).  Then \(K=QA_\rho Q\) and the arrival
matrix is \(A_\rho Q^2\).  Sylvester's identity
\(\det(I-UV)=\det(I-VU)\), with \(U=Q A_\rho\) and \(V=Q\), proves the finite
determinant equality. ∎

### Corollary 9 — source-locked arithmetic selectivity no-go

Every algebraic identity and every leakage coefficient above persists under
arbitrary substitution of the independent atom variables.  The frozen
transition mechanism therefore cannot distinguish prime atoms from shuffled,
composite, random, rational, or formal controls.

#### Proof

The incidence table uses only set inclusion and the cardinalities of the
three incidence regions.  The determinant proofs take place over the free
commutative polynomial ring in the variables \(x_p\).  Replacing those
variables by any matched inventory is a ring homomorphism and preserves every
polynomial identity and inequality of coefficients.  Since neither the
cocycle nor the grammar tests arithmetic properties of a substituted atom,
the transition mechanism has zero symbolic control margin. ∎

## Finite enumeration evidence

The exact searches over all two-atom incidence tables returned:

| group | tables | weak clean | all-irrep clean | count/gauge clean | nongauge clean |
|---|---:|---:|---:|---:|---:|
| \(S_3\) | (7{,}776) | sign: (972) | (36) | (36) | (0) |
| \(D_4\) | (32{,}768) | not promoted | (64) | (64) | (0) |
| \(Q_8\) | (32{,}768) | all 1D: (512) | (64) | (64) | (0) |

These data support, but do not prove, the conjecture that all-irrep
cleanliness forces (P.3) in the restricted two-atom grammar.  The general
statement is kept open because character spectra are not complete switching
invariants in larger gain graphs and finite-group SFT extensions.

## Corrections or missing assumptions

- “Edge variables isolate a cycle” requires the unique connected traversal
  condition or a stronger cyclic-word marker.  The theorem includes that
  condition explicitly.
- “All-irrep clean implies coboundary” is weakened to exact finite evidence
  plus a conjecture.
- The infinite nontrivial block is claimed trace class only on
  \(\operatorname{Re}s>2\).  No interpolation into the strip
  \(1<\operatorname{Re}s\le2\) is used.

## Open risks

- A larger incidence grammar may contain nongauge cocycles with identical
  unmarked character determinants.
- Three- and four-atom low-degree cleanliness is not a global classification.
- The trace-class half-plane is far from the critical strip and carries no
  continuation theorem.
- The inventory-blind no-go can be escaped only by changing the intrinsic
  allowed-word grammar or adding data outside this source lock.
