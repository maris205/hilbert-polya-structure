# Parameter proof V2: every first cancellation time occurs

Date: 2026-09-05. Author-side proof for the fixed-four-dimensional
coefficient-cancellation candidate. Not a candidate PASS, scientific lock,
publication lock, or independent review.

This version corrects the false numerator-degree estimate detected during
the full derivation in
[the retained first draft](PAPER29_CANCELLATION_PARAMETER_PROOF_20260905.md).
The map, first-hit problem and iteration polynomials are unchanged.

## Claim

For each integer $L\ge3$, there is a nonzero algebraic complex parameter $c$
such that
$$
R_c(z)=1+\frac{c}{z^4},\qquad z\in\mathbb P^1,
$$
has the exact cycle
$$
0\longmapsto\infty\longmapsto1\longmapsto\cdots\longmapsto0
$$
of length $L$. Equivalently, the orbit starting at $1$ first reaches $0$
at time $m=L-2$.

Define the polynomials
$$
A_0=1,\quad A_1=1+c,\quad
A_{j+1}=A_j^4+cA_{j-1}^{16}\quad(j\ge1).
$$
Their exact degrees are
$$
a_j=\deg A_j=\left\lfloor\frac{4^{j+1}}{15}\right\rfloor
=\begin{cases}
(4^{j+1}-1)/15,&j\text{ odd},\\
(4^{j+1}-4)/15,&j\text{ even}.
\end{cases}
$$
The even formula includes $j=0$.

Let $E_L$ be the finite set of parameters with the exact cycle length $L$,
and put
$$
w_L=\sum_{c_*\in E_L}\operatorname{ord}_{c_*}A_{L-2},\qquad
b_L=a_{L-2}=\left\lfloor\frac{4^{L-1}}{15}\right\rfloor.
$$
Then
$$
b_L=\sum_{d\mid L,\ d\ge3}w_d,\qquad
w_L=\sum_{d\mid L,\ d\ge3}\mu(L/d)b_d>0.
$$
The symbol $\mu$ denotes the number-theoretic Möbius function. The numbers
$w_L$ count multiplicities, not distinct parameters. Root simplicity,
irreducibility, Galois groups and transversality are not claimed.

## Status

**Author status: PROVABLE AS STATED. Independent check: requested.**

## Assumptions and notation

All orbits and local expansions are over $\mathbb C$. The parameter $c=0$
is excluded because the rational map degenerates there. Every root used in
the proof is algebraic, since it is a root of a nonzero integer polynomial.
An order of vanishing is the positive integer exponent of the first
nonzero term in the local parameter $c-c_*$.

The relation to the four-dimensional Hamiltonian map is
$$
P=p+x^3+2xy,\quad Z=z+x^2,\quad
X=x+P^2,\quad Y=y+\delta Z^6,\qquad c=2\delta.
$$
The auxiliary ratio iteration $r\mapsto\delta/(1+2r)^4$ is conjugate to
$R_c$ by $u=1+2r$. Its starting values are $r_0=0$, $u_0=1$.
Thus a first scalar hit at $r_m=-1/2$ is exactly the first $R_c$ hit at
$u_m=0$. This relation does not itself prove the multivariate degree
recursion; that is a separate dependency.

## Strategy and dependency map

1. Compute reduced iterate numerators, including the alternating degree
   comparison which the first draft missed.
2. Classify the subsequent zeros at any first-hit parameter by its exact
   cycle length.
3. Prove that the same root has the same multiplicity at every later
   return, without assuming a transverse critical relation.
4. Count roots with multiplicity and show that proper shorter periods
   cannot account for all roots of any $A_{L-2}$.

## Proof

### 1. Reduced fractions and exact degrees

Induction by substitution gives, for $j\ge1$,
$$
R_c^j(1)=\frac{A_j(c)}{A_{j-1}(c)^4}
$$
as a rational function of $c$. The recursion also gives $A_j(0)=1$.
If two consecutive polynomials had a common root $c_*$, this root would
be nonzero, and
$$
A_j(c_*)=A_{j-1}(c_*)=0
\quad\Longrightarrow\quad A_{j-2}(c_*)=0.
$$
Descending reaches $A_0=1$, a contradiction. Hence each displayed fraction
is reduced, and numerator zeros genuinely correspond to the value $0$,
not an indeterminate ratio.

