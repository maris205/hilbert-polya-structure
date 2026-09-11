# Proof Package — precise algebraic exclusions

## Claim

1. A map built from an invariant projection, a section and a map on labels
   inherits its post-first-step dynamics and fibres. The exact old
   characteristic-companion map is a height-one retraction with evaluated
   all-target fibres.
2. Standard unpivoted LR on invertible two-by-two matrices does not preserve
   its LU domain. It bijects two different domains; every finite
   forward-closed restriction has unit fibres.
3. The labelled periodic Toda equations used by Kanki, Takahashi and
   Tokihiro are not a single-valued map on the full state set, even after
   their cyclic quotient in the two-site example below.

## Status

**PROVABLE AS STATED** for these three bounded claims.
A new finite autonomous nonlinear map passing the requested residual
two-axis gate is **NOT CURRENTLY JUSTIFIED** by these entrances.

## Assumptions

All sets used in cardinalities are finite. A field has at least two
elements. In finite-field statements, $q$ is a prime power and $\mathbb F_q$
is the field of that order. The Toda paper states its equations over prime
fields; the field-independent obstruction calculations below extend only
these elementary statements to prime powers.

LR means unpivoted factorization with the lower-triangular factor normalized
to have ones on the diagonal. No pivoting, restart, absorbing extension,
branch selection or extra quotient is silently added.

## Notation

$\operatorname{Mat}_2(F)$ and $\operatorname{GL}_2(F)$ denote two-by-two
matrices and invertible matrices over a field $F$. Trace and determinant
are $\operatorname{tr}$ and $\det$.
A fibre is $T^{-1}(y)=\{x:T(x)=y\}$.
A successor of a relation is a state satisfying its equations, not a
deterministic-map fibre.

## Proof Strategy

Direct factorization, induction and coefficient counting. No orbit
classification, asymptotic theorem or numerical output is a premise.

## Dependency Map

1. $\pi s=\operatorname{id}$ implies section injectivity, the iterate
   formula and disjoint fibre decomposition.
2. The companion formula and the count of solutions of $bc=r$ give its
   target count and maximum.
3. Unique LU/UL factorizations give the LR domain bijection; one symbolic
   matrix refutes forward closure.
4. Substitution in Toda gives a one-site quadratic and a two-site product
   constraint. A cyclic shift preserves zero/nonzero status.

## Proof

### 1. Canonical-section subtraction and exact old M08 control

**Step 1.1 — General wrapper.**
Let $\pi:X\to Y$ and $s:Y\to X$ satisfy $\pi s=\operatorname{id}_Y$.
For any $g:Y\to Y$, put $T=sg\pi$. For every integer $t\geq1$,
$$
T^t=sg^t\pi.
$$
The case $t=1$ is the definition. If it holds at $t$, then
$T^{t+1}=sg\pi sg^t\pi=sg^{t+1}\pi$ by the section identity, proving the
claim by induction. Applying $\pi$ to $s(y_1)=s(y_2)$ proves $y_1=y_2$,
so $s$ is injective.

The image of $T$ lies in $s(Y)$ and $T(s(y))=s(g(y))$. Thus $T$ restricted
to $s(Y)$ is conjugate to $g$, and no periodic point lies outside $s(Y)$.
Injectivity of $s$ also gives the disjoint decomposition
$$
T^{-1}(s(y))
=\coprod_{\substack{z\in Y\\g(z)=y}}\pi^{-1}(z),
\qquad
|T^{-1}(s(y))|
=\sum_{\substack{z\in Y\\g(z)=y}}|\pi^{-1}(z)|.
$$
Targets outside $s(Y)$ have empty fibres. When $g=\operatorname{id}_Y$,
this is a retraction with $T^2=T$. A changed representation of the labels
alone does not create a new dynamical mechanism.

**Step 1.2 — Literal old companion map.**
The original old M08 code defines
$$
C(A)=\begin{pmatrix}0&-\det A\\1&\operatorname{tr}A\end{pmatrix},
\qquad A\in\operatorname{Mat}_2(\mathbb F_q).
$$
Take $\pi(A)=(\operatorname{tr}A,\det A)$ and
$$
s(\tau,\delta)=\begin{pmatrix}0&-\delta\\1&\tau\end{pmatrix}.
$$
Its trace and determinant are $\tau,\delta$, so $\pi s$ is the identity.
Every one of the $q^2$ companion matrices is fixed and all other states
have depth one. Since $q^4>q^2$ for $q\geq2$, maximum depth is exactly one.

