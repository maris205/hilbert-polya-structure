# Literal proof package and dependency spine

This document is the source-design proof certificate.  It records the
definitions and algebra that the eventual manuscript must expose in the main
text.  “Degree” means a weighted degree of a certified leading form; it is not
a claim about a global dynamical degree.

## 1. Scope, notation, and typed states

Let \(K\) be a field of characteristic zero and \(r\ge3\).  Let
\[
 E_V,E_W\subset\mathbb Z_{\ge2}^{\,r}
\]
be finite, nonempty, collected supports, and write
\[
 V(q)=\sum_{\alpha\in E_V}c_\alpha q^\alpha,\qquad
 W(p)=\sum_{\beta\in E_W}d_\beta p^\beta,\qquad c_\alpha,d_\beta\in K^\times .
\]
The polynomial variables \(q,p\) and the incoming leading tuples are taken in
disjoint blocks.  Degree vectors \(u,w,v\in\mathbb R_{>0}^r\) belong to an
ordered real degree space, independent of \(K\).  For a monomial,
\(\deg_u(q^\alpha)=\alpha\cdot u\).  A weighted seed has positive integer
\(u,w\), together with algebraically independent incoming leading tuples;
disjoint fresh blocks realize any declared integer pair.

Define
\[
 S_V(q,p)=(q,p+\nabla V(q)),\qquad
 T_W(q,p)=(q+\nabla W(p),p),\qquad F=T_W\circ S_V .
\]
For \(\alpha,\beta\) put
\[
 A_\alpha=\mathbf1\alpha^{\mathsf T}-I,\qquad
 B_\beta=\mathbf1\beta^{\mathsf T}-I,\qquad
 \mathbf1=(1,\ldots,1)^{\mathsf T}.
\]
Then \(A_\alpha u=(\alpha\cdot u)\mathbf1-u\), and similarly for
\(B_\beta v\).  Let
\[
 h_V(u)=\max_{\alpha\in E_V}\alpha\cdot u,\qquad
 h_W(v)=\max_{\beta\in E_W}\beta\cdot v .
\]