Each $A_j$ is monic. The degrees at the start are $a_0=0$, $a_1=1$.
To prove the stated formula, compare the degrees of the summands of
$A_{j+1}$ using the inductive formulas. If $j$ is odd, then
$$
4a_j=\frac{4^{j+2}-4}{15},\qquad
1+16a_{j-1}=\frac{4^{j+2}-49}{15}.
$$
The first exceeds the second by $3$ and gives the asserted even formula
for $a_{j+1}$. If $j$ is even and positive, then
$$
4a_j=\frac{4^{j+2}-16}{15},\qquad
1+16a_{j-1}=\frac{4^{j+2}-1}{15}.
$$
The second exceeds the first by $1$ and gives the asserted odd formula.
There is no tie and therefore no leading-coefficient cancellation. The
dominant summand is monic in each case. This proves the degree formula and
monicity for every index.

In particular,
$$
a_1,a_2,a_3,a_4,a_5=1,4,17,68,273.
$$
These values replace the incorrect geometric sequence in the first draft.

### 2. Exact periods at root parameters

Fix any root $c_*$ of any $A_j$, and let $m_0\ge1$ be the first index
with $A_{m_0}(c_*)=0$. Before this time the orbit of $1$ stays finite and
nonzero: the only pole of $R_{c_*}$ is $0$, and reaching a pole would
require an earlier zero. At the first zero it continues as
$$
1\longmapsto\cdots\longmapsto0\longmapsto\infty\longmapsto1.
$$
Put $L_0=m_0+2$. This return to $1$ is its first return. Indeed, a return
to $1$ at a time $j\le m_0$ would make its orbit periodic with period
dividing $j$, so the first zero would occur before time $j$, contrary to
the choice of $m_0$. Time $m_0+1$ is $\infty$, not $1$.

Consequently $L_0$ is the exact period, and
$$
A_m(c_*)=0
\quad\Longleftrightarrow\quad
m=m_0+kL_0\ (k\ge0)
\quad\Longleftrightarrow\quad L_0\mid m+2.
$$
For the last equivalence one restricts to $m\ge1$. There are no cycles
of length $1$ or $2$ in this portrait because $0$, $\infty$ and $1$
are distinct.

### 3. Multiplicity is preserved at repeated returns

Fix the parameter $c_*$ and first time $m_0$ from Step 2. In a neighborhood
of $c_*$, define the holomorphic function
$$
u(c)=R_c^{m_0}(1).
$$
It is holomorphic there because its denominator
$A_{m_0-1}(c)^4$ is nonzero at $c_*$. Let $e\ge1$ be its order of
vanishing. The function is not identically zero since its numerator is a
nonzero polynomial.

An exact calculation near $z=0$ gives
$$
R_c^2(z)=1+\frac{c z^{16}}{(z^4+c)^4}
       =1+z^{16}v(c,z),\qquad v(c_*,0)=c_*^{-3}\ne0.
$$
The rational map $R_c^{m_0}$ is holomorphic near $(c_*,1)$ as a function
of both variables: along the relevant input orbit all intermediate points
before its last step are finite and nonzero. Therefore, for a holomorphic
function $B(c,z)$ near $(c_*,0)$,
$$
R_c^{L_0}(z)=u(c)+z^{16}B(c,z).
$$
This identity follows by substituting the displayed formula for $R_c^2$
into $R_c^{m_0}$. It is an actual local rational-function identity, not a
formal replacement of a pole by a finite number. In fact $B(c_*,0)\ne0$:
the derivative of $R_{c_*}^{m_0}$ at $1$ is a product of nonzero factors
$-4c_*/z^5$ along nonzero finite orbit points, and $v(c_*,0)\ne0$.
Only holomorphicity of $B$ is needed for the multiplicity argument.

