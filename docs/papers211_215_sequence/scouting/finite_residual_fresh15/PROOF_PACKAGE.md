# Proof Package — old-mechanism subtraction controls

## Claim

The three elementary control statements below hold under their stated
assumptions. They diagnose already-occupied mechanisms; they are not new
literal candidates, a fresh entrance ledger, or a two-axis paper proposal.

A. Let $B_n$ be the algebra of upper triangular $n$ by $n$ matrices over
$\mathbb F_2$, with $n\geq1$, and let $J_n$ be its strictly upper triangular
ideal. Put $\phi(X)=X+X^2$. Then $\phi(B_n)=J_n$, its restriction to $J_n$ is
bijective, every point outside $J_n$ has transient depth exactly one, and for
every $Y\in J_n$ its full fibre is in bijection with the idempotents of
$B_n$ commuting with $Y$.

B. For any finite group $G$, the already-screened product-exchange update
$F(a,b)=(ab,ba)$ has fibre over $(u,v)\in G^2$ of size $|C_G(u)|$ when
$u$ and $v$ are conjugate, and zero otherwise. Its largest fibre has size
$|G|$, attained exactly at central diagonal targets.

C. Let $S$ be a finite set, $f:S\to S$, and $N\geq0$. On the finite set of
nonnegative integer multiplicity vectors of total $N$, let $T=f_*$ be
ordinary pushforward. Its iterates, full-target fibres and transient depths
are inherited from $f$ by the formulas proved below. This control applies to
unconstrained multisets, not automatically to Frobenius-invariant multisets.

## Status

PROVABLE AS STATED for A, B and C. No original new-candidate theorem is
being promoted or repaired. A separate all-target inverse theorem for
non-split finite-field polynomial root powers is NOT CURRENTLY JUSTIFIED
by this packet.

## Assumptions

- A uses upper triangular matrices over exactly $\mathbb F_2$, not the full
  matrix algebra over arbitrary fields. No global additivity of $\phi$ is
  assumed.
- B assumes every factor is invertible because its carrier is a group.
  It does not extend the fibre formula to the full matrix or transformation
  semigroup.
- C uses nonnegative multiplicities and a finite autonomous base map.
  Its fibre choices have no additional equivariance or orbit constraints.

## Notation

$C_G(u)=\{c\in G:cu=uc\}$. For A choose any integer $r\geq1$ with
$2^r\geq n$ and put $g(Y)=\sum_{j=0}^{r-1}Y^{2^j}$ for $Y\in J_n$.
For C write
$$
X_N(S)=\{\mu:S\to\mathbb Z_{\geq0}:\ \sum_{s\in S}\mu(s)=N\},
\qquad
(T\mu)(y)=\sum_{f(s)=y}\mu(s).
$$
Let $C\subseteq S$ be the periodic points of $f$ and let $h(s)$ be the least
$t\geq0$ with $f^t(s)\in C$. Empty support has maximum depth zero. For
$t\geq0$ let $r_t(y)=|\{s\in S:f^t(s)=y\}|$, and set
$$
W(m,r)=
\begin{cases}
\binom{m+r-1}{r-1},&r\geq1,\\
1,&r=0,\ m=0,\\
0,&r=0,\ m>0.
\end{cases}
$$

## Proof Strategy

Direct algebra for A, a conjugacy transporter for B, and disjoint
multiplicity allocation plus finite support transport for C. These strategies
are precisely the subtraction burden; an elementary restatement does not
supply independent paper credit.

## Dependency Map

1. A uses nilpotence of strictly upper triangular matrices and commutativity
   among powers of a single matrix.
2. The fibre assertion in A additionally uses the fact that a solution $X$
   commutes with its polynomial $Y=\phi(X)$.
3. B uses only cancellation and conjugation in a finite group.
4. C uses induction for iterates, a balls-and-separators bijection for weak
   compositions, and permutation dynamics on finite invariant support.

## Proof

### Step 1. Triangular image and inverse

The diagonal entry of $X^2$ equals the square of the corresponding diagonal
entry of $X$. Since $a^2+a=0$ for $a\in\mathbb F_2$, $\phi(B_n)\subseteq J_n$.
Every $Y\in J_n$ has $Y^n=0$, so $Y^{2^r}=0$. Powers of this one $Y$ commute;
successive squaring in characteristic two and telescoping therefore give
$$
g(Y)^2+g(Y)=Y+Y^{2^r}=Y.
$$
For $N_0\in J_n$, the powers of $N_0$ also commute, and
$$
g(N_0+N_0^2)=
\sum_{j=0}^{r-1}(N_0^{2^j}+N_0^{2^{j+1}})
=N_0.
$$
Thus $g$ and $\phi|_{J_n}$ are two-sided inverses and the image is all $J_n$.
A permutation of the finite set $J_n$ makes every point there periodic.
A point outside $J_n$ enters $J_n$ in one step and cannot be periodic,
because all its positive iterates lie in $J_n$. Its depth is exactly one.

### Step 2. Exact, but unevaluated, target parametrization

