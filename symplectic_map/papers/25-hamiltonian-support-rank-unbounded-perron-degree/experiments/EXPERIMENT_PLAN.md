# Proof-Validation Plan

## Purpose and prohibition

This is a claim-to-lemma validation roadmap for a theorem-only project. The
word experiment refers only to adversarial symbolic proof checks. No code,
CAS, numerical evaluation, finite search, parameter sweep, GPU job, dataset,
or empirical certificate is authorized or needed. A finite example may
illustrate a proved formula later, but it cannot carry evidence for any
headline claim.

## Frozen target

For every integer $d\ge2$, the target family is

$$
V(q)=\prod_jq_j^2+\sum_iq_i^{a_i+1},\qquad
W(p)=\prod_jp_j^b,\qquad F=T_W\circ S_V,
$$

with parameter order and inequalities frozen in the final proposal. The
selected complete-step matrix is

$$
C=b\mathbf1a^{\mathsf T}-D.
$$

The roadmap validates the conjunction:

$$
\text{support-rank bound}
\Longrightarrow
\text{sharp Hamiltonian realization}
\Longrightarrow
\text{exact visible degrees}
\Longrightarrow
\text{irreducible Perron degree and scalar order }d.
$$

## Validation principles

1. Each obligation has a symbolic witness, a pass criterion, and a concrete
   falsifier.
2. A later obligation cannot repair a failed earlier dependency by changing
   parameters or notation.
3. Strict inequalities must remain strict at every stated boundary.
4. Matrix degree propagation is insufficient until polynomial carries and
   leading-form survival are proved.
5. Cayley--Hamilton is insufficient until scalar minimality is proved.
6. Literature positioning is not mathematical evidence and cannot rescue a
   proof failure.

## Work packages

### PV-01: support-row factorization

**Input.** Matrices
$A=-I_n+\mathsf P\mathsf Q$,
$B=-I_n+\mathsf R\mathsf S$, $C=BA$, and
$r=\operatorname{rank}\binom{\mathsf Q}{\mathsf S}$.

**Symbolic action.** Multiply $C-I_n$, factor it through a full row basis
$T_0$ of the stacked row space, and apply the rectangular Sylvester
determinant identity.

**Pass criterion.**

$$
\chi_C(t)=(t-1)^{n-r}
\det((t-1)I_r-T_0X)
$$

as a polynomial identity, including $t=1$. The reduced determinant is monic
of degree $r$, and the write-up says only that the unit multiplicity is at
least $n-r$.

**Fail criterion.** Any dimension mismatch, division by $t-1$ without a
polynomial-identity justification, or claim of exact unit multiplicity.

### PV-02: parameter quantifier audit

**Input.** Fixed $d\ge2$.

**Symbolic action.** Prove existence in the order

$$
d\to p,c\to(a_1<\cdots<a_d)\to b\to R.
$$

**Pass criterion.** Dirichlet supplies $p\equiv1\pmod d$; cyclicity supplies
$c$ of order $p-1$; one common sufficiently large multiple of $p$ produces
ordered positive lifts with $a_1+1>4d$; and one sufficiently large $b$ in
the fixed congruence class satisfies $b\ge2$, $R^2<2$, and all finitely many
visibility inequalities.

**Fail criterion.** The lifts depend on $b$, the residue class for $b$ is not
soluble, or different inequalities require incompatible choices of $b$.

### PV-03: literal Hamiltonian support audit

**Symbolic action.** Differentiate $V$ and $W$ and pull back the standard
symplectic form under both shears.

**Pass criterion.** The competing $V$-rows have weighted degrees
$a_i u_i$ and $2\sum_j u_j-u_i$; the unique $W$-row is
$b\mathbf1^{\mathsf T}-e_i^{\mathsf T}$; Hessian symmetry proves
symplecticity; and the matrices $D$, $bJ-I_d$, and $C$ arise from these
literal supports.

**Fail criterion.** A matrix row is inserted without a gradient monomial, a
derivative coefficient can vanish in the stated field, or a shear lacks a
polynomial inverse.

### PV-04: broad selector cone

**Input.**

$$
\mathcal K_{\rm ratio}(R)=
\{u>0:\max u_i\le R\min u_i\}.
$$

**Symbolic action.** Compare every pure spike against the product competitor.

