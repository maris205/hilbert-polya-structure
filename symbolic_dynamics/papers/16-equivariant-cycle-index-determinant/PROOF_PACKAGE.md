# PROOF PACKAGE — SD-C18

## Claim

For the frozen Koszul-subset one-vertex shift, a canonical
\(C_2\)-colored Burnside/species ledger retains nonzero primitive-cycle
character data erased by scalar dimension.  In the canonical rank-one and
diagonal realizations studied here, that data cannot simultaneously define a
fixed arithmetic character fiber, preserve the pure Euler trace-log, and
obey the standard Fredholm power ledger.

## Status

`PROVABLE AS STATED`, with the explicit restriction to the canonical
rank-one and diagonal lifts and the isolated squarefree residual.  A universal
no-go for every conceivable equivariant symbolic extension is **not**
justified and is not claimed.

## Assumptions

- \(P\) is a finite label set, \(|P|=n\ge2\).
- \(E(P)=2^P\setminus\{\varnothing\}\).
- \(x_p\) are independent commuting variables and
  \(x_S=\prod_{p\in S}x_p\).
- \(\epsilon(S)=(-1)^{|S|+1}\).
- Cyclic words are quotiented by rotation, not reflection.
- Temporal repetition uses powers of the full scalar edge weight.
- \(S_P\) acts by relabeling subset edges and variables.
- Character readouts are linear on the isolated multigraded coefficient
  under consideration.

## Notation

\[
 b_P(x)=\sum_{S\ne\varnothing}\epsilon(S)x_S
       =1-\prod_{p\in P}(1-x_p).
\]

Let \(V_P=\mathbb C[E(P)]\),
\(u_P=\sum_Se_S\), \(\ell_x(e_S)=\epsilon(S)x_S\), and
\(A_x=u_P\otimes\ell_x\).  Let \(D_xe_S=x_Se_S\).  Write \(\tau\) for the
nontrivial one-dimensional \(C_2\) character.

## Proof strategy

The proof separates four data types.  First, unique primitive-root
decomposition produces a Burnside/species cycle ledger.  Second, the
\(pqr\) coefficient is computed before scalar dimension, revealing a nonzero
virtual \(S_3\)-class.  Third, fixed-fiber commutation is checked directly for
the rank-one transfer.  Fourth, standard diagonal power traces and Schatten
norms are calculated exactly.  The incompatibility theorem follows because
each proposed readout loses a different required datum.

## Dependency map

1. Theorem 1 establishes the scalar rank-one trace and determinant.
2. Theorem 2 constructs the squarefree primitive cycle ledger and its
   \(C_2\) power carrier.
3. Theorem 3 computes the first nonzero Burnside and representation residual.
4. Proposition 4 proves that higher Adams powers cannot cancel that residual.
5. Theorems 5 and 6 distinguish semilinear covariance from a fixed character
   decomposition.
6. Theorem 7 separates rank-one ghosts from diagonal Adams ghosts and their
   determinants.
7. Theorem 8 turns the \(pqr\) residual into the character-readout
   incompatibility.
8. Theorems 9 and 10 control the finite-to-infinite and Schatten boundaries.
9. Theorem 11 combines these facts into the scoped no-go.

## Proofs

### Theorem 1 — rank-one scalar shadow

For every finite \(P\),

\[
 A_x^r=b_P(x)^{r-1}A_x,\qquad
 \operatorname{tr}A_x^r=b_P(x)^r,
\]

and

\[
 \det(I-A_x)=1-b_P(x)=\prod_{p\in P}(1-x_p).
\]

#### Proof

Since \(A_x(v)=\ell_x(v)u_P\),

\[
 A_x^2(v)=\ell_x(v)\ell_x(u_P)u_P=b_P(x)A_x(v).
\]

Induction gives the power formula.  A rank-one operator \(u\otimes\ell\)
has trace \(\ell(u)\), so
\(\operatorname{tr}A_x^r=b_P^{r-1}\ell_x(u_P)=b_P^r\).  The matrix
determinant lemma yields \(\det(I-u_P\otimes\ell_x)=1-\ell_x(u_P)\).
Finally, finite inclusion--exclusion gives
\(1-b_P=\prod_p(1-x_p)\).  ∎

### Theorem 2 — squarefree primitive cycle ledger

At full squarefree content \(\prod_{p\in P}x_p\), every cyclic word is
primitive and corresponds to a cyclically ordered set partition of \(P\).
The words with \(m\) blocks form an \(S_P\)-set of cardinality

\[
 (m-1)!S(n,m),
\]

and scalar sign \((-1)^{n+m}\).  For \(n\ge2\), the total scalar signed
count is zero.

The sign admits a power-compatible formal lift: color an edge \(S\) by
\(\tau^{|S|+1}\).  Evaluation at the nontrivial element \(c\in C_2\) gives
\(\epsilon(S)\), and the \(r\)-th Adams operation evaluates to
\(\epsilon(S)^r\).

