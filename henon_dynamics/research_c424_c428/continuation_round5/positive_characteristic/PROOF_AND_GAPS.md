# PC424-D: exact gap after the R5 connectivity check

2026-09-08 UTC. Current-team author hand derivation. No mathematical
program was run; no complete-candidate review or admission is claimed.

## 1. Original claim and status

The [frozen original question](FROZEN_CONTRACTS.md) asks for all geometric
irreducible components of the reduced $\Phi_{p^e}(x,c)=0$ curve for every
odd $p$ and every $e\geq1$, on the full parameter plane with native
one-step map $f_c=x^2+c$.

**Original question: NOT CURRENTLY JUSTIFIED / UNCLOSED.** Neither
irreducibility of the entire tower nor its full alternative component
classification is proved or disproved here. The auxiliary statements
below are complete elementary checks, not a new all-tower answer.

## 2. Assumptions, notation and dependency map

Fix any odd $p$ and $e\geq1$. Write

$$
k=\overline{\mathbb F}_p,\quad n=p^e,\quad m=p^{e-1},
\quad \Psi_j=f_c^{\circ j}(x)-x,\quad
P=\overline{\Phi_n}\in k[c][x],\quad K=k(c).
$$

Here the bar denotes reduction of the integral dynatomic polynomial,
so $\Psi_n=P\Psi_m$ is an identity after reduction. The letter $K$
here is a function field, not the cocycle kernel from PC424-L.

The checks have the following dependency chain:

1. The explicit fibre at $c=0$ gives generic separability, no vertical
   component, and generic exact native period $n$.
2. Separable factorization over $K$ turns the unknown component count
   into a finite Galois-orbit problem, without computing that group.
3. The commuting native cyclic action separates orbit-level
   transitivity from an additional cyclic-stabilizer condition.
4. The source check does not establish those conditions for all
   $(p,e)$; their proof is the remaining global work.

No local calculation changes the fixed clock or the original quantifiers.

## 3. Complete auxiliary check: the same regular fibre for every pair

Set $q_j=2^j-1$ and $N=2^n-2^m$. Since $m\mid n$, $q_m\mid q_n$.
At $c=0$ the integral identity becomes

$$
P(x,0)=\frac{x^{q_n}-1}{x^{q_m}-1}.
\tag{1}
$$

In $\mathbb F_p$, repeated Frobenius gives
$2^{p^t}=2$ for every integer $t\geq0$. Consequently both $q_n$ and
$q_m$ equal $1$ modulo $p$. Each polynomial $x^{q_j}-1$ in (1) has
distinct nonzero roots, because its derivative at any root is
$q_jx^{q_j-1}\ne0$. Thus (1) is monic, has exactly $N$ distinct roots,
and its root set is precisely

$$
S=\mu_{q_n}(k)\setminus\mu_{q_m}(k).
\tag{2}
$$

Every point of $S$ has exact native period $n$ for $x\mapsto x^2$.
Indeed its period divides $n$; any proper divisor of the prime power
$n$ divides $m$, and such a point would belong to $\mu_{q_m}$.
Also, $0$ is a root of $\Psi_m(x,0)$ and is not a root of (1).
Therefore $P(x,0)$ and $\Psi_m(x,0)$ are coprime.

The discriminant of the monic $P$ has a nonzero value at $c=0$, so
$P\in K[x]$ is separable. The resultant with $\Psi_m$ likewise has
a nonzero value there; thus every generic root of $P$ has exact
period $n$. This does not exclude lower exact periods at other
special parameter values.

Because $P$ is monic in $x$, it has no nonconstant factor depending
only on $c$. A repeated irreducible factor in $k[c,x]$ would retain
positive $x$-degree and remain repeated in $K[x]$, contradicting
separability. Hence the full affine curve in the original contract
is already reduced and has no vertical components. Its irreducible
components correspond exactly to the irreducible factors in $K[x]$,
by Gauss's lemma. Factors may be chosen monic in $k[c][x]$, so each
component still meets the fibre (2); distinct components, if any,
have disjoint roots in that particular fibre.

There is a stronger local observation, with no global conclusion.
For each $a\in S$, solve $P(u(c),c)=0$ with $u(0)=a$ recursively in
$k[[c]]$. If coefficients through degree $r-1$ have been chosen,
the coefficient of $c^r$ has the form
$P_x(a,0)u_r+b_r$, where $b_r$ is already determined.
Since $P_x(a,0)\ne0$, there is exactly one choice of $u_r$.
The resulting $N$ roots have pairwise distinct constant terms and
factor the monic polynomial completely over $k[[c]]$.

Thus this geometric formal neighbourhood is completely split: its
local inertia supplies no nontrivial point permutation. It is an
excellent separability check, but not a transitivity proof. Connected
global covers may have completely split local neighbourhoods.

These elementary facts are consistent with the broader reducedness
and separability inputs in S1. They are not claimed as a new mechanism.

## 4. Complete auxiliary check: the exact cyclic-stabilizer deficit

