# SOURCE LOCK — SD-C20

**Title:** *Transition Holonomy on the Tensor-Subset Shift:
Noncommutative Artin Blocks and an Arithmetic Selectivity No-Go*
**Freeze date:** 2026-08-14
**Primary family:** Symbolic Dynamics
**Status:** frozen construction-plus-obstruction candidate

## 1. Tensor source and base shift

Let

\[
\mathcal M=\{F_n:n\ge1\},\qquad
F_m\otimes F_n=F_{mn},\qquad h(F_n)=\log n.
\]

The tensor-indecomposable objects are \(F_p\).  For a finite atom set \(P\),
put

\[
\mathcal E_P=2^P\setminus\{\varnothing\},\qquad
X_P=\mathcal E_P^{\mathbb Z},
\]

with the full shift.  Attach independent commuting variables \(x_p\) and
define

\[
x_S=\prod_{p\in S}x_p,\qquad
\varepsilon(S)=(-1)^{|S|+1},\qquad
w_s(S)=\varepsilon(S)e^{-sT(S)},
\]

\[
T(S)=\sum_{p\in S}\log p.
\]

The construction is first defined over the free commutative polynomial
ring.  Arithmetic specialization is \(x_p=p^{-s}\).  No Riemann-zero data,
prime-indexed group label, von Mangoldt table, fitted phase, or post-hoc
adjacency rule is allowed.

## 2. Same-object edge presentation and cocycle

Use the two-block presentation of the same full shift: vertices are
\(\mathcal E_P\), and every ordered pair \((S,T)\) is an allowed directed
edge.  Let \(G\) be a fixed finite group and

\[
\alpha_P:\mathcal E_P\times\mathcal E_P\longrightarrow G
\]

be a one-step edge cocycle.  The skew product convention is

\[
\widetilde\sigma_\alpha(x,g)
=\bigl(\sigma x,g\alpha_P(x_0,x_1)\bigr).
\]

Left fiber translations commute with this right-cocycle skew shift and do
not alter atom labels, scalar weights, or roofs.  Thus the finite-group
fiber is a genuine deck symmetry of one symbolic object.

## 3. Twisted transfer and determinant

For an irreducible unitary representation
\(\rho:G\to U(V_\rho)\), \(d_\rho=\dim V_\rho\), define the arrival matrix

\[
B_{\rho,P}(s)_{S,T}
=w_s(T)\rho\bigl(\alpha_P(S,T)\bigr),
\qquad
D_{\rho,P}(s)=\det(I-B_{\rho,P}(s)).
\]

The right regular block has the same-object factorization

\[
D_{\mathrm{reg},P}
=\prod_{\rho\in\widehat G}D_{\rho,P}^{d_\rho}.
\]

The trivial block is independent of the cocycle:

\[
D_{\mathbf1,P}
=1-\sum_{\varnothing\ne T\subseteq P}\varepsilon(T)x_T
=\prod_{p\in P}(1-x_p).
\]

At \(x_p=p^{-s}\), finite cutoffs therefore retain the scalar Euler factor.
This identity is universal over atom inventories and is not by itself an
arithmetic selection theorem.

## 4. Gauge, holonomy, and determinant boundary

For \(b_P:\mathcal E_P\to G\),

\[
\alpha_P^b(S,T)=b_P(S)^{-1}\alpha_P(S,T)b_P(T).
\]

The twisted matrices are block-diagonally conjugate, so every
\(D_{\rho,P}\) is gauge invariant.  For a closed directed word
\(\gamma=(S_0,\ldots,S_{n-1},S_0)\), freeze

\[
H_\alpha(\gamma)
=\alpha(S_0,S_1)\cdots\alpha(S_{n-1},S_0).
\]

Gauge changes \(H_\alpha(\gamma)\) by conjugation at \(S_0\).  A spanning-tree
test using formal inverse darts decides gauge equivalence.  All fundamental
based holonomies must agree through one simultaneous root conjugator.

Character determinants aggregate periodic words and are not declared to be
complete gauge invariants.  Equal character determinants do not imply
cohomology without an additional restricted theorem or an edge/group-ring
refinement.

## 5. Functorial incidence grammar

The target group carries no atom action.  Relabeling naturality, restriction
compatibility, one-step locality, and the ban on numeric atom data force

