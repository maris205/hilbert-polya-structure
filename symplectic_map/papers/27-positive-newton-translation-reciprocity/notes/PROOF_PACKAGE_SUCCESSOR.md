# Paper 27 successor proof package

author_disposition: AUTHOR_STOP_FOR_FRESH_INDEPENDENT_PROOF_SCOPE_REVIEW
controlling_event: B07-E0234-P27-RECOVERY-PLAN-PASS-CONSUMPTION-AND-S1-PROOF-SCOPE-AUTHORIZATION
candidate_id: positive_newton_translation_reciprocity_v5
artifact_role: prospective mathematical proof certificate; not a review PASS
external_effect: none

## 1. Successor boundary and supersession map

Let \(K\) be a field of characteristic zero, let \(r\geq 3\), and let
\[
 E_V,E_W\subset\mathbb Z_{\geq2}^{\,r}
\]
be finite nonempty collected supports with nonzero coefficients.  For
\[
 V(q)=\sum_{\alpha\in E_V}c_\alpha q^\alpha,\qquad
 W(p)=\sum_{\beta\in E_W}d_\beta p^\beta
\]
consider
\[
 S_V(q,p)=(q,p+\nabla V(q)),\qquad
 T_W(q,p)=(q+\nabla W(p),p),\qquad F=T_W\circ S_V .
\]
The degree space is an ordered real vector space independent of \(K\).
Incoming leading tuples occupy disjoint algebraically independent blocks.

This successor package retains the earlier theorem but replaces four
insufficient formulations:

1. every selector, carry, reflected, target, and transformed-pair condition
   is now an enumerated finite linear family; no opaque PairGaps predicate
   carries proof content;
2. a target-dependent transition uses an arrow domain, so a source-only
   margin is never confused with target-cell inclusion;
3. a nonempty strict homogeneous integer cell has full observable spans;
   proper-span and nonliteral-selector claims are deleted; and
4. the selector-change count is the discrete ordered-pair count, with
   simultaneous component changes counted once and an exact equality
   criterion.

The local perturbation theorem changes only a normalized degree state with
the support, labels, exponent rows, comparison-row sets, and projection
domains fixed.  It stops after one forward and one reflected inverse step.

No result below asserts a universal equality-pattern realization, global
support reflection, map-level reversor, conjugacy, support classification,
target inclusion inferred from a margin, support or exponent perturbation,
multi-edge robustness, all-iterate robustness, positive-characteristic
extension, or an \(r=2\) theorem.

## 2. M1: typed cells, four inequality families, and transitions