**Pass criterion.** For $m=\min u_i$,

$$
a_i u_i\ge a_1m>(2dR-1)m
\ge2\sum_j u_j-u_i
$$

for every $i$, with the strict middle inequality derived from
$a_1+1>4d$ and $R<\sqrt2<2$.

**Fail criterion.** A selector tie occurs at the seed or a cone wall.

### PV-05: broad-cone invariance

**Symbolic action.** For $H=a^{\mathsf T}u$ and
$z_i=bH-a_i u_i$, bound the output coordinate ratio.

**Pass criterion.**

$$
\frac{\max z_i}{\min z_i}
\le\frac1{1-\frac{MR}{bS_a}}<R,
$$

where the last strict inequality is reduced exactly to $R^2<2$.

**Fail criterion.** A denominator is not proved positive, or the estimate
only gives a non-strict ratio $R$.

### PV-06: fine visibility chamber

**Input.**

$$
\mathcal K_{\rm vis}(R)=
\{u>0:u_i\le u_1<Ru_i,\ 
a_1u_1<a_i u_i\text{ for }i>1\}.
$$

**Symbolic action.** Verify seed membership, inclusion in the broad cone, and
all walls after applying $C$.

**Pass criterion.** For $w=Cu$,

$$
w_i<w_1<Rw_i,\qquad a_1w_1<a_iw_i
\quad(i>1),
$$

with the ratio wall using $R^2<2$ and the weighted wall using
$b(a_i-a_1)S_a>a_i^2R-a_1^2$.

**Fail criterion.** The coordinate-ratio and weighted inequalities are
conflated, or the seed is incorrectly required to satisfy $u_i<u_1$.

### PV-07: phase-labelled carry audit

**Symbolic action.** Track degrees at the input of $S_V$, after $S_V$, and
after $T_W$ for every iterate.

**Pass criterion.** Prove

$$
(Cu)_i>\max_j a_j u_j>u_i
$$

throughout the broad cone. At the first $V$-phase, $a_i>1$ beats the momentum
seed. At later $V$-phases, $D u_n>D u_{n-1}$. At every $W$-phase, $Cu_n$
beats both the carried position coordinate and every current momentum
coordinate.

**Fail criterion.** Any old coordinate is omitted from the comparison, or an
inequality is only componentwise where a global block comparison is needed.

### PV-08: leading-form survival

**Symbolic action.** Induct in
$\mathbb Z_{\ge0}[q_1,\ldots,q_d,p_1,\ldots,p_d]$ before base change.

**Pass criterion.** Every coordinate iterate has nonnegative integer
coefficients; each selected source has a unique strictly larger degree than
its competitor and carry; powers and products of nonzero top forms remain
nonzero; and characteristic zero preserves every positive integer
coefficient.

**Fail criterion.** The proof invokes generic coefficients, assumes
noncancellation, or uses an ordered structure on the base field.

### PV-09: exact ordinary-degree visibility

**Symbolic action.** Combine PV-04 through PV-08 along
$u_0=\mathbf1$.

**Pass criterion.**

$$
u_n=C^n\mathbf1,\qquad
\deg(F^n)=e_1^{\mathsf T}u_n
$$

for all $n\ge0$, with $q_1$ uniquely maximal for $n\ge1$ and all degrees
equal to one at $n=0$.

**Fail criterion.** The conclusion is merely a tropical upper bound or the
visible coordinate changes with $n$.

### PV-10: characteristic coefficient audit

**Symbolic action.** Apply the rank-one determinant lemma and count each
$k$-fold product in the derivative sum.

**Pass criterion.**

$$
\chi_C(t)=
\prod_i(t+a_i)-b\sum_i a_i\prod_{j\ne i}(t+a_j)
=t^d+\sum_{k=1}^d(1-bk)e_k(a)t^{d-k}.
$$

The factor $k$ is justified combinatorially.

**Fail criterion.** A sign, factor $k$, or constant term is inferred from
examples rather than derived.

### PV-11: modular irreducibility and boundaries

**Symbolic action.** Reduce the elementary symmetric functions modulo $p$
and verify the finite-field binomial criterion.

**Pass criterion.**

$$
e_k(a)\equiv0\ (1\le k<d),\qquad
e_d(a)\equiv(-1)^{d+1},\qquad
\chi_C(t)\equiv t^d-c.
$$