\[
\alpha_P(S,T)=g_{u,v,w},\qquad
u=|S\setminus T|,\quad v=|S\cap T|,\quad w=|T\setminus S|.
\]

For \(|P|=n\), the exact number of stable incidence types is

\[
N(n)=\binom{n+3}{3}-(2n+1),
\]

so \(N(1),N(2),N(3),N(4)=1,5,13,26\).  This classifies the
allowed local data; it does not force those data to be cohomologous to a
one-letter clock.

A natural gauge has \(b_P(S)=q_{|S|}\).  The natural gauge orbit of the
one-letter reference

\[
\alpha_a(S,T)=a^{|T|}
\]

is

\[
g_{u,v,w}=q_{u+v}^{-1}a^{v+w}q_{v+w},
\]

and its character determinants factor as

\[
D_{\rho,P}=\prod_{p\in P}\det(I-x_p\rho(a)).
\]

For \(P=\{p,q\}\), write the five values as
\((a,c,h,u,v)\) for singleton loop, pair loop, disjoint singletons,
refinement, and coarsening.  With \(q_1=e\), membership in the natural
counting gauge orbit is exactly

\[
h=a,\qquad v=u^{-1}a^3,\qquad c=u^{-1}a^2u.
\]

## 6. Frozen nonabelian candidate

Let \(G=S_3\), \(r=(12)\), and \(t=(23)\).  Freeze

\[
\alpha(S,T)=
\begin{cases}
r,&S\subsetneq T,\\
t,&T\subsetneq S,\\
e,&\text{otherwise}.
\end{cases}
\]

This rule is intrinsic to subset incidence, relabeling-natural,
restriction-compatible, and genuinely transition-dependent.  On two atoms
its tuple is \((e,e,e,r,t)\), so it is outside the natural count+coboundary
class.  It is not gauge equivalent to any one-letter reference: singleton
loops force the reference element to be \(e\), whereas the closed word
\([p,pq]\) has holonomy \(rt\ne e\).

The primitive four-cycle

\[
\gamma_\square=[p,pq,q,pq]
\]

has holonomy

\[
H(\gamma_\square)=rtrt=(rt)^2=[r,t]\ne e
\]

and scalar weight \(x^3y^3\).  It is primitive, not a temporal repetition.
Its four directed edges have a unique connected cyclic traversal, so its
edge monomial separates the commutator contribution.

The holonomy image is genuinely noncommutative, not merely a cyclic subgroup
containing a commutator value.  On three atoms, the two based closed words
\[
p\to\{p,q\}\to p,\qquad
p\to\{p,q\}\to\{p,q,\ell\}\to p
\]
have holonomies \(rt\) and \(rrt=t\), respectively, and these elements do
not commute.

## 7. Exact two-atom blocks

For \(x=x_p\), \(y=x_q\), the trivial and sign factors are

\[
D_{\mathbf1}(x,y)=D_{\mathrm{sgn}}(x,y)=(1-x)(1-y).
\]

For the standard representation,

\[
\rho(r)=\begin{pmatrix}-1&1\\0&1\end{pmatrix},\qquad
\rho(t)=\begin{pmatrix}1&0\\1&-1\end{pmatrix},
\]

and

\[
D_{\mathrm{std}}(x,y)
=(1-x)^2(1-y)^2
+3xy(x+y)(xy+1)(x+y-1).
\]

Relative to the identity/counting reference,

\[
[x^2y]\,\Delta\log D=-3,\qquad
[xy^2]\,\Delta\log D=-3,\qquad
[x^2y^2]\,\Delta\log D=-6.
\]

The edge-separated commutator cycle has standard-character gap (3): the
character is (-1) on its 3-cycle holonomy and (2) at the identity.  The
unmarked coefficient \([x^3y^3]\Delta\log D=-9\) aggregates other cycles and
repetitions and must not be identified with this isolated value.  The full
total-degree-four ledger also contains
\([x^3y]\Delta\log D=[xy^3]\Delta\log D=-3\).

## 8. Primitive/repetition convention

Primitive closed words are quotiented by cyclic rotation only, never by
reflection.  For primitive \(\gamma\),

\[
w(\gamma)=\prod_jw(S_{j+1}),\qquad
H(\gamma)=\prod_j\alpha(S_j,S_{j+1}).
\]

The formal determinant expansion is