**Step 1.3 — Every target fibre and the maximum.**
For $(\tau,\delta)\in\mathbb F_q^2$, define
$$
N(\tau,\delta)=\#\{a\in\mathbb F_q:a^2-\tau a+\delta=0\}.
$$
A matrix of trace $\tau$ has unique form
$$
A=\begin{pmatrix}a&b\\c&\tau-a\end{pmatrix}.
$$
Its determinant is $\delta$ if and only if $bc=a(\tau-a)-\delta$.
If the right side is nonzero, there are $q-1$ choices: choose any nonzero
$b$ and then determine $c$. If it is zero, the $q$ pairs with $b=0$ and
the $q-1$ pairs with $b\ne0,c=0$ give $2q-1$ solutions. Precisely
$N(\tau,\delta)$ values of $a$ give the zero case. Therefore
$$
|C^{-1}(s(\tau,\delta))|
=N(\tau,\delta)(2q-1)+(q-N(\tau,\delta))(q-1)
=q(q-1+N(\tau,\delta)).
$$
Every noncompanion target has empty fibre.

A monic quadratic has at most two roots over a field. Distinct field
elements $r,s$ exist even when $q=2$; choosing $\tau=r+s,\delta=rs$ gives
two distinct roots. Consequently
$$
\max_B|C^{-1}(B)|=q(q+1),
$$
attained exactly at companion targets whose characteristic polynomial
splits with distinct roots. Double-root, irreducible and characteristic
two cases are all included in the root-count formula. This is a deduction
for an exact old retraction, not a new candidate.

### 2. LR: an unclosed domain and unit fibres on closed restrictions

**Step 2.1 — Exact domain and factorization.**
Let
$$
D=\left\{
\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{GL}_2(F):a\ne0
\right\}.
$$
For $\Delta=ad-bc\ne0$, the unique normalized factorization is
$$
A=
\underbrace{\begin{pmatrix}1&0\\c/a&1\end{pmatrix}}_L
\underbrace{\begin{pmatrix}a&b\\0&\Delta/a\end{pmatrix}}_U.
$$
Multiplication verifies it; matching entries forces these factors, proving
uniqueness. The standard LR step is
$$
T(A)=UL=
\begin{pmatrix}a+bc/a&b\\\Delta c/a^2&\Delta/a\end{pmatrix}.
$$
This is exactly the normalized lower/upper factor swap in Rutishauser's
definition, actually read on printed pages 47–49.

**Step 2.2 — Failure of forward closure over every field.**
The matrix
$$
A_0=\begin{pmatrix}1&1\\-1&0\end{pmatrix}
$$
has determinant one and belongs to $D$. Substitution yields
$$
T(A_0)=\begin{pmatrix}0&1\\-1&1\end{pmatrix}.
$$
The target is invertible but has zero upper-left entry, so it does not
belong to $D$. This remains valid in characteristic two, where $-1=1$.
The standard formula is therefore not a self-map of $D$.

**Step 2.3 — Exact inverse on the opposite domain.**
Define
$$
E=\left\{
\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}
\in\operatorname{GL}_2(F):\delta\ne0
\right\}.
$$
Step 2.1 maps into $E$. Every $B\in E$ has unique factorization
$$
B=
\begin{pmatrix}\alpha-\beta\gamma/\delta&\beta\\0&\delta\end{pmatrix}
\begin{pmatrix}1&0\\\gamma/\delta&1\end{pmatrix}.
$$
Put $u=\alpha-\beta\gamma/\delta=\det(B)/\delta\ne0$.
Reversing these factors gives the unique preimage in $D$,
$$
T^{-1}(B)=
\begin{pmatrix}u&\beta\\\gamma u/\delta&\delta+\beta\gamma/\delta\end{pmatrix}.
$$
Thus $T:D\to E$ is a bijection, which is not a self-map statement.

For finite $S\subseteq D$ with $T(S)\subseteq S$, this inverse proves that
$T|_S$ is injective. Its image has $|S|$ elements, hence equals $S$.
Therefore it is a permutation: every state is periodic from time zero,
and every target has exactly one predecessor under every positive iterate.
No nontrivial inverse count remains on such a restriction.