Fix $Y\in J_n$. If $\phi(X)=Y$, then $XY=YX$, because $Y$ is a polynomial
in $X$. Consequently $X$ commutes with $g(Y)$. The matrix
$E=X+g(Y)$ satisfies
$$
E^2+E=(X^2+X)+(g(Y)^2+g(Y))=Y+Y=0,
$$
so $E^2=E$, and $E$ commutes with $Y$. Conversely, if $E^2=E$ and
$EY=YE$, then $E$ commutes with $g(Y)$, and the identical calculation shows
$\phi(E+g(Y))=Y$. These translations are inverse bijections.

This is not an evaluated all-target count of such idempotents. It also
does not permit replacing $\phi$ by a globally additive operator: for
$n=2$, $A=E_{11}$ and $B=E_{12}$ have
$\phi(A)=0$, $\phi(B)=B$, but $\phi(A+B)=0$.
For $n=1$, $J_1=\{0\}$ and both scalar matrices are idempotent; the same
argument covers this boundary.

### Step 3. Product exchange reduces to a conjugacy transporter

If $ab=u$, then $b=a^{-1}u$ and
$ba=a^{-1}ua$. Thus $F(a,b)=(u,v)$ is equivalent to
$a^{-1}ua=v$ together with the uniquely forced $b=a^{-1}u$.
There are no solutions unless $u,v$ are conjugate. If $a_0$ is one
solution, every $c a_0$ with $c\in C_G(u)$ is a solution. Conversely any
solution $a$ has $a a_0^{-1}\in C_G(u)$, since
$u a=a v$ and $v a_0^{-1}=a_0^{-1}u$.
The transporter therefore has exactly $|C_G(u)|$ elements.

This count is at most $|G|$. Equality holds exactly when
$C_G(u)=G$, that is, $u$ is central. A conjugate of a central element is
itself, so equality targets are precisely $(u,u)$ with $u\in Z(G)$.
The identity provides one such target even for the trivial group. This
proves no all-group recurrent classification and no noninvertible-semigroup
fibre theorem.

### Step 4. Multiset iterates and full-target fibres

For all $t\geq0$, induction on $t$ and grouping the finite sums give
$$
(T^t\mu)(y)=\sum_{f^t(s)=y}\mu(s).
$$
Fix a target $\nu\in X_N(S)$. Its preimages are the multiplicity choices
over the pairwise disjoint sets $(f^t)^{-1}(y)$, each of whose sum must be
$\nu(y)$. For a set of size $r\geq1$ and total $m$, ordering its elements
identifies these choices with strings of $m$ balls and $r-1$ separators;
the separator positions give $\binom{m+r-1}{r-1}$ choices. An empty set
admits exactly one total-zero allocation and no positive-total allocation.
The constraints automatically sum to total $N$, so
$$
|(T^t)^{-1}(\nu)|=\prod_{y\in S}W(\nu(y),r_t(y)).
$$
In particular the zero-size preimage cases are not discarded.

### Step 5. Multiset recurrence and exact depth

If $T^p\mu=\mu$ for $p\geq1$, positivity of multiplicities implies
$f^p(A)=A$ for $A=\operatorname{supp}\mu$. The restriction of $f^p$ to
this finite set is surjective, hence a permutation. Each $s\in A$ therefore
satisfies $f^{p k}(s)=s$ for some positive $k$, proving $A\subseteq C$.
Conversely $f$ permutes $C$, and a power of this finite permutation is the
identity. Every multiset supported on $C$ is periodic under $T$.

The support of $T^t\mu$ is exactly $f^t(A)$, again by nonnegativity.
For each $s$, membership $f^t(s)\in C$ is equivalent to $t\geq h(s)$.
It follows that the transient depth of $\mu$ is
$$
\max_{s\in\operatorname{supp}\mu}h(s).
$$
When $N=0$, the zero multiplicity vector is fixed and has fibre one at
every time. If $S$ is empty and $N>0$, $X_N(S)$ is empty and all
pointwise claims are vacuous. These observations cover the degenerate cases.
This completes A, B and C. $\square$

## Corrections or Missing Assumptions

The old labelled-word histogram formula in NCC_PROOF_BOUNDARY.md is not
literally the unlabelled multiset formula in C. The common subtraction is
pushforward allocation, while the displayed counting factors differ.

A degree-bounded polynomial over $\mathbb F_q$ is encoded by a
Frobenius-invariant root multiset in a finite splitting extension.
Applying C on all multisets in that extension and ignoring invariance
overcounts polynomial preimages in general. This packet has not evaluated
the corresponding constrained full-target fibres, their extremizers, or
a separate all-parameter two-axis residual. No theorem about all non-split
polynomials is inferred from the split or scalar source statements.

## Open Risks

The proofs are author deductions, not independently reviewed new research.
A is the literal old UTAS control and B is the elementary group restriction
of an already-screened product-exchange mechanism. C is generic transport
bookkeeping. Their validity does not establish novelty, source priority,
or eligibility for either open seat. No finite scientific replay was run.