Set $u_k(c)=R_c^{m_0+kL_0}(1)$. Since $u_0=u$, the local identity implies
$$
u_{k+1}(c)=u(c)+u_k(c)^{16}B(c,u_k(c)).
$$
Inductively $u_k$ has order $e$ and the same leading local coefficient as
$u$: the second summand has order at least $16e>e$. It cannot cancel
the first summand's leading term. Every $u_k$ is holomorphic after
shrinking the neighborhood, as is also evident from consecutive
coprimality at its return numerator.

At each return index $m=m_0+kL_0$, the factor $A_{m-1}(c_*)$ is nonzero.
Thus the order of $u_k$ equals the order of $A_m$ at $c_*$. All repeated
return numerators have exactly the same root multiplicity $e$.

### 4. Root count and existence at every exact period

Every root of $A_{L-2}$ belongs to exactly one set $E_d$ with $d\mid L$
and $d\ge3$, by Step 2. Step 3 shows that its multiplicity in this
polynomial is its multiplicity at its first return. Hence
$$
b_L=\deg A_{L-2}=\sum_{d\mid L,\ d\ge3}w_d.
$$
Extend the sequences by $b_1=b_2=w_1=w_2=0$. Finite divisor-sum
inversion gives the claimed Möbius formula. This inversion is an identity
of integer sequences, not a distinct-root count.

For $L=3,4,5$ there is no proper divisor at least $3$, so
$w_L=b_L=1,4,17$, respectively. For $L\ge6$, put $k=\lfloor L/2\rfloor$.
A proper divisor $d\ge3$ is at most $k$, and $0\le w_d\le b_d$.
The exact degree formula gives
$$
b_d\le 4^{d-2},\qquad b_L\ge4^{L-3}.
$$
The second inequality holds for $L\ge3$: writing $j=L-2\ge1$, the
formula for $a_j$ is at least $4^{j-1}$, with equality for $j=1,2$.
Therefore
$$
\sum_{d\mid L,\ 3\le d<L}w_d
\le\sum_{d=3}^{k}4^{d-2}
=\frac{4^{k-1}-4}{3}
<4^{L-3}\le b_L.
$$
Here $k\le L-2$ and the displayed geometric sum is strictly smaller than
$4^{L-3}$; all exponents are nonnegative in the range $L\ge6$.
It follows that $w_L>0$ for every $L$. Since positive total root
multiplicity requires at least one root, $E_L$ is nonempty.
Each $E_L$ is finite because it is a subset of the roots of $A_{L-2}$.
All these parameters are nonzero and algebraic by Step 1. This proves
the headline existence theorem. $\square$

### 5. Conversion to the Hamiltonian coefficient parameter

For $\delta=c/2\ne0$, conjugacy by $u=1+2r$ gives
$$
1+2\frac{\delta}{(1+2r)^4}=R_c(1+2r).
$$
Thus every $L\ge3$ supplies a parameter for which the ratio starting at
$r_0=0$ first hits $-1/2$ at time $L-2$. Up to that first time all
denominators in the finite ratio iteration are nonzero. The initial ratio
$r_1=\delta$ matches the first completed Hamiltonian step.

The exceptional parameter sets for different $L$ are disjoint, and their
union is a countable infinite set of algebraic numbers. Its complement in
$\mathbb C^*$ is uncountable. In a one-dimensional affine parameter space,
any infinite set is Zariski dense; this observation makes no Euclidean
density assertion.

## Corrections, attribution and open risks

- V2 preserves the exact original existence question and corrects only the
  auxiliary numerator-degree/count formulas. The first draft remains as
  evidence of the detected error; it must not be cited for those formulas.
- No simplicity assumption was added to rescue the counting argument.
  Multiplicity preservation is proved explicitly.
- This is a self-contained author proof of an auxiliary existence result.
  Bicritical rational maps and critical-relation polynomials are established
  subjects; their use here is not a claim of a new general theory.
- A separate independent reader must still verify this document and the
  multivariate cancellation/restart proof. Neither numerical diagnostics nor
  this scalar theorem establishes a candidate-value or publication PASS.
- No assertion is made that every period has a real or rational parameter.
  The required realization here is over algebraic complex coefficients.
