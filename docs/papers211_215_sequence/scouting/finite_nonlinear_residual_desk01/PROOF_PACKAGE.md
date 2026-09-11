# Proof package: old nonlinear mechanisms and exact limits

## Claim and status

The intended research target is a finite autonomous deterministic literal with
a full-parameter temporal/recurrent theorem and a materially separate
inverse/enumeration/extremal theorem after internal and direct-source
subtraction. Status: **NOT CURRENTLY JUSTIFIED** in this bounded desk.

The propositions below are **PROVABLE AS STATED**, but reproduce old literals
and elementary mechanisms. They are not new nominations. The deductions are
written by /root/round211_rational_scout; no finite search supports an induction.

## Assumptions, notation and dependencies

Fields are finite. In Proposition 1 the cardinality is an odd prime power
$q$; in Proposition 2 it is an odd prime $p$. The quadratic character is
$\chi:\mathbb F_p\to\{-1,0,1\}$, with $\chi(0)=0$. Proposition 3 uses the
coordinate dot and cross products on $\mathbb F_q^3$, with $q$ odd.

The proof dependencies are: root factorization and unordered-pair counting;
the directed cycle structure of a nearest-neighbor map with a fixed zero;
and elementary rank-two cross-product linear algebra plus the Lagrange
identity. No source's unproved general functional-graph assertion is needed.

## 1. Both two-coordinate Viète orders are already old

Old C8 is $V(a,b)=(a+b,ab)$; old ESP is $W(a,b)=(ab,a+b)$.
C8 and old cubic C9 occur in the actual P122 algebraic ledger. ESP occurs in
the actual P152 algebraic-replacement original.

### Proposition 1: exact common inverse mechanism

For target $(s,t)$ of $V$, the sources are the ordered roots of
$X^2-sX+t$. Consequently
$$|V^{-1}(s,t)|=1+\chi_q(s^2-4t),$$
where $\chi_q$ is the quadratic character of $\mathbb F_q$, extended by zero.
There are $q$ targets with one source, $q(q-1)/2$ with two sources, and
$q(q-1)/2$ with no source. Thus the image has $q(q+1)/2$ elements.
For $W$, exchange the two target coordinates in these statements.

**Proof.** The equations $a+b=s$, $ab=t$ are equivalent to
$(X-a)(X-b)=X^2-sX+t$. A nonzero-square discriminant gives two distinct
field roots and the two orders; zero discriminant gives one repeated root;
a nonsquare discriminant gives no roots in the field. Each unordered pair
with repetition determines exactly one polynomial, and polynomial
factorization determines that pair uniquely. There are $q$ repeated pairs
and $\binom q2=q(q-1)/2$ distinct pairs. Their polynomials exhaust the
image. Subtracting their number from the $q^2$ targets counts the empty
fibres. The assertion for $W$ follows by exchanging only its output
coordinates. ∎

An invertible change of output coordinates transfers fibres; this does
**not** establish conjugacy of the two autonomous dynamics. Both updates
are independently present in old originals. No all-$q$ temporal theorem is
deduced from this discriminant calculation, and no new higher-dimensional
Viète map is instantiated here.

## 2. Old QCD: a nearest-neighbor run mechanism

The old literal is $Q(x)=x+\chi(x)$ on $\mathbb F_p$.

### Proposition 2: recurrent shape and exact elementary inverse

Zero is fixed. Every other recurrent orbit is a two-cycle
$a\leftrightarrow a+1$ with $\chi(a)=1$, $\chi(a+1)=-1$.
For any target $y$, its sources are exactly
$$\{y-1:\chi(y-1)=1\}\ \cup\
  \{y+1:\chi(y+1)=-1\}\ \cup\
  \bigl(\{0\}\ \text{if }y=0\bigr).$$
Each fibre has at most two elements.

**Proof.** Nonzero states move one step clockwise or anticlockwise on the
$p$-cycle. A directed periodic orbit of length greater than two would give
a simple undirected cycle in that $p$-cycle; the only such cycle uses every
vertex, including zero. This is impossible because zero is fixed. A
nonzero fixed point would require $\chi(x)=0$, also impossible. Thus a
nonzero periodic orbit is an adjacent two-cycle, and its two arrow
conditions are exactly the displayed character signs. Every orbit
eventually becomes periodic by finiteness.