#### Proof

At squarefree content, each label appears once.  The edge subsets in a word
are therefore disjoint and cover \(P\), hence form an ordered set partition.
Quotienting word positions by cyclic rotation gives a cyclic order on the
blocks.  A nontrivial temporal repetition would repeat every label in the
primitive root, contradicting squarefree content; every such cyclic word is
primitive.

There are \(S(n,m)\) set partitions with \(m\) unordered blocks and
\((m-1)!\) cyclic orders on those blocks.  The product of edge signs is

\[
 \prod_{j=1}^m(-1)^{|S_j|+1}=(-1)^{n+m}.
\]

The squarefree mixed coefficient of

\[
 -\log\det(I-A_x)=-\sum_{p\in P}\log(1-x_p)
\]

is zero for \(n\ge2\).  Unique primitive-root regrouping identifies that
coefficient with the signed count just computed.

For the color lift, \(\tau(c)=-1\).  Thus
\(\tau^{|S|+1}(c)=\epsilon(S)\).  Since Adams operations on a character
satisfy \(\psi^r(\chi)(c)=\chi(c^r)\), and for this one-dimensional line
\(\psi^r(\tau)=\tau^r\), evaluation gives
\((-1)^{r(|S|+1)}=\epsilon(S)^r\).  ∎

### Theorem 3 — the \(pqr\) Burnside certificate

For \(P=\{p,q,r\}\), the positive and negative primitive sets are

\[
 C_+=\{[pqr],[p][q][r],[p][r][q]\},
\]

\[
 C_-=\{[p][qr],[q][pr],[r][pq]\}.
\]

Their virtual Burnside class is

\[
 \mathcal R_3=[S_3/S_3]+[S_3/C_3]-[S_3/C_2].
\]

Its marks at \((1,C_2,C_3,S_3)\) are \((0,0,3,1)\).  Under permutation
linearization,

\[
 R_3=\mathbf1\oplus\mathbf{sgn}-\mathbf{Std},
\]

with character \((0,0,3)\) on \((e,(12),(123))\).  In particular,
\(\mathcal R_3\) and \(R_3\) are nonzero although their scalar dimensions
vanish.

#### Proof

The one-block cycle is fixed by \(S_3\), so it is \(S_3/S_3\).  The two
orientations of three singleton blocks are interchanged by a transposition
and fixed as cyclic necklaces by \(C_3\); they form \(S_3/C_3\).  The three
singleton--pair cycles form the natural three-point orbit \(S_3/C_2\).
This proves the Burnside formula.

For subgroup marks, the identity fixes all three positive and all three
negative objects.  A transposition fixes the one-block positive object and
one singleton--pair negative object.  A three-cycle fixes all three positive
objects and no negative object.  The full group fixes only the one-block
positive object.  Subtracting gives \((0,0,3,1)\).

The permutation modules of the three orbits are

\[
 \mathbb C[S_3/S_3]=\mathbf1,\quad
 \mathbb C[S_3/C_3]=\mathbf1\oplus\mathbf{sgn},\quad
 \mathbb C[S_3/C_2]=\mathbf1\oplus\mathbf{Std}.
\]

Their virtual difference is the asserted representation.  The standard
character table gives
\(\chi_{R_3}=(1+1-2,1-1-0,1+1-(-1))=(0,0,3)\).  ∎

### Proposition 4 — Adams isolation of the squarefree residual

No Adams operation \(\psi^r\), \(r>1\), applied to a monomial of integral
nonnegative multidegree can contribute to multidegree \((1,1,1)\).
Consequently the \(pqr\) residual of Theorem 3 has no higher-power
counterterm.

#### Proof

On the multigraded coefficient ring,
\(\psi^r(x_p^{a_p}x_q^{a_q}x_r^{a_r})
=x_p^{ra_p}x_q^{ra_q}x_r^{ra_r}\).  Equality with multidegree
\((1,1,1)\) would require \(ra_p=ra_q=ra_r=1\), impossible for integral
\(a_i\ge0\) and \(r>1\).  ∎

### Theorem 5 — semilinear covariance and stabilizer

Let \(\rho(g)e_S=e_{gS}\).  Then

\[
 \rho(g)A_x\rho(g)^{-1}=A_{g\cdot x}.
\]

Moreover, \([A_x,\rho(g)]=0\) if and only if \(x_{gp}=x_p\) for every
\(p\in P\).  Under \(x_p=p^{-s}\) and \(\operatorname{Re}s>0\), the
stabilizer of the fixed operator is trivial.

#### Proof

The vector \(u_P\) is invariant.  Conjugation therefore changes only the
covector:

\[
 (\ell_x\rho(g)^{-1})(e_S)
 =\epsilon(S)x_{g^{-1}S}
 =\ell_{g\cdot x}(e_S),
\]

which gives covariance.  Commutation is equivalent to invariance of
\(\ell_x\), hence to \(x_{gS}=x_S\) for every nonempty \(S\).  Singleton
subsets make this equivalent to \(x_{gp}=x_p\) for every \(p\); the converse
follows multiplicatively.

For distinct rational primes and \(\sigma=\operatorname{Re}s>0\),
\(|p^{-s}|=p^{-\sigma}\) are pairwise distinct.  Any stabilizing permutation
fixes every singleton label and is the identity.  ∎

### Theorem 6 — symmetry restoration erases nontrivial modes

If \(x_p=t\) for all \(p\in P\), then \(A_t\) is \(S_P\)-equivariant and
its image is the invariant line \(\mathbb Cu_P\).  Its restriction to every
nontrivial \(S_P\)-isotype is zero, so

\[
 \det(I-A_t\mid V_\lambda)=1
\]

for every nontrivial irreducible type \(\lambda\).  The only nonzero
eigenvalue is

\[
 b_P(t)=1-(1-t)^n.
\]

#### Proof

Equal weights make \(\ell_t\) invariant, hence \(A_t\) equivariant by
Theorem 5.  Its image is contained in \(\mathbb Cu_P\), which is the trivial
representation.  An equivariant map from a nontrivial isotype to a trivial
representation is zero by Schur's lemma, applied on each irreducible
summand.  The rank-one eigenvalue is \(\ell_t(u_P)=b_P(t)\); all remaining
eigenvalues vanish.  ∎

### Theorem 7 — rank-one/diagonal ghost and determinant separation

For \(n\ge2\) and \(r\ge2\),

\[
 [x_1^{r-1}x_2]b_P(x)^r=r,
 \qquad
 [x_1^{r-1}x_2]b_P(x_1^r,\ldots,x_n^r)=0.
\]

The diagonal signed readout satisfies

\[
 \operatorname{str}D_x^r=b_P(x_1^r,\ldots,x_n^r)
\]

and

\[
 \operatorname{sdet}(I-D_x)
 =\prod_{S\ne\varnothing}(1-x_S)^{\epsilon(S)}.
\]

For every \(n\ge2\), this superdeterminant differs from
\(\prod_{p\in P}(1-x_p)\).

#### Proof

Every monomial of \(b_P\) has total degree at least one.  A monomial of total
degree \(r\) in \(b_P^r\) must therefore choose a degree-one singleton term
from every factor.  The target monomial is obtained by choosing \(x_2\) from
one of the \(r\) factors and \(x_1\) from the other \(r-1\), giving
coefficient \(r\).  Every exponent in \(b_P(x_1^r,\ldots,x_n^r)\) is a
multiple of \(r\), so its target coefficient is zero.

The diagonal power has eigenvalue \(x_S^r\) on \(e_S\).  Taking the signed
trace gives the stated \(b_P(x^r)\).  Exponentiating its trace-log yields the
product formula.  With two variables,

\[
 \operatorname{sdet}(I-D_x)
 =\frac{(1-x_1)(1-x_2)}{1-x_1x_2},
\]

which is not \((1-x_1)(1-x_2)\).  For \(n>2\), setting all other variables
to zero reduces equality to the false two-variable identity.  ∎

### Theorem 8 — character-readout incompatibility

Let \(L\) be a linear readout on the squarefree \(S_3\) representation
coefficient, and assume the \(pqr\) coefficient is isolated as in
Proposition 4.  If \(L(R_3)\ne0\), the readout has a nonzero mixed
\(x_px_qx_r\) coefficient in its primitive trace-log.  If the readout agrees
with the pure Euler trace-log

\[
 -\log\prod_{a\in P}(1-x_a)
 =\sum_{a\in P}\sum_{k\ge1}\frac{x_a^k}{k},
\]

then \(L(R_3)=0\).  Thus no such readout both sees the first resolved motion
and preserves the pure Euler trace-log.

#### Proof

By Theorem 3, the primitive coefficient at \(x_px_qx_r\) is exactly
\(R_3\); Proposition 4 excludes higher-power contributions at that
multidegree.  Linearity makes the scalar coefficient \(L(R_3)\).  The pure
Euler trace-log is a sum of one-variable series and contains no mixed
monomial.  Equality with it therefore forces \(L(R_3)=0\).  ∎

### Theorem 9 — formal projectivity and raw-transfer noninductivity

For \(P\subset Q\), setting \(x_q=0\) for all \(q\in Q\setminus P\)
specializes \(b_Q\) to \(b_P\) and deletes all edges containing new labels.
These maps define a formal projective multigraded ledger.

Under the canonical isometric edge embedding
\(i_{P,Q}:V_P\to V_Q\), the rank-one transfers do not intertwine when
\(P\subsetneq Q\):