Let $L/K$ be the splitting field of $P$, let $G=\operatorname{Gal}(L/K)$,
and let $\Omega\subset L$ be its $N$ roots. Define
$\sigma(\alpha)=f_c(\alpha)$ on $\Omega$. Section 3 shows that
$\sigma$ consists of cycles all of length $n$. For every $g\in G$,

$$
g\sigma(\alpha)=g(\alpha^2+c)=g(\alpha)^2+c=\sigma g(\alpha).
\tag{3}
$$

Let $\mathcal C=\Omega/\langle\sigma\rangle$ be the set of native
cycles. Decompose it into $G$-orbits
$\mathcal C_1,\ldots,\mathcal C_s$, of cardinalities $r_1,\ldots,r_s$.
Choose a cycle $O_j\in\mathcal C_j$ and a point $\alpha_j\in O_j$.
Its setwise stabilizer $G_{O_j}$ has a homomorphism

$$
\rho_j:G_{O_j}\longrightarrow\mathbb Z/n\mathbb Z,
\qquad g\alpha_j=\sigma^{\rho_j(g)}\alpha_j.
\tag{4}
$$

The exponent is unique since the period is exactly $n$; (3) proves
that (4) is additive under composition. Let $H_j$ be its image.
It is a subgroup of the cyclic group of order $p^e$, so there is a
unique $h_j\in\{0,\ldots,e\}$ with $|H_j|=p^{h_j}$.
Changing the point within $O_j$ leaves (4) unchanged. Transporting
to another cycle in $\mathcal C_j$ conjugates the stabilizer and
leaves its rotation image unchanged by (3).

The $G$-orbit of $\alpha_j$ meets $O_j$ in exactly the $|H_j|$ points
$\sigma^a\alpha_j$ with $a\in H_j$. For any cycle in $\mathcal C_j$,
choose an element transporting $O_j$ to that cycle; it gives a
bijection between the corresponding intersections. Consequently
every point-orbit over $\mathcal C_j$ has $r_j|H_j|$ elements.
There are $nr_j$ points in total over that cycle-orbit, whence
there are exactly $n/|H_j|$ such point-orbits.

For a separable polynomial, its irreducible factors correspond to
Galois orbits of its roots: conjugates of a root are precisely the
images of the root under embeddings of its simple extension, and
normality of $L/K$ extends those embeddings to $G$. Together with
Section 3, this proves the identity

$$
\#\operatorname{Irr}(P)=\sum_{j=1}^{s}p^{e-h_j}.
\tag{5}
$$

Above $\mathcal C_j$ each factor has $x$-degree $r_jp^{h_j}$.
In particular the whole curve is irreducible if and only if

$$
s=1\quad\hbox{and}\quad H_1=\mathbb Z/p^e\mathbb Z.
\tag{6}
$$

The second condition is equivalent to finding, in the stabilizer of
one native cycle, a Galois permutation rotating by an exponent not
divisible by $p$. A merely nonzero rotation is insufficient when
$e>1$: it may generate a proper subgroup.

Equation (5) is an exact *conditional description in unknown Galois
data*, not the requested classification. Neither the $G$-orbits
$\mathcal C_j$ nor the groups $H_j$ have been determined for all pairs.
The native map $\sigma$ is known to commute with $G$, but that does
not prove $\sigma\in G$. Confusing those statements would insert
the missing condition by assumption.

For clarity, the abstract finite étale algebra $K^n$ with its cyclic
permutation has one native cycle but trivial Galois action and $n$
components; its cyclic quotient is $K$. This is a counterexample to
the *general inference* from orbit-quotient transitivity to point
transitivity. It is not a counterexample for the polynomial $P$.

The orbit quotient used in this argument is defined intrinsically
over characteristic $p$. Applying an integral model of $Y_0$ to it
must respect the source's quotient/specialization hypotheses; no
averaging by $1/n$ is available here.

## 5. Where the attempted global proof actually stops

The nearest-source argument leaves two distinct obligations:

1. Determine enough surviving noncolliding inertia, or another
   global mechanism, to control the full native-cycle quotient for
   every $(p,e)$. A bound allowing two deleted edges does not itself
   identify the actual collision set throughout this tower.
2. Establish the missing point-level rotation/transitivity, or
   classify its exact failure, in characteristic dividing $n$.
   Even granting a transitive cycle quotient leaves $H_1$ in (6)
   undetermined. The cited tame lifting argument does not apply.

These obligations describe one possible proof route, not a theorem
that every solution must use this route. A different global component
argument could bypass them. The new abstract-level source leads do
not supply either obligation with the original quantifiers.

There is no theorem here that the full tower is impossible to classify,
no inferred global research-open status, and no assertion that a
singular point entails reducibility. The inaccessible thesis proofs
remain a source-access risk. No finite table or local germ is
substituted for the missing global argument.

## 6. Outcome

The original question survives unchanged and unclosed. The complete
auxiliary fibre and stabilizer checks make the remaining obligation
testable in a future proof, but are elementary reductions and do not
qualify as another complete research contract. Zero new mathematical
programs, no old reruns, and no formal evaluation were performed.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.