For the inverse formula, a positive-character source must be $y-1$, a
negative-character source must be $y+1$, and the only zero-character
source is zero. These are exhaustive alternatives from the literal.
For nonzero $y$ only the first two apply. For $y=0$, the second alternative
would require $\chi(1)=-1$, whereas $\chi(1)=1$. Hence there are at most
two sources also at zero. ∎

Before reaching zero or the two-cycle, successive steps follow a constant-
sign character run. A switch of direction at adjacent nonzero states
creates that two-cycle. This identifies the old run-length dependence;
it is not an evaluated all-prime distribution or sharp all-prime maximum.
The old numerical rows were not reproduced or used as new evidence.

## 3. Old XPF: nondegenerate norm dynamics and a linear inverse

The old XPF literal is
$$R(u,v)=(v,u\times v),\qquad (u,v)\in(\mathbb F_q^3)^2.$$
It is not old XCF's different literal $(u\times v,v\times u)$, but XPF
itself is already explicitly defined in the P197 fifth-fresh original.

### Proposition 3: full one-step fibres and the actual norm factor

For target $(a,b)$,
$$|R^{-1}(a,b)|=
\begin{cases}
q^3,&a=b=0,\\
0,&a=0,\ b\ne0,\\
q,&a\ne0,\ a\cdot b=0,\\
0,&a\ne0,\ a\cdot b\ne0.
\end{cases}$$
The image has $1+(q^3-1)q^2$ elements; zero is the unique maximizing target.

The first image consists of orthogonal pairs. On an orthogonal pair, the
squared norms $\alpha=u\cdot u$, $\beta=v\cdot v$ evolve by
$$(\alpha,\beta)\longmapsto(\beta,\alpha\beta).$$

**Proof.** The first output forces $v=a$, so the remaining source equation
is $u\times a=b$. For $a=0$ the left side vanishes for all $q^3$ choices
of $u$. Suppose $a\ne0$. A cross product vanishes exactly when its two
vectors are linearly dependent: choose a nonzero coordinate of $a$ and
solve the corresponding two minor equations to express all coordinates
of $u$ as one common multiple of those of $a$. The kernel of
$u\mapsto u\times a$ is therefore the one-dimensional span of $a$.
Its image has dimension two by rank-nullity. Every image vector is
orthogonal to $a$. The linear functional $b\mapsto a\cdot b$ is nonzero
because some coordinate of $a$ is nonzero, so its kernel also has dimension
two. The image is exactly this kernel. Every consistent fibre is an affine
coset of the one-dimensional kernel, and hence has size $q$.
This argument includes nonzero isotropic $a$.

There are $q^3-1$ possible nonzero first coordinates, each allowing $q^2$
second coordinates, and one image target with zero first coordinate.
Since $q^3>q$, the unique maximal fibre is the zero target.

The identity $v\cdot(u\times v)=0$ gives orthogonality in the first image
and preserves it thereafter. Expanding the three coordinates of the cross
product gives
$$(u\times v)\cdot(u\times v)
 =(u\cdot u)(v\cdot v)-(u\cdot v)^2.$$
On orthogonal pairs this is $\alpha\beta$, proving the factor formula. ∎

The norm factor is the already-subtracted multiplicative Fibonacci
mechanism. Norm zero does not mean vector zero over a finite field, and a
factor formula is not automatically a conjugacy or a full-carrier cycle
classification. No all-parameter atlas of the remaining vector lift or
degenerate strata is claimed.

## 4. Source boundary and disposition

The exact QTS original and its actual owner-specialization argument were
read alongside the cited primary bodies. Their read extent, old $n=1$
display caveat and the broader source boundary are recorded in
SOURCES_AND_SUBTRACTION.md. That source work introduces no new literal.

The three propositions leave no new theorem contract: their maps are old,
and their formulas reproduce the exact standard inverse/run/norm engines.
They neither prohibit other nonlinear systems nor establish that a
remaining hard stratum can never yield new results. Zero scientific
execution, no cutoff extension, no admission, no paper-review claim.