\[
 A_Qi_{P,Q}\ne i_{P,Q}A_P.
\]

Furthermore,

\[
 \|A_x\|=\sqrt{2^{|P|}-1}
 \left(\sum_{S\in E(P)}|x_S|^2\right)^{1/2},
\]

so the prime-weighted raw transfers have no bounded inductive limit along
these embeddings.

#### Proof

Every monomial indexed by an edge meeting \(Q\setminus P\) vanishes under
zero-specialization, while all old monomials remain unchanged.  This proves
projectivity.

For \(T\in E(P)\),

\[
 A_Qi(e_T)=\epsilon(T)x_Tu_Q,
 \qquad
 iA_P(e_T)=\epsilon(T)x_Ti(u_P).
\]

The vectors differ because \(u_Q\) contains new subset edges.  The norm
formula follows from the rank-one identity
\(\|u\otimes\ell\|=\|u\|\|\ell\|\), with
\(\|u_P\|^2=2^{|P|}-1\).  For prime weights with any fixed
\(\operatorname{Re}s>0\), the second factor is bounded below by the modulus
of the first singleton weight, while the first factor diverges.  ∎

### Theorem 10 — Schatten boundary for the diagonal prime-subset operator

Let \(\mathcal P\) be the rational primes, let
\(\mathcal H=\ell^2(E(\mathcal P))\), and define

\[
 D_se_S=\left(\prod_{p\in S}p^{-s}\right)e_S,
 \qquad \sigma=\operatorname{Re}s>0.
\]

For every \(q\ge1\),

\[
 D_s\in\mathcal S_q
 \quad\Longleftrightarrow\quad q\sigma>1,
\]

and

\[
 \|D_s\|_{\mathcal S_q}^q
 =\prod_p(1+p^{-q\sigma})-1.
\]

#### Proof

The operator is diagonal, so the \(q\)-th power sum of its singular values is

\[
 \sum_{S\ne\varnothing}\prod_{p\in S}p^{-q\sigma}.
\]

Monotone convergence over finite prime sets gives the Euler product in the
statement.  For nonnegative \(a_p=p^{-q\sigma}\), the product
\(\prod_p(1+a_p)\) is finite exactly when \(\sum_pa_p\) is finite: use
\(\log(1+a_p)\le a_p\) for sufficiency and
\(\log(1+a_p)\ge a_p/2\) for all sufficiently large \(p\) for necessity.
The prime Dirichlet series \(\sum_pp^{-\alpha}\) converges exactly for
\(\alpha>1\).  Substituting \(\alpha=q\sigma\) proves the criterion.  ∎

### Theorem 11 — scoped character-Fredholm no-go

Within SD-C18 and the canonical rank-one and diagonal lifts defined above,
the following cannot hold simultaneously:

1. the pure Euler trace-log and determinant are preserved;
2. a fixed arithmetically specialized operator admits a nontrivial
   \(S_P\)-character fiber;
3. a character readout detects the \(pqr\) residual;
4. temporal powers are represented by the standard operator trace or
   supertrace ledger;
5. the finite objects assemble into the canonical bounded raw edge-state
   inductive limit.

#### Proof

Distinct arithmetic weights violate item 2 by Theorem 5.  Equal weights
restore item 2 only by making every nontrivial rank-one mode determinant one,
by Theorem 6.  A diagonal representation-preserving lift obeys standard
Adams ghosts, but Theorem 7 shows that it violates items 1 and 4 relative to
the rank-one Euler shadow.  Theorem 8 proves directly that items 1 and 3 are
incompatible at the isolated \(pqr\) coefficient.  Theorem 9 rules out item
5 for the canonical raw transfers.  Each branch therefore violates at least
one required property.  ∎

## Corrections or missing assumptions

- The no-go is intentionally restricted to the canonical models above.
  Removing that qualifier would make the statement too strong.
- Theorem 8 assumes no same-multidegree counterterm.  Proposition 4 verifies
  this for temporal Adams powers in the frozen squarefree ledger.
- The formal Burnside/species projective family is not an analytic
  \(S_\infty\) Fredholm object.
- The scalar rank-one determinant is valid, but it is a shadow with no
  nontrivial character fibers after arithmetic specialization.

## Open risks

- A genuine finite-group cocycle acting in a fiber independently of the
  arithmetic roof could evade the base-label symmetry obstruction.  That
  would be a new Symbolic Dynamics candidate and requires its own source
  lock.
- A nonstandard completed or regularized equivariant trace could alter the
  diagonal determinant.  Unless it preserves all power traces, it would also
  change the candidate; no such construction is claimed here.
- Nothing in this proof supplies a functional equation, Gamma factor,
  Riemann--von Mangoldt law, Weil compression, or operator lift.