**Step 2.4 — The two-by-two slice has an elementary clock.**
The formula preserves $b$, trace $\tau=a+d$ and determinant $\Delta$.
Trace and determinant conservation follow by substitution, or from
$T(A)=L^{-1}AL$.

If $b\ne0$, the fixed triple $(b,\tau,\Delta)$ reconstructs the other
coordinates from the pivot $a$:
$$
d=\tau-a,\qquad c=\frac{a(\tau-a)-\Delta}{b},
\qquad a'=\tau-\frac{\Delta}{a}.
$$
The projective extension is the Möbius transformation represented by
$\begin{pmatrix}\tau&-\Delta\\1&0\end{pmatrix}$, of nonzero
determinant $\Delta$. The actual matrix carrier still requires a nonzero
pivot; a projective extension is a different carrier.

If $b=0$, invertibility forces $a,d\ne0$. The step fixes $a,d$ and
multiplies $c$ by $d/a$. These two cases exhaust the slice. They do not
provide a new nonlinear time contribution after Möbius/scalar dynamics
and the unit-fibre inverse are deducted.

### 3. Toda: polynomial equations define a relation

**Step 3.1 — Literal equations.**
For $N\geq1$, a state is $(I_1,V_1,\ldots,I_N,V_N)\in F^{2N}$ with
indices modulo $N$. A successor $(J_1,W_1,\ldots,J_N,W_N)$ satisfies
$$
I_n+V_n=J_n+W_{n-1},
\qquad I_{n+1}V_n=J_nW_n
\quad(1\leq n\leq N).
$$
These are the primary paper's equations (1)–(2). Definition 1 specifies
this successor relation; it does not select one successor.

**Step 3.2 — One site.**
For $N=1$ the equations are $j+w=i+v$ and $jw=iv$.
Eliminating $w$ gives $(j-i)(j-v)=0$. A field has no zero divisors, so
$j=i$ or $j=v$. These give precisely $(j,w)=(i,v)$ and $(v,i)$, and both
satisfy the equations. An equal-coordinate state has one successor and
an unequal-coordinate state exactly two.

Every field has unequal-coordinate states on the full carrier.
On the nonzero carrier the same obstruction works for $q\geq3$.
For $q=2$ the one-site nonzero carrier has one state, so it is not used
as a branching example.

**Step 3.3 — Exact two-site zero-state count.**
For $N=2$ and initial state zero, the sum equations force
$$
(J_1,W_1,J_2,W_2)=(a,b,-b,-a)
$$
for unique $a,b\in F$. Both product equations reduce to $ab=0$.
Over $\mathbb F_q$, count the $q$ pairs with $a=0$, then the $q-1$ pairs
with $a\ne0,b=0$. Thus zero has exactly $2q-1$ distinct successors,
greater than one for every $q\geq2$. At $q=2$ these are precisely the
three arrows in the primary source's Example 1.

**Step 3.4 — Cyclic quotienting does not restore single-valuedness.**
The source's trivial evolution is the cyclic shift
$$
\sigma(I_1,V_1,\ldots,I_N,V_N)
=(V_1,I_2,V_2,I_3,\ldots,V_N,I_1),
$$
with $\sigma^{2N}=\operatorname{id}$. Its quotient identifies powers
of this shift.

For $N=2$, Step 3.3 gives both zero and $(1,0,0,-1)$ as successors.
A cyclic coordinate shift fixes zero and preserves whether a vector is
nonzero. These successors are therefore in different quotient classes,
so even the zero quotient class has at least two successor classes.
This agrees with the source's graph formulation, not a contradiction
of its graph theorem.

The source already counts nonzero-state branching in Proposition 1.
Example 2 supplies distinct successors $(1,3,5,1)$ and $(6,4,4,3)$ of
$(3,6,4,4)$ modulo seven. These occupied relation results do not supply
an inverse axis for a newly defined deterministic map. ∎

## Corrections or Missing Assumptions

Standard LR needs a specified forward-closed carrier or an additional
boundary rule before it can be called a self-map. Toda needs an explicit
single-valued selection rule before it can be called a map. Neither repair
is silently made. General normal forms need not factor through a section;
Claim 1 applies only under the displayed section identity.

## Open Risks

No gap remains in the stated elementary exclusion certificates. They are
not a global novelty claim or a retained paper. Higher-dimensional
pivoted/refined factorizations, specially chosen Toda subsets and genuinely
new selectors remain outside this bounded desk. No experimental assertion
or unverified old census is used.