For a strict edge \(e=(\alpha,\beta)\), \(K_e\) denotes the intersection of
the positive orthant with all declared strict source-selector, source-carry,
target-selector, target-carry, and reflected selector/carry inequalities.  Its
typed positive pair cell is
\[
 C_e^+=\{(u,w):u\in K_e,\;w>0,\;A_\alpha u-w>0\},
\]
where inequalities are componentwise.  The forward pair transition is
\[
 \Phi_e(u,w)=(u',v)=(B_\beta A_\alpha u,A_\alpha u).
\]

Let \(R\) be the permutation matrix reversing coordinates,
\(R(x_1,\ldots,x_r)=(x_r,\ldots,x_1)\), and define
\[
 R_{\rm state}(u,w)=(Rw,Ru).
\]
The reflected inverse edge is an additional certificate: it must have the
labels \(R\alpha\) and \(R\beta\) available in the appropriate supports, or
must explicitly state the induced action on the observed span.  A finite
normal fan alone is not a universal target automaton; all target inclusions
used below are printed edge certificates.

For an edge, let
\[
 C_e^{\mathbb Z}=C_e^+\cap(\mathbb Z_{>0}^r)^2,\qquad
 U_e=\operatorname{span}_{\mathbb R}\{u:(u,w)\in C_e^{\mathbb Z}\},
\]
\[
 V_e=\operatorname{span}_{\mathbb R}\{A_\alpha u:(u,w)\in C_e^{\mathbb Z}\}.
\]
These spans are hypotheses of the reciprocity statement, not automatic
properties of an arbitrary cell.

## 2. Symplectic maps and inverse order

The Jacobians are
\[
 DS_V=\begin{pmatrix}I&0\\ \operatorname{Hess}V&I\end{pmatrix},\qquad
 DT_W=\begin{pmatrix}I&\operatorname{Hess}W\\0&I\end{pmatrix}.
\]
The Hessians are symmetric, so direct multiplication with
\(J=\begin{psmallmatrix}0&I\\-I&0\end{psmallmatrix}\) gives
\(DS_V^{\mathsf T}JDS_V=J\) and \(DT_W^{\mathsf T}JDT_W=J\).  Thus
\(S_V,T_W,F\) are polynomial symplectomorphisms.  Their inverses are
\[
 S_V^{-1}(q,p)=(q,p-\nabla V(q)),\qquad
 T_W^{-1}(q,p)=(q-\nabla W(p),p),
\]
and therefore
\[
 F^{-1}=S_V^{-1}\circ T_W^{-1}.
\]
The inverse phase order is W first and V second.  The subtraction signs are
nonzero scalar signs and do not change a strict fresh leading degree once the
survival lemma below has been applied.

## 3. Degree transport on a strict edge

Suppose the V selector at \(u\) is the unique \(\alpha\), and the W selector
at the fresh V degree is the unique \(\beta\).  Every component of
\(\nabla V\) has fresh weighted degree represented by \(A_\alpha u\).  The
first strict carry
\[
 A_\alpha u-w>0
\]
keeps this fresh block above the old \(p\)-block.  The W gradient then has
degree \(B_\beta A_\alpha u\), and
\[
 B_\beta A_\alpha u-u>0
\]
keeps it above the old \(q\)-block.  Hence a certified forward step is
\[
 (u,w)\longmapsto (u',v)=(B_\beta A_\alpha u,A_\alpha u).
\tag{3.1}
\]
The same bookkeeping in \(F^{-1}\), starting at \(R_{\rm state}(u,w)\), uses
the reflected W label first and the reflected V label second.  Ties at the
exposed maximum, a nonpositive carry, an empty lattice cell, or an
uncertified face is a terminal/out-of-scope branch, not an implicit equality.

## 4. Grouped positive-face Hessian certificate

Let \(E_0\subseteq E_V\) (or \(E_W\)) be an exposed face and
\[
 P_{E_0}(X)=\sum_{\alpha\in E_0}c_\alpha X^\alpha .
\]
For \(h_{ij}(\alpha)=\alpha_i(\alpha_j-\delta_{ij})\), grouping the
determinant by row-labelled tuples gives
\[
 \det\operatorname{Hess}P_{E_0}
 =\sum_{(\alpha_1,\ldots,\alpha_r)\in E_0^r}
 \left(\prod_i c_{\alpha_i}\right)
 D(\alpha_1,\ldots,\alpha_r)X^{\sum_i\alpha_i-2\mathbf1},
\]
where \(D=\det[h_{ij}(\alpha_i)]\).  Choose a generic secondary linear
weight on \(E_0\) with a unique minimizer \(\alpha_0\).  The tuple
\((\alpha_0,\ldots,\alpha_0)\) is then the unique lowest secondary-weight
group.  Its matrix is
\[
 [h_{ij}(\alpha_0)]
 =\operatorname{diag}(\alpha_0)
   (\mathbf1\alpha_0^{\mathsf T}-I),
\]
so the matrix determinant lemma gives
\[
 D(\alpha_0,\ldots,\alpha_0)
 =(-1)^r(1-|\alpha_0|)\prod_i\alpha_{0i}\ne0.
\tag{4.1}
\]
The corresponding coefficient is
\(c_{\alpha_0}^{\,r}(-1)^r(1-|\alpha_0|)\prod_i\alpha_{0i}\), nonzero
because \(K\) has characteristic zero and every coordinate of
\(\alpha_0\) is at least two.  Thus the grouped determinant is nonzero for
every nonzero coefficient choice in the headline class.  The argument is
valid for a one-point face and for a tied face; it is an auxiliary wall
certificate and does not select a tied vertex by itself.

## 5. Jacobian independence and all-phase survival

In characteristic zero, a nonzero Jacobian determinant of a polynomial tuple
implies algebraic independence by the Jacobian criterion.  Applying this to
\(\nabla P_{E_0}\) and (4.1) shows that the face-gradient components are
algebraically independent.  If \(Z_1,\ldots,Z_r\) are independent incoming
leading forms, substitution \(X_i\mapsto Z_i\) is injective on the polynomial
algebra generated by the face tuple.  Therefore a selected face gradient
cannot vanish through a hidden coefficient cancellation after substitution.

For a strict singleton, the same fact is visible directly from
\[
 \det A_\alpha=(-1)^r(1-|\alpha|)\ne0.
\]
At each forward half-step, strict carries separate a fresh gradient block from
the carried old block.  Algebraic independence prevents cancellation within
the fresh block, and the strict inequality prevents cancellation with the old
block.  The inverse induction is identical: subtraction multiplies a fresh
block by \(-1\), a nonzero scalar in \(K\).  This proves simultaneous forward
and reflected-inverse leading-form visibility on every edge whose selector,
carry, target, and reflected certificates are printed.

## 6. Exact all-ones translation

For a strict edge, write \(s=\alpha\cdot u=h_V(u)\).  Then
\[
 v=A_\alpha u=s\mathbf1-u=h_V(u)\mathbf1-u .
\]
Since \(\beta\cdot A_\alpha u=|\beta|s-\beta\cdot u\),
\[
\begin{aligned}
 u'&=B_\beta v=(\beta\cdot v)\mathbf1-v\\
 &=u+\bigl((|\beta|-1)\alpha-\beta\bigr)\cdot u\;\mathbf1 .
\end{aligned}
\]
Define
\[
 \delta(u)=h_W(v)-h_V(u)
 =\bigl((|\beta|-1)\alpha-\beta\bigr)\cdot u.
\tag{6.1}
\]
The second carry is exactly \(\delta(u)>0\).  Starting from an integer seed,
all matrices and carries are integral, so a strict branch has integer
\(\delta\ge1\) at every step.  Consequently
\[
 u_n=u_0+t_n\mathbf1,\qquad t_0=0,\qquad t_{n+1}-t_n=\delta(u_n)>0.
\tag{6.2}
\]
This is an actual weighted-degree identity after Section 5, not merely a
formal matrix observation.

## 7. Global wall monotonicity and selector bound

Let
\[
 T_V=\{|\alpha|:\alpha\in E_V\},\quad
 T_W=\{|\beta|:\beta\in E_W\},\quad
 d_V=|T_V|,\quad d_W=|T_W|.
\]
Along \(u(t)=u_0+t\mathbf1\),
\[
 h_V(u(t))=\max_{s\in T_V}(M_s+st),\qquad
 M_s=\max_{|\alpha|=s}\alpha\cdot u_0.
\]
Put
\[
 g(t)=h_V(u(t))-t=\max_{s\in T_V}(M_s+(s-1)t).
\]
All \(s-1>0\), so \(g\) is strictly increasing: for \(t_2>t_1\), an
argmax line at \(t_1\) increases strictly at \(t_2\).  Moreover
\[
 v(t)=h_V(u(t))\mathbf1-u(t)=g(t)\mathbf1-u_0 .
\]
For \(\beta,\eta\in E_W\),
\[
 \beta\cdot v(t)-\eta\cdot v(t)
 =(|\beta|-|\eta|)g(t)-(\beta-\eta)\cdot u_0 .
\tag{7.1}
\]
Thus W selectors form an upper envelope of \(d_W\) lines in the increasing
variable \(g\).  A wall between unequal total degrees is crossed at most
once; a wall between equal total degrees is invariant along the ray.  The V
upper envelope has at most \(d_V-1\) selector changes and the W envelope at
most \(d_W-1\), so the actual strict phase word satisfies
\[
 \#\{\text{selector changes}\}
 \le(d_V-1)+(d_W-1)=d_V+d_W-2.
\tag{7.2}
\]
Discrete steps may skip a wall and only lower this count.  A strict branch
that reaches an exposed tie or a failed carry terminates at that boundary.  An
infinite strict branch has a stationary selector pair after finitely many
changes.  The older \(d_Vd_W-1\) and pair-wall estimates are conservative
historical bounds and are not the headline bound.

## 8. Stationary affine phase tail

On a stationary pair \((\alpha,\beta)\), set
\[
 c=(|\beta|-1)\alpha-\beta .
\]
Then \(c\cdot\mathbf1=(|\alpha|-1)(|\beta|-1)-1\).  Substitution of
\(u_n=u_0+t_n\mathbf1\) into (6.1) gives
\[
 t_{n+1}=\lambda t_n+\mu,\qquad
 \lambda=1+c\cdot\mathbf1=(|\alpha|-1)(|\beta|-1),\qquad
 \mu=c\cdot u_0 .
\tag{8.1}
\]
The origin is global (\(t_0=0\)); it is not reset when a transient selector
changes.  Since all support totals are at least \(2r\ge6\) in the headline
class, in particular \(\lambda>1\).  A phase-local origin gives an equivalent
intercept but must be translated back to (8.1).  No minimal scalar recurrence,
Perron degree, entropy, or higher-dynamical-degree conclusion follows.

## 9. Reflected inverse and observable-span reciprocity

For \(\bar\alpha=R\alpha\) and \(\bar\beta=R\beta\), use
\(R\mathbf1=\mathbf1\), \(R^2=I\), and \(R^{\mathsf T}=R\) to obtain
\[
 B_{\bar\alpha}R
 =(\mathbf1(R\alpha)^{\mathsf T}-I)R
 =\mathbf1\alpha^{\mathsf T}-R
 =RA_\alpha ,
\]
\[
 A_{\bar\beta}R=RB_\beta .
\tag{9.1}
\]
Starting at \(R_{\rm state}(u,w)=(Rw,Ru)\), the reflected inverse uses W
first and V second, and for \(v=A_\alpha u\) gives
\[
 B_{\bar\alpha}Ru=RA_\alpha u=Rv,\qquad
 A_{\bar\beta}Rv=RB_\beta v=Ru' .
\tag{9.2}
\]
If phase-resolved equality holds for every integer seed in \(C_e^{\mathbb Z}\),
the first equality in (9.2) forces the restriction
\(B_{\bar\alpha}R=RA_\alpha\) on \(U_e\), and the second forces
\(A_{\bar\beta}R=RB_\beta\) on \(V_e\).  Conversely, these restrictions on
every edge of the finite seed-indexed word, together with reflected score,
carry, and target certificates, induct on the phase state and imply all-\(n\)
phase-resolved reciprocity.  If \(U_e=V_e=\mathbb R^r\), the restrictions
upgrade to literal full-matrix identities; on a proper span they do not.
Equality of scalar total degrees, or comparison of a non-\(R_{\rm state}\)-
fixed same numerical seed, is insufficient.

## 10. Local one-edge lower-ideal lemma

Fix one strict typed pair core and normalize by the \(\ell^1\)-norm.  Require a
nonempty compact set
\[
 \widehat\Sigma_e^+\subset C_e^+\cap\{\|(u,w)\|_1=1\}
\]
on which every coordinate of \(u,w,A_\alpha u-w\) is at least
\(\varepsilon>0\), and every selected score, carry, target, and reflected
pair gap is at least \(\eta>0\).  Define the four nonempty normalized
projections
\[
 \begin{aligned}
 X^{V,+}&=\pi_u(C_e^+),&
 X^{W,+}&=\{A_\alpha u:(u,w)\in C_e^+\},\\
 X^{W,-}&=\{Ru:(u,w)\in C_e^+\},&
 X^{V,-}&=\{RA_\alpha u:(u,w)\in C_e^+\}.
 \end{aligned}
\]
Let \(\widehat X^{S,\pm}\) be their closures after \(\ell^1\)-normalization
and the coordinate lower bound \(\varepsilon\).  For every retained row
\(\ell\) and lower/new row \(\rho\) in the corresponding section, assume
\[
 \min_{x\in\widehat X^{S,\pm}}(\ell-\rho)\cdot x
 \ge\Delta_{S,\pm}>0 .
\tag{10.1}
\]
For an unnormalized \(x=s\widehat x\), homogeneity gives a gap at least
\(s\Delta_{S,\pm}>0\).  Together with the typed pair margins, (10.1)
preserves the selected leading rows for exactly one forward step and one
reflected inverse step.  The retained rows are
\((\alpha,\beta,R\alpha,R\beta)\), with the selected-minus-new sign
convention.

This lemma does not assert that the image belongs to a second declared core;
that would require an explicit normalized target inclusion.  It does not
assert C1→C2 perturbation stability, multi-edge stability, or all-iterate
stability.  A forward-only margin does not imply the reflected inverse margin.

## 11. Exact asymmetric \(r=3\) fixture

Take
\[
 E_V=\{a_1=(8,2,2),\ a_2=(2,5,6),\ \gamma=(2,8,2)\},\qquad
 E_W=\{b_1=(2,2,8),\ b_2=(6,5,2)\},
\]
with \(b_i=Ra_i\) and \(R\gamma\notin E_W\).  The matrices are
\[
 A_1=\begin{pmatrix}7&2&2\\8&1&2\\8&2&1\end{pmatrix},\quad
 A_2=\begin{pmatrix}1&5&6\\2&4&6\\2&5&5\end{pmatrix},\quad
 A_\gamma=\begin{pmatrix}1&8&2\\2&7&2\\2&8&1\end{pmatrix},
\]
\[
 B_1=\begin{pmatrix}1&2&8\\2&1&8\\2&2&7\end{pmatrix},\quad
 B_2=\begin{pmatrix}5&5&2\\6&4&2\\6&5&1\end{pmatrix}.
\]

Define the strict cones (all displayed forms and all coordinates are \(>0\)):
\[
\begin{aligned}
 K_1:&\quad (6,-3,-4)\cdot u>0,\ (6,-6,0)\cdot u>0,\\
 &\quad(4,-1,8)\cdot u>0,\ (4,5,2)\cdot u>0;\\
 K_2:&\quad (-6,3,4)\cdot u>0,\ (0,-3,4)\cdot u>0,\\
 &\quad(-2,2,12)\cdot u>0,\ (-2,8,6)\cdot u>0 .
\end{aligned}
\]
Set \(C_i^+=\{(u,w):u\in K_i,w>0,A_i u-w>0\}\) and
\(C_i^-=R_{\rm state}(C_i^+)\).  Direct multiplication gives
\[
 C_{21}=B_2A_1=I+\mathbf1(90,19,22),\qquad
 C_{22}=B_2A_2=I+\mathbf1(18,55,70).
\tag{11.1}
\]

For C1→C2, the target selector gaps are
\[
 (a_2-a_1)C_{21}u=(84,22,26)\cdot u,\qquad
 (a_2-\gamma)C_{21}u=(90,16,26)\cdot u,
\]
\[
 (b_2-b_1)A_2C_{21}u=(1078,230,276)\cdot u,\qquad
 (a_2-\gamma)RA_2C_{21}u=(1078,236,270)\cdot u,
\]
and \(A_2C_{21}u-A_1u=\mathbf1(1074,231,268)\cdot u>0\).
For the C2 self-loop, the corresponding forms are
\[
\begin{aligned}
 &(a_2-a_1)C_{22}u=(12,58,74)\cdot u,\quad
 (a_2-\gamma)C_{22}u=(18,52,74)\cdot u,\\
 &(b_2-b_1)A_2C_{22}u=(214,662,852)\cdot u,\\
 &(a_2-\gamma)RA_2C_{22}u=(214,668,846)\cdot u,\\
 &A_2C_{22}u-A_2u=\mathbf1(216,660,840)\cdot u>0,\quad
 C_{22}u-u=\mathbf1(18,55,70)\cdot u>0 .
\end{aligned}
\]
The source W gap and reflected source gap are respectively
\((4,-1,8)\cdot u\) and \((4,5,2)\cdot u\) in C1, and
\((-2,2,12)\cdot u\) and \((-2,8,6)\cdot u\) in C2.  Hence the listed cones
and pair cells certify C1→C2→C2 and the reflected C1−→C2−→C2− path.

The weighted C1 seed \((u,w)=((2,1,1),(1,1,1))\) has V scores
\(20,15,14\), gives \(A_1u=(18,19,19)\) and
\(C_{21}u=(223,222,222)\), and has W gap \(15\).  The ordinary C2 seed
\(((1,1,1),(1,1,1))\) gives \(A_2u=(12,12,12)\) and
\(C_{22}u=(144,144,144)\); it is a stationary baseline, not the transient
witness.  Three independent C1 \(u\)-seeds are
\((2,1,1),(2,1,2),(3,1,1)\); three independent C2 seeds are
\((1,1,1),(1,1,2),(1,2,2)\).  Their determinants are nonzero, and
\(\det A_1,\det A_2\ne0\), so the corresponding \(V_e\) spans are full.

The literal reflected identities on the fixture are
\[
 B_1Ru=RA_1u,\quad A_2B_1Ru=RC_{21}u,\qquad
 B_2Ru=RA_2u,\quad A_2B_2Ru=RC_{22}u.
\]
The support is not globally reflection-closed: at \(u=(1,10,1)\),
\(\gamma\cdot u=84\), while \(a_1\cdot u=30\) and \(a_2\cdot u=58\), and
\(R\gamma\) is absent from \(E_W\).  Thus this is a local reflection-closed
component, not a map-level reversor.

## 12. Failure and boundary fixtures

* If a support coordinate is zero or one, the positive-support determinant
  witness and the fresh all-ones carry can fail.  The planar wall/period-two
  setting is an adjacent excluded boundary, not a limiting theorem here.
* If \(A_\alpha u\le w\) or \(\delta\le0\), the fresh block need not dominate
  the old block and (6.2) is not an actual degree law.
* The cancellation fixture
  \(V=(q_1+q_2+q_3)^3,\ W=(p_1-p_2)^3\) has zero/unit coordinates and
  equal leading V-gradient components.  At the W half-step of \(F^1\), the
  leading \(p_1-p_2\) terms cancel, so the predicted W degree is lost.  This
  is deliberately outside the headline class; it is not mislabeled as a full
  \(n=2\) iterate.
* If a reflected support/action or reflected cell certificate is missing,
  (9.2) gives an \(n=1\) phase-vector mismatch on an open integer seed cell.
* Exposed ties, empty lattice cells, positive characteristic, and proper-span
  complements are excluded.  Inactive submaximal ties are harmless.

## 13. Dependency spine and anti-claims

The logical order is
\[
 \text{typed supports/seeds}\to\text{gradient degree maps}
 \to\text{strict carries}\to\text{translation}
 \to\text{monotone walls and tail}.
\]
The Hessian/Jacobian lemma feeds every exact-degree induction, the reflected
identities plus spans feed the reciprocity converse, and the four-section
margins feed only the local lemma.  The fixture verifies arithmetic but is
not universal evidence.

The article makes no claim of arbitrary-support or zero-coordinate extension,
an unconditional algorithm, a global map-level reversor, global conjugacy or
classification, entropy, higher dynamical degrees, minimal scalar recurrence,
Perron algebraic degree, same-seed reciprocity away from an
\(R_{\rm state}\)-fixed pair, multi-edge/all-iterate perturbation stability,
or priority.

BATCH07_PAPER27_PROOF_PACKAGE_FROZEN

## 14. Typed-definition correction (authoritative addendum)

The paragraph in Section 1 that used \(K_e\) for both a degree-vector domain
and a pair-dependent collection of carries is superseded by this explicit
typing.  No earlier byte is deleted; from this marker onward every occurrence
of \(K_e\) and \(C_e^+\) is to be read as follows.

First define the **u-only cone**
\[
 \mathcal K_e^u=\{u\in\mathbb R_{>0}^r:
   \alpha\text{ is the unique V maximizer at }u,\ 
   \beta\text{ is the unique W maximizer at }A_\alpha u,
   \ B_\beta A_\alpha u-u>0,
   \text{ and all listed target/reflection score checks involving only }u
   \text{ hold}\}.
\]
The source fresh-carry inequality is not part of this cone.  Define instead
the **typed pair cell**
\[
 \mathcal C_e^+
 =\{(u,w)\in\mathbb R_{>0}^r\times\mathbb R_{>0}^r:
       u\in\mathcal K_e^u,\quad A_\alpha u-w>0,\quad
       \mathsf{PairGaps}_e(u,w)>0\}.
\tag{14.1}
\]
Here \(\mathsf{PairGaps}_e(u,w)>0\) is a finite, explicitly printed list of
all remaining inequalities whose arguments include \(w\), \(Rw\), or a
transformed pair: source/target pair carries, reflected inverse carries, and
typed target-cell predicates.  Every vector inequality in (14.1) is
componentwise.  Thus \(u\in\mathcal K_e^u\) is well-typed, while
\((u,w)\in\mathcal C_e^+\) is the only assertion that can involve \(w\).

The lattice seed set and observable spans are consequently
\[
 \mathcal C_e^{\mathbb Z}
   =\mathcal C_e^+\cap(\mathbb Z_{>0}^r)^2,\qquad
 U_e=\operatorname{span}_{\mathbb R}
       \{u:(u,w)\in\mathcal C_e^{\mathbb Z}\},
\]
\[
 V_e=\operatorname{span}_{\mathbb R}
       \{A_\alpha u:(u,w)\in\mathcal C_e^{\mathbb Z}\}.
\tag{14.2}
\]
The reflected cell is \(R_{\rm state}(\mathcal C_e^+)\); its pair predicates
are checked after the swap and are never silently folded into
\(\mathcal K_e^u\).

For the fixture, \(K_1,K_2\) are exactly the displayed u-only cones in
Section 11, and
\[
 C_i^+=\{(u,w):u\in K_i,\ w>0,\ A_i u-w>0\}
\]
with any separately displayed reflected/target pair predicates understood as
part of \(\mathsf{PairGaps}_e\).  This is the canonical interpretation of
all source, target, reflected, and span statements in this package and
removes the prior \(K_e/C_e^+\) type ambiguity.

BATCH07_PAPER27_PROOF_PACKAGE_TYPED_DEFINITION_CORRECTION