\[
D_{\rho,P}
=\prod_{[\gamma]\ \mathrm{primitive}}
\det\bigl(I-w(\gamma)\rho(H(\gamma))\bigr).
\]

The \(m\)-fold traversal uses \(w(\gamma)^m\) and \(H(\gamma)^m\).  Scalar
Koszul signs remain ordinary coefficients and are not reinterpreted as a
supertrace.

## 9. Function space and analytic boundary

Choose \(q_S(s)=\eta_Se^{-sT(S)/2}\),
\(\eta_S^2=\varepsilon(S)\), and set

\[
K_{\rho,P}(s)_{S,T}
=q_S(s)\rho(\alpha_P(S,T))q_T(s).
\]

Sylvester's identity gives

\[
\det(I-K_{\rho,P})=D_{\rho,P}.
\]

On
\(\mathcal H_\rho=\ell^2(\mathcal E_\infty)\otimes V_\rho\), where
\(\mathcal E_\infty\) is the set of all nonempty finite prime subsets,

\[
\sum_S|q_S(s)|
=\prod_p(1+p^{-\operatorname{Re}s/2})-1<\infty
\quad\text{for }\operatorname{Re}s>2.
\]

Therefore \(K_\rho(s)\) is trace class for
\(\operatorname{Re}s>2\), with

\[
\|K_\rho(s)\|_1
\le d_\rho\left(\sum_S|q_S(s)|\right)^2.
\]

Finite atom cutoffs converge in trace norm and their Fredholm determinants
converge locally uniformly in that half-plane.  The trivial rank-one block
is trace class already for \(\operatorname{Re}s>1\).

No general nontrivial-block trace-class claim is made on
\(1<\operatorname{Re}s\le2\).  There is no claimed meromorphic continuation,
Gamma factor, functional equation, Riemann--von Mangoldt law, Weil
compression, or critical-zero realization.

## 10. Evidence and claim firewall

The completed finite enumeration is evidence, not a universal theorem:

| group | all tables | weak clean | all-irrep clean | gauge/count clean | nongauge clean |
|---|---:|---:|---:|---:|---:|
| \(S_3\) | \(6^5=7{,}776\) | sign: (972) | (36) | (36) | (0) |
| \(D_4\) | \(8^5=32{,}768\) | not promoted | (64) | (64) | (0) |
| \(Q_8\) | \(8^5=32{,}768\) | all 1D: (512) | (64) | (64) | (0) |

These counts support a two-atom rigidity conjecture.  They do not prove that
all finite groups, larger inventories, or arbitrary gain graphs are rigid.
Known equal-zeta and cospectral examples prohibit a determinant-classifies-
cohomology claim.

Allowed evidence includes exact finite-group arithmetic, symbolic
determinants, character tables, primitive ledgers, trace-norm bounds, and
formal/composite/shuffled/random inventory controls.  Riemann zeros,
parameter fitting, geometric carriers, and Route-B operators are forbidden.

## 11. Frozen route decision

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

GO_GENUINE_TRANSITION_HOLONOMY
GO_SAME_OBJECT_ARTIN_BLOCKS
GO_TRIVIAL_EULER_FACTOR
GO_TRACE_CLASS_RE_GT_2

STOP_NONABELIAN_CLEAN_FACTOR
STOP_DETERMINANT_IMPLIES_COHOMOLOGY
STOP_ONE_DIMENSIONAL_CHARACTER_AUDIT
STOP_ROBUST_NO_LEAK
STOP_ARITHMETIC_SELECTIVITY
PROVES_TOO_MUCH

ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

A0 credits the tensor-factorization/entropy source but not the inventory-
blind transition rule.  A1 credits exact primitive holonomy but records the
absence of a prime/prime-power bijection.  A2 credits the genuine same-object
finite determinants and the honest trace-class realization on
\(\operatorname{Re}s>2\).  A3 and A4 fail.  Route B is not invoked.

## 12. Scope firewall

The paper remains entirely inside Symbolic Dynamics: full shifts, edge
cocycles, skew products, primitive cycles, symbolic cohomology, transfer
operators, and Fredholm determinants.  Voltage/gain terminology is used only
for the finite edge presentation.

Geometric flat bundles, quantum graphs, Hamiltonian or scattering systems,
and self-adjoint operators may appear only in `ROUND2_CLUES.md`.  Altering the
base grammar, cocycle locality, function space, determinant convention, or
allowed-word language creates a new candidate.