Every prime divisor of $d$ divides $p-1=\operatorname{ord}(c)$, the quotient
$(p-1)/\operatorname{ord}(c)$ equals one, and $p\equiv1\pmod4$ whenever
$4\mid d$. For $d=2$, $p$ is odd and $c$ is a nonsquare. Monicity and
Gauss's lemma then lift irreducibility to $\mathbb Q$.

**Fail criterion.** The $4\mid d$ clause is omitted, primitive is weakened to
nonzero, or reduction loses degree.

### PV-12: Perron degree and dynamical degree

**Symbolic action.** Apply Perron--Frobenius to the strictly positive matrix
$C$ and combine it with PV-09 and PV-11.

**Pass criterion.** The Perron root is simple and strictly dominant, its
minimal polynomial is the irreducible $\chi_C$, its algebraic degree is
$d$, the visible Perron coefficient is positive, and

$$
\lim_{n\to\infty}\deg(F^n)^{1/n}=\rho(C).
$$

**Fail criterion.** Positivity is replaced by mere nonnegativity without a
primitivity check, or irreducibility is not connected to the minimal
polynomial of the Perron root.

### PV-13: exact scalar recurrence order

**Symbolic action.** Build reachability and observability matrices for
$(C,\mathbf1,e_1^{\mathsf T})$.

**Pass criterion.** Irreducibility makes every nonzero vector cyclic for
$C$ and every nonzero covector cyclic for $C^{\mathsf T}$. Hence both
matrices are invertible and

$$
\operatorname{rank}
\bigl(e_1^{\mathsf T}C^{i+j}\mathbf1\bigr)_{0\le i,j<d}=d.
$$

Cayley--Hamilton gives an order-$d$ recurrence, Hankel rank excludes every
smaller recurrence from $n=0$, and Perron asymptotics exclude every smaller
eventual recurrence.

**Fail criterion.** The argument stops at an order-at-most-$d$ matrix
recurrence.

### PV-14: rank sharpness

**Symbolic action.** Present
$D=-I_d+I_d(D+I_d)$ and
$bJ-I_d=-I_d+(b\mathbf1)\mathbf1^{\mathsf T}$.

**Pass criterion.** Since $D+I_d$ is invertible, the stacked support-row rank
is $d$; since $\chi_C$ is irreducible of degree $d\ge2$, the nonunit factor
has degree $d$. The upper bound is attained for every constructed
$r=d\ge2$.

**Fail criterion.** Sharpness is promoted to every presentation, exact unit
profile, rank zero or one, minimal dimension, or optimal sparsity.

### PV-15: novelty and anti-claim audit

**Symbolic action.** Compare the exact conjunction against local Papers
20--24 and the bounded primary-source landscape frozen in the candidate
review.

**Pass criterion.** The article subtracts the kernel lemma, fixed cubic and
quartic cases, isolated $d=5$, standard spectral tools, and general
weak-Perron realization context. It uses bounded noncollision wording and
contains every mandatory anti-claim.

**Fail criterion.** Any first, only, unprecedented, exhaustive, or absolute
priority statement appears.

## Dependency order

PV-01 is independent infrastructure. PV-02 and PV-03 feed PV-04 through
PV-08. PV-04, PV-05, PV-06, PV-07, and PV-08 jointly feed PV-09. PV-10 and
PV-11 feed PV-12 and PV-13. PV-01, PV-03, PV-11, and PV-14 establish
sharpness. PV-15 is a final scope gate and cannot alter a mathematical claim.

## Stop conditions

Stop the source-design lifecycle immediately if any of the following occurs:

- a selector, cone, carry, or visibility inequality cannot be made strict
  under the frozen parameter order;
- top-form survival needs a genericity or cancellation assumption;
- $t^d-c$ fails one condition of the exact binomial criterion;
- the scalar Hankel rank cannot be proved to be $d$;
- the sharpness statement requires exact unit multiplicity;
- a headline contribution reduces to a local fixed-dimensional predecessor;
- any validation would require code, CAS, numerical evidence, network use,
  or a new project object.

At this gate the response to a stop condition is a written blocker by a
separately authorized reviewer, not an unauthorized repair, run, or source
creation.
