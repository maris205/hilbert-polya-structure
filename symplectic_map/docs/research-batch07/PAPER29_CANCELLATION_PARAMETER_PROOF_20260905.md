# Parameter proof: arbitrary first cancellation times

Date: 2026-09-05. Author-side bounded proof for a new Paper29 candidate.
This is not a candidate PASS, publication lock, or independent review.
It does not modify the rejected first-integral candidate.

## Claim

For each integer $L\ge3$, there is a nonzero algebraic complex number $c$
such that the rational map
$$
R_c:\mathbb P^1\longrightarrow\mathbb P^1,\qquad
R_c(z)=1+\frac{c}{z^4}
$$
has the exact critical cycle
$$
0\longmapsto\infty\longmapsto1\longmapsto\cdots\longmapsto0
$$
of length $L$. Equivalently, the orbit starting at $1$ first reaches $0$
after $m=L-2$ steps.

More precisely, define polynomials in $\mathbb Z[c]$ by
$$
A_0=1,\qquad A_1=1+c,\qquad
A_{j+1}=A_j^4+cA_{j-1}^{16}\quad(j\ge1).
$$
Let $E_L$ be the set of parameters with the exact cycle length $L$, and
let $w_L$ be the sum of their root multiplicities in $A_{L-2}$.
Then every $E_L$ is finite and nonempty,
$$
4^{L-3}=\sum_{d\mid L,\ d\ge3}w_d,
\qquad
w_L=\sum_{d\mid L,\ d\ge3}\mu(L/d)4^{d-3}>0.
$$
Here $\mu$ is the ordinary number-theoretic Möbius function. These formulas
count multiplicities, not distinct parameters. No root-simplicity or
transversality statement is asserted or needed.

## Status and assumptions

**Author status: PROVABLE AS STATED. Independent check: requested.**

All parameters and orbits are complex; $c=0$ is excluded because it makes
the rational map degenerate. The proof uses only explicit iteration,
factorization over $\mathbb C$, and convergent local rational expansions.
It does not use numerical root finding, a generic-parameter assertion,
hyperbolic-component theory, or a transversality theorem.

This scalar rational map is an auxiliary coefficient system of the
four-dimensional polynomial symplectomorphism
$$
P=p+x^3+2xy,\quad Z=z+x^2,\quad
X=x+P^2,\quad Y=y+\delta Z^6,
\qquad c=2\delta.
$$
No scalar-system claim substitutes for the separate multivariate degree
proof. The scalar coordinate is $u=1+2r$ when the leading coefficient
ratio satisfies $r\mapsto\delta/(1+2r)^4$, with $r_0=0$ and $r_1=\delta$.

## Dependency map

1. Explicit numerator recursion and its degrees.
2. Exact return-time classification for a root parameter.
3. Constant root multiplicity at all repeated returns, proved locally.
4. Degree counting and the strict proper-divisor bound.
5. Conversion back to the coefficient ratio and its first hitting time.

## Proof

### 1. Reduced iterate numerators

For every $j\ge1$,
$$
R_c^j(1)=\frac{A_j(c)}{A_{j-1}(c)^4}
$$
as a rational function of the parameter. For $j=1$, this is $1+c$.
Substituting the fraction into $1+c/z^4$ proves the recursion and the next
identity inductively.

The recursion gives $A_j(0)=1$ for all $j$. Consecutive polynomials have
no common root: if $A_j(c_*)=A_{j-1}(c_*)=0$, then $c_*\ne0$ and the
recursion forces $A_{j-2}(c_*)=0$. Repeating reaches $A_0=1$, a
contradiction. Thus the displayed fractions are reduced over $\mathbb C[c]$.

For $j=1$, $A_1$ is monic of degree $1$. At the step producing $A_2$,
the two summands have degrees $4$ and $1$. At each later step, if
$\deg A_j=4^{j-1}$ and $\deg A_{j-1}=4^{j-2}$, their degrees are
$$
4\deg A_j=4^j,\qquad
1+16\deg A_{j-1}=1+4^j.
$$
**This computation refutes the tentative degree formula
$\deg A_j=4^{j-1}$ beyond $j=2$.** The second summand has larger degree
at that step. The correct degree sequence must be used below; the
preliminary claim and counting formula above are not yet justified as
written.

## Corrections or missing assumptions

The author has found an indexing/growth error while writing the full proof.
The claimed exact degree and Möbius-count formulas need replacement.
The iterate identities, consecutive coprimality and $A_j(0)=1$ survive.
No file created here constitutes a completed proof of the headline claim.

## Open risks and next action

**Current corrected status: NOT CURRENTLY JUSTIFIED AS WRITTEN.**
Derive the correct max recurrence
$a_{j+1}=\max(4a_j,1+16a_{j-1})$, checking for ties; then finish the
return-multiplicity proof and verify a strict proper-divisor bound with
those actual degrees. Preserve this failed draft and save a clearly named
successor rather than silently retaining its false formula.