For labels \(\alpha\in E_V,\beta\in E_W\), set
\[
 A_\alpha=\mathbf1\alpha^{\mathsf T}-I,\qquad
 B_\beta=\mathbf1\beta^{\mathsf T}-I,\qquad
 C_{\alpha,\beta}=B_\beta A_\alpha .
\]
For a pair state \(z=(u,w)\in\mathbb R^{2r}\), define
\[
 v=A_\alpha u,\qquad u'=C_{\alpha,\beta}u,\qquad
 \Phi_{\alpha,\beta}(u,w)=(u',v).
\tag{2.1}
\]
All inequalities in this section are strict.  Vector inequalities are
componentwise.

### 2.1 Source selector and source carry

The complete source family for \(e=(\alpha,\beta)\) is
\[
\begin{array}{ll}
u_i>0,\quad w_i>0,&1\leq i\leq r,\\
(\alpha-\gamma)\cdot u>0,&\gamma\in E_V\setminus\{\alpha\},\\
(A_\alpha u-w)_i>0,&1\leq i\leq r,\\
(\beta-\eta)\cdot A_\alpha u>0,&\eta\in E_W\setminus\{\beta\},\\
(C_{\alpha,\beta}u-u)_i>0,&1\leq i\leq r .
\end{array}
\tag{2.2}
\]
The selector rows and carries are hypotheses.  They imply, rather than
assume,
\[
 A_\alpha u>w>0,\qquad C_{\alpha,\beta}u>u>0,
\tag{2.3}
\]
so the transformed pair in (2.1) is positive.

### 2.2 Reflected selector and reflected carry

Let \(R\) reverse coordinates and put
\[
 R_{\rm state}(u,w)=(Rw,Ru),\qquad
 \bar\alpha=R\alpha,\quad\bar\beta=R\beta .
\]
The discrete support conditions
\[
 \bar\alpha\in E_W,\qquad\bar\beta\in E_V
\tag{2.4}
\]
are separate hypotheses.  Starting at \(R_{\rm state}(u,w)\), the inverse
uses \(W\) first and \(V\) second.  Its printed family is
\[
\begin{array}{ll}
(\bar\alpha-\eta)\cdot Ru>0,
  &\eta\in E_W\setminus\{\bar\alpha\},\\
(B_{\bar\alpha}Ru-Rw)_i>0,&1\leq i\leq r,\\
(\bar\beta-\gamma)\cdot B_{\bar\alpha}Ru>0,
  &\gamma\in E_V\setminus\{\bar\beta\},\\
(A_{\bar\beta}B_{\bar\alpha}Ru-Ru)_i>0,&1\leq i\leq r .
\end{array}
\tag{2.5}
\]
For literal labels,
\[
 B_{R\alpha}R=RA_\alpha,\qquad A_{R\beta}R=RB_\beta ,
\tag{2.6}
\]
and therefore the two reflected carries are exactly
\[
 R(A_\alpha u-w)>0,\qquad R(C_{\alpha,\beta}u-u)>0 .
\tag{2.7}
\]
They are algebraically redundant once (2.4) and (2.6) hold, but remain
printed because they type the inverse phases.  Reflected selector comparisons
against all competing rows are not consequences of the forward family.

### 2.3 Additional finite rows and the positive source cell

Any remaining homogeneous pair rows must be supplied as a literal finite
list
\[
 D_{e,k}(u,w)=d^u_{e,k}\cdot u+d^w_{e,k}\cdot w>0,
\qquad 1\leq k\leq m_e .
\tag{2.8}
\]
The list may be empty.  Let \(\mathcal S_e^+\) be the set satisfying
(2.2), (2.4)--(2.5), and (2.8), and let
\[
 \mathcal S_e^{\mathbb Z}
 =\mathcal S_e^+\cap(\mathbb Z_{>0}^{r})^2 .
\tag{2.9}
\]
This is a source cell.  It does not yet name a target.

### 2.4 Target selector, target carry, and transformed membership

For a declared target \(f=(a,b)\), set
\[
 z'=(u',w')=\Phi_e(z)
 =(C_{\alpha,\beta}u,A_\alpha u).
\]
The target family is
\[
\begin{array}{ll}
(a-\gamma)\cdot u'>0,&\gamma\in E_V\setminus\{a\},\\
(A_a u'-w')_i>0,&1\leq i\leq r,\\
(b-\eta)\cdot A_a u'>0,&\eta\in E_W\setminus\{b\},\\
(B_bA_a u'-u')_i>0,&1\leq i\leq r .
\end{array}
\tag{2.10}
\]
After substituting \(z'\), these are the explicit rows
\[
\begin{array}{ll}
(a-\gamma)\cdot C_{\alpha,\beta}u>0,\\
(A_aC_{\alpha,\beta}u-A_\alpha u)_i>0,\\
(b-\eta)\cdot A_aC_{\alpha,\beta}u>0,\\
(B_bA_aC_{\alpha,\beta}u-C_{\alpha,\beta}u)_i>0 .
\end{array}
\tag{2.11}
\]
The reflected target family is (2.5) with \(e,z\) replaced by \(f,z'\).
The remaining transformed-pair rows are
\[
 D_{f,k}(C_{\alpha,\beta}u,A_\alpha u)>0 .
\tag{2.12}
\]

Define the typed arrow domain
\[
\mathcal C_{e\to f}^+
=\{z\in\mathcal S_e^+:
 \text{(2.10), its reflected target family, and (2.12) hold}\}.
\tag{2.13}
\]
Every row in (2.13) is a displayed homogeneous linear form in \(u,w\).

**Typed inclusion lemma.**
For every declared arrow,
\[
 \Phi_e(\mathcal C_{e\to f}^+)\subseteq\mathcal S_f^+ .
\tag{2.14}
\]

**Proof.**
For \(z\in\mathcal C_{e\to f}^+\), (2.3) gives positivity of
\(z'=\Phi_e(z)\).  The four groups in (2.10) are precisely the source
selector and carry groups (2.2) for \(f\).  The reflected target group is
(2.5) for \(f\), and (2.12) supplies all \(D_f\)-rows.  Hence
\(z'\in\mathcal S_f^+\).  No source-only margin was used to infer a target
selector. \(\square\)

If a source selector pair has several possible targets, (2.13) partitions
the corresponding domains.  The notation
\(\Phi_e(\mathcal S_e^+)\subseteq\mathcal S_f^+\) is allowed only when all
of \(\mathcal S_e^+\) has the complete \(f\)-certificate.

### 2.5 Realization of every integer pair seed

**Seed realization lemma.**
Every positive integer pair \((u,w)\) is realized by disjoint algebraically
independent incoming leading tuples.

**Proof.**
In
\[
 K[X_1,\ldots,X_r,Y_1,\ldots,Y_r]
\]
take \(Q_i=X_i^{u_i}\) and \(P_i=Y_i^{w_i}\), with ordinary degree.
Distinct monomials in abstract variables \(T_i,S_i\) map to monomials with
distinct exponent vector
\[
 (u_1a_1,\ldots,u_ra_r,w_1b_1,\ldots,w_rb_r).
\]
Positivity makes this exponent map injective.  Thus the \(Q_i,P_i\) are
algebraically independent and have the requested degrees.  Independent
variable blocks realize the six fixture pairs separately. \(\square\)

The formal map (2.1) becomes an actual leading-degree map only after the
survival lemmas below.

## 3. M2: face Hessians and leading-form survival

### 3.1 Grouped determinant and the secondary-lowest monomial

For a nonempty exposed face \(E_0\) of either support, write
\[
 P_{E_0}(X)=\sum_{\xi\in E_0}c_\xi X^\xi,\qquad
 h_{ij}(\xi)=\xi_i(\xi_j-\delta_{ij}).
\]
Expansion by determinant rows gives
\[
\det\operatorname{Hess}P_{E_0}
=\sum_{(\xi^{(1)},\ldots,\xi^{(r)})\in E_0^r}
\left(\prod_i c_{\xi^{(i)}}\right)
D(\xi^{(1)},\ldots,\xi^{(r)})
X^{\sum_i\xi^{(i)}-2\mathbf1},
\tag{3.1}
\]
where
\[
D(\xi^{(1)},\ldots,\xi^{(r)})
=\det[h_{ij}(\xi^{(i)})]_{i,j}.
\]
Choose a real linear functional \(\omega\) with unique minimizer
\(\xi_0\) on the finite set \(E_0\).  The secondary weight of a term in
(3.1) is
\[
\sum_i\omega\cdot\xi^{(i)}-2\omega\cdot\mathbf1,
\]
so the repeated tuple \((\xi_0,\ldots,\xi_0)\) is the unique minimizer.
No different row tuple can contribute to its monomial.  Its row matrix is
\[
\operatorname{diag}(\xi_0)(\mathbf1\xi_0^{\mathsf T}-I),
\]
and the determinant lemma gives
\[
D(\xi_0,\ldots,\xi_0)
=(-1)^r(1-|\xi_0|)\prod_i\xi_{0i}.
\tag{3.2}
\]
The isolated coefficient
\[
c_{\xi_0}^{\,r}(-1)^r(1-|\xi_0|)\prod_i\xi_{0i}
\tag{3.3}
\]
is nonzero in characteristic zero because every \(\xi_{0i}\geq2\).
Therefore
\[
\det\operatorname{Hess}P_{E_0}\neq0.
\tag{3.4}
\]
The secondary functional isolates a determinant term.  It does not select
a vertex on the original tied face.

### 3.2 Jacobian independence

**Jacobian lemma.**
If \(G_1,\ldots,G_r\in K[X_1,\ldots,X_r]\) have nonzero Jacobian
determinant, then they are algebraically independent.

**Proof.**
Assume a nonzero relation \(H(G)=0\) of least total degree.  Differentiation
gives
\[
J_G^{\mathsf T}(H_{Y_1}(G),\ldots,H_{Y_r}(G))^{\mathsf T}=0 .
\]
Over the fraction field, \(J_G\) is invertible, so every
\(H_{Y_i}(G)=0\).  Minimality makes every nonzero derivative impossible;
all derivatives of \(H\) vanish.  In characteristic zero \(H\) is constant,
a contradiction. \(\square\)

Applied to \(G=\nabla P_{E_0}\), (3.4) proves algebraic independence of the
face-gradient tuple.  The criterion is classical; the new use is its typed
placement in the phase induction.

### 3.3 Injective substitution in the associated graded ring

Let \(\mathcal A\) be a filtered \(K\)-algebra and suppose the initial forms
\(Z_i=\operatorname{in}(Q_i)\) are algebraically independent.  Then
\[
K[X_1,\ldots,X_r]\longrightarrow\operatorname{gr}\mathcal A,
\qquad X_i\longmapsto Z_i
\tag{3.5}
\]
is injective.  If \(H_1,\ldots,H_r\) are algebraically independent, so are
\(H_1(Z),\ldots,H_r(Z)\): a relation after substitution pulls back through
(3.5).

On an exposed face, every monomial of
\(\partial_iP_{E_0}\) has weight \(h_{E_0}(u)-u_i\).  Hence the top part
after substitution is \((\partial_iP_{E_0})(Z)\), which is nonzero.
The selected fresh tuple therefore has the exact componentwise degree
\[
 A_\alpha u=(\alpha\cdot u)\mathbf1-u
\]
and remains algebraically independent.  The same argument applies to a
\(W\)-face and \(B_\beta v\).

### 3.4 Fresh/old separation

If filtered elements \(F_i,O_i\) satisfy
\(\deg F_i>\deg O_i\), then
\[
\operatorname{in}(F_i\pm O_i)=\operatorname{in}(F_i).
\tag{3.6}
\]
Indeed, \(O_i\) has no component in the top graded degree and cannot cancel
the initial form of \(F_i\).  Internal cancellation in a substituted fresh
gradient is excluded by Section 3.3; cancellation between the fresh and old
blocks is excluded separately by the strict carries in (2.2).

### 3.5 Forward and inverse half-step induction

**Survival lemma.**
At a certified half-step, assume the incoming active tuple has algebraically
independent leading components, the selected face lies in the positive
support class, and the fresh carry is strict.  Then the selected gradient has
the predicted degree and independent leading tuple; adding or subtracting
the carried old tuple preserves it; and the outgoing active tuple satisfies
the same hypothesis for the next half-step.

**Proof.**
Sections 3.1--3.3 give exact nonzero substituted initial forms and their
independence.  Section 3.4 separates the old block.  Iteration proves every
finite prefix.  For
\[
F^{-1}=S_V^{-1}\circ T_W^{-1}
\]
the phase order is \(W\) then \(V\); multiplication of a fresh block by
\(-1\) changes neither degree nor independence.  Apply the reflected rows
(2.5). \(\square\)

For an infinite branch, every finite prefix is certified; no limiting
argument is asserted.

### 3.6 Three distinct failure mechanisms

1. **Zero-coordinate Hessian failure.**
   For \(P=X_1^2X_2^2\) in three variables, \(\partial_3P=0\) and the
   Hessian determinant vanishes.
2. **Unit-coordinate selector/carry failure.**
   With \(\alpha=(1,2,2)\), \(\gamma=(2,1,2)\), and
   \(u=(1,1,1)\), the two scores tie.  For the singleton \(\alpha\),
   \(A_\alpha u=(4,4,4)\); choosing \(w=(4,1,1)\) makes the first carry
   \((0,3,3)\).  These are distinct selector and old-block failures.
3. **Positive-characteristic derivative cancellation.**
   In characteristic \(p\), \(P=(X_1X_2X_3)^p\) has positive exponents but
   zero gradient.

These examples delimit the assumptions and do not propose extensions.

## 4. Translation and M3: exact envelopes and equality

For a strict selected pair, put \(s=\alpha\cdot u=h_V(u)\).  Then
\[
v=A_\alpha u=s\mathbf1-u,
\]
and
\[
\begin{aligned}
u'&=B_\beta v\\
&=u+\bigl((|\beta|-1)\alpha-\beta\bigr)\cdot u\,\mathbf1.
\end{aligned}
\tag{4.1}
\]
Let
\[
\delta_{\alpha,\beta}(u)
=\bigl((|\beta|-1)\alpha-\beta\bigr)\cdot u.
\tag{4.2}
\]
The second carry is exactly \(\delta_{\alpha,\beta}(u)>0\).  On integer
seeds it is an integer at least one.  Thus an infinite strict branch has
\[
u_n=u_0+t_n\mathbf1,\qquad
0=t_0<t_1<t_2<\cdots .
\tag{4.3}
\]

### 4.1 Within-total representatives

Let
\[
T_V=\{|\alpha|:\alpha\in E_V\},\quad
T_W=\{|\beta|:\beta\in E_W\},\quad
d_V=|T_V|,\quad d_W=|T_W|.
\]
For \(s\in T_V\), define
\[
M_s=\max_{|\alpha|=s}\alpha\cdot u_0
\tag{4.4}
\]
and freeze a maximizer \(\alpha_s\).  For \(s\in T_W\), define
\[
N_s=-\min_{|\beta|=s}\beta\cdot u_0
\tag{4.5}
\]
and freeze a minimizer \(\beta_s\).

Let \(S_V\) be the totals whose optimizer in (4.4) is unique and \(S_W\)
the totals whose optimizer in (4.5) is unique; set
\[
q_V=|S_V|,\qquad q_W=|S_W|.
\tag{4.6}
\]
Within a total class the score difference is constant on the diagonal ray.
A tie therefore persists, while a unique representative never switches to
another representative of the same total.

### 4.2 Strict activity intervals

Along \(u(t)=u_0+t\mathbf1\),
\[
h_V(u(t))=\max_{s\in T_V}(M_s+st),\qquad
g(t)=h_V(u(t))-t
=\max_{s\in T_V}(M_s+(s-1)t).
\tag{4.7}
\]
Because every slope \(s-1>0\), \(g\) is strictly increasing.  Moreover
\[
v(t)=g(t)\mathbf1-u_0
\]
and hence
\[
h_W(v(t))=\max_{s\in T_W}(s\,g(t)+N_s).
\tag{4.8}
\]

Define
\[
I_s^V=\{t\geq0:M_s+st>M_a+at\ \text{for all }a\neq s\},
\tag{4.9}
\]
\[
I_s^W=\{g\geq g(0):sg+N_s>ag+N_a\ \text{for all }a\neq s\},
\tag{4.10}
\]
with the unique within-total condition understood.  Each is an open interval,
possibly empty.  A line that touches the upper envelope only at a tie has an
empty strict activity interval and is not counted as visited.

For an upper envelope of affine lines, if the uniquely active line at
\(x\) has slope \(a\) and a different uniquely active line at \(y>x\) has
slope \(b\), then \(b>a\): the affine difference changes from negative to
positive.  Thus active totals increase strictly at every switch.

### 4.3 Discrete pair-change count

At the branch samples, put \(g_n=g(t_n)\) and let
\[
s_V(n)=|\alpha_n|,\qquad s_W(n)=|\beta_n|.
\]
Both sequences are nondecreasing and increase strictly at a component
switch.  Discrete sampling may skip activity intervals but cannot return
across a wall.  Landing on a wall is excluded by strict certification.

Let
\[
I_V=\{n:s_V(n+1)\neq s_V(n)\},\qquad
I_W=\{n:s_W(n+1)\neq s_W(n)\}
\]
and define
\[
N_{\rm pair}
=\#\{n:(s_V(n+1),s_W(n+1))
\neq(s_V(n),s_W(n))\}.
\tag{4.11}
\]
Then
\[
\begin{aligned}
N_{\rm pair}
&=|I_V\cup I_W|\\
&\leq |I_V|+|I_W|\\
&\leq(q_V-1)+(q_W-1)\\
&\leq d_V+d_W-2 .
\end{aligned}
\tag{4.12}
\]
A simultaneous \(V\)- and \(W\)-switch belongs to
\(I_V\cap I_W\) and counts once.

**Exact equality theorem.**
Equality in the final bound holds if and only if:

1. \(q_V=d_V\) and \(q_W=d_W\);
2. every \(V\)-total class has a nonempty interval \(I_s^V\) containing
   some \(t_n\);
3. every \(W\)-total class has a nonempty interval \(I_s^W\) containing
   some \(g_n\); and
4. \(I_V\cap I_W=\varnothing\).

**Proof.**
Equality in (4.12) forces equality at every intermediate inequality.
Consequently each monotone selector sequence makes the maximum possible
number of strict increases and visits every available class; every visit is
a sample in a nonempty strict interval.  Equality in the union bound is
equivalent to disjoint switch-index sets.  Conversely, conditions 1--3 make
the two sequences visit all \(d_V,d_W\) classes in increasing order, yielding
\(d_V-1,d_W-1\) component switches, and condition 4 makes all indices
distinct. \(\square\)

This characterizes equality on an existing branch.  It does not realize all
patterns.

### 4.4 Closed stationary tail with the global origin

After the last pair change, fix \((\alpha,\beta)\), let \(N\) be the first
stationary index, and put
\[
c=(|\beta|-1)\alpha-\beta,\quad
\lambda=(|\alpha|-1)(|\beta|-1),\quad
\mu=c\cdot u_0 .
\]
Then, for \(n\geq N\),
\[
t_{n+1}=\lambda t_n+\mu
\tag{4.13}
\]
and
\[
t_n=\lambda^{n-N}t_N+
\mu\frac{\lambda^{n-N}-1}{\lambda-1},\qquad
u_n=u_0+t_n\mathbf1 .
\tag{4.14}
\]
The intercept uses the original \(u_0\); no transient reset is made.

## 5. M4: full observable spans and literal word reciprocity

For an arrow domain, define
\[
U_e=\operatorname{span}_{\mathbb R}
\{u:(u,w)\in\mathcal C_{e\to f}^+\cap\mathbb Z^{2r}\},
\]
\[
V_e=\operatorname{span}_{\mathbb R}
\{A_\alpha u:(u,w)\in\mathcal C_{e\to f}^+\cap\mathbb Z^{2r}\}.
\]

**Full-span lemma.**
If a set
\[
\mathcal C=\{z:h_jz>0,\ 1\leq j\leq N\}
\]
is defined by finitely many strict homogeneous linear inequalities and
contains an integer point \(z_0=(u_0,w_0)\), then its \(u\)-projection
generates \(\mathbb R^r\).

**Proof.**
Let \(E_k=(e_k,0)\), let
\[
m=\min_jh_jz_0>0,\qquad
M=\max_{j,k}|h_jE_k|.
\]
For any integer \(N>M/m\), both \(Nz_0\) and \(Nz_0+E_k\) satisfy every
strict row and remain positive integer pairs.  The difference of their
\(u\)-projections is \(e_k\).  Hence all coordinate vectors lie in the
span. \(\square\)

Since
\[
\det A_\alpha=(-1)^r(1-|\alpha|)\neq0,
\tag{5.1}
\]
we also have \(V_e=A_\alpha U_e=\mathbb R^r\).

The assignments \(\xi\mapsto A_\xi\) and \(\xi\mapsto B_\xi\) are
injective because equality leaves
\(\mathbf1(\xi-\xi')^{\mathsf T}=0\).  Therefore any phase identities
\[
B_{\widetilde\alpha}R=RA_\alpha,\qquad
A_{\widetilde\beta}R=RB_\beta
\tag{5.2}
\]
force
\[
\widetilde\alpha=R\alpha,\qquad
\widetilde\beta=R\beta.
\tag{5.3}
\]

**Finite-word reciprocity theorem.**
Let \(e_k=(\alpha_k,\beta_k)\), \(0\leq k<n\), be a finite typed word whose
arrow domains are strict, homogeneous, and contain integer seeds.  Phase-
resolved reflected-inverse reciprocity for every seed and every prefix holds
if and only if, at every edge:

1. \(R\alpha_k\in E_W\) and is the unique reflected \(W\)-selector;
2. \(R\beta_k\in E_V\) and is the unique reflected \(V\)-selector; and
3. all reflected source, carry, target, and transformed membership rows hold.

**Proof.**
For sufficiency, if \(v_k=A_{\alpha_k}u_k\) and
\(u_{k+1}=B_{\beta_k}v_k\), then
\[
B_{R\alpha_k}Ru_k=Rv_k,\qquad
A_{R\beta_k}Rv_k=Ru_{k+1}.
\]
The reflected carries are the reversals of the forward carries, and the
target certificate advances the induction to \(k+1\).  For necessity, the
first phase identity on all integer seeds gives a matrix identity on
\(U_e=\mathbb R^r\); the second gives one on
\(V_e=\mathbb R^r\).  Injectivity forces the literal labels, while
persistence to the next edge forces its reflected target rows. \(\square\)

No proper-span or nonliteral example exists under these hypotheses.
Observable-span notation remains only as the intermediate object in the
necessity proof.

## 6. M5: quantitative one-step fixed-state robustness

Normalize a fixed certified state \(z=(u,w)\) by \(\|z\|_1=1\).  Supports,
labels, exponent rows, arrow, permitted comparison rows, and projection
domains are frozen.  Define
\[
P_u=(I\ 0),\qquad P_w=(0\ I),\qquad
F_e=\begin{pmatrix}C_{\alpha,\beta}&0\\A_\alpha&0\end{pmatrix}.
\]
The four projection domains are
\[
P_uz=u,\quad A_\alpha P_uz=v,\quad
RP_uz=Ru,\quad RA_\alpha P_uz=Rv.
\tag{6.1}
\]

For fixed finite competitor/lower/new row sets, the forward family \(J_+\)
contains:

1. coordinate positivity for \(u,w\);
2. every selected-minus-competitor row at \(u\);
3. every coordinate of \(A_\alpha u-w\);
4. every selected-minus-competitor row at \(A_\alpha u\);
5. every coordinate of \(C_{\alpha,\beta}u-u\);
6. every target selector and carry row (2.11);
7. every transformed \(D_f\)-row; and
8. every fixed selected-minus-lower/new row on the first two projections in
   (6.1).

The reflected family \(J_-\) contains the four groups (2.5), their target
versions after \(F_ez\), all reflected transformed rows, and every fixed
selected-minus-lower/new row on the last two projections in (6.1).

After composing with the displayed projection and transition matrices, write
every member as
\[
\ell_j(z)=a_j\cdot z>0 .
\]
Define
\[
m_+=\min_{j\in J_+}\ell_j(z),\quad
L_+=\max_{j\in J_+}\|a_j\|_1,
\]
\[
m_-=\min_{j\in J_-}\ell_j(z),\quad
L_-=\max_{j\in J_-}\|a_j\|_1
\tag{6.2}
\]
and the explicit radius
\[
\boxed{\displaystyle
\rho_e(z)=
\frac{\min\{m_+,m_-\}}
     {2\max\{1,L_+,L_-\}} .}
\tag{6.3}
\]

**Half-margin theorem.**
For every perturbation \(\delta\in\mathbb R^{2r}\) satisfying
\[
\|\delta\|_\infty<\rho_e(z),
\tag{6.4}
\]
the perturbed state \(z+\delta\) retains more than half of every fixed
forward and reflected margin.  If one insists on the normalized section,
also impose \(\mathbf1_{2r}^{\mathsf T}\delta=0\).

**Proof.**
For every \(j\),
\[
|a_j\cdot\delta|
\leq\|a_j\|_1\|\delta\|_\infty
<\frac12\min\{m_+,m_-\}
\leq\frac12\ell_j(z).
\]
Thus \(\ell_j(z+\delta)>\ell_j(z)/2>0\), separately for
\(J_+\) and \(J_-\). \(\square\)

The theorem supplies an exact symbolic radius for any predeclared finite
row family.  It does not invent a numerical radius before those rows are
frozen, and it does not perturb the rows themselves.

**Indispensable-row example.**
In the fixture below, delete only
\[
(a_1-\gamma)\cdot u=(6,-6,0)\cdot u>0
\]
and take \(u=(2,2,1),w=\mathbf1\).  The other three source rows are
\(2,14,20>0\); the two carries are
\[
A_1u-w=(19,19,20)>0,\qquad C_{21}u-u=240\mathbf1>0;
\]
and the four target rows are \(238,238,2892,2898>0\).  Nevertheless
\[
a_1\cdot u=\gamma\cdot u=22>a_2\cdot u=20.
\]
Removing that margin destroys unique selection while all retained rows
remain strict.  Normalization by \(8\) preserves the example.

This is one-state, one-edge, one-forward-step and one-reflected-step
robustness.  It supplies no new whole-core inclusion or later-edge claim.

## 7. M6: complete integer-pair fixture

Take
\[
\begin{aligned}
a_1&=(8,2,2),&a_2&=(2,5,6),&\gamma&=(2,8,2),\\
b_1&=(2,2,8)=Ra_1,&b_2&=(6,5,2)=Ra_2 .
\end{aligned}
\]
The edge labels are \(e_1=(a_1,b_2)\) and \(e_2=(a_2,b_2)\).  The matrices
are
\[
A_1=\begin{pmatrix}7&2&2\\8&1&2\\8&2&1\end{pmatrix},\quad
A_2=\begin{pmatrix}1&5&6\\2&4&6\\2&5&5\end{pmatrix},
\]
\[
A_\gamma=\begin{pmatrix}1&8&2\\2&7&2\\2&8&1\end{pmatrix},\quad
B_1=\begin{pmatrix}1&2&8\\2&1&8\\2&2&7\end{pmatrix},\quad
B_2=\begin{pmatrix}5&5&2\\6&4&2\\6&5&1\end{pmatrix}.
\]
Direct multiplication gives
\[
C_{21}=B_2A_1=I+\mathbf1(90,19,22),\qquad
C_{22}=B_2A_2=I+\mathbf1(18,55,70).
\tag{7.1}
\]

### 7.1 Complete row lists

The four source rows for the two cells are
\[
K_1=\begin{pmatrix}
6&-3&-4\\6&-6&0\\4&-1&8\\4&5&2
\end{pmatrix},\qquad
K_2=\begin{pmatrix}
-6&3&4\\0&-3&4\\-2&2&12\\-2&8&6
\end{pmatrix}.
\tag{7.2}
\]
They record two \(V\)-score gaps, the forward \(W\)-gap, and the additional
reflected \(V\)-gap.  The target rows are
\[
T_{21}=K_2C_{21}
=\begin{pmatrix}
84&22&26\\90&16&26\\1078&230&276\\1078&236&270
\end{pmatrix},
\]
\[
T_{22}=K_2C_{22}
=\begin{pmatrix}
12&58&74\\18&52&74\\214&662&852\\214&668&846
\end{pmatrix}.
\tag{7.3}
\]
The source second-carry rows are
\[
\delta_1=(90,19,22),\qquad\delta_2=(18,55,70).
\]
The target first-carry rows are
\[
\kappa_{21}=(1074,231,268),\qquad
\kappa_{22}=(216,660,840),
\tag{7.4}
\]
and the target second-carry rows are
\[
\tau_{21}=\delta_2C_{21}=(12888,2772,3216),
\]
\[
\tau_{22}=\delta_2C_{22}=(2592,7920,10080).
\tag{7.5}
\]
Equations (7.2)--(7.5) enumerate every non-coordinate row needed for the
two declared arrows \(e_1\to e_2\) and \(e_2\to e_2\).  Their reflected
versions are obtained by the literal identities, not by an unprinted
predicate.

### 7.2 Six full pairs and forward scores

All six pairs use the explicit canonical choice \(w=\mathbf1\).  This is
valid without a search because each coordinate of \(A_i u\) is at least
five for positive \(u\) and positive support coordinates.

| ID | Edge | \((u;w)\) | \((a_1u,a_2u,\gamma u)\) | \(v=A_i u\) | \((b_1v,b_2v)\) | \(u'=C_{2i}u\) |
|---|---|---|---|---|---|---|
| P1 | \(e_1\) | \((2,1,1;1,1,1)\) | \((20,15,14)\) | \((18,19,19)\) | \((226,241)\) | \((223,222,222)\) |
| P2 | \(e_1\) | \((2,1,2;1,1,1)\) | \((22,21,16)\) | \((20,21,20)\) | \((242,265)\) | \((245,244,245)\) |
| P3 | \(e_1\) | \((3,1,1;1,1,1)\) | \((28,17,16)\) | \((25,27,27)\) | \((320,339)\) | \((314,312,312)\) |
| Q1 | \(e_2\) | \((1,1,1;1,1,1)\) | \((12,13,12)\) | \((12,12,12)\) | \((144,156)\) | \((144,144,144)\) |
| Q2 | \(e_2\) | \((1,1,2;1,1,1)\) | \((14,19,14)\) | \((18,18,17)\) | \((208,232)\) | \((214,214,215)\) |
| Q3 | \(e_2\) | \((1,2,2;1,1,1)\) | \((16,24,22)\) | \((23,22,22)\) | \((266,292)\) | \((269,270,270)\) |

### 7.3 Source, carry, and reflected tables

In the next table the source-row tuple is \(K_i u\),
\[
W^-=(b_1Ru,b_2Ru),\qquad
V^-=(a_1Rv,a_2Rv,\gamma Rv).
\]

| ID | \(K_i u\) | \(v-w\) | \(u'-u\) | \(W^-\) | \(V^-\) | \(R(v-w)\) |
|---|---:|---|---|---|---|---|
| P1 | \((5,6,15,15)\) | \((17,18,18)\) | \(221\mathbf1\) | \((20,15)\) | \((226,241,226)\) | \((18,18,17)\) |
| P2 | \((1,6,23,17)\) | \((19,20,19)\) | \(243\mathbf1\) | \((22,21)\) | \((242,265,248)\) | \((19,20,19)\) |
| P3 | \((11,12,19,19)\) | \((24,26,26)\) | \(311\mathbf1\) | \((28,17)\) | \((320,339,320)\) | \((26,26,24)\) |
| Q1 | \((1,1,12,12)\) | \((11,11,11)\) | \(143\mathbf1\) | \((12,13)\) | \((144,156,144)\) | \((11,11,11)\) |
| Q2 | \((5,5,24,18)\) | \((17,17,16)\) | \(213\mathbf1\) | \((14,19)\) | \((208,232,214)\) | \((16,17,17)\) |
| Q3 | \((8,2,26,26)\) | \((22,21,21)\) | \(268\mathbf1\) | \((16,24)\) | \((266,292,266)\) | \((21,21,22)\) |

The reflected second carry is \(R(u'-u)=u'-u\), since each is a scalar
multiple of \(\mathbf1\).

### 7.4 Target and reflected-target tables

Let \(v'=A_2u'\).  The entries in \(T_{2i}u\) are, in order, the two target
\(V\)-gaps, the target \(W\)-gap, and the additional reflected target
\(V\)-gap.

| ID | \(T_{2i}u\) | \((a_1u',a_2u',\gamma u')\) | \(v'\) | \((b_1v',b_2v')\) | \((a_1Rv',a_2Rv',\gamma Rv')\) | target carries |
|---|---|---|---|---|---|---|
| P1 | \((216,222,2662,2662)\) | \((2672,2888,2666)\) | \((2665,2666,2666)\) | \((31990,34652)\) | \((31990,34652,31990)\) | \(2647\mathbf1;\ 31764\mathbf1\) |
| P2 | \((242,248,2938,2932)\) | \((2938,3180,2932)\) | \((2935,2936,2935)\) | \((35222,38160)\) | \((35222,38160,35228)\) | \(2915\mathbf1;\ 34980\mathbf1\) |
| P3 | \((300,312,3740,3740)\) | \((3760,4060,3748)\) | \((3746,3748,3748)\) | \((44972,48712)\) | \((44972,48712,44972)\) | \(3721\mathbf1;\ 44652\mathbf1\) |
| Q1 | \((144,144,1728,1728)\) | \((1728,1872,1728)\) | \((1728,1728,1728)\) | \((20736,22464)\) | \((20736,22464,20736)\) | \(1716\mathbf1;\ 20592\mathbf1\) |
| Q2 | \((218,218,2580,2574)\) | \((2570,2788,2570)\) | \((2574,2574,2573)\) | \((30880,33460)\) | \((30880,33460,30886)\) | \(2556\mathbf1;\ 30672\mathbf1\) |
| Q3 | \((276,270,3242,3242)\) | \((3232,3508,3238)\) | \((3239,3238,3238)\) | \((38858,42100)\) | \((38858,42100,38858)\) | \(3216\mathbf1;\ 38592\mathbf1\) |

The two target carries are
\[
v'-v=(\kappa_{2i}\cdot u)\mathbf1,\qquad
C_{22}u'-u'=(\tau_{2i}\cdot u)\mathbf1.
\]
Target reflected first-phase scores
\((b_1Ru',b_2Ru')\) equal \((a_1u',a_2u')\), and the target reflected
carries are reversals of the displayed scalar vectors.  Thus every target
and reflected target row is strict.

### 7.5 Determinants and full spans

With seed vectors as rows,
\[
U_1=\begin{pmatrix}2&1&1\\2&1&2\\3&1&1\end{pmatrix},
\quad\det U_1=1,
\]
\[
U_2=\begin{pmatrix}1&1&1\\1&1&2\\1&2&2\end{pmatrix},
\quad\det U_2=-1.
\tag{7.6}
\]
Separately,
\[
\det A_1=11,\qquad\det A_2=12.
\tag{7.7}
\]
Hence both \(u\)-seed families span, and their images under \(A_i\) span.
The seed determinants \(1,-1\) are not the matrix determinants \(11,12\).

### 7.6 Explicit missing-reflection mismatch

At \(u=(1,10,1)\), \(w=\mathbf1\),
\[
(a_1u,a_2u,\gamma u)=(30,58,84),
\]
so \(\gamma\) is the unique forward \(V\)-selector and
\[
A_\gamma u=(83,74,83).
\]
But \(R\gamma=\gamma\notin E_W\).  The available reflected first-phase
scores are \((b_1Ru,b_2Ru)=(30,58)\), so \(b_2\) is selected and
\[
B_2Ru=(57,48,57)\neq(83,74,83)=RA_\gamma u.
\tag{7.8}
\]
Both relevant carries are positive; the mismatch is caused by the missing
literal reflected label and occurs at \(n=1\).

## 8. Boundary dossier

| Boundary | Exact witness | Consequence |
|---|---|---|
| positive characteristic | In characteristic \(2\), \(V=q_1^2q_2^2q_3^2\) has zero gradient although the formal matrix sends \(\mathbf1\) to \(5\mathbf1\). | Formal weights do not prove survival outside characteristic zero. |
| selector tie | \(u=(2,2,1)\) gives \(a_1u=\gamma u=22>a_2u=20\). | No unique vertex is selected. |
| failed carry | \(u=(2,1,1)\), \(w=(18,1,1)\) gives \(A_1u-w=(0,18,18)\). | Fresh/old separation is unavailable. |
| full-span calculation | The two seed matrices in (7.6) have determinants \(1\) and \(-1\). | The general full-span lemma is visible concretely. |
| missing reflection | Equation (7.8). | Reciprocity fails at the first phase. |
| omitted margin | Delete \((a_1-\gamma)u>0\) and use \((2,2,1;\mathbf1)/8\). | All retained rows are strict, but the selected label ties. |
| cancellation outside class | With \(L=q_1+q_2+q_3\), \(V=L^3\), and \(W=(p_1-p_2)^3\), the equal fresh terms cancel in \(p_1'-p_2'=p_1-p_2\). | Zero/unit-coordinate supports permit actual cancellation. |

The \(r=2\) setting is only an excluded predecessor and portfolio boundary.

## 9. Dependency spine and review obligations

The logical chain is
\[
\text{explicit typed rows}
\to\text{face Hessian}
\to\text{Jacobian independence}
\to\text{graded substitution}
\to\text{fresh/old separation}
\to\text{actual phase map}
\to\text{diagonal translation}
\to\text{envelopes/equality/tail}.
\]
The full-span lemma and matrix injectivity feed word reciprocity.  The finite
row families and dual-norm inequality feed only the one-step robustness
radius.  The fixture verifies arithmetic but proves no universal theorem.

A fresh reviewer must independently check:

1. every row in Sections 2 and 6 is well typed and every target inclusion
   consumes a complete target family;
2. the unique secondary-lowest determinant term cannot cancel;
3. the Jacobian and associated-graded arguments do not assume generic
   coefficients;
4. the equality theorem counts pair changes, handles tie-only lines, and
   excludes simultaneous switches in the equality case;
5. the scaling proof really gives full integer spans and forces literal
   labels;
6. the radius perturbs only \(z\) and uses composed coefficient rows;
7. every entry of the six-pair tables follows from (7.1)--(7.5); and
8. all anti-claims and the local-only effect remain intact.

## 10. Mathematical page yield

The successor manuscript allocation is:

| Module | Genuine new proof-content pages |
|---|---:|
| M1 typed rows, arrow domains, inclusion, seed realization | 1.8 |
| M2 split Hessian, independence, substitution, survival, failures | 2.0 |
| M3 strict activity, discrete pair count, equality, closed tail | 1.9 |
| M4 full spans, injectivity, finite-word reciprocity, mismatch | 1.7 |
| M5 composed rows, radius, half-margin proof, deleted-row witness | 1.7 |
| M6 six full pairs, target/reflected tables, determinants, boundaries | 2.6 |
| **Total** | **11.7** |

This is theorem, proof, and exact example material.  It excludes references,
governance prose, typesetting changes, and warning repair.  The accepted
anonymous manuscript must still measure 24--28 proof-content pages using the
separate reference-start sentinel.

This package creates no source lock, manuscript, build, PDF, release, terminal
PASS, Paper28 action, or external effect.  It now stops for a wholly fresh
independent mathematical review together with the successor claims matrix and
paper plan.

BATCH07_P27_PROOF_PACKAGE_SUCCESSOR_AUTHOR_STOP
